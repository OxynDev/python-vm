import ast, sys



class Vm:

    def __init__(self):
        self.processor = []
        self.instructions = []
        self.index = 0
        self.instructions_count = 0


    def push(self, x):
        self.processor.append(x)
        
    # math

    def plus(self, a, b):
        return a + b
        
    def minus(self, a, b):
        return a - b

    def mod(self, a, b):
        return a % b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b

    # builtins

    def _int(self, x):
        return int(x)

    def _str(self, x):
        return str(x)

    def _print(self):
        self.index += 1
        sys.stdout.write(str(self.processor[13](self.processor[self.index])) + "\n")
        sys.stdout.flush()

    def _load(self, x):
        return self.processor[x]

    # logic

    def _assign(self):
        self.index += 1
        if self.processor[self.index] == 9:
            self.index += 1
            x = self.processor[self.index]
            self.index += 1
            self.processor[self.index] = self.processor[6](x)
            #print("ASSIGN: " + str(self.index), self.processor[6](x))
        elif self.processor[self.index] in [1,2,3,4,5]:
            opcode = self.processor[self.index]
            self.index += 1
            var_type = self.processor[self.index]
            self.index += 1
            x = self.processor[self.index]
            self.index += 1
            y = self.processor[self.index]
            self.index += 1
            res = self.processor[opcode](self.processor[13](x),self.processor[13](y))
            if var_type == 9:
                self.processor[self.index] = self.processor[6](res)
            #print("ASSIGN: " + str(self.index), self.processor[6](res))

    def load_functions(self):

        self.instructions = [
                0, # free
                self.plus, # 1
                self.minus, # 2
                self.mod, # 3
                self.mul, # 4
                self.div, # 5
                self._int, # 6
                self._str, # 7
                self._print, # 8
                9, # int
                10, # str
                11, # float
                self._assign, # 12
                self._load # 13
            ]

        for i in self.instructions:
            self.push(i)
        self.instructions_count = len(self.processor)
        
    def run(self):
        self.load_functions()
        for i in [12, 9, 1, 0, 12, 9, 2, 0, 12, 1, 9, 17, 21, 0, 8, 27, 12, 9, 1, 0, 12, 9, 10, 0, 12, 2, 9, 33, 37, 0, 8, 43]:
            self.processor.append(i)
        self.index = self.instructions_count
        print("VM INSTRUCTIONS: " + str(self.index))
        print("TOTAL: " + str(len(self.processor)))
        while True:
            #print("VM RUN: " + str(self.instructions[self.processor[self.index]]), self.index)
            self.instructions[self.processor[self.index]]()
            self.index += 1
            if self.index >= len(self.processor):
                break
        #print(self.processor)

        


if __name__ == "__main__":

    Vm().run()

    
