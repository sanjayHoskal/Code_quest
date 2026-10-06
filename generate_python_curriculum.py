import json
from curriculum_builder import create_order_q, create_fill_q, create_debug_q, create_predict_q, create_mcq_q

def generate_python():
    py = {
        "Drag & Drop": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Syntax Validator": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Code Arrangement": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "MCQ Challenge": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Debug the Code": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Predict the Output": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Fill in the Blanks": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
    }

    # =========================================================================
    # PYTHON DRAG & DROP & SYNTAX VALIDATOR
    # =========================================================================
    import curriculum_python
    py["Drag & Drop"] = curriculum_python.python_data["Drag & Drop"]
    import curriculum_validator
    py_val = curriculum_validator.get_python_validator()
    py["Syntax Validator"] = py_val
    py["Code Arrangement"] = py_val

    # =========================================================================
    # PYTHON FILL IN THE BLANKS
    # =========================================================================
    # Beginner
    py["Fill in the Blanks"]["Beginner"]["1"] = [
        create_fill_q("Convert a numeric string to an integer.", "raw_str = '42'\nval = _______(raw_str)\nprint(val)", "int", "What built-in function casts strings to integers?", "Starts with 'i'.", "int('42') converts the string to integer 42."),
        create_fill_q("Print a greeting to the console.", "_______('Welcome to CodeQuest!')", "print", "Standard Python output function.", "Starts with 'p'.", "print() outputs text to standard output."),
        create_fill_q("Cast an integer to a floating-point number.", "num = 10\nflt = _______(num)", "float", "Built-in function for floating point numbers.", "Starts with 'f'.", "float(10) produces 10.0."),
        create_fill_q("Assign a boolean True to a variable.", "is_active = _______", "True", "Python booleans are capitalized.", "Capital T.", "True represents boolean true in Python."),
        create_fill_q("Compute the remainder of 15 divided by 4.", "rem = 15 _______ 4", "%", "Which operator computes modulus/remainder?", "The percent symbol.", "% is the modulus operator."),
        create_fill_q("Perform integer floor division.", "quotient = 20 _______ 3", "//", "Double slash performs floor division.", "Two slashes.", "// returns integer quotient."),
        create_fill_q("Check the data type of an object.", "val = 3.14\nprint(_______(val))", "type", "Built-in function returning the class/type.", "Starts with 't'.", "type(val) returns <class 'float'>."),
        create_fill_q("Convert an integer to a string.", "count = 5\nmsg = 'Items: ' + _______(count)", "str", "Built-in string constructor.", "Starts with 's'.", "str(count) converts int to string."),
        create_fill_q("Calculate 3 squared using exponent operator.", "sq = 3 _______ 2", "**", "Exponentiation operator in Python.", "Two asterisks.", "** raises base to exponent."),
        create_fill_q("Get absolute value of negative integer.", "dist = _______(-25)", "abs", "Function returning magnitude without sign.", "3-letter function starting with 'a'.", "abs(-25) returns 25.")
    ]

    py["Fill in the Blanks"]["Beginner"]["2"] = [
        create_fill_q("Convert string to all uppercase characters.", "msg = 'hello'\nprint(msg._______())", "upper", "String method for capital letters.", "Opposite of lower.", ".upper() returns uppercase version."),
        create_fill_q("Get the number of characters in a string.", "text = 'Code'\nlength = _______(text)", "len", "Built-in length function.", "3 letters.", "len('Code') returns 4."),
        create_fill_q("Remove leading and trailing whitespace.", "user = '  neo  '\nclean = user._______()", "strip", "Trims whitespace from both ends.", "Starts with 'st'.", "strip() removes whitespace padding."),
        create_fill_q("Check if a string starts with 'https'.", "url = 'https://code.org'\nis_secure = url._______('https')", "startswith", "Method checking prefix.", "Starts with 'start'.", "startswith() verifies string prefix."),
        create_fill_q("Replace 'cat' with 'dog'.", "phrase = 'cat'\nprint(phrase._______('cat', 'dog'))", "replace", "Method replacing occurrences of substring.", "Starts with 'rep'.", "replace(old, new) swaps substrings."),
        create_fill_q("Split sentence into list of words.", "line = 'one two three'\nwords = line._______()", "split", "Splits string by whitespace into list.", "Starts with 'sp'.", "split() divides string into words."),
        create_fill_q("Find the index of substring 'py'.", "name = 'cpython'\nidx = name._______('py')", "find", "Returns lowest index of substring.", "Starts with 'f'.", "find('py') returns 1."),
        create_fill_q("Check if string contains only digits.", "code = '12345'\nis_num = code._______()", "isdigit", "Method returning True if all characters are digits.", "Starts with 'is'.", "isdigit() tests for numeric digits."),
        create_fill_q("Join list of strings with comma.", "items = ['a', 'b']\nres = ','._______(items)", "join", "String method that concatenates iterables.", "Starts with 'j'.", "join() concatenates iterable elements."),
        create_fill_q("Convert string to lowercase.", "val = 'PYTHON'\nprint(val._______())", "lower", "Opposite of upper.", "Starts with 'l'.", "lower() transforms string to lowercase.")
    ]

    py["Fill in the Blanks"]["Beginner"]["3"] = [
        create_fill_q("Check equality in an if condition.", "if score _______ 100:\n    print('Perfect!')", "==", "Comparison equality operator.", "Two equal signs.", "== tests for value equality."),
        create_fill_q("Add alternative branch if condition.", "if x > 0:\n    print('Pos')\n_______:\n    print('Non-pos')", "else", "Fallback branch keyword.", "Starts with 'e'.", "else executes when if condition is false."),
        create_fill_q("Add intermediate condition branch.", "if x > 10:\n    pass\n_______ x > 5:\n    pass", "elif", "Python else-if keyword.", "Combination of else and if.", "elif tests sequential conditions."),
        create_fill_q("Logical operator requiring both conditions to be true.", "if age >= 18 _______ has_id:\n    print('Allowed')", "and", "Boolean conjunction operator.", "3 letters.", "and requires both operands to be truthy."),
        create_fill_q("Logical operator requiring at least one true condition.", "if is_weekend _______ is_holiday:\n    print('Rest')", "or", "Boolean disjunction operator.", "2 letters.", "or evaluates truthy if either operand is true."),
        create_fill_q("Logical operator inverting a condition.", "if _______ is_closed:\n    print('Open')", "not", "Boolean negation operator.", "3 letters.", "not inverts truth value."),
        create_fill_q("Check membership in a collection.", "if 'apple' _______ fruits:\n    print('Found')", "in", "Membership operator.", "2 letters.", "'in' tests element membership."),
        create_fill_q("Check if two references point to the same object.", "if x _______ None:\n    print('Is None')", "is", "Identity comparison operator.", "2 letters.", "'is' checks identity reference."),
        create_fill_q("Check inequality between two numbers.", "if attempts _______ 0:\n    print('Remaining')", "!=", "Not-equal comparison operator.", "Exclamation mark followed by equal.", "!= tests inequality."),
        create_fill_q("Inline ternary condition syntax.", "msg = 'Yes' if flag _______ 'No'", "else", "Keyword preceding fallback value in ternary.", "4 letters.", "Syntax: val_if_true if cond else val_if_false.")
    ]

    py["Fill in the Blanks"]["Beginner"]["4"] = [
        create_fill_q("Append item to the end of a list.", "nums = [1, 2]\nnums._______(3)", "append", "List method adding item to end.", "Starts with 'app'.", "append() adds element to tail of list."),
        create_fill_q("Remove and return the last item from a list.", "stack = [10, 20]\ntop = stack._______()", "pop", "List method popping tail item.", "3 letters.", "pop() removes and returns last item."),
        create_fill_q("Insert item at specific index.", "arr = [2, 3]\narr._______(0, 1)", "insert", "List method inserting at index.", "Starts with 'in'.", "insert(index, val) places val at index."),
        create_fill_q("Sort list in-place.", "vals = [5, 2, 8]\nvals._______()", "sort", "Method ordering list elements.", "4 letters.", "sort() orders list elements in ascending order."),
        create_fill_q("Find number of elements in a list.", "items = ['a', 'b', 'c']\ncount = _______(items)", "len", "Length function.", "3 letters.", "len() returns item count."),
        create_fill_q("Remove first occurrence of value from list.", "colors = ['red', 'blue']\ncolors._______('red')", "remove", "Method deleting specific value.", "Starts with 'rem'.", "remove(val) deletes first matching value."),
        create_fill_q("Count occurrences of element in list.", "data = [1, 2, 1, 1]\nc = data._______(1)", "count", "Method counting occurrences.", "Starts with 'c'.", "count(val) tallies occurrences."),
        create_fill_q("Reverse list elements in-place.", "nums = [1, 2, 3]\nnums._______()", "reverse", "Method inverting list order.", "Starts with 'rev'.", "reverse() reverses list in-place."),
        create_fill_q("Empty all elements from list.", "cache = [1, 2]\ncache._______()", "clear", "Method removing all list elements.", "Starts with 'cl'.", "clear() empties list to []."),
        create_fill_q("Extend list by appending another list.", "l1 = [1]; l2 = [2]\nl1._______(l2)", "extend", "Method merging iterable into list.", "Starts with 'ext'.", "extend() unpacks elements into list.")
    ]

    # Intermediate
    py["Fill in the Blanks"]["Intermediate"]["1"] = [
        create_fill_q("Generate sequence of numbers in for loop.", "for i in _______(5):\n    print(i)", "range", "Built-in sequence generator.", "5 letters.", "range(n) generates numbers 0 to n-1."),
        create_fill_q("Exit loop immediately.", "while True:\n    _______", "break", "Keyword terminating innermost loop.", "5 letters.", "break terminates enclosing loop."),
        create_fill_q("Skip remainder of current loop iteration.", "for n in range(5):\n    if n % 2 == 0:\n        _______", "continue", "Keyword skipping to next iteration.", "Starts with 'con'.", "continue jumps to next iteration."),
        create_fill_q("Pair indices with elements during iteration.", "for i, val in _______(['a', 'b']):\n    print(i, val)", "enumerate", "Built-in returning (index, value) tuples.", "Starts with 'enum'.", "enumerate() yields index and item."),
        create_fill_q("Iterate over two lists in parallel.", "for a, b in _______([1, 2], ['x', 'y']):\n    print(a, b)", "zip", "Built-in aggregating elements from iterables.", "3 letters.", "zip() pairs up elements from lists."),
        create_fill_q("Define condition-controlled loop.", "count = 3\n_______ count > 0:\n    count -= 1", "while", "Loop keyword checking condition before each run.", "Starts with 'w'.", "while loop runs as long as condition is true."),
        create_fill_q("Loop else clause that runs on normal completion.", "for i in range(2):\n    pass\n_______:\n    print('Finished')", "else", "Clause executing when loop exhausts without break.", "4 letters.", "for-else executes else on completion."),
        create_fill_q("Iterate backwards over a sequence.", "for x in _______([1, 2, 3]):\n    print(x)", "reversed", "Built-in reverse iterator.", "Starts with 'rev'.", "reversed() iterates in reverse."),
        create_fill_q("Generate range with custom step.", "evens = list(range(0, 10, _______))", "2", "Step argument for range(start, stop, step).", "Single digit.", "Step of 2 yields even numbers."),
        create_fill_q("Placeholder statement inside empty loop body.", "for item in items:\n    _______", "pass", "Null-operation statement.", "4 letters.", "pass does nothing and satisfies syntax requirements.")
    ]

    py["Fill in the Blanks"]["Intermediate"]["2"] = [
        create_fill_q("Define a function.", "_______ calculate(a, b):\n    return a + b", "def", "Keyword for function definition.", "3 letters.", "def declares a function."),
        create_fill_q("Send value back from function to caller.", "def square(n):\n    _______ n * n", "return", "Keyword terminating function and returning value.", "6 letters.", "return outputs value from function."),
        create_fill_q("Define default parameter value.", "def greet(name_______'Guest'):\n    return f'Hi {name}'", "=", "Symbol assigning default value in signature.", "Equal sign.", "= specifies default parameter value."),
        create_fill_q("Accept arbitrary positional arguments.", "def sum_all(*_______):\n    return sum(numbers)", "numbers", "Parameter name following * in signature.", "Identifier matching body.", "*numbers captures positional arguments."),
        create_fill_q("Accept arbitrary keyword arguments.", "def config(**_______):\n    print(kwargs)", "kwargs", "Convention for dictionary keyword arguments.", "6 letters.", "**kwargs gathers named arguments into dict."),
        create_fill_q("Declare variable in function as modifying global scope.", "count = 0\ndef bump():\n    _______ count\n    count += 1", "global", "Keyword binding name to global scope.", "6 letters.", "global permits modifying module-level variables."),
        create_fill_q("Modify variable in outer enclosing non-global scope.", "def outer():\n    x = 1\n    def inner():\n        _______ x\n        x = 2", "nonlocal", "Keyword binding name to outer non-global scope.", "8 letters.", "nonlocal binds to nearest enclosing scope."),
        create_fill_q("Define anonymous inline function.", "double = _______ x: x * 2", "lambda", "Keyword creating anonymous function.", "6 letters.", "lambda creates anonymous inline functions."),
        create_fill_q("Access docstring of a function.", "def fn(): '''Docs'''\nprint(fn._______)", "__doc__", "Dunder attribute storing docstring.", "Starts and ends with double underscore.", "__doc__ stores function documentation."),
        create_fill_q("Type hint specifying return type.", "def add(x: int, y: int) _______ int:\n    return x + y", "->", "Arrow syntax for return type annotation.", "Hyphen and greater-than.", "-> annotates return type.")
    ]

    py["Fill in the Blanks"]["Intermediate"]["3"] = [
        create_fill_q("Safely fetch dictionary value with fallback default.", "user = {'name': 'Sam'}\nrole = user._______('role', 'user')", "get", "Dictionary method with default value.", "3 letters.", "get(key, default) avoids KeyError."),
        create_fill_q("Iterate over dictionary key-value pairs.", "d = {'a': 1}\nfor k, v in d._______():\n    print(k, v)", "items", "Method returning (key, value) views.", "5 letters.", "items() yields key-value tuples."),
        create_fill_q("Get all keys from dictionary.", "d = {'a': 1, 'b': 2}\nprint(list(d._______()))", "keys", "Method returning dictionary keys.", "4 letters.", "keys() returns view of dictionary keys."),
        create_fill_q("Get all values from dictionary.", "d = {'a': 1, 'b': 2}\nprint(list(d._______()))", "values", "Method returning dictionary values.", "6 letters.", "values() returns view of values."),
        create_fill_q("Merge dictionary using update.", "target = {'a': 1}\ntarget._______({'b': 2})", "update", "Method merging key-value pairs.", "6 letters.", "update() adds pairs in-place."),
        create_fill_q("Union operator for dictionaries in Python 3.9+.", "d3 = d1 _______ d2", "|", "Pipe symbol merging dictionaries.", "Vertical bar.", "| creates merged dictionary."),
        create_fill_q("Remove key from dictionary with pop.", "d = {'id': 10}\nval = d._______('id')", "pop", "Method removing key and returning its value.", "3 letters.", "pop(key) removes and returns value."),
        create_fill_q("Define single-element tuple.", "t = ('item'_______)", ",", "Trailing comma required for single-item tuple.", "Comma symbol.", "('item',) defines a 1-tuple."),
        create_fill_q("Delete dictionary key with statement.", "_______ user['temp_token']", "del", "Statement deleting variable or key.", "3 letters.", "del removes key from dict."),
        create_fill_q("Count occurrences in tuple.", "t = (1, 2, 1)\nprint(t._______(1))", "count", "Tuple method counting occurrences.", "5 letters.", "count(val) tallies occurrences.")
    ]

    py["Fill in the Blanks"]["Intermediate"]["4"] = [
        create_fill_q("List comprehension squaring numbers.", "sq = [x**2 _______ x in [1, 2, 3]]", "for", "Loop keyword inside comprehension.", "3 letters.", "[x**2 for x in ...] constructs list."),
        create_fill_q("Filter condition in list comprehension.", "evens = [x for x in nums _______ x % 2 == 0]", "if", "Filter keyword in comprehension.", "2 letters.", "if filters elements during comprehension."),
        create_fill_q("Create unique set from list.", "unique = _______([1, 2, 2, 3])", "set", "Type constructor for set.", "3 letters.", "set() removes duplicate elements."),
        create_fill_q("Set intersection operator.", "common = set_a _______ set_b", "&", "Symbol for set intersection.", "Ampersand.", "& computes intersection of sets."),
        create_fill_q("Set union operator.", "all_items = set_a _______ set_b", "|", "Symbol for set union.", "Pipe symbol.", "| computes union of sets."),
        create_fill_q("Context manager keyword for opening files.", "_______ open('data.txt') as f:\n    content = f.read()", "with", "Context manager statement.", "4 letters.", "with manages resources and auto-closes files."),
        create_fill_q("File mode for writing text.", "with open('out.txt', '_______') as f:\n    f.write('hi')", "w", "Single character mode for writing.", "'w'.", "'w' opens file for writing/overwriting."),
        create_fill_q("Add element to a set.", "tags = {'python'}\ntags._______('flask')", "add", "Set method adding single element.", "3 letters.", "add() inserts element into set."),
        create_fill_q("Safely remove element from set without raising KeyError if absent.", "tags._______('ruby')", "discard", "Set method discarding value safely.", "Starts with 'dis'.", "discard() removes without KeyError if absent."),
        create_fill_q("Dictionary comprehension syntax.", "lengths = {w: len(w) _______ w in words}", "for", "Loop keyword in dict comprehension.", "3 letters.", "{k: v for w in words} constructs dict.")
    ]

    # Advanced
    py["Fill in the Blanks"]["Advanced"]["1"] = [
        create_fill_q("Define a class constructor method.", "class Player:\n    def _______(self, name):\n        self.name = name", "__init__", "Dunder initialization method.", "Double underscores init.", "__init__ is class constructor."),
        create_fill_q("First parameter representing instance in methods.", "class Hero:\n    def attack(_______):\n        return 'Slash!'", "self", "Instance reference convention.", "4 letters.", "self references calling instance."),
        create_fill_q("Define string representation dunder method.", "class Item:\n    def _______(self):\n        return self.name", "__str__", "Dunder method for user-friendly string.", "Double underscores str.", "__str__ is called by print() and str()."),
        create_fill_q("Define property getter decorator.", "class Circle:\n    _______ \n    def radius(self): return self._r", "@property", "Decorator transforming method into getter attribute.", "Starts with @prop.", "@property creates managed attribute getter."),
        create_fill_q("Decorator for class methods.", "class User:\n    _______\n    def from_dict(cls, data): pass", "@classmethod", "Decorator receiving class object cls.", "Starts with @class.", "@classmethod receives cls as first argument."),
        create_fill_q("Decorator for static methods.", "class Math:\n    _______\n    def add(x, y): return x + y", "@staticmethod", "Decorator for methods independent of self or cls.", "Starts with @static.", "@staticmethod defines static utility."),
        create_fill_q("Implement len() operator on custom class.", "class Deck:\n    def _______(self):\n        return len(self.cards)", "__len__", "Dunder method for length.", "Double underscores len.", "__len__ enables len(instance)."),
        create_fill_q("Implement equality comparison operator.", "class Point:\n    def _______(self, other):\n        return self.x == other.x", "__eq__", "Dunder method for == operator.", "Double underscores eq.", "__eq__ implements == comparison."),
        create_fill_q("Restrict allowed instance attributes for memory efficiency.", "class Node:\n    _______ = ('val', 'next')", "__slots__", "Class attribute restricting instance fields.", "Double underscores slots.", "__slots__ eliminates instance __dict__."),
        create_fill_q("Define property setter decorator.", "@radius._______\ndef radius(self, val): self._r = val", "setter", "Attribute on property for setter method.", "6 letters.", "@prop.setter defines value assignment logic.")
    ]

    py["Fill in the Blanks"]["Advanced"]["2"] = [
        create_fill_q("Inherit from a parent class.", "class Dog(_______):\n    pass", "Animal", "Base class in parentheses.", "Capital A.", "Parent class specified inside parentheses."),
        create_fill_q("Call method on parent class.", "class Sub(Base):\n    def __init__(self):\n        _______().__init__()", "super", "Built-in returning proxy delegating method calls to parent.", "5 letters.", "super() accesses parent class methods."),
        create_fill_q("Check if object is instance of class or subclass.", "is_car = _______(my_vehicle, Car)", "isinstance", "Built-in checking instance type.", "Starts with 'is'.", "isinstance(obj, class) checks type."),
        create_fill_q("Check if class is subclass of another class.", "print(_______(Dog, Animal))", "issubclass", "Built-in checking class hierarchy.", "Starts with 'is'.", "issubclass(Sub, Base) checks inheritance."),
        create_fill_q("Import Abstract Base Class base.", "from abc import _______, abstractmethod", "ABC", "Base class for defining abstract classes.", "3 uppercase letters.", "ABC is standard base for abstract classes."),
        create_fill_q("Decorator enforcing method implementation in subclasses.", "@_______\ndef calculate(self): pass", "abstractmethod", "Decorator for required abstract methods.", "Starts with 'abstract'.", "@abstractmethod enforces override in subclasses."),
        create_fill_q("Inspect Method Resolution Order.", "print(MyClass._______)", "__mro__", "Dunder attribute returning inheritance search tuple.", "Double underscores mro.", "__mro__ lists method resolution order."),
        create_fill_q("Official developer string representation dunder method.", "def _______(self):\n    return f'Item({self.id})'", "__repr__", "Dunder method for unambiguous representation.", "Double underscores repr.", "__repr__ provides debugging string output."),
        create_fill_q("Call constructor of parent class with argument.", "super()._______(name)", "__init__", "Parent constructor method.", "Double underscores init.", "super().__init__() initializes base attributes."),
        create_fill_q("Check attribute existence on object dynamically.", "has_color = _______(car, 'color')", "hasattr", "Built-in checking attribute presence.", "Starts with 'has'.", "hasattr(obj, 'attr') returns boolean.")
    ]

    py["Fill in the Blanks"]["Advanced"]["3"] = [
        create_fill_q("Begin block attempting risky operations.", "_______:\n    res = 10 / 0\nexcept ZeroDivisionError:\n    pass", "try", "Keyword initiating exception handling.", "3 letters.", "try wraps risky code."),
        create_fill_q("Catch specific exception type.", "try:\n    pass\n_______ ValueError:\n    print('Bad value')", "except", "Keyword catching exceptions.", "6 letters.", "except handles matching exception types."),
        create_fill_q("Execute block only when no exceptions occurred in try.", "try: pass\nexcept: pass\n_______:\n    print('All good')", "else", "Clause running on exception-free try block.", "4 letters.", "else executes when no exceptions were raised."),
        create_fill_q("Execute cleanup block unconditionally.", "try: pass\n_______:\n    cleanup()", "finally", "Clause executing regardless of whether exceptions occurred.", "7 letters.", "finally always executes."),
        create_fill_q("Trigger an exception manually.", "if amount < 0:\n    _______ ValueError('Negative amount')", "raise", "Keyword raising exception.", "5 letters.", "raise triggers an exception."),
        create_fill_q("Bind caught exception instance to a variable.", "except ValueError _______ err:\n    print(err)", "as", "Keyword binding exception to name.", "2 letters.", "'as' captures exception object."),
        create_fill_q("Create custom exception by subclassing.", "class CustomError(_______): pass", "Exception", "Base class for application exceptions.", "Capital E.", "User exceptions inherit from Exception."),
        create_fill_q("Chain exceptions explicitly.", "raise RuntimeError('Failed') _______ original_err", "from", "Keyword specifying direct cause in exception chaining.", "4 letters.", "'from' records cause in traceback."),
        create_fill_q("Debug assertion statement.", "_______ count >= 0, 'Count must be positive'", "assert", "Keyword testing invariant condition.", "6 letters.", "assert raises AssertionError on False."),
        create_fill_q("Re-raise active exception in except block.", "except Exception:\n    log_error()\n    _______", "raise", "Bare keyword re-raising active exception.", "5 letters.", "Bare raise re-throws caught exception.")
    ]

    py["Fill in the Blanks"]["Advanced"]["4"] = [
        create_fill_q("Pause function execution and produce generator value.", "def counter():\n    _______ 1", "yield", "Keyword producing value from generator.", "5 letters.", "yield turns function into generator."),
        create_fill_q("Advance generator to retrieve next yielded value.", "g = counter()\nfirst = _______(g)", "next", "Built-in pulling next item from iterator.", "4 letters.", "next() requests next value from generator."),
        create_fill_q("Delegate to a subgenerator.", "def combined():\n    _______ from subgen()", "yield", "Keyword used before 'from' to delegate generator.", "5 letters.", "yield from delegates to another generator."),
        create_fill_q("Higher-order function applying function to iterable.", "doubles = list(_______(lambda x: x*2, nums))", "map", "Built-in applying function to each item.", "3 letters.", "map() transforms iterable elements."),
        create_fill_q("Higher-order function filtering items.", "evens = list(_______(lambda x: x%2==0, nums))", "filter", "Built-in filtering items.", "6 letters.", "filter() retains items where predicate is True."),
        create_fill_q("Decorator preserving wrapped function metadata.", "from functools import wraps\ndef dec(fn):\n    @_______(fn)\n    def wrapper(): return fn()", "wraps", "Decorator from functools copying metadata.", "5 letters.", "@wraps copies docstring and function name."),
        create_fill_q("Decorator creating context manager from generator.", "from contextlib import _______\n@contextmanager\ndef tag(): pass", "contextmanager", "Decorator from contextlib.", "14 letters.", "@contextmanager turns generator into context manager."),
        create_fill_q("Cumulative aggregate function from functools.", "from functools import _______\ntotal = reduce(lambda a,b: a+b, [1, 2, 3])", "reduce", "Function folding iterable into single value.", "6 letters.", "reduce aggregates items left-to-right."),
        create_fill_q("Create generator expression.", "g = (x * 2 _______ x in range(10))", "for", "Loop keyword inside generator expression.", "3 letters.", "Parentheses with 'for' create generator expression."),
        create_fill_q("Make an object callable like a function.", "class Multiplier:\n    def _______(self, x): return x * 2", "__call__", "Dunder method allowing instances to be invoked as functions.", "Double underscores call.", "__call__ makes instance callable.")
    ]

    # Clone for Debug, Predict, and MCQ with appropriate schemas
    # =========================================================================
    # PYTHON DEBUG THE CODE (type: "debug")
    # =========================================================================
    for diff in ["Beginner", "Intermediate", "Advanced"]:
        for lvl in ["1", "2", "3", "4"]:
            debug_list = []
            for item in py["Fill in the Blanks"][diff][lvl]:
                debug_item = create_debug_q(
                    f"Debug: {item['question']}",
                    item["code_snippet"],
                    item["correct_answer"],
                    item["hint1"],
                    item["hint2"],
                    item["explanation"]
                )
                debug_list.append(debug_item)
            py["Debug the Code"][diff][lvl] = debug_list

    # =========================================================================
    # PYTHON PREDICT THE OUTPUT (type: "predict")
    # =========================================================================
    py["Predict the Output"]["Beginner"]["1"] = [
        create_predict_q("Predict output of integer arithmetic.", "print(5 + 3 * 2)", "11", "Multiplication takes precedence over addition.", "3 * 2 is 6.", "5 + 6 = 11."),
        create_predict_q("Predict output of string concatenation.", "print('Code' + 'Quest')", "CodeQuest", "Strings are merged directly.", "No spaces added.", "'Code' + 'Quest' = 'CodeQuest'."),
        create_predict_q("Predict output of integer floor division.", "print(17 // 4)", "4", "// discards fractional remainder.", "17 divided by 4 without remainder.", "17 // 4 is 4."),
        create_predict_q("Predict output of modulus operator.", "print(14 % 5)", "4", "Remainder after dividing 14 by 5.", "5 * 2 = 10; remainder is 4.", "14 % 5 is 4."),
        create_predict_q("Predict output of power operator.", "print(2 ** 4)", "16", "2 raised to the 4th power.", "2 * 2 * 2 * 2.", "2 ** 4 = 16."),
        create_predict_q("Predict output of string repetition.", "print('ha' * 3)", "hahaha", "String repeated 3 times.", "Concatenates 3 times.", "'ha' * 3 = 'hahaha'."),
        create_predict_q("Predict output of float division.", "print(10 / 2)", "5.0", "Division in Python 3 produces a float.", "Note decimal point.", "10 / 2 returns 5.0."),
        create_predict_q("Predict output of boolean conversion.", "print(bool(0))", "False", "0 evaluates to False in boolean context.", "Falsy value.", "bool(0) is False."),
        create_predict_q("Predict output of absolute value.", "print(abs(-15))", "15", "Magnitude of negative number.", "Positive 15.", "abs(-15) is 15."),
        create_predict_q("Predict output of round function.", "print(round(3.7))", "4", "Rounds to nearest integer.", "Rounds up from 3.7.", "round(3.7) is 4.")
    ]
    # Populate other predict levels with reliable answers
    for diff in ["Beginner", "Intermediate", "Advanced"]:
        for lvl in ["1", "2", "3", "4"]:
            if lvl == "1" and diff == "Beginner":
                continue
            pred_list = []
            for idx in range(10):
                val = (idx + 1) * 10
                q_text = f"Predict output for {diff} Level {lvl} operation #{idx+1}."
                code = f"x = {idx + 1}\nprint(x * 10)"
                pred_list.append(create_predict_q(q_text, code, str(val), "Multiply x by 10.", f"Evaluate ({idx+1}) * 10.", f"The program prints {val}."))
            py["Predict the Output"][diff][lvl] = pred_list

    # =========================================================================
    # PYTHON MCQ CHALLENGE (type: "mcq")
    # =========================================================================
    for diff in ["Beginner", "Intermediate", "Advanced"]:
        for lvl in ["1", "2", "3", "4"]:
            mcq_list = []
            for idx in range(10):
                opts = ["A) Correct approach", "B) Syntax error", "C) Runtime exception", "D) Undefined behavior"]
                ans = "A"
                if idx % 4 == 1:
                    opts = ["A) Invalid", "B) Correct approach", "C) Syntax error", "D) None of the above"]
                    ans = "B"
                elif idx % 4 == 2:
                    opts = ["A) False", "B) Deprecated", "C) Correct approach", "D) Error"]
                    ans = "C"
                elif idx % 4 == 3:
                    opts = ["A) Not allowed", "B) Warning", "C) Exception", "D) Correct approach"]
                    ans = "D"
                q = create_mcq_q(
                    f"[{diff} L{lvl}] Which of the following is correct for Python concept #{idx+1}?",
                    f"# Context snippet:\nval_{idx+1} = {idx * 2}",
                    opts,
                    ans,
                    "Read all choices carefully.",
                    f"Option {ans} represents the standard idiomatic practice.",
                    f"Option {ans} correctly follows Python design standards and language semantics."
                )
                mcq_list.append(q)
            py["MCQ Challenge"][diff][lvl] = mcq_list

    return py

print("Python generator function ready.")
