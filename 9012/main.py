for T in range(int(input())):
    str = list(input())
    for i in range(len(str)):
        if str[0] == ')':
            print("NO")
            break
        
        if str[0] == '(':
            if ')' not in str:
                print("NO")
                break
            if ')' in str :
                str.remove('(')
                str.remove(')')
        if len(str) == 0 :
            print("YES")
            break
    #print("NO")