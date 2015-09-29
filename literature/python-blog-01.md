# Introduction to Python

## Python prerequisites

* Python is an interpreted language
When you install Python on your computer you are installing a Python interpreter application and a standard library of packages and modules.  Python is an interpreted language like Java, JavaScript, and Ruby; it is not a "compiled" language.  Python is dynamically typed.

### Python is duck-typed

A name (or variable) in Python points to an object, and that object can be anything! You don't have to tell the interpreter what your variable name is pointing to. This is a very powerful quality of the language when you want to get something mildly complicated written very quickly. You will rarely need to write things like interfaces, abstract base classes, or class factories. For example, say you are writing a function called "sum"

```
def sum(list_of_nums):
    '''Iterates over input argument and adds up the elements'''
    s = 0.0
    for x in list_of_nums:
        s += x
    return s
```

You don't have to worry about whether or not the user passed you a list, or even if that list has only numbers in it! If the user gave you an object that you can't iterate over then your function will raise an exception at the `for x in list_of_nums` statement. If the user gave you an iterable object that contains something you can't add then your function will raise an exception at the `s += x` statement. Be aware of the qualities of input arguments that you are expecting to have when you write code like this, and document it. Then the onus is on the user to handle the exception that will get thrown when they pass inappropriate arguments to your function. If you don't then your users aren't going be behave nicely when they use your code, or they just won't use it and then you've wasted your time writing it.

**You are expected you write beautiful and well-documented code for a reasonable user.**

### Passing by value and by reference

*Everything is passed by reference*, keep that in mind at all times. There are ways to make things behave like we are passing by value, and knowing how is a good lesson in the fundamental concepts of Python. Remember that all of your variables are actually names pointing to objects, when you call a function with one of your variables as an argument you are telling the function to work with that object, not a copy of it. The key to getting "pass by value" behavior is to pass immutable object as arguments, this way it the function tries to modify the object it will either have to make a copy or it will end up causing an exception to be raised.

In Python these issues boil down to trust, manners, and good coding practice. As a developer you will not have permission keywords like "const", "final", or "private" to lean on, you need to write code that has good structure and is easy to understand.

### Some basic manners

Avoid modifying input arguments.  If you can just as easily copy, modify, and return an object, then do that.  If you really need to modify an input object, then you should be writing a method for that class.  Think about how sorting is done in Python. There is a function called "sorted" which takes in a sequence (potential mutable) and return a new version on the object with a different order. On the other hand, the list class has a method called "sort". This method will modify the object instance it is called from.

```
# This is a list, remember these are mutable
a = [5, 6, 1, 24, -6, 0]
a_sorted = sorted(a)
# The sorted function politely did not modify our list
print('a = {}'.format(a))
# Instead it gave us a new copy that is sorted
print('b = {}'.format(b))
# The sort method will modify our object
print('a = {}'.format(a))
```

Output

```
a = [5, 6, 1, 24, -6, 0]
b = [-6, 0, 1, 5, 6, 24]
a = [-6, 0, 1, 5, 6, 24]
```

**Rule of thumb**: Functions should not modify arguments, methods should. (`output = func(input)`, `object.modify_me()`)

Nothing is private in Python. Think about it this way; since Python is an interpreted language in order to run code you *must* have the source code, if something was marked private you could just modify the code to make it not private. Therefore, a "private" keyword would be pointless in Python. In Python you cannot write walls into your code, only curtains.  You are making a simple deal with the user of your code: "I will write you beautiful, easy to use code, and then you won't have to look behind the curtain."

**Make it easy to do the right thing, because you can't prevent other programmers from doing anything**

How do you raise some curtains to let the user know what's out-of-bounds? There is a Python-wide style standard for denoting things you wish to be treated as thought they are private, a leading underscore.  For example a "private" attribute or method would be named something like `_my_hidden_stuff`.  You can't stop a bad developer from messing with your `_my_hidden_stuff`, but you also aren't expected to have your code work properly once they do. That should be good enough, use that *single* leading underscore to let the user know what they can and should not touch. Your default should be to leave things "public", because in reality they all are. If you find that your code really will start to fall apart when a user starts touching or using something, then and only then put up a curtain.

**Rule of thumb**: Don't touch other people's stuff. A leading underscore is your sign that you are flirting with trouble. (`._please_dont_touch`)

## Things you might want to do with Python

* Write a script
* Analyze some data
* Develop a package
* Glue code together

## Learn to walk

1. Write a simple

## Writing Scripts

* Know how to write regular expressions
* The xml module
* Know how to navigate and manipulate files/folders
* Know how to read and write files
* Know how to manipulate strings

## Being a Pythonista

* duck-typing

## Advanced topics (that are useful)

* Python 2 vs. 3
* magic methods (e.g operator overloading)
* "private" variables
* Modifying the global path
* Decorators
* The multiprocessing module
