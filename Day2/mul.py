import dis
def get_input():
    a = input()
    b = input()
    
    return a,b
    
def mul(a,b):
    val = int(a) * int(b)
    return val

def main():
    
    a,b = get_input()
    res = mul(a,b)
    print(res)
    dis.dis(mul)
    
main()
