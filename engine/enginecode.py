class Interpreter:
    def __init__(self, parse_tree):
        self.parse_tree = parse_tree
        self.variables = {}

    def interpret(self):
        self.visit(self.parse_tree)

    def visit(self, node):
        method_name = f'visit_{node.type}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{node.type} method defined')

    def visit_PROGRAM(self, node):
        for child in node.children:
            self.visit(child)

    def visit_KEYWORD_STATEMENT(self, node):
        keyword = node.children[0].leaf
        if keyword == 'cvar':
            self.visit_cvar(node)

    def visit_cvar(self, node):
        name = node.children[1].leaf
        value = self.visit(node.children[3])
        self.variables[name] = value
