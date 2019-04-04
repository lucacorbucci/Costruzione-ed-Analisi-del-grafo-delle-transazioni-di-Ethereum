

def extractData():
    with open("10mila.txt") as file:
        for line in file:
            array = line.strip("\n").split(",")
        
        count = 0
        for item in array:
            
            print(count,":",'%.08f' % float(item), sep="", end=' ')
            count += 1

extractData()

