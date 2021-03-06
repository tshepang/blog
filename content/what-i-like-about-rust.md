+++
title = "what I like about Rust"
date = 2015-12-31
[taxonomies]
tags = ['Rust']
+++

-   Ambitious: the aim of being memory safe without the use of a garbage
    collector, allowing it to achieve C++ execution speeds.
-   Naming conventions:
    -   `name_with_underscores` for variable and function names
    -   `HttpRequest` instead of `HTTPRequest` for type names
-   Error reporting: compile errors are the best I've seen (though
    I've only really seen those of C and C++); they are even
    color-coded!
-   2 short keywords:
    -   `fn` for function declarations
    -   `use`, instead of `using` or `import`
-   I love that I don't need to add (the tedious) parenthesis around
    the *condition expression* in an *if*, *while*, and *match*
    statements:

    ```rust
    if true {
        // always executes
    }

-   The semicolon rule: I initially found it surprising that omitting a
    semicolon after a value is shorthand for returning. I appreciate it
    now... it's quite nifty, and I in fact now find `return`
    statements ugly.
-   Traits: they are an elegant way of providing abstract interfaces,
    and are therefore used in generic programming. As an example, a
    function can be made to accept different data types, so long as
    those types implement the given trait (or traits). Gorgeous!
-   The `match` statement is kool: exhaustiveness check, no
    fall-through, and nice syntax.
-   Allowing a trailing comma after a list of items, which is really
    great for copy-pasting and diffs.
-   Packaging conventions: by default, the build tool, Cargo, ensures
    that all build sources (which may include documentation) are placed
    in src/ in the root of a source distribution.
-   A fast-paced and time-based release cycle: a stable release will be
    made every 6 weeks, which is very ambitious for a programming
    language.
-   Development process:
    -   No one, including the Core Team, pushes anything to the Rust
        tree. Each person gets their changes reviewed first, and they
        mostly get approved by someone else.
    -   Merging the changes to the tree is nearly always done via a
        continuous integration system, which first ensures that each
        change passes all tests.
-   Allows masking of variables, even with different types:

    ```rust
    let foo = 10;
    let foo = "ten";
    ```

    This is convenient.

-   The amount of iterations its design went through during its pre-1.0
    development, which included numerous breaking changes, was...
    impressive. That's an indication that what resulted is a far better
    design than we could have had. The sheer amount of effort taken,
    which was such a unique experience for me, makes me feel grateful (I
    watched the activity for about a year before 1.0 was released). I am
    also grateful for the resilient users who kept up with the pain of
    the frequent changes, for they helped keep the language relevant and
    exciting, while also providing feedback.
