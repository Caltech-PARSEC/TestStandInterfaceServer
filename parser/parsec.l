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
[a-zA-Z](L|D)*	{ count(); returntoken(IDENTIFIER); }
"break"			{ count(); returntoken(BREAK); }
"parallel"		{ count(); returntoken(PARALLEL); }
"run"			{ count(); returntoken(RUN); }
"wait"			{ count(); returntoken(WAIT); }
"wait_until"	{ count(); returntoken(WAIT_UNTIL); }
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

"..."			{ count(); returntoken(ELLIPSIS); }
">>="			{ count(); returntoken(RIGHT_ASSIGN); }
"<<="			{ count(); returntoken(LEFT_ASSIGN); }
"+="			{ count(); returntoken(ADD_ASSIGN); }
"-="			{ count(); returntoken(SUB_ASSIGN); }
"*="			{ count(); returntoken(MUL_ASSIGN); }
"/="			{ count(); returntoken(DIV_ASSIGN); }
"%="			{ count(); returntoken(MOD_ASSIGN); }
"&="			{ count(); returntoken(AND_ASSIGN); }
"^="			{ count(); returntoken(XOR_ASSIGN); }
"|="			{ count(); returntoken(OR_ASSIGN); }
">>"			{ count(); returntoken(RIGHT_OP); }
"<<"			{ count(); returntoken(LEFT_OP); }
"++"			{ count(); returntoken(INC_OP); }
"--"			{ count(); returntoken(DEC_OP); }
"->"			{ count(); returntoken(PTR_OP); }
"&&"			{ count(); returntoken(BOOL_AND_OP); }
"||"			{ count(); returntoken(BOOL_OR_OP); }
"<="			{ count(); returntoken(LE_OP); }
">="			{ count(); returntoken(GE_OP); }
"=="			{ count(); returntoken(EQ_OP); }
"!="			{ count(); returntoken(NE_OP); }
";"			{ count(); returntoken(SEMICOLON); }
("{"|"<%")		{ count(); returntoken(LBRACE); }
("}"|"%>")		{ count(); returntoken(RBRACE); }
","			{ count(); returntoken(COMMA); }
":"			{ count(); returntoken(COLON); }
"="			{ count(); returntoken(ASSIGN); }
"("			{ count(); returntoken(LPAREN); }
")"			{ count(); returntoken(RPAREN); }
("["|"<:")		{ count(); returntoken(LBRACKET); }
("]"|":>")		{ count(); returntoken(RBRACKET); }
"."			{ count(); returntoken(PERIOD); }
"&"			{ count(); returntoken(AND_OP); }
"!"			{ count(); returntoken(BANG); }
"~"			{ count(); returntoken(TILDE); }
"-"			{ count(); returntoken(MINUS); }
"+"			{ count(); returntoken(PLUS); }
"*"			{ count(); returntoken(STAR); }
"/"			{ count(); returntoken(SLASH); }
"%"			{ count(); returntoken(PERCENT); }
"<"			{ count(); returntoken(LT_OP); }
">"			{ count(); returntoken(GT_OP); }
"^"			{ count(); returntoken(CIRCUMFLEX); }
"|"			{ count(); returntoken(OR_OP); }
"?"			{ count(); returntoken(QUESTIONMARK); }

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
