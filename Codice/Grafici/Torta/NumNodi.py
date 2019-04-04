import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Transazioni verso utenti esterni', 'Transazioni verso contratti', 'Creazione di contratti'
sizes = [5857493, 1128344, 293751]
plt.rcParams['font.size'] = 30.0
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
         startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()