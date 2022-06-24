from processor.core import replace_text, loop_replace_text, replace_file


def test_replace_text():
    text = """hello, world. This is \hl{highlighted text}. My fate, my Love."""
    removed_text= """hello, world. This is highlighted text. My fate, my Love."""
    assert removed_text == replace_text(text)


def test_loop_replace_text():
    text2 = """hello, world. This is \hl{highlighted text}. My fate, my Love. This is \hl{highlighted text}. My fate, my Love."""
    removed_text2 = """hello, world. This is highlighted text. My fate, my Love. This is highlighted text. My fate, my Love."""
    assert removed_text2 == loop_replace_text(text2)


def test_replace_file():
    res = replace_file('examples/hello.tex')
    assert res.find('\\hl') == -1
