Title: The Economics of JS
Date: 2018-04-02
Tags: software

This is an opinion piece.

## tldr;

The democratization of the web platform has brought about an influx of JS alternatives - some of which will eventually overtake JS as the de-facto tool for writing user interfaces on the web.


## JavaScript Has Reached Its Zenith

It's easy to forget JS's early history. [The language was built by one person in just a few days](https://en.wikipedia.org/wiki/JavaScript#Beginnings_at_Netscape). I don't think Brendan Eich imagined JS would become such a central player in the evolution of the web. Nor did he intend it to be the language for use in basically every type of application. But browsers have over-time come to dominate the software landscape making JS the default language for reaching millions of users. Economics, not JavaScript's inherent features, are what lead it to become so prominent. There was no alternative way to add interactivity and delight to web pages. JS had a monopoly on front-end languages.

Since its inception, JS has continued to evolve; pushing the limits of what could be accomplished while also improving the developer experience of the language by leaps and bounds. We're spoiled in this day and age when dealing with asynchronicity, but we all remember a time when callback-hell was the norm. The barrier to creating complex apps has progressively declined.

But there are only so much changes one can make, and features one can add to a language, before any [additions become only marginally beneficial](https://www.britannica.com/topic/diminishing-returns). This is simply an economic law.

I think the last game-changing update to JS was `async / await`. Everything after that has been nice, but not revolutionary. In essence; JS will only get marginally better, but will stay fundamentally as it is for the foreseeable future.

At its optimal state, JS is good to use, but it is not the tool to solve every conceivable task as [some people are lead to believe](https://twitter.com/TheLarkInn/status/979921194467110912).


## The Democratization of the Web Platform

As JS's evolution slows down, the web platform is undergoing a democratization. You no longer need to use JavaScript to deliver a web application to your users. This was not the case at the outset of the web platform. The monopoly is no more, and the market for front-end programming languages is starting to resemble something closer to a free market; fueled by a large supply of alternative languages.

Technologies such as [WebAssembly](http://webassembly.org/) are opening the door to solving problems which were historically restricted to the domain of JavaScript - Languages that arguably deal much better with software complexity at a large scale.


## Software Complexity and JS

As JS apps got more and more ambitious, the need to manage software complexity increased. Unit tests are no longer enough. Linting is no longer enough.

Out of this need, [Flow](https://flow.org/) and [TypeScript](https://www.typescriptlang.org/) emerged to help bring typesystems into JS, and hence help increase software correctness.

Herein lies a hint that we've reached the limits of JS's capabilities. We're forcing types on an untyped language. And these aren't toy projects - there's a lot of demand for this featureset; just look at the downloads per day for each of the respective npm packages.

I thank the heavens for TypeScript. It has made my day job a lot less stressful. But it's not without its rough edges:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">
  This is the source code for a TS declaration file for a Google package w aprx. ~170,000 downs/mnth. <br><br>Eventually people get lazy when writing these files and just start telling the compiler, &quot;ahh don&#39;t worry about it!&quot;<br><br>&#39;any&#39; types defeat the purpose of static typing.<br><br>facepalm. <a href="https://t.co/a8iyfrolEV">pic.twitter.com/a8iyfrolEV</a></p>&mdash; Gio (@_gdelgado) <a href="https://twitter.com/_gdelgado/status/974324130479718400?ref_src=twsrc%5Etfw">March 15, 2018</a>
</blockquote>

The above tweet represents the TypeScript ecosystem fairly in my opinion. The sheer amount of outdated or simply improperly written types is astounding. As I mentioned in the twitter thread: I would have considered contributing to the DefinitelyTyped project but from the looks of it, I get the impression that it's a lost cause.

The prolific use of `any` in TypeScript is saddening. By using `any` you have thrown all type safety out the window. Now you're writing a Java-esque version of JS, that has *some* type safety but it's not guaranteed because of the `any` escape hatch.

I think this is partly because of how fast the JS ecosystem moves: For every typedef written, 3 new packages come out and one week later the aforementioned typedef becomes outdated due to a major version bump (I am only estimating, so please correct me if I am way off). With this sort of pace it's impossible to keep up. The rationale becomes, "I'll fix the types later, but for now I'll just say everything is an `any`."


So here we are with a plethora of very large JS projects, and the current solution is to throw a type system on top of a dynamic language. This makes total sense for projects that are too large to undergo a total rewrite ... But what about all the smaller projects? Why not just use a whole other (better) language altogether?

#### A paradigm shift

Nowadays there is lots of talk about functional programming. Many have realized the perils of object oriented architectures and we are slowly seeing a shift toward functional programming and stateless architectures.

This shift isn't inherently bad for JS as it has FP features, however, most JS programmers have no idea how to code functionally.

Further, much like in typescript, if you allow for escape hatches, you will use escape hatches. That is to say; if you can use a `for` loop to get a feature out quicker than thinking ahead of time of a more functional (and longer lasting) approach, then you'll eventually succumb to the temptation. Again, this is economics at play: It's much easier to follow the path of least resistance.


## Moving away from JS

As mentioned above, the web platform's opening up to new languages is evidence of demand for better guarantees around software complexity.

Now that there are capable alternatives to writing web applications in languages other than JS, we'll start seeing growing usage of these languages for serious projects. Most notably ReasonML within Facebook.

- [ReasonML](https://reasonml.github.io/)
- [Elm](http://elm-lang.org/)
- [ClojureScript](https://clojurescript.org/)
- [PureScript](http://www.purescript.org/)

These are the compile-to-JS languages that I'm aware of, and I'm sure there are many more which deserve a shot-out. The point being that there is clearly a trend here. Many people are unsatisfied with JS's ability to write complex software.

That's not to say you can't write complex software in JS. It's just way harder to do so.

These are the sorts of things you have to deal with when writing apps in JS:

- No type system (and if you use Flow and JS, have fun dealing with their verbosity - not to mention the insidious usage of `any`)
- Quirks around the language (don't use `==` or you'll implicitly coerce types! Don't use `arguments` as it's not actually an array! What does `this` mean in this context?)
- Highly fragmented package ecosystem. There are **many** alternative packages to solving the same problem:
    - "Oh you want to unit test? Well, just use mocha + chai + sinon. Or alternatively Jest. Or Ava. Or Tape. Or ..."
    - Which one is the right one? Only an expert JS dev could tell you.
    - Now you need a bundler (Webpack is the current standard - which is a glorified compiler)
    - Are you using CommonJS or AMD modules?
    - Are you transpiling your code?
    - Which version of Node are you using?


JS is a bit of a catch 22: It's probably one of the easiest languages to get started with, however its simplicity means that it's also one of the toughest languages to master. The amount of discipline and skill required to build a healthy and maintainable codebase is testament to this.

The simplicity in getting started with JS defers complexity further down the time horizon. You'll shoot yourself in the foot sooner or later because there are basically no restrictions to what you can or cannot do in the language. And then you're left staring at a cesspool of code-smells with nothing to help you.


<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Unreadable code does not get maintained. It gets patched around, avoided, or scrapped. <a href="https://twitter.com/hashtag/WriteCleanCode?src=hash&amp;ref_src=twsrc%5Etfw">#WriteCleanCode</a></p>&mdash; Eric Elliott (@_ericelliott) <a href="https://twitter.com/_ericelliott/status/976836311943385088?ref_src=twsrc%5Etfw">March 22, 2018</a></blockquote>

> Hmm, maybe JS isn't conducive to maintainability in the first place?

Tell a novice JS dev, "write clean code" and let me know how that pans out. Conversely, writing in, say Elm or Rust is a lot saner. You have a compiler that **helps you**. It ensures that your code will run as you intend it to and it [provides you feedback as you go](http://elm-lang.org/blog/compiler-errors-for-humans). It's materially harder to write unclean code in many other languages relative to JS.


Do you want to refactor a large chunk of your JS codebase? I sure hope you have written enough unit tests and your ESLint config is there to catch other errors (so much so that you've essentially done what a compiler would have done for you out of the box).



#### NPM == jungle full unpredictable packages

You don't need to unit test your package / library before publishing it to npm.
You also don't have a compiler in JS to provide guarantees that the package you wrote isn't going to crash.

So the packages you download from npm are basically at your own peril. This is why you need a downloads counter in npm. The logic being, "If others are downloading this package, then surely it's safe to use". But obviously this is not always the case as edge cases often take a long time to surface.

This is in stark contrast to any of the package ecosystems in strictly typed languages (crates.io, Hackage, Elm-Package, etc...)

Another benefit with these other languages is that they are sustained by communities consisting of very skilled developers (the influx of devs coming from code bootcamps doesn't help alleviate the code quality problem plaguing npm). That's not to say that you don't have amazing devs in JS-land (you do), but the distribution of talent in JS has a massive standard deviation.


## Equilibrium in the Web Platform

In the back-end ecosystem, there is complete freedom to choose whichever language best solves the task at hand. There is no monopoly unlike the front-end world. But I've mentioned already, this is no longer the case, and over time, we will see the advent of incredibly large and complex front-end applications built without JS (or with JS as a minor component to the app: Much like the concept of [ports in Elm](https://guide.elm-lang.org/interop/javascript.html))

This is known as [equilibrium in economics](https://en.wikipedia.org/wiki/Economic_equilibrium) and it's about time we reached it in the front end development ecosystem.



<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
