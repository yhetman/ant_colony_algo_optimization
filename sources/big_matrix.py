#!/usr/bin/python
# /* ************************************************************************** */
# /*                                                                            */
# /*                                                                            */
# /*   big_matrix.py                                                            */
# /*                                                                            */
# /*   By: yhetman <hetmanyuliia@gmail.com>                                     */
# /*                                                                            */
# /*   Created: 2021/03/02 22:05:50 by yhetman                                  */
# /*   Updated: 2021/03/03 13:32:04 by yhetman                                  */
# /*                                                                            */
# /* ************************************************************************** */

import numpy as np
import sys

def generate_big_matrix(size):
	big_matrix = np.random.randint(0, 10000, size=(size, size))/100.0
	np.fill_diagonal(big_matrix, np.inf, wrap=True)
	return (big_matrix)



if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("USAGE:\t./big_matrix.py [size_of_square_matrix]")
		exit(1)
	size = int(sys.argv[1])
	print (generate_big_matrix(size))
	exit(0)