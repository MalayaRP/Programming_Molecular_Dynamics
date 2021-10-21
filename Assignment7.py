# Program to Build the symmetric orthogonalization matrix
from numpy import *
from scipy import linalg as lg
dim=7 # Dimension of the basis set
def matrix_format(file): # this function transforms the given data into matrix format
    A_file=open(file,'r+')
    file_content=A_file.readlines()
    A=zeros([dim,dim])
    A_file.close()
    for line in file_content:
        A_line=line.rstrip()
        A_line=A_line.split()
        i=int(A_line[0])-1
        j=int(A_line[1])-1
        A[i][j]=float(A_line[2])
        A[j][i]=float(A_line[2])
    return A
S=matrix_format('s.dat') # overlap matrix; make sure the s.dat file is in the same directory where this code is present
values , vectors = lg.eig(S) # calculates eigen values and eigen vectors
values = values.real # eigenvalues of a real symmetric matrix are real
diag_values=zeros([dim,dim])
for i in range(dim):
    for j in range(dim):
        if i==j:
            diag_values[i][j]=values[i] # building diagonal matrix of corresponding eigenvalues
        else:
            continue
# building symmetric orthogonalization matrix
sym_orthogonalization_matrix=vectors.dot(((lg.inv(lg.sqrtm(diag_values)))).dot(vectors.T))
print('symmetric orthogonalization matrix=')
set_printoptions(suppress=True)
print(sym_orthogonalization_matrix)

