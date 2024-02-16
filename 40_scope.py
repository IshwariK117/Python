# variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.
def myfunc():
  x = 300
  print(x)

myfunc()



x = 50
def myfunc():
  print(x)

myfunc()

print(x)


def myfunc():
  global x       #global keyword
  x = 300

myfunc()

print(x)