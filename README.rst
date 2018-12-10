Convert marked Pandoc ``Div`` to LaTeX ``environments``
=======================================================

When structuring a document, one frequently wants to specify a region as
a particular type for latter rendering.  In HTML, one can use the
``<div>`` tag and an associate CSS for this task.  In LaTeX, one would
use an ``environment``.  Each one works well with its associated display
format.  However, using Pandoc_ to convert the HTML markup to LaTeX
looses the information.  One sticking point is HTML and LaTeX have very
different concepts of what a class and an environment should do.
Further, when introducing Pandoc to the mix, one must deal with all
`potential outputs`_.

The natural solution is to use a filter_.  But, how does one mark the
region that needs to be processed?  One option is to use a ``class``,
but we have seen that that does not play well with other Pandoc outputs.
A nice option is to use a specialized attribute for the ``<div>`` like
the `data attributes`_ in HTML5.  This has the advantage of marking
fenced ``<div>`` regions for use in a particular output that can be
safely ignored by others.  This filter processes specially marked
regions of a Pandoc markdown file and places them in a LaTeX
``environment``.

.. _Pandoc: https://pandoc.org
.. _potential outputs: https://github.com/jgm/pandoc/issues/2106
.. _filter: http://pandoc.org/filters.html
.. _data attributes: https://johnresig.com/blog/html-5-data-attributes/

Installation
------------

Run::

   python setup.py install

Alternatively, you can use ``develop`` or the ``--user`` flag if you
want to hack the filter or install for a single user.

Usage
-----

To declare an environment in Pandoc's markdown, use the attribute
``data-environment=.*`` like::

   ::: data-environment=example
   This is in an `example` environment
   :::

Then simply run Pandoc with the filter argument and set the output to
``latex``::

   pandoc --filter pandoc-div2env example.md -t latex -o example.latex

This will yield::

   \begin{example}%
   This is in an \texttt{example} environment%
   \end{example}

The ``%`` is included to strip additional spaces around the content.
This filter attempts to tightly place the environment beginning and
ending around the content.  This is an attempt to prevent introducing
additional paragraphs where they might not be intended.

.. note:: The environment *must* be defined in the LaTeX document.

To add positional arguments, use ``data-environment-args=...``::

   ::: {data-environment=example data-environment-args="one,two"}
   An example with arguments
   :::

becomes::

   \begin{example}{one}{two}%
   An example with arguments%
   \end{example}

To add keyword style arguments use::

   ::: {data-environment=example data-environment-args="one" data-environment-keyword="width=0.6\textwidth,color=blue"}
   A final example with keyword arguments and positional arguments
   :::

becomes::

   \begin{example}[width=0.6\textwidth,color=blue]{one}
   A final example with keyword arguments and positional arguments
   \end{example}

.. note:: Keyword arguments are copied as provided inside the quotes
          while positional arguments are separated by the ',' and
          enclosed within '{...}'.

Similar filters
---------------

Two other Pandoc filters exist for converting ``<div>`` tags to LaTeX
environments: pandoc-latex-environment_ and latexdivs.py_.  Both of
these filters use the class of the ``<div>`` to define the environment.
Pandoc-latex-environment uses the classes designated in the metadata
header while latexdivs.py uses an attribute from the ``<div>``.  They
both use the original pandocfilters_ whereas this filter uses the newer
panflute_ package.  Further, those packages only convert the environment
and do not convert arguments.

Finally, those filters simply place the begin and end code as blocks
around the content.  This introduces additional line breaks around the
content of the environment which may increase the size of the
environment.  In some cases, such as color blocks in a presentation,
this is undesirable.  This filter places the raw LaTeX blocks inside the
``<div>`` to reduce the line breaks.

.. _pandoc-latex-environment: https://github.com/chdemko/pandoc-latex-environment
.. _latexdivs.py: https://github.com/jgm/pandocfilters/blob/master/examples/latexdivs.py
.. _pandocfilters: https://github.com/jgm/pandocfilters
.. _panflute: https://github.com/sergiocorreia/panflute

Limitations
-----------

This filter targets ``latex`` output.  As such, it only works for
``latex`` and ``beamer`` outputs.

This filter cannot handle optional arguments defined using ``xparse``.
All arguments must either be positional (enclosed individually in
``{...}``) or optional, keyword like (enclosed in ``[...]``).

Additionally, this filter does not check if an environment is valid or
has the proper syntax.  It is up to the author to make sure the
environment exists in the final document just like any LaTeX document.

