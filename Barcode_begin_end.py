import math
def begin_end(first_rank,last_rank,Bisector_Length,pixel_intensity):

sigma = []
    for j in range(first_rank, last_rank):
        #Left Summantion
        summation_stop = 0
        summation_start = 0 - Bisector_Length
        Left_summation = 0
        for i in range(summation_start,summation_stop):
            Left_summation = math.abs(pixel_intensity[i]-pixel_intensity[i-1]) + Left_summation
        #Right Summation
        summation_start = 0
        summation_stop = 0 + Bisector_Length
        Right_summation = 0
        for i in range(summation_start,summation_stop):
            Right_summation = math.abs(pixel_intensity[i]-pixel_intensity[i+1]) + Left_summation
        sigma.append(Left_summation - Right_summation)
    return sigma