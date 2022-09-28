# run this by running the command: python3 filename x y

# import a library to handle arguments being passed through a command
import sys

# pass the arguments (argv) and transform them into a list, into a variable (arguments_list)
arguments_list = list(sys.argv)

# get the first argument
number_1 = arguments_list[1]

# get the second argument
number_2 = arguments_list[2]

# print the sum of both
print(int(number_1) + int(number_2))