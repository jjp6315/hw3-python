# Author: Ji Woong Park jjp6315@psu.edu
# Section: 005R

def sum_n(n):
  if n == 0:
    return n
  else: 
    n1 = n % 10
    n2 = n // 10
    return n1 + n2
  

def run():
  n = input("Enter an int: ")
  n = int (n)
  print(f"sum of digits of a number is: {sum_n(n)} ")
 


if __name__ == "__main__":
  run()