### May 14th answer

## 115 steps required.

We use a stack data structure to keep track of the consecutive characters. We iterate over the string and push each character onto the stack if it is the same as the previous character. If the current character is different from the previous character, we pop all the characters from the stack and increment the step counter. This allows us to avoid iterating over the same characters multiple times and improve the time complexity of the algorithm ideally from O(n) to O(m), where m is the number of distinct consecutive characters in the series.

Language used is Python.