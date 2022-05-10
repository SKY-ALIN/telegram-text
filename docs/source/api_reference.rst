API Reference
=============

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
^^^^^^^^^^^^^
.. autoclass:: telegram_text.markdown.OrderedList
   :members:
   :show-inheritance:


telegram\_text.custom module
----------------------------

.. automodule:: telegram_text.custom
   :members:
   :undoc-members:
   :show-inheritance:
