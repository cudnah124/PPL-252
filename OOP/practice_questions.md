# Object-Oriented Programming - Practice Questions

## Question 1: Expression Classes with eval()

Define 5 classes to represent arithmetic expressions:
- `Exp`: base class
- `BinExp`: binary operator (+, -, *, /)
- `UnExp`: unary operator (+, -)
- `IntLit`: integer literal
- `FloatLit`: float literal

Objects must have `eval()` method that returns the value of the expression.

Example: 
```python
x = BinExp(IntLit(3), '+', BinExp(IntLit(4), '*', FloatLit(2.0)))
x.eval()  # → 11.0
```

---

## Question 2: Add printPrefix()

Extend the classes above to have `printPrefix()` method that prints expression in prefix format.

Format: 
- Binary: `"op left right "`
- Unary: `"op. operand "` (with dot)

Example:
```python
x = BinExp(UnExp('-', IntLit(1)), '+', BinExp(IntLit(4), '*', FloatLit(2.0)))
x.printPrefix()  # → "+ -. 1 * 4 2.0 "
```

---

## Question 3: Visitor Pattern

Refactor code so classes don't need to change when new operations are added. Use Visitor Pattern.

Implement:
- Base class `Visitor` 
- `Eval` visitor: calculate value
- `PrintPrefix` visitor: print prefix format
- `PrintPostfix` visitor: print postfix format

Cannot use `type()` or `isinstance()`

Example:
```python
x = BinExp(IntLit(1), '+', IntLit(1))
x.accept(Eval())         # → 2
x.accept(PrintPrefix())  # → "+ 1 1 "
x.accept(PrintPostfix()) # → "1 1 + "
```
