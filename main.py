import numpy as np
from csv import reader


with open('mnist.csv', 'rt') as data:
    r = reader(data, delimiter=',')
    data_set = list(r)
    data_set = np.array(data_set).astype('float')




# data = pd.read_csv("./mnist.csv")

# label = data.iloc[:,0]
# image = data.iloc[:,1:]

label = data_set[:,0]
image = data_set[:,1:]

# print('%.11f'%image[1,1])

image_ave = np.mean(image,axis = 0)

i = 0
j = 0

Xc = image 

for i in range(len(image)):
    for j in range(len(image[0])):
        Xc[i][j] = image[i][j] - image_ave[j]

Cx = np.cov(Xc)

eig = np.linalg.eig(Cx)

va = eig[0]

rank_data = np.sort(va)
P={}

n = len(rank_data)
i=0;
for i in range(10):
    P[i] = rank_data[n-i-1]

re = P * Xc 



# with open("result.txt","w") as f:
#     for i in range(len(P)):
#         print(i)
#         print (P[i],file=f)
# f.close()


