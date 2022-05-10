Module API Usage
================

Any element from this module inherent following interface:

.. autoclass:: telegram_text.bases.AbstractElement
   :noindex:
   :members:
   :show-inheritance:
   :special-members: __add__

Let's discuss with examples every function.

``__add__``
-----------

This is a magic method that let us sum elements e.g.

.. code-block:: python

   >>> text = Bold("Hello") + Italic("world") + "!!!"
   >>> text
   <Chain: <Bold: 'Hello'> + <Italic: 'world'> + <PlainText: '!!!'>, sep=' '>

.. note::
   You can sum any element object with :obj:`str`, then :obj:`str` will be
   wrapped with :class:`telegram_text.bases.PlainText`, as in this case with
   ``"!!!"``.

As a result, we get a :class:`telegram_text.bases.Chain` object.

:class:`telegram_text.bases.Chain`
----------------------------------

Chain is a combination of a few elements. We get this element when summing a
few elements. This element has the same interface and it let us use following
functions:

``to_plain_text()``
-------------------

Format the element to plain text without escaping, tags or special characters.
It's a good method for debugging or logging, but don't use it with Telegram API
because it doesn't have escaping, so Telegram API may reject you.

.. note::
   If you have some element with styles and you want to send it to
   Telegram without styling just use this construction:

   .. code-block:: python

      >>> PlainText(text).to_markdown()
      'Hello world \\!\\!\\!'

   It'll add an escaping.

``to_markdown()``
-----------------

This function formats the element to Markdown/MarkdownV2 format according to
`Telegram specification <https://core.telegram.org/bots/api#markdownv2-style>`_
with escaping if necessary.

.. code-block:: python

   >>> text.to_markdown()
   '*Hello* _world_ \\!\\!\\!'

``to_html()``
-------------

This function formats the element to html according to
`Telegram specification <https://core.telegram.org/bots/api#html-style>`_.

.. code-block:: python

   >>> text.to_html()
   '<b>Hello</b> <i>world</i> !!!'

----

To discover all available elements see :ref:`api-reference`.

.. toctree::
   :hidden:

   self
   telebot_example
