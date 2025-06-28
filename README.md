# Pypp
Python superset **in work**

# IMPORTANT
if planning to use and not building the project from source, go to any release in the release page and download any stable release _marked by (stable)_ and put in in the folder where your .pypp file lives and run to compile the file, rest are down below

# Intro
 - adds datatypes
 - adds semicolon
 - adds curly braces
 - Etc

# Main

the PYpp is called PY++ similar as Typescript is to Javascript and C++ is to C PY++ is to Python. The project has a MIT license which means everything is open source and anybody can contribute. Feel free to do so. Back into what i was talking about, when you run the compiler.py placed in the same folder as the _pypp_ file eg(main.pypp) it asks you the file you want to target and compiles the **.pypp** into a **.py**. The way to input the compiler is to type in commands in form of:
>filname.pypp -o destinationfile.py\
this will automatically write to the destination file.

In terms of syntax everything is very simple, except for variables that have data types you have to declare it in the form of:
>*datatype varname = value
Important thing to note is that reassignment to different data types on these **Non-Vanilla** variables will cause error

For other changes of now you can write code blocks like if and while not like vanilla python using _:_ but using _{}_ like Java or Rust.
>if 2 < 4 {
>  print("Hi")    
>}
Also missing out the end brace wont cause errors, however the starting braces need to be on the **same line** as the conditional and statement

Otherwise we have semicolons like C or Javascript that is also optional
>code;

Last but not least we have the _const_ variables. This is a very special thing compared to others, as the syntax goes like:
>#define varname varvalue
this value as you may guess cannot be changed though out the program if done similar error will rise. 
