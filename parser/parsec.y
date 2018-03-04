
%{

%}

%token IDENTIFIER NUM_CONST STRING_LITERAL

%token VALVE SENSOR 

%token COMMA
%token IF ELSE 
%token PARALLEL RUN BREAK 
%token WAIT WAIT_UNTIL
%token READ OPEN CLOSE
%token ROUTINE EMERGENCY ABORT
%token MAIN CHECKS
%token LOG LOG_ERR
%token REL_TIME
%token LEFT_OP RIGHT_OP
%token LPAREN RPAREN LCURLY RCURLY
%token PLUS MINUS TIMES DIVIDE MOD
%token BOOL_OR_OP BOOL_AND_OP OR_OP AND_OP CIRCUMFLEX EQ_OP NE_OP
%token LT_OP LE_OP GT_OP GE_OP
%token NOT
%token SEMICOLON

%left PLUS MINUS TIMES DIVIDE

/* WTF is a translation_unit?? */
%start translation_unit



%%

translation_unit
    : routine_declaration
    | translation_unit routine_declaration
    ;


routine_declaration
	: ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY routine_body RCURLY
	| ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY RCURLY
	| ROUTINE IDENTIFIER LPAREN RPAREN LCURLY routine_body RCURLY
    | ROUTINE IDENTIFIER LPAREN RPAREN LCURLY RCURLY
	| ROUTINE MAIN LPAREN valve_list RPAREN LCURLY main_routine_body RCURLY
	| ROUTINE MAIN LPAREN valve_list RPAREN LCURLY RCURLY
	| ROUTINE CHECKS LPAREN RPAREN LCURLY emergency_routine_body RCURLY
	| ROUTINE CHECKS LPAREN RPAREN LCURLY RCURLY
	| EMERGENCY ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY emergency_routine_body RCURLY
	| EMERGENCY ROUTINE IDENTIFIER LPAREN valve_list RPAREN LCURLY RCURLY
	| EMERGENCY ROUTINE IDENTIFIER LPAREN RPAREN LCURLY emergency_routine_body RCURLY
    | EMERGENCY ROUTINE IDENTIFIER LPAREN RPAREN LCURLY RCURLY
	;

valve_list
	: VALVE
	| valve_list COMMA VALVE
	;

routine_body:
    | serial_statement routine_body
    | serial_statement
    ;

main_routine_body:
    | routine_body
    ;

emergency_routine_body:
    | routine_body
    ;

checks_routine_body:
    | routine_body
    ;

serial_statement:
    | parallel_block
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
    ;

/** cond expression, bool expression?**/

expression:
    | READ VALVE
    | READ SENSOR
    | REL_TIME
    | NUM_CONST
    ;

parallel_block:
    | PARALLEL LCURLY parallel_list RCURLY
    | PARALLEL LCURLY RCURLY
    ;

parallel_list:
    | run_statement parallel_list
    | run_statement
    ;

run_statement:
    | RUN INDENTIFIER SEMICOLON
    ;

conditional_block:
    | if_block
    | if_block else_series
    ;

if_block:
    | IF conditional_expression LCURLY routine_body RCURLY
    | IF conditional_expression LCURLY RCURLY
    ;

else_series:
    | ELSE if_block
    | ELSE if_block else_series
    | ELSE LCURLY routine_body RCURLY
    | ELSE LCURLY RCURLY
    ;

wait_statement:
    | WAIT NUM_CONST SEMICOLON
    ;

wait_until_statement:
    | WAIT_UNTIL conditional_expression SEMICOLON
    ;

open_statement:
    | OPEN VALVE SEMICOLON
    ;

close_statement:
    | CLOSE VALVE SEMICOLON
    ;

log_statement:
    | LOG log_value SEMICOLON
    ;

log_err_statement:
    | LOG_ERROR log_value SEMICOLON
    ;

log_value:
    | STRING_LITERAL
    | expression
    | conditional_expression
    | log_value PLUS log_value
    ;

break_statement:
    | BREAK STRING_LITERAL SEMICOLON
    ;

abort_statement:
    | ABORT SEMICOLON
    ;

primary_expression
	: expression
	| LPAREN conditional_expression RPAREN
	;

unary_expression
	: primary_expression
	| MINUS primary_expression
	;

multiplicative_expression
	: unary_expression
	| multiplicative_expression TIMES unary_expression
	| multiplicative_expression DIVIDE unary_expression
	| multiplicative_expression MOD unary_expression
	;

additive_expression
	: multiplicative_expression
	| additive_expression PLUS multiplicative_expression
	| additive_expression MINUS multiplicative_expression
	;

shift_expression
	: additive_expression
	| shift_expression LEFT_OP additive_expression
	| shift_expression RIGHT_OP additive_expression


relational_expression
	: shift_expression
	| relational_expression LT_OP shift_expression
	| relational_expression GT_OP shift_expression
	| relational_expression LE_OP shift_expression
	| relational_expression GE_OP shift_expression
	;

equality_expression
	: relational_expression
	| equality_expression EQ_OP relational_expression
	| equality_expression NE_OP relational_expression
	;

and_expression
	: equality_expression
	| and_expression AND_OP equality_expression
	;

exclusive_or_expression
	: and_expression
	| exclusive_or_expression CIRCUMFLEX and_expression
	;

inclusive_or_expression
	: exclusive_or_expression
	| inclusive_or_expression OR_OP exclusive_or_expression
	;

logical_and_expression
	: inclusive_or_expression
	| logical_and_expression BOOL_AND_OP inclusive_or_expression
	;

logical_or_expression
	: logical_and_expression
	| logical_or_expression BOOL_OR_OP logical_and_expression
	;

conditional_expression
	: logical_or_expression
	;
%%
