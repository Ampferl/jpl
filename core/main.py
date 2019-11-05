#######################################
# IMPORTS
#######################################

from core.strings_with_arrows import *

import hashlib
import string
import math
import random
import datetime
import os

currentDirectory = os.getcwd()



# Constants
exec(compile(source=open(currentDirectory + '/core/errors.py').read(), filename='errors.py', mode='exec'))

# Errors
exec(compile(source=open(currentDirectory + '/core/constants.py').read(), filename='constants.py', mode='exec'))

# Position
exec(compile(source=open(currentDirectory + '/core/position.py').read(), filename='position.py', mode='exec'))

# Tokens
exec(compile(source=open(currentDirectory + '/core/tokens.py').read(), filename='tokens.py', mode='exec'))

# Lexer
exec(compile(source=open(currentDirectory + '/core/lexer.py').read(), filename='lexer.py', mode='exec'))

# Nodes
exec(compile(source=open(currentDirectory + '/core/nodes.py').read(), filename='nodes.py', mode='exec'))

# Parse Result
exec(compile(source=open(currentDirectory + '/core/parse_result.py').read(), filename='parse_result.py', mode='exec'))

# Parser
exec(compile(source=open(currentDirectory + '/core/parser.py').read(), filename='parser.py', mode='exec'))

# Runtime Result
exec(compile(source=open(currentDirectory + '/core/runtime_result.py').read(), filename='runtime_result.py', mode='exec'))

# Values
exec(compile(source=open(currentDirectory + '/core/values.py').read(), filename='values.py', mode='exec'))

# Functions
exec(compile(source=open(currentDirectory + '/core/functions.py').read(), filename='functions.py', mode='exec'))
	
# Built-In-Functions
exec(compile(source=open(currentDirectory + '/core/builtin_functions.py').read(), filename='builtin_functions.py', mode='exec'))

# Context
exec(compile(source=open(currentDirectory + '/core/context.py').read(), filename='context.py', mode='exec'))

# Symbol Table
exec(compile(source=open(currentDirectory + '/core/symbol_table.py').read(), filename='symbol_table.py', mode='exec'))

# Interpreter
exec(compile(source=open(currentDirectory + '/core/interpreter.py').read(), filename='interpreter.py', mode='exec'))



#######################################
# RUN
#######################################

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("true", Number.true)

global_symbol_table.set("print", BuiltInFunction.print)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("is_number", BuiltInFunction.is_number)
global_symbol_table.set("is_string", BuiltInFunction.is_string)
global_symbol_table.set("is_list", BuiltInFunction.is_list)
global_symbol_table.set("is_function", BuiltInFunction.is_function)
global_symbol_table.set("append_l", BuiltInFunction.append_l)
global_symbol_table.set("pop_l", BuiltInFunction.pop_l)
global_symbol_table.set("set_l", BuiltInFunction.set_l)
global_symbol_table.set("extend_l", BuiltInFunction.extend_l)
global_symbol_table.set("len_l", BuiltInFunction.len_l)
global_symbol_table.set("rand", BuiltInFunction.rand)
global_symbol_table.set("run", BuiltInFunction.run)
global_symbol_table.set("datetime", BuiltInFunction.datetime)
global_symbol_table.set("split", BuiltInFunction.split)
global_symbol_table.set("join", BuiltInFunction.join)
global_symbol_table.set("replace", BuiltInFunction.replace)
global_symbol_table.set("search_l", BuiltInFunction.search_l)
# Formats
global_symbol_table.set("int", BuiltInFunction.int)
global_symbol_table.set("str", BuiltInFunction.str)
global_symbol_table.set("float", BuiltInFunction.float)
global_symbol_table.set("hash", BuiltInFunction.hash)


def run(fn, text):
	# Generate tokens
	lexer = Lexer(fn, text)
	tokens, error = lexer.make_tokens()
	if error: return None, error
	
	# Generate AST
	parser = Parser(tokens)
	ast = parser.parse()
	if ast.error: return None, ast.error

	# Run program
	interpreter = Interpreter()
	context = Context('<program>')
	context.symbol_table = global_symbol_table
	result = interpreter.visit(ast.node, context)

	return result.value, result.error