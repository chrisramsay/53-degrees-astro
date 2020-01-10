Useful reStructuredText
#######################

:date: 2020-01-02 10:14
:category: astrophotography
:tags: astronomy, astrophotography
:slug: useful-restructuredtext
:related_posts:
:series:
:author: Chris Ramsay
:status: published
:language: en
:show_source: True

.. Roles
.. role:: banana(strong)
.. role:: highlight(code)
    :language: python
.. role:: porcupine(code)
    :language: c
.. contents::

.. The main document

Purpose
-------

.. PELICAN_BEGIN_SUMMARY

This is a brief memory aid for me with some small, and perhaps useful, tips when
writing articles using |RST|_ [#]_. I am aiming to keep on top of this document
and maintain it as a living thing; when I find something new and useful, it will
be appended.

.. PELICAN_END_SUMMARY

Hints and Tips
--------------

Subscripts and Superscripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The difficulty with sub and superscripts is that whitespace is not usually
needed with them as they usually accompany one or more letters closely. So when
using them in |RST| whitespace can be backslash escaped - this means that the
whitespace added for readability here will be removed during processing. Here is
an example for a superscript.

.. code-block:: restructuredtext

   Inter Intergrated Circuit, or I\ :sup:`2`\ C, was invented by Phillips
   Semiconductor in 1982.

This renders like the following:

    Inter Intergrated Circuit, or I\ :sup:`2`\ C, was invented by Phillips
    Semiconductor in 1982.

Subscripts work in pretty much the same way, so without further ado, here is an
example. Note the mix of backslash escapes and genuinely desired whitespace.

.. code-block:: restructuredtext

    The difference between t\ :sub:`ground` and t\ :sub:`sky` gives us a
    reading known as t\ :sub:`∆`\ .

The above looks like this when rendered:

    The difference between t\ :sub:`ground` and t\ :sub:`sky` gives us a
    reading known as t\ :sub:`∆`\ .

Maths
~~~~~

Otherwise known as *math* by our American friends, mathematical formulae can
fairly easily be rendered rather nicely using a combination of |RST| and
standard :math:`{\LaTeX}` syntax.

Maths can be written up as a standard |RST| role such as:

.. code-block:: restructuredtext

    The well known quadratic formula:

    .. math::

        x = -b \pm \frac{\sqrt{b^{2}-4ac}}{2a}

Which renders like this:

    The well known quadratic formula:

    .. math::

        x = -b \pm \frac{\sqrt{b^{2}-4ac}}{2a}

One can also include maths inline, such as the following:

.. code-block:: restructuredtext

    The power series, :math:`\frac{1}{0!}+\frac{2}{1!}x+\frac{3}{2!}x^2+\frac{4}{3!}x^3+...` states
    that...

Which looks like this when rendered:

    The power series, :math:`\frac{1}{0!}+\frac{2}{1!}x+\frac{3}{2!}x^2+\frac{4}{3!}x^3+...` states
    that...

For further information on what :math:`{\LaTeX}` can do with mathematical
formulae `visit this very informative site`_.

Custom Roles
~~~~~~~~~~~~

Roles are a custom interpreted text role that, once registered with the parser
by first declaring them, can be used throughout the document. Custom roles can
be used to extend existing roles by specifying them as a second argument.

General Role Usage
^^^^^^^^^^^^^^^^^^

Let us take a look at applying in line styles using custom roles.

.. code-block:: restructuredtext

    .. role:: banana(strong)

    We all love :banana:`yellow fruit` flavoured milk shakes.

Renders as:

    We all love :banana:`yellow fruit` flavoured milk shakes.

Some roles accept an extra parameter, depending on the base role which they are
extending. For example, one very useful role to define is an inline syntax
highlight:

.. code-block:: restructuredtext

    .. role:: highlight(code)
        :language: python

    Here is a suggestion :highlight:`['%s=%s' % (n, v) for n, v in zip(self.all_names, self)]`. I think that will do what you need.

Renders as:

    Here is a suggestion :highlight:`['%s=%s' % (n, v) for n, v in zip(self.all_names, self)]`
    . I think that will do what you need.

One must bear in mind that there are a couple of considerations to be made when
using roles. The first consideration is that we cannot define this role more
than once in a given document. Well, that's not entirely true, because you might
do the following:

.. code-block:: restructuredtext

    .. role:: highlight(code)
        :language: haskell
    .. role:: highlight(code)
        :language: python

This will not cause an error in the |RST| parser; instead, the last
role definition will simply override any previous roles with the same name. This
leads to another important point: as we now know, because a highlight role is
only usable once, it is only worth using if you have more than a small amount of
syntax highlighting to do within a document, and the language you are referring
to remains the same throughout.

Next, and rather importantly, your new role name is inexorably linked to the
class name defined in your CSS. Let us define a role named ``porcupine``:

.. code-block:: restructuredtext

    .. role:: porcupine(code)
        :language: c

    This is important :porcupine:`float t_ref = read_dev(dev, TEMP_OBJ);`

As can be seen below, the rendered code is formatted correctly as C code by the
work of the Pygments syntax highlighting engine, so no problem there then.

.. code-block:: html

    <code class="porcupine c">
        <span class="kt">float</span>
        <span class="n">t_ref</span>
        <span class="o">=</span>
        <span class="n">read_dev</span>
        <span class="p">(</span>
        <span class="n">dev</span>
        <span class="p">,</span>
        <span class="n">TEMP_OBJ</span>
        <span class="p">);</span>
    </code>

However, unless you have a ``porcupine`` class in your CSS defining your syntax
colour rules, the syntax highlighting will not be coloured correctly by the
browser. This leads us nicely to problems particular to code syntax
highlighting.

Usage of Roles for Syntax highlighting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let us have a look at how the highlighted part above is rendered. By default the
`Pygments`_ theme CSS that comes with many Pelican themes will not syntax
highlight anything other than code in ``pre`` tags. Take a look at the HTML
below; this is what the rendered Python from the previous section looks like:

.. code-block:: html

    <code class="highlight python">
        <span class="p">[</span>
        <span class="s">'</span>
        <span class="si">%s</span>
        <span class="s">=</span>
        <span class="si">%s</span>
        <span class="s">'</span>
        <span class="o">%</span>
        <span class="p">(</span>
        <span class="n">n</span>
        <span class="p">,</span>
        <span class="n">v</span>
        <span class="p">)</span>
        <span class="k">for</span>
        <span class="n">n</span>
        <span class="p">,</span>
        <span class="n">v</span>
        <span class="ow">in</span>
        <span class="nb">zip</span>
        <span class="p">(</span>
        <span class="bp">self</span>
        <span class="o">.</span>
        <span class="n">all_names</span>
        <span class="p">,</span>
        <span class="bp">self</span>
        <span class="p">)]</span>
    </code>

As mentioned, the whichever Pygments theme CSS you are using, it may need to
have the following change made:

.. code-block:: css

    [...]
    .highlight pre .g { color: #657b83 } /* Generic */
    .highlight pre .k { color: #859900 } /* Keyword */
    .highlight pre .l { color: #657b83 } /* Literal */
    [...]

to:

.. code-block:: css

    [...]
    .highlight .g, .highlight pre .g { color: #657b83 } /* Generic */
    .highlight .k, .highlight pre .k { color: #859900 } /* Keyword */
    .highlight .l, .highlight pre .l { color: #657b83 } /* Literal */
    [...]

This takes into account that we also want to highlight items that are direct
descendants of the ``.highlight`` class, as well as those grandchildren with
``pre`` as a parent tag [#]_.

Comments
~~~~~~~~

I do not know about anyone else, but I find adding comments to articles that I
am writing incredibly useful [#]_; they help me by serving as small reminders to
complete a section or just give me a reason why something has been put together
in a certain way.

Comments are processed into a comment element by the |RST| parser but, depending
on the output formatter, are removed prior to being processed output on the
final document.

Below are some comment mark up examples:

.. code-block:: restructuredtext

    .. This is a comment
    ..
       [this is also] a comment
    ..
       |this is| also a comment
    ..
       _this: is also a comment
    ..
       .. finally:: this is also a comment


The only restriction on comments is that they may not contain any other markup
syntax constructs, unless the comment begins with a ``..`` on a line by itself.

In Conclusion
-------------

In writing this document I have read the excellent |RST| documentation so much
more thoroughly; more so than I would have done otherwise. In itself, this has
been a genuine learning experience and I have been able to put some key lessons
into practice in the production of this document. So there we are, a few useful
bits of information to keep referring back to as and when.

.. Text replacements
.. |RST| replace:: reStructuredText
.. Footnotes
.. [#] This may also be useful for other people.
.. [#] Not being a CSS expert, this explanation might be simplistic, or even
    plain wrong but that is pretty much how I understand it at this stage.
.. [#] In fact, I find them so useful that they are left behind in completed
    articles, in perpetuity.
.. Links
.. _RST: http://docutils.sourceforge.net/rst.html
.. _`visit this very informative site`: http://en.wikibooks.org/wiki/LaTeX/Mathematics
.. _`Pygments`: http://pygments.org/
