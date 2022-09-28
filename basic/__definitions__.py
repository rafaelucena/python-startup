# This is a file to illustrate some keywords and what happens when we use them in Python

### . "#" comments
#
#   Comments are a very important part of the code, specially because it's IGNORED by
#   the code. They are important because they are made to tell the computer what parts
#   of our script should not do anything. In this case they are mostly used for documenting
#   the code, when you need to explain why you wrote a line in one specific way for example
#   or why one library needs to be import
#
#   To uncomment something, you just need to remove the # that preceeds it and the code will
#   then try to perform an action to that line that was previously ignored

# . "import":
#
#   This is a keyword to bring a module or library into our own code we use this simply
#   because our "script" is quite limited in it's raw form so, often, we need to import
#   a library to handle several things that we don't to rewrite on our own, in this case
#   I'm importing the sys library
import sys

### . single "variables":
#
#   Variables are places where we store information for our code, given they are "variables"
#   there's an implicit understanding that the values inside of them can change inside the
#   spectrum of the type of data they are.
#
#   In this example, my variable is called "my_variable", and it holds a 3 characters sized
#   string with the content "Run".
my_variable = 'Run'

#   If you want to see what's inside of it, uncomment the next line
# print(my_variable)

### . list "variables":
#
#   List variables are also places for storing information, it behaves similarly as the single
#   variables one, except it holds a list with very specific addresses assigned to it, each
#   address is called an "index".
#
#   In this example, my list is called "my_list", and it holds 3 integers, meaning the list
#   has a size 3 being that the first element is into the index 0 and the last into the index 2.
my_list = [1,2,3]

#   If you want to see what's inside of it, uncomment the next line
# print(my_list)

#   If you want to see what's inside an specific position of the list, uncomment the next line
# print(my_list[0])

### . the "print" method
#
#   Methods is how we call functions that might or might not receive arguments while performing
#   an specific job. The "print" method will output to the terminal any kind of information that's
#   passed to it. It's mostly used to identify the content of some variables or to try and identify
#   errors in very specific parts of a script. In our case we are "printing" the variables so we know
#   our code is working or how is it working

### . the "casting" methods
#
#   Casting is when we want one specific type of data to be presented as a different one, or a more
#   specific one. If you have a string "1234", it will behave as a text for every other operation until
#   it's casted specifically to a numerical value, either by using the method int() or float().
#
#   Float is also used for numbers, but in this case is for any kind of numbers that needs a bigger
#   precision than simply integers.

# . Math operators (sum, subtraction, division, multiplication)
#
#   They work as in most languages with the basic operators, it is recommended though that we wrap
#   each statement into curved brackets () just so you can make sure the result is what we expect to see
my_next_variable = (((5+4) - 3)/2) * 1

#   If you want to see what's inside of it, uncomment the next line
# print(my_next_variable)