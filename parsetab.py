
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARRAY AS BITAND BITNOT BITOR BOOL BREAK CALLABLE CASE CATCH CLASS CLONE CLOSE_TAG COLON COMMA CONCAT CONCATASSIGN CONST CONTINUE DECLARE DECREMENT DEFAULT DIE DIVIDE DIVIDEASSIGN DO DOC_COMMENT ECHO ELSE ELSEIF EMPTY ENDWHILE EQUAL ERRORCONTROL EVAL EXECUTION EXIT EXP EXPASSIGN EXTENDS FGETS FINAL FINALLY FLOAT FN FNARROW FOR FOREACH FUNCTION GLOBAL GOTO GREATEREQUALTHAN GREATERTHAN ID IDENTICAL IF IMPLEMENTS INCLUDE INCLUDE_ONCE INCREMENT INSTANCEOF INSTEADOF INTEGER INTERFACE ISSET IS_EQUAL LCURLY LESSEQUALTHAN LESSTHAN LIST LOGICALNOT LPAREN LSQUARE MATCH MINUS MINUSASSIGN MOD MODASSIGN NAMESPACE NEW NOTEQUAL NULL OBJOP OPEN_TAG OR PLUS PLUSASSIGN POP PRINT PRIVATE PROTECTED PUBLIC PUSH QUEUE QUOTE RCURLY REQUIRE REQUIRE_ONCE RETURN RPAREN RSQUARE SEMICOLON STACK STATIC STDIN STRING SWITCH THROW TIMES TIMESASSIGN TRAIT TRY UNSET USE VAR WHILE XOR YIELD YIELD_FROM __HALT_COMPILERcuerpo : arithmeticExpression\n              | switchStatement\n              | queueDeclaration\n              | queueEnqueue\n              | queueDequeue\n              | arrowFunction\n              | echo\n              | fgets\n    switchStatement : SWITCH LPAREN value RPAREN LCURLY switchCases switchDefault RCURLYswitchDefault : DEFAULT COLON arithmeticExpressionswitchCase : CASE value COLON arithmeticExpression BREAK SEMICOLONswitchCases : switchCase\n                   | switchCases switchCase\n    queueDeclaration : ID EQUAL NEW QUEUE SEMICOLONqueueEnqueue : ID OBJOP PUSH LPAREN value RPAREN SEMICOLONqueueDequeue : ID OBJOP POP SEMICOLONarrowFunction : FN LPAREN ID RPAREN FNARROW arrowBody SEMICOLONarrowBody : FN LPAREN ID RPAREN FNARROW arrowBody\n                 | cuerpo\n    echo : ECHO values SEMICOLONvalues : value\n               | values COMMA value\n    fgets : ID EQUAL FGETS LPAREN STDIN RPAREN SEMICOLONarithmeticExpression : value arithmeticOperator valuevalue : ID \n             | INTEGER\n             | FLOAT\n             | STRING\n             | BOOL\n             | NULL\n    arithmeticOperator : PLUS\n                          | MINUS \n                          | TIMES \n                          | DIVIDE\n                          | MOD\n                          | EXP\n    '
    
_lr_action_items = {'SWITCH':([0,54,79,],[11,11,11,]),'ID':([0,14,20,21,22,23,24,25,26,27,30,42,46,54,57,69,72,73,79,],[12,33,33,-31,-32,-33,-34,-35,-36,33,40,33,33,12,33,74,33,33,12,]),'FN':([0,54,79,],[13,60,60,]),'ECHO':([0,54,79,],[14,14,14,]),'INTEGER':([0,14,20,21,22,23,24,25,26,27,42,46,54,57,72,73,79,],[15,15,15,-31,-32,-33,-34,-35,-36,15,15,15,15,15,15,15,15,]),'FLOAT':([0,14,20,21,22,23,24,25,26,27,42,46,54,57,72,73,79,],[16,16,16,-31,-32,-33,-34,-35,-36,16,16,16,16,16,16,16,16,]),'STRING':([0,14,20,21,22,23,24,25,26,27,42,46,54,57,72,73,79,],[17,17,17,-31,-32,-33,-34,-35,-36,17,17,17,17,17,17,17,17,]),'BOOL':([0,14,20,21,22,23,24,25,26,27,42,46,54,57,72,73,79,],[18,18,18,-31,-32,-33,-34,-35,-36,18,18,18,18,18,18,18,18,]),'NULL':([0,14,20,21,22,23,24,25,26,27,42,46,54,57,72,73,79,],[19,19,19,-31,-32,-33,-34,-35,-36,19,19,19,19,19,19,19,19,]),'$end':([1,2,3,4,5,6,7,8,9,15,16,17,18,19,33,34,41,47,51,67,68,70,71,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-26,-27,-28,-29,-30,-25,-24,-20,-16,-14,-23,-15,-17,-9,]),'SEMICOLON':([2,3,4,5,6,7,8,9,15,16,17,18,19,31,32,33,34,39,41,44,47,49,51,58,59,61,62,67,68,70,71,78,81,],[-1,-2,-3,-4,-5,-6,-7,-8,-26,-27,-28,-29,-30,41,-21,-25,-24,47,-20,51,-16,-22,-14,67,68,70,-19,-23,-15,-17,-9,80,70,]),'PLUS':([10,12,15,16,17,18,19,33,],[21,-25,-26,-27,-28,-29,-30,-25,]),'MINUS':([10,12,15,16,17,18,19,33,],[22,-25,-26,-27,-28,-29,-30,-25,]),'TIMES':([10,12,15,16,17,18,19,33,],[23,-25,-26,-27,-28,-29,-30,-25,]),'DIVIDE':([10,12,15,16,17,18,19,33,],[24,-25,-26,-27,-28,-29,-30,-25,]),'MOD':([10,12,15,16,17,18,19,33,],[25,-25,-26,-27,-28,-29,-30,-25,]),'EXP':([10,12,15,16,17,18,19,33,],[26,-25,-26,-27,-28,-29,-30,-25,]),'LPAREN':([11,13,37,38,60,],[27,30,45,46,69,]),'EQUAL':([12,],[28,]),'OBJOP':([12,],[29,]),'COMMA':([15,16,17,18,19,31,32,33,49,],[-26,-27,-28,-29,-30,42,-21,-25,-22,]),'RCURLY':([15,16,17,18,19,33,34,63,75,],[-26,-27,-28,-29,-30,-25,-24,71,-10,]),'BREAK':([15,16,17,18,19,33,34,76,],[-26,-27,-28,-29,-30,-25,-24,78,]),'RPAREN':([15,16,17,18,19,33,35,40,52,53,74,],[-26,-27,-28,-29,-30,-25,43,48,58,59,77,]),'COLON':([15,16,17,18,19,33,65,66,],[-26,-27,-28,-29,-30,-25,72,73,]),'NEW':([28,],[36,]),'FGETS':([28,],[37,]),'PUSH':([29,],[38,]),'POP':([29,],[39,]),'QUEUE':([36,],[44,]),'LCURLY':([43,],[50,]),'STDIN':([45,],[52,]),'FNARROW':([48,77,],[54,79,]),'CASE':([50,55,56,64,80,],[57,57,-12,-13,-11,]),'DEFAULT':([55,56,64,80,],[65,-12,-13,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,54,79,],[1,62,62,]),'arithmeticExpression':([0,54,72,73,79,],[2,2,75,76,2,]),'switchStatement':([0,54,79,],[3,3,3,]),'queueDeclaration':([0,54,79,],[4,4,4,]),'queueEnqueue':([0,54,79,],[5,5,5,]),'queueDequeue':([0,54,79,],[6,6,6,]),'arrowFunction':([0,54,79,],[7,7,7,]),'echo':([0,54,79,],[8,8,8,]),'fgets':([0,54,79,],[9,9,9,]),'value':([0,14,20,27,42,46,54,57,72,73,79,],[10,32,34,35,49,53,10,66,10,10,10,]),'arithmeticOperator':([10,],[20,]),'values':([14,],[31,]),'switchCases':([50,],[55,]),'switchCase':([50,55,],[56,64,]),'arrowBody':([54,79,],[61,81,]),'switchDefault':([55,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> arithmeticExpression','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',5),
  ('cuerpo -> switchStatement','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',6),
  ('cuerpo -> queueDeclaration','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',7),
  ('cuerpo -> queueEnqueue','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',8),
  ('cuerpo -> queueDequeue','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',9),
  ('cuerpo -> arrowFunction','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',10),
  ('cuerpo -> echo','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',11),
  ('cuerpo -> fgets','cuerpo',1,'p_cuerpo','Analizador_sintactico.py',12),
  ('switchStatement -> SWITCH LPAREN value RPAREN LCURLY switchCases switchDefault RCURLY','switchStatement',8,'p_switchStatement','Analizador_sintactico.py',16),
  ('switchDefault -> DEFAULT COLON arithmeticExpression','switchDefault',3,'p_switchDefault','Analizador_sintactico.py',19),
  ('switchCase -> CASE value COLON arithmeticExpression BREAK SEMICOLON','switchCase',6,'p_switchCase','Analizador_sintactico.py',22),
  ('switchCases -> switchCase','switchCases',1,'p_switchCases','Analizador_sintactico.py',25),
  ('switchCases -> switchCases switchCase','switchCases',2,'p_switchCases','Analizador_sintactico.py',26),
  ('queueDeclaration -> ID EQUAL NEW QUEUE SEMICOLON','queueDeclaration',5,'p_queueDeclaration','Analizador_sintactico.py',32),
  ('queueEnqueue -> ID OBJOP PUSH LPAREN value RPAREN SEMICOLON','queueEnqueue',7,'p_queueEnqueue','Analizador_sintactico.py',35),
  ('queueDequeue -> ID OBJOP POP SEMICOLON','queueDequeue',4,'p_queueDequeue','Analizador_sintactico.py',38),
  ('arrowFunction -> FN LPAREN ID RPAREN FNARROW arrowBody SEMICOLON','arrowFunction',7,'p_arrowFunction','Analizador_sintactico.py',43),
  ('arrowBody -> FN LPAREN ID RPAREN FNARROW arrowBody','arrowBody',6,'p_arrowBody','Analizador_sintactico.py',46),
  ('arrowBody -> cuerpo','arrowBody',1,'p_arrowBody','Analizador_sintactico.py',47),
  ('echo -> ECHO values SEMICOLON','echo',3,'p_echo','Analizador_sintactico.py',53),
  ('values -> value','values',1,'p_values','Analizador_sintactico.py',56),
  ('values -> values COMMA value','values',3,'p_values','Analizador_sintactico.py',57),
  ('fgets -> ID EQUAL FGETS LPAREN STDIN RPAREN SEMICOLON','fgets',7,'p_fgets','Analizador_sintactico.py',63),
  ('arithmeticExpression -> value arithmeticOperator value','arithmeticExpression',3,'p_arithmeticExpression','Analizador_sintactico.py',66),
  ('value -> ID','value',1,'p_value','Analizador_sintactico.py',70),
  ('value -> INTEGER','value',1,'p_value','Analizador_sintactico.py',71),
  ('value -> FLOAT','value',1,'p_value','Analizador_sintactico.py',72),
  ('value -> STRING','value',1,'p_value','Analizador_sintactico.py',73),
  ('value -> BOOL','value',1,'p_value','Analizador_sintactico.py',74),
  ('value -> NULL','value',1,'p_value','Analizador_sintactico.py',75),
  ('arithmeticOperator -> PLUS','arithmeticOperator',1,'p_arithmeticOperator','Analizador_sintactico.py',79),
  ('arithmeticOperator -> MINUS','arithmeticOperator',1,'p_arithmeticOperator','Analizador_sintactico.py',80),
  ('arithmeticOperator -> TIMES','arithmeticOperator',1,'p_arithmeticOperator','Analizador_sintactico.py',81),
  ('arithmeticOperator -> DIVIDE','arithmeticOperator',1,'p_arithmeticOperator','Analizador_sintactico.py',82),
  ('arithmeticOperator -> MOD','arithmeticOperator',1,'p_arithmeticOperator','Analizador_sintactico.py',83),
  ('arithmeticOperator -> EXP','arithmeticOperator',1,'p_arithmeticOperator','Analizador_sintactico.py',84),
]
