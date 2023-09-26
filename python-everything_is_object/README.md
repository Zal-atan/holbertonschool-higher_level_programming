# This is a Readme for the Python-Everything is Object Project
## In this project we will be answering questions about memory and objects in Python, as well as a couple tasks

# Author - Ethan Zalta

## There are 28 tasks/questions in this project and 6 bonus tasks/questions


## **Question 0**
* What function would you use to print the type of an object?
* Write the name of the function in the file, without ().

## **Question 1**
* How do you get the variable identifier (which is the memory address in the CPython implementation)?
* Write the name of the function in the file, without ().

## **Question 2**
* In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 100

## **Question 3**
* In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 89

## **Question 4**
*  In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a

## **Question 5**
* In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a + 1

## **Question 6**
* What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

## **Question 7**
* What do these 3 lines print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

## **Question 8**
* What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

## **Question 9**
* What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

## **Question 10**
* What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

## **Question 11**
* What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

## **Question 12**
* What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

## **Question 13**
* What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

## **Question 14**
* What does this script print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)

## **Question 15**
* What does this script print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]
>>> print(l2)

## **Question 16**
* What does this script print?
>>> def increment(n):
>>>     n += 1
>>>
>>> a = 1
>>> increment(a)
>>> print(a)

## **Question 17**
* What does this script print?

>>> def increment(n):
>>>     n.append(4)
>>>
>>> l = [1, 2, 3]
>>> increment(l)
>>> print(l)

## **Question 18**
* What does this script print?

>>> def assign_value(n, v):
>>>    n = v
>>>
>>> l1 = [1, 2, 3]
>>> l2 = [4, 5, 6]
>>> assign_value(l1, l2)
>>> print(l1)

## **Task 19**
* Write a function def copy_list(a_list): that returns a copy of a list.

    * The input list can contain any type of objects
    * Your file should be maximum 3-line long (no documentation needed)
    * You are not allowed to import any module

## **Question 20**
* Is a a tuple? Answer with Yes or No.
>>> a = ()

## **Question 21**
* Is a a tuple? Answer with Yes or No.
>>> a = (1, 2)

## **Question 22**
* Is a a tuple? Answer with Yes or No.
>>> a = (1)

## **Question 23**
* Is a a tuple? Answer with Yes or No.
a = (1, )

## **Question 24**
* What does this script print?
>>> a = (1)
>>> b = (1)
>>> a is b

## **Question 25**
* What does this script print?
>>> a = (1, 2)
>>> b = (1, 2)
>>> a is b

## **Question 26**
* What does this script print?
>>> a = ()
>>> b = ()
>>> a is b

## **Question 27**
* Will the last line of this script print 139926795932424? Answer with Yes or No.

>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)

## **Question 28**
* Will the last line of this script print 139926795932424? Answer with Yes or No.
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)

## **Task 29**
* Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

    * introduction
    * id and type
    * mutable objects
    * immutable objects
    * why does it matter and how differently does Python treat mutable and immutable objects
    * how arguments are passed to functions and what does that imply for mutable and immutable objects
* If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

* Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

* When done, please add all urls below (blog post, LinkedIn post, etc.)

https://medium.com/@ethanzalta/but-is-everything-really-object-b234434ea27


## **Task 100**
* Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):

    * Format: see example
    * Your file should be maximum 4-line long (no documentation needed)
    * You are not allowed to import any module

## **Task 101**
* Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

    * You are not allowed to import any module

## **Question 103**
* Assuming we are using a CPython implementation of Python3 with default options/configuration:

    * How many int objects are created by the execution of the first line of the script? (103-line1.txt)
    * How many int objects are created by the execution of the second line of the script (103-line2.txt)

>>> a = 1
>>> b = 1

## **Question 104**
* Assuming we are using a CPython implementation of Python3 with default options/configuration:

    * How many int objects are created by the execution of the first line of the script? (104-line1.txt)
    * How many int objects are created by the execution of the second line of the script (104-line2.txt)
    * After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
    * After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
    * How many int objects are created by the execution of the last line of the script (104-line5.txt)

>>> a = 1024
>>> b = 1024
>>> del a
>>> del b
>>> c = 1024

## **Question 105**
* Assuming we are using a CPython implementation of Python3 with default options/configuration:

    * Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
    * Why? (optional blog post :))

## **Question 106**
* Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

    * How many string objects are created by the execution of the first line of the script? (106-line1.txt)
    * How many string objects are created by the execution of the second line of the script (106-line2.txt)
    * After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
    * After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
    * How many string objects are created by the execution of the last line of the script (106-line5.txt)

>>> a = "SCHL"
>>> b = "SCHL"
>>> del a
>>> del b
>>> c = "SCHL"
