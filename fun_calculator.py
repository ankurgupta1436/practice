def calculator(operation,a,b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a-b
    elif operation == "multiply":
        return a*b
    elif operation == "devide":
        if b != 0:
            return a/b
        else:
            return "Error : Division by zero"
    else:
        return "Error : Invalid operation"
def main():
    print(calculator("add",5,3))         
    print(calculator("subtract",10,4))    
    print(calculator("multiply",2,3))     
    print(calculator("devide",8,2))      
    print(calculator("devide",5,0))       
    print(calculator("modulus",5,2))      