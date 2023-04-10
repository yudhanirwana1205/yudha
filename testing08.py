def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function("indonesia")
my_function("Brazil")

#kedua
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def multiply_by_two():
    return a * 2

assert(multiply_by_two(3)) == 0

def multply_by_x():
   "if x not passed, than define the default value to 2"
    return a * x

assert(multiply_by_x(3)) == 6
assert(multiply_by_x(3, 1)) == 3

   user_inout = input ('input dikali dengan 2')
    print(multply_by_x(int(user_input)))