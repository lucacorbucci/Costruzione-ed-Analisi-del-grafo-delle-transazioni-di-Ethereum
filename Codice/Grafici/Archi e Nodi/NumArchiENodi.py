import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():

    
    # Sulla X il tempo
    tempo =range(0,17)

    # Sulla y il numero di archi
    archi = [12563, 19258, 25945, 39330, 91777, 147228, 265006, 400125, 505942, 613409, 738068, 857135, 1009025, 1483354, 2455703, 4656451, 7050485]
    
    # Sulla y il numero di nodi
    nodi = [14353, 22690, 30983, 47371, 112578, 166761, 283953, 413424, 506109, 613542, 705683, 819284, 944516, 1350779, 2228019, 4041198, 5950174]

    # Dimensione scritte 
    fig, ax = plt.subplots()
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(30)


    df = pd.DataFrame({'AsseX': tempo,
                   'Transazioni': archi,
                   'Account': nodi,
                   })
    
    df = df.melt('AsseX', var_name='Dati',  value_name='val')

    sns.set_context("notebook", font_scale=1.1)
    sns.set_style("ticks")
    sns.lineplot(x="AsseX", y="val", hue='Dati', data=df)


    #plt.title('Crescita del numero di nodi e di transazioni')
    plt.xlabel('Tempo')
    plt.ylabel('Transazioni o nodi')


    plt.show()


plotGraph()