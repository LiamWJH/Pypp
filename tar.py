class TypedValue:
    def __init__(self, value, expected_type):
        self.value = value
        self.expected_type = expected_type

    def checkTE(self):


        if not isinstance(self.value, self.expected_type):
            if self.expected_type == 'var':
                 pass
            else:
                 print('ERROR: Wrong DataType error!')
                 exit()


x = TypedValue(12345, int)
x.checkTE()
print(x.value)
name = TypedValue(input("Hello whats your name?"), str)
name.checkTE()
print(f"Hello{name.expected_type}!")
name = TypedValue("hi", str)
name.checkTE()
print(name.value)
input("")
