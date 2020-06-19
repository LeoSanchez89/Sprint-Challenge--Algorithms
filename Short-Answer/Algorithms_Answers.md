#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
Because it is using a single loop and the time increases linearly depending on n

b) O(n log(n))
Because it is using nested loops, one linear time depending on another linear time gives us O(n^2)

c) O(n)
Because it is calling itself n times until it reaches its base case, it is a linear time

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

if drop >= f:
egg_safe = false
if drop < f:
egg_safe = true

To find f, the most efficient way would be to find the total number of floors, and do a binary search by finding the middle point, and dropping eggs from middle +1 on the right and middle -1 on the left until an egg breaks. The time complexity on it would be O(n) because it would either be using recursion or iteration
