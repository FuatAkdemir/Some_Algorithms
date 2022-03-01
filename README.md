# **Some Algorithms**
This repo is about **algorithms** and **solutions** that I made. You can examine my solutions to these algorithms that I come across. If there are any questions you want me to solve, please let me know.

## 1) **Even Pair:** (Medium)
Program that returns True if 2 numbers are even in consecutive numbers in the given string expression.
### **Examples**: 
- "hy361jpa68"            -> True, because 6 and 8 is even.
- "75khs34qas98wlk"       -> False.
- "411sd95sl436kdg5fh4"   -> True,  because 4 and 6 is even in 436.

## 2) **Array Couples (Inverted Pairs):** (Hard)
This program looks for pairs with 2 in a given array and if the inverse of the corresponding pair is found, it deletes it from the array.
### **Examples**:
- [4, 5, 1, 4, 5, 4, 4, 1]      -> prints "yes", because all pairs have an reversed form in the array.
- [6, 2, 2, 6, 5, 14, 14, 1]    -> prints "5, 14, 14, 1", because '5, 14' and '14, 1' don't have a reversed form.
- [2, 1, 1, 2, 30, 50]          -> prints "30, 50", because '30, 50' has no reversed form  

## 3) **Flatten List:** (Medium)
Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3], 2]) or non-scalar data. 
### **Example**:
- [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5] -> [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

## 4) **Reverse List:** (Medium)
Write a function that reverses the elements inside the given list. If the elements inside the list also contain the list, reverse their elements as well. 
### **Examples**:
- [[1, 2], [3, 4], [5, 6, 7]] -> [[7, 6, 5], [4, 3], [2, 1]]
- [["a", ["b", "c"]], ["123", 123, [456, 789]]]   ->   [[[789, 456], 123, '123'], [['c', 'b'], 'a']]

## 5) **Counting Minutes**: (Medium)
Function that finds the total minutes in a given time interval in hours.
### **Examples**:
- "9:00am-10:00am" -> 60
- "1:00pm-11:00am" -> 1320

## 6) **Knight Jumps:** (Hard)
A function that returns the number of positions the knight can go if there are no other pieces on a standard chessboard. The current position of the horse will be given as ("x y").
### **Examples**:
- "(1 1)" -> 2
- "(7 6)" -> 6
- "(3 3)" -> 8

## 7) **Fibonacci Checker:** (Medium)
Program that returns "yes" if the given number is in the Fibonacci sequence, and "no" if it is not.

### **Examples**:
- Input: 34 -> Output: yes
- Input: 54 -> Output: no

## 8) **Nearest Smaller Values:** (Medium)
This program compares the elements in a given array in order and prints the lesser or equal number. If there is no element smaller than itself, it adds -1 instead.

### **Examples**:
- Input: [5, 2, 8, 3, 9, 12] -> Output: -1, -1, 2, 2, 3, 9
- Input: [5, 3, 1, 9, 7, 3, 4, 1] -> Output: -1, -1, -1, 1, 1, 1, 3, 1
