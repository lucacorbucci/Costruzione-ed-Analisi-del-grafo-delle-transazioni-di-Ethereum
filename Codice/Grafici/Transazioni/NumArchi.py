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
    p = sns.lineplot(x=data['Tempo'], y=data['Numero di transazioni'], data=data,color='#009cff')
    p.tick_params(labelsize=10)
    for item in ([p.title, p.xaxis.label, p.yaxis.label] + p.get_xticklabels() + p.get_yticklabels()):
        item.set_fontsize(12)
    plt.setp(p.lines,linewidth=7)

def plotGraph():
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    fig = plt.figure(figsize=(15,8))
    plt.xlim(0, 17)
    plt.ylim(-100000, max(df['Numero di transazioni'])+100000)
    plt.xlabel('Tempo',fontsize=20)
    plt.ylabel('Numero di transazioni',fontsize=20)
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=160, repeat=True)
    ani.save('Graph.mp4', writer=writer)
    plt.tight_layout()
    
    plt.show()




df = pd.DataFrame()
df['Tempo'] =range(0,17)
df['Numero di transazioni'] = [12563, 19258, 25945, 39330, 91777, 147228, 265006, 400125, 505942, 613409, 738068, 857135, 1009025, 1483354, 2455703, 4656451, 7050485]

plotGraph()