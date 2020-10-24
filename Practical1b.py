#Write a program to perform the Matrix addition, Multiplication and Transpose Operation. 
#3005 (New Rollno:372) Shravan SYIT
Mat1 = [[5, 8, -5], 
      [31,44,94], 
      [16,108,109]]

Mat2 = [[5, 1, -3],
           [2,6,-8], 
           [-1,3,3]]
Mat3 = [[0,0,0,],
     [0,0,0,],
     [0,0,0,]]

for i in range(len(Mat1)):
    for j in range(len(Mat2[0])):
        for k in range(len(Mat2)):
            Mat3[i][j] += Mat1[i][k] + Mat2[k][j]
        
print(Mat3)

Mat3 = [[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]] 

for i in range(len(Mat1)):
    for j in range(len(Mat2[0])):
        for k in range(len(Mat2)):
            Mat3[i][j] += Mat1[i][k] * Mat2[k][j]
        
print(Mat3)

for i in map(list, zip(*Mat1)):
    print(i)
