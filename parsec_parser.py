import sys
sys.path.insert(0, "../..")


tokens = (
    "IDENTIFIER",
    "NUM_CONST",
    "STRING_LITERAL",
    "VALVE",
    "SENSOR",
    "COMMA",
    "IF",
    "ELSE",
    "PARALLEL",
    "RUN",
    "BREAK",
    "WAIT",
    "WAIT_UNTIL",
    "READ",
    "OPEN",
    "CLOSE",
    "ROUTINE",
    "EMERGENCY",
    "ABORT",
    "MAIN",
    "CHECKS",
    "LOG",
    "LOG_ERR",
    "REL_TIME",
    "LEFT_OP",
    "RIGHT_OP",
    "LPAREN",
    "RPAREN",
    "LCURLY",
    "RCURLY",
    "PLUS",
    "MINUS",
    "TIMES",
    "OR_OP",
    "DIVIDE",
    "MOD",
    "BOOL_OR_OP",
    "BOOL_AND_OP",
    "AND_OP",
    "CIRCUMFLEX",
    "EQ_OP",
    "NE_OP",
    "LT_OP",
    "LE_OP",
    "GT_OP",
    "GE_OP",
    "NOT",
    "SEMICOLON"
)

t_NUM_CONST = (
    r"0[xX][a-fA-F0-9]+|"
    r"\d+|"
    r"\d+\.\d*|"
    r"\d*\.\d+"
)
t_VALVE = "valve"
t_SENSOR = "sensor"
t_COMMA = "comma"
t_IF = "if"
t_ELSE = "else"
t_PARALLEL = "parallel"
t_RUN = "run"
t_BREAK = "break"
t_WAIT = "wait"
t_WAIT_UNTIL = "wait_until"
t_READ = "read"
t_OPEN = "open"
t_CLOSE = "close"
t_ROUTINE = "routine"
t_EMERGENCY = "emergency"
t_ABORT = "abort"
t_MAIN = "main"
t_CHECKS = "checks"
t_LOG = "log"
t_LOG_ERR = "log_err"
t_REL_TIME = "rel_time"
t_LEFT_OP = "<<"
t_RIGHT_OP = ">>"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LCURLY = r"\{"
t_RCURLY = r"\}"
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = "/"
t_MOD = "%"
t_BOOL_OR_OP = "\\|\\|"
t_BOOL_AND_OP = "\\&\\&"
t_OR_OP = "\\|"
t_AND_OP = "\\&"
t_CIRCUMFLEX = "\\^"
t_EQ_OP = "=="
t_NE_OP = "!="
t_LT_OP = "<"
t_LE_OP = "<="
t_GT_OP = ">"
t_GE_OP = ">="
t_NOT   = "~"
t_SEMICOLON = ";"

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex(debug=1)

# Parsing rules

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

#parsing below here
def p_translation_unit(p):
    """
    translation_unit    : routine_declaration
                        | translation_unit routine_declaration
    """
    print('translation_unit')

def p_routine_declaration(p):
    """
    routine_declaration : ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY routine_body RCURLY
                        | ROUTINE MAIN LPAREN valve_list RPAREN LCURLY main_routine_body RCURLY
                        | ROUTINE CHECKS LPAREN RPAREN LCURLY checks_routine_body RCURLY
                        | EMERGENCY ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY emergency_routine_body RCURLY
    """
    print("routine ", p[1])
    print("valves: ",end="")

def p_valve_list(p):
    """
    valve_list  : %empty
                | VALVE
                | valve_list COMMA VALVE
    """
    if len(p)>1:
        print(p[len(p)-1],end=", ")

def p_routine_body(p):
    """
    routine_body    : %empty
                    | serial_statement routine_body
    """
    print("routine line")

def p_main_routine_body(p):
    """
    main_routine_body   : routine_body
    """
    print("main")

def p_emergency_routine_body(p):
    """
    emergency_routine_body  : routine_body
    """
    print("emergency")

def p_checks_routine_body(p):
    """
    checks_routine_body : routine_body
    """
    print("checks")

def p_serial_statement(p):
    """
    serial_statement    : parallel_block
                        | run_statement
                        | conditional_block
                        | wait_statement
                        | wait_until_statement
                        | open_statement
                        | close_statement
                        | log_statement
                        | log_err_statement
                        | break_statement
                        | abort_statement
    """
    pass

def p_expression(p):
    """
    expression  : READ VALVE
                | READ SENSOR
                | REL_TIME
                | NUM_CONST
    """
    for i in range(1,len(p)):
        print(p[i])

def p_parallel_block(p):
    """
    parallel_block  : PARALLEL LCURLY parallel_list RCURLY
    """
    print("parallel")


def on_parallel_list(self, target, option, names, values):
    """
    parallel_list   : run_statement parallel_list
                    | run_statement
    """
    pass

def p_run_statement(p):
    """
    run_statement   : RUN IDENTIFIER SEMICOLON
    """
    print(p[1],p[2])

def p_conditional_block(p):
    """
    conditional_block   : IF conditional_expression LCURLY routine_body RCURLY
                        | IF conditional_expression LCURLY routine_body RCURLY ELSE conditional_block
                        | IF conditional_expression LCURLY routine_body RCURLY ELSE LCURLY routine_body RCURLY
    """
    if len(p)<=6:
        print("if")
    elif len(p)<=8:
        print("else if")
    else:
        print("else")

def p_wait_statement(p):
    """
    wait_statement  : WAIT NUM_CONST SEMICOLON
    """
    print(p[1]," ",p[2])

def p_wait_until_statement(p):
    """
    wait_until_statement    : WAIT_UNTIL conditional_expression SEMICOLON
    """
    print("wait until")

def p_open_statement(p):
    """
    open_statement  : OPEN VALVE SEMICOLON
    """
    print(p[1]," ",p[2])

def p_close_statement(p):
    """
    close_statement : CLOSE VALVE SEMICOLON
    """
    print(p[1]," ",p[2])

def p_log_statement(p):
    """
    log_statement   : LOG log_value SEMICOLON
    """
    print("log")

def p_log_err_statement(p):
    """
    log_err_statement   : LOG_ERR log_value SEMICOLON
    """
    print("log_error")

def p_log_value(p):
    """
    log_value   : STRING_LITERAL
                | conditional_expression
                | log_value PLUS log_value
    """
    if type(p[1]) is str:
        print(p[1])

def p_break_statement(p):
    """
    break_statement : BREAK STRING_LITERAL SEMICOLON
    """
    print(p[1], p[2])

def p_abort_statement(p):
    """
    abort_statement : ABORT SEMICOLON
    """
    print("abort")

def p_primary_expression(p):
    """
    primary_expression  : expression
                        | LPAREN conditional_expression RPAREN
    """
    pass

def on_unary_expression(self, target, option, names, values):
    """
    unary_expression    : primary_expression
                        | MINUS primary_expression
    """
    if len(p)>2:
        print("-",end="")

def on_multiplicative_expression(self, target, option, names, values):
    """
    multiplicative_expression   : unary_expression
                                | multiplicative_expression TIMES unary_expression
                                | multiplicative_expression DIVIDE unary_expression
                                | multiplicative_expression MOD unary_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
        print(p[1] + "*" + p[3])
    elif p[2] == '/':
        p[0] = p[1] / p[3]
        print(p[1] + "/" + p[3])
    elif p[2] == '%':
        p[0] = p[1] % p[3]
        print(p[1] + "%" + p[3])
    else:
        print("help me I'm a dumbass multiplicative_expression")


def on_additive_expression(self, target, option, names, values):
    """
    additive_expression : multiplicative_expression
                        | additive_expression PLUS multiplicative_expression
                        | additive_expression MINUS multiplicative_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
        print(p[1] + "+" + p[3])
    elif p[2] == '-':
        p[0] = p[1] - p[3]
        print(p[1] + "-" + p[3])
    else:
        print("help me I'm a dumbass additive_expression")

def on_shift_expression(self, target, option, names, values):
    """
    shift_expression    : additive_expression
                        | shift_expression LEFT_OP additive_expression
                        | shift_expression RIGHT_OP additive_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '<<':
        p[0] = p[1] << p[3]
        print(p[1] + "<<" + p[3])
    elif p[2] == '>>':
        p[0] = p[1] >> p[3]
        print(p[1] + ">>" + p[3])
    else:
        print("help me I'm a dumbass shift_expression")

def on_relational_expression(self, target, option, names, values):
    """
    relational_expression   : shift_expression
                            | relational_expression LT_OP shift_expression
                            | relational_expression GT_OP shift_expression
                            | relational_expression LE_OP shift_expression
                            | relational_expression GE_OP shift_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
        print(p[1] + "<" + p[3])
    elif p[2] == '>':
        p[0] = p[1] > p[3]
        print(p[1] + ">" + p[3])
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
        print(p[1] + "<=" + p[3])
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
        print(p[1] + ">=" + p[3])
    else:
        print("help me I'm a dumbass relational_expression")

def on_equality_expression(self, target, option, names, values):
    """
    equality_expression : relational_expression
                        | equality_expression EQ_OP relational_expression
                        | equality_expression NE_OP relational_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
        print(p[1] + "==" + p[3])
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
        print(p[1] + "!=" + p[3])
    else:
        print("help me I'm a dumbass equality_expression")

def on_and_expression(self, target, option, names, values):
    """
    and_expression  : equality_expression
                    | and_expression AND_OP equality_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '&':
        p[0] = p[1] & p[3]
        print(p[1] + "&" + p[3])
    else:
        print("help me I'm a dumbass on_and_expression")

def on_exclusive_or_expression(self, target, option, names, values):
    """
    exclusive_or_expression : and_expression
                            | exclusive_or_expression CIRCUMFLEX and_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '^':
        p[0] = p[1] ^ p[3]
        print(p[1] + "^" + p[3])
    else:
        print("help me I'm a dumbass exclusive_or_expression")

def on_inclusive_or_expression(self, target, option, names, values):
    """
    inclusive_or_expression : exclusive_or_expression
                            | inclusive_or_expression OR_OP exclusive_or_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '|':
        p[0] = p[1] | p[3]
        print(p[1] + "|" + p[3])
    else:
        print("help me I'm a dumbass inclusive_or_expression")

def on_logical_and_expression(self, target, option, names, values):
    """
    logical_and_expression  : inclusive_or_expression
                            | logical_and_expression BOOL_AND_OP inclusive_or_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '&&':
        p[0] = p[1] and p[3]
        print(p[1] + "&&" + p[3])
    else:
        print("help me I'm a dumbass logical_and_expression")

def on_logical_or_expression(self, target, option, names, values):
    """
    logical_or_expression   : logical_and_expression
                            | logical_or_expression BOOL_OR_OP logical_and_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '||':
        p[0] = p[1] or p[3]
        print(p[1] + "||" + p[3])
    else:
        print("help me I'm a dumbass logical_or_expression")

def on_conditional_expression(self, target, option, names, values):
    """
    conditional_expression  : logical_or_expression
                            | NOT logical_or_expression
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '~':
        p[0] = ~ p[2]
        print("~" + p[2])
    else:
        print("help me I'm a dumbass conditional_expression")


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

if __name__ == "__main__":
    lex.runmain()
