Title: Adventures In Building Arbitrarily Large, Distributed and Immutable Trees 🌲
Tags: software
Summary: Stumbling on an interesting challenge while building ParlezVous.
UUID: 9eb19bc6-6b2e-4648-877d-0683de1396a4

I'm working on an embeddable commenting platform called [ParlezVous](https://parlezvous.io/) focused on:

- Privacy
    - The business model will not be based on selling user data
    - You can read the code for yourself
- Performance
    - Fast load times
    - Low Bandwidth
- Tiered Pricing
    - There will be a low-volume free tier (with potentially a subset of features)

It's still early days (demo [here](https://demo.parlezvous.io/)), but signups should be open in about a month.

If you're not sure what "embeddable commenting platform" really means. Think of it as a little widget you embed on each blog post so that people can comment and engage with your content.

At the heart of this application is the idea of a "comment thread".

> A **thread** is a set of comments for a particular **post**.

Pictorally, it looks a little like this:

![Comment Tree]({filename}/images/comment-tree-structure.png)

So one can see that, formally speaking, a thread is one or many comment trees. A tree can, at least hypothetically, be arbitrarily wide and deep as well.

I didn't want to impose a superficial limitation on this data structure (not yet at least). So right now, it is technically possible to have 1000+ consecutive replys for any post. Or 1000+ top-level comments for any post.

Go on, try it:

https://demo.parlezvous.io/

Let me know if it breaks :) I'll really appreciate the feedback.

So, how do you efficiently read and update this data structure knowing that it could be arbitrarily large?


## Loading Threads Incrementally

Knowing that any one thread may contain extremely deep trees, or extremely wide trees, it's not wise to naively load the entire thread at once. Thus, when the front end asks for a thread, it receives only a subset of the entire thread. Currently, I only impose [depth limits](https://github.com/parlez-vous/server/blob/2496bacf55a2acbebc30631b5562f34272794d76/src/db/actions.ts#L227) on the thread but no width limits.


![Comment Tree]({filename}/images/diagram-2.png)

So if the front end only has a partial tree, how does it go about:

- Appending nodes to this partial tree, and
- Loading the remainder of the tree
    - The `???` in the above diagram represents *potential* pagination points - subsequent round trips to the server in order to continue retrieving the missing parts of the tree. More on this later.


### Receiving And Storing The Initial Chunk

During initialization the Elm front end [requests](https://github.com/parlez-vous/embed/blob/master/src/elm/Model.elm#L135) for the initial subset of the comments in the tree as described above.


The server responds with the following data:


```json
{
  "data": {
    "comments": {
      "ckiryujoj0114nptmpixc0r1q": {
          "id": "ckiryujoj0114nptmpixc0r1q",
          "anonAuthorName": "happy-whirl-warlord",
          "body": "ma dawgggg",
          "votes": 0,
          "postId": "ckiru6kcx08096atms0b3m46j",
          "createdAt": 1608156482852,
          "updatedAt": 1608156482852,
          "parentCommentId": "ckirymbiz0029nptmdbpddf0y",
          "authorId": null,
          "author": null,
          "replyIds": [],
          "isLeaf": false
      },
      "ckirym7fq0020nptm42cg5fco": {
          "id": "ckirym7fq0020nptm42cg5fco",
          "anonAuthorName": "jolly-bionic-emperor",
          "body": "Yooooooo",
          "votes": 0,
          "postId": "ckiru6kcx08096atms0b3m46j",
          "createdAt": 1608156093734,
          "updatedAt": 1608156093734,
          "parentCommentId": null,
          "authorId": null,
          "author": null,
          "replyIds": [
              "ckirymbiz0029nptmdbpddf0y"
          ],
          "isLeaf": false
      },
      ... etc,
    },
    "postId": "ckiru6kcx08096atms0b3m46j",
    "topLevelComments": [
      "ckirym7fq0020nptm42cg5fco",
    ],
  }
}
```








## Preface: Quick Intro To Elm

> This blog post isn't specifically about Elm. But if you're not familiar with Elm, then the code examples may not make sense.

In Elm and other pure languages such as Haskell, you can't mutate values, including the contents of "containers" (like arrays, hashmaps, sets, etc).


```typescript
// TypeScript example:
// Although `myList` is assigned to be a constant, `myList` holds nothing more
// than a reference, or a pointer.
// You can mutate everything about the referenced value,
// so long as you don't change / mutate the reference itself.
const myList = [ { name: "Jerry", age: 45 }, { name: "Elaine", age: 47 } ]

// swap the reference for something else, not allowed (runtime exception)
myList = "hello"

// mutate the referenced data in-place, this is allowed
myList[0].name = "Cosmo"
```

In pure languages like Elm, you can't just hold a reference to some data and update the data as you wish. Here is how you would go about doing the above in Elm.


```elm
myList =
  [ { name = "Jerry"
    , age = 45
    }
  , { name = "Elaine"
    , age = 47
    }
  ]

newArray =
  List.indexedMap
    (\idx person ->
      if idx == 0 then
        -- This is elm's record / object update syntax
        -- note that this doesn't mutate the existing object
        -- instead it creates a new one
        { person | name = "Cosmo" }
      else
        person
    )
    myList
```

Note that the above runs (likely - sometimes compilers optimize functional code like this quite aggressively) in `O(n)` whereas before we had `O(1)`. Ewwwwwww.


