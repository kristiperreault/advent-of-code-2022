# Day 1 - Calorie Counting https://adventofcode.com/2022/day/1

def calorie_counting():

  input = open("../test/input_day1.txt")

  sum = 0
  calories_total = []

  for line in input:

    if line == '\n':
      calories_total.append(sum)
      sum = 0
    else:
      num = int(line)
      sum = sum + num

  total = 0
  for i in range(0,3):
    maximum = max(calories_total)
    total = total + maximum
    calories_total.remove(maximum)

  print(total)

calorie_counting()
