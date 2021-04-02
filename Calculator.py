#Calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

x = input("Input your first number\n")
y = input("Input your second number\n")
x = int(x)
y = int(y)
sign = input("Input your sign (add,sub,mult,div)\n")


if sign == "add":
    add_answer = add(x,y)
    print(add_answer)
if sign == "sub":
    sub_answer = sub(x,y)
    print(sub_answer)
if sign == "mult":
    mult_answer = mult(x,y)
    print(mult_answer)
if sign == "div":
    div_answer = div(x,y)
    print(div_answer)

