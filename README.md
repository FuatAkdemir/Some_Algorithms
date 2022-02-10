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
Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data. 
### **Example**:
input: [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

