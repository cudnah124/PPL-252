"""
Object-Oriented Programming - Practice Test Runner
Run this file to test your implementations against all test cases.
"""

print("=" * 80)
print("OBJECT-ORIENTED PROGRAMMING - PRACTICE TEST")
print("=" * 80)
print()

# ============================================================================
# YOUR IMPLEMENTATIONS GO HERE
# ============================================================================

# Question 1: Basic Expression Classes with eval()
class Exp:
    def eval(self):
        pass

class BinExp(Exp):
    def __init__(self, left, op, right):
        # TODO: Implement
        pass
    
    def eval(self):
        # TODO: Implement
        pass

class UnExp(Exp):
    def __init__(self, op, operand):
        # TODO: Implement
        pass
    
    def eval(self):
        # TODO: Implement
        pass

class IntLit(Exp):
    def __init__(self, value):
        # TODO: Implement
        pass
    
    def eval(self):
        # TODO: Implement
        pass

class FloatLit(Exp):
    def __init__(self, value):
        # TODO: Implement
        pass
    
    def eval(self):
        # TODO: Implement
        pass

# Question 2: Add printPrefix() method
# Extend the classes above to include printPrefix() method

# Question 3: Visitor Pattern Implementation
# Implement Visitor base class and concrete visitors (Eval, PrintPrefix, PrintPostfix)

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
    # TODO: Implement
    pass

class PrintPrefix(Visitor):
    # TODO: Implement
    pass

class PrintPostfix(Visitor):
    # TODO: Implement
    pass

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
    test("x6.eval()", lambda: x6.eval(), -8.0)
    
    # Test Question 2: printPrefix()
    print("\n--- Question 2: printPrefix() method ---")
    try:
        test("x1.printPrefix()", lambda: x1.printPrefix(), "1 ")
        test("x2.printPrefix()", lambda: x2.printPrefix(), "2.0 ")
        test("x3.printPrefix()", lambda: x3.printPrefix(), "+ 1 1 ")
        test("x4.printPrefix()", lambda: x4.printPrefix(), "-. 1 ")
        test("x5.printPrefix()", lambda: x5.printPrefix(), "+ -. 1 * 4 2.0 ")
    except AttributeError:
        print("✗ printPrefix() method not implemented")
        total_tests += 5
    
    # Test Question 3: Visitor Pattern
    print("\n--- Question 3: Visitor Pattern ---")
    try:
        # Recreate expressions for visitor pattern
        x1 = IntLit(1)
        x2 = FloatLit(2.0)
        x3 = BinExp(IntLit(1), '+', IntLit(1))
        x4 = UnExp('-', IntLit(1))
        x5 = BinExp(UnExp('-', IntLit(1)), '+', BinExp(IntLit(4), '*', FloatLit(2.0)))
        
        # Test Eval visitor
        test("x1.accept(Eval())", lambda: x1.accept(Eval()), 1)
        test("x3.accept(Eval())", lambda: x3.accept(Eval()), 2)
        test("x5.accept(Eval())", lambda: x5.accept(Eval()), 7.0)
        
        # Test PrintPrefix visitor
        test("x1.accept(PrintPrefix())", lambda: x1.accept(PrintPrefix()), "1 ")
        test("x3.accept(PrintPrefix())", lambda: x3.accept(PrintPrefix()), "+ 1 1 ")
        test("x5.accept(PrintPrefix())", lambda: x5.accept(PrintPrefix()), "+ -. 1 * 4 2.0 ")
        
        # Test PrintPostfix visitor
        test("x1.accept(PrintPostfix())", lambda: x1.accept(PrintPostfix()), "1 ")
        test("x3.accept(PrintPostfix())", lambda: x3.accept(PrintPostfix()), "1 1 + ")
        test("x5.accept(PrintPostfix())", lambda: x5.accept(PrintPostfix()), "1 -. 4 2.0 * + ")
        
    except (AttributeError, NameError) as e:
        print(f"✗ Visitor pattern not fully implemented: {e}")
        total_tests += 9
    
    print("\n" + "=" * 80)
    print(f"RESULTS: {passed_tests}/{total_tests} tests passed")
    print("=" * 80)
    
    if passed_tests == total_tests:
        print("🎉 Congratulations! All tests passed!")
    else:
        print(f"📝 Keep practicing! {total_tests - passed_tests} tests still need work.")

if __name__ == "__main__":
    run_tests()
