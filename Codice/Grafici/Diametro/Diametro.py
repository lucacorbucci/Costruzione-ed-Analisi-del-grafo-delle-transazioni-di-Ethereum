import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():

    
    # Sulla X il tempo
    tempo =range(0,17)

    # Sulla y il diametro del grafo
    diametro = [16, 39, 51, 51, 8268, 8268, 5003, 8267, 8267, 8267, 8267, 8267, 8267, 8267, 8267, 8267, 8267]
    
    fig, ax = plt.subplots()
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(30)


    df = pd.DataFrame({'AsseX': tempo,
                   'Diametro': diametro,
                   })
    
    df = df.melt('AsseX', var_name='dati',  value_name='val')

    sns.set_context("notebook", font_scale=1.1)
    sns.set_style("ticks")
    sns.lineplot(x="AsseX", y="val", data=df)


    #plt.title('Diametro del grafo non orientato')
    plt.xlabel('Tempo')
    plt.ylabel('Diametro')


    plt.show()


plotGraph()