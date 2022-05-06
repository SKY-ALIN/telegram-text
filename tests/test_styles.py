from telegram_text.styles import (
    Bold,
    PlainText,
    Italic,
    Underline,
    Strikethrough,
)

testing_string = "Hello world!"


def test_plain_text():
    obj = PlainText(testing_string)
    assert obj.text == testing_string
    assert str(obj) == testing_string
    assert obj.to_plain_text() == testing_string
    assert obj.to_markdown() == testing_string
    assert obj.to_html() == testing_string


def test_bold():
    obj = Bold(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '*' + testing_string + '*'
    assert obj.to_markdown() == '*' + testing_string + '*'
    assert obj.to_html() == '<b>' + testing_string + '</b>'


def test_italic():
    obj = Italic(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '_' + testing_string + '_'
    assert obj.to_markdown() == '_' + testing_string + '_'
    assert obj.to_html() == '<i>' + testing_string + '</i>'


def test_underline():
    obj = Underline(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '__' + testing_string + '__'
    assert obj.to_markdown() == '__' + testing_string + '__'
    assert obj.to_html() == '<u>' + testing_string + '</u>'


def test_strikethrough():
    obj = Strikethrough(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '~' + testing_string + '~'
    assert obj.to_markdown() == '~' + testing_string + '~'
    assert obj.to_html() == '<s>' + testing_string + '</s>'
