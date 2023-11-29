import sys
from clingo import Control


class AspifSymbolicPrinter:
    def print(self):
        pass


class AspifPrinter:
    def print(self):
        pass


if __name__ == "__main__":

    if sys.argv[1] == "--help":
        print("""
    Run:\n  python aspif-pretty-printer.py [--text] <files>
    """)
        sys.exit()

    path = sys.argv[1:]
    printer = AspifPrinter()
    if len(path)>0 and path[0] == "--text":
        path = sys.argv[2:]
        printer = AspifSymbolicPrinter()

    ctl = Control()
    for file_ in path:
        ctl.load(file_)
    if not path:
        ctl.load("-")
    ctl.register_observer(printer)
    ctl.ground([("base", [])])
    printer.print()

