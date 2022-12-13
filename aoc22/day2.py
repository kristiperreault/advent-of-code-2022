# Day 2 - Rock Paper Scissors https://adventofcode.com/2022/day/2

def part1():

  input = open("../test/input_day2.txt")
  score = 0

  for line in input:
    opp_shape = line[0]
    my_shape = line[2]

    if my_shape == 'X':
      score += 1
      if opp_shape == 'A':
        score += 3
      elif opp_shape == 'C':
        score += 6
    elif my_shape == 'Y':
      score += 2
      if opp_shape == 'A':
        score += 6
      elif opp_shape == 'B':
        score += 3
    elif my_shape == 'Z':
      score += 3
      if opp_shape == 'B':
        score += 6
      elif opp_shape == 'C':
        score += 3
  
  print(score)

def part2():
  input = open("../test/input_day2.txt")
  score = 0

  for line in input:
    opp_shape = line[0]
    my_shape = line[2]

    if my_shape == 'X':
      if opp_shape == 'A':
        score += 3
      elif opp_shape == 'B':
        score += 1
      elif opp_shape == 'C':
        score += 2
    elif my_shape == 'Y':
      score += 3
      if opp_shape == 'A':
        score += 1
      elif opp_shape == 'B':
        score += 2
      elif opp_shape == 'C':
        score += 3
    elif my_shape == 'Z':
      score += 6
      if opp_shape == 'A':
        score += 2
      elif opp_shape == 'B':
        score += 3
      elif opp_shape == 'C':
        score += 1
  
  print(score)

part1()
part2()