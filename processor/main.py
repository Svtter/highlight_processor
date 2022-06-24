import argparse
import sys
from .core import loop_replace_text, replace_file


def cli():
    parser = argparse.ArgumentParser('highlight handle tools')
    parser.add_argument('--file', type=str, help='The file need to handle.')

    args = parser.parse_args()

    if args.file:
        replace_file(args.file)
        print('Well done.')
    else:
        def fun():
            input_text = sys.stdin.read()
            res = loop_replace_text(input_text)
            print('EOF<<<')
            print(res)

        # Enter REPL
        print('Input>>> ')
        fun()


