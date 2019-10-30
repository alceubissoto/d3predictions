import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
print(args)

df = pd.read_csv(args.file, delimiter=',', skiprows=4, header=None, names=['name', 'score'])

df = df.sort_values(['name']) # parameter ascending is applied to 'col1' and 'col2' respectively.

#df.to_csv('sorted_test.csv')
sorted_scores = df.values

name = args.file.split('.')[0] + '_processed.csv'
w = open(name, 'w')

#f = open('sorted_test.csv')
#f.readline()
x = np.arange(40)
count_y = -1

# prepare the labels dicts
label_isic = open('isic2018-part2-all.csv', 'r')
label_isic.readline()
isic_dict = {}
for line in label_isic:
    read_line = line.strip().split(';')
    isic_dict[read_line[0]] = read_line[1]

w.write('name,score,x,y,label\n')
for idx, item in enumerate(sorted_scores):
    if idx%40 == 0:
        count_y += 1
    w.write(item[0] + ',' + str(item[1]) + ',' + str(x[idx%40]) + ',' + str(count_y) + ',' + str(isic_dict[item[0]]) + '\n')
