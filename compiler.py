import ast
import sys



vm_instructions = {

   "ASSING": 12,

    "FREE": 0,
    "STR": 10,
    "INT": 9,

    "MINUS": 2,
    "PLUS": 1,

    "PRINT": 8
}


class CodeVisitor(ast.NodeVisitor):
    vm = []
    varbles = {}
    index = 0

    def __init__(self):
        for i in range(14):
            self.vm.append(0)
            pass

    def visit_BinOp(self, node):
        

        left = self.visit(node.left)
        right = self.visit(node.right)
        operator = node.op.__class__.__name__
        print(operator)

        op = {
            "Add":"PLUS",
            "Sub":"MINUS"
              }

        if (isinstance(node.right, ast.Constant)) and (isinstance(node.left, ast.Constant)):
            if (type(node.left.value) == int) and (type(node.right.value) == int):
                pass

                left_vm_index = len(self.vm) - 5
                right_vm_index = len(self.vm) - 1

                self.vm.append(vm_instructions['ASSING'])
                self.vm.append(vm_instructions[op[operator]]) 
                self.vm.append(vm_instructions['INT']) 
                self.vm.append(left_vm_index) 
                self.vm.append(right_vm_index) 
                self.vm.append(vm_instructions['FREE']) 

        elif (isinstance(node.right, ast.Name)) and (isinstance(node.left, ast.Name)):
            left_vm_index = self.varbles[node.left.id]['index']
            right_vm_index = self.varbles[node.right.id]['index']
            self.vm.append(vm_instructions['ASSING'])
            self.vm.append(vm_instructions[op[operator]]) 
            self.vm.append(vm_instructions['INT']) 
            self.vm.append(left_vm_index - 1) 
            self.vm.append(right_vm_index - 1) 
            self.vm.append(vm_instructions['FREE']) 
            

    def visit_Num(self, node):
        #print(node.n)
        self.vm.append(vm_instructions['ASSING'])
        self.vm.append(vm_instructions['INT']) 
        self.vm.append(node.n)
        self.vm.append(vm_instructions['FREE'])
    
    def visit_Str(self, node):
        self.vm.append(vm_instructions['ASSING'])
        self.vm.append(vm_instructions['STR']) 
        self.vm.append(node.s)
        self.vm.append(vm_instructions['FREE'])


    def visit_Call(self, node):
        
        if node.args:
            for arg in node.args:
                self.visit(arg)  
        else:
            print("No arguments")

        if node.keywords:
            for kwarg in node.keywords:
                print(f"{kwarg.arg}:")
                self.visit(kwarg.value)

        func_args = len(self.vm) - 1

        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            self.vm.append(vm_instructions['PRINT'])  
        else:
            self.generic_visit(node)
            
        self.vm.append(func_args)  

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name):
            self.vm.append(vm_instructions['ASSING']) 
            if type(node.value.value) == int:
                self.vm.append(vm_instructions['INT']) 
            
            self.vm.append(node.value.value) 
            self.vm.append(vm_instructions['FREE']) 

            variable_name = node.targets[0].id
            #print(variable_name)
            self.varbles[variable_name] = {"value":node.value.value, "index":len(self.vm)}


def compile_and_run(code):
    pass

if __name__ == "__main__":
    source_code = """
a = 1
b = 2
print(a + b)
print(1-10)
"""

    parsed_code = ast.parse(source_code)
    code_visitor = CodeVisitor()
    code_visitor.visit(parsed_code)
    for i in range(14):
        code_visitor.vm.pop(0)
        pass
    print(code_visitor.vm)



