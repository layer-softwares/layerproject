import re


class Tokenizer:
    def __init__(self):
        self.tokens = {
            'COMMENT': r'^\s*#.*$',
            'INDENT': r'^\s{4}.*$',
            'NEWLINE': r'^\n$',
            'WHITESPACE': r'^\s+$',
            'IDENTIFIER': r'^[a-zA-Z_][a-zA-Z0-9_]*$',
            'NUMBER': r'^[0-9]+(\.[0-9]+)?$',
            'STRING': r'^".*"$',
            'OPERATOR': r'^(\+|-|\*|/|%|\^|=|==|!=|<|>|<=|>=|and|or|not)$',
            'KEYWORD': r'^(cvar|ivar|if|else|while|for|break|continue|def|return|class|import|from|as)$',
            'PUNCTUATION': r'^(\.|,|:|\(|\)|\[|\]|\{|\})$',
            'BOOLEAN': r'^(true|false)$'
        }

    def tokenize(self, code):
        token_stream = []
        lines = code.split('\n')
        for line in lines:
            for token_type, regex in self.tokens.items():
                match = re.match(regex, line)
                if match:
                    token_stream.append((token_type, match.group()))
                    break
        return token_stream


# Test the tokenizer
if __name__ == '__main__':
    sourceCode = open("/Users/ajay/projectlayer/ly/zero.ly").read()
    tokenizer = Tokenizer()
    tok_stream = tokenizer.tokenize(sourceCode)

    print(tok_stream)
