from matplotlib import pyplot as plt
import numpy as np

a=[1,2,5,6,9,11,15,17,18]
b=[1,2,3,4,5,6,7,8,9,14,13,15]

#set the range of x and y
plt.xlim(0,21)     
plt.ylim(0.5,1.5)

#draw a Horizontal line
plt.hlines(y=1,xmin=1,xmax=20)
y1 = np.ones(np.shape(a)) #set y as 1  
plt.plot(a,y1,'|',ms = 40) 


#adding a Horizontal line
plt.hlines(y=1+0.2,xmin=1,xmax=20) 
y2=np.ones(np.shape(b))  #set y as 1
plt.plot(b,y2+0.2,'|',ms = 40)
plt.text(-1, 1,"chr1")

plt.axis('off')

plt.show()