from telegram_text.elements import Hashtag, Link
from telegram_text.bases import PlainText
from telegram_text.styles import Bold, Italic


def test_link():
    assert Link("link text", "https://Alinsky.tech/").to_markdown() == "[link text](https://Alinsky.tech/)"
    assert Link("link text", "https://Alinsky.tech/").to_html() == '<a href="https://Alinsky.tech/">link text</a>'


def test_hashtag_creation():
    assert Hashtag("hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("#hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("hashtag").to_markdown() == "#hashtag"
    assert Hashtag("#hashtag").to_markdown() == "#hashtag"
    assert Hashtag("hashtag").to_html() == "#hashtag"
    assert Hashtag("#hashtag").to_html() == "#hashtag"


def test_hashtag_style_fabric():
    assert Hashtag("hashtag", style=PlainText).to_markdown() == "#hashtag"
    assert Hashtag("hashtag", style=Bold).to_markdown() == "*#hashtag*"
    assert Hashtag("hashtag", style=Italic).to_markdown() == "_#hashtag_"
    assert Hashtag("hashtag", style=lambda string: Bold(Italic(string))).to_markdown() == "*_#hashtag_*"
    assert Hashtag("hashtag", style=lambda string: Bold(Italic(string))).to_plain_text() == "#hashtag"


def test_hashtag_main_styling():
    assert Bold(Hashtag("hashtag")).to_markdown() == "*#hashtag*"
    assert Italic(Hashtag("hashtag")).to_markdown() == "_#hashtag_"
    assert Bold(Italic(Hashtag("hashtag"))).to_markdown() == "*_#hashtag_*"
    assert Bold(Italic(Hashtag("hashtag"))).to_plain_text() == "#hashtag"
