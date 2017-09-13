def function(x):
    return x ** 2

def derivative_at(x):
    return 2*x

x = 10
learning_rate = 0.1
acceptable_range = 0.0001

# gradient descent helps us find minimas of a function
print("x", "f(x)")
print(x, function(x))
for i in range(1, 10000):
    x -= learning_rate * derivative_at(x)
    print(x, function(x))
    if function(x) < acceptable_range:
        print("timesteps:", i)
        break
