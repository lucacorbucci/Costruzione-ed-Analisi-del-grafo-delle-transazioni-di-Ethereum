import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():


    tipo = ["Utenti Esterni", "Contratti", "Creazione Contratti"]
    Nodi = [5417764, 1616056, 614010]
    
    fig, ax = plt.subplots()
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(27)

    df = pd.DataFrame({'Tipo': tipo,
                   'Diametro': Nodi,
                   })
    
    df = df.melt('Tipo', var_name='dati',  value_name='Nodi')


    sns.catplot(x="Tipo", y="Nodi", data=df,
                height=6, kind="bar", palette="muted", ax=ax)


   # plt.title('Numero di nodi per tipo')
    #plt.xlabel('Tipo')
    #plt.ylabel('Nodi')


    plt.show()


plotGraph()
