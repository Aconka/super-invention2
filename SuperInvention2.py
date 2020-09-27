def disp(num): #disp stuff
  print("result = ", num)

num1 = 0 #diming vars
num2 = 0
data = -1
while data != 0: #main program look exits on 0 selection
  if data == 1: #pick numbers
    num1 = int(input("number 1:"))
    num2 = int(input("number 2:"))
  if data == 2: #add
    disp(num1 + num2)
  if data == 3: #subtract
    disp(num1 - num2)
  if data == 4: #divide
    disp(num1 * num2)
  if data == 5:
    if num2 == 0:
      disp("infinity")
    else:
      disp(num1 / num2)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("number 1 = ",num1," number 2 = ",num2)
  data = int(input("enter\n0 to exit\n1 to pick numbers\n2 to add\n3 to subtract\n4 to multiply\n5 to divide\n:"))
