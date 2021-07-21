tags = {"info": "[INFO]", "warn": "[WARNING]", "out": "[OUTPUT]", "in": "[INPUT]"}
numbers = [x for x in range(0, 10)]

class Brainfuck:
	def __init__(self, code):
		self.unparsed_code = code

	def process(self):
		self.processed_code = []
		for command in self.parsed_code:
			if command not in self.simple_commands:
				tmp_storage = [command[-1] for x in range(0, int(command[:-1]))]
				for x in tmp_storage:
					self.processed_code.append(x)
			else: self.processed_code.append(command)

	def parse(self):
		self.parsed_code = []; tmp_storage = ""
		self.simple_commands = [x for x in "<>+-,.[]"]
		to_process = False
		for command in self.unparsed_code:
			try:
				if command in self.simple_commands:
					self.parsed_code.append(f"{tmp_storage}{command}")
					tmp_storage = ""
				elif command not in self.simple_commands and int(command) in numbers:
					tmp_storage = f"{tmp_storage}{command}"
					to_process = True
			except:
				print(f"{tags['warn']} Invalid char filtered: {command}")
		print(f"{tags['info']} Code parsed successfully!")
		if to_process:
			print(f"{tags['info']} Code processing need detected.")
			self.process()
			print(f"{tags['info']} Code processed successfully")
			return self.processed_code
		else: return self.parsed_code

class MemoryBlock:
	def __init__(self): self.memory_block = [0 for x in range(0,32768)]; self.ptr = 0; self.output = ""

	def move_right(self): self.ptr += 1 if self.ptr < 32767 else 0

	def move_left(self): self.ptr -= 1 if self.ptr > 0 else 32767

	def ptr_add(self): self.memory_block[self.ptr] += 1 if self.memory_block[self.ptr] < 255 else 0

	def ptr_subtract(self): self.memory_block[self.ptr] -= 1 if self.memory_block[self.ptr] > 0 else 255

	def putchar(self): self.output = f"{self.output}{chr(self.memory_block[self.ptr])}"

	def inputchar(self): 
		input_char = ord(input(f"{tags['in']}: "))
		if input_char not in numbers: self.memory_block[self.ptr] = input_char
		else: self.memory_block[self.ptr] = int(input_char)

	def loop(self): 
		if ptr != 0 and self.memory_block[self.ptr-1] != 0: self.execute_code(self.ptr[1,-1])

	def loop_navigation(self, loop):
		index = 1; nested_loops = 0
		end_index = -1; end_index_found = False
		while not end_index_found:
			command = loop[index]
			if command == "[": nested_loops += 1
			elif command == "]":
				if nested_loops == 0:
					end_index = index
					end_index_found = True
				else: nested_loops -= 1
			index += 1
		return end_index

	def execute_code(self, code, loop = False):
		running_index = 0
		if code == []:
			print(f"{tags['warn']} Program doesn't contain any commands!")
		else:
			if loop == False: print(f"{tags['info']} Running program...")
			while running_index < len(code):
				if code[running_index] == ">": self.move_right()
				elif code[running_index] == "<": self.move_left()
				elif code[running_index] == "+": self.ptr_add()
				elif code[running_index] == "-": self.ptr_subtract()
				elif code[running_index] == ".": self.putchar()
				elif code[running_index] == ",": self.inputchar()
				elif code[running_index] == "[": 
					if self.memory_block[self.ptr] > 0 and running_index > 0: 
						self.execute_code(code[running_index + 1:self.loop_navigation(code[running_index:])+running_index], loop = True); 
						running_index -= 1
					else: running_index = self.loop_navigation(code[running_index:])+running_index
				running_index += 1
			if loop == False: print(f"{tags['out']} Program output:\n{self.output}")

hello_world = Brainfuck(",>,.<.").parse()
memory = MemoryBlock()
memory.execute_code(hello_world)
