from telegram_text.elements import Hashtag
from telegram_text.bases import PlainText
from telegram_text.styles import Bold, Italic


def test_creation():
    assert Hashtag("hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("#hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("hashtag").to_markdown() == "#hashtag"
    assert Hashtag("#hashtag").to_markdown() == "#hashtag"
    assert Hashtag("hashtag").to_html() == "#hashtag"
    assert Hashtag("#hashtag").to_html() == "#hashtag"


def test_style_fabric():
    assert Hashtag("hashtag", style_fabric=PlainText).to_markdown() == "#hashtag"
    assert Hashtag("hashtag", style_fabric=Bold).to_markdown() == "*#hashtag*"
    assert Hashtag("hashtag", style_fabric=Italic).to_markdown() == "_#hashtag_"
    assert Hashtag("hashtag", style_fabric=lambda string: Bold(Italic(string))).to_markdown() == "*_#hashtag_*"
    assert Hashtag("hashtag", style_fabric=lambda string: Bold(Italic(string))).to_plain_text() == "#hashtag"
