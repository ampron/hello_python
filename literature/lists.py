A = [1, 2, 'a', 4 + 6j, (9, 8), 24]

A.append('new item')
print(A)

A.insert(0, 7)
print(A)

A.extend([5, 10])
print(A)

A += [25, 11]
print(A)

item = A.pop()
print(A)
print(item)

A.pop(0)
print(A)

print(A[0])

print(A[-2])

print(A[:2])

print(A[-2:])

print(A[2:4:-1])

print(A[::-1])

# list comprehensions
B = [x + x for x in A[::2]]
print(B)

C = [x for x in A if isinstance(x, str)]
print(C)

D = [(i, x) for i, x in enumerate(A)]
print(D)
