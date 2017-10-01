def ew(t):
    for i, x in enumerate(t):
        if (x[-1] == 's') or (x[-1] == 'e'):
            t[i] = t[i][:-1]
        for a in 'aeiou':
            if a in t[i]:
                print(t[i],len(a))
            elif a not in t[i]:
                print(t[i],1)

    return(t)


print(ew(['this','is','just','a','taest','pw']))

