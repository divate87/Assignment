import sys
import ast


def evalPostfix(text):
    s = []
    for symbol in text:
        try:
            result = int(symbol)
        except ValueError:
            if symbol not in '+-*/':
                raise ValueError('text must contain only numbers and operators')
            operand2=s.pop()
            operand1=s.pop()   
            result = doMath(symbol,operand1,operand2)
        s.append(result)
    return s.pop() 

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def main():
    inputFP=open(sys.argv[1],"r+")
    outputFP=open(sys.argv[2],"r+")
    for line in inputFP:
        
        if len(line)>2: 
         myList=ast.literal_eval(line)
         result=evalPostfix(myList)       
         outputFP.write("%s ==> %d\n" %(myList,result))
   
    inputFP.close()
    outputFP.close()         

if __name__=="__main__":
    main()



