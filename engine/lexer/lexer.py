class Lexer:
    def __init__(self, token_stream):
        self.token_stream = token_stream

    def lex(self):
        lexed_tokens = []
        for token in self.token_stream:
            lexed_tokens.append({
                'type': token[0],
                'value': token[1]
            })
        return lexed_tokens
