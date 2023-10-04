#BAR CHART
import matplotlib.pyplot as plt

categories=['xy','ab','cd']
values=[20,30,40]
plt.bar(categories,values)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar chart')
plt.show()


#PIE CHART
import matplotlib.pyplot as plt

categories=['s','r','u','s','h','t','i']
values=[10,15,20,25,30,35,40]
plt.pie(values)
plt.title('pie chart')
plt.show()

#SCATTER
import matplotlib.pyplot as plt

categories=['xy','ab','cd']
values=[40,10,30]
plt.scatter(categories,values)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('scatter plot')
plt.show()