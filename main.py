import sys

file_name = input("pypp>>>")
file_name = file_name.split("-o")

with open(file_name[0].strip(), "r") as f:
    tarfile = f.read()

with open(file_name[1].strip(), "w") as destfile:
    print("Convert Init\n\n\n\n\n\n\n\n")
    tarfile = tarfile.splitlines()

    typedvalue_code = [
        "class TypedValue:",
        "    def __init__(self, value, expected_type):",
        "        self.value = value",
        "        self.expected_type = expected_type",
        "",
        "    def checkTE(self):",
        "        if not isinstance(self.value, self.expected_type):",
        "            if self.expected_type == 'var' or self.expected_type == 'const':",
        "                pass",
        "            else:",
        "                print(f'ERROR: Wrong DataType error for value: {self.value} and type: {self.expected_type}')",
        "                exit()",
        ""
    ]

    varandtypes = {}

    for line in typedvalue_code:
        destfile.write(line + "\n")

    for line in tarfile:
        line = line.rstrip()
        if not line:
            continue

        if line.endswith(";"):
            line = line.rstrip(";")

        if line.startswith("*"):
            line = line[1:].strip()
            parts = line.split("=", 1)

            if len(parts) != 2:
                continue

            left = parts[0].strip()
            right = parts[1].strip()
            typename, varname = left.split()

            if varname in varandtypes:
                prev_type = varandtypes[varname]
                if prev_type != typename:
                    print(f"ERROR: Variable '{varname}' already declared as '{prev_type}', not '{typename}'")
                    exit()
                if prev_type == "const":
                    continue  # skip redefining const

            varandtypes[varname] = typename

            if typename == "var":
                destfile.write(f"{varname} = TypedValue({right}, '{typename}')\n")
            else:
                destfile.write(f"{varname} = TypedValue({right}, {typename})\n")
                destfile.write(f"{varname}.checkTE()\n")

        elif line.startswith("#define"):
            parts = line.split()
            if len(parts) >= 3:
                const_name = parts[1]
                const_value = parts[2]

                if const_name in varandtypes:
                    print(f"ERROR: Constant '{const_name}' already defined.")
                    exit()

                varandtypes[const_name] = "const"
                destfile.write(f"{const_name} = TypedValue({const_value}, 'const')\n")

        elif line.rstrip().endswith("{"):
            line = line.replace("{", ":")
            destfile.write(line + "\n")
        elif line == "}":
            continue
        
        else:
            destfile.write(line + "\n")
