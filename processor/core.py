import pathlib


def locate_text(text: str):
    pos = text.find('\\hl{')
    rest_text = text[pos+3:]
    pos2 = rest_text.find('}')

    if pos2 == -1:
        return "", 0, 0

    end = pos+3+pos2+1
    inner_text = text[pos:end]

    return inner_text, pos, end


def replace_text(text: str) ->str:
    inner_text, pos, end = locate_text(text=text)
    if inner_text == "":
        return text
    text = text[:pos] + text[pos+4:end-1] + text[end:]
    return text


def loop_replace_text(text: str):
    while True:
        text_new = replace_text(text)
        if text_new == text:
            return text_new
        text = text_new


def replace_file(filename: str):
    fp = pathlib.Path(filename)
    with open(filename, 'r') as f:
        text = f.read()

    new_text = loop_replace_text(text)
    with open(fp.parent / (fp.name[:len(fp.suffix)] + '-copy.tex'), 'w') as f:
        f.write(new_text)
    return new_text
