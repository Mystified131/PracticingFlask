def proclist(instr):
    instr = instr.lower()
    instrb = ""
    for elem in instr:
        if elem.isalpha() or elem == " ":
            instrb += elem
    anslist = []
    anslist = instrb.split()
    anslistb = list(set(anslist))
    anslistb.sort()
    return anslistb

    ## THE GHOST OF THE SHADOW ##