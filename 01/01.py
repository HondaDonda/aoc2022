#!/usr/bin/python3
  
  with open('01/input') as infile:
  highest = 0
  current = 0
  lst = []
  for line in infile:
    if len(line.strip()) == 0:
      lst.append(current)
      if current > highest:
        highest = current    
      current = 0
    else:
      current += int(line.strip())

print(highest)
lst = sorted(lst)
print(lst[-1] + lst[-2] + lst[-3])




