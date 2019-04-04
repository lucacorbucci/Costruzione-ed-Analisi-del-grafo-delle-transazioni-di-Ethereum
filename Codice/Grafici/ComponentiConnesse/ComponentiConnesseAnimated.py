import pandas as pd
import random
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
import numpy as np
np.set_printoptions(threshold='nan')


def animate(i):
    data = df.iloc[:int(i+1)] #select data range
    p = sns.lineplot(x=data['Tempo'], y=data['Dimensione Componente Connessa'], data=data,color='#009cff')
    p.tick_params(labelsize=10)
    for item in ([p.title, p.xaxis.label, p.yaxis.label] + p.get_xticklabels() + p.get_yticklabels()):
        item.set_fontsize(12)
    plt.setp(p.lines,linewidth=7)

def plotGraph():
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    fig = plt.figure(figsize=(15,8))
    plt.xlim(0, 17)
    plt.ylim(0.98, max(df['Dimensione Componente Connessa'])+0.001)
    plt.xlabel('Tempo',fontsize=20)
    plt.ylabel('Percentuale di nodi nella componente connessa',fontsize=20)
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=160, repeat=True)
    ani.save('Graph.mp4', writer=writer)
    plt.tight_layout()
    
    plt.show()


tempo = range(0,17)
    # Sulla y il DIR AverageDegree
CCSize = [14102, 22395, 30606, 46886, 111807, 165749, 283082, 413035, 505704, 613111, 703352, 812204, 930294, 1333993, 2210947, 4024190, 5933068]
nodi = [14352, 22689, 30981, 47369, 112568, 166739, 283924, 413419, 506100, 613531, 705503, 819105, 944336, 1350601, 2227841, 4041021, 5950174]
divided = []

    

for i in range(0, len(CCSize)):
    divided.append(float(CCSize[i])/nodi[i])

df = pd.DataFrame({'Tempo': tempo,
                   'Dimensione Componente Connessa': divided,
                   })

plotGraph()