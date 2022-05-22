import matplotlib.pyplot as plt
Partition = 'Holidays', 'Eating Out', 'Shopping', 'Grocery'
sizes = [250, 100, 300, 200]
figl, ax1 = plt.subplots()
ax1.pie(sizes, labels=Partition, autopct='%1.1f%%', shadow=True, startangle=90)
ax1. axis('equal')
plt.show()
