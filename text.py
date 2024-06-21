from multiprocessing.spawn import old_main_modules
import numpy as np
from csv import reader
import random


with open('mnist.csv', 'rt') as data:
    r = reader(data, delimiter=',')
    data_set = list(r)
    data_set = np.array(data_set).astype('float')

# data = pd.read_csv("./mnist.csv")

# label = data.iloc[:,0]
# image = data.iloc[:,1:]

label = data_set[:,0]
image = data_set[:,1:]

x = random.randint(0,5999)
y = random.randint(0,783)

old_center0 = image[x][y]
x_1 = random.randint(0,5999)
y_1 = random.randint(0,783)
old_center1 = image[x_1][y_1]
x_2 = random.randint(0,5999)
y_2 = random.randint(0,783)
old_center2 = image[x_2][y_2]
x_3 = random.randint(0,5999)
y_3 = random.randint(0,783)
old_center3 = image[x_3][y_3]
x_4 = random.randint(0,5999)
y_4 = random.randint(0,783)
old_center4 = image[x_4][y_4]
x_5 = random.randint(0,5999)
y_5 = random.randint(0,783)
old_center5 = image[x_5][y_5]
x_6 = random.randint(0,5999)
y_6 = random.randint(0,783)
old_center6 = image[x_6][y_6]
x_7 = random.randint(0,5999)
y_7 = random.randint(0,783)
old_center7 = image[x_7][y_7]
x_8 = random.randint(0,5999)
y_8 = random.randint(0,783)
old_center8 = image[x_8][y_8]
x_9 = random.randint(0,5999)
y_9 = random.randint(0,783)
old_center9 = image[x_9][y_9]

class_0 = {}
class_1 = {}
class_2 = {}
class_3 = {}
class_4 = {}
class_5 = {}
class_6 = {}
class_7 = {}
class_8 = {}
class_9 = {}

change_0 = 0
change_1 = 0
change_2 = 0
change_3 = 0
change_4 = 0
change_5 = 0
change_6 = 0
change_7 = 0
change_8 = 0
change_9 = 0

t = 0
for t in range(1000):
    i=0
    j=0
    for i in range(5999):
        for j in range(783):
            arrI = image[i][j]
            
            arrC_0 = old_center0
            vec1 = np.array(arrI)
            vec2 = np.array(arrC_0)
            dis_0 = np.lianlg.norm(vec1 - vec2)
            
            arrC_1 = old_center1
            vec2 = np.array(arrC_1)
            dis_1 = np.linalg.norm(vec1 - vec2)
            
            arrC_2 = old_center2
            vec2 = np.array(arrC_2)
            dis_2 = np.linalg.norm(vec1 - vec2)
            
            arrC_3 = old_center3
            vec2 = np.array(arrC_3)
            dis_3 = np.linalg.norm(vec1 - vec2)
            
            arrC_4 = old_center4
            vec2 = np.array(arrC_4)
            dis_4 = np.linalg.norm(vec1 - vec2)
            
            arrC_5 = old_center5
            vec2 = np.array(arrC_5)
            dis_5 = np.linalg.norm(vec1 - vec2)
            
            arrC_6 = old_center6
            vec2 = np.array(arrC_6)
            dis_6 = np.linalg.norm(vec1 - vec2)
            
            arrC_7 = old_center7
            vec2 = np.array(arrC_7)
            dis_7 = np.linalg.norm(vec1 - vec2)
            
            arrC_8 = old_center8
            vec2 = np.array(arrC_8)
            dis_8 = np.linalg.norm(vec1 - vec2)
            
            arrC_9 = old_center9
            vec2 = np.array(arrC_9)
            dis_9 = np.linalg.norm(vec1 - vec2)
                
            
