from telegram_text.markdown import OrderedList, UnorderedList
from telegram_text.styles import Bold, PlainText, Underline


def test_ordered_list():
    assert OrderedList(
        PlainText("First line"),
        PlainText("Second line"),
        PlainText("Third line"),
    ).to_plain_text() == (
        "1. First line\n"
        "2. Second line\n"
        "3. Third line"
    )
    assert OrderedList(
        Underline("First line"),
        Underline("Second line"),
        Underline("Third line"),
        style=Bold,
        sep='\n\n'
    ).to_markdown() == (
        "*1\\.* __First line__\n\n"
        "*2\\.* __Second line__\n\n"
        "*3\\.* __Third line__"
    )


def test_unordered_list():
    assert UnorderedList(
        PlainText("First line"),
        PlainText("Second line"),
        PlainText("Third line"),
    ).to_plain_text() == (
        "* First line\n"
        "* Second line\n"
        "* Third line"
    )
    assert UnorderedList(
        Underline("First line"),
        Underline("Second line"),
        Underline("Third line"),
        sep='\n\n'
    ).to_markdown() == (
        "*\\** __First line__\n\n"
        "*\\** __Second line__\n\n"
        "*\\** __Third line__"
    )
