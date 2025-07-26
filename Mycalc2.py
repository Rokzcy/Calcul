def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

print( ('*'* 23) + "  Welcome to the home of all calculations" + ('*' * 23))
print(('*' * 23) +' what  can i help you with? ' + ('*' * 23))

A = ' A = Additon'
S = ' S = Subtraction'
M = ' M = Multiplication'
D = ' D = Division'
m = ' m = modulus'
P = ' P = Power'
dict1 = ['A','S','M','D','m','P']

print(A.rjust(16,'-'))
print(( '*' * 4 + S ))
print(( '*' * 4 + M))
print(( '*' * 4 + P ))
print(( '*' * 4 + m))
print(D.rjust(17,'-'))

operation = input('Enter your choice : ')
if operation in dict1:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if operation == 'A': print("Result:", add(num1, num2))
        elif operation == 'S':print("Result:", subtract(num1, num2))
        elif operation == 'M': print("Result:", multiply(num1, num2))
        elif operation == 'D': print("Result:", divide(num1, num2))
        elif operation == 'm': print("Result:", modulus(num1, num2))
        elif operation == 'p': print("Result:", power(num1, num2))
    except ValueError:
        print('<UNK> Invalid Choice')

else:
    print('❌ Invalid Mode of Operation ')