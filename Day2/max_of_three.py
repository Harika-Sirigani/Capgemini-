import dis

def display(data):
    print(f"the max of three is {data}")
    
def get_input():
     a = int(input("enter a:"))
     b = int(input("enter b:"))
     c = int(input("enter c:"))
     
     return (a,b,c)
 
def max(a,b,c):
     if a>b and a>c:
         print("a is greater")
         return a
     elif b>c:
         print("b is greater")
         return b
     else:
         print("c is greater")
         return c
     
def main():
    a,b,c = get_input()
    result = max(a,b,c)
    #print(result)
    display(result)
    dis.dis(display)
    
main()
     