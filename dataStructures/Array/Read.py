a=[12,13,14,15,16,17];

for i in range(len(a)):
    print(a[i])

for j in a:
    print(j,end=" , ")

for index, value in enumerate(a):
    print(index, value)

print(*a)

numbers = [1, 2, 3, 4]

squares = list(map(lambda number: number * number, numbers))

b = list(map(lambda value: value * value, a))

print(squares);
print(b);

print([words**2 for words in a])
