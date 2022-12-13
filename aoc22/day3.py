# Day 3 - Rucksack Reorg https://adventofcode.com/2022/day/3
import string

def part1():
  input = open("../test/input_day3.txt")
  values = priority()

  total = 0
  for line in input:
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    char = ''.join(set(first).intersection(second))
    num = values.get(char)
    total += num
  print(total)

def part2():
  input = open("../test/input_day3.txt")
  values = priority()
  total = 0

  for first, second, third in zip(*(map(str.strip, input),) * 3):
    char = ''.join(set(first).intersection(second).intersection(third))
    num = values.get(char)
    total += num
  print(total)

def priority():
  values = dict()
  for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1
  
  for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27
  return values

part1()
part2()