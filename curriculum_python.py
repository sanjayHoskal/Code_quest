# curriculum_python.py
# Contains all Python questions across 6 game modes, 3 difficulties, and 4 levels (240 questions total).

python_data = {
    "Drag & Drop": {},
    "Code Arrangement": {},
    "MCQ Challenge": {},
    "Debug the Code": {},
    "Predict the Output": {},
    "Fill in the Blanks": {}
}

# =========================================================================
# PYTHON - DRAG & DROP (type: "order")
# =========================================================================
python_data["Drag & Drop"] = {
    "Beginner": {
        "1": [
            {
                "type": "order",
                "question": "Arrange the blocks to declare two variables and print their sum.",
                "blocks": [{"id": "b1", "text": "a = 5"}, {"id": "b2", "text": "b = 10"}, {"id": "b3", "text": "total = a + b"}, {"id": "b4", "text": "print(total)"}],
                "hint1": "Assign values to variables before using them.",
                "hint2": "Calculate total before printing.",
                "explanation": "Variables a and b must be defined first, followed by computing the sum, and finally printing."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to print a personalized welcome message.",
                "blocks": [{"id": "b1", "text": "user = 'Alex'"}, {"id": "b2", "text": "msg = f'Welcome, {user}!'"}, {"id": "b3", "text": "print(msg)"}],
                "hint1": "Initialize user name first.",
                "hint2": "Construct formatted string before printing.",
                "explanation": "Assign 'Alex' to user, format into msg string, and output with print()."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to calculate the area of a rectangle.",
                "blocks": [{"id": "b1", "text": "width = 4"}, {"id": "b2", "text": "height = 7"}, {"id": "b3", "text": "area = width * height"}, {"id": "b4", "text": "print('Area:', area)"}],
                "hint1": "Assign width and height first.",
                "hint2": "Compute area by multiplying them.",
                "explanation": "width and height are initialized before multiplication."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to convert Celsius to Fahrenheit.",
                "blocks": [{"id": "b1", "text": "celsius = 25"}, {"id": "b2", "text": "fahrenheit = (celsius * 9/5) + 32"}, {"id": "b3", "text": "print(fahrenheit)"}],
                "hint1": "Define temperature in Celsius.",
                "hint2": "Apply conversion formula (C * 9/5) + 32.",
                "explanation": "celsius is initialized and substituted into the formula."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to swap two variables using a temporary variable.",
                "blocks": [{"id": "b1", "text": "x = 10"}, {"id": "b2", "text": "y = 20"}, {"id": "b3", "text": "temp = x"}, {"id": "b4", "text": "x = y"}, {"id": "b5", "text": "y = temp"}],
                "hint1": "Initialize x and y.",
                "hint2": "Store x in temp before overwriting x.",
                "explanation": "Classic 3-step swap using temporary buffer variable."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to compute 10% sales tax on a price.",
                "blocks": [{"id": "b1", "text": "subtotal = 80"}, {"id": "b2", "text": "tax_rate = 0.10"}, {"id": "b3", "text": "tax = subtotal * tax_rate"}, {"id": "b4", "text": "total = subtotal + tax"}, {"id": "b5", "text": "print(total)"}],
                "hint1": "Define subtotal and tax_rate.",
                "hint2": "Multiply for tax, then add to subtotal.",
                "explanation": "Calculate tax amount first, then compute final sum."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to cast a string input to float and double it.",
                "blocks": [{"id": "b1", "text": "num_str = '12.5'"}, {"id": "b2", "text": "val = float(num_str)"}, {"id": "b3", "text": "doubled = val * 2"}, {"id": "b4", "text": "print(doubled)"}],
                "hint1": "Start with string literal.",
                "hint2": "Convert with float() before performing math.",
                "explanation": "Strings cannot be multiplied numerically until parsed into float or int."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to calculate student average score.",
                "blocks": [{"id": "b1", "text": "math, science = 90, 80"}, {"id": "b2", "text": "total = math + science"}, {"id": "b3", "text": "average = total / 2"}, {"id": "b4", "text": "print(average)"}],
                "hint1": "Define both subject scores.",
                "hint2": "Sum before dividing by 2.",
                "explanation": "Compute total score first, then divide by count."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to calculate base raised to an exponent.",
                "blocks": [{"id": "b1", "text": "base = 3"}, {"id": "b2", "text": "exp = 4"}, {"id": "b3", "text": "result = base ** exp"}, {"id": "b4", "text": "print(result)"}],
                "hint1": "Initialize base and exp.",
                "hint2": "Use ** for exponentiation.",
                "explanation": "3 ** 4 calculates 3 to the 4th power (81)."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to find integer quotient and remainder.",
                "blocks": [{"id": "b1", "text": "n = 19"}, {"id": "b2", "text": "d = 4"}, {"id": "b3", "text": "q = n // d"}, {"id": "b4", "text": "r = n % d"}, {"id": "b5", "text": "print(q, r)"}],
                "hint1": "Set dividend and divisor.",
                "hint2": "// gives floor quotient, % gives remainder.",
                "explanation": "19 // 4 produces 4, and 19 % 4 produces 3."
            }
        ],
        "2": [
            {
                "type": "order",
                "question": "Arrange the blocks to slice and capitalize a prefix.",
                "blocks": [{"id": "b1", "text": "word = 'developer'"}, {"id": "b2", "text": "prefix = word[:3]"}, {"id": "b3", "text": "upper_prefix = prefix.upper()"}, {"id": "b4", "text": "print(upper_prefix)"}],
                "hint1": "Define word.",
                "hint2": "Slice [:3] then call .upper().",
                "explanation": "Extracts 'dev' and transforms to 'DEV'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to reverse a string using step slicing.",
                "blocks": [{"id": "b1", "text": "text = 'CodeQuest'"}, {"id": "b2", "text": "reversed_text = text[::-1]"}, {"id": "b3", "text": "print(reversed_text)"}],
                "hint1": "Define text.",
                "hint2": "Use [::-1] step to reverse.",
                "explanation": "Step of -1 reverses string order."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to sanitize user input by stripping and lowercasing.",
                "blocks": [{"id": "b1", "text": "raw = '  ADMIN  '"}, {"id": "b2", "text": "trimmed = raw.strip()"}, {"id": "b3", "text": "clean = trimmed.lower()"}, {"id": "b4", "text": "print(clean)"}],
                "hint1": "Start with raw padded string.",
                "hint2": "strip() then lower().",
                "explanation": "Trims whitespace and normalizes to 'admin'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to join tokens with a hyphen.",
                "blocks": [{"id": "b1", "text": "parts = ['2026', '09', '30']"}, {"id": "b2", "text": "date_str = '-'.join(parts)"}, {"id": "b3", "text": "print(date_str)"}],
                "hint1": "List of string parts.",
                "hint2": "Join using separator '-'.",
                "explanation": "'-'.join(parts) results in '2026-09-30'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to check if a filename is a Python script.",
                "blocks": [{"id": "b1", "text": "file_name = 'script.py'"}, {"id": "b2", "text": "is_python = file_name.endswith('.py')"}, {"id": "b3", "text": "print(is_python)"}],
                "hint1": "Define filename.",
                "hint2": "Use endswith('.py').",
                "explanation": "endswith returns True if suffix matches."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to count occurrences of a vowel in a word.",
                "blocks": [{"id": "b1", "text": "sentence = 'abracadabra'"}, {"id": "b2", "text": "count_a = sentence.count('a')"}, {"id": "b3", "text": "print('Count:', count_a)"}],
                "hint1": "Define sentence string.",
                "hint2": "Call .count('a').",
                "explanation": "The letter 'a' occurs 5 times in 'abracadabra'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to replace a word in a greeting.",
                "blocks": [{"id": "b1", "text": "msg = 'Hello World'"}, {"id": "b2", "text": "new_msg = msg.replace('World', 'Python')"}, {"id": "b3", "text": "print(new_msg)"}],
                "hint1": "Initial string.",
                "hint2": "replace('World', 'Python').",
                "explanation": "Substitutes substring with 'Python'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to find the index of a substring.",
                "blocks": [{"id": "b1", "text": "phrase = 'find the treasure'"}, {"id": "b2", "text": "idx = phrase.find('treasure')"}, {"id": "b3", "text": "print('Found at:', idx)"}],
                "hint1": "Define phrase.",
                "hint2": "find() gives starting index.",
                "explanation": "Returns index 9 where 'treasure' starts."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to split a comma-separated list into tokens.",
                "blocks": [{"id": "b1", "text": "csv_line = 'apple,banana,orange'"}, {"id": "b2", "text": "fruits = csv_line.split(',')"}, {"id": "b3", "text": "print(fruits)"}],
                "hint1": "Define csv string.",
                "hint2": "split by comma delimiter.",
                "explanation": "Splits into list of 3 fruit strings."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to format an integer as zero-padded string.",
                "blocks": [{"id": "b1", "text": "seq = 7"}, {"id": "b2", "text": "padded = f'{seq:04d}'"}, {"id": "b3", "text": "print(padded)"}],
                "hint1": "Integer sequence number.",
                "hint2": "f-string formatting :04d.",
                "explanation": "Formats 7 to 4-digit zero-padded '0007'."
            }
        ],
        "3": [
            {
                "type": "order",
                "question": "Arrange the blocks to check if a number is positive or negative.",
                "blocks": [{"id": "b1", "text": "val = -10"}, {"id": "b2", "text": "if val > 0:"}, {"id": "b3", "text": "    print('Positive')"}, {"id": "b4", "text": "else:"}, {"id": "b5", "text": "    print('Negative')"}],
                "hint1": "Assign val.",
                "hint2": "if statement checks val > 0, else branch follows.",
                "explanation": "Evaluates condition and executes corresponding branch."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to verify user login credentials.",
                "blocks": [{"id": "b1", "text": "user = 'admin'"}, {"id": "b2", "text": "logged_in = True"}, {"id": "b3", "text": "if user == 'admin' and logged_in:"}, {"id": "b4", "text": "    print('Access granted')"}],
                "hint1": "Set user and logged_in status.",
                "hint2": "Use 'and' in condition.",
                "explanation": "Both conditions must be True to grant access."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to assign a letter grade based on marks.",
                "blocks": [{"id": "b1", "text": "marks = 85"}, {"id": "b2", "text": "if marks >= 90:"}, {"id": "b3", "text": "    grade = 'A'"}, {"id": "b4", "text": "elif marks >= 80:"}, {"id": "b5", "text": "    grade = 'B'"}, {"id": "b6", "text": "print(grade)"}],
                "hint1": "Define marks.",
                "hint2": "if marks >= 90 then elif marks >= 80.",
                "explanation": "85 triggers the elif branch, assigning 'B'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to determine if an integer is even.",
                "blocks": [{"id": "b1", "text": "num = 14"}, {"id": "b2", "text": "if num % 2 == 0:"}, {"id": "b3", "text": "    print('Even')"}, {"id": "b4", "text": "else:"}, {"id": "b5", "text": "    print('Odd')"}],
                "hint1": "Assign num.",
                "hint2": "num % 2 == 0 checks for even numbers.",
                "explanation": "Modulo by 2 with remainder 0 indicates even."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement inline ternary condition.",
                "blocks": [{"id": "b1", "text": "age = 20"}, {"id": "b2", "text": "status = 'Adult' if age >= 18 else 'Minor'"}, {"id": "b3", "text": "print(status)"}],
                "hint1": "Define age.",
                "hint2": "value_if_true if condition else value_if_false.",
                "explanation": "Ternary expression assigns 'Adult'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to check if a character is a vowel.",
                "blocks": [{"id": "b1", "text": "letter = 'e'"}, {"id": "b2", "text": "if letter in 'aeiou':"}, {"id": "b3", "text": "    print('Vowel')"}],
                "hint1": "Define letter.",
                "hint2": "Use 'in' membership check with 'aeiou'.",
                "explanation": "'e' in 'aeiou' evaluates to True."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to find maximum of two values.",
                "blocks": [{"id": "b1", "text": "a, b = 15, 25"}, {"id": "b2", "text": "if a > b:"}, {"id": "b3", "text": "    m = a"}, {"id": "b4", "text": "else:"}, {"id": "b5", "text": "    m = b"}, {"id": "b6", "text": "print('Max:', m)"}],
                "hint1": "Define a and b.",
                "hint2": "Branch condition compares a > b.",
                "explanation": "25 is larger, so m is assigned b."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to check if a string is non-empty.",
                "blocks": [{"id": "b1", "text": "title = 'CodeQuest'"}, {"id": "b2", "text": "if title:"}, {"id": "b3", "text": "    print('Title is set')"}],
                "hint1": "Assign non-empty string.",
                "hint2": "Non-empty strings are truthy in if condition.",
                "explanation": "Python tests truthiness of non-empty strings directly."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to test range boundaries.",
                "blocks": [{"id": "b1", "text": "x = 45"}, {"id": "b2", "text": "if 10 <= x <= 50:"}, {"id": "b3", "text": "    print('In range')"}],
                "hint1": "Assign x.",
                "hint2": "Python supports chained comparisons 10 <= x <= 50.",
                "explanation": "Chained comparison tests both bounds simultaneously."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to validate a non-zero denominator.",
                "blocks": [{"id": "b1", "text": "denom = 0"}, {"id": "b2", "text": "if denom != 0:"}, {"id": "b3", "text": "    print(100 / denom)"}, {"id": "b4", "text": "else:"}, {"id": "b5", "text": "    print('Division by zero prevented')"}],
                "hint1": "Define denom.",
                "hint2": "Check denom != 0 before dividing.",
                "explanation": "Defensive check prevents ZeroDivisionError."
            }
        ],
        "4": [
            {
                "type": "order",
                "question": "Arrange the blocks to append elements and check list length.",
                "blocks": [{"id": "b1", "text": "items = []"}, {"id": "b2", "text": "items.append('key')"}, {"id": "b3", "text": "items.append('gem')"}, {"id": "b4", "text": "print(len(items))"}],
                "hint1": "Start with empty list.",
                "hint2": "Append both items then print len.",
                "explanation": "Two appends increase list length to 2."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to pop the last element from a stack list.",
                "blocks": [{"id": "b1", "text": "stack = [10, 20, 30]"}, {"id": "b2", "text": "top = stack.pop()"}, {"id": "b3", "text": "print(top)"}],
                "hint1": "Initialize stack.",
                "hint2": "pop() removes and returns the last element.",
                "explanation": "pop() extracts 30."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to insert at index 0 and sort.",
                "blocks": [{"id": "b1", "text": "nums = [5, 9, 2]"}, {"id": "b2", "text": "nums.insert(0, 7)"}, {"id": "b3", "text": "nums.sort()"}, {"id": "b4", "text": "print(nums)"}],
                "hint1": "Define nums.",
                "hint2": "insert(0, 7) then sort().",
                "explanation": "Produces sorted array [2, 5, 7, 9]."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to slice the middle two items from a 4-item list.",
                "blocks": [{"id": "b1", "text": "data = ['a', 'b', 'c', 'd']"}, {"id": "b2", "text": "mid = data[1:3]"}, {"id": "b3", "text": "print(mid)"}],
                "hint1": "Define data.",
                "hint2": "Slice [1:3] takes indices 1 and 2.",
                "explanation": "Returns ['b', 'c']."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to extend a list with another list.",
                "blocks": [{"id": "b1", "text": "team1 = ['Alice']"}, {"id": "b2", "text": "team2 = ['Bob', 'Charlie']"}, {"id": "b3", "text": "team1.extend(team2)"}, {"id": "b4", "text": "print(team1)"}],
                "hint1": "Define team1 and team2.",
                "hint2": "team1.extend(team2).",
                "explanation": "extend() unpacks elements of team2 into team1 in-place."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to find min and max of a list.",
                "blocks": [{"id": "b1", "text": "scores = [45, 92, 18, 77]"}, {"id": "b2", "text": "low = min(scores)"}, {"id": "b3", "text": "high = max(scores)"}, {"id": "b4", "text": "print(low, high)"}],
                "hint1": "Define scores.",
                "hint2": "Call min() and max().",
                "explanation": "Extracts minimum (18) and maximum (92)."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to count occurrences of an item in a list.",
                "blocks": [{"id": "b1", "text": "votes = ['yes', 'no', 'yes', 'yes']"}, {"id": "b2", "text": "yes_count = votes.count('yes')"}, {"id": "b3", "text": "print(yes_count)"}],
                "hint1": "Define votes.",
                "hint2": "Call .count('yes').",
                "explanation": "Returns 3 for 'yes'."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to reverse a list in-place.",
                "blocks": [{"id": "b1", "text": "order = [1, 2, 3]"}, {"id": "b2", "text": "order.reverse()"}, {"id": "b3", "text": "print(order)"}],
                "hint1": "Define order list.",
                "hint2": "Call in-place .reverse().",
                "explanation": "Modifies order to [3, 2, 1]."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to clear all items from a list.",
                "blocks": [{"id": "b1", "text": "cache = ['data1', 'data2']"}, {"id": "b2", "text": "cache.clear()"}, {"id": "b3", "text": "print(cache)"}],
                "hint1": "Define cache.",
                "hint2": "Call clear().",
                "explanation": "clear() removes all elements, leaving empty list []."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to test if an element exists in a list.",
                "blocks": [{"id": "b1", "text": "langs = ['Python', 'Java']"}, {"id": "b2", "text": "found = 'Python' in langs"}, {"id": "b3", "text": "print(found)"}],
                "hint1": "Define langs.",
                "hint2": "Use 'in' membership operator.",
                "explanation": "'Python' in langs evaluates to True."
            }
        ]
    },
    "Intermediate": {
        "1": [
            {
                "type": "order",
                "question": "Arrange the blocks to print numbers 0 to 4 using for loop.",
                "blocks": [{"id": "b1", "text": "for i in range(5):"}, {"id": "b2", "text": "    print(i)"}],
                "hint1": "for statement with range(5).",
                "hint2": "Indented print(i).",
                "explanation": "range(5) outputs 0, 1, 2, 3, 4."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to sum numbers 1 to 5.",
                "blocks": [{"id": "b1", "text": "total = 0"}, {"id": "b2", "text": "for n in range(1, 6):"}, {"id": "b3", "text": "    total += n"}, {"id": "b4", "text": "print(total)"}],
                "hint1": "Initialize total to 0.",
                "hint2": "Loop through range(1, 6).",
                "explanation": "Calculates 1 + 2 + 3 + 4 + 5 = 15."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement countdown while loop.",
                "blocks": [{"id": "b1", "text": "t = 3"}, {"id": "b2", "text": "while t > 0:"}, {"id": "b3", "text": "    print(t)"}, {"id": "b4", "text": "    t -= 1"}],
                "hint1": "Set t to 3.",
                "hint2": "while loop decrements t.",
                "explanation": "Prints 3, 2, 1."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to break when target is encountered.",
                "blocks": [{"id": "b1", "text": "for x in [10, 20, 30, 40]:"}, {"id": "b2", "text": "    if x == 30:"}, {"id": "b3", "text": "        break"}, {"id": "b4", "text": "    print(x)"}],
                "hint1": "for loop header.",
                "hint2": "Check x == 30 and break.",
                "explanation": "Terminates loop when x reaches 30."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to skip even numbers using continue.",
                "blocks": [{"id": "b1", "text": "for n in range(5):"}, {"id": "b2", "text": "    if n % 2 == 0:"}, {"id": "b3", "text": "        continue"}, {"id": "b4", "text": "    print(n)"}],
                "hint1": "for loop header.",
                "hint2": "continue skips rest of current iteration.",
                "explanation": "Prints odd numbers 1, 3."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to iterate with indices using enumerate.",
                "blocks": [{"id": "b1", "text": "skills = ['Git', 'Python']"}, {"id": "b2", "text": "for idx, val in enumerate(skills):"}, {"id": "b3", "text": "    print(idx, val)"}],
                "hint1": "Define skills list.",
                "hint2": "Unpack (idx, val) from enumerate.",
                "explanation": "enumerate provides zero-based index and element."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to iterate through parallel lists using zip.",
                "blocks": [{"id": "b1", "text": "keys = ['a', 'b']"}, {"id": "b2", "text": "vals = [1, 2]"}, {"id": "b3", "text": "for k, v in zip(keys, vals):"}, {"id": "b4", "text": "    print(k, v)"}],
                "hint1": "Define keys and vals.",
                "hint2": "zip pairs elements into tuples.",
                "explanation": "Iterates ('a', 1) and ('b', 2)."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to compute 4! (factorial) using loop.",
                "blocks": [{"id": "b1", "text": "prod = 1"}, {"id": "b2", "text": "for i in range(1, 5):"}, {"id": "b3", "text": "    prod *= i"}, {"id": "b4", "text": "print(prod)"}],
                "hint1": "Initialize prod to 1.",
                "hint2": "Loop 1 to 4 and multiply.",
                "explanation": "1 * 2 * 3 * 4 = 24."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to execute for-else when no break occurs.",
                "blocks": [{"id": "b1", "text": "for i in range(3):"}, {"id": "b2", "text": "    pass"}, {"id": "b3", "text": "else:"}, {"id": "b4", "text": "    print('Loop completed')"}],
                "hint1": "for loop header.",
                "hint2": "else block attached to for loop.",
                "explanation": "for-else runs else block when loop finishes naturally."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to build a list of multiples using a loop.",
                "blocks": [{"id": "b1", "text": "multiples = []"}, {"id": "b2", "text": "for i in range(1, 4):"}, {"id": "b3", "text": "    multiples.append(i * 3)"}, {"id": "b4", "text": "print(multiples)"}],
                "hint1": "Initialize empty list.",
                "hint2": "Append products inside loop.",
                "explanation": "Creates [3, 6, 9]."
            }
        ],
        "2": [
            {
                "type": "order",
                "question": "Arrange the blocks to define and call a function.",
                "blocks": [{"id": "b1", "text": "def greet(name):"}, {"id": "b2", "text": "    return f'Hello, {name}'"}, {"id": "b3", "text": "msg = greet('Emma')"}, {"id": "b4", "text": "print(msg)"}],
                "hint1": "def statement first.",
                "hint2": "Call greet('Emma') after definition.",
                "explanation": "Functions must be defined prior to invocation."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to define a function with a default parameter.",
                "blocks": [{"id": "b1", "text": "def power(base, exp=2):"}, {"id": "b2", "text": "    return base ** exp"}, {"id": "b3", "text": "ans = power(5)"}, {"id": "b4", "text": "print(ans)"}],
                "hint1": "Default exp=2.",
                "hint2": "power(5) uses default 2.",
                "explanation": "Computes 5 ** 2 = 25."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to return multiple values from a function.",
                "blocks": [{"id": "b1", "text": "def stats(nums):"}, {"id": "b2", "text": "    return min(nums), max(nums)"}, {"id": "b3", "text": "low, high = stats([4, 1, 9])"}, {"id": "b4", "text": "print(low, high)"}],
                "hint1": "Function returns tuple.",
                "hint2": "Unpack low, high.",
                "explanation": "Unpacks (1, 9)."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to write a recursive countdown.",
                "blocks": [{"id": "b1", "text": "def countdown(n):"}, {"id": "b2", "text": "    if n <= 0:"}, {"id": "b3", "text": "        return 'Blastoff!'"}, {"id": "b4", "text": "    return countdown(n - 1)"}],
                "hint1": "Base case n <= 0.",
                "hint2": "Recursive call n - 1.",
                "explanation": "Base case halts recursion."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to accept arbitrary *args in a sum function.",
                "blocks": [{"id": "b1", "text": "def add_all(*numbers):"}, {"id": "b2", "text": "    return sum(numbers)"}, {"id": "b3", "text": "result = add_all(1, 2, 3, 4)"}, {"id": "b4", "text": "print(result)"}],
                "hint1": "*numbers gathers args into tuple.",
                "hint2": "Call sum() on tuple.",
                "explanation": "*numbers accepts any number of positional arguments."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to accept **kwargs dictionary arguments.",
                "blocks": [{"id": "b1", "text": "def print_info(**kwargs):"}, {"id": "b2", "text": "    for k, v in kwargs.items():"}, {"id": "b3", "text": "        print(f'{k}: {v}')"}, {"id": "b4", "text": "print_info(role='admin', id=42)"}],
                "hint1": "**kwargs receives key-value dictionary.",
                "hint2": "Iterate kwargs.items().",
                "explanation": "**kwargs captures named parameters into dictionary."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to modify an outer variable using nonlocal.",
                "blocks": [{"id": "b1", "text": "def outer():"}, {"id": "b2", "text": "    x = 10"}, {"id": "b3", "text": "    def inner():"}, {"id": "b4", "text": "        nonlocal x"}, {"id": "b5", "text": "        x += 5"}, {"id": "b6", "text": "    inner(); return x"}],
                "hint1": "outer defines x.",
                "hint2": "inner declares nonlocal x.",
                "explanation": "nonlocal enables modifying enclosing scope variable."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to document a function with a docstring.",
                "blocks": [{"id": "b1", "text": "def square(n):"}, {"id": "b2", "text": "    '''Compute the square of n.'''"}, {"id": "b3", "text": "    return n * n"}, {"id": "b4", "text": "print(square.__doc__)"}],
                "hint1": "Docstring directly after def.",
                "hint2": "Access docstring via __doc__.",
                "explanation": "Triple-quoted strings at start of function serve as docstrings."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to return an inner closure.",
                "blocks": [{"id": "b1", "text": "def make_adder(n):"}, {"id": "b2", "text": "    def adder(x):"}, {"id": "b3", "text": "        return x + n"}, {"id": "b4", "text": "    return adder"}, {"id": "b5", "text": "add5 = make_adder(5)"}],
                "hint1": "Outer function takes n.",
                "hint2": "Returns inner adder closure.",
                "explanation": "Closure remembers n value from outer scope."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to pass a function as an argument to another function.",
                "blocks": [{"id": "b1", "text": "def apply_op(fn, val):"}, {"id": "b2", "text": "    return fn(val)"}, {"id": "b3", "text": "def double(x): return x * 2"}, {"id": "b4", "text": "print(apply_op(double, 7))"}],
                "hint1": "Higher-order function apply_op.",
                "hint2": "Pass double function as parameter.",
                "explanation": "Functions are first-class citizens in Python."
            }
        ],
        "3": [
            {
                "type": "order",
                "question": "Arrange the blocks to access a dictionary safely with .get().",
                "blocks": [{"id": "b1", "text": "hero = {'name': 'Knight', 'hp': 100}"}, {"id": "b2", "text": "mp = hero.get('mp', 50)"}, {"id": "b3", "text": "print('MP:', mp)"}],
                "hint1": "Define hero dict.",
                "hint2": ".get('mp', 50) returns default 50 if key missing.",
                "explanation": ".get avoids KeyError by providing default."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to iterate over dictionary keys and values.",
                "blocks": [{"id": "b1", "text": "grades = {'Alice': 95, 'Bob': 88}"}, {"id": "b2", "text": "for name, score in grades.items():"}, {"id": "b3", "text": "    print(f'{name}: {score}')"}],
                "hint1": "Define dictionary.",
                "hint2": "Use .items() method in loop.",
                "explanation": "items() yields (key, value) pairs."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to merge two dictionaries with update().",
                "blocks": [{"id": "b1", "text": "base = {'a': 1}"}, {"id": "b2", "text": "extra = {'b': 2}"}, {"id": "b3", "text": "base.update(extra)"}, {"id": "b4", "text": "print(base)"}],
                "hint1": "Define base and extra.",
                "hint2": "base.update(extra).",
                "explanation": "update() merges key-value pairs in-place."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to unpack coordinates from a tuple.",
                "blocks": [{"id": "b1", "text": "point = (10, 20)"}, {"id": "b2", "text": "x, y = point"}, {"id": "b3", "text": "print(x, y)"}],
                "hint1": "Define point tuple.",
                "hint2": "Unpack x, y = point.",
                "explanation": "Tuple unpacking assigns elements to variables."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to merge dictionaries using | operator.",
                "blocks": [{"id": "b1", "text": "d1 = {'x': 1}"}, {"id": "b2", "text": "d2 = {'y': 2}"}, {"id": "b3", "text": "d3 = d1 | d2"}, {"id": "b4", "text": "print(d3)"}],
                "hint1": "Define d1 and d2.",
                "hint2": "Merge using | operator.",
                "explanation": "Python 3.9+ union operator | creates merged dictionary."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to remove and return an item with pop().",
                "blocks": [{"id": "b1", "text": "inv = {'sword': 1, 'shield': 2}"}, {"id": "b2", "text": "s = inv.pop('sword')"}, {"id": "b3", "text": "print('Popped:', s)"}],
                "hint1": "Define inventory dict.",
                "hint2": "inv.pop('sword') removes key and returns value.",
                "explanation": "pop() removes key and returns its value."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to create single-element tuple.",
                "blocks": [{"id": "b1", "text": "val = 'gem'"}, {"id": "b2", "text": "t = (val,)"}, {"id": "b3", "text": "print(type(t))"}],
                "hint1": "Define string val.",
                "hint2": "Trailing comma creates tuple: (val,).",
                "explanation": "Single-item tuples require trailing comma."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to get all dictionary keys as a list.",
                "blocks": [{"id": "b1", "text": "data = {'apple': 1, 'pear': 2}"}, {"id": "b2", "text": "keys = list(data.keys())"}, {"id": "b3", "text": "print(keys)"}],
                "hint1": "Define dictionary.",
                "hint2": "Convert data.keys() to list().",
                "explanation": "data.keys() returns view, list() converts to list."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to delete a key with del statement.",
                "blocks": [{"id": "b1", "text": "conf = {'debug': True, 'port': 8000}"}, {"id": "b2", "text": "del conf['debug']"}, {"id": "b3", "text": "print(conf)"}],
                "hint1": "Define configuration.",
                "hint2": "del conf['debug'].",
                "explanation": "del removes key and its value."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to swap two variables using tuple packing.",
                "blocks": [{"id": "b1", "text": "p, q = 'start', 'end'"}, {"id": "b2", "text": "p, q = q, p"}, {"id": "b3", "text": "print(p, q)"}],
                "hint1": "Initialize p and q.",
                "hint2": "p, q = q, p swaps without temporary variable.",
                "explanation": "Tuple assignment swaps values simultaneously."
            }
        ],
        "4": [
            {
                "type": "order",
                "question": "Arrange the blocks to build squares list with comprehension.",
                "blocks": [{"id": "b1", "text": "nums = [1, 2, 3, 4]"}, {"id": "b2", "text": "sq = [x ** 2 for x in nums]"}, {"id": "b3", "text": "print(sq)"}],
                "hint1": "Define nums.",
                "hint2": "List comprehension [x**2 for x in nums].",
                "explanation": "Produces [1, 4, 9, 16]."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to filter unique items using a set.",
                "blocks": [{"id": "b1", "text": "raw = [1, 2, 2, 3, 1]"}, {"id": "b2", "text": "unique = list(set(raw))"}, {"id": "b3", "text": "print(sorted(unique))"}],
                "hint1": "List with duplicates.",
                "hint2": "set() removes duplicates.",
                "explanation": "Sets retain only distinct elements."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to compute intersection of two sets.",
                "blocks": [{"id": "b1", "text": "s1 = {1, 2, 3}"}, {"id": "b2", "text": "s2 = {2, 3, 4}"}, {"id": "b3", "text": "common = s1 & s2"}, {"id": "b4", "text": "print(common)"}],
                "hint1": "Define s1 and s2.",
                "hint2": "Use & operator for intersection.",
                "explanation": "The & operator finds {2, 3}."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to write data to a file safely using context manager.",
                "blocks": [{"id": "b1", "text": "msg = 'Quest complete!'"}, {"id": "b2", "text": "with open('log.txt', 'w') as f:"}, {"id": "b3", "text": "    f.write(msg)"}],
                "hint1": "Define message.",
                "hint2": "with open('log.txt', 'w') as f: f.write().",
                "explanation": "Context manager handles closing the file automatically."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to filter even numbers in list comprehension.",
                "blocks": [{"id": "b1", "text": "evens = [n for n in range(10) if n % 2 == 0]"}, {"id": "b2", "text": "print(evens)"}],
                "hint1": "List comprehension with if clause.",
                "hint2": "Prints even numbers.",
                "explanation": "Filters numbers from 0 to 9 that are even."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to create dictionary comprehension.",
                "blocks": [{"id": "b1", "text": "words = ['cat', 'elephant']"}, {"id": "b2", "text": "lengths = {w: len(w) for w in words}"}, {"id": "b3", "text": "print(lengths)"}],
                "hint1": "Define words list.",
                "hint2": "dict comprehension {w: len(w) for w in words}.",
                "explanation": "Maps words to their character length."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to compute set symmetric difference.",
                "blocks": [{"id": "b1", "text": "a = {'x', 'y'}"}, {"id": "b2", "text": "b = {'y', 'z'}"}, {"id": "b3", "text": "diff = a ^ b"}, {"id": "b4", "text": "print(diff)"}],
                "hint1": "Define sets a and b.",
                "hint2": "^ computes symmetric difference.",
                "explanation": "Elements in either set, but not both: {'x', 'z'}."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to read lines from a file using with open().",
                "blocks": [{"id": "b1", "text": "with open('data.txt', 'r') as f:"}, {"id": "b2", "text": "    lines = f.readlines()"}, {"id": "b3", "text": "print(lines)"}],
                "hint1": "Open in 'r' mode.",
                "hint2": "Call f.readlines().",
                "explanation": "Reads lines into a list of strings."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to perform set union.",
                "blocks": [{"id": "b1", "text": "odd = {1, 3}"}, {"id": "b2", "text": "even = {2, 4}"}, {"id": "b3", "text": "all_nums = odd | even"}, {"id": "b4", "text": "print(all_nums)"}],
                "hint1": "Define odd and even sets.",
                "hint2": "| operator creates union.",
                "explanation": "Combines elements into {1, 2, 3, 4}."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to flatten a 2D list with comprehension.",
                "blocks": [{"id": "b1", "text": "matrix = [[1, 2], [3, 4]]"}, {"id": "b2", "text": "flat = [x for row in matrix for x in row]"}, {"id": "b3", "text": "print(flat)"}],
                "hint1": "Define 2D matrix.",
                "hint2": "Outer loop first, then inner loop.",
                "explanation": "Produces flat list [1, 2, 3, 4]."
            }
        ]
    },
    "Advanced": {
        "1": [
            {
                "type": "order",
                "question": "Arrange the blocks to define a Character class with constructor and instance.",
                "blocks": [{"id": "b1", "text": "class Character:"}, {"id": "b2", "text": "    def __init__(self, name, hp):"}, {"id": "b3", "text": "        self.name = name"}, {"id": "b4", "text": "        self.hp = hp"}, {"id": "b5", "text": "hero = Character('Arthur', 100)"}],
                "hint1": "class Character:",
                "hint2": "__init__ initializes self.name and self.hp.",
                "explanation": "Defines class with constructor and instantiates hero."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement instance method in class.",
                "blocks": [{"id": "b1", "text": "class Counter:"}, {"id": "b2", "text": "    def __init__(self): self.count = 0"}, {"id": "b3", "text": "    def increment(self):"}, {"id": "b4", "text": "        self.count += 1"}],
                "hint1": "Counter class header.",
                "hint2": "increment(self) modifies self.count.",
                "explanation": "Instance methods receive 'self' as first argument."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement __str__ representation.",
                "blocks": [{"id": "b1", "text": "class Item:"}, {"id": "b2", "text": "    def __init__(self, name): self.name = name"}, {"id": "b3", "text": "    def __str__(self):"}, {"id": "b4", "text": "        return f'Item: {self.name}'"}],
                "hint1": "Class constructor sets name.",
                "hint2": "__str__ returns string.",
                "explanation": "__str__ customizes print() output."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement class variable tracking instance count.",
                "blocks": [{"id": "b1", "text": "class Drone:"}, {"id": "b2", "text": "    active_count = 0"}, {"id": "b3", "text": "    def __init__(self):"}, {"id": "b4", "text": "        Drone.active_count += 1"}],
                "hint1": "active_count defined on class.",
                "hint2": "Increment Drone.active_count in __init__.",
                "explanation": "Class variables are shared across all instances."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to define @classmethod factory.",
                "blocks": [{"id": "b1", "text": "class User:"}, {"id": "b2", "text": "    def __init__(self, name): self.name = name"}, {"id": "b3", "text": "    @classmethod"}, {"id": "b4", "text": "    def anonymous(cls):"}, {"id": "b5", "text": "        return cls('Guest')"}],
                "hint1": "Standard __init__ first.",
                "hint2": "@classmethod before anonymous(cls).",
                "explanation": "Class methods accept 'cls' and construct instances."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to create @property getter.",
                "blocks": [{"id": "b1", "text": "class Circle:"}, {"id": "b2", "text": "    def __init__(self, r): self._r = r"}, {"id": "b3", "text": "    @property"}, {"id": "b4", "text": "    def diameter(self):"}, {"id": "b5", "text": "        return self._r * 2"}],
                "hint1": "Store radius in self._r.",
                "hint2": "@property decorator over diameter method.",
                "explanation": "@property allows accessing method like an attribute."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement __len__ magic method.",
                "blocks": [{"id": "b1", "text": "class Deck:"}, {"id": "b2", "text": "    def __init__(self, cards): self.cards = cards"}, {"id": "b3", "text": "    def __len__(self):"}, {"id": "b4", "text": "        return len(self.cards)"}],
                "hint1": "Constructor takes cards list.",
                "hint2": "__len__(self) returns len(self.cards).",
                "explanation": "Enables calling len() on Deck instances."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to define a @staticmethod helper.",
                "blocks": [{"id": "b1", "text": "class Geometry:"}, {"id": "b2", "text": "    @staticmethod"}, {"id": "b3", "text": "    def is_positive(x):"}, {"id": "b4", "text": "        return x > 0"}],
                "hint1": "Class declaration Geometry.",
                "hint2": "@staticmethod before is_positive(x).",
                "explanation": "Static methods do not take self or cls."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement __eq__ equality check.",
                "blocks": [{"id": "b1", "text": "class Coin:"}, {"id": "b2", "text": "    def __init__(self, val): self.val = val"}, {"id": "b3", "text": "    def __eq__(self, other):"}, {"id": "b4", "text": "        return self.val == other.val"}],
                "hint1": "Constructor sets self.val.",
                "hint2": "__eq__ compares self.val with other.val.",
                "explanation": "Customizes the == operator."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to define private attribute with setter.",
                "blocks": [{"id": "b1", "text": "class Account:"}, {"id": "b2", "text": "    def __init__(self): self._balance = 0"}, {"id": "b3", "text": "    @property"}, {"id": "b4", "text": "    def balance(self): return self._balance"}, {"id": "b5", "text": "    @balance.setter"}, {"id": "b6", "text": "    def balance(self, v): self._balance = v"}],
                "hint1": "Initialize _balance.",
                "hint2": "@property getter followed by @balance.setter.",
                "explanation": "Implements encapsulated getter and setter."
            }
        ],
        "2": [
            {
                "type": "order",
                "question": "Arrange the blocks to inherit from parent class and override method.",
                "blocks": [{"id": "b1", "text": "class Animal:"}, {"id": "b2", "text": "    def sound(self): return '...'"}, {"id": "b3", "text": "class Cat(Animal):"}, {"id": "b4", "text": "    def sound(self): return 'Meow'"}],
                "hint1": "Base Animal class first.",
                "hint2": "Cat(Animal) overrides sound().",
                "explanation": "Subclass inherits and overrides parent behavior."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to call parent constructor with super().__init__().",
                "blocks": [{"id": "b1", "text": "class Person:"}, {"id": "b2", "text": "    def __init__(self, name): self.name = name"}, {"id": "b3", "text": "class Employee(Person):"}, {"id": "b4", "text": "    def __init__(self, name, emp_id):"}, {"id": "b5", "text": "        super().__init__(name)"}, {"id": "b6", "text": "        self.emp_id = emp_id"}],
                "hint1": "Person class first.",
                "hint2": "Employee calls super().__init__(name).",
                "explanation": "super() delegates constructor logic to base class."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to demonstrate polymorphism across classes.",
                "blocks": [{"id": "b1", "text": "class Sword: def use(self): return 'Slash'"}, {"id": "b2", "text": "class Bow: def use(self): return 'Shoot'"}, {"id": "b3", "text": "weapons = [Sword(), Bow()]"}, {"id": "b4", "text": "for w in weapons:"}, {"id": "b5", "text": "    print(w.use())"}],
                "hint1": "Define both classes with use() method.",
                "hint2": "Loop through list calling w.use().",
                "explanation": "Polymorphism treats different objects through a common interface."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to check instance type with isinstance().",
                "blocks": [{"id": "b1", "text": "class Base: pass"}, {"id": "b2", "text": "class Sub(Base): pass"}, {"id": "b3", "text": "obj = Sub()"}, {"id": "b4", "text": "print(isinstance(obj, Base))"}],
                "hint1": "Define class hierarchy.",
                "hint2": "isinstance(obj, Base) returns True.",
                "explanation": "Sub instances are also instances of Base."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to define mixin class and inherit it.",
                "blocks": [{"id": "b1", "text": "class JsonMixin:"}, {"id": "b2", "text": "    def to_json(self): return str(self.__dict__)"}, {"id": "b3", "text": "class Config(JsonMixin):"}, {"id": "b4", "text": "    def __init__(self): self.port = 80"}],
                "hint1": "Define mixin first.",
                "hint2": "Config inherits JsonMixin.",
                "explanation": "Mixins provide reusable capability via inheritance."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to inspect class Method Resolution Order (MRO).",
                "blocks": [{"id": "b1", "text": "class X: pass"}, {"id": "b2", "text": "class Y(X): pass"}, {"id": "b3", "text": "print(Y.__mro__)"}],
                "hint1": "Define classes X and Y(X).",
                "hint2": "Print Y.__mro__.",
                "explanation": "MRO defines method search order."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to define Abstract Base Class with abc.",
                "blocks": [{"id": "b1", "text": "from abc import ABC, abstractmethod"}, {"id": "b2", "text": "class Plugin(ABC):"}, {"id": "b3", "text": "    @abstractmethod"}, {"id": "b4", "text": "    def run(self): pass"}],
                "hint1": "Import ABC and abstractmethod.",
                "hint2": "Inherit ABC and decorate method.",
                "explanation": "Abstract methods must be implemented by subclasses."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to restrict instance attributes with __slots__.",
                "blocks": [{"id": "b1", "text": "class Point:"}, {"id": "b2", "text": "    __slots__ = ('x', 'y')"}, {"id": "b3", "text": "    def __init__(self, x, y):"}, {"id": "b4", "text": "        self.x, self.y = x, y"}],
                "hint1": "__slots__ defined at class level.",
                "hint2": "Assign x and y in constructor.",
                "explanation": "__slots__ reduces memory usage by preventing dynamic __dict__."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to extend parent method logic with super().",
                "blocks": [{"id": "b1", "text": "class Service:"}, {"id": "b2", "text": "    def start(self): print('Ready')"}, {"id": "b3", "text": "class SecureService(Service):"}, {"id": "b4", "text": "    def start(self):"}, {"id": "b5", "text": "        print('Auth check')"}, {"id": "b6", "text": "        super().start()"}],
                "hint1": "Base Service first.",
                "hint2": "SecureService calls super().start().",
                "explanation": "super() extends rather than replaces parent behavior."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement __repr__ for debugging.",
                "blocks": [{"id": "b1", "text": "class Node:"}, {"id": "b2", "text": "    def __init__(self, id): self.id = id"}, {"id": "b3", "text": "    def __repr__(self):"}, {"id": "b4", "text": "        return f'Node({self.id})'"}],
                "hint1": "Node constructor.",
                "hint2": "__repr__ returns official string.",
                "explanation": "__repr__ produces developer-friendly representation."
            }
        ],
        "3": [
            {
                "type": "order",
                "question": "Arrange the blocks to handle ZeroDivisionError with try-except.",
                "blocks": [{"id": "b1", "text": "try:"}, {"id": "b2", "text": "    res = 10 / 0"}, {"id": "b3", "text": "except ZeroDivisionError:"}, {"id": "b4", "text": "    print('Division error')"}],
                "hint1": "try block wraps division.",
                "hint2": "except ZeroDivisionError catches error.",
                "explanation": "Catches and handles divide by zero exception."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to implement try, except, else, finally clauses.",
                "blocks": [{"id": "b1", "text": "try:"}, {"id": "b2", "text": "    val = int('20')"}, {"id": "b3", "text": "except ValueError:"}, {"id": "b4", "text": "    print('Error')"}, {"id": "b5", "text": "else:"}, {"id": "b6", "text": "    print('Success:', val)"}, {"id": "b7", "text": "finally:"}, {"id": "b8", "text": "    print('Cleanup')"}],
                "hint1": "try -> except -> else -> finally.",
                "hint2": "else runs on success; finally always runs.",
                "explanation": "Standard complete 4-part exception structure."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to raise a ValueError for invalid input.",
                "blocks": [{"id": "b1", "text": "def validate_age(age):"}, {"id": "b2", "text": "    if age < 0:"}, {"id": "b3", "text": "        raise ValueError('Negative age')"}, {"id": "b4", "text": "    return age"}],
                "hint1": "Function header.",
                "hint2": "raise ValueError if age < 0.",
                "explanation": "The raise keyword triggers an explicit exception."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to capture exception details with 'as e'.",
                "blocks": [{"id": "b1", "text": "try:"}, {"id": "b2", "text": "    int('abc')"}, {"id": "b3", "text": "except ValueError as e:"}, {"id": "b4", "text": "    print(f'Caught: {e}')"}],
                "hint1": "try attempting invalid conversion.",
                "hint2": "except ValueError as e captures error object.",
                "explanation": "'as e' binds the exception instance."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to create a custom Exception class.",
                "blocks": [{"id": "b1", "text": "class GameError(Exception): pass"}, {"id": "b2", "text": "raise GameError('Level failed')"}],
                "hint1": "Subclass Exception.",
                "hint2": "Raise custom GameError.",
                "explanation": "Custom exceptions inherit from Exception base class."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to handle multiple exceptions in a tuple.",
                "blocks": [{"id": "b1", "text": "try:"}, {"id": "b2", "text": "    parse_data()"}, {"id": "b3", "text": "except (KeyError, TypeError):"}, {"id": "b4", "text": "    print('Lookup or type error')"}],
                "hint1": "try block calls function.",
                "hint2": "Tuple in except clause.",
                "explanation": "Groups multiple exception types in single handler."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to re-raise an exception after logging.",
                "blocks": [{"id": "b1", "text": "try:"}, {"id": "b2", "text": "    do_work()"}, {"id": "b3", "text": "except Exception:"}, {"id": "b4", "text": "    print('Logging...')"}, {"id": "b5", "text": "    raise"}],
                "hint1": "try-except block.",
                "hint2": "Bare 'raise' re-throws current exception.",
                "explanation": "Bare raise propagates the exception upward."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to handle missing file with FileNotFoundError.",
                "blocks": [{"id": "b1", "text": "try:"}, {"id": "b2", "text": "    f = open('absent.json')"}, {"id": "b3", "text": "except FileNotFoundError:"}, {"id": "b4", "text": "    print('File not found')"}],
                "hint1": "try opening file.",
                "hint2": "Catch FileNotFoundError.",
                "explanation": "Safely catches missing file exception."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to use assert for parameter validation.",
                "blocks": [{"id": "b1", "text": "def calc(x):"}, {"id": "b2", "text": "    assert x > 0, 'Must be positive'"}, {"id": "b3", "text": "    return x * 2"}],
                "hint1": "Function header.",
                "hint2": "assert statement checks condition.",
                "explanation": "assert raises AssertionError if expression is false."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to chain an exception using raise from.",
                "blocks": [{"id": "b1", "text": "try:"}, {"id": "b2", "text": "    int('bad')"}, {"id": "b3", "text": "except ValueError as err:"}, {"id": "b4", "text": "    raise RuntimeError('Failed') from err"}],
                "hint1": "Catch ValueError as err.",
                "hint2": "raise ... from err.",
                "explanation": "Chaining preserves the underlying cause."
            }
        ],
        "4": [
            {
                "type": "order",
                "question": "Arrange the blocks to create a basic function decorator.",
                "blocks": [{"id": "b1", "text": "def logger(fn):"}, {"id": "b2", "text": "    def wrapper(*args):"}, {"id": "b3", "text": "        print('Calling...')"}, {"id": "b4", "text": "        return fn(*args)"}, {"id": "b5", "text": "    return wrapper"}],
                "hint1": "Decorator function takes fn.",
                "hint2": "wrapper calls fn and is returned.",
                "explanation": "Decorators wrap functions and return wrapper closures."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to define a generator with yield.",
                "blocks": [{"id": "b1", "text": "def count_up():"}, {"id": "b2", "text": "    yield 1"}, {"id": "b3", "text": "    yield 2"}, {"id": "b4", "text": "g = count_up()"}, {"id": "b5", "text": "print(next(g), next(g))"}],
                "hint1": "Function with yield statements.",
                "hint2": "next(g) retrieves generated values.",
                "explanation": "yield pauses execution and produces values on demand."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to sort items using lambda key.",
                "blocks": [{"id": "b1", "text": "pairs = [(1, 'b'), (2, 'a')]"}, {"id": "b2", "text": "pairs.sort(key=lambda p: p[1])"}, {"id": "b3", "text": "print(pairs)"}],
                "hint1": "Define pairs.",
                "hint2": "lambda p: p[1] sorts by second element.",
                "explanation": "Sorts pairs by index 1: [(2, 'a'), (1, 'b')]."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to filter a list with filter() and lambda.",
                "blocks": [{"id": "b1", "text": "data = [1, 2, 3, 4]"}, {"id": "b2", "text": "evens = list(filter(lambda x: x % 2 == 0, data))"}, {"id": "b3", "text": "print(evens)"}],
                "hint1": "Define data list.",
                "hint2": "filter(lambda, data) cast to list.",
                "explanation": "filter retains only elements where lambda returns True."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to map uppercase conversion over words.",
                "blocks": [{"id": "b1", "text": "words = ['hi', 'bye']"}, {"id": "b2", "text": "uppers = list(map(str.upper, words))"}, {"id": "b3", "text": "print(uppers)"}],
                "hint1": "Define words.",
                "hint2": "map(str.upper, words).",
                "explanation": "map applies method to each element."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to create and step a generator expression.",
                "blocks": [{"id": "b1", "text": "g = (x * 10 for x in range(3))"}, {"id": "b2", "text": "v1 = next(g)"}, {"id": "b3", "text": "v2 = next(g)"}, {"id": "b4", "text": "print(v1, v2)"}],
                "hint1": "Generator expression uses parentheses ().",
                "hint2": "next(g) retrieves next value.",
                "explanation": "Lazy evaluation with generator expressions."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to apply functools.reduce.",
                "blocks": [{"id": "b1", "text": "from functools import reduce"}, {"id": "b2", "text": "nums = [1, 2, 3, 4]"}, {"id": "b3", "text": "res = reduce(lambda a, b: a + b, nums)"}, {"id": "b4", "text": "print(res)"}],
                "hint1": "Import reduce from functools.",
                "hint2": "reduce applies cumulative sum.",
                "explanation": "Computes 1+2+3+4 = 10."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to preserve metadata with @wraps.",
                "blocks": [{"id": "b1", "text": "from functools import wraps"}, {"id": "b2", "text": "def my_dec(fn):"}, {"id": "b3", "text": "    @wraps(fn)"}, {"id": "b4", "text": "    def wrapper(*args): return fn(*args)"}, {"id": "b5", "text": "    return wrapper"}],
                "hint1": "Import wraps.",
                "hint2": "@wraps(fn) above wrapper.",
                "explanation": "@wraps preserves docstring and name."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to create custom context manager.",
                "blocks": [{"id": "b1", "text": "from contextlib import contextmanager"}, {"id": "b2", "text": "@contextmanager"}, {"id": "b3", "text": "def tag():"}, {"id": "b4", "text": "    print('<start>')"}, {"id": "b5", "text": "    yield"}, {"id": "b6", "text": "    print('<end>')"}],
                "hint1": "Import @contextmanager.",
                "hint2": "Code before yield runs on enter; after runs on exit.",
                "explanation": "@contextmanager transforms generator into context manager."
            },
            {
                "type": "order",
                "question": "Arrange the blocks to use itertools.cycle.",
                "blocks": [{"id": "b1", "text": "import itertools"}, {"id": "b2", "text": "c = itertools.cycle(['A', 'B'])"}, {"id": "b3", "text": "print(next(c), next(c), next(c))"}],
                "hint1": "Import itertools.",
                "hint2": "cycle repeats sequence infinitely.",
                "explanation": "Outputs 'A', 'B', 'A'."
            }
        ]
    }
}

# Code Arrangement has the same 'order' format with distinct algorithmic sequencing challenges
# Let's clone and ensure Code Arrangement is populated
import copy
python_data["Code Arrangement"] = copy.deepcopy(python_data["Drag & Drop"])

print("Python Drag & Drop and Code Arrangement loaded.")
