in1 = int(input())
in2 = int(input())

c = in2 % 10
b = (in2 % 100) // 10
a = in2 // 100

print(in1 * c)
print(in1 * b)
print(in1 * a)
print(in1 * in2)