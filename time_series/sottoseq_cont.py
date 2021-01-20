def contains(elem_grande, elem_piccolo):
    return set(elem_grande).issuperset(set(elem_piccolo))

def cercacontigui(mainSequence, subSequence, i):
    if (i + len(subSequence) > len(mainSequence)):
        return False
    for j in range(len(subSequence)):
        if (not contains(mainSequence[i+j], subSequence[j])):
            return False
    return True


def isSubsequence(mainSequence, subSequence):
    first_elem = subSequence[0]
    for i in range(len(mainSequence)):
        if (contains(mainSequence[i], first_elem)):
            if (cercacontigui(mainSequence, subSequence, i)):
                return True
    return False







subSequence = [["a"], ["b"], ["e"]]
mainSequence = [["a", "d"], ["a", "b", "c"], ["a", "c", "d"], ["c", "e"]]

print (isSubsequence(mainSequence, subSequence))