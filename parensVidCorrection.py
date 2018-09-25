def balanceParens(s):
    parenTrack=[]
    openType = ['(','{','[']
    closeType = [')','}',']']

    for ch in range(0,len(s)):
        if s[ch] in openType:
            parenTrack.append(s[ch])
        else:
            if len(parenTrack) > 0:
                if s[ch] == ')':
                    if parenTrack.pop()!='(':
                        return False
                if s[ch] == '}':  
                    if parenTrack.pop()!='{':
                        return False              
                if s[ch] == ']':
                    if parenTrack.pop()!='[':
                        return False
            else:
                return False
    if len(parenTrack) == 0:
        return True
    else:
        return False

print(balanceParens('(()[]{}()'))