import os, shutil, random
random.seed(0)
import numpy as np
from sklearn.model_selection import train_test_split

val_size = 0.1
test_size = 0.1
postfix = 'jpg'
imgpath = 'C:/Users/Lenovo/Desktop/data1/images'
txtpath = 'C:/Users/Lenovo/Desktop/data1/labels'

os.makedirs('C:/Users/Lenovo/Desktop/data1/images/train', exist_ok=True)
os.makedirs('C:/Users/Lenovo/Desktop/data1/images/val', exist_ok=True)
os.makedirs('C:/Users/Lenovo/Desktop/data1/images/test', exist_ok=True)
os.makedirs('C:/Users/Lenovo/Desktop/data1/labels/train', exist_ok=True)
os.makedirs('C:/Users/Lenovo/Desktop/data1/labels/val', exist_ok=True)
os.makedirs('C:/Users/Lenovo/Desktop/data1/labels/test', exist_ok=True)

listdir = np.array([i for i in os.listdir(txtpath) if 'txt' in i])
random.shuffle(listdir)
train, val, test = listdir[:int(len(listdir) * (1 - val_size - test_size))], listdir[int(len(listdir) * (1 - val_size - test_size)):int(len(listdir) * (1 - test_size))], listdir[int(len(listdir) * (1 - test_size)):]
print(f'train set size:{len(train)} val set size:{len(val)} test set size:{len(test)}')

for i in train:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'C:/Users/Lenovo/Desktop/data1/images/train/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'C:/Users/Lenovo/Desktop/data1/labels/train/{}'.format(i))

for i in val:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'C:/Users/Lenovo/Desktop/data1/images/val/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'C:/Users/Lenovo/Desktop/data1/labels/val/{}'.format(i))

for i in test:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'C:/Users/Lenovo/Desktop/data1/images/test/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'C:/Users/Lenovo/Desktop/data1/labels/test/{}'.format(i))