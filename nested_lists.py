# Using a nested list comprehension and range(), create a variable called answer  with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] . 
answer = [[num for num in range(0,3)] for num in range(0,3)]
print(answer)