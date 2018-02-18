from enum import Enum


# TODO: ternary, four space indention, streams
class Type(Enum):
    BLOCK_COMMENT = "(/\\*.*?\\*/).*"
    LINE_COMMENT = "(//(.*?)[\r$]?\n).*"
    WHITE_SPACE = "( ).*"
    OPEN_BRACE = "(\\().*"
    CLOSE_BRACE = "(\\)).*"
    SEMICOLON = "(;).*"
    COMMA = "(,).*"
    OPEN_CURLY_BRACE = "(\\{).*"
    CLOSE_CURLY_BRACE = "(\\}).*"
    DOUBLE_CONSTANT = "\\b(\\d{1,9}\\.\\d{1,32})\\b.*"
    INT_CONSTANT = "\\b(\\d{1,9})\\b.*"
    VOID = "\\b(void)\\b.*"
    INT = "\\b(int)\\b.*"
    DOUBLE = "\\b(int|double)\\b.*"
    TAB = "(\\t).*"
    NEW_LINE = "(\\n).*"
    PUBLIC = "\\b(public)\\b.*"
    PRIVATE = "\\b(private)\\b.*"
    FALSE = "\\b(false)\\b.*"
    TRUE = "\\b(true)\\b.*"
    NULL = "\\b(null)\\b.*"
    RETURN = "\\b(return)\\b.*"
    NEW = "\\b(new)\\b.*"
    CLASS = "\\b(class)\\b.*"
    IF = "\\b(if)\\b.*"
    ELSE = "\\b(else)\\b.*"
    WHILE = "\\b(while)\\b.*"
    STATIC = "\\b(static)\\b.*"
    STRING = "\\b(String)\\b.*"
    CHAR = "\\b(char)\\b.*"
    FINAL = "\\b(final)\\b.*"
    ABSTRACT = "\\b(abstract)\\b.*"
    CONTINUE = "\\b(continue)\\b.*"
    FOR = "\\b(for)\\b.*"
    SWITCH = "\\b(switch)\\b.*"
    ASSERT = "\\b(assert)\\b.*"
    DEFAULT = "\\b(default)\\b.*"
    GOTO = "\\b(goto)\\b.*"
    PACKAGE = "\\b(package)\\b.*"
    SYNCHRONIZED = "\\b(synchronized)\\b.*"
    BOOLEAN = "\\b(boolean)\\b.*"
    DO = "\\b(do)\\b.*"
    THIS = "\\b(this)\\b.*"
    BYTE = "\\b(byte)\\b.*"
    IMPORT = "\\b(import)\\b.*"
    THROWS = "\\b(throws)\\b.*"
    BREAK = "\\b(break)\\b.*"
    IMPLEMENTS = "\\b(implements)\\b.*"
    PROTECTED = "\\b(protected)\\b.*"
    THROW = "\\b(throw)\\b.*"
    CASE = "\\b(case)\\b.*"
    ENUM = "\\b(enum)\\b.*"
    INSTANCEOF = "\\b(instanceof)\\b.*"
    TRANSIENT = "\\b(transient)\\b.*"
    CATCH = "\\b(catch)\\b.*"
    EXTENDS = "\\b(extends)\\b.*"
    SHORT = "\\b(short)\\b.*"
    TRY = "\\b(try)\\b.*"
    INTERFACE = "\\b(INTERFACE)\\b.*"
    FINALLY = "\\b(FINALLY)\\b.*"
    LONG = "\\b(LONG)\\b.*"
    STRICTFP = "\\b(strictfp)\\b.*"
    VOLATILE = "\\b(volatile)\\b.*"
    CONST = "\\b(const)\\b.*"
    FLOAT = "\\b(float)\\b.*"
    NATIVE = "\\b(native)\\b.*"
    super = "\\b(super)\\b.*"
    POINT = "(\\.).*"
    PLUS = "(\\+{1}).*"
    MINUS = "(\\-{1}).*"
    MULTIPLY = "(\\*).*"
    DIVIDE = "(/).*"
    EQUAL = "(==).*"
    ASSIGNMENT = "(=).*"
    NOT_EQUAL = "(\\!=).*"
    CLOSE_CARET = "(>).*"
    OPEN_CARET = "(<).*"
    IDENTIFIER = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"
    STRING_LITERAL = '\"(\\.|[^\\"])*\"'

