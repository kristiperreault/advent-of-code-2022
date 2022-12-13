# Day 4 - Camp Cleanup https://adventofcode.com/2022/day/4

def part1():
  input = open("../test/input_day4.txt")
  count = 0

  for line in input:
    my_list = line.split('-')
    first_low = int(my_list[0])
    first_high = int(my_list[1].split(',')[0])
    second_low = int(my_list[1].split(',')[1])
    second_high = int(my_list[2].split('/')[0])

    if (first_low >= second_low and first_high <= second_high):
      count += 1   
    elif (second_low >= first_low and second_high <= first_high):
      count += 1
  
  print(count)

def part2():
  input = open("../test/input_day4.txt")
  count = 0

  for line in input:
    my_list = line.split('-')
    first_low = int(my_list[0])
    first_high = int(my_list[1].split(',')[0])
    second_low = int(my_list[1].split(',')[1])
    second_high = int(my_list[2].split('/')[0])

    if (first_low <= second_high and first_high >= second_low):
      count += 1   
  
  print(count)

part1()
part2()