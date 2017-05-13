def start_end_index(sigma, reference_point, y_axis_comparison, jump):
    found = 0
    end_sigma = int(sigma.size - 1)
    print "end_sigma: ", end_sigma
    print reference_point

    if abs(sigma[reference_point] - 5000) < 500:
        y_comparison = y_axis_comparison[0]
        print 'sigma is above 5000'
        print 'test_1'
        for i in range(reference_point,0,-jump) :
            print abs(sigma[i-1] - sigma[i])
            if abs(sigma[i-1] - sigma[i]) > y_comparison and found == 0:
                start_position = i
                found = 1
                print 'found start position'
        print "test_2"
        found = 0
        for i in range(reference_point,end_sigma,jump) :
            print abs(sigma[i + 1] - sigma[i])
            if abs(sigma[i] - sigma[i+1]) > y_comparison and found == 0:
                end_position = i
                found = 1
                print 'found end position'
        start_end = [start_position, end_position]
        return start_end
    else:
        y_comparison = y_axis_comparison[1]
        print 'sigma is below 5000'
        print 'test_1'
        for i in range(reference_point, 0, -jump):
            if abs(sigma[i]) > y_comparison and found == 0:
                start_position = i
                found = 1
        print "test_2"
        found = 0
        for i in range(reference_point,end_sigma,jump) :
            if abs(sigma[i]) > y_comparison and found == 0:
                end_position = i
                found = 1
        start_end = [start_position, end_position]
        return start_end


#---------------First Approach only comparing with the threshold------
# def start_end_index(sigma, reference_point, y_comparison, jump):
#     found = 0
#     end_sigma = int(sigma.size - 1)
#     print 'test_1'
#     print reference_point
#     for i in range(reference_point,0,-jump) :
#         if abs(sigma[i]) > y_comparison and found == 0:
#             start_position = i
#             found = 1
#     print "test_2"
#     found = 0
#     for i in range(reference_point,end_sigma,jump) :
#         if abs(sigma[i]) > y_comparison and found == 0:
#             end_position = i
#             found = 1
#     start_end = [start_position, end_position]
#     return start_end
#--------------------------------------------------------------------

#-------------------Second Approach----------------------------------
# for i in range(reference_point,0,-jump) :
#     print abs(sigma[i-1] - sigma[i])
#     if abs(sigma[i-1] - sigma[i]) > y_comparison and found == 0: #Can I encounter an error because of i+1?
#         start_position = i
#         found = 1
#         print 'found start position'
# print "test_2"
# found = 0
# for i in range(reference_point,end_sigma,jump) :
#     print abs(sigma[i + 1] - sigma[i])
#     if abs(sigma[i] - sigma[i+1]) > y_comparison and found == 0: #Can I encounter an error because of i+1?
#         end_position = i
#         found = 1
#         print 'found end position'
# start_end = [start_position, end_position]
# return start_end