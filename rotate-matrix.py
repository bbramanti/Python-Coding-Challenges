import numpy as np

def rotate(mat,degrees):
	# a dictionary allows conversion
	# from degrees --> # of counter-clockwise rotations
	dict={90:3,180:2,270:1}
	# rot90() rotates counter-clockwise
	print (np.rot90(mat,dict[degrees]))

mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

#rotate a matrix 270 degrees clockwise
rotate(mat1,270)
#rotate a matrix 180 degrees clockwise                
rotate(mat1,180)
#rotate a matrix 90 degrees clockwise
rotate (mat1, 90)