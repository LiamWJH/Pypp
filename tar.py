class TypedValue:
    def __init__(self, value, expected_type):
        self.value = value
        self.expected_type = expected_type

    def checkTE(self):
        if not isinstance(self.value, self.expected_type):
            if self.expected_type == 'var' or self.expected_type == 'const':
                pass
            else:
                print(f'ERROR: Wrong DataType error for value: {self.value} and type: {self.expected_type}')
                exit()

PI = TypedValue(3.141592, 'const')
radius = TypedValue(10, int)
radius.checkTE()
if PI.value > 1 :
    print("Yes")
