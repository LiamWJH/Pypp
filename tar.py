class TypedValue:
    def __init__(self, value, expected_type):
        self.value = value
        self.expected_type = expected_type

    def checkTE(self):
        if not isinstance(self.value, self.expected_type):
            if self.expected_type == 'var' or self.expected_type == 'const':
                pass
            else:
                print('ERROR: Wrong DataType error!')
                exit()

PI = TypedValue(3.14, 'const')
print(PI.value)
#*str PI = "Nope"
age = TypedValue(5, int)
age.checkTE()
print(age.value)
print(age.value)
print("Hello?")
