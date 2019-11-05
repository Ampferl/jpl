#######################################
# TOKENS
#######################################

TT_INT			= 'INT'
TT_FLOAT    	= 'FLOAT'
TT_STRING		= 'STRING'
TT_IDENTIFIER	= 'IDENTIFIER'
TT_KEYWORD		= 'KEYWORD'
TT_PLUS     	= 'PLUS'
TT_MINUS    	= 'MINUS'
TT_MUL      	= 'MUL'
TT_DIV      	= 'DIV'
TT_POW			= 'POW'
TT_MOD			= 'MOD'
TT_EQ			= 'EQ'
TT_LPAREN   	= 'LPAREN'
TT_RPAREN   	= 'RPAREN'
TT_LBRACE		= 'LBRACE'
TT_RBRACE		= 'RBRACE'
TT_LSQUARE		= 'LSQUARE'
TT_RSQUARE		= 'RSQUARE'
TT_SC			= 'SC'
TT_COMMA		= 'COMMA' 
TT_EE			= 'EE' 
TT_NE			= 'NE' 
TT_LT			= 'LT' 
TT_GT			= 'GT' 
TT_LTE			= 'LTE' 
TT_GTE			= 'GTE' 
TT_NEWLINE		= 'NEWLINE'
TT_EOF			= 'EOF'

KEYWORDS = [
	'var',
	'and', 
	'or', 
	'not',
	'if',
	'elif',
	'else',
	'for',
	'while',
	'function',
	'return',
	'continue',
	'break'
]

class Token:
	def __init__(self, type_, value=None, pos_start=None, pos_end=None):
		self.type = type_
		self.value = value

		if pos_start:
			self.pos_start = pos_start.copy()
			self.pos_end = pos_start.copy()
			self.pos_end.advance()

		if pos_end:
			self.pos_end = pos_end.copy()

	def matches(self, type_, value):
		return self.type == type_ and self.value == value
	
	def __repr__(self):
		if self.value: return f'{self.type}:{self.value}'
		return f'{self.type}'