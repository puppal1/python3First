blkChain = [1,5,6,"abc", [1,2,"prashant" , ["uppal"]]]
blkChain
blkChain[1]
print((blkChain[4][2])[6])

print(blkChain)
blkChain.count(blkChain)
print(blkChain.count(blkChain))

blkChain.pop()
print(blkChain)
blkChain.remove(blkChain[1])
print(blkChain)

def func1 () :
    print ("ola ")

func1()

def holds (func, arg) :
    pass

def wierd (func) :
    if holds(func, func):
        print(" in holds")
        while True :
            print ("non Halting")
            pass

    else :
        print(" halting")
        return

wierdstr = """def wierd (func) :
    if holds(func, func):
        print(" in holds")
        while True :
            print ("non Halting")
            pass

    else :
        print(" halting")
        return"""
wierd(wierdstr)