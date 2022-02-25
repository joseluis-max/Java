# Java

- [Java](#java)
  - [Naming Convetions](#naming-convetions)
  - [Brackets and Parentheses](#brackets-and-parentheses)
  - [Indentations and Spacing](#indentations-and-spacing)
  - [Java and the Command Line](#java-and-the-command-line)
  - [Hello World and Class Structure](#hello-world-and-class-structure)
  - [Print Stataments and Comments](#print-stataments-and-comments)
  - [Variables and types](#variables-and-types)
  - [Conditional Statements and Comparison Operators](#conditional-statements-and-comparison-operators)
  - [Loops](#loops)
  - [User-Defined Methods](#user-defined-methods)
  - [String Methods](#string-methods)
  - [Arrays](#arrays)
  - [2D Arrays](#2d-arrays)
  - [Classes and Constructors](#classes-and-constructors)
  - [Object State and Behavior](#object-state-and-behavior)
  - [Getter and Setter Methods](#getter-and-setter-methods)
  - [Scope](#scope)
  - [Inheritance](#inheritance)
  - [Polymorphism](#polymorphism)
  - [Built-In Data Structures](#built-in-data-structures)
  - [HashMaps](#hashmaps)
  - [Sets](#sets)
  - [Introduction to Dynamic Programming](#introduction-to-dynamic-programming)

## Naming Convetions

Java use `camelCase` for most names, including variables and methods.

Homever, there are some variations:

- Class and Interface names use `PascalCase`
- Constants names use `snake_case` with all uppercase letters.

## Brackets and Parentheses

Brackets `{ }` must be used for all method and class declarations, as well conditionals and loops that contain multiple lines of code.

You can omit brackets for single line conditionals and loops, it's best practice for use them for readability.

``` java
    if (true) {
        return false;
    }
```

is much more readable than

``` java
    if true
        return false;
```

Along the same lines, parentheses `( )` should be used for the arguments of the conditional or loop, as seen in the example above.

## Indentations and Spacing

Whitespace amount doesn't affect the compilation and running, there are standards that help with readability

All indentations should be two spaces and there should be an indentation each time a new block.
There should be spaces before and after keywords and operators.

## Java and the Command Line

**Downloading Java**
Java is available (for free) through Oracle’s website. You can find the appropriate version for your computer [here](https://www.java.com/en/download/manual.jsp). If you have trouble downloading Java, take a look at Oracle’s [help page](https://www.java.com/en/download/help/index_installing.html).

**Compiling Java**
Before you can run the program from the command line, you must compile it. Open your terminal or command prompt (depending on OS), and navigate to the directory where the file you want to run is located. Once there, use javac and the filename to compile:

``` shell
    javac MyClass.java
```

This creates the `.class` file that can be executed. However, if there are any bugs found in your program, they will be flagged at this point, and the executable .class file will not be created. You won’t be able to run the file until it compiles with no issues.

**Running Java**
Once you have your executable file, use java and the name of the class to run it:

``` text
java MyClass
```

**Note**: Do not include the `.java` or `.class` suffixes, only use the name of the class.

Let’s say we had the following Java class:

``` java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}
```

We would compile this using:

``` text
javac HelloWorld.java
```

Then run it using:

``` text
java HelloWorld
```

It would output the following:

``` text
Hello world!
```

**main Method Parameters**
Each Java class must have a main method, and every main method contains the parameters String[] args, but what does that mean?

args is an array of Strings that is passed to the program when it’s run. We don’t need to pass anything in, but we can if we want to. For example, we can edit our HelloWorld class to use elements from args:

``` java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello world, my name is " + args[0] + "!");
  }
}
```

Note that we access the elements of the args array the same way we would access the elements of any other array.

Let’s use the new HelloWorld class to introduce ourselves! First, we’ll compile our class the same way we did before:

``` text
    javac HelloWorld.java
```

Next we’ll run it. However, this time, we’ll add in a `String` argument:

``` text
    java HelloWorld Batman
```

The program will output the following:

``` text
    Hello world, my name is Batman!
```

## Hello World and Class Structure

Printing "Hello world"

``` java
    public class HelloWorld {
        public static void main(String[] args) {
            System.out.print("Hello world");
        }
    }

```

**Java Class Structure**
Java is an object-oriented programming language, which means it consists of classes and their methods. Unlike some other programming languages, Java only has methods (which are associated with classes), and no functions.

Classes

Java classes can be public, private, or protected, depending on the intended scope. They’re declared using one of those keywords, followed by class and the name of the class. The curly braces, { and }, mark the scope of the class. Everything inside the curly braces is part of the class.

Methods

Every Java program must have a method called main(). A method is a sequence of tasks for the computer to execute. This main() method holds all of the instructions for our program and every Java program begins in this method.

## Print Stataments and Comments

**Print Statements**
There are two common ways of printing in Java:

- `System.out.print()`
- `System.out.println()` -> end with a new line

**Comments**
Comments provide information outside the actual lines of code.
They help developvers manintain and document their code.

Inline Comments

``` java
    // This will print: Today is Wednesday.
    System.out.println("Today is Wednesday.");
```

Block comments

``` java
    /* This method takes in two whole numbers and then
    returns their sum */
    public void addNumbers(int a, int b) {
        return a + b;
    }
```

## Variables and types

Variables are used to name, store and reference different types of data.

**Declaring a Variable**
To declare a variable with a value, use the following syntax:

``` java
    dataType variableName = value;
```

To declare a variable without a value, use this syntax instead:

``` java
    dataType variableName;
```

To assign or change a variable value, state the name of the variable followed by the assignment operator (=) and the new value:

``` java
    variableName = newValue;
```

**Types of Data**
In Java, there are several primitive, or built-in, data types:

int

ints store whole number values between -2147483648 and 2147483647.

``` java
    int moonLanding = 1969;
```

double

doubles store decimal number values between 4.9E-324 and 1.7976931348623157E+308:

``` java
    double PI = 3.14;
```

boolean

booleans store true or false values:

``` java
    boolean isRaining = true;
    boolean isSunny = false;
```

char

chars store single character values:

``` java
char firstLetter = 'a';
```

**Manipulating Number-Based Variables**
Arithmetic Operators

Arithmetic Operators can be used to change the value of a number-based variable. These operators can be used for addition (+), subtraction (-), multiplication (*), division (/), and getting the remainder (%):

``` java
    int num = 3 + 2; // num now equals 5
    num = num - 1; // num now equals 4
    num = 4 * 4; // num now equals 16
    num = num / 2; // num now equals 8
    num = num % 5; // num now equals 3
```

**Compound Assignment Operators**
Compound assignment operators perform an arithmetic operation on a variable and then reassigns its value in one step. The compound assignment operator is made up of one arithmetic operator immediately followed by the assignment operator:

``` java
    int num = 3;
    num += 2; // num now equals 5
    num -= 1; // num now equals 4
    num *= 4; // num now equals 16
    num /= 2; // num now equals 8
    num %= 5; // num now equals 3
```

**Increment and Decrement Operators**
The increment operator ++ increases a number value by 1 while the decrement operator decreases a number value by 1:

``` java
    // Increment:
    int age = 47;
    age++; // age now equals 48
    // Decrement:
    int apples = 7;
    apples--; // apples now equals 6
```

Strings

Another common data type in Java is the String. Strings are a reference data type because they are objects from the String class. Strings hold sequences of characters contained within double quotes (").

``` java
    // Option 1 for declaring a String
    String greetings = "Greetings, earthlings!";
    // Option 2 for declaring a String
    String request = new String("Take me to your leader.");
```

## Conditional Statements and Comparison Operators

Conditional statements control the flow of code execution based on the truth value of given boolean expressions.

**if Statements**
The if statement executes a block of code when a specified boolean expression is evaluated as true.

``` java
    if (expression) {
    // Code to run if expression is true
    }
```

**else Statements**
The else statement executes a block of code when the condition inside the if statement is false. The else statement is always the last condition.

``` java
    if (expression) {
    // Code to run if expression is true
    } else {
    // Code to run if expression is false
    }
```

**if-else Statements**
The if-else statement evaluates another condition only when the previous conditional statements evaluate to false. There can be multiple if-else statements in a single conditional statement.

``` java
    if (expression) {
    // Code to run if expression is true
    } else if (expression) {
    // Code to run if previous expression is false and current condition is true
    } else if (expression) {
    // Code to run if previous expression is false and current condition is true
    } else {
    // Code to run if all previous expressions are false
    }
```

**Comparison Operators**
Comparison operators evaluate the relationship between two values in order to determine the expression as true or false.

``` java
    Less Than - x < y

    Greater Than - x > y

    Less Than or Equal To - x <= y

    Greater Than or Equal To - x >= y

    Equal To - x == y

    Not Equal To - x != y
```

**Logical Operators**
Logical operators evaluate the truth value between two or more boolean expressions.

AND - &&

The && operator will return true only if both boolean expressions have a true value; otherwise it will return false:

``` java
    boolean statementA = true;
    boolean statementB = false;
    boolean statementC = true;

    System.out.println(statementA && statementB); // Prints: false
    System.out.println(statementA && statementC); // Prints: true
```

OR - ||

The || operator will return true if at least one of the boolean expressions have a true value; otherwise it will return false:

``` java
    boolean statementA = true;
    boolean statementB = false;
    boolean statementC = false;

    System.out.println(statementA || statementB); // Prints: true
    System.out.println(statementB || statementC); // Prints: false
```

NOT - !

The ! operator returns the negated, or opposite, value of a boolean expression:

``` java
    boolean statementA = true;
    boolean statementB = false;
    System.out.println(!statementA); // Prints: false
    System.out.println(!statementB); // Prints: true
```

## Loops

**while loops**
while loops in Java hinge on a boolean expression that must evaluate to true in order for the loop to run:

``` java
    int num = 0;
    while (num < 20) {
        num = num + 1;
    }
    System.out.println(num) // Prints: 20
```

In the above case, the loop will continue to run until num is no longer less than 20.

**do-while loops**
A do-while loop is very similar to a while loop. The only distinction is that a do-while loop will always execute once before evaluating the condition.

``` java
    do {
        System.out.println("2 is equal to 4!");
    } while (2 == 4);
    // Prints: 2 is equal to 4!
```

If the above code loop was simply a while loop, it would never run since 2 does not equal 4. However, since this is a do-while loop, it will run once, then look at the condition and not run again.
for loops

A for loop header is made up of the following three parts, each separated by a semicolon:

  1. The initialization of the loop control variable.
  2. A boolean expression.
  3. An increment or decrement statement.

``` java
    for (int i = 0; i <= 10; i++) {
        System.out.println(i);
    }
```

The above code will print the numbers from 0 to 10 (inclusive).

**for-each loops**
for-each loops, which are also referred to as enhanced loops, allow us to directly loop through each item in a list of items (like an array or ArrayList) and perform some action with each item.

for-each loop is simpler and more straightforward:

```java
    for (String s : myArray) {
    // Do something
    }
```

**break and continue statements**
break and continue are statements that are used within loops to further control the number of iterations. If we ever want to exit a loop before it finishes all its iterations or want to skip one of the iterations, we can use the break and continue keywords.

break

The break keyword is used to exit, or break, a loop. Once break is executed, the loop will stop iterating. For example:

``` java
    for (int i = 0; i < 10; i++) {
        System.out.println(i);
        if (i == 4) {
            break;
        }
    }
```

Even though the loop was set to iterate until the condition i < 10 is false, the above code will only output the numbers from 0 to 4 (inclusive) because we used break.

continue

The continue keyword can be placed inside of a loop if we want to skip an iteration. If continue is executed, the current loop iteration will immediately end, and the next iteration will begin.

We can use the continue keyword to skip any even valued iteration:

``` java
    int[] numbers = {1, 2, 3, 4, 5};

    for (int i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 == 0) {
            continue;
        }
        System.out.println(numbers[i]);
    }
```

This program would output 1, 3, and 5 since if a number is even, we hit a continue statement, which skips the rest of that iteration, so the print statement is skipped. As a result, we only see odd numbers printed.

## User-Defined Methods

A method is a modular, reusable block of code that can be called throughout a program to complete a certain task.

**Anatomy of a Method**
The first line of a Java method provides important information about a method.

For example:

``` java
    public static void exampleMethod() {
        System.out.println("Hello Method!");
    }
```

The method above is a public, static, method called exampleMethod() that takes in no parameters and returns no values.

- A public method can be accessed by any part of a program, including other classes.
- A static method can be called throughout a program without creating an object of the class.
- A void method does not return a value.
- The above declaration contains empty parentheses; therefore, this method takes no parameters.
- All code placed within the brackets ({ and }) is considered the method body.

**Calling a Method**
To call a method, state the name of the method followed by parentheses (()) and a semicolon (;):

``` java
    public static void exampleMethod() {
        System.out.println("Hello Method!");
    }
    public static void main(String[] args) {
        exampleMethod(); // Prints: Hello Method!
        exampleMethod(); // Prints: Hello Method!
        exampleMethod(); // Prints: Hello Method!
    }
```

**Parameters and Arguments**
Parameters

In order to pass information into a method, we need to add parameters to our method declaration. `Parameters` are placed inside the parentheses of the declaration and must state the data type as well as the parameter name.

``` java
    public static void exampleMethod(String greeting, String name) { // parameters
        System.out.println(greeting + " " + name);
    }
```

The above method takes in two String parameters, greeting and name. Parameters are treated like variables within the body of the method.

Arguments

`Arguments` are the pieces of data that get passed into a method. When calling a method, we must place the `arguments` inside the parentheses of the method call. The `arguments` must be the same data type as the parameters and appear in the same chronological order.

``` java
public static void exampleMethod(String greeting, String name) {
    System.out.println(greeting + " " + name);
}

public static void main(String[] args) {
    exampleMethod("Greetings", "Earthling"); // Prints: Greetings Earthling
    exampleMethod("Hello", "World"); // Prints: Hello World
    exampleMethod("Howdy", "Planet"); // Prints: Howdy Planet
}
```

**Returning a Value**
To return a value from a function, we first must change our method declaration to include the data type of the return value. The return type is placed before the method name. To return a value, use the return keyword followed by the return value inside the method body:

``` java
// Method will return an int value
public static int findProduct(int num1, int num2) {
  return num1 * num2;
}
public static void main(String[] args) {
  int product = findProduct(3,4);
  System.out.println(product); // Prints: 12
}
```

**Method Scope**
Scope defines the environment in which data is available within a program. Method scope dictates what variables accessible within a method. Variables that are created within a method are only accessible inside the method it was created. If we try referencing a method variable outside its method, we would receive an error message.

The following code would produce an error because the main() method references the msg variable which is only available inside the scopeExample() method:

``` java
public static void scopeExample() {
  String msg = "This value is only accessible within this method";
}
public static void main(String[] args) {
  System.out.println(msg);
}
```

## String Methods

The Java String class has many useful methods to help us perform operations and data manipulation on them. We don’t have to import anything to use the String class because it’s a part of the java.lang package, which is available by default.

If you’re looking for a different String method, you can find Oracle’s comprehensive list [here](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html).

**.length()**
The `.length()` method returns the length, or total number of characters, of the String it’s called on:

``` java
String str1 = "Hello World!";
String str2 = "Hi!";
String str3 = "";

System.out.println(str1.length()); // Prints: 12
System.out.println(str2.length()); // Prints: 3
System.out.println(str3.length()); // Prints: 0
```

> Note that spaces and punctuation are included in the count.

**.concat()**
The `.concat()` method concatenates one String to the end of another String. Concatenation is the operation of joining two strings together:

``` java
String name = "Code";
name = name.concat("cademy");
System.out.println(name); // Prints: Codecademy
```

Strings are immutable objects which means that String methods like .concat() do not actually change a String object. If we use .concat() on name without reassigning its value, it won’t change:

``` java
String name = "Code";
name.concat("cademy");
System.out.println(name); // Prints: Code
```

**.equals()**
With objects like Strings, we can’t use the primitive equality operator == to check for equality. Instead, we use the String‘s `.equals()` method:

``` java
String flavor1 = "Mango";
String flavor2 = "Matcha";

System.out.println(flavor1.equals("Mango")); // Prints: true
System.out.println(flavor2.equals("Mango")); // Prints: false
System.out.println(flavor1.equals(flavor2)); // Prints: false
```

There is also an .equalsIgnoreCase() that compares two Strings without considering upper/lower case.

**.indexOf()**
If we want to know the index of the first occurrence of a character in a string, we can use the `.indexOf()` method on a string. Remember that the indices in Java start with 0:

``` java
String letters = "ABCDEFGHIJKLMN";
System.out.println(letters.indexOf("C")); // Prints: 2
```

Although C is the third letter in the English alphabet, it is located in the second index of the string.

Suppose we want to know the index of the first occurrence of an entire substring. The .indexOf() instance method can also return where the substring begins (the index of the first character in the substring):

``` java
String letters = "ABCDEFGHIJKLMN";
System.out.println(letters.indexOf("EFG")); // Prints: 4
```

This outputs 4, because EFG starts at index 4.

If the `.indexOf()` method doesn’t find what it’s looking for, it will return -1.

**.charAt()**
The `.charAt()` method returns the character located at the String‘s specified index:

``` java
String currency = "Yen";
System.out.println(currency.charAt(2)); // Prints: n
```

Suppose we try to return the character located at index 4. It would produce an IndexOutOfBoundsException error because the index 4 is out of currency‘s range:

> java.lang.StringIndexOutOfBoundsException: String index out of range: 4

**.substring()**
There may be times when we only want a part of a string. In such cases, we may want to extract a substring from a string. The .substring() method does exactly that:

```java
String line = "It was the best of times, it was the worst of times.";
System.out.println(line.substring(26)); // Prints: it was the worst of times.
```

It outputs what begins at index 26 and ends at the end of line. The substring begins with the character at the specified index and extends to the end of the string.

But suppose we want a substring from the middle of the string. We can include two arguments with this string method:

``` java
String line = "It was the best of times, it was the worst of times.";
System.out.println(line.substring(7, 24)); // Prints: the best of times
```

It outputs the substring that begins at index 7 and ends at index 23.

**.toUpperCase() and .toLowerCase()**
There will be times when we have a word in a case other than what we need it in. Luckily, Java has a couple String methods to help us out:

- `.toUpperCase()`: returns the string value converted to uppercase
- `.toLowerCase()`: returns the string value converted to lowercase

For example:

``` java
String input = "Cricket!";
System.out.println(input.toUpperCase()); // Prints: "CRICKET!"
System.out.println(input.toLowerCase()); // Prints: "cricket!"
```

## Arrays

**Creating a Populated Array**
To declare an array, state the data type of the array followed by square brackets [] and the array name:

``` java
// Array of ints:
int[] lottoNumbers;

// Array of Strings:
String[] clothingItems;
```

To declare a populated array, the values must be contained within curly brackets ({}) and separated by commas:

``` java
// Array of ints:
int[] lottoNumbers = {12, 29, 4, 38, 3};

// Array of Strings:
String[] clothingItems = {"Huipil", "Beanie", "Kimono", "Sari"};
```

**Accessing an Element by Index**
To access an individual element, state the array name followed by the index of the array element contained within brackets:

``` java
String[] clothingItems = {"Huipil", "Beanie", "Kimono", "Sari"};
System.out.println(clothingItems[2]); // Prints: Kimono
```

> Note that indexing in Java always starts at 0.

**Changing an Element’s Value**
To change a value, select the element via its index and use the assignment operator to set a new value:

``` java
arrayName[index] = newValue;
```

For example:

``` java
String[] clothingItems = {"Huipil", "Beanie", "Kimono", "Sari"};

// Change element value:
clothingItems[1] = "Sweater";
System.out.println(clothingItems[1]); // Prints: Sweater
```

**Creating an Empty Array**
Arrays can be declared as empty and populated at a later time. To declare an empty array, use the following formula:

``` text
dataType[] emptyArrayName = new dataType[number of elements in array];
```

An empty array must be declared with the number of elements it will contain. To populate an empty array, set the index of an element to a value:

``` java
String[] menuItems = new String[5];

menuItems[0] = "Grilled Chicken Fajita";
menuItems[1] = "Fried Plantains";
menuItems[2] = "Black Bean Taco";
menuItems[3] = "Chili Nachos";
menuItems[4] = "Chorizo Burrito";
```

**Getting Array Length**
To find the number of items in a single array, append `.length` to the array name:

``` java
int[] lottoNumbers = {12, 29, 4, 38, 3};
System.out.println(lottoNumbers.length); // Prints: 5
```

**Traversing Through an Array**  
*for loops*  
To traverse an array, use a for loop to iterate from 0 to one less than the length of the array. Inside the loop, use the loop control variable to access the element at the current index:

``` java
int[] lottoNumbers = {12, 29, 4, 38, 3};
for (int i = 0; i < lottoNumbers.length; i++) {
  // Output the current index value:
  System.out.println(lottoNumbers[i]);
}
/*
Prints:
12
29
4
38
3
*/
```

*for-each loops*  
Another option for traversing an array is using a for-each loop:

``` java
int[] lottoNumbers = {12, 29, 4, 38, 3};
for (int num: lottoNumbers) {
  System.out.println(num);
}
/*
Prints:
12
29
4
38
3
*/
```

## 2D Arrays

**Creating a Populated 2D Array**
To declare a 2D array, state the data type of the arrays it will hold followed by two square brackets and the 2D array’s name:

``` java
// 2D int array
int[][] nums;
```

To declare and populate a 2D array using one line of code, place each individual array within curly brackets and separate them using commas:

``` java
int[][] nums = {{10, 9, 8}, {7, 6, 5}, {4, 3, 2}};
```

**Accessing an Element in a 2D Array**
To access an individual element in a 2D array, state the array name followed by two square brackets:

- The first bracket should hold the index of the individual array the element exists in.
- The second bracket should store the index of the element within that individual array.

``` java
int[][] nums = {{10, 9, 8}, {7, 6, 5}, {4, 3, 2}};
// Within the first array, access the second element:
System.out.println(nums[0][1]); // Prints: 9
```

**Updating a 2D Array Element**
To update an element’s value, select the element via its index and use the assignment operator to set a new value:

``` java
char[][] letters = {{'A', 'a'}, {'B', 'x'}, {'C', 'c'}};

// Update the value:
letters[1][1] = 'b';
System.out.println(letters[1][1]); // Prints: b
```

**Creating an Empty 2D Array**
To create an empty 2D array, we must specify the data type, the number of arrays the 2D array will contain, and the number of elements that will be contained within each individual array:

``` java
// This will create an int array with 2 arrays containing 3 elements each:
int[][] intArray = new int[2][3];
```

To populate an empty array, select the index of an element and use the assignment operator to set a value:

``` java
int[][] intArray = new int[2][3];

intArray[0][0] = 1;
intArray[0][1] = 2;
intArray[0][2] = 4;
intArray[1][0] = 1;
intArray[1][1] = 3;
intArray[1][2] = 6;
```

**Traversing Through a 2D Array**
When traversing through a 2D array, we can iterate using row-major order or column-row order.

*Row-Major Order*  
Row-major order for 2D arrays refers to a traversal path that moves horizontally through each row starting at the first row and ending with the last.

![Diagram of row-major order](https://static-assets.codecademy.com/Paths/ap-computer-science/TwoDArrays/row_major.png)

To iterate through a 2D array using row-major order, create a nested for loop.

- The outer loop will iterate from 0 to the length of the 2D array minus 1.
- The nested loop will iterate from 0 to the length of one of the nested arrays minus 1.
- Access the individual element by placing the outer loop’s control variable in the first bracket while placing the inner loop’s control variable in the second bracket:

``` java
char[][] letters = {{'A', 'a'}, {'B', 'b'}, {'C', 'c'}};

for (int i = 0; i < letters.length; i++){
  for (int j = 0; j < letters[0].length; j++){
    System.out.print(letters[i][j]);
  }
}
// Prints: AaBbCc
```

*Column-Row Order*  
Column-major order for 2D arrays refers to a traversal path which moves vertically down each column starting at the first column and ending with the last.

![Diagram of column-major order](https://static-assets.codecademy.com/Paths/ap-computer-science/TwoDArrays/column_major.png)

To iterate through a 2D array using row-major order, create a nested for loop.

- The outer loop will iterate from 0 to the length of one of the nested arrays minus 1.
- The nested loop will iterate from 0 to the length of the 2D array minus 1.
- Access the individual element by placing the inner loop’s control variable in the first bracket while placing the outer loop’s control variable in the second bracket:

``` java
char[][] letters = {{'A', 'a'}, {'B', 'b'}, {'C', 'c'}};

for (int i = 0; i < letters[0].length; i++){
  for (int j = 0; j < letters.length; j++){
    System.out.print(letters[j][i]);
  }
}
// Prints: ABCabc
```

## Classes and Constructors

**Classes**
A class is the set of instructions that describe how an instance can behave and what information it contains. Java has predefined classes such as System, which we’ve used in logging text to our screen, but we will often have to create our own classes.

**General Structure**
Here’s a definition of a Java class:

``` java
public class Car {

  public static void main(String[] args) {

  }
}
```

This example defines a `public class` named `Car`.

**Access Modifiers**
public is an access level modifier that allows other classes to interact with this class.

There are four types of access modifiers, each with different scopes:

![public is visible everywhere; protected is visible in the class, the package, and child classes; a member with no modifier is visible in the class and package; private is visible only in the class itself](https://content.codecademy.com/courses/learn-java/revised-2019/access-modifiers-chart.png)

The scope ranges from `public` classes, which are accessible from anywhere in the program, to `private` classes, which are only accessible in the class itself.

**Constructors**
In order to create an object (an instance of a class), we need a constructor method. The constructor is defined within the class.

Let’s take a look at the `Car` class with a constructor. The constructor, Car(), shares the same name as the class:

``` java
public class Car {
  // Constructor method:
  public Car() {
    // Instructions for creating a Car instance
  }  

  public static void main(String[] args) {

  }
}
```

To create an instance, we need to call or invoke the constructor within `main()`. The following example assigns a `Car` instance to the variable `ferrari`:

``` java
public class Car {

  public Car() {
    // Instructions for creating a Car instance
  }

  public static void main(String[] args) {
    // Invoke the constructor:
    Car ferrari = new Car();
  }
}
```

In this example, instead of being declared with a primitive data type like `int` or `boolean`, our variable `ferrari` is declared as a reference data type. This means that the value of our variable is a reference to an instance’s memory address. During its declaration, the class name is used as the variable’s type. In this case, the type is `Car`.

After the assignment operator, (=), we invoke the constructor method: `Car()`, and use the keyword `new` to indicate that we’re creating an instance. Omitting new causes an error.

If we were to output the value of ferrari we would see its memory address:

``` text
Car@76ed5528
```

**Invoking the Constructor**
When we create a new instance of our class, we invoke (or call) the constructor. This means that any code inside the constructor will be executed:

``` java
public class Car {

  public Car() {
    System.out.println("I'm a constructor!");
  }

  public static void main(String[] args) {
    // Invoke the constructor:
    Car ferrari = new Car(); // Prints: I'm a constructor!
  }
}
```

## Object State and Behavior

**Creating an Object**
Objects and classes are closely related because classes define the attributes and behaviors of an object. To create an object, declare a variable in the main() method with the class name as the data type and set the value to a call to the class’ constructor:

``` java
class Cat {
  // Class constructor:
  public Cat(){
    // Instructions for creating an instance of Cat goes here:
  }

  public static void main(String[] args) {
    // Create a Cat object by calling the constructor:
    Cat myCat = new Cat();
  }
}
```

The class name is used as the data type because objects have reference data types meaning that the value of the variable is a reference to an instance’s memory address.

**Object State**
State refers to the attributes of an object. State can be defined using instance variables, or instance fields, which are placed inside of a class.

**Creating Instance Fields**
To create an instance field, initialize variables inside the class container:

``` java
class Cat {
  // instance fields:
  String noise = "meow";
  int numLives = 9;

  public Cat(){
    // Instructions for creating an instance of Cat goes here:
  }

  public static void main(String[] args) {
    Cat myCat = new Cat();
  }
}
```

To access an object’s instance fields, append the dot operator followed by the instance field’s name to the name of the object:

``` java
Cat myCat = new Cat();
// Access instance variable of an object:
System.out.println(myCat.noise); // Prints: meow
```

**Defining State with Parameters**
To create dynamic objects, parameters can be added to the class constructor. Instance variables can then be assigned the parameter values:

``` java
class Cat {
  // Instance fields:
  String noise;
  int numLives = 9;

  // Constructor takes in one String parameter
  public Cat(String animalNoise){
    // Assign instance variable to parameter value:
    noise = animalNoise;
  }

  public static void main(String[] args) {
    // Send argument to constructor when creating an object:
    Cat firstCat = new Cat("mew");
    // Send argument to constructor when creating another object:
    Cat secondCat = new Cat( "mow");

    System.out.println(firstCat.noise); // Prints: mew
    System.out.println(secondCat.noise); // Prints: mow
  }
}
```

**The this Keyword**
The `this` keyword is used to reference the current object within any class method or constructor. The `this` keyword can be useful in clarifying what value is being referred to if any parameter values use the same name as an instance variable.

To use the `this` keyword, prepend `this` followed by `.` to the instance variable:

``` java
class Cat {
  String noise;
  int numLives = 9;

  // Parameter has same name as the instance variable
  public Cat(String noise){
    // Assign instance variable to parameter value:
    this.noise = noise;
  }
}
```

**Object Behavior**  
*Non-Static Methods*  
In order to give behavior to objects, we need to create non-static methods. A non-static method is a method that belongs to a class. A non-static method can be identified by the lack of the `static` keyword in the method signature:

``` java
class Cat {
  String noise;
  int numLives = 9;

  // Non-static method:
  public void speak() {
    System.out.println(noise);
  }

  public Cat(String animalNoise){
    noise = animalNoise;
  }

  public static void main(String[] args) {
    Cat myCat = new Cat("mew");
  }
}
```

*Invoking a Non-Static Method*  
A non-static method can only be invoked by an object of the class in which the method was created. To call a non-static method, state the object’s name followed by `.`, the method name, and parentheses:

``` java
Cat myCat = new Cat("mew");
// Invoke non-static method on an object:
myCat.speak(); // Prints: mew
```

**The .toString() Method**
If an object is placed inside of a print statement, the output shows the data type of the object (the class name) followed by the memory address of the object:

``` java
public static void main(String[] args) {
  Cat myCat = new Cat("mew");
  System.out.println(myCat); // Prints: Cat@6bc7c054
}
```

The `.toString()` method can be added to a class in order to create a unique output when printing an object. The original .toString() method exists within the Object class; however, the .toString() method is often overridden in subclasses to create a unique output for each individual class:

``` java
class Cat {
  String noise;
  int numLives = 9;

  public String toString() {
    System.out.println("The cat with " + numLives + " lives says " + noise);
  }

  public Cat(String animalNoise){
    noise = animalNoise;
  }

  public static void main(String[] args) {
    Cat myCat = new Cat("mew");
    System.out.println(myCat); // Prints: The cat with 9 lives says mew
  }
}
```

## Getter and Setter Methods

When writing classes, we often make all of our instance variables private. However, we still might want some other classes to have access to them, we just don’t want those classes to know the exact variable name.

**Accessor Methods**
To give other classes access to a private instance variable, we would write an accessor method (also known as a “getter” method).

``` java
public class Dog {
  private String name;

  // Other methods and constructors

  public String getName() {
    return name;
  }

  public static void main(String[] args) {
    Dog myDog = new Dog("Lassie");
    System.out.println(myDog.getName()); // Prints: Lassie
  }
}
```

Even though the instance variable `name` is `private`, other classes could call the `public` method `getName()` which returns the value of that instance variable. Accessor methods are always `public` and have a return type that matches the type of the instance variable they’re accessing.

**Mutator Methods*
Similarly, `private` instance variables often have mutator methods (also known as “setters”). These methods allow other classes to reset the value stored in `private` instance variables.

``` java
public class Dog {
  private String name;

  // Other methods and constructors

  public void setName(String newName) {
    name = newName;
  }

  public static void main(String[] args){
    Dog myDog = new Dog("Cujo");
    myDog.setName("Lassie");
  }
}
```

Mutator methods are often `void` methods. They don’t return anything, they just reset the value of an existing variable. Similarly, they often have one parameter that is the same type as the variable they’re created to change.

## Scope

`scope` defines where a certain variable or method is accessible in a program.

**Variable Scope**
Variables can be defined as having one of three types of scope:

1. class level scope
2. method level scope
3. block scope

**Class Level Scope**
Class level scope (instance variables): any variable declared within a class is accessible by all methods in that class. Depending on its access modifier (ie. `public` or `private`), it can sometimes be accessed outside the class.

``` java
public class Car {
  public String color;
  private int speed;

  public Car(String color, int speed) {
    // Variables color and speed accessible here
  }

  public void drive(boolean fourWheel) {
    // Variables color and speed accessible here
  }
}

public class BuyCar {
  public static void main(String[]args) {
    Car carObject = new Car("blue", 70);
    // Can access the public variable, color, in this class
    String carColor = carObject.color;
    // Can’t access the private variable, speed, in this class
    // int carSpeed = carObject.speed -- This results in an error, can’t access speed here
  }
}
```

**Method Level Scope**
Method level scope (local variables): any variable declared within a method, arguments included, is NOT accessible outside that method.

``` java
public class Car {
  public String color;
  private int speed;

  public void drive(boolean fourWheel) {
    String tires = "wide";
    // fourWheel and tires are only accessible here
    // fourWheel and tires are destroyed after drive() finishes
  }

  public void paint(String newColor, String oldColor) {
    // newColor and oldColor are only accessible here
    // newColor and oldColor are destroyed after paint() finishes
  }
}

public class PaintCar {
  // The only variable from Car accessible in this class is color
  // None of the variables declared in Car methods are accessible in this class
}
```

**Block Scope**
Block scope (loop variables): any variable declared in a `for` loop condition is not accessible after the loop, unless you defined it beforehand.

``` java
public class Car {
  public void changeTires() {
    int numTires = 4;
    int changedTires = 0;
    for (i = 0; i < numTires; i++) {
      changedTires += 1;
    }
    // numTires and changedTires are accessible here, i is not
  }
}
```

**Access Modifiers**
In Java, there are four access modifiers that restrict the accessibility of the method or variable to which the modifier is applied. They are only used within classes, not within methods. public and private are the most relevant modifiers to our work, but let’s briefly discuss all of them.

*private*  
The most restrictive modifier. It limits access to methods and variables to the class in which they are declared. private is chosen when there is no need to use certain methods or variables outside the class.

*default*  
Allows access only from within the current package. If there is no specified access modifier, the method or variable will take on this one. Learn more about the [default modifier](https://javarevisited.blogspot.com/2012/10/difference-between-private-protected-public-package-access-java.html).

*protected*  
Allows access to a method or variable only from within the current package, unless it is accessed through a child class outside of the package. Learn more about the [protected modifier](https://javarevisited.blogspot.com/2012/10/difference-between-private-protected-public-package-access-java.html).

*public*  
The least restrictive modifier. It allows access to a class, method or variable not only from within the class in which it is declared, but outside as well. This is the modifier we will most commonly use, but to understand the scenarios in which to use the others, check out the [Oracle documentation](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html).

*Example*  
Min-heaps are a data structure that keeps track of the minimum element in a dataset; let’s look at the `MinHeap` class to help us understand `private` vs. `public`.

The `.bubbleUp()` method is `private` because “bubbling up,” or adjusting a heap after adding an element, is an internal process, not something that needs to be performed outside the `MinHeap` class. `.add()` on the other hand is a basic min-heap function so should be made `public`.

``` java
public class MinHeap {
  public ArrayList<Integer> heap;
  public int size;

  public MinHeap() {
    // Body of constructor
  }
  public void add(int value) {
    heap.add(value);
    size++;
    bubbleUp();
  }
  private void bubbleUp() {
    // Body of .bubbleUp() method
  }
}

public class TrackAges {
  public static void main(String[]args) {
    MinHeap ages = new MinHeap();
    // Can call public MinHeap .add() method here:
    ages.add(42);
    ages.add(15);
    ages.add(27);
    // Can’t call private MinHeap .bubbleUp() method here
    // Don’t need to because .add() calls .bubbleUp()!
  }
}
```

## Inheritance

Inheritance is the concept of allowing a class to inherit the methods and properties of another class.

**Superclasses and Subclasses**
Superclasses refer to the class that another class inherits from. Subclasses refer to the class that inherits qualities from another class. An object of a subclass inherits all the available instance variables and methods provided in the superclass class.

In order to create a superclass/subclass relationship between two classes, the class declaration of the subclass must be modified to include the extends keyword followed by the name of the superclass. No changes need to be made to the superclass:

``` java
class Shape {
  Shape() {
    System.out.println("I am a shape!");
  }
}
// Make Triangle a subclass of Shape:
class Triangle extends Shape {
  Triangle() {
    System.out.print("I am a triangle!");
  }
  public static void main(String[] argos) {
    Shape sq = new Shape(); // Prints: I am a shape!
    Triangle tri = new Triangle();
    /*Prints:
    I am a shape!
    I am a triangle!
    */
  }
}
```

**The super() Method**
When an instance of a subclass is created, the subclass’ constructor will automatically invoke the superclass’ constructor. The `super()` method allows us to control what arguments are sent to the superclass constructor when creating an object of the subclass.

To invoke the `super()` method, place `super()` in the body of the subclass’ constructor; the `()` can hold any specific arguments that an instance of the subclass should contain:

``` java
class Shape {
  int numSides;
  Shape(int numSides) {
    this.numSides = numSides;
  }
}

class Triangle extends Shape {
  Triangle() {
    // Use super() to call the Shape constructor:
    super(3);
  }

  public static void main(String[] args) {
    Shape sq = new Shape(4);
    Triangle tri = new Triangle();
    System.out.println(sq.numSides); // Prints: 4
    System.out.println(tri.numSides); // Prints: 3
  }
}
```

**Access Modifiers**
public is an access level modifier that allows other classes to interact with this class.

![There are four types of access modifiers, each with different scopes: public is visible everywhere. protected is visible in the class, the package, and child classes. a member with no modifier is visible in the class and package. private is visible only in the class itself](https://content.codecademy.com/courses/learn-java/revised-2019/access-modifiers-chart.png)

The scope ranges from `public` classes, which are accessible from anywhere in the program, to `private` classes, which are only accessible in the class itself.

## Polymorphism

polymorphism allows a subclass to share the information and behavior of its superclass while also incorporating its own functionality.

**Using Methods of a Superclass**
In order for an instance of a subclass to use a superclass method, append `.` and the superclass’ method name to the name of the object:

``` java
// Parent class:
class Bird {
  public Bird() {
    // Instructions for creating a Bird go here:
  }

  public void move() {
    System.out.println("The bird flies away");
  }
}

// Child class:
class Flamingo extends Bird {
  public Flamingo() {
    // Instructions for creating a Flamingo go here:
  }

  public static void main(String[] args) {
     Flamingo myFlamingo = new Flamingo();
     myFlamingo.move(); // The bird flies away
  }
}
```

**Overriding Superclass Methods**
If we want a subclass method that behaves differently than a superclass method with the same name, we can override the method. To override a superclass method, the method in the subclass must have the same method signature as the superclass method. The subclass method should also have @Override placed above its method signature:

``` java
// Parent class:
class Bird {
  public Bird() {
    // Instructions for creating a Bird go here:
  }

  public void move() {
    System.out.println("The bird flies away");
  }
}

// Child class:
class Penguin extends Bird {
  public Penguin() {
    // Instructions for creating a Penguin go here:
  }

  // Override the parent class method:
  @Override
  public void move() {
    System.out.println("The penguin waddles away");
  }

  public static void main(String[] args) {
    Penguin myPenguin = new Penguin();
    myPenguin.move(); // Prints: The penguin waddles away
  }
}
```

**Using a Subclass in Place of its Superclass**
Polymorphism makes it possible to send an instance of a subclass somewhere where an instance of the superclass is expected.

*Creating an Instance*  
We can use the superclass as the reference data type when creating a new object from a subclass. For example, if `Succulent` is a subclass of `Plant`, we can create an instance with a declared type of `Plant` but an actual type of `Succulent`:

``` java
Plant echeveria = new Succulent();
```

*Creating Arrays or ArrayLists*  
Arrays and `ArrayList`s can only contain values of the same type. If we declare either of these data structures to hold objects from a superclass, we can also use the data structure to store objects from its subclasses.

For example, if `Monster` is a superclass to the classes `Vampire`, `Werewolf`, and `Zombie`, we can create a `Monster` type `ArrayList` that stores objects from any of `Monster`‘s subclasses:

``` java
Monster dracula, wolfman, evilZombie;

dracula = new Vampire();
wolfman = new Werewolf();
evilZombie = new Zombie();

Monster[] monsters = {dracula, wolfman, evilZombie};
```

*Sending an Object as a Parameter*  
If a method or constructor parameter requires an object of a superclass to be passed in when it is invoked, we can send an object of the subclass as an argument.

For example, if Cat is a subclass of Animal, we can send in an instance of Cat as an argument:

``` java
class Vet {
  public void Vet() {
    // Instructions for instance go here:
  }
  public void getCheckUp(Animal patient) {
    // Instructions for method go here:
  }

  public void main(String[] args) {
    // Create a Vet object
    Vet catDoctor = newVet();
    // Create an Animal object
    Animal myCat = new Cat();
    // Send Animal object as a parameter for a Vet method:
    catDoctor.getCheckUp(myCat);
  }
}
```

## Built-In Data Structures

**Lists**
When we work with arrays in Java, we’re limited by the fact that once an array is created, it has a fixed size. To create mutable and dynamic lists, we can use Java’s built-in List classes. They allow us to:

- Store object references as elements
- Store elements of the same type (just like arrays)
- Access elements by index (just like arrays)
- Add elements
- Remove elements

If you want to know more about Java’s other built-in `List` classes, you can look through the [Javadocs here](https://docs.oracle.com/javase/8/docs/api/java/util/List.html).

**ArrayLists**
Java’s built-in ArrayList class uses a dynamic array to store its elements. You can still retrieve elements using their indices, but there is no size limit. In general, ArrayLists are more efficient than other types of lists when it comes to storing and accessing their elements.

We’ll covering the most common methods, but you can find the [comprehensive list here](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html).

***Declaring an ArrayList***

`ArrayLists` must be declared with the type that it will store inside the angle brackets (`<>`). You can declare a new `ArrayList` of `Integer`s as follows:

``` java
ArrayList<Integer> myList = new ArrayList<Integer>();
```

We can’t use primitive types inside the angle brackets, which is why we have `Integer` instead of `int`.

The above code creates an empty list with the initial capacity of `10`. If you want to create your list with a specified initial capacity, you can do that as well:

``` java
// Create an ArrayList with a capacity of 12:
ArrayList<String> months = new ArrayList<String>(12);
```

As you add to the list, it will grow to accommodate all the elements, regardless of what your initial capacity was.

> Note: You must import `java.util.ArrayList` at the top of your program.

***Adding to an ArrayList***

You can add to the end of the list using the `.add()` method:

``` java
ArrayList<String> months = new ArrayList<String>(12);
months.add("January");
System.out.println(months): // Prints: [January]
```

Since this is an `ArrayList`, you can also add an element to a specified index:

``` java
ArrayList<String> months = new ArrayList<String>(12);
months.add("January");
months.add("February");
months.add("June");
// Change the value at index 2:
months.add(2, "March");
System.out.println(months); // Prints: [January, February, March, June]
```

If an element already exists at that index, the new element takes its place, and everything following (including the original element) is shifted over by one.

Note that you can only add an element to a specified index that already exists, or to the end of the list. For example, if we tried to add an element to index 9 in a list that only has 3 elements, we will get this message:

> java.lang.IndexOutOfBoundsException

***Retrieving a Value from an ArrayList***

The `ArrayList` class has a `.get()` method that takes in an index and returns the element at the index:

``` java
ArrayList<String> months = new ArrayList<String>(12);
months.add("January");
months.add("February");
months.add("March");
System.out.println(months.get(1)); // Prints: February
```

> Note that, like arrays, ArrayList‘s indices start at 0.

***Removing from an ArrayList***

We can use `.remove()` to remove elements from an `ArrayList`:

``` java
ArrayList<String> months = new ArrayList<String>(12);
months.add("January");
months.add("February");
months.add("March");
months.remove(1);
System.out.println(months); // Prints: [January, March]
```

In the above code, we removed the element found at index 1. We can also use the `.remove()` method to remove the first occurrence of an element (meaning we don’t need to know its index):

``` java
ArrayList<String> months = new ArrayList<String>(12);
months.add("January");
months.add("February");
months.add("March");
months.remove("February");
System.out.println(months); // Prints: [January, March]
```

**LinkedLists**
While `ArrayList`s are better for storing and accessing data, `LinkedList`s are more efficient when manipulating data. This is because the `LinkedList` class uses a doubly linked list to store its elements.

We’ll covering the most common methods, but you can find the comprehensive list [here](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html).

***Declaring a LinkedList***

There are no sizes associated with `LinkedList`s, but we still have to specify what type we want the list to be:

``` java
LinkedList<String> days = new LinkedList<String>();
```

> Note: You must `import java.util.LinkedList` at the top of your program.

***Adding to a LinkedList***

The LinkedList class has an `.add()` method that we use to add to the end of the list:

``` java
LinkedList<String> days = new LinkedList<String>();
days.add("Monday");
days.add("Tuesday");
System.out.println(days); // Prints: [Monday, Tuesday]
```

You can also include an index to specify where you want the new element to go:

``` java
LinkedList<String> days = new LinkedList<String>();
days.add("Monday");
days.add("Tuesday");
days.add(0, "Sunday");
System.out.println(days); // Prints: [Sunday, Monday, Tuesday]
```

***Retrieving a Value from a LinkedList***

We can use the `.get()` method to retrieve elements from specified indices in the list:

``` java
LinkedList<String> days = new LinkedList<String>();
days.add("Monday");
days.add("Tuesday");
days.add(0, "Sunday");
System.out.println(days.get(1)); // Prints: Monday
```

There are also `.getFirst()` and `.getLast()` methods that return the first and last elements in the list, respectively.

***Removing from a LinkedList***

We can use `.remove()` to remove elements from the list:

``` java
LinkedList<String> days = new LinkedList<String>();
days.add("Monday");
days.add("Tuesday");
days.add(0, "Sunday");
days.remove(1);
System.out.println(days); // Prints: [Sunday, Tuesday]
```

Above, we specified the index from which we wanted an element removed, but we can also use the method to remove the first occurrence of a specified element:

``` java
LinkedList<String> days = new LinkedList<String>();
days.add("Monday");
days.add("Tuesday");
days.add(0, "Sunday");
days.remove("Monday");
System.out.println(day); // Prints: [Sunday, Tuesday]
```

We can also use `.remove()` with no arguments to remove the `head` (first element) of the list:

``` java
LinkedList<String> days = new LinkedList<String>();
days.add("Monday");
days.add("Tuesday");
days.add(0, "Sunday");
days.remove();
System.out.println(days); // Prints: [Monday, Tuesday]
```

## HashMaps

A HashMap is a built-in data structure that stores a collection of key-value pairs. Each key acts as a unique identifier for its associated value.

***Creating a HashMap***

In order to use this built-in data structure and its methods, we need to import `HashMap` class at the top of our Java code:

``` java
import java.util.HashMap;
```

To declare a `HashMap`, we need to state the data type of both the key and the value.

> Note that a HashMap only takes in reference type values:

``` java
// Declare a HashMap with String keys and Integer values:
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
```

***Adding a Key-Value Pair***

The HashMap class contains a `.put()` method that is used to add `key-value` pairs to a `HashMap`. The method requires two arguments; the first argument will be added as the key, while the second argument will be added as the associated value:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();

// Add key-value pairs to HashMap:
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Output a HashMap:
System.out.println(teaSteepingTemp); // Prints: {Oolong=185, Rooibos=212}
```

***Accessing a Value***

The `.get()` method is used to access an individual HashMap value. This method requires one argument: the key. The key is used as a unique identifier for its value:

int oolongTemp = teaSteepingTemp.get("Oolong");
System.out.println(oolongTemp);  // Prints: 185

***Removing Values***
***Removing a Single Key-Value Pair***

To remove a single key-value pair, attach the `.remove()` method to the name of the HashMap with the key as the argument:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Remove an item:
teaSteepingTemp.remove("Oolong");
System.out.println(teaSteepingTemp); // Prints: {Rooibos=212}
```

***Removing all Key-Value Pairs***

The `.clear()` method will remove all the key-value pairs in a HashMap:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Remove all items:
teaSteepingTemp.clear();
System.out.println(teaSteepingTemp); // Prints: {}
```

***Finding a HashMap’s Size***

The `.size()` method returns the number of key-value pairs present in a HashMap:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Output the size of a HashMap:
System.out.println(teaSteepingTemp.size()); // Prints: 2
```

***Traversing a HashMap***

In order to access each individual element in a HashMap, we can use for-each loops to iterate through the data structure:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Iterate through the HashMap:
for (String key : teaSteepingTemp.keySet()) {
  System.out.println("Brew " + key + " tea at " + teaSteepingTemp.get(key) + "°F");
}
/*
Prints:
Brew Oolong tea at 185°F
Brew Rooibos tea at 212°F
*/
```

***Additional HashMap Methods***

To view the complete list of `HashMap` methods, take a look at [Java’s official documentation](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html).

`*.containsKey()*`
The .containsKey() method takes in a key as an argument and returns true or false depending on if the key is present in the HashMap:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Check for keys:
System.out.println(teaSteepingTemp.containsKey("Oolong")); // Prints: true
System.out.println(teaSteepingTemp.containsKey("Green")); // Prints: false
```

`*.replace()*`
The `.replace()` method is used to modify the value associated with a key. This method takes two arguments: the key and the new value:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Replace a value:
teaSteepingTemp.replace("Rooibos", 245);
System.out.println(teaSteepingTemp.get("Rooibos")); // Prints: 245
```

`*.keySet()*`
The `.keySet()` method returns a Set containing all the key values in the HashMap:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Output only the keys:
System.out.println(teaSteepingTemp.keySet()); // Prints: [Oolong, Rooibos]
```

`*.values()*`
The `.values()` method returns a Collection containing all the values (without their keys) in the HashMap:

``` java
HashMap<String, Integer> teaSteepingTemp = new HashMap<>();
teaSteepingTemp.put("Oolong", 185);
teaSteepingTemp.put("Rooibos", 212);

// Output only the values:
System.out.println(teaSteepingTemp.values()); // Prints: [185, 212]
```

## Sets

A Set stores an unordered collection of unique values.

**Set Types**  
The `Set` class is derived from the `Collection` class. It contains all the methods from the `Collection` class, but ensures that every element it contains is unique.

There are multiple implementations of a `Set`: the `HashSet`, the `TreeSet`, and the `LinkedHashSet`. While these classes share the similarities of storing unique objects and having access to the same methods, there are a few key differences between the three.

***HashSet***

- `HashSet` is implemented using a `HashMap` instance.
- The order of the elements stored within a `HashSet` is random.
- A `HashSet` is capable of storing a null value.
- A `HashSet` has a O(1) runtime for the `.add()`, `.remove()`, and `.contains()` methods. `HashSets` typically runs faster than the other two options.

***TreeSet***

- A `TreeSet` is implemented using a `TreeMap` instance.
- The element order is determined using a comparator (e.g. numerical or alphabetical order).
- A `TreeSet` cannot store a null value.
- A `TreeSet` has a slower runtime with an O(log n) run time for the `.add()`, `.remove()`, and `.contains()` methods.

***LinkedHashSet***

- A LinkedHashSet is implemented using a doubly-linked list and a hash table.
- The order in which elements are stored is determined by the order in which the element is added.
- A LinkedHashSet is capable of storing a null value.
- A LinkedHashSet has a O(1) runtime for the .add(), .remove(), and .contains() methods, but has a slightly slower runtime than a `HashSet`.

**Creating a Set**
In order to utilize a `Set` and its associated operations, we must import its class at the top of our program. Note that we only need to import the class of the type of set we are using:

``` java
// Import Set class:
import java.util.Set;

// Import HashSet class:
import java.util.HashSet;

// Import TreeSet class:
import java.util.TreeSet;

// Import LinkedHashSet class:
import java.util.LinkedHashSet;

// Import all classes:
import java.util.*;
```

To create a `Set`, state the data type of the elements as well as the type of set that will be used. Note that a Set can only contain reference type values:

``` java
// Create a HashSet that will contain String values:
Set<String> colors = new HashSet<String>();

// Create a TreeSet that will contain Integer values:
TreeSet<Integer> myNumbers = new TreeSet<Integer>();
```

***Set Methods***

There are many useful methods within the `Set` class that allow us to create and modify our `Set` objects.

> Note: The following examples will only show methods being performed on HashSets; however, these methods can be used on TreeSets and LinkedHashSets as well.

***Adding Items to a Set***

To populate a Set with items, use the .add() method with the new value as an argument.

``` java
Set<String> colors = new HashSet<String>();

// Add items to Set:
colors.add("red");
colors.add("blue");
colors.add("blue"); // Duplicate value

System.out.println(colors); // Prints: [red, blue]
```

> Note that any duplicate items added to the Set will be ignored.

***Removing Items from a Set***

To remove a single item from a Set, attach the .remove() method to the Set name with the value to be removed as the argument:

``` java
Set<String> colors = new HashSet<String>();
colors.add("red");
colors.add("blue");

// Remove an item:
colors.remove("red");
System.out.println(colors); // Prints: [blue]
```

***Checking for A Value***

The `.contains()` method returns a true or false value depending on if the given argument is contained within the Set:

``` java
Set<String> colors = new HashSet<String>();
colors.add("red");
colors.add("blue");

// Check for items:
System.out.println(colors.contains("red")); // Prints: true
System.out.println(colors.contains("green")); // Prints: false
```

***Finding the Size of a Set***

The `.size()` method returns the number of items contained in a Set:

``` java
Set<String> colors = new HashSet<String>();
colors.add("red");
colors.add("blue");

// Find size of Set
System.out.println(colors.size()); // Prints: 2
```

***Iterating Through A Set***

If we want to iterate through each item in a Set, we can use a for-each loop:

``` java
Set<String> colors = new HashSet<String>();
colors.add("red");
colors.add("blue");

// Iterate through the Set:
for (String item: colors) {
  System.out.println(item);
}
/*
Prints:
red
blue
*/
```

***Using Set Operations***

The `Set` class contains several methods that perform different mathematical operations on two different sets. We can use these methods to create new sets or modify existing ones.
Union

The union of two sets will combine all the values in each set together. We can create a set union by invoking the `.addAll()` method.

To implement this method, attach `.addAll()` to the name of a `Set` and use the other `Set` as the argument value:

``` java
Set<String> colors = new HashSet<String>();
colors.add("red");
colors.add("orange");

Set<String> primary = new HashSet<String>();
primary.add("red");
primary.add("yellow");

// Modify colors to store a union between colors set and primary set:
colors.addAll(primary);
System.out.println(colors); // Prints: [red, orange, yellow]
```

***Intersection***

The intersection of two sets will contain all the overlapping values between two sets. We can replicate the intersection of two sets by appending `.retainAll()` method to one set while sending the other set as an argument:

``` java
Set<String> colors = new HashSet<String>();
colors.add("red");
colors.add("orange");

Set<String> primary = new HashSet<String>();
primary.add("red");
primary.add("yellow");

// Modify colors to store the intersection between colors set and primary set:
colors.retainAll(primary);
System.out.println(colors); // Prints: [red]
```

***Complement***

The complement of two sets stores the values of one set after removing any overlapping values from another set. To show the complement of two sets in Java, we can use the `.removeAll()` method. The placement of the Sets in this method call matters. The resulting `Set` will contain only the values found only in the Set that the method is appended to; any value that appears in the argument `Set` will be removed:

``` java
Set<String> colors = new HashSet<String>();
colors.add("red");
colors.add("orange");

Set<String> primary = new HashSet<String>();
primary.add("red");
primary.add("yellow");

// Modify colors to store the complement between colors set and primary set:
colors.removeAll(primary);
System.out.println(colors); // Prints: [orange]
```

## Introduction to Dynamic Programming

**What is Dynamic Programming?**
Dynamic Programming is a programming technique used to solve recursive problems more efficiently. Specifically, it adds time efficiency, and it does so by taking advantage of data structures to store reusable solutions to intermediate steps, thus saving redundant computations. It’s a way of solving problems with recursive relationships by solving smaller problems and building up to the solution to the original problem.

Let’s take a look at a simple algorithm that can get computationally complex very quickly, and then let’s use dynamic programming to increase its efficiency.

***Fibonacci***
The Fibonacci series is a classic mathematical series in which each number is equal to the sum of the two numbers before it, always starting with 0 and 1:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, etc.

The 0th Fibonacci number is always 0 and first Fibonacci number is always 1. So the second Fibonacci number is 0 + 1 = 1, third Fibonacci number is 1 + 1 = 2, and so on. You could calculate the nth number iteratively this way, but you could also calculate it recursively:

``` text
fib(n)
  if n is 0 or 1
    return n
  else
    return fib(n - 1) + fib(n - 2)
```

This technique breaks up calculating the nth number into many smaller problems, calculating each step as the sum of calculating the previous two numbers.

Although this technique will certainly work to find the correct number, as n grows, the number of recursive calls grows very quickly. Let’s visualize all the function calls if we were to calculate the fourth Fibonacci number:

``` text
fib(4) -> fib(3) + fib(2)
  fib(3) -> fib(2) + fib(1)
    fib(2) -> fib(1) + fib(0)
  fib(2) -> fib(1) + fib(0)
```

As you can see fib(2) is called twice, fib(1) is called three times. If n were larger than 4, you’d see these numbers of calls get high very quickly. For instance, to calculate the 10th number, we’d make 34 calls to fib(2) and 177 total function calls! Why do we need to call the same function multiple times with the same input?

We don’t! We can use a dynamic programming technique called memoization to cut down greatly on the number of function calls necessary to calculate the correct number.

***Memoization***
Memoization is a specialized form of caching used to store the result of a function call. The next time that function is called, if the result of that function call is already stored somewhere, we’ll retrieve that instead of running the function itself again. Memoization can result in much faster overall execution times (although it can increase memory requirements as function results are stored in memory).

Memoization is a great technique to use alongside recursion. The memo can even be saved between function calls if it’s being used for common calculations in a program.

***Memoizing Fibonacci***
In the previous example, many function calls to fib() were redundant. Let’s memoize it in order to speed up execution.

To begin, we’ll use a Java HashMap to store the memoized values. Each key will represent n (starting from 0), and the corresponding value will be the result of that Fibonacci number. Then, whenever we need to calculate a number, if it’s already been calculated, we can retrieve the value from the map in O(1) time.

In pseudocode, our approach to memoization will look something like this:

``` text
Create a memo map

fibMemo(n, map)
  if n is 0 or 1
    return n
  if n key exists in map
    return map.get(n)
  else
    calculate current fibonacci number through a recursive call
    store value in map
    return value
```

***Conclusion***

Dynamic programming and memoization are great techniques breaking up complex recursive problems into smaller chunks. They are especially useful when tackling problems that involve combinations. For example, if I asked you to calculate the total number of ways to get four dice rolls to sum to 13, you could imagine breaking that into multiple parts. You could split 13 into 6 and 7 and then find all the combinations of two rolls that would match each one of these. As you went down each path, you’d probably start seeing a lot of similar calculations, and memoization would help you reduce the number of overall function calls by storing intermediate values.

Some other common problems that can be solved using dynamic programming are the knapsack problem, the rod cutting problem, and the word break problem.
