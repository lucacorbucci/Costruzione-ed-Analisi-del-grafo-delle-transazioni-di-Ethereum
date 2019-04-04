import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():


    tipo = ["Utenti Esterni", "Contratti", "Creazione Contratti"]
    archi = [4.26693336955984, 2.792833911696129, 1.9136593866549405]


    df = pd.DataFrame({'AsseX': tipo,
                   'Diametro': archi,
                   })
    
    df = df.melt('AsseX', var_name='dati',  value_name='val')


    sns.catplot(x="AsseX", y="val", data=df,
                height=6, kind="bar", palette="muted")


    plt.title('Grado medio dei nodi nel grafo non orientato')
    plt.xlabel('Tipo')
    plt.ylabel('Grado')


    plt.show()


plotGraph()
