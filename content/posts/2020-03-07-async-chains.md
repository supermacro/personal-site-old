Title: Chaining Failable Tasks
Tags: software
Summary: This post introduces the new chaining API for the "neverthrow" package and what problems it solves.
UUID: 30b03e60-ab82-4fb6-bc2e-2654d3fda6fa

*This post assumes familiarity with TypeScript.*

In my [previous post]({filename}2019-04-29-neverthrow.md), I introduced a [npm package](https://www.npmjs.com/package/neverthrow) to model failure at the type level.

If you're not familiar with `neverthrow`, here's a quick rundown (feel free to skip this tiny intro by [clicking here](#main-content)):

- The package introduces a functional alternative to throwing exceptions
    - By getting rid of `throw`ing exceptions, you make your error handling logic pure!
    - This is the standard approach in other languages, such as Rust, Elm and Haskell to name a few
- `neverthrow` has a `Result` type that represents either success (`Ok`) or failure (`Err`)

`Result` is defined as follows:

```typescript
type  Result<T, E>
  =  Ok<T, E>
  |  Err<T, E>
```

`Ok<T, E>`: contains the success value of type `T`

`Err<T, E>`: contains the failure value of type `E`

**Usage**:

Create `Ok` or `Err` instances with the `ok` and `err` functions.

```typescript
import { ok, err } from 'neverthrow'

// something awesome happend

const yesss = ok(someAwesomeValue)

// moments later ...

const mappedYes = yesss.map(doingSuperUsefulStuff)
```

You can access the value inside of `Err` and `Ok` instances as follows:

```typescript
if (myResult.isOk()) {
  // if I didn't first call `isOk`, I would get a compilation error
  myResult.value
}

// or accessing values
if (myResult.isErr()) {
  myResult.error
}
```

This quick rundown doesn't do the package justice, so I highly recommend you check out my [previous post]({filename}2019-04-29-neverthrow.md) that really walks you through the package.

---

A while back<span id="main-content">,</span> I got feedback ([link to github issue](https://github.com/gDelgado14/neverthrow/issues/2)) from two users that this module wasn't very ergonomic when it came to `Result`s wrapped inside of a promise.

This post is dedicated to covering the problem, and the solution to it.

### The Problem

Let's suppose we're working on a project that has 3 async functions:

- `getUserFromSessionId`
- `getCatsByUserId`
- `getCatFavoriteFoodsByCatIds`

And here are the type signatures for each of these functions:

```typescript
type GetUserFromSessionId = (sessionUUID: string) => Promise<Result<User, AppError>>
```

```typescript
type GetCatsByUserId = (userId: number) => Promise<Result<Cat[], AppError>>
```

```typescript
type GetCatFavoriteFoodsByCatIds = (catIds: number[]) => Promise<Result<Food[], AppError>>
```

Let's also assume that you're a developer tasked with leveraging these functions in order to *get all of the favorite foods of all of the cats owned by a single user*.

By taking a close look at the type signatures of these functions, we can start to see how we might go about implementing our task:

- First call `getUserFromSession`
- then get the `User` and use that value to call `getCatsByUserId`
- then get all of the cats (`Cat[]`) and call `getCatFavoriteFoodsByCatIds` by passing it an array of cat ids

The issue is that the values we need (`User`, `Cat[]` and `Food[]`) are wrapped inside of `Promise` and `Result`.

### First Attempt At A Solution

Let's see how we might implement this naively.

The `neverthrow` api has a `asyncMap` [method](https://github.com/gdelgado14/neverthrow#resultasyncmap-method) and `andThen` [method](https://github.com/gdelgado14/neverthrow#resultandthen-method) that we could use to solve this:

```typescript
// imagine we have a sessionId already

const result1 = await getUserFromSessionId(sessionId)

// result2 is a Result<Result<Cat[]>, AppError>, AppError>
const result2 = await result1.asyncMap((user) => getCatsByUserId(user.id))

// need to get the inner result using `andThen`
// now catListResult is Result<Cat[]>, AppError>
const catListResult = result2.andThen((innerResult) => innerResult)

// result3 is
// Result<Result<Food[], AppError>, AppError>
const result3 = await catListResult.asyncMap(
  (cats) => getCatFavoriteFoodsByCatIds(cats.map((cat) => cat.id))
)

// so now we need to unwrap the inner result again ...
// foodListResult is Result<Food[], AppError>
const foodListResult = result3.andThen((innerResult => innerResult))
```

Holy boilerplate! That was not fun. And super cumbersome! There was a lot of legwork required to continue this chain of async `Result` tasks.

... If there were only a better way!


### Using Result Chains! 🔗

Version 2.2.0 of `neverthrow` introduces a wayyy better approach to dealing with this issue.

This is what it would look like

```typescript
import { chain3 } from 'neverthrow'

// foodListResult is Result<Food[], AppError>
const foodListResult = chain3(
  getUserFromSessionId(sessionId),
  (user) => getCatsByUserId(user.id),
  (cats) => {
    const catIds = cats.map((cat) => cat.id)
    return getCatFavoriteFoodsByCatIds(catIds)
  }
)
```

That's it.

<iframe src="https://giphy.com/embed/3rg3vxFMGGymk" width="480" height="396" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Check out the API docs [here](https://github.com/gdelgado14/neverthrow#chaining-api).

Obviously the above example is quite contrived, but I promise you that this has very practical implications. As an example, here's a snippet from my own side project where I use the `chain3` function:

```typescript
chain3(
  validateAdmin(parsed.username, parsed.password),
  async (admin) => {
    const sessionResult = await session.createSession(admin)

    return sessionResult.map((sessionToken) => {
      return {
        sessionToken,
        admin
      }
    })
  },
  ({ sessionToken, admin }) => Promise.resolve(
    ok(AppData.init(
      removePassword(admin),
      sessionToken
    ))
  )
)
```

There are 8 different `chain` functions, each of which only vary in their arity (the number of arguments that the functions take). 

- `chain`: takes 2 async `Result` tasks
- `chain3`: takes 3 async `Result` tasks
- `chain4`: takes 4 async `Result` tasks
- `chain5`: etc
- `chain6`: etc
- `chain7`: etc
- `chain8`: etc

The beautiful thing about this `chain` API is that it retains the same properties as synchronous `Result.map` chains ... namely, these async chains short-circuit whenever something at the top of the chain results in a `Err` value 😍

A useful way to think of the `chain` api is to think of it as the asynchronous alternative to the `andThen` method.

---

I've had this issue noodling in my head for a while. Eventually in that same github issue I mentioned at the top of this post, [I proposed](https://github.com/gDelgado14/neverthrow/issues/2#issuecomment-551867175) an approach to chaining many async computations with a set of utility functions.

Before committing to that solution, I started dogfooding this approach through my own side project. After a few days of using this `chain` API, I concluded that it was in fact quite good and ergonomic.

This API is [heavily tested](https://github.com/gDelgado14/neverthrow/blob/master/tests/index.test.ts#L235) and [well-documented](https://github.com/gDelgado14/neverthrow/blob/master/README.md#chaining-api)!

Cheers!
