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
    p = sns.lineplot(x=data['Tempo'], y=data['Distanza Media'], data=data,color='#009cff')
    p.tick_params(labelsize=10)
    for item in ([p.title, p.xaxis.label, p.yaxis.label] + p.get_xticklabels() + p.get_yticklabels()):
        item.set_fontsize(12)
    plt.setp(p.lines,linewidth=7)

def plotGraph():
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    fig = plt.figure(figsize=(15,8))
    plt.xlim(0, 17)
    plt.ylim(-10, max(df['Distanza Media'])+10)
    plt.xlabel('Tempo',fontsize=20)
    plt.ylabel('Distanza Media',fontsize=20)
    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=160, repeat=True)
    ani.save('Graph.mp4', writer=writer)
    plt.tight_layout()
    
    plt.show()


    
    # Sulla X il tempo
tempo =range(0,17)

    # Sulla y il DIR AverageDegree
diametro = [3.795925670046663, 6.332842148899395, 6.842268984133245, 5.997016175048191, 119.29800457990845, 82.76542524399633, 50.66312310659986, 96.56285084381338, 36.42327760978471, 34.08527755429695, 6.6274345826518655, 6.722508392915147, 4.357685006871879, 4.366134130914215, 4.382190569541134, 15.701994751068161, 12.519729626475083]
  
df = pd.DataFrame({'Tempo': tempo,
                   'Distanza Media': diametro,
                   })  
plotGraph()