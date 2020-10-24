#Write a program to perform the Matrix addition, Multiplication and Transpose Operation. 
#3005 (New Rollno:372) Shravan SYIT
mat_1 = [[5, 8, -5], 
      [31,44,94], 
      [16,108,109]]

mat_2 = [[5, 1, -3],
           [2,6,-8], 
           [-1,3,3]]
mat_3 = [[0,0,0,],
     [0,0,0,],
     [0,0,0,]]

for i in range(len(mat_1)):
    for j in range(len(mat_2[0])):
        for k in range(len(mat_2)):
            mat_3[i][j] += mat_1[i][k] + mat_2[k][j]
        
print(mat_3)

mat_3 = [[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]] 

for i in range(len(mat_1)):
    for j in range(len(mat_2[0])):
        for k in range(len(mat_2)):
            mat_3[i][j] += mat_1[i][k] * mat_2[k][j]
        
print(mat_3)

for i in map(list, zip(*mat_1)):
    print(i)
