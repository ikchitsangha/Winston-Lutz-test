#flexmap
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as nm

y,x =nm.loadtxt('dx.txt', delimiter=',',unpack=True) #loadtext filename delimter unpack true
plt.plot(x,y)
plt.xlabel('Gantry Angle')
plt.ylabel('displacement U')
plt.title('Flex Map U')
plt.show()

y,x =nm.loadtxt('dy.txt', delimiter=',',unpack=True) #loadtext filename delimter unpack true
plt1.plot(x,y)
plt1.xlabel('Gantry Angle')
plt1.ylabel('displacement V')
plt1.title('Flex Map v')
plt1.show()



data1=open('dx.txt',mode='w')
#data1.write(" ")
data1.close()
data1=open('dy.txt',mode='w')
#data1.write(" ")
data1.close()

