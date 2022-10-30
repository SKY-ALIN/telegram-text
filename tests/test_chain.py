from telegram_text.bases import Chain
from telegram_text.styles import Bold, InlineCode, Italic, Spoiler


def test_chain_structure():
    bold = Bold("bold text")
    italic = Italic("italic text")
    code = InlineCode("Some code...")
    chain = Chain(bold, italic, code)

    assert isinstance(chain, Chain)
    assert bold in chain
    assert italic in chain
    assert code in chain

    assert chain.to_plain_text() == (
        bold.to_plain_text() + ' ' +
        italic.to_plain_text() + ' ' +
        code.to_plain_text()
    )
    assert chain.to_markdown() == (
        bold.to_markdown() + ' ' +
        italic.to_markdown() + ' ' +
        code.to_markdown()
    )
    assert chain.to_html() == (
        bold.to_html() + ' ' +
        italic.to_html() + ' ' +
        code.to_html()
    )


def test_add_magic_method():
    bold = Bold("bold text")
    italic = Italic("italic text")
    code = InlineCode("Some code...")
    chain = bold + italic
    chain += code

    assert Chain(bold, italic, code) == chain
    assert bold in chain
    assert italic in chain
    assert code in chain


def test_nested_styles_combination():
    combination = Bold("Bold") + "and" + Italic("italic")

    assert combination.to_plain_text() == "Bold and italic"
    assert combination.to_markdown() == "*Bold* and _italic_"

    obj = Spoiler(combination)

    assert obj.to_plain_text() == "Bold and italic"
    assert obj.to_markdown() == "||*Bold* and _italic_||"


def test_reverse():
    obj = "s1" + Italic("e")
    obj = "s2" + obj
    assert isinstance(obj, Chain)
    assert obj.to_plain_text() == "s2 s1 e"
