from .Types import (
    Token,
    TT_INT, TT_FLOAT,
    TT_PLUS, TT_MINUS, TT_MUL, TT_DIV,
    TT_LPAREN, TT_RPAREN,
    DIGITS
)

from .Errors import Position, IllegalCharError


class Lexer:
    def __init__(self,fn,text) -> None:
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1,fn,text)
        self.current_char = None
        self.__advance()

    def __advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(
            self.text) else None

    def __make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.__advance()
        if dot_count == 0:
            return Token(type_=TT_INT, value=int(num_str))
        else:
            return Token(type_=TT_FLOAT, value=float(num_str))

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ['\t',' ']:
                self.__advance()
            if self.current_char in DIGITS:
                tokens.append(self.__make_number())
            elif self.current_char == '+':
                tokens.append(Token(type_=TT_PLUS))
                self.__advance()
            elif self.current_char == '-':
                tokens.append(Token(type_=TT_MINUS))
                self.__advance()
            elif self.current_char == '*':
                tokens.append(Token(type_=TT_MUL))
                self.__advance()
            elif self.current_char == '/':
                tokens.append(Token(type_=TT_DIV))
                self.__advance()
            elif self.current_char == '(':
                tokens.append(Token(type_=TT_LPAREN))
                self.__advance()
            elif self.current_char == ')':
                tokens.append(Token(type_=TT_RPAREN))
                self.__advance()
            else:
                post_start = self.pos.copy()
                char = self.current_char
                self.__advance()
                return [], IllegalCharError(post_start,self.pos,details=f"'{char}'")
        return tokens, None
