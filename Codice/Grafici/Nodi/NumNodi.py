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
    p = sns.lineplot(x=data['Tempo'], y=data['Numero di Nodi'], data=data,color='#009cff')
    p.tick_params(labelsize=10)
    for item in ([p.title, p.xaxis.label, p.yaxis.label] + p.get_xticklabels() + p.get_yticklabels()):
        item.set_fontsize(12)
    plt.setp(p.lines,linewidth=7)

def plotGraph():
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    fig = plt.figure(figsize=(15,8))
    plt.xlim(0, 17)
    plt.ylim(0, max(df['Numero di Nodi']))
    plt.xlabel('Tempo',fontsize=20)
    plt.ylabel('Numero di nodi',fontsize=20)
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=160, repeat=True)
    ani.save('Graph.mp4', writer=writer)
    plt.tight_layout()
    
    plt.show()


d1 = range(0,17)
d2 = [14353, 22690, 30983, 47371, 112578, 166761, 283953, 413424, 506109, 613542, 705683, 819284, 944516, 1350779, 2228019, 4041198, 5950174]


df = pd.DataFrame()
df['Tempo'] = d1
df['Numero di Nodi'] = d2


plotGraph()