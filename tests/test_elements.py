from telegram_text.elements import Hashtag


def test_creation():
    assert Hashtag("hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("#hashtag").to_plain_text() == "#hashtag"
    assert Hashtag("hashtag").to_markdown() == "#hashtag"
    assert Hashtag("#hashtag").to_markdown() == "#hashtag"
    assert Hashtag("hashtag").to_html() == "#hashtag"
    assert Hashtag("#hashtag").to_html() == "#hashtag"
