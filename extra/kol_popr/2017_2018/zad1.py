def rek(t, i, steps, s1, s2, best):
    if i == len(t)-1:
        if s1 == s2:
            return True, s1, steps
        return False, 0, 0
    

    if s1 == s2:
        ans, val, ln = rek(t, i+1, steps,s2, t[i], best)
        if ans and ln > best:
            best = ln

    ans2, val2, ln2 = rek(t, i+1, steps+1, s1, s2+t[i], best)
    if ans2 and ln2 > best:
        best = ln2
    
    if ans or ans2:
        return True, s1, best
    
    return False, 0, 0


def runner(t):
    ans, s, ln = rek(t,0,0,)
    
