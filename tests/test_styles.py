from telegram_text.bases import PlainText
from telegram_text.styles import (
    Bold,
    Code,
    InlineCode,
    Italic,
    Spoiler,
    Strikethrough,
    Underline,
)

testing_string = "Hello world"


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

    obj = Italic(Italic(Italic(testing_string)))
    assert obj.to_markdown() == '_' + testing_string + '_'


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


def test_spoiler():
    obj = Spoiler(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '||' + testing_string + '||'
    assert obj.to_markdown() == '||' + testing_string + '||'
    assert obj.to_html() == '<span class="tg-spoiler">' + testing_string + '</span>'


def test_inline_code():
    obj = InlineCode(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '`' + testing_string + '`'
    assert obj.to_markdown() == '`' + testing_string + '`'
    assert obj.to_html() == '<code>' + testing_string + '</code>'


def test_code_block():
    obj = Code(testing_string)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == '```\n' + testing_string + '```'
    assert obj.to_markdown() == '```\n' + testing_string + '```'
    assert obj.to_html() == '<pre>' + testing_string + '</pre>'


def test_code_block_with_language():
    language = 'python'
    obj = Code(testing_string, language=language)
    assert obj.text.to_plain_text() == testing_string
    assert obj.to_plain_text() == testing_string
    assert str(obj) == f'```{language}\n' + testing_string + '```'
    assert obj.to_markdown() == f'```{language}\n' + testing_string + '```'
    assert obj.to_html() == f'<pre><code class="language-{language}">' + testing_string + '</code></pre>'
