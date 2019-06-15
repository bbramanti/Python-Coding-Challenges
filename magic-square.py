import numpy as np

# non magic square
square_1 = [ [1,2,3],
             [4,5,6],
             [7,8,9] ]
# magic square
square_2 = [ [2,7,6],
             [9,5,1],
             [4,3,8] ]
# non magic square different size
square_3 = [ [10,4],
             [3,17] ]
           
def magic_check(square):
    row_sums = np.sum(square, 0)
    column_sums = np.sum(square, 1)
    diagonal_one = np.diagonal(square).sum()
    diagonal_two = np.fliplr(square).diagonal().sum()
    all_sums = []
    all_sums.extend(row_sums)
    all_sums.extend(column_sums)
    all_sums.append(diagonal_one)
    all_sums.append(diagonal_two)
    if len(set(all_sums)) == 1:
        print ("this is a magic square")
    else:
        print ("this is not a magic square")
         
magic_check(square_1)
magic_check(square_2)
magic_check(square_3)
