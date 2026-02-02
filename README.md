# PPL Programming Practice - README

## 📚 Overview

This practice set was created from Programming Code tests of the Principles of Programming Languages (PPL) course. It includes 2 main topics:

- Functional Programming (FP): 13 questions
- Object-Oriented Programming (OOP): 3 questions

## 📁 Folder Structure

```
ProgrammingCode/
├── FP/                                    # Functional Programming
│   ├── practice_questions.md              # Detailed questions
│   ├── practice_test.py                   # Automated test runner
│   ├── solutions.py                       # Complete solutions
│   └── fp_questions_extracted.txt         # Raw text from PDF
│
├── OOP/                                   # Object-Oriented Programming
│   ├── practice_questions.md              # Detailed questions
│   ├── practice_test.py                   # Automated test runner
│   ├── solutions.py                       # Complete solutions
│   └── oop_questions_extracted.txt        # Raw text from PDF
│
└── README.md                              # This file
```

## 🎯 How to Use

### Method 1: Practice and Test

1. Read questions: Open `practice_questions.md` in corresponding folder
2. Write code: Open `practice_test.py` and implement functions/classes as required
3. Run tests: 
   ```bash
   python FP/practice_test.py
   # or
   python OOP/practice_test.py
   ```
4. View solutions: If needed, check `solutions.py`

### Method 2: Learn from Solutions

1. Read questions in `practice_questions.md`
2. Think about solutions
3. Review solutions in `solutions.py`
4. Understand logic and implementation
5. Rewrite code from scratch to practice

## 📖 Content Details

### Functional Programming (13 questions)

Topics: Higher-order functions, Recursion, List Comprehension

| Q# | Topic | Requirement |
|-----|--------|---------|
| 1-3 | `dist()` | Create list of pairs - 3 approaches: HOF, Recursive, List Comprehension |
| 4-6 | `flatten()` | Flatten nested list - 3 approaches: HOF, Recursive, List Comprehension |
| 7-9 | `lessThan()` | Filter elements < n - 3 approaches: HOF, Recursive, List Comprehension |
| 10-12 | `lstSquare()` | List of squares - 3 approaches: Recursive, List Comprehension, HOF |
| 13 | `compose()` | Function composition with variable arguments |

Skills practiced:
-  Higher-order functions: `map()`, `filter()`, `reduce()`
-  Lambda expressions
-  Recursion and base cases
-  List comprehension
-  Variable arguments (`*args`)

### Object-Oriented Programming (3 questions)

Topics: Class design, Methods, Visitor Pattern

| Q# | Topic | Requirement |
|-----|--------|---------|
| 1 | Class Hierarchy | Implement expression classes with `eval()` method |
| 2 | Extension | Add `printPrefix()` method to classes |
| 3 | Visitor Pattern | Refactor code using Visitor pattern to separate logic |

Skills practiced:
-  Class inheritance
-  Method overriding
-  Polymorphism
-  Visitor Pattern (Important Design Pattern!)
-  Separation of concerns

## 💡 Study Tips

### Functional Programming

1. Understand 3 approaches:
   - High-order function: Use `map()`, `filter()`, `reduce()` with lambda
   - Recursion: Base case + recursive case
   - List comprehension: Concise syntax `[expr for item in list if condition]`

2. Practice each pattern:
   - Complete all `dist()` questions first to understand the 3 approaches
   - Then apply similarly to `flatten()` and `lessThan()`

3. Watch for edge cases:
   - Empty list `[]`
   - Single element
   - Different data types

### Object-Oriented Programming

1. Question 1: Understand class hierarchy
   ```
   Exp (base)
   ├── BinExp (+, -, *, /)
   ├── UnExp (+, -)
   ├── IntLit
   └── FloatLit
   ```

2. Question 2: Extending classes
   - Add method to all classes
   - Remember format: Binary `"op left right"`, Unary `"op. operand"`

3. Question 3: VISITOR PATTERN (Important!)
   - Why needed: Avoid adding new methods to classes for every new operation
   - How it works: Double dispatch (accept → visit)
   - Benefits: Separation of concerns, Open/Closed Principle

## 🔥 Additional Challenges

After completing basic exercises:

### FP Challenges:
1. Write `compose()` without using recursion
2. Implement `unflatten(lst, pattern)` - reverse of flatten
3. Create decorator to cache results of recursive functions

### OOP Challenges:
1. Add `PrintInfix()` visitor to print regular format: `"1 + (2 * 3)"`
2. Create `Simplify()` visitor to simplify expressions (e.g., `x + 0 = x`)
3. Implement `Derivative()` visitor to calculate derivatives

## 📊 Study Progress

Create personal checklist:

### Functional Programming
- [ ] dist() - 3 approaches
- [ ] flatten() - 3 approaches  
- [ ] lessThan() - 3 approaches
- [ ] lstSquare() - 3 approaches
- [ ] compose() - Variable arguments

### Object-Oriented Programming
- [ ] Expression classes with eval()
- [ ] Extend with printPrefix()
- [ ] Visitor Pattern implementation
- [ ] Understand why we use Visitor

## 🚀 Next Steps

1. LEXER: Lexical analysis (no practice set yet)
2. SYNTAX: Syntax analysis (no practice set yet)

More practice sets can be created for these 2 topics if PDFs are available!

## 📞 Support

If you encounter issues:
- Check test cases in `practice_test.py`
- Read explanations carefully in `solutions.py`
- Debug by printing intermediate results
- Compare output with expected output

---

Good luck with your practice! 🎓
