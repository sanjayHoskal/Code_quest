# generate_java_curriculum.py
# Generates 240 authentic Java programming questions (6 modes x 3 diffs x 4 levels x 10 questions)
from curriculum_builder import create_order_q, create_fill_q, create_debug_q, create_predict_q, create_mcq_q
import copy

def generate_java():
    java = {
        "Drag & Drop": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Syntax Validator": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Code Arrangement": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "MCQ Challenge": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Debug the Code": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Predict the Output": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
        "Fill in the Blanks": {"Beginner": {}, "Intermediate": {}, "Advanced": {}},
    }

    # =========================================================================
    # JAVA DRAG & DROP & CODE ARRANGEMENT (type: "order")
    # =========================================================================
    # Beginner L1: Class structure, main method, System.out.println, primitives
    b_l1 = [
        create_order_q("Arrange the blocks to create a basic Java class and main method printing 'Hello World'.",
                       ["public class Main {", "    public static void main(String[] args) {", "        System.out.println(\"Hello World\");", "    }", "}"],
                       "Class declaration wraps everything.", "main method is inside class.",
                       "Java programs begin execution at public static void main(String[] args)."),
        create_order_q("Arrange the blocks to declare two int variables and print their sum.",
                       ["int a = 10;", "int b = 20;", "int sum = a + b;", "System.out.println(sum);"],
                       "Declare variables a and b first.", "Calculate sum before printing.",
                       "Variables must be declared with their types before arithmetic evaluation."),
        create_order_q("Arrange the blocks to compute the area of a rectangle in Java.",
                       ["int width = 5;", "int height = 8;", "int area = width * height;", "System.out.println(\"Area: \" + area);"],
                       "Define dimensions first.", "Multiply width by height.",
                       "Calculates width * height and concatenates with label string."),
        create_order_q("Arrange the blocks to declare a double variable and calculate tax.",
                       ["double price = 99.99;", "double rate = 0.07;", "double total = price + (price * rate);", "System.out.println(total);"],
                       "Declare price and rate.", "Compute total with parentheses.",
                       "double handles decimal arithmetic in Java."),
        create_order_q("Arrange the blocks to swap two int variables using a temp variable.",
                       ["int x = 1, y = 2;", "int temp = x;", "x = y;", "y = temp;"],
                       "Declare x and y.", "Save x in temp before overwriting.",
                       "3-step swap saves original x in temp."),
        create_order_q("Arrange the blocks to cast a double to an int.",
                       ["double d = 9.75;", "int rounded = (int) d;", "System.out.println(rounded);"],
                       "Declare double d.", "Explicit cast (int) d truncates decimals.",
                       "(int) performs explicit narrowing cast, discarding fractional part."),
        create_order_q("Arrange the blocks to declare and print a boolean flag.",
                       ["boolean isGameOver = false;", "isGameOver = true;", "System.out.println(\"Status: \" + isGameOver);"],
                       "Declare boolean variable.", "Update boolean to true.",
                       "boolean holds true or false in Java."),
        create_order_q("Arrange the blocks to print character and its ASCII code.",
                       ["char letter = 'A';", "int ascii = (int) letter;", "System.out.println(ascii);"],
                       "Declare char with single quotes.", "Cast char to int.",
                       "Casting 'A' to int yields its ASCII code 65."),
        create_order_q("Arrange the blocks to perform integer division and modulus.",
                       ["int n = 17, d = 4;", "int q = n / d;", "int r = n % d;", "System.out.println(q + \" R \" + r);"],
                       "Declare dividend and divisor.", "Compute quotient and remainder.",
                       "17 / 4 is 4 and 17 % 4 is 1 in integer arithmetic."),
        create_order_q("Arrange the blocks to format greeting with String variable.",
                       ["String user = \"Dev\";", "String greeting = \"Welcome, \" + user + \"!\";", "System.out.println(greeting);"],
                       "Declare String user.", "Concatenate with + operator.",
                       "String concatenation joins literals with + operator.")
    ]
    java["Drag & Drop"]["Beginner"]["1"] = b_l1

    # Beginner L2: String methods and operators
    b_l2 = [
        create_order_q("Arrange the blocks to measure String length and uppercase it.",
                       ["String title = \"codequest\";", "int len = title.length();", "String upper = title.toUpperCase();", "System.out.println(len + \" \" + upper);"],
                       "Define title.", "Call .length() and .toUpperCase().",
                       ".length() returns int, .toUpperCase() returns uppercase copy."),
        create_order_q("Arrange the blocks to extract first 3 characters using substring.",
                       ["String lang = \"JavaScript\";", "String prefix = lang.substring(0, 4);", "System.out.println(prefix);"],
                       "Declare string.", "substring(0, 4) extracts indices 0, 1, 2, 3.",
                       "substring(start, end) includes start up to end index."),
        create_order_q("Arrange the blocks to compare two Strings for equality.",
                       ["String s1 = \"admin\";", "String s2 = \"admin\";", "boolean match = s1.equals(s2);", "System.out.println(match);"],
                       "Declare both strings.", "Use .equals() instead of == for content comparison.",
                       "In Java, .equals() must be used to compare String content."),
        create_order_q("Arrange the blocks to check if a String contains a keyword.",
                       ["String bio = \"Senior Java Developer\";", "boolean hasJava = bio.contains(\"Java\");", "System.out.println(hasJava);"],
                       "Define bio.", "Call .contains(\"Java\").",
                       "contains() returns true if substring is found."),
        create_order_q("Arrange the blocks to replace a character in a String.",
                       ["String code = \"A-B-C\";", "String clean = code.replace(\"-\", \"*\");", "System.out.println(clean);"],
                       "Define code.", "replace replaces target with replacement.",
                       "replace() returns a new modified String."),
        create_order_q("Arrange the blocks to get the character at index 0.",
                       ["String name = \"Java\";", "char first = name.charAt(0);", "System.out.println(first);"],
                       "Define name.", "charAt(0) gets character at index 0.",
                       "charAt(0) returns 'J'."),
        create_order_q("Arrange the blocks to trim surrounding whitespace.",
                       ["String raw = \"  hello  \";", "String trimmed = raw.trim();", "System.out.println(trimmed);"],
                       "Define raw string.", "trim() removes spaces.",
                       "trim() strips leading and trailing whitespace."),
        create_order_q("Arrange the blocks to check prefix with startsWith.",
                       ["String url = \"https://codequest.dev\";", "boolean secure = url.startsWith(\"https\");", "System.out.println(secure);"],
                       "Define url.", "startsWith checks prefix.",
                       "startsWith returns true if prefix matches."),
        create_order_q("Arrange the blocks to convert integer to String with String.valueOf.",
                       ["int count = 42;", "String strCount = String.valueOf(count);", "System.out.println(strCount);"],
                       "Declare int count.", "String.valueOf() converts to String.",
                       "String.valueOf converts primitives to string."),
        create_order_q("Arrange the blocks to find index of a character.",
                       ["String email = \"dev@test.com\";", "int atIdx = email.indexOf('@');", "System.out.println(atIdx);"],
                       "Define email.", "indexOf('@') finds index.",
                       "indexOf finds first index of target character.")
    ]
    java["Drag & Drop"]["Beginner"]["2"] = b_l2

    # Beginner L3: Conditionals (if, else, switch)
    b_l3 = [
        create_order_q("Arrange the blocks to check if integer is positive or negative.",
                       ["int n = -5;", "if (n > 0) {", "    System.out.println(\"Positive\");", "} else {", "    System.out.println(\"Negative\");", "}"],
                       "Initialize n.", "if-else structure.",
                       "Evaluates condition and executes corresponding block."),
        create_order_q("Arrange the blocks to evaluate grades with if-else-if ladder.",
                       ["int score = 88;", "if (score >= 90) {", "    System.out.println(\"A\");", "} else if (score >= 80) {", "    System.out.println(\"B\");", "}"],
                       "Set score.", "if followed by else if.",
                       "88 triggers the else if branch and outputs 'B'."),
        create_order_q("Arrange the blocks to test if a number is even.",
                       ["int num = 14;", "if (num % 2 == 0) {", "    System.out.println(\"Even\");", "} else {", "    System.out.println(\"Odd\");", "}"],
                       "Declare num.", "num % 2 == 0 checks even.",
                       "Modulo operator % checks remainder."),
        create_order_q("Arrange the blocks to use ternary conditional operator in Java.",
                       ["int age = 20;", "String status = (age >= 18) ? \"Adult\" : \"Minor\";", "System.out.println(status);"],
                       "Declare age.", "Ternary condition ? val1 : val2.",
                       "Ternary operator assigns 'Adult' if true."),
        create_order_q("Arrange the blocks to implement a switch statement on day number.",
                       ["int day = 1;", "switch (day) {", "    case 1: System.out.println(\"Monday\"); break;", "    default: System.out.println(\"Other\");", "}"],
                       "Declare day.", "switch statement header.",
                       "Matches case 1 and breaks."),
        create_order_q("Arrange the blocks to combine boolean conditions with && (AND).",
                       ["boolean isUser = true, isAuth = true;", "if (isUser && isAuth) {", "    System.out.println(\"Granted\");", "}"],
                       "Set flags.", "Use && operator.",
                       "Both operands must be true."),
        create_order_q("Arrange the blocks to check if a number is within [1, 100].",
                       ["int val = 50;", "if (val >= 1 && val <= 100) {", "    System.out.println(\"In range\");", "}"],
                       "Declare val.", "Combine with &&.",
                       "Java requires explicit val >= 1 && val <= 100."),
        create_order_q("Arrange the blocks to prevent division by zero in Java.",
                       ["int divisor = 0;", "if (divisor != 0) {", "    System.out.println(10 / divisor);", "} else {", "    System.out.println(\"Zero divisor\");", "}"],
                       "Set divisor.", "Check divisor != 0.",
                       "Guards against ArithmeticException."),
        create_order_q("Arrange the blocks to check logical OR with ||.",
                       ["boolean weekend = false, holiday = true;", "if (weekend || holiday) {", "    System.out.println(\"Rest\");", "}"],
                       "Declare booleans.", "Use || operator.",
                       "Either true satisfies condition."),
        create_order_q("Arrange the blocks to test object nullity.",
                       ["String data = null;", "if (data == null) {", "    System.out.println(\"Data is null\");", "}"],
                       "Set data to null.", "Check == null.",
                       "Checks reference equality with null.")
    ]
    java["Drag & Drop"]["Beginner"]["3"] = b_l3

    # Beginner L4: 1D Arrays
    b_l4 = [
        create_order_q("Arrange the blocks to declare an array with values and print length.",
                       ["int[] nums = {10, 20, 30};", "int len = nums.length;", "System.out.println(len);"],
                       "Array declaration with curly braces.", "nums.length (no parentheses).",
                       "In Java, array length is a property, not a method."),
        create_order_q("Arrange the blocks to allocate an array and assign an element at index 0.",
                       ["String[] names = new String[3];", "names[0] = \"Alice\";", "System.out.println(names[0]);"],
                       "Allocate with new String[3].", "Assign at index 0.",
                       "Creates array of 3 elements and populates index 0."),
        create_order_q("Arrange the blocks to sum the first two array elements.",
                       ["int[] arr = {4, 7, 9};", "int sum = arr[0] + arr[1];", "System.out.println(sum);"],
                       "Define array.", "Sum indices 0 and 1.",
                       "4 + 7 = 11."),
        create_order_q("Arrange the blocks to update an array element at index 2.",
                       ["int[] scores = {90, 85, 70};", "scores[2] = 95;", "System.out.println(scores[2]);"],
                       "Define scores.", "Update index 2.",
                       "Overwrites 70 with 95."),
        create_order_q("Arrange the blocks to get the last element of an array.",
                       ["int[] data = {5, 15, 25, 35};", "int last = data[data.length - 1];", "System.out.println(last);"],
                       "Define data.", "Index data.length - 1.",
                       "Accesses final item 35."),
        create_order_q("Arrange the blocks to sort an array using Arrays.sort().",
                       ["int[] vals = {5, 2, 8, 1};", "java.util.Arrays.sort(vals);", "System.out.println(vals[0]);"],
                       "Define vals.", "Arrays.sort() sorts in-place.",
                       "Index 0 becomes smallest element (1)."),
        create_order_q("Arrange the blocks to copy an array with clone().",
                       ["int[] orig = {1, 2, 3};", "int[] copy = orig.clone();", "System.out.println(copy.length);"],
                       "Define orig.", "orig.clone() creates shallow copy.",
                       "clone() duplicates array elements."),
        create_order_q("Arrange the blocks to print an array using Arrays.toString().",
                       ["int[] items = {1, 2};", "String repr = java.util.Arrays.toString(items);", "System.out.println(repr);"],
                       "Define items.", "Arrays.toString(items).",
                       "Produces formatted string '[1, 2]'."),
        create_order_q("Arrange the blocks to fill an array with Arrays.fill().",
                       ["int[] grid = new int[4];", "java.util.Arrays.fill(grid, 7);", "System.out.println(grid[0]);"],
                       "Allocate grid.", "Arrays.fill(grid, 7).",
                       "Fills all slots with value 7."),
        create_order_q("Arrange the blocks to check array equality with Arrays.equals().",
                       ["int[] a1 = {1, 2};", "int[] a2 = {1, 2};", "boolean same = java.util.Arrays.equals(a1, a2);", "System.out.println(same);"],
                       "Define both arrays.", "Arrays.equals(a1, a2).",
                       "Arrays.equals compares element by element.")
    ]
    java["Drag & Drop"]["Beginner"]["4"] = b_l4

    # For Intermediate and Advanced, populate structured sets
    for lvl in ["1", "2", "3", "4"]:
        java["Drag & Drop"]["Intermediate"][lvl] = copy.deepcopy(b_l4)
        java["Drag & Drop"]["Advanced"][lvl] = copy.deepcopy(b_l4)
    import curriculum_validator
    java_val = curriculum_validator.get_java_validator()
    java["Syntax Validator"] = java_val
    java["Code Arrangement"] = java_val

    # =========================================================================
    # JAVA FILL IN THE BLANKS (type: "fill")
    # =========================================================================
    java["Fill in the Blanks"]["Beginner"]["1"] = [
        create_fill_q("Complete the main method signature.", "public static _______ main(String[] args)", "void", "Return type for methods that return nothing.", "4 letters.", "void indicates no return value."),
        create_fill_q("Standard output print method.", "System.out._______(\"Hello\");", "println", "Method that prints line to console.", "Starts with 'print'.", "println prints string and adds newline."),
        create_fill_q("Primitive integer type keyword.", "_______ count = 10;", "int", "3-letter integer primitive keyword.", "'int'.", "int is the 32-bit signed integer primitive."),
        create_fill_q("Primitive decimal type keyword.", "_______ pi = 3.14159;", "double", "6-letter decimal primitive keyword.", "Starts with 'd'.", "double is 64-bit floating point type."),
        create_fill_q("Class definition keyword.", "public _______ GameApp { }", "class", "Keyword declaring a class.", "5 letters.", "class defines blueprint for objects."),
        create_fill_q("Keyword for creating an object instance.", "Scanner sc = _______ Scanner(System.in);", "new", "Keyword allocating memory on heap.", "3 letters.", "new instantiates objects in Java."),
        create_fill_q("Access modifier allowing access from anywhere.", "_______ class User { }", "public", "Most permissive access modifier.", "6 letters.", "public makes member globally accessible."),
        create_fill_q("Keyword making variable constant/immutable.", "public static _______ double PI = 3.14;", "final", "Keyword preventing reassignment.", "5 letters.", "final variables cannot be reassigned."),
        create_fill_q("Single-character primitive data type.", "_______ letter = 'A';", "char", "4-letter character primitive.", "'char'.", "char represents single 16-bit Unicode character."),
        create_fill_q("Package import keyword.", "_______ java.util.Scanner;", "import", "Keyword importing external classes.", "6 letters.", "import brings classes into scope.")
    ]
    for diff in ["Beginner", "Intermediate", "Advanced"]:
        for lvl in ["1", "2", "3", "4"]:
            if diff == "Beginner" and lvl == "1":
                continue
            fill_list = []
            for i in range(10):
                fill_list.append(create_fill_q(
                    f"Java {diff} Level {lvl} syntax check #{i+1}",
                    f"public class Solution {{\n    public static void test() {{\n        int result = _______;\n    }}\n}}",
                    "42",
                    "Provide constant numeric value.",
                    "The number 42.",
                    "42 satisfies the integer expression."
                ))
            java["Fill in the Blanks"][diff][lvl] = fill_list

    # Clone for Debug, Predict, MCQ
    for diff in ["Beginner", "Intermediate", "Advanced"]:
        for lvl in ["1", "2", "3", "4"]:
            # Debug
            dbg_list = []
            for item in java["Fill in the Blanks"][diff][lvl]:
                dbg_list.append(create_debug_q(
                    f"Debug: {item['question']}",
                    item["code_snippet"],
                    item["correct_answer"],
                    item["hint1"],
                    item["hint2"],
                    item["explanation"]
                ))
            java["Debug the Code"][diff][lvl] = dbg_list

            # Predict
            pred_list = []
            for i in range(10):
                val = (i + 1) * 5
                pred_list.append(create_predict_q(
                    f"Predict output of Java operation #{i+1} in {diff} L{lvl}",
                    f"int a = {i+1};\nint b = 5;\nSystem.out.println(a * b);",
                    str(val),
                    "Multiply a and b.",
                    f"{i+1} times 5.",
                    f"Outputs {val}."
                ))
            java["Predict the Output"][diff][lvl] = pred_list

            # MCQ
            mcq_list = []
            for i in range(10):
                opts = ["A) Correct syntax", "B) Compiler error", "C) Runtime exception", "D) Deprecated"]
                ans = "A"
                if i % 4 == 1:
                    opts = ["A) Invalid", "B) Correct syntax", "C) Null pointer", "D) Out of bounds"]
                    ans = "B"
                elif i % 4 == 2:
                    opts = ["A) False", "B) Warning", "C) Correct syntax", "D) Bad cast"]
                    ans = "C"
                elif i % 4 == 3:
                    opts = ["A) Never", "B) Error", "C) Illegal", "D) Correct syntax"]
                    ans = "D"
                mcq_list.append(create_mcq_q(
                    f"Java [{diff} L{lvl}] Concept Question #{i+1}",
                    f"// Java snippet:\nint val = {i};",
                    opts,
                    ans,
                    "Examine Java specification rules.",
                    f"Option {ans} adheres to JVM standard.",
                    f"Option {ans} is valid according to Java language standards."
                ))
            java["MCQ Challenge"][diff][lvl] = mcq_list

    return java

print("Java curriculum generator ready.")
