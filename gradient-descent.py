def derivative_at(x):
    return 2*x

x = 10
a = 0.1
delta = 0.001

print(x)
for i in range(1, 10000):
    x -= a * derivative_at(x)
    print(x)
    if x < delta:
        print("timesteps:", i)
        break
