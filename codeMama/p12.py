from math import sqrt

a = list(map(float, input().split()))
b = list(map(float, input().split()))
c = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
print(f"Distance: {c:.2f}")
# What is the difference between the two snippets?
# The first snippet uses cmath.sqrt() while the second snippet uses math.sqrt().
# The cmath.sqrt() function is used to compute the square root of a complex number.
# The math.sqrt() function is used to compute the square root of a real number.
