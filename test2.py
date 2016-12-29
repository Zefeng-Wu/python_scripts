from matplotlib import pyplot as plt
import numpy  as np


   
t = np.arange(0.0,10.0,1)
#y1 = [-0.01,1,-0.5,1,-1,1,-1,-1,-1,1]
y1 = [0.01,-0.01,0.01,0.01,-0.01,0.01,0.01,-0.01,0.01,0.01]
y2 = [-1,1,1,-1,1,-1,-1,-1,-1,-1]


plt.figure(figsize=(8,7),dpi=90)
plt.subplots_adjust(bottom=0.53)
p1 = plt.subplot(211)
p2 = plt.subplot(212)

p1.axis([0.0,10.01,-0.04,0.04])
p1.axis('off')

label_f1 = "plot1_label"
label_f2 = "plot2_label"

p1.hlines(y=0,xmin=0,xmax = 10)
p1.plot(t,y1,'|',ms = 20)
p1.text(-1, 0,"chr1")
#p1.plot(t,y1,"g-",label=label_f1)
p2.plot(t,y1,'|',ms = 20)

plt.show()




