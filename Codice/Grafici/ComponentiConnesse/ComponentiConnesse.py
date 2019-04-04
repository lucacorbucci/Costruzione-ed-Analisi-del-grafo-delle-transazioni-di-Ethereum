import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():

    
    # Sulla X il tempo
    tempo =range(0,17)

    # Sulla y il DIR AverageDegree
    CCSize = [14102, 22395, 30606, 46886, 111807, 165749, 283082, 413035, 505704, 613111, 703352, 812204, 930294, 1333993, 2210947, 4024190, 5933068]
    nodi = [14352, 22689, 30981, 47369, 112568, 166739, 283924, 413419, 506100, 613531, 705503, 819105, 944336, 1350601, 2227841, 4041021, 5950174]
    divided = []

    

    for i in range(0, len(CCSize)):
        divided.append(float(CCSize[i])/nodi[i])


    fig, ax = plt.subplots()
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(30)


    df = pd.DataFrame({'AsseX': tempo,
                   'CCSize': divided,
                   })
    
    df = df.melt('AsseX', var_name='dati',  value_name='val')

    sns.set_context("notebook", font_scale=1.1)
    sns.set_style("ticks")
    g = sns.lineplot(x="AsseX", y="val", data=df)


    #plt.title('Grado medio dei nodi del grafo non orientato')
    plt.xlabel('Tempo')
    plt.ylabel("Frazione di nodi nella CC piu' grande")

   
    plt.show()


plotGraph()