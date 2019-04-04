import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():


    tipo = ["Utenti Esterni", "Contratti", "Creazione Contratti"]
    archi = [5847493, 1128344, 293751]
    
    fig, ax = plt.subplots()
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(25)

    df = pd.DataFrame({'Tipo': tipo,
                   'Diametro': archi,
                   })
    
    df = df.melt('Tipo', var_name='dati',  value_name='Transazioni')


    sns.catplot(x="Tipo", y="Transazioni", data=df,
                height=6, kind="bar", palette="muted", ax =ax)


   # plt.title('Numero di transazioni per tipo')
   # plt.xlabel('Tipo')
    #plt.ylabel('Transazioni')


    plt.show()


plotGraph()
