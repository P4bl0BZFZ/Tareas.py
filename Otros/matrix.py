#Lista con datos de un curso emulado una matrix
#Se desea almacenar nombre, edad y nota final
matrix=[        ['ANA','JOAQUIN','LAURA'],
                [  21,    22,    24],
                [  4.9,   5.6,   6.1]]
#PRESENTAR DATOS A TRAVEZ DE LA MATRIX
#A TRAVEZ DE for in range DIRECTO

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[j][i],end=" ")
        if(j==2):
            print()