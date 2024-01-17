#define the functions: add, sub, div, mul
#print options to the user
#ask for values
#call the functions
#while loop to continue the programe untill the user exit

def add(a, b):
    answer = a+b
    print(str(a)+" + "+str(b)+" = "+str(answer)+"\n")
    print("-------------------------------------------\n")

def sub(a, b):
    answer = a-b
    print(str(a)+" - "+str(b)+" = "+str(answer)+"\n")
    print("-------------------------------------------\n")

def mul(a, b):
    answer = a*b
    print(str(a)+" * "+str(b)+" = "+str(answer)+"\n")
    print("-------------------------------------------\n")

def div(a, b):
    answer = a/b
    print(str(a)+" / "+str(b)+" = "+str(answer)+"\n")
    print("-------------------------------------------\n")
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choise = input("Enter your choise: ")

    if choise == 'a' or choise == 'A':
        print("Addition")
        a = int(input("Input the fast number: "))
        b = int(input("Input the second number: "))
        add(a, b)

    elif choise == 'b' or choise == 'B':
        print("Subtraction")
        a = int(input("Input the fast number: "))
        b = int(input("Input the second number: "))
        sub(a, b)

    elif choise == 'c' or choise == 'C':
        print("Multiplication")
        a = int(input("Input the fast number: "))
        b = int(input("Input the second number: "))
        mul(a, b)

    elif choise == 'd' or choise == 'D':
        print("Division")
        a = int(input("Input the fast number: "))
        b = int(input("Input the second number: "))
        div(a, b)

    elif choise == 'e' or choise == 'E':
        print('Programe edded.')   
        quit()