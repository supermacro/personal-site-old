Title: NeverThrow + Subtyping = ❤️
Tags: software
Summary: Or, "Why I deviated from the norm"
UUID: 925f3673-8389-44d2-8d72-37095ce3d80a

> This post is about the `neverthrow` TypeScript package, which is an implementation of `Result` / `Either`. If you've stumbled onto this post and haven't heard of these things, [here is a gentle introduction](https://gdelgado.ca/type-safe-error-handling-in-typescript.html#title) that doesn't assume anything about the reader other than knowledge of TypeScript.

---

When I first created [`neverthrow`](https://github.com/supermacro/neverthrow/), my goal was to adhere strictly to the interface defined by those languages that I had borrowed so heavily from - notably Haskell, Elm and Rust.

I figured that those who came before me had put quite a lot of thought into their design of a `Result` / `Either` type, so there couldn't possibly be a need to re-assess or re-think those designs while porting them over to TypeScript. And, for a while, things were fine and everyone was happy.

Then one day, a user opened [this interesting issue](https://github.com/supermacro/neverthrow/issues/30), "Why can't I return different error types in a `andThen` chain?".

### Context: What is `andThen` and how does it work in Rust and most other languages?

A `Result` can be mapped over with a function that itself may fail.

Suppose you are making a math engine that answers questions to life.

You first retrieve a mythical number from some unsafe IO operation (let's say from disk) ...

```typescript
getRandomValue(seed: Seed): Result<number, GeneratorError>
```


... and then you need to divide a constant by this value (don't you love contrived examples!?).

```typescript
import { ok, err } from 'neverthrow'

const safeDivide = (
  denominator: number
): Result<number, 'division_by_zero'> => {
  const ANSWER_TO_LIFE = 42

  return denominator === 0
    ? err('division_by_zero')
    : ok(ANSWER_TO_LIFE / denominator)
}
```

Well, if the value in question is 0, then this computation should fail (division by zero is undefined).

Putting it all together. This is where `andThen` (or in Rust; `and_then`, or in Elm; `|> andThen`) comes in:

```typescript
import { Result } from 'neverthrow'

const mathEngine = (seed: Seed) => {
  const value: Result<number, GeneratorError> = getRandomValue(seed)

  return value.andThen(safeDivide)
}
```

In practice, `andThen` is massively useful. I use it [a lot in my applications](https://github.com/parlez-vous/server/blob/5a17f2e1dfc7ba6e100df15ed5cebf5ef01ec9f8/src/routes/embed/get-comments.ts#L77).

Anyways, the astute reader may have noticed that the above example isn't actually valid.

`saveDivide` returns a `Result<number, 'division_by_zero'>` and `getRandomValue` returns a `Result<number, GeneratorError>`.

The signature of `andThen` is as follows (and this is true for basically all languages):

```typescript
// true in Haskell, Elm, Rust, etc ..
class Result<T, E> {
  andThen<A>(fn: (val: T) => Result<A, E>): Result<A, E>
}
```

Note that the `E` value is unchanged and is bound by the originating Result. So in the above example, we would get a compiler error that basically says that `'division_by_zero'` is not the same as `GeneratorError`.

So to fix the compiler error, you need to map the `Result<number, GeneratorError>` into a `Result<number, 'division_by_zero'>`. Or you could do more sophisticated wrangling in order to return something like `Result<number, Either<'division_by_zero', GeneratorError>>` if you wanted to.


### Ok so why are you telling me all this?

So going back to that issue that was openend up over 8 months ago, "Why can't I return different error types in a `andThen` chain?".

Rust, Haskell, Elm and most other languages that have mainstream usage of a `Either` / `Result` type do not have subtyping.

You can't have a function in Rust that looks like this: `fn union<T, A>(val1: T, val2: A) -> T | A`. You would have to wrap `T` and `A` inside some other type, like (ironically) `Either`. So in order for the function to compile, you'd have to refactor it to be `fn union<T, A>(val1: T, val2: A) -> Either<T, A>`.

But in TypeScript ... we don't have that limitation (or downside as some may see it).

Therefore you get unions for free without having to introduce wrapper types!

This is why I finally caved and decided to veer off the tradition of all other implementations of `Result`.

The new signature of `andThen` for `neverthrow` is:

```typescript
class Result<T, E> {
  andThen<U, F>(fn: (val: T) => Result<U, F>): Result<U, E | F> { ... }
}
```

See how the returned error type (`F`) is distinct from the error type on the originating result (`E`)?

The beautiful thing about this is that TypeScript joins duplicate types. So if you do, `Result<number, string>.andThen<Cat, string>` the output result is not `Result<Cat, string | string>` but `Result<Cat, string>` since the two error types are the same!

Anyways, curious to hear what folks think about this new functionality.


---

I want to give a special shoutout to [`@paduc`](https://github.com/paduc) who has been helping **a lot** for, what feels like, more than a year now. He's super helpful on issues and has contributed significantly to `neverthrow`. Thank you, Pierre.
