def printLine(lines):
  print("\nThis file contains", len(lines), "lines")
  line = 1
  while line != 0:
    line = int(input("\nEnter which line to print or type 0 to stop: "))
    if line > 0 and line <= len(lines):
      index = line - 1
      print("\"" + lines[index] + "\"")
    elif line < 0 or line > len(lines):
      print(">Invalid line. Please try again")
  print("\nHave a good day now.")