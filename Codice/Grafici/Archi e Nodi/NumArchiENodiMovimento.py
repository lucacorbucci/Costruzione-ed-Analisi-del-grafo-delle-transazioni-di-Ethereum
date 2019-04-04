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
    global multi
    global j
    if i == 159 or multi:
        print j, "ciao"
        multi = True
        data = df.iloc[:int(j+1)]
        j += 1
        ax2 = sns.lineplot(x=data['Tempo'], y=data['Transazioni'], legend=False, color='#d90d21')
        p =sns.lineplot(x=data['Tempo'], y=data['Account'], ax=ax2, data=data, color='#009cff')
    else:
        print "ciuao"
        p = sns.lineplot(x=data['Tempo'], y=data['Account'], data=data, color='#009cff')

    p.tick_params(labelsize=10)
    for item in ([p.title, p.xaxis.label, p.yaxis.label] + p.get_xticklabels() + p.get_yticklabels()):
        item.set_fontsize(12)
    plt.setp(p.lines,linewidth=7)

def plotGraph():
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    fig = plt.figure(figsize=(15,8))
    plt.xlim(0, 17)
    plt.ylim(0, max(df['Transazioni']))
    plt.xlabel('Tempo',fontsize=20)
    plt.ylabel('Numero di nodi',fontsize=20)
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=320, repeat=True)
    
    ani.save('Graph.mp4', writer=writer)
    plt.tight_layout()
    
    plt.show()


tempo =range(0,17)

    # Sulla y il numero di archi
archi = [12563, 19258, 25945, 39330, 91777, 147228, 265006, 400125, 505942, 613409, 738068, 857135, 1009025, 1483354, 2455703, 4656451, 7050485]
    
    # Sulla z il numero di nodi
nodi = [14353, 22690, 30983, 47371, 112578, 166761, 283953, 413424, 506109, 613542, 705683, 819284, 944516, 1350779, 2228019, 4041198, 5950174]



df = pd.DataFrame({'Tempo': tempo,
                   'Transazioni': archi,
                   'Account': nodi,
                   })
    

j = 0
multi = False
plotGraph()