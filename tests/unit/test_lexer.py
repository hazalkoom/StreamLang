import pytest
from antlr4 import InputStream
from streamlang.parser.StreamLangLexer import StreamLangLexer

def tokenize(code):
    input_stream = InputStream(code)
    lexer = StreamLangLexer(input_stream)
    # getAllTokens loads all tokens into a list
    return [t.type for t in lexer.getAllTokens()]

def test_lexer_keywords():
    # 1. Test basic keywords
    tokens = tokenize("var let if while function")
    
    # We check against the Integer IDs Antlr assigns. 
    # You might need to check StreamLangLexer.py to see exact names if this fails,
    # but usually: VAR, LET, IF, WHILE, FUNCTION are attributes of the Lexer class.
    
    assert len(tokens) == 5
    assert tokens[0] == StreamLangLexer.VAR
    assert tokens[1] == StreamLangLexer.LET
    assert tokens[2] == StreamLangLexer.IF

def test_lexer_operators():
    # 2. Test operators sticking together
    tokens = tokenize("== != >=")
    assert tokens[0] == StreamLangLexer.EQ
    assert tokens[1] == StreamLangLexer.NEQ
    assert tokens[2] == StreamLangLexer.GTE

def test_lexer_identifiers_vs_strings():
    # 3. Test that "text" is string, but text is identifier
    tokens = tokenize('"hello" hello')
    assert tokens[0] == StreamLangLexer.STRING
    assert tokens[1] == StreamLangLexer.ID

def test_lexer_comments():
    # 4. Comments should be skipped (not produce tokens)
    tokens = tokenize("var // this is ignored\n x")
    # Should be VAR, ID (x)
    assert len(tokens) == 2
    assert tokens[0] == StreamLangLexer.VAR
    assert tokens[1] == StreamLangLexer.ID