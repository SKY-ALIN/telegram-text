API Reference
=============

You can import as :code:`from telegram_text import ...` following elements:

* :class:`telegram_text.bases.Chain`
* :class:`telegram_text.bases.PlainText`
* :class:`telegram_text.styles.Bold`
* :class:`telegram_text.styles.Code`
* :class:`telegram_text.styles.InlineCode`
* :class:`telegram_text.styles.Italic`
* :class:`telegram_text.styles.Spoiler`
* :class:`telegram_text.styles.Strikethrough`
* :class:`telegram_text.styles.Underline`
* :class:`telegram_text.elements.Hashtag`
* :class:`telegram_text.elements.InlineUser`
* :class:`telegram_text.elements.Link`
* :class:`telegram_text.elements.User`
* :class:`telegram_text.markdown.OrderedList`
* :class:`telegram_text.markdown.UnorderedList`
* :class:`telegram_text.custom.TOMLSection`


telegram\_text.bases
--------------------
.. automodule:: telegram_text.bases
   :exclude-members: AbstractElement, Element, Text, PlainText, Chain

AbstractElement
^^^^^^^^^^^^^^^
.. autoclass:: telegram_text.bases.AbstractElement
   :members:
   :show-inheritance:
   :special-members: __add__

Element
^^^^^^^
.. autoclass:: telegram_text.bases.Element
   :members:
   :show-inheritance:
   :special-members: __add__, __eq__, __str__

Text
^^^^
.. autoclass:: telegram_text.bases.Text
   :members:
   :show-inheritance:

PlainText
^^^^^^^^^
.. autoclass:: telegram_text.bases.PlainText
   :members:
   :show-inheritance:

Chain
^^^^^
.. autoclass:: telegram_text.bases.Chain
   :members:
   :show-inheritance:
   :special-members: __contains__


telegram\_text.styles
---------------------

Style
^^^^^
.. autoclass:: telegram_text.styles.Style
   :members:
   :show-inheritance:

Bold
^^^^
.. autoclass:: telegram_text.styles.Bold
   :members:
   :show-inheritance:

Italic
^^^^^^
.. autoclass:: telegram_text.styles.Italic
   :members:
   :show-inheritance:

Underline
^^^^^^^^^
.. autoclass:: telegram_text.styles.Underline
   :members:
   :show-inheritance:

Strikethrough
^^^^^^^^^^^^^
.. autoclass:: telegram_text.styles.Strikethrough
   :members:
   :show-inheritance:

Spoiler
^^^^^^^
.. autoclass:: telegram_text.styles.Spoiler
   :members:
   :show-inheritance:

InlineCode
^^^^^^^^^^
.. autoclass:: telegram_text.styles.InlineCode
   :members:
   :show-inheritance:

Code
^^^^
.. autoclass:: telegram_text.styles.Code
   :members:
   :show-inheritance:


telegram\_text.elements
-----------------------

.. automodule:: telegram_text.elements
   :exclude-members: Link, InlineUser, User, Hashtag

Link
^^^^
.. autoclass:: telegram_text.elements.Link
   :members:
   :show-inheritance:

InlineUser
^^^^^^^^^^
.. autoclass:: telegram_text.elements.InlineUser
   :members:
   :show-inheritance:

User
^^^^
.. autoclass:: telegram_text.elements.User
   :members:
   :show-inheritance:

Hashtag
^^^^^^^
.. autoclass:: telegram_text.elements.Hashtag
   :members:
   :show-inheritance:


telegram\_text.markdown
-----------------------

.. automodule:: telegram_text.markdown
   :exclude-members: UnorderedList, OrderedList

UnorderedList
^^^^^^^^^^^^^
.. autoclass:: telegram_text.markdown.UnorderedList
   :members:
   :show-inheritance:

OrderedList
^^^^^^^^^^^
.. autoclass:: telegram_text.markdown.OrderedList
   :members:
   :show-inheritance:


telegram\_text.custom
---------------------

.. automodule:: telegram_text.custom
   :exclude-members: TOMLSection

TOMLSection
^^^^^^^^^^^
.. autoclass:: telegram_text.custom.TOMLSection
   :members:
   :show-inheritance:
