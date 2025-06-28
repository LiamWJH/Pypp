import subprocess, sys
import ast

def installpkg(packagename):
    subprocess.check_call([sys.executable, "-m", "pip", "install", packagename])

try:
    import pyinstaller
except ImportError as IE:
    installpkg("pyinstaller")

   

file_name = input("pypp>>>")
#input style is like pypp_filename -o py_filename
file_name = file_name.split("-o")

with open(file_name[0].strip(), "r") as f:
    tarfile = f.read()




#main cause im too lazy
with open(file_name[1].strip(), "w") as destfile:
    print("Convert Init\n\n\n\n\n\n\n\n")
    exetarfile = tarfile
    tarfile = tarfile.splitlines()

    #class for variables and types
    typedvalue_code = [
        "class TypedValue:",
        "    def __init__(self, value, expected_type):",
        "        self.value = value",
        "        self.expected_type = expected_type",
        "",
        "    def checkTE(self):",
        "",
        "",
        "        if not isinstance(self.value, self.expected_type):",
        "            if self.expected_type == 'var':",
        "                 pass",
        "            else:",
        "                 print('ERROR: Wrong DataType error!')",
        "                 exit()",
        "",
        ""
    ]

    for line in typedvalue_code:
        destfile.write(line + "\n")

    #doing line by line
    for line in tarfile:
        if line:            
            if line[-1] == ";":
                line = line.strip(";")

            if line[0] == "*":
                line = line[1:].strip()
                parts = line.split("=", 1)

                left = parts[0].strip()
                right = parts[1].strip()

                typename, varname = left.split()
                if typename == "var":
                    destfile.write(f"{varname} = TypedValue({right}, '{typename}')\n")

                else:
                    destfile.write(f"{varname} = TypedValue({right}, {typename})\n")
                    destfile.write(f"{varname}.checkTE()\n")

            else:
                destfile.write(f"{line}\n")

        
        else:
            continue