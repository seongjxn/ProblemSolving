import sys ; input = sys.stdin.readline

results = []

while True :
    string = input().rstrip()
    
    if string == '.' :
        break
    
    brackets = []
    error = 0
    
    for i in string :
        if   i == '.' :
            if brackets: error += 1
            break
        
        elif i == '(' : brackets.append(i)
        elif i == '[' : brackets.append(i)
        
        elif i == ')' : 
            if not brackets :
                error += 1
                continue
            
            if brackets.pop() != '(' :
                error += 1
                
        elif i == ']' :
            if not brackets :
                error += 1
                continue
            
            if brackets.pop() != '[' :
                error += 1
        
    
    if error: results.append('no')
    else : results.append('yes')    
    
    
for result in results:
    print(result)