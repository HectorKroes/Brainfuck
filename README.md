# Brainfuck Interpreter
List-based implementation of an interpreter and code processor for the programming language brainfuck

# Installation
Clone the github page:
```
git clone https://github.com/HectorKroes/Brainfuck
```

# Utilization
To import relevant functions:
```
from brainfuck import Brainfuck, MemoryBlock
```
To execute a program is necessary to create an object and parse it first:
```
program = Brainfuck("+>+-<-").parse()
```
Then you must create a memory block object in which you'll execute your program:
```
memory = MemoryBlock()
```
And then finally, to execute it:
```
memory.execute_code(program)
```
