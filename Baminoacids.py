"""
Define a function weightedstring that takes a string input protein. The function returns the weighted string of that protein based on masstable.txt.

weightedstring should read from masstable.txt. It's helpful to have those masses in a dictionary.
"""

def weightedstring(protein):
  dct = {}
  weight = 0
  with open("masstable.txt") as file:
    for line in file:
      (key, value) = line.split(" ")
      dct[key] = (float(value[:-2]))
  lst = [char for char in protein]
  for i in lst:
    weight += dct[i] 
  print(weight)