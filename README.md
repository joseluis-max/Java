# Java

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
