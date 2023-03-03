TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'

TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_DIV = 'TT_DIV'
TT_MUL = 'TT_MUL'

TT_LPAREN ='TT_LPAREN'
TT_RPAREN ='TT_RPAREN'

DIGITS  = '0123456789'

class Token:
    def __init__(self, type_, value=None) -> None:
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'