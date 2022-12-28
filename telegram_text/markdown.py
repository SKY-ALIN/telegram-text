"""Telegram markdown and official markdown standards are very different.
Telegram markdown has new elements and hasn't some main old elements from
the official markdown format. This file is a compromise that adds missing
elements to Telegram.
"""

from typing import Callable

from .bases import Chain, Element, NEW_LINE
from .styles import Bold, PlainText


class UnorderedList(Chain):
    """Unordered (bullet) list.

    Example:

    * First element.
    * Second element.
    * Third element.

    Args:
        elements (Tuple[Element]):
            Elements for the list. Every element is a single point.
        style (Callable[[str], Element]):
            Style factory that will be applied to every point
            (only special characters of list, not passed elements).
            :class:`telegram_text.styles.Bold` by default.
        sep (str):
            Separator between every point.
            :const:`telegram_text.bases.NEW_LINE` by default.
    """

    def __init__(self, *elements: Element, style: Callable[[str], Element] = Bold, sep: str = NEW_LINE):
        points = [
            style("*") + element
            for element in elements
        ]
        super().__init__(*points, sep=sep)


class OrderedList(Chain):
    """Ordered (numbered) list.

    Example:

    1. First element.
    2. Second element.
    3. Third element.

    Args:
        elements (Tuple[Element]):
            Elements for the list. Every element is a single point.
        style (Callable[[str], Element]):
            Style factory that will be applied to every point
            (only special characters of list, not passed elements).
            :class:`telegram_text.bases.PlainText` by default.
        sep (str):
            Separator between every point.
            :const:`telegram_text.bases.NEW_LINE` by default.
    """

    def __init__(self, *elements: Element, style: Callable[[str], Element] = PlainText, sep: str = NEW_LINE):
        points = [
            style(f"{n}.") + element
            for n, element in enumerate(elements, start=1)
        ]
        super().__init__(*points, sep=sep)
