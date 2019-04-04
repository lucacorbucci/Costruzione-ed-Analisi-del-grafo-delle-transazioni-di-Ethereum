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
    p = sns.lineplot(x=data['Tempo'], y=data['Diametro'], data=data,color='#009cff')
    p.tick_params(labelsize=10)
    for item in ([p.title, p.xaxis.label, p.yaxis.label] + p.get_xticklabels() + p.get_yticklabels()):
        item.set_fontsize(12)
    plt.setp(p.lines,linewidth=7)

def plotGraph():
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    fig = plt.figure(figsize=(15,8))
    plt.xlim(0, 17)
    plt.ylim(-100, max(df['Diametro'])+200)
    plt.xlabel('Tempo',fontsize=20)
    plt.ylabel('Diametro',fontsize=20)
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=160, repeat=True)
    ani.save('Graph.mp4', writer=writer)
    plt.tight_layout()
    
    plt.show()


# Sulla X il tempo
tempo =range(0,17)

# Sulla y il diametro del grafo
diametro = [16, 39, 51, 51, 8268, 8268, 5003, 8267, 8267, 8267, 8267, 8267, 8267, 8267, 8267, 8267, 8267]
df = pd.DataFrame({'Tempo': tempo,
                   'Diametro': diametro,
                   })
plotGraph()