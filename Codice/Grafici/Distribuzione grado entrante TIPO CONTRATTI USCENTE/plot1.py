import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph(outDegree, nodesNum):

    df = pd.DataFrame()

    df['x'] = outDegree
    df['y'] = nodesNum
    
    df.head()

    sns.set_style("ticks")
    
    fig, ax = plt.subplots(figsize=(11.7, 8.27))
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(27)



    g = sns.regplot('x', 'y', data=df, fit_reg=False, ax=ax)


    
    g.set_xscale('log')
    g.set_yscale('log')

    

    #plt.title('Distribuzione del grado entrante nel grafo con le transazioni verso contratti')
    plt.xlabel('Grado')
    plt.ylabel('Nodi')
    plt.xlim(1, 1000000)
    plt.ylim(1, 100000000)

    plt.show()

def extractData():
    with open("DIRIndegreeDistributionCONTRATTIUSCENTE.txt") as file:
        for line in file:
            array = line.strip("\n").split(" ")
            values = array[2:]
            

            outDegree = [float(item.split(":")[0]) for item in values[:-1]]
            nodesNum =  [float(item.split(":")[1]) for item in values[:-1]]
    return outDegree, nodesNum

outDegree, nodesNum = extractData()

plotGraph(outDegree, nodesNum)