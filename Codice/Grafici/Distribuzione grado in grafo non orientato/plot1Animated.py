import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
import matplotlib

def animate(i):
    data = df.iloc[:int(i+1)] #select data range
    p = sns.regplot('x', 'y', data=df, fit_reg=False)
    p.tick_params(labelsize=10)
    p.set_xscale('log')
    p.set_yscale('log')
    for item in ([p.title, p.xaxis.label, p.yaxis.label] + p.get_xticklabels() + p.get_yticklabels()):
        item.set_fontsize(12)
    plt.setp(p.lines,linewidth=7)

def plotGraph(outDegree, nodesNum):


    sns.set_style("ticks")
    
    fig, ax = plt.subplots(figsize=(11.7, 8.27))
    
    
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(32)
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)

    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=10, repeat=True)
    ani.save('Graph.mp4', writer=writer)

  

    

    #plt.title('Distribuzione del grado nel grafo non orientato')
    plt.xlabel('Grado')
    plt.ylabel('Nodi')
    plt.xlim(1, 1000000)
    plt.ylim(1, 100000000)

    plt.show()

def extractData():
    with open("UndirDegreeDistribuition.txt") as file:
        for line in file:
            array = line.strip("\n").split(" ")
            values = array[2:]
            

            outDegree = [float(item.split(":")[0]) for item in values[:-1]]
            nodesNum =  [float(item.split(":")[1]) for item in values[:-1]]
    return outDegree, nodesNum

outDegree, nodesNum = extractData()

df = pd.DataFrame()

df['x'] = outDegree
df['y'] = nodesNum
    
    
plotGraph(outDegree, nodesNum)