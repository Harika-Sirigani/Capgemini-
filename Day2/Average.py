def display(val):
    print(f"the average of 4 numbers is {val}")
    
def get_input():
    num1 = input("n1=")
    num2 = input("n2=")
    num3 = input("n3=")
    num4 = input("n4=")
    n = input("enter n:")
   
    
    return (num1,num2,num3,num4,n)

def add(n1,n2,n3,n4):
    value = (int(n1) + int(n2) + int(n3) + int(n4))
    
    return (value)

def average(n1,n2,n3,n4,n):
    div = add(n1,n2,n3,n4)
    val = int(div)/int(n)
    return (val)
    

def main():
    (n1,n2,n3,n4,n) = get_input()
    #value  = add(n1,n2,n3,n4)
    val = average(n1,n2,n3,n4,n)
    display(val)
    
main()
    
    
    