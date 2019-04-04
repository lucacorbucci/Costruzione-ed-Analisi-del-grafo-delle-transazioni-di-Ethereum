import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


def plotGraph():

    
    # Sulla X il tempo
    tempo =range(0,17)

    # Sulla y il DIR AverageDegree
    diametro = [3.795925670046663, 6.332842148899395, 6.842268984133245, 5.997016175048191, 119.29800457990845, 82.76542524399633, 50.66312310659986, 96.56285084381338, 36.42327760978471, 34.08527755429695, 6.6274345826518655, 6.722508392915147, 4.357685006871879, 4.366134130914215, 4.382190569541134, 15.701994751068161, 12.519729626475083]
    
    
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


   # plt.title('Distanza media nel grafo non orientato')
    plt.xlabel('Tempo')
    plt.ylabel('Distanza media')


    plt.show()


plotGraph()