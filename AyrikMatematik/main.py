

kume1 = (0,1,2,3,4)

R =[]
for i in kume1:
    for j in kume1:
        R.append((i,j))

print(R)

def isReflexive(kume):
    for i in kume:
        if((i[0],i[0]) not in kume):
            return False
    return True

def isIrreflexive(kume):
    for i in kume:
        if((i[0],i[0]) in kume):
            return False
    return True

def isSymmetry(kume):
    for i in kume:
        if((i[1],i[0]) not in kume):
            return False
    return True

def isAntiSymmetry(kume):
    for i in kume:
        if (i[0] == i[1]):
            continue
        if((i[1],i[0]) in kume):
            return False
    return True

def isTransitive(kume):
    for i in kume:
        for j in kume:
            if(i[1]==j[0]):
                if((i[0],j[1]) not in kume):
                    return False
    return True


def isEquivalenceRelation(kume):
    R=isReflexive(kume)
    S=isSymmetry(kume)
    T=isTransitive(kume)
    return all([R,S,T])


print(isEquivalenceRelation(R))