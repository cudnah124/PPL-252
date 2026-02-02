"""
Object-Oriented Programming - Complete Solutions
This file contains all correct implementations from the practice answers.
Use this to verify the test runner works correctly.
"""

print("=" * 80)
print("OBJECT-ORIENTED PROGRAMMING - SOLUTION VERIFICATION")
print("=" * 80)
print()

# ============================================================================
# COMPLETE SOLUTIONS
# ============================================================================

# Question 1 & 2: Basic Expression Classes with eval() and printPrefix()
class Exp:
    def eval(self):
        pass
    
    def printPrefix(self):
        pass
    
    def accept(self, visitor):
        pass

class BinExp(Exp):
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right
    
    def eval(self):
        if self.op == '+':
            return self.left.eval() + self.right.eval()
        elif self.op == '-':
            return self.left.eval() - self.right.eval()
        elif self.op == '*':
            return self.left.eval() * self.right.eval()
        elif self.op == '/':
            return self.left.eval() / self.right.eval()
    
    def printPrefix(self):
        return f"{self.op} {self.left.printPrefix()}{self.right.printPrefix()}"
    
    def accept(self, visitor):
        return visitor.visitBinExp(self)

class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    
    def eval(self):
        if self.op == '+':
            return self.operand.eval()
        elif self.op == '-':
            return -self.operand.eval()
    
    def printPrefix(self):
        return f"{self.op}. {self.operand.printPrefix()}"
    
    def accept(self, visitor):
        return visitor.visitUnExp(self)

class IntLit(Exp):
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value) + " "
    
    def accept(self, visitor):
        return visitor.visitIntLit(self)

class FloatLit(Exp):
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value) + " "
    
    def accept(self, visitor):
        return visitor.visitFloatLit(self)

# Question 3: Visitor Pattern Implementation
class Visitor:
    def visitBinExp(self, exp):
        pass
    
    def visitUnExp(self, exp):
        pass
    
    def visitIntLit(self, exp):
        pass
    
    def visitFloatLit(self, exp):
        pass

class Eval(Visitor):
    def visitBinExp(self, exp):
        if exp.op == '+':
            return exp.left.accept(self) + exp.right.accept(self)
        elif exp.op == '-':
            return exp.left.accept(self) - exp.right.accept(self)
        elif exp.op == '*':
            return exp.left.accept(self) * exp.right.accept(self)
        elif exp.op == '/':
            return exp.left.accept(self) / exp.right.accept(self)
    
    def visitUnExp(self, exp):
        if exp.op == '+':
            return exp.operand.accept(self)
        elif exp.op == '-':
            return -exp.operand.accept(self)
    
    def visitIntLit(self, exp):
        return exp.value
    
    def visitFloatLit(self, exp):
        return exp.value

class PrintPrefix(Visitor):
    def visitBinExp(self, exp):
        return f"{exp.op} {exp.left.accept(self)}{exp.right.accept(self)}"
    
    def visitUnExp(self, exp):
        return f"{exp.op}. {exp.operand.accept(self)}"
    
    def visitIntLit(self, exp):
        return str(exp.value) + " "
    
    def visitFloatLit(self, exp):
        return str(exp.value) + " "

class PrintPostfix(Visitor):
    def visitBinExp(self, exp):
        return f"{exp.left.accept(self)}{exp.right.accept(self)}{exp.op} "
    
    def visitUnExp(self, exp):
        return f"{exp.operand.accept(self)}{exp.op}. "
    
    def visitIntLit(self, exp):
        return str(exp.value) + " "
    
    def visitFloatLit(self, exp):
        return str(exp.value) + " "

# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    total_tests = 0
    passed_tests = 0
    
    def test(name, func, expected):
        nonlocal total_tests, passed_tests
        total_tests += 1
        try:
            result = func()
            if result == expected:
                print(f"✓ {name}")
                passed_tests += 1
            else:
                print(f"✗ {name}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
        except Exception as e:
            print(f"✗ {name}")
            print(f"  Error: {e}")
    
    # Test Question 1: eval()
    print("\n--- Question 1: eval() method ---")
    x1 = IntLit(1)
    x2 = FloatLit(2.0)
    x3 = BinExp(IntLit(1), '+', IntLit(1))
    x4 = UnExp('-', IntLit(1))
    x5 = BinExp(UnExp('-', IntLit(1)), '+', BinExp(IntLit(4), '*', FloatLit(2.0)))
    x6 = BinExp(UnExp('-', IntLit(1)), '-', BinExp(IntLit(4), '*', FloatLit(2.0)))
    
    test("x1.eval()", lambda: x1.eval(), 1)
    test("x2.eval()", lambda: x2.eval(), 2.0)
    test("x3.eval()", lambda: x3.eval(), 2)
    test("x4.eval()", lambda: x4.eval(), -1)
    test("x5.eval()", lambda: x5.eval(), 7.0)
    test("x6.eval()", lambda: x6.eval(), -9.0)
    
    # Test Question 2: printPrefix()
    print("\n--- Question 2: printPrefix() method ---")
    test("x1.printPrefix()", lambda: x1.printPrefix(), "1 ")
    test("x2.printPrefix()", lambda: x2.printPrefix(), "2.0 ")
    test("x3.printPrefix()", lambda: x3.printPrefix(), "+ 1 1 ")
    test("x4.printPrefix()", lambda: x4.printPrefix(), "-. 1 ")
    test("x5.printPrefix()", lambda: x5.printPrefix(), "+ -. 1 * 4 2.0 ")
    
    # Test Question 3: Visitor Pattern
    print("\n--- Question 3: Visitor Pattern ---")
    
    # Recreate expressions for visitor pattern
    x1_v = IntLit(1)
    x2_v = FloatLit(2.0)
    x3_v = BinExp(IntLit(1), '+', IntLit(1))
    x4_v = UnExp('-', IntLit(1))
    x5_v = BinExp(UnExp('-', IntLit(1)), '+', BinExp(IntLit(4), '*', FloatLit(2.0)))
    
    # Test Eval visitor
    test("x1.accept(Eval())", lambda: x1_v.accept(Eval()), 1)
    test("x3.accept(Eval())", lambda: x3_v.accept(Eval()), 2)
    test("x5.accept(Eval())", lambda: x5_v.accept(Eval()), 7.0)
    
    # Test PrintPrefix visitor
    test("x1.accept(PrintPrefix())", lambda: x1_v.accept(PrintPrefix()), "1 ")
    test("x3.accept(PrintPrefix())", lambda: x3_v.accept(PrintPrefix()), "+ 1 1 ")
    test("x5.accept(PrintPrefix())", lambda: x5_v.accept(PrintPrefix()), "+ -. 1 * 4 2.0 ")
    
    # Test PrintPostfix visitor
    test("x1.accept(PrintPostfix())", lambda: x1_v.accept(PrintPostfix()), "1 ")
    test("x3.accept(PrintPostfix())", lambda: x3_v.accept(PrintPostfix()), "1 1 + ")
    test("x5.accept(PrintPostfix())", lambda: x5_v.accept(PrintPostfix()), "1 -. 4 2.0 * + ")
    
    print("\n" + "=" * 80)
    print(f"RESULTS: {passed_tests}/{total_tests} tests passed")
    print("=" * 80)
    
    if passed_tests == total_tests:
        print("🎉 Congratulations! All tests passed!")
    else:
        print(f"📝 Keep practicing! {total_tests - passed_tests} tests still need work.")

if __name__ == "__main__":
    run_tests()
