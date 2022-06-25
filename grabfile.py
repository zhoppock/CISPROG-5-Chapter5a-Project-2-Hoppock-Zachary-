def grabfile():
  fileName = input("Enter filename of numbers: ")
  f = open(fileName, 'r')

  lineList = [line.rstrip('\n') for line in f]

  print("Your sequence of line from", fileName, "are:\n", lineList)
  return lineList