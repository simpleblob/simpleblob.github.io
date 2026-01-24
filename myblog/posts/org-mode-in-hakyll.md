---

title: Org Mode in Hakyll
subtitle: The Ultimate Toolkit for Publishing?
description: Testing Pandoc's org to HTML compilation.
tags: emacs, haskell
created: 2017-11-25
published: 2017-11-26
status: finished
confidence: log
importance: 1
---
Testing Pandoc\'s emacs-org file conversion to html, based on this
[page](https://github.com/turboMaCk/turboMaCk.github.io/blob/develop/posts/2016-12-21-org-mode-in-hakyll.org).

This is the end of post itself. Everything below is just to test how
Pandoc handles org files.

# This is H1

There is paragraph under h1

## H2

### H3

# Some basic test

This is **bold**, *italic*, `code`{.verbatim}, `verbatim` and ~~strike~~
text.

-   However ***bold and italic*** doesn\'t play well when used together
    like in markdown.
-   However ***bold and italic*** doesn\'t play well when used together
    like in markdown.

# List

-   Bullet
-   Another bullet
    -   child
        -   deep

## Other style

-   Bullet
-   Another bullet
    -   child
        -   deep

## Other style

1.  Bullet
2.  Another bullet
    1.  child
        1.  deep

Style `*`{.verbatim} isn\'t supported.

# Links

[*<http://orgmode.org/>*]{.spurious-link
target="link to org mode homepage"}

# Check List \[1/3\] \[33%\]

-   [ ] Item
-   [ ] Item
-   [x] Checked item

Heading and has special class however `<ul>`{.verbatim} and
`<li>`{.verbatim} are plain.

# Task List

## [TODO]{.todo .TODO} some to-do {#some-to-do}

## [DONE]{.done .DONE} done to-do {#done-to-do}

Items are added with special class.

# Tables

  number   description
  -------- --------------------
  1        looooong long name
  5        name

`<tr>`{.verbatim} has `even`{.verbatim} and `odd`{.verbatim} classes.

# Source Code

**Emacs Lisp:**

``` {.commonlisp org-language="emacs-lisp"}
(defun negate (x)
    "Negate the value of x."
    (- x))
```

``` {.commonlisp org-language="emacs-lisp" results="output"}
(print
    (negate 10))
```

``` example
-10
```

There are interesting classes like `sourceCode`{.verbatim} and
`example`{.verbatim}. Also there html5 attributes prefixed with
`rundoc-`{.verbatim}.

**Haskell:**

``` {.haskell results="output"}
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

# LaTeX

-   **Characters:** α β → ↑ ∨ \\and ⟹ π ∞
-   **Inline Math:** $f(x) = x^2$
-   **More complex:** $\frac{x^2}{2}$

LaTeX characters are wrapped in `<em>` and Math inside
`<span class="math inline">`.

## ℋℯ𝓁𝓁ℴ!

```{=latex}
\begin{align*}
  8 * 3 &= 8 + 8 \\
        &= 24
\end{align*}
```
**NOTE:** *There is standard LaTeX embeded above which is skipped during
compilation to HTML.*

**This is using** [*<https://www.mathjax.org/>*]{.spurious-link
target="MathJax"}

$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$

# Deadline

# Tagged [[tag]{.smallcaps}]{.tag tag-name="tag"} {#tagged}

Tags are not visible in render

# Block Quote

> Org mode is amazing. So is Hakyll & Pandoc.

# Image

```{=org}
#+CAPTION: This is the caption for the next figure link (or table)
```
```{=org}
#+NAME:    figure
```
```{=org}
#+KEY:     fig
```
<http://media.riffsy.com/images/f8534774b678ad1932b379a03460680b/raw>

Images has to have extension like:

![](../assets/lena-image.jpg)

then it can be loaded even from other origin..

![](https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png)

# Description List

Frodo
:   The hobbit ringbearer

Aragorn
:   The human ranger, true kind of Gondor

Gandalf
:   The Grey Wizard

creddits to [*<https://www.reddit.com/user/nihilmancer>*]{.spurious-link
target="nihilmancer"}

# Footnotes

This has some[^1] foot note.

[^1]: The link is: <http://orgmode.org>
