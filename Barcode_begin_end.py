import numpy as np
import math
def begin_end(pixel_intensity , increase):
    x = pixel_intensity
    y = x.shape[0]
    alpha = increase
    sigma_left = []
    for i in range(0,y):
        if i == 0:
            left_summation = 0
            sigma_left.append(left_summation)
        else:
            if i <= alpha:
                left_summation = 0
                for m in range(0,i):
                    left_summation = math.fabs(x[m] - x[m+1]) + left_summation
            else:
                left_summation = 0
                for m in range((i-alpha),i):
                    left_summation =  math.fabs(x[m] - x[m+1]) + left_summation
            sigma_left.append(left_summation)
    sigma_left = np.array(sigma_left)
    max_sigma_left = max(sigma_left)
    index_end = np.where(sigma_left == max_sigma_left)
    sigma_right = []
    for i in range(0, y):
        right_summation = 0
        for j in range(i, (i + alpha)):
            if (j + 1) <= (y - 1):
                right_summation = math.fabs(x[j] - x[j + 1]) + right_summation
        sigma_right.append(right_summation)
    sigma_right = np.array(sigma_right)
    max_sigma_right = max(sigma_right)
    index_begining = np.where(sigma_right == max_sigma_right)

    begining_ending = [index_begining,index_end]
    #sigma = sigma_right - sigma_left
    # max_value = max(sigma)
    # min_value = min(sigma)
    # if abs(max_value) > abs(min_value):
    #     max_value = max_value
    # else:
    #     max_value = min_value
    # for i in range(0,y):
    #     sigma[i] = sigma[i]/float(max_value)
    return begining_ending