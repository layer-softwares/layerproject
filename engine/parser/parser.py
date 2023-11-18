class Node:
    def __init__(self, tok_type, children=None, leaf=None):
        self.type = tok_type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf


class Parser:
    def __init__(self, lexed_tokens):
        self.lexed_tokens = lexed_tokens
        self.index = 0

    def parse(self):
        return self.program()

    def program(self):
        children = []
        while self.index < len(self.lexed_tokens):
            children.append(self.statement())
        return Node('PROGRAM', children)

    def statement(self):
        token = self.lexed_tokens[self.index]
        if token['type'] == 'KEYWORD':
            return self.keyword_statement()
        # Add more cases as needed for your language
        else:
            raise Exception(f'Unexpected token type: {token["type"]}')

    def keyword_statement(self):
        keyword = self.lexed_tokens[self.index]['value']
        self.index += 1
        if keyword == 'cvar':
            name = self.lexed_tokens[self.index]['value']
            self.index += 1
            if self.lexed_tokens[self.index]['value'] == '=':
                self.index += 1
                value = self.expression()
                return Node('cvar', [Node('IDENTIFIER', leaf=name), Node('EQUALS'), value])
            else:
                raise Exception('Expected "=" after variable name')
        else:
            return Node('KEYWORD_STATEMENT', [Node('KEYWORD', leaf=keyword)])

    def expression(self):
        # This method should parse an expression and return a Node representing it.
        # For now, let's just handle numbers, strings, and booleans.
        token = self.lexed_tokens[self.index]
        self.index += 1
        if token['type'] == 'NUMBER':
            return Node('NUMBER', leaf=float(token['value']))
        elif token['type'] == 'STRING':
            return Node('STRING', leaf=token['value'][1:-1])  # remove quotes
        elif token['type'] == 'BOOLEAN':
            return Node('BOOLEAN', leaf=token['value'] == 'T')
        else:
            raise Exception(f'Unexpected token type: {token["type"]}')


