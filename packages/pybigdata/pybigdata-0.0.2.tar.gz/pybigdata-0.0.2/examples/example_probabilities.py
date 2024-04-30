import random
from pybigdata import probabilities as PROB

x = [random.randint(1, 1000) for _ in range(100)]

var = PROB.var(x)
mean = PROB.mean(x)
mode = PROB.mode(x)

print(f"Variance: {var}")
print(f"Mean: {mean}")
print(f"Mode: {mode}")

# Does variable 'x' normally distributed?
result = PROB.shapiro_wilk_test(x)

if result:
    print("The data points appears to be normally distributed.")
else:
    print("The data points does not appear to be normally distributed.")
