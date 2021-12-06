import ast
import inspect


def source(o):
    s = inspect.getsource(o).split("\n")
    indent = len(s[0]) - len(s[0].lstrip())
    return "\n".join(i[indent:] for i in s)


class Patcher:
    def __init__(self, module):
        self.tree = ast.parse(source(module))
        self.module = module

    def apply(self):
        self.tree = ast.fix_missing_locations(self.tree)
        exec(compile(self.tree, "<ast>", "exec"), self.module.__dict__)
