def loadDict():
    with open("Associazioni.txt") as file:
        for line in file:
            array = line.strip("\n").split(" ")
            associazioni[int(array[1])] = array[0]
        

def loadTop():
    top = []
    with open("TopVertici.txt") as file:
        for line in file:
           array = line.strip("\n").split(" ")
           values = [item.split(":") for item in array[2:]]
           top.append(values)
        return top

def translate(top, associazioni):
    result = []
    for item in top:
        array = []
        for x in item:
            ar = []
            ar.append(associazioni[int(x[0])])
            ar.append(x[1])
            array.append(ar)
        result.append(array)
    return result

associazioni = {}
loadDict()
top = loadTop()

result = translate(top, associazioni)

for item in result:
    item.sort(key=lambda tup: (int(tup[1])))
    item.reverse()
    for x in item:
        print x[0], x[1]
    print "-----------------"