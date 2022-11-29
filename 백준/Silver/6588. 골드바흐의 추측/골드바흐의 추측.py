import sys

def is_prime(num):
  if num == 1:
      return False

  if num == 2:
      return True

  for i in range(2, int(num**0.5)+1):
      if num % i == 0:
          return False

  return True

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break

    for i in range(3, N, 2):
        if is_prime(i) == True and is_prime(N-i) == True:
            
            print("{0} = {1} + {2}".format(N, i, N-i))
            break