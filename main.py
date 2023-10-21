import hyperloglog
import random
random.seed(12)

def generate_random_ip():
    num1 = str(random.randint(1,255))
    num2 = str(random.randint(1,255))
    num3 = str(random.randint(1,255))
    num4 = str(random.randint(1,255))
    ip = num1 + '.' + num2 + '.' + num3 + '.' + num4
    return ip

myset = set()
hll = hyperloglog.HyperLogLog(0.01)

insert = int(input('number of starting people : '))
for i in range(insert):
    ip = generate_random_ip()
    hll.add(ip)
    myset.add(ip)

print('---------------------------------')
print(f'Hyperloglog count is {len(hll)}')
print(f'Normal count is {len(myset)}')
print('---------------------------------')

while 1:
    cur = input('insert random ip (-1 to exit) ): ')
    if cur == '-1':
        break
    hll.add(cur)
    myset.add(cur)
    print('---------------------------------')
    print(f'Hyperloglog count is {len(hll)}')
    print(f'Real count is {len(myset)}')

