from fastdtw import fastdtw
import matplotlib.pyplot as plt
#グラフを横長固定
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 10,6

#データ作成
from numpy.random import *

seed(100)
rand()

a = list(randint(0, 20, 30))
#bはaを少しだけずらしたデータ
b = [0, 1, 10, 4] + a

plt.plot(a, label="a")
plt.plot(b, label="b")
plt.legend()
plt.show()

distance, path =fastdtw(a, b)
print(distance)
print(path)

for a_x, b_x in path:
  plt.plot([a_x, b_x], [a[a_x], b[b_x]], color='gray', linestyle='dotted', linewidth=1)
  
plt.plot(a, label="a")
plt.plot(b, label="b")
plt.legend()
plt.show()