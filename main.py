import subprocess, sys


def installpkg(packagename):
    subprocess.check_call([sys.executable, "-m", "pip", "install", packagename])

try:
    import pyinstaller
except ImportError as IE:
    installpkg("pyinstaller")


class TypedValue:
    def __init__(self, value, expected_type):
        self.value = value
        self.expected_type = expected_type
    
    def checkTE(self):
        if not isinstance(self.value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type} as type for value {self.value}")
    

file_name = input("pypp>>>")
#input style is like pypp_filename -o py_filename
file_name = file_name.split("-o")

with open(file_name[0].strip(), "r") as f:
    tarfile = f.read()




#main cause im too lazy
with open(file_name[1].strip(), "w") as destfile:
    print("Convert Init\n\n\n\n\n\n\n\n")
    tarfile = tarfile.splitlines()
    declared_types = {}
    #doing line by line
    destfile.write("""
    class TypedValue:
        def __init__(self, value, expected_type):
            self.value = value
            self.expected_type = expected_type

        def checkTE(self):
            if not isinstance(self.value, self.expected_type):
                raise TypeError(f"Expected {self.expected_type.__name__} as type for value {self.value}")
    """.strip() + "\n\n")

    for line in tarfile:
        if line:
            if line[0] == "*":
                line = line[1:].strip()
                parts = line.split("=", 1)

                left = parts[0].strip()
                right = parts[1].strip()

                typename, varname = left.split()

                declared_types[varname] = typename

                destfile.write(f"{varname} = TypedValue({right}, {typename})\n")
                destfile.write(f"{varname}.checkTE()\n")
            else:
                destfile.write(line)
        
        else:
            continue

        print(line)