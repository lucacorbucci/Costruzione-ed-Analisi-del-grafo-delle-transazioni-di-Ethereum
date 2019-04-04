import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():

    
    # Sulla X il tempo
    tempo =range(0,17)

    # Sulla y il DIR AverageDegree
    diametro = [3.4342251950947604, 3.33174666137776, 3.2931151350827927, 3.4342251950947604, 3.20474735271125, 3.46554795218875, 3.675265211817247, 3.816321939727008, 3.9456075874333134, 3.9493424130158052, 4.131812338147393, 4.135880015382643, 4.225269395638841, 4.35209658514987, 4.373129859805974, 4.572481558497222, 4.695194123734869]
    
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


    #plt.title('Grado medio dei nodi del grafo non orientato')
    plt.xlabel('Tempo')
    plt.ylabel('Grado')


    plt.show()


plotGraph()