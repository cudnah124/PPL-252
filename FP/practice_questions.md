# Functional Programming - Practice Questions

## Question 1: dist() - High-order Function
Write function `dist(lst, n)` that returns a list of pairs (element, n) using higher-order function.

Example: `dist([1,2,3], 4)` → `[(1,4), (2,4), (3,4)]`

---

## Question 2: dist() - Recursive
Write function `dist(lst, n)` that returns a list of pairs (element, n) using recursion.

Example: `dist([1,2,3], 4)` → `[(1,4), (2,4), (3,4)]`

---

## Question 3: dist() - List Comprehension
Write function `dist(lst, n)` that returns a list of pairs (element, n) using list comprehension.

Example: `dist([1,2,3], 4)` → `[(1,4), (2,4), (3,4)]`

---

## Question 4: flatten() - High-order Function
Write function `flatten(lst)` that flattens nested list using higher-order function.

Example: `flatten([[1,2,3], [4,5], [6,7]])` → `[1,2,3,4,5,6,7]`

---

## Question 5: flatten() - List Comprehension
Write function `flatten(lst)` that flattens nested list using list comprehension.

Example: `flatten([[1,2,3], [4,5], [6,7]])` → `[1,2,3,4,5,6,7]`

---

## Question 6: flatten() - Recursive
Write function `flatten(lst)` that flattens nested list using recursion.

Example: `flatten([[1,2,3], [4,5], [6,7]])` → `[1,2,3,4,5,6,7]`

---

## Question 7: lessThan() - High-order Function
Write function `lessThan(lst, n)` that returns a list of numbers < n using higher-order function.

Example: `lessThan([1,2,3,4,5], 4)` → `[1,2,3]`

---

## Question 8: lessThan() - Recursive
Write function `lessThan(lst, n)` that returns a list of numbers < n using recursion.

Example: `lessThan([1,2,3,4,5], 4)` → `[1,2,3]`

---

## Question 9: lessThan() - List Comprehension
Write function `lessThan(lst, n)` that returns a list of numbers < n using list comprehension.

Example: `lessThan([1,2,3,4,5], 4)` → `[1,2,3]`

---

## Question 10: lstSquare() - Recursive
Write function `lstSquare(n)` that returns a list of squares from 1 to n using recursion.

Example: `lstSquare(3)` → `[1,4,9]`

---

## Question 11: lstSquare() - List Comprehension
Write function `lstSquare(n)` that returns a list of squares from 1 to n using list comprehension.

Example: `lstSquare(3)` → `[1,4,9]`

---

## Question 12: lstSquare() - High-order Function
Write function `lstSquare(n)` that returns a list of squares from 1 to n using higher-order function.

Example: `lstSquare(3)` → `[1,4,9]`

---

## Question 13: compose()
Write function `compose(f, g, h, ...)` that composes functions. Example: `compose(f,g,h)(x)` = `f(g(h(x)))`

Example: `compose(increase, square)(3)` → `10` (because increase(square(3)) = increase(9) = 10)
