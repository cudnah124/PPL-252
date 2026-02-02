"""
Functional Programming - Complete Solutions
This file contains all correct implementations from the practice answers.
Use this to verify the test runner works correctly.
"""

from functools import reduce

print("=" * 80)
print("FUNCTIONAL PROGRAMMING - SOLUTION VERIFICATION")
print("=" * 80)
print()

# Helper functions for Question 13
def increase(x):
    return x + 1

def square(x):
    return x * x

def double(x):
    return x * 2

def decrease(x):
    return x - 1

# ============================================================================
# COMPLETE SOLUTIONS
# ============================================================================

# Question 1: dist() - High-order Function Approach
def dist_hof(lst, n):
    return list(map(lambda x: (x, n), lst))

# Question 2: dist() - Recursive Approach
def dist_recursive(lst, n):
    if lst == []:
        return []
    else:
        return [(lst[0], n)] + dist_recursive(lst[1:], n)

# Question 3: dist() - List Comprehension
def dist_comprehension(lst, n):
    return [(x,n) for x in lst]

# Question 4: flatten() - High-order Function Approach
def flatten_hof(lst):
    if not lst: 
        return []
    return list(reduce(lambda x,y: x+y, lst))

# Question 5: flatten() - List Comprehension
def flatten_comprehension(lst):
    return [x for y in lst for x in y]

# Question 6: flatten() - Recursive Approach
def flatten_recursive(lst):
    if lst == []:
        return []
    else:
        return lst[0] + flatten_recursive(lst[1:])

# Question 7: lessThan() - High-order Function Approach
def lessThan_hof(lst, n):
    return list(filter(lambda x: x < n, lst))

# Question 8: lessThan() - Recursive Approach
def lessThan_recursive(lst, n):
    if lst == []:
        return []
    else:
        if lst[0] < n:
            return [lst[0]] + lessThan_recursive(lst[1:], n)
        else:
            return lessThan_recursive(lst[1:], n)

# Question 9: lessThan() - List Comprehension
def lessThan_comprehension(lst, n):
    return [x for x in lst if x < n]

# Question 10: lstSquare() - Recursive Approach
def lstSquare_recursive(n: int):
    if (not n):
        return []
    else:
        return lstSquare_recursive(n-1) + [n2]

# Question 11: lstSquare() - List Comprehension
def lstSquare_comprehension(n: int):
    return [x2 for x in range(1,n+1)]

# Question 12: lstSquare() - High-order Function Approach
def lstSquare_hof(n: int):
    return list(map(lambda x: x2, range(1,n+1)))

# Question 13: compose() - Function Composition
def compose(arg1, arg2, *args):
    if not args:
        return lambda x: arg1(arg2(x))
    else:
        return lambda x: arg1(compose(arg2, *args)(x))

# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    total_tests = 0
    passed_tests = 0
    
    def test(name, func, expected, *args):
        nonlocal total_tests, passed_tests
        total_tests += 1
        try:
            result = func(*args)
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
    
    # Test dist functions
    print("\n--- Question 1-3: dist() ---")
    for func_name, func in [("HOF", dist_hof), ("Recursive", dist_recursive), ("Comprehension", dist_comprehension)]:
        test(f"dist {func_name}: ([1,2,3],4)", func, [(1, 4),(2, 4),(3, 4)], [1,2,3], 4)
        test(f"dist {func_name}: ([],4)", func, [], [], 4)
        test(f"dist {func_name}: ([1,2,3],'a')", func, [(1, 'a'),(2, 'a'),(3, 'a')], [1,2,3], 'a')
    
    # Test flatten functions
    print("\n--- Question 4-6: flatten() ---")
    for func_name, func in [("HOF", flatten_hof), ("Comprehension", flatten_comprehension), ("Recursive", flatten_recursive)]:
        test(f"flatten {func_name}: ([[1,2,3],[4,5],[6,7]])", func, [1,2,3,4,5,6,7], [[1,2,3],[4,5],[6,7]])
        test(f"flatten {func_name}: ([[]])", func, [], [[]])
        test(f"flatten {func_name}: ([])", func, [], [])
    
    # Test lessThan functions
    print("\n--- Question 7-9: lessThan() ---")
    for func_name, func in [("HOF", lessThan_hof), ("Recursive", lessThan_recursive), ("Comprehension", lessThan_comprehension)]:
        test(f"lessThan {func_name}: ([1,2,3,4,5],4)", func, [1,2,3], [1,2,3,4,5], 4)
        test(f"lessThan {func_name}: ([],3)", func, [], [], 3)
        test(f"lessThan {func_name}: ([5,2,6,4,1],3)", func, [2,1], [5,2,6,4,1], 3)
    
    # Test lstSquare functions
    print("\n--- Question 10-12: lstSquare() ---")
    for func_name, func in [("Recursive", lstSquare_recursive), ("Comprehension", lstSquare_comprehension), ("HOF", lstSquare_hof)]:
        test(f"lstSquare {func_name}: (3)", func, [1,4,9], 3)
        test(f"lstSquare {func_name}: (1)", func, [1], 1)
        test(f"lstSquare {func_name}: (5)", func, [1,4,9,16,25], 5)
    
    # Test compose function
    print("\n--- Question 13: compose() ---")
    try:
        f = compose(increase, square)
        test("compose(increase,square)(3)", lambda: f(3), 10)
        
        f = compose(increase, square, double)
        test("compose(increase,square,double)(3)", lambda: f(3), 37)
        
        f = compose(increase, square, double, decrease)
        test("compose(increase,square,double,decrease)(3)", lambda: f(3), 17)
    except Exception as e:
        print(f"✗ compose tests - Error: {e}")
    
    print("\n" + "=" * 80)
    print(f"RESULTS: {passed_tests}/{total_tests} tests passed")
    print("=" * 80)
    
    if passed_tests == total_tests:
        print("🎉 Congratulations! All tests passed!")
    else:
        print(f"📝 Keep practicing! {total_tests - passed_tests} tests still need work.")

if __name__ == "__main__":
    run_tests()
