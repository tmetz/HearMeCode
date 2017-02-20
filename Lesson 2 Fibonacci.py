fib_seq = [0, 1]

for i in range(2,10):
    fib_seq.append(fib_seq[i - 2] + fib_seq[i - 1])

print fib_seq
