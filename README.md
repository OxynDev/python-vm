# GxHook Vm

GxHook Vm is a program that translates Python code into opcodes (individual bytecode instructions). The compiler analyzes various code segments and transforms them into something similar to assembly language, making the code unreadable without prior reverse engineering of the virtual machine code and understanding individual instructions. Currently, the program supports basic instructions, but it will be further developed in the future. I created it mainly to demonstrate the concept of a VM for Python.

## Change log
```diff
v1.0.1 ⋮ 22/10/2023
+ added function logic
+ added minus, div, mul, mod operators
```

## Opcodes
```markdown
- `free` [0] (MEMORY)
- `plus` [1] (A + B)
- `minus` [2] (A - B)
- `mod` [3] (a % b) 
- `mul` [4] (a * b) 
- `div` [5] (a / b) 
- `int` [6] (int(x))
- `str` [7] (str(x)) SOON
- `print` [8] (print(x))
- `int` [9] (declaration)
- `str` [10] (declaration) SOON
- `float` [11] (declaration) SOON
- `assign` [12] (a = 1)
- `load` [13] (x = proc[i])
- `function_def` [14] (def foo)
- `label` [15] (end mark)
- `function_run` [16] (foo())

More coming soon.
```
GxHook also includes a compiler that automatically converts Python code into VM code.

```python
source_code = """
a = 1
def foo():
    print(a/2)
def foo2():
    print(1-10)
foo()
foo2()
"""

parsed_code = ast.parse(source_code)
code_visitor = CodeVisitor()
code_visitor.visit(parsed_code)
for i in range(14):
    code_visitor.vm.pop(0)
print(code_visitor.vm)

# [12, 9, 1, 0, 14, 12, 9, 2, 0, 8, 25, 15, 0, 14, 12, 9, 1, 0, 12, 9, 10, 0, 12, 2, 9, 34, 38, 0, 8, 44, 15, 0, 16, 22, 16, 31]
```

### How to Use GxHook

To use GxHook, follow these steps:

1. Compile your code using `compiler.py`.
2. Place the compiled code in `vm.py`.
3. Ensure that you obfuscate the VM before using it in public projects.

```python
def run(self):
    self.load_functions()
    for i in [12, 9, 1, 0, 12, 9, 2, 0, 12, 1, 9, 17, 21, 0, 8, 27, 12, 9, 1, 0, 12, 9, 10, 0, 12, 2, 9, 33, 37, 0, 8, 43]:
        self.processor.append(i)
    self.index = self.instructions_count
    print("VM INSTRUCTIONS: " + str(self.index))
    print("TOTAL: " + str(len(self.processor)))
    while True:
        # print("VM RUN: " + str(self.instructions[self.processor[self.index]]), self.index)
        self.instructions[self.processor[self.index]]()
        self.index += 1
        if self.index >= len(self.processor):
            break
    # print(self.processor)
```

