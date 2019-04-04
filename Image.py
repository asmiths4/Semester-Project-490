import numpy as np
import re
import matplotlib.pyplot as plt


#format of .csv file data to show how the x and y coordinates interact
#[[[200, 150, 116, 83, 73, 69, 67, 83, 104, 119, 175, 193, 208, 226, 228, 225, 210, 166], [97, 86, 88, 110, 123, 138, 183, 203, 218, 222, 224, 213, 192, 138, 120, 114, 106, 101]],
# [[53, 21], [159, 152]],
# [[11, 0], [151, 149]],
# [[190, 190], [148, 148]],
# [[189, 188, 179], [92, 140, 229]],
# [[143, 144, 135, 128], [105, 118, 158, 216]],
# [[147, 118, 107], [96, 182, 232]],
# [[95, 78, 73], [94, 157, 230]],
# [[179, 179, 148, 144, 142], [112, 118, 189, 204, 231]],
# [[120, 107, 90], [92, 134, 226]],
# [[213, 213], [139, 139]],
# [[207, 202, 203], [139, 146, 155]],
# [[75, 83, 99, 113, 147, 168, 175, 180, 180, 162, 134], [106, 55, 12, 1, 0, 9, 16, 25, 37, 71, 107]],
# [[163, 169, 181, 207, 236, 253, 253, 232, 201], [95, 67, 40, 25, 22, 39, 62, 87, 106]]]


#sample lists to test with. copy and pasted from bee.csv
#s = "[[[200, 150, 116, 83, 73, 69, 67, 83, 104, 119, 175, 193, 208, 226, 228, 225, 210, 166], [97, 86, 88, 110, 123, 138, 183, 203, 218, 222, 224, 213, 192, 138, 120, 114, 106, 101]], [[53, 21], [159, 152]], [[11, 0], [151, 149]], [[190, 190], [148, 148]], [[189, 188, 179], [92, 140, 229]], [[143, 144, 135, 128], [105, 118, 158, 216]], [[147, 118, 107], [96, 182, 232]], [[95, 78, 73], [94, 157, 230]], [[179, 179, 148, 144, 142], [112, 118, 189, 204, 231]], [[120, 107, 90], [92, 134, 226]], [[213, 213], [139, 139]], [[207, 202, 203], [139, 146, 155]], [[75, 83, 99, 113, 147, 168, 175, 180, 180, 162, 134], [106, 55, 12, 1, 0, 9, 16, 25, 37, 71, 107]], [[163, 169, 181, 207, 236, 253, 253, 232, 201], [95, 67, 40, 25, 22, 39, 62, 87, 106]]]"
#s = "[[[125, 82, 50, 17, 3, 1, 15, 36, 62, 122, 174, 214, 241, 253, 255, 253, 244, 232, 209, 178, 156, 161], [55, 60, 74, 96, 117, 140, 166, 183, 195, 203, 200, 188, 170, 147, 134, 119, 100, 87, 72, 65, 64, 66]], [[130, 149, 177, 204, 224, 235, 231, 213, 177], [72, 46, 25, 14, 12, 18, 29, 51, 80]], [[116, 104, 93, 90, 94, 117, 136, 147, 157], [77, 61, 36, 15, 4, 0, 7, 19, 41]], [[83, 82], [197, 216]], [[138, 137], [189, 209]], [[176, 181], [201, 215]], [[232, 246], [190, 211]], [[46, 39, 39, 45, 58, 76, 83, 87, 83, 78, 63], [102, 112, 139, 149, 151, 142, 131, 114, 103, 99, 96]], [[20, 17, 15, 19, 25, 34, 41, 41, 34], [109, 117, 139, 143, 142, 136, 123, 112, 104]], [[25, 26], [119, 119]], [[65, 65], [122, 122]], [[68, 68], [121, 121]], [[41, 70, 93], [176, 176, 166]], [[200, 202, 197], [85, 116, 193]], [[153, 148], [88, 207]], [[98, 104, 99], [64, 128, 211]]]"
s = "[[[19, 18, 34, 59, 83, 136, 145, 179], [148, 140, 131, 119, 112, 112, 114, 139]], [[15, 9, 1, 0, 10, 24, 49, 148, 173, 192, 208, 211, 209, 200, 153], [124, 128, 149, 180, 209, 225, 234, 238, 221, 194, 162, 145, 131, 126, 112]], [[107, 100, 98, 98, 107, 120, 134, 172], [121, 113, 87, 51, 36, 25, 19, 17]], [[106, 147, 163, 167, 167, 162, 157], [124, 95, 73, 61, 24, 5, 0]], [[114, 111, 111, 114, 136, 170], [141, 150, 195, 210, 235, 255]], [[104, 128, 152, 157, 160, 162], [127, 131, 154, 169, 196, 249]], [[27, 30], [173, 180]], [[39, 31, 40], [136, 137, 142]]]"


s = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in s.split("], ")] #remove all special characters and split on specific occurrence
xs = s[0::2] #grabs x coordinates
ys = s[1::2] #grabs y coordinates

x = []
y = []
temp1 = []
temp2 = []

for i in xs: #converts list of list format to 1d list of strings
    temp1 = i.strip(" ")
    temp1 = temp1.split(" ")
    for a in temp1:
        x.append(a)

for j in ys:
    temp2 = j.strip(" ")
    temp2 = temp2.split(" ")
    for b in temp2:
        y.append(b)

x = list(map(int, x)) #converts list of strings to list of ints
y = list(map(int, y))

plt.xlabel("X-axis") #set labels for axis and graph title
plt.ylabel("Y-axis")
plt.title("A test graph")

for (i,j) in zip(x,y): #plot the points on a graph
    plt.plot(i,j, 'ro')

plt.axis([0, 255, 0, 255]) #set the axis to be the image h:256px w:256px
plt.axis('auto') #fits the plot to the graph
#plt.xticks(rotation=90) #optional to rotate axis
plt.show()
