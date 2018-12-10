---
header-includes: |
    \usepackage{xparse}
    \newenvironment{example}{%
        \texttt{begin example}\par
    }{%
        \par\texttt{end example}
    }
    \newenvironment{with space}{%
        \texttt{begin with space}\par
    }{%
        \par\texttt{end with space}
    }
    \newenvironment{arguments}[2]{%
        \texttt{begin arguments #1 #2}\par
    }{%
        \par\texttt{end arguments}
    }
    \NewDocumentEnvironment{keyword}{O{one} O{two} O{three} O{four}}{%
        \texttt{begin keyword [#1 #2 #3 #4]}\par
    }{%
        \par\texttt{end keyword}
    }
---
A test document
===============

Here we have an example document.

A section
---------

Our main goal is to convert a `div` with the [data attribute][ref] into
a `\LaTeX` environment.  We want to find only `div`s with the
`data-environment=([\w-]+)` (in quotes if the environment contains
spaces) and convert those to `\LaTeX` environments.

::: {data-environment=example}
For example, this should be in an `example` environment.
:::

::: {data-different=other width='100%'}
And this should not.
:::

::: { data-environment="with space" }
An environment with a space in the name!
:::

::: { data-environment=arguments data-environment-args="one,two" }
And this one has arguments.
:::

::: { data-environment=optional data-environment-keyword="here's,another,example" }
How about keyword arguments?
:::

[ref]: https://johnresig.com/blog/html-5-data-attributes/
