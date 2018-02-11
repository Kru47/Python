'''Optimised Prime number finding'''
def h(n):
  f = 0
  for i in range(1,n+1):
    if n%i == 0:
      f = f + 1
  return(f == 2)
print(h(11))
print(h(15))