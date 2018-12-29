Title: Parlez-Vous Anglais? (Part 2)
Tags: software
Summary: In Part 2 of my blog series on my side project "Parlez-Vous", I dive into the architecture & design decisions made for the API server.
Status: draft

# The Server

I have a lot of experience working with TypeScript and express because of my [day-job](https://setter.com/). This experience has taught me a lot about how dangerous expressjs middleware can become. 

You have functions that assume that some other function has done something. ExpressJS middleware encourages tight coupling between request-handling functions.

Example: The `body-parser` npm module adds the `.body` field to your express `req` request handler parameters.

As a server grows in scale and complexity, developers can and will add way too much indirection by way of middleware; eventually leading to request handlers that assume way too much (Does req have `x` inside it? does `req` have `y` inside it also? If it doesn't have `y` then it means that it has `z`).

If you read through the code, you'll notice that I don't really leverage the notion of express middleware. I make everything self-contained. With zero assumptions :)

My experience working with Rust, Elm and to a small extent Haskell, has taught me the value of strongly-typed systems. It's amazing how much clarity you have as a developer when you code *after* you've thought about the types of your system. The puzzle puts itself together! It's also great working with systems that don't throw exceptions, but rather encode the potential for error within the typesystem itself.

JavaScript / TypeScript both have the `throw` and `try` / `catch` idioms at your disposal, but there's a more elengant (and safer) way to handle potential failure states.

That's why I wrote my own `Result` type. You can find the class declaration [here](https://github.com/parlez-vous/server/blob/master/src/utils.ts#L7). A `Result` encodes the possibility of success or failure within the typesystem.

Dealing with errors by throwing exceptions is bound to lead to runtime exceptions when you or a colleague forget to catch these thrown exceptions. The beauty of encoding a success or failure state in the typesystem is that now you get compile-time guarantees around functions that *may* fail. 

Here's an example usage of result from my server: 

<script src="https://gist.github.com/gDelgado14/86287bd69d3459fe4b566deb149497d4.js"></script>

A few things to note. The return type is `Promise<Result<whatever>, string>`. In plain english, this means, "I return a Promise, which will never throw, and has only two scenarios: Success, in which case I have a `whatever` value, or failure in which case I have a `string` value". 

You can then do cool functional things like `map` a result. There's also a convenient `mapErr` method which maps a failure value into some other failure value!

Another thing to note is that the function is guaranteed to never throw. This is because I wrap it inside a big `try/catch`. This means, like I mentioned, that there are only two (**and only two**) scenarios. Success and failure. There isn't a third random thing waiting to happen if you don't `.catch` this promise. Then the compiler becomes your friend and ensures that you are ever only dealing with one of the two states of a `Result`.

These ideas are ripped right off from the FP community (see the [Elm](https://package.elm-lang.org/packages/elm/core/latest/Result), [Haskell](https://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Either.html#t:Either) and [Rust](https://doc.rust-lang.org/std/result/enum.Result.html) variants of Result), and the design of my `Result` class is heavily inspired by the Rust api. I figured since I'm going to port this server to Rust eventually, I may as well make it as Rust-like as possible to begin with.


##### Proving You Control a Domain

In order to protect my server, and only allow legitimate requests, I will be implementing a [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) whitelist. Therefore, I must know who is legitimately a user, and who is trying to post comments on behalf of a website that hasn't yet registered on parlez-vous. By knowing which sites are legitimate, I can then add them to the CORS whitelist and allow that domain to start making requests to my server.

In order to prove that someone has control of a domain, I will require them to add a `TXT` record to their domain's DNS. My server will then perform DNS lookups and search for the associated `TXT` record. At which point, a user is now free to embedd parlez-vous' comment widget into their site!


