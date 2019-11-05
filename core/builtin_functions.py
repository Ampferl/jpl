class BuiltInFunction(BaseFunction):
	def __init__(self, name):
		super().__init__(name)

	def execute(self, args):
		res = RTResult()
		exec_ctx = self.generate_new_context()

		method_name = f'execute_{self.name}'
		method = getattr(self, method_name, self.no_visit_method)

		res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
		if res.should_return(): return res

		return_value = res.register(method(exec_ctx))
		if res.should_return(): return res

		return res.success(return_value) 

	def no_visit_method(self, node, context):
		raise Exception(f'No execute_{self.name} method defined')

	def copy(self):
		copy = BuiltInFunction(self.name)
		copy.set_context(self.context)
		copy.set_pos(self.pos_start, self.pos_end)
		return copy

	def __repr__(self):
		return f"<built-in function {self.name}>"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_print(self, exec_ctx):
		print(str(exec_ctx.symbol_table.get('value')))
		return RTResult().success(Number.null)
	execute_print.arg_names = ['value']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_input(self, exec_ctx):
		typ = exec_ctx.symbol_table.get('type')
		text = input()
		
		string = str(text)

		return RTResult().success(String(string))

	execute_input.arg_names = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_is_number(self, exec_ctx):
		is_number = isinstance(exec_ctx.symbol_table.get('value'), Number)
		return RTResult().success(Number.true if is_number else Number.false)
	execute_is_number.arg_names = ['value']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_is_string(self, exec_ctx):
		is_number = isinstance(exec_ctx.symbol_table.get('value'), String)
		return RTResult().success(Number.true if is_number else Number.false)
	execute_is_string.arg_names = ['value']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_is_list(self, exec_ctx):
		is_number = isinstance(exec_ctx.symbol_table.get('value'), List)
		return RTResult().success(Number.true if is_number else Number.false)
	execute_is_list.arg_names = ['value']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_is_function(self, exec_ctx):
		is_number = isinstance(exec_ctx.symbol_table.get('value'), BaseFunction)
		return RTResult().success(Number.true if is_number else Number.false)
	execute_is_function.arg_names = ['value']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_append_l(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")
		value = exec_ctx.symbol_table.get("value")

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be list",
				exec_ctx
			))

		list_.elements.append(value)
		return RTResult().success(Number.null)
	execute_append_l.arg_names = ['list', 'value']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_pop_l(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")
		index = exec_ctx.symbol_table.get("index")

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be list",
				exec_ctx
			))


		if not isinstance(index, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second argument must be number",
				exec_ctx
			))
		try:
			element = list_.elements.pop(index.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Element at this index could not be removed from list, because index is out of bounds",
				exec_ctx
			))
		return RTResult().success(element)
	
	execute_pop_l.arg_names = ['list', 'index']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_set_l(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get("list")
		index = exec_ctx.symbol_table.get("index")
		rplce = exec_ctx.symbol_table.get("rplce")

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be list",
				exec_ctx
			))


		if not isinstance(index, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second argument must be number",
				exec_ctx
			))

		
			

		try:
			if isinstance(index, Number):
				list_.elements[index.value] = Number(rplce.value)
			else:
				list_.elements[index.value] = String(rplce.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Element at this index could not be replace this in the list, because index is out of bounds",
				exec_ctx
			))
		return RTResult().success(list_)
	
	execute_set_l.arg_names = ['list', 'index', 'rplce']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_extend_l(self, exec_ctx):
		listA = exec_ctx.symbol_table.get("listA")
		listB = exec_ctx.symbol_table.get("listB")

		if not isinstance(listA, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be list",
				exec_ctx
			))

		if not isinstance(listB, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second argument must be list",
				exec_ctx
			))

		listA.elements.extend(listB.elements)
		return RTResult().success(Number.null)

	execute_extend_l.arg_names = ['listA', 'listB']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_len_l(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get('list')

		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Argument must be list",
				exec_ctx
			))

		return RTResult().success(Number(len(list_.elements)))

	execute_len_l.arg_names = ['list']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_run(self, exec_ctx):
		fn = exec_ctx.symbol_table.get('fn')

		if not isinstance(fn, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Argument must be string",
				exec_ctx
			))
		
		fn = fn.value

		try:
			with open(fn, "r") as f:
				script = f.read()
		except Exception as e:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				f'Failed to load code \"{fn}\"\n' + str(e),
				exec_ctx
			))

		_, error = run(fn, script)

		if error:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				f"Failed to finish executing code \"{fn}\"\n" +
				error.as_string(),
				exec_ctx
			))

		return RTResult().success(Number.null)

	execute_run.arg_names = ['fn']	

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_rand(self, exec_ctx):
		start_value = exec_ctx.symbol_table.get('start_val')
		end_value = exec_ctx.symbol_table.get('end_val')

		if not isinstance(start_value, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First argument must be number",
				exec_ctx
			))
		if not isinstance(end_value, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second argument must be number",
				exec_ctx
			))

		try:
			start_value = int(start_value.value)
			end_value = int(end_value.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Arguments must be number",
				exec_ctx
			))
	
		rand = random.randrange(start_value, end_value)
		return RTResult().success(Number(rand))
	execute_rand.arg_names = ['start_val', 'end_val']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_datetime(self, exec_ctx):
		
		return RTResult().success(String(str(datetime.datetime.now())))
	execute_datetime.arg_names = []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_split(self, exec_ctx):
		string = exec_ctx.symbol_table.get('string')
		separator = exec_ctx.symbol_table.get('separator')
		if not isinstance(string, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be string",
				exec_ctx
			))
		if not isinstance(separator, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second Argument must be string",
				exec_ctx
			))
		reslist = (string.value).split(separator.value)
		rest = [String(x) for x in reslist]
		return RTResult().success(List(rest))
	execute_split.arg_names = ['string', 'separator']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_join(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get('list')
		separator = exec_ctx.symbol_table.get('separator')
		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a List",
				exec_ctx
			))
		if not isinstance(separator, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second Argument must be string",
				exec_ctx
			))
		relist = str(list_).split(", ")
		res = (separator.value).join(relist)
		return RTResult().success(String(res))
	execute_join.arg_names = ['list', 'separator']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_search_l(self, exec_ctx):
		list_ = exec_ctx.symbol_table.get('list')
		search = exec_ctx.symbol_table.get('search_string')
		if not isinstance(list_, List):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a List",
				exec_ctx
			))
		if not isinstance(search, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second Argument must be a String",
				exec_ctx
			))
		relist = str(list_).split(", ")
		res = relist.index(search.value)
		return RTResult().success(Number(res))
	execute_search_l.arg_names = ['list', 'search_string']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_replace(self, exec_ctx):
		string = exec_ctx.symbol_table.get('string')
		replace_this = exec_ctx.symbol_table.get('replace_this')
		replacer = exec_ctx.symbol_table.get('replacer')
		if not isinstance(string, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be string",
				exec_ctx
			))

		if not isinstance(replace_this, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second Argument must be string",
				exec_ctx
			))
		if not isinstance(replacer, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Third Argument must be string",
				exec_ctx
			))

		
		res = (string.value).replace(replace_this.value, replacer.value)
		return RTResult().success(String(res))
	execute_replace.arg_names = ['string', 'replace_this', 'replacer']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_int(self, exec_ctx):
		string = exec_ctx.symbol_table.get('string')

		if not isinstance(string, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a String",
				exec_ctx
			))
			
		try:
			res = int(string.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Cant format this string to a number",
				exec_ctx
			))

		return RTResult().success(Number(res))
	execute_int.arg_names = ['string']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_str(self, exec_ctx):
		number = exec_ctx.symbol_table.get('number')

		if not isinstance(number, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a Number",
				exec_ctx
			))
			
		try:
			res = str(number.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Cant format this number to a string",
				exec_ctx
			))

		return RTResult().success(String(res))
	execute_str.arg_names = ['number']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_float(self, exec_ctx):
		string = exec_ctx.symbol_table.get('string')

		if not isinstance(string, String) and not isinstance(string, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a Number or a String",
				exec_ctx
			))
			
		try:
			res = float(string.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Cant format this number or string to a float",
				exec_ctx
			))

		return RTResult().success(Number(res))
	execute_float.arg_names = ['string']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_hash(self, exec_ctx):
		string = exec_ctx.symbol_table.get('string')
		type_ = exec_ctx.symbol_table.get('type')

		if not isinstance(string, String):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a Number or a String",
				exec_ctx
			))
			
		if type_.value == "sha256":
			res = hashlib.sha256((string.value).encode()).hexdigest()
		elif type_.value == "sha1":
			res = hashlib.sha1((string.value).encode()).hexdigest()
		elif type_.value == "sha512":
			res = hashlib.sha512((string.value).encode()).hexdigest()
		elif type_.value == "md5":
			res = hashlib.md5((string.value).encode()).hexdigest()
		else:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Type is not available",
				exec_ctx
			))

		return RTResult().success(String(res))
	execute_hash.arg_names = ['string', 'type']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_round(self, exec_ctx):
		number = exec_ctx.symbol_table.get('number')
		digits = exec_ctx.symbol_table.get('digits')

		if not isinstance(number, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a Number ",
				exec_ctx
			))

		if not isinstance(digits, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Second Argument must be a Number ",
				exec_ctx
			))
			
		try:
			res = round(number.value, digits.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Cant round number",
				exec_ctx
			))

		return RTResult().success(Number(res))
	execute_round.arg_names = ['number', 'digits']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_cos(self, exec_ctx):
		number = exec_ctx.symbol_table.get('number')

		if not isinstance(number, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a Number ",
				exec_ctx
			))

			
		try:
			res = math.cos(number.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Cos() dont work with this number",
				exec_ctx
			))

		return RTResult().success(Number(res))
	execute_cos.arg_names = ['number']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	def execute_sin(self, exec_ctx):
		number = exec_ctx.symbol_table.get('number')

		if not isinstance(number, Number):
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"First Argument must be a Number ",
				exec_ctx
			))

			
		try:
			res = math.sin(number.value)
		except:
			return RTResult().failure(RTError(
				self.pos_start, self.pos_end,
				"Sin() dont work with this number",
				exec_ctx
			))

		return RTResult().success(Number(res))
	execute_sin.arg_names = ['number']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

BuiltInFunction.print						= BuiltInFunction("print")
BuiltInFunction.input						= BuiltInFunction("input")
BuiltInFunction.is_number					= BuiltInFunction("is_number")
BuiltInFunction.is_string					= BuiltInFunction("is_string")
BuiltInFunction.is_list						= BuiltInFunction("is_list")
BuiltInFunction.is_function					= BuiltInFunction("is_function")
BuiltInFunction.append_l					= BuiltInFunction("append_l")
BuiltInFunction.pop_l						= BuiltInFunction("pop_l")
BuiltInFunction.set_l						= BuiltInFunction("set_l")
BuiltInFunction.extend_l					= BuiltInFunction("extend_l")
BuiltInFunction.run							= BuiltInFunction("run")
BuiltInFunction.len_l						= BuiltInFunction("len_l")
BuiltInFunction.datetime					= BuiltInFunction("datetime")
BuiltInFunction.split						= BuiltInFunction("split")
BuiltInFunction.join						= BuiltInFunction("join")
BuiltInFunction.replace						= BuiltInFunction("replace")
BuiltInFunction.search_l					= BuiltInFunction("search_l")
# Formats
BuiltInFunction.int							= BuiltInFunction("int")
BuiltInFunction.str							= BuiltInFunction("str")
BuiltInFunction.float						= BuiltInFunction("float")
BuiltInFunction.hash						= BuiltInFunction("hash")
# Math
BuiltInFunction.rand						= BuiltInFunction("rand")
BuiltInFunction.round						= BuiltInFunction("round")
BuiltInFunction.cos							= BuiltInFunction("cos")
BuiltInFunction.sin							= BuiltInFunction("sin")