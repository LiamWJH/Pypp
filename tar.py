class TypedValue:
        def __init__(self, value, expected_type):
            self.value = value
            self.expected_type = expected_type

        def checkTE(self):
            if not isinstance(self.value, self.expected_type):
                raise TypeError(f"Expected {self.expected_type.__name__} as type for value {self.value}")

x = TypedValue(12345, int)
x.checkTE()
print(x.value)