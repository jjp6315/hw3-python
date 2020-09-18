# Author: Ji Woong Park jjp6315@psu.edu
# Section: 005R

def digit_sum(n):
  if n == 0:
    return n
  else: 
     s = 0
  while n > 0:
      s = s + (n % 10)
      n = n // 10
  return s

def run():
  n = input("Enter an int: ")
  n = int (n)
  print(f"sum of digits of a number is: {digit_sum(n)} ")
 

if __name__ == "__main__":
  run()