import sys
n = int(sys.stdin.readline())
count = [0 for i in range(10001)]
for i in range(n):
    m = int(sys.stdin.readline())
    count[m] += 1

for i in range(len(count)):
    sys.stdout.write('%s\n' % i*count[i])
