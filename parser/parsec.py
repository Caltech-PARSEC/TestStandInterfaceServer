#!/usr/bin/env python

"""
PyBison file automatically generated from grammar file parsec.y
You can edit this module, or import it and subclass the Parser class
"""

import sys

from bison import BisonParser, BisonNode, BisonSyntaxError

bisonFile = 'parsec.y'  # original bison file
lexFile = 'parsec.l'    # original flex file

class Parser(BisonParser):
    """
    bison Parser class generated automatically by bison2py from the
    grammar file "parsec.y" and lex file "parsec.l"

    You may (and probably should) edit the methods in this class.
    You can freely edit the rules (in the method docstrings), the
    tokens list, the start symbol, and the precedences.

    Each time this class is instantiated, a hashing technique in the
    base class detects if you have altered any of the rules. If any
    changes are detected, a new dynamic lib for the parser engine
    will be generated automatically.
    """

    # -------------------------------------------------
    # Default class to use for creating new parse nodes
    # -------------------------------------------------
    defaultNodeClass = BisonNode

    # --------------------------------------------
    # basename of binary parser engine dynamic lib
    # --------------------------------------------
    bisonEngineLibName = 'parsec-engine'

    # ----------------------------------------------------------------
    # lexer tokens - these must match those in your lex script (below)
    # ----------------------------------------------------------------
    tokens = [['logical_or_expression'], ['NOT', 'logical_or_expression']]

    # ------------------------------
    # precedences
    # ------------------------------
    precedences = (
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        ('left', [['logical_or_expression'], ['NOT', 'logical_or_expression']],),
        )

    # ---------------------------------------------------------------
    # Declare the start target here (by name)
    # ---------------------------------------------------------------
    start = 'translation_unit'

    # ---------------------------------------------------------------
    # These methods are the python handlers for the bison targets.
    # (which get called by the bison code each time the corresponding
    # parse target is unambiguously reached)
    #
    # WARNING - don't touch the method docstrings unless you know what
    # you are doing - they are in bison rule syntax, and are passed
    # verbatim to bison to build the parser engine library.
    # ---------------------------------------------------------------

    def on_translation_unit(self, target, option, names, values):
        """
        translation_unit
            : routine_declaration
            | translation_unit routine_declaration
        """
        return self.defaultNodeClass(
            target='translation_unit',
            option=option,
            names=names,
            values=values)

    def on_routine_declaration(self, target, option, names, values):
        """
        routine_declaration
            : ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY routine_body RCURLY
            | ROUTINE MAIN LPAREN valve_list RPAREN LCURLY main_routine_body RCURLY
            | ROUTINE CHECKS LPAREN RPAREN LCURLY checks_routine_body RCURLY
            | EMERGENCY ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY emergency_routine_body RCURLY
        """
        return self.defaultNodeClass(
            target='routine_declaration',
            option=option,
            names=names,
            values=values)

    def on_valve_list(self, target, option, names, values):
        """
        valve_list
            : %empty
            | VALVE
            | valve_list COMMA VALVE
        """
        return self.defaultNodeClass(
            target='valve_list',
            option=option,
            names=names,
            values=values)

    def on_routine_body(self, target, option, names, values):
        """
        routine_body
            : %empty
            | serial_statement routine_body
        """
        return self.defaultNodeClass(
            target='routine_body',
            option=option,
            names=names,
            values=values)

    def on_main_routine_body(self, target, option, names, values):
        """
        main_routine_body
            : routine_body
        """
        return self.defaultNodeClass(
            target='main_routine_body',
            option=option,
            names=names,
            values=values)

    def on_emergency_routine_body(self, target, option, names, values):
        """
        emergency_routine_body
            : routine_body
        """
        return self.defaultNodeClass(
            target='emergency_routine_body',
            option=option,
            names=names,
            values=values)

    def on_checks_routine_body(self, target, option, names, values):
        """
        checks_routine_body
            : routine_body
        """
        return self.defaultNodeClass(
            target='checks_routine_body',
            option=option,
            names=names,
            values=values)

    def on_serial_statement(self, target, option, names, values):
        """
        serial_statement
            : parallel_block
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
        return self.defaultNodeClass(
            target='serial_statement',
            option=option,
            names=names,
            values=values)

    def on_expression(self, target, option, names, values):
        """
        expression
            : READ VALVE
            | READ SENSOR
            | REL_TIME
            | NUM_CONST
        """
        return self.defaultNodeClass(
            target='expression',
            option=option,
            names=names,
            values=values)

    def on_parallel_block(self, target, option, names, values):
        """
        parallel_block
            : PARALLEL LCURLY parallel_list RCURLY
        """
        return self.defaultNodeClass(
            target='parallel_block',
            option=option,
            names=names,
            values=values)

    def on_parallel_list(self, target, option, names, values):
        """
        parallel_list
            : run_statement parallel_list
            | run_statement
        """
        return self.defaultNodeClass(
            target='parallel_list',
            option=option,
            names=names,
            values=values)

    def on_run_statement(self, target, option, names, values):
        """
        run_statement
            : RUN IDENTIFIER SEMICOLON
        """
        return self.defaultNodeClass(
            target='run_statement',
            option=option,
            names=names,
            values=values)

    def on_conditional_block(self, target, option, names, values):
        """
        conditional_block
            : IF conditional_expression LCURLY routine_body RCURLY
            | IF conditional_expression LCURLY routine_body RCURLY ELSE conditional_block
            | IF conditional_expression LCURLY routine_body RCURLY ELSE LCURLY routine_body RCURLY
        """
        return self.defaultNodeClass(
            target='conditional_block',
            option=option,
            names=names,
            values=values)

    def on_wait_statement(self, target, option, names, values):
        """
        wait_statement
            : WAIT NUM_CONST SEMICOLON
        """
        return self.defaultNodeClass(
            target='wait_statement',
            option=option,
            names=names,
            values=values)

    def on_wait_until_statement(self, target, option, names, values):
        """
        wait_until_statement
            : WAIT_UNTIL conditional_expression SEMICOLON
        """
        return self.defaultNodeClass(
            target='wait_until_statement',
            option=option,
            names=names,
            values=values)

    def on_open_statement(self, target, option, names, values):
        """
        open_statement
            : OPEN VALVE SEMICOLON
        """
        return self.defaultNodeClass(
            target='open_statement',
            option=option,
            names=names,
            values=values)

    def on_close_statement(self, target, option, names, values):
        """
        close_statement
            : CLOSE VALVE SEMICOLON
        """
        return self.defaultNodeClass(
            target='close_statement',
            option=option,
            names=names,
            values=values)

    def on_log_statement(self, target, option, names, values):
        """
        log_statement
            : LOG log_value SEMICOLON
        """
        return self.defaultNodeClass(
            target='log_statement',
            option=option,
            names=names,
            values=values)

    def on_log_err_statement(self, target, option, names, values):
        """
        log_err_statement
            : LOG_ERR log_value SEMICOLON
        """
        return self.defaultNodeClass(
            target='log_err_statement',
            option=option,
            names=names,
            values=values)

    def on_log_value(self, target, option, names, values):
        """
        log_value
            : STRING_LITERAL
            | conditional_expression
            | log_value PLUS log_value
        """
        return self.defaultNodeClass(
            target='log_value',
            option=option,
            names=names,
            values=values)

    def on_break_statement(self, target, option, names, values):
        """
        break_statement
            : BREAK STRING_LITERAL SEMICOLON
        """
        return self.defaultNodeClass(
            target='break_statement',
            option=option,
            names=names,
            values=values)

    def on_abort_statement(self, target, option, names, values):
        """
        abort_statement
            : ABORT SEMICOLON
        """
        return self.defaultNodeClass(
            target='abort_statement',
            option=option,
            names=names,
            values=values)

    def on_primary_expression(self, target, option, names, values):
        """
        primary_expression
            : expression
            | LPAREN conditional_expression RPAREN
        """
        return self.defaultNodeClass(
            target='primary_expression',
            option=option,
            names=names,
            values=values)

    def on_unary_expression(self, target, option, names, values):
        """
        unary_expression
            : primary_expression
            | MINUS primary_expression
        """
        return self.defaultNodeClass(
            target='unary_expression',
            option=option,
            names=names,
            values=values)

    def on_multiplicative_expression(self, target, option, names, values):
        """
        multiplicative_expression
            : unary_expression
            | multiplicative_expression TIMES unary_expression
            | multiplicative_expression DIVIDE unary_expression
            | multiplicative_expression MOD unary_expression
        """
        return self.defaultNodeClass(
            target='multiplicative_expression',
            option=option,
            names=names,
            values=values)

    def on_additive_expression(self, target, option, names, values):
        """
        additive_expression
            : multiplicative_expression
            | additive_expression PLUS multiplicative_expression
            | additive_expression MINUS multiplicative_expression
        """
        return self.defaultNodeClass(
            target='additive_expression',
            option=option,
            names=names,
            values=values)

    def on_shift_expression(self, target, option, names, values):
        """
        shift_expression
            : additive_expression
            | shift_expression LEFT_OP additive_expression
            | shift_expression RIGHT_OP additive_expression
        """
        return self.defaultNodeClass(
            target='shift_expression',
            option=option,
            names=names,
            values=values)

    def on_relational_expression(self, target, option, names, values):
        """
        relational_expression
            : shift_expression
            | relational_expression LT_OP shift_expression
            | relational_expression GT_OP shift_expression
            | relational_expression LE_OP shift_expression
            | relational_expression GE_OP shift_expression
        """
        return self.defaultNodeClass(
            target='relational_expression',
            option=option,
            names=names,
            values=values)

    def on_equality_expression(self, target, option, names, values):
        """
        equality_expression
            : relational_expression
            | equality_expression EQ_OP relational_expression
            | equality_expression NE_OP relational_expression
        """
        return self.defaultNodeClass(
            target='equality_expression',
            option=option,
            names=names,
            values=values)

    def on_and_expression(self, target, option, names, values):
        """
        and_expression
            : equality_expression
            | and_expression AND_OP equality_expression
        """
        return self.defaultNodeClass(
            target='and_expression',
            option=option,
            names=names,
            values=values)

    def on_exclusive_or_expression(self, target, option, names, values):
        """
        exclusive_or_expression
            : and_expression
            | exclusive_or_expression CIRCUMFLEX and_expression
        """
        return self.defaultNodeClass(
            target='exclusive_or_expression',
            option=option,
            names=names,
            values=values)

    def on_inclusive_or_expression(self, target, option, names, values):
        """
        inclusive_or_expression
            : exclusive_or_expression
            | inclusive_or_expression OR_OP exclusive_or_expression
        """
        return self.defaultNodeClass(
            target='inclusive_or_expression',
            option=option,
            names=names,
            values=values)

    def on_logical_and_expression(self, target, option, names, values):
        """
        logical_and_expression
            : inclusive_or_expression
            | logical_and_expression BOOL_AND_OP inclusive_or_expression
        """
        return self.defaultNodeClass(
            target='logical_and_expression',
            option=option,
            names=names,
            values=values)

    def on_logical_or_expression(self, target, option, names, values):
        """
        logical_or_expression
            : logical_and_expression
            | logical_or_expression BOOL_OR_OP logical_and_expression
        """
        return self.defaultNodeClass(
            target='logical_or_expression',
            option=option,
            names=names,
            values=values)

    def on_conditional_expression(self, target, option, names, values):
        """
        conditional_expression
            : logical_or_expression
            | NOT logical_or_expression
        """
        return self.defaultNodeClass(
            target='conditional_expression',
            option=option,
            names=names,
            values=values)

    # -----------------------------------------
    # raw lex script, verbatim here
    # -----------------------------------------
    lexscript = r"""
D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS			(f|F|l|L)
IS			(u|U|l|L)*


%{

/* this scanner sourced from: http://www.lysator.liu.se/c/ANSI-C-grammar-l.html */

void count();
int yylineno = 0;
#include <stdio.h>
#include <string.h>
#include "Python.h"
#define YYSTYPE void *
#include "tokens.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) /*printf("%d=%s\n", tok, yytext);*/ yylval = PyString_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) { (*py_input)(py_parser, buf, &result, max_size); }

%}


%%
"/*"			{ comment(); }


"if"			{ count(); returntoken(IF); }
"else"			{ count(); returntoken(ELSE); }
"break"			{ count(); returntoken(BREAK); }
"parallel"		{ count(); returntoken(PARALLEL); }
"run"			{ count(); returntoken(RUN); }
"wait"			{ count(); returntoken(WAIT); }
"wait_until"		{ count(); returntoken(WAIT_UNTIL); }
"read"			{ count(); returntoken(READ); }
"open"			{ count(); returntoken(OPEN); }
"close"			{ count(); returntoken(CLOSE); }
"routine"		{ count(); returntoken(ROUTINE); }
"emergency"		{ count(); returntoken(EMERGENCY); }
"abort"			{ count(); returntoken(ABORT); }
"MAIN"			{ count(); returntoken(MAIN); }
"CHECKS"		{ count(); returntoken(CHECKS); }
"log"			{ count(); returntoken(LOG); }
"log_err"		{ count(); returntoken(LOG_ERR); }
"rel_time"		{ count(); returntoken(REL_TIME); }

{L}({L}|{D})*		{ count(); returntoken(check_type()); }

0[xX]{H}+{IS}?		{ count(); returntoken(NUM_CONST); }
0{D}+{IS}?		{ count(); returntoken(NUM_CONST); }
{D}+{IS}?		{ count(); returntoken(NUM_CONST); }
L?'(\\.|[^\\'])+'	{ count(); returntoken(NUM_CONST); }

{D}+{E}{FS}?		{ count(); returntoken(NUM_CONST); }
{D}*"."{D}+({E})?{FS}?	{ count(); returntoken(NUM_CONST); }
{D}+"."{D}*({E})?{FS}?	{ count(); returntoken(NUM_CONST); }

L?\"(\\.|[^\\"])*\"	{ count(); returntoken(STRING_LITERAL); }

">>"			{ count(); returntoken(RIGHT_OP); }
"<<"			{ count(); returntoken(LEFT_OP); }
"&&"			{ count(); returntoken(BOOL_AND_OP); }
"||"			{ count(); returntoken(BOOL_OR_OP); }
"<="			{ count(); returntoken(LE_OP); }
">="			{ count(); returntoken(GE_OP); }
"=="			{ count(); returntoken(EQ_OP); }
"!="			{ count(); returntoken(NE_OP); }
";"			{ count(); returntoken(SEMICOLON); }
"{"			{ count(); returntoken(LCURLY); }
"}"			{ count(); returntoken(RCURLY); }
","			{ count(); returntoken(COMMA); }
":"			{ count(); returntoken(COLON); }
"("			{ count(); returntoken(LPAREN); }
")"			{ count(); returntoken(RPAREN); }
"."			{ count(); returntoken(PERIOD); }
"&"			{ count(); returntoken(AND_OP); }
"!"			{ count(); returntoken(NOT); }
"-"			{ count(); returntoken(MINUS); }
"+"			{ count(); returntoken(PLUS); }
"*"			{ count(); returntoken(TIMES); }
"/"			{ count(); returntoken(DIVIDE); }
"%"			{ count(); returntoken(MOD); }
"<"			{ count(); returntoken(LT_OP); }
">"			{ count(); returntoken(GT_OP); }
"^"			{ count(); returntoken(CIRCUMFLEX); }
"|"			{ count(); returntoken(OR_OP); }

[ \t\v\n\f]		{ count(); }
.			{ /* ignore bad characters */ }

%%

yywrap()
{
	return(1);
}


comment()
{
	char c, c1;

loop:
	while ((c = input()) != '*' && c != 0)
      /*putchar(c)*/;

	if ((c1 = input()) != '/' && c != 0)
	{
		unput(c1);
		goto loop;
	}

	if (c != 0)
      /*putchar(c1)*/;
}


int column = 0;

void count()
{
	int i;

	for (i = 0; yytext[i] != '\0'; i++)
		if (yytext[i] == '\n')
			column = 0;
		else if (yytext[i] == '\t')
			column += 8 - (column % 8);
		else
			column++;

	/*ECHO*/;
}


int check_type()
{
/*
* pseudo code --- this is what it should check
*
*	if (yytext == type_name)
*		return(TYPE_NAME);
*
*	return(IDENTIFIER);
*/

/*
*	it actually will only return IDENTIFIER
*/

	return(IDENTIFIER);
}

    """
    # -----------------------------------------
    # end raw lex script
    # -----------------------------------------

def usage():
    print '%s: PyBison parser derived from %s and %s' % (sys.argv[0], bisonFile, lexFile)
    print 'Usage: %s [-k] [-v] [-d] [filename]' % sys.argv[0]
    print '  -k       Keep temporary files used in building parse engine lib'
    print '  -v       Enable verbose messages while parser is running'
    print '  -d       Enable garrulous debug messages from parser engine'
    print '  filename path of a file to parse, defaults to stdin'

def main(*args):
    """
    Unit-testing func
    """

    keepfiles = 0
    verbose = 0
    debug = 0
    filename = None

    for s in ['-h', '-help', '--h', '--help', '-?']:
        if s in args:
            usage()
            sys.exit(0)

    if len(args) > 0:
        if '-k' in args:
            keepfiles = 1
            args.remove('-k')
        if '-v' in args:
            verbose = 1
            args.remove('-v')
        if '-d' in args:
            debug = 1
            args.remove('-d')
    if len(args) > 0:
        filename = args[0]

    p = Parser(verbose=verbose, keepfiles=keepfiles)
    tree = p.run(file=filename, debug=debug)
    return tree

if __name__ == '__main__':
    main(*(sys.argv[1:]))

