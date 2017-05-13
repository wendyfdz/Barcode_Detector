import numpy as np
import math
import matplotlib.pyplot as plt
def begin_end(pixel_intensity , increase, count):
    x = np.array(pixel_intensity)
    y = x.shape[1]
    alpha = increase
    sigma_left = []

    #---- Sigma Left---------------------------------------
    for i in range(0,y):
        if i == 0:
            left_summation = 0
            sigma_left.append(left_summation)
        else:
            if i <= alpha:
                left_summation = 0
                for m in range(0,i):
                    left_summation = math.fabs(x[0][m] - x[0][m+1]) + left_summation
            else:
                left_summation = 0
                for m in range((i-alpha),i):
                    left_summation =  math.fabs(x[0][m] - x[0][m+1]) + left_summation
            sigma_left.append(left_summation)
     #------------------------------------------------------


    #-------------- Test ----------------------
    # k = 2200
    # rang = range(1400, k+1)
    # rang.reverse()
    # left_summation = 0
    # for m in rang:
    #     if m != 0:
    #         left_summation += math.fabs(x[m] - x[m-1])
    #         sigma_left.append(left_summation)

    sigma_left = np.array(sigma_left)
    #--------------------MaxIndex--------------------------
    # max_sigma_left = max(sigma_left)
    # index_end = np.where(sigma_left == max_sigma_left)
    # index_end = np.array(index_end)
    # if index_end.shape[1] > 1:
    #     index_end = index_end[0,0]
    #-----------------------------------------------

    #----- Sigma Right ----------------------------
    sigma_right = []
    for i in range(0, y):
        right_summation = 0
        for j in range(i, (i + alpha)):
            if (j + 1) <= (y - 1):
                right_summation = math.fabs(x[0][j] - x[0][j + 1]) + right_summation
        sigma_right.append(right_summation)
     #--------------------------------------------

    #---------- Test -------------------------------
    # rang = range(k, 3001)
    # right_summation = 0
    # for m in rang:
    #         right_summation += math.fabs(x[m] - x[m + 1])
    #         sigma_right.append(right_summation)
    #-----------------------------------------------
    sigma_right = np.array(sigma_right)

    #--------------------MaxIndex---------------------------
    # max_sigma_right = max(sigma_right)
    # index_begining = np.where(sigma_right == max_sigma_right)
    # index_begining = np.array(index_begining)
    # if index_begining.shape[1] > 1:
    #     index_begining = index_begining[0, 0]
    # begining_ending = [index_begining , index_end]
    #-------------------------------------------------

    #-----------------Sigma---------------------------
    sigma = sigma_left - sigma_right
    #sigma_plus = sigma_right + sigma_left
    #-------------------------------------------------

    #-----------------Normalized Sigma----------------
    # max_value = max(sigma)
    # min_value = min(sigma)
    # if abs(max_value) > abs(min_value):
    #     max_value = max_value
    # else:
    #     max_value = min_value
    # for i in range(0,y):
    #     sigma[i] = sigma[i]/float(max_value)
    #-------------------------------------------------

    #--------------- Plot ----------------------------
    # plt.figure(1)
    # plt.plot(sigma)
    # plt.show()
    # plt.savefig("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + "Image"+ str(count) + "_sigma_px2.png")
    # plt.figure(2)
    # plt.plot(sigma_right)
    # plt.savefig("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + "Image"+str(count) + "_sigma_right_px2.png")
    # plt.figure(3)
    # plt.plot(sigma_left)
    # plt.savefig("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + "Image"+ str(count) + "_sigma_left_px2.png")
    # plt.figure(4)
    # # plt.plot(pixel_intensity)
    # # plt.savefig("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + "Image"+str(count) + "_pixel_intensity_px2.png")

    #-----------------------------------------

    print sigma
    return sigma
