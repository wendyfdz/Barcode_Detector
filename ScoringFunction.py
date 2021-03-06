import math
import glob
from skimage import  io
import numpy as np
import cv2
from Create_Several_Offsets import Bisector_offsets
from GetPixelIntesity import pix_intesity
from Calc_barcode_begin_end import begin_end
import matplotlib.pyplot as plt
from test_final_bounding_box import barcode_area
import Save_Images
from Sigma_start_end import start_end_index

image_list = []
count = 0
for filename in glob.glob('/Users/wendyfernandez/PycharmProjects/Grocery_items/Photos_2/*.jpg'):
#Get Line Segments
    barcode = io.imread(filename)
    barcodeGray = cv2.cvtColor(barcode, cv2.COLOR_BGR2GRAY)
    det = cv2.createLineSegmentDetector()
    parameters = det.detect(barcodeGray)
    imageShape = np.shape(barcodeGray)
    barcodeWhiteBackground = np.ones(imageShape)
    barcodeLSD = det.drawSegments(barcodeWhiteBackground,parameters[0])
    barcodeLSD = barcodeLSD.astype('uint8')
    barcodeLSD = cv2.cvtColor(barcodeLSD, cv2.COLOR_BGR2GRAY)
    (thresh, barcodeLSD) = cv2.threshold(barcodeLSD, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    Segments = parameters[0]
    NumSeg = Segments.__len__()
    Score_Value=np.zeros([NumSeg,1])

    print 'LSD finished'

    for i in range(0,NumSeg):
        Seg_coordinates = Segments[i]
        Seg_center = [(Seg_coordinates[0, 0] + Seg_coordinates[0, 2]) / 2, (Seg_coordinates[0, 1] + Seg_coordinates[0, 3]) / 2]
        Seg_center = np.array(Seg_center)
        Seg_length = math.hypot((Seg_coordinates[0, 0] - Seg_coordinates[0, 2]), (Seg_coordinates[0, 1] - Seg_coordinates[0, 3]))
        vertical_segment=Seg_coordinates[0, 2] - Seg_coordinates[0, 0]
        if vertical_segment==0:
            Seg_slope=float('nan')
            Seg_angle=math.pi/2
        elif vertical_segment!=0:
             Seg_slope=(Seg_coordinates[0, 3] - Seg_coordinates[0, 1]) / float((Seg_coordinates[0, 2] - Seg_coordinates[0, 0]))
             Seg_angle = math.atan(Seg_slope)
        Seg_perp_angle = Seg_angle + math.pi / 2
        x_increase = abs(Seg_length * math.cos(Seg_perp_angle))
        y_increase = abs(Seg_length * math.sin(Seg_perp_angle))
        box=np.zeros([4,2])
        #Create bounding box according to the slope
        if math.isnan(Seg_slope):
            box[0] = [Seg_coordinates[0, 0] + x_increase, Seg_coordinates[0, 1]]
            box[1] =    [Seg_coordinates[0, 0] - x_increase, Seg_coordinates[0, 1]]
            box[2] = [Seg_coordinates[0, 2] + x_increase, Seg_coordinates[0, 3]]
            box[3] = [Seg_coordinates[0, 2] - x_increase, Seg_coordinates[0, 3]]
        elif Seg_slope==0:
            box[0] = [Seg_coordinates[0, 0], Seg_coordinates[0, 1] + y_increase]
            box[1] = [Seg_coordinates[0, 0], Seg_coordinates[0, 1] - y_increase]
            box[2] = [Seg_coordinates[0, 2], Seg_coordinates[0, 3] + y_increase]
            box[3] = [Seg_coordinates[0, 2], Seg_coordinates[0, 3] - y_increase]
        elif Seg_slope>0:
            box[0] = [Seg_coordinates[0, 0] - x_increase, Seg_coordinates[0, 1] + y_increase]
            box[1] = [Seg_coordinates[0, 0] + x_increase, Seg_coordinates[0, 1] - y_increase]
            box[2] = [Seg_coordinates[0, 2] - x_increase, Seg_coordinates[0, 3] + y_increase]
            box[3] = [Seg_coordinates[0, 2] + x_increase, Seg_coordinates[0, 3] - y_increase]
        elif Seg_slope<0:
            box[0] = [Seg_coordinates[0, 0] - x_increase, Seg_coordinates[0, 1] + y_increase]
            box[1] = [Seg_coordinates[0, 0] + x_increase, Seg_coordinates[0, 1] - y_increase]
            box[2] = [Seg_coordinates[0, 2] - x_increase, Seg_coordinates[0, 3] + y_increase]
            box[3] = [Seg_coordinates[0, 2] + x_increase, Seg_coordinates[0, 3] - y_increase]
        #Get limits of bounding Box
        x_lower_limit = box[:,0].min()
        x_upper_limit = box[:,0].max()
        y_lower_limit = box[:,1].min()
        y_upper_limit = box[:,1].max()
        # Get the segments inside the bounding boxes and save them in Neighborhood
        Neighborhood = []
        for k in range(0, NumSeg):
            if (x_lower_limit <= Segments[k, 0, 0] <= x_upper_limit and x_lower_limit <= Segments[k, 0, 2] <= x_upper_limit
                and y_lower_limit <= Segments[k, 0, 1] <= y_upper_limit and y_lower_limit <=Segments[k, 0, 3] <= y_upper_limit):
                Neighborhood.append(Segments[k])
        Neighborhood = np.asarray(Neighborhood)
        Elements_Neighborhood = Neighborhood.__len__()

        if Elements_Neighborhood==0:
            Score_Value[i]=0;
        elif Elements_Neighborhood==1:
            Neighbor_center = [(Neighborhood[0, 0,0] + Neighborhood[0,0, 2]) / 2, (Neighborhood[0,0, 1] + Neighborhood[0,0, 3]) / 2]
            Neighbor_center = np.array(Neighbor_center)
            Neighbor_Length = math.hypot((Neighborhood[0,0, 0] - Neighborhood[0,0, 2]), (Neighborhood[0,0, 1] - Neighborhood[0,0, 3]))
            vertical_neighbor = Neighborhood[0, 0, 2] - Neighborhood[0,0, 0]
            if vertical_neighbor == 0:
                Neighbor_angles = math.pi/2
            else:
                Neighbor_angles = math.atan((Neighborhood[0,0, 3] - Neighborhood[0,0, 1]) / float((Neighborhood[0, 0, 2] - Neighborhood[0,0, 0])))

            max_angle = max(Seg_angle,Neighbor_angles)
            min_angle = min(Seg_angle,Neighbor_angles)
            max_length = max(Seg_length,Neighbor_Length)
            min_length = min(Seg_length,Neighbor_Length)
            max_xcenter = max(Seg_center[0],Neighbor_center[0])
            min_xcenter = min(Seg_center[0],Neighbor_center[0])
            max_ycenter = max(Seg_center[1],Neighbor_center[1])
            min_ycenter = min (Seg_center[1],Neighbor_center[1])

            #Normalize Values
            if max_length == min_length :
                Seg_length = 1
                Neighbor_Length = 1
            else:
                Seg_length = (Seg_length - min_length) / float(max_length - min_length)
                Neighbor_Length = (Neighbor_Length - min_length) / float(max_length - min_length)
            if max_angle == min_angle :
                Seg_angle == 1
                Neighbor_angles == 1
            else:
                Seg_angle = (Seg_angle - min_angle) / float(max_angle - min_angle)
                Neighbor_angles = (Neighbor_angles - min_angle) / float(max_angle - min_angle)
            if max_xcenter == min_xcenter:
                Seg_center[0] = 1
                Neighbor_center[0] = 1
            else:
                Seg_center[0] = (Seg_center[0] - min_xcenter) / float(max_xcenter - min_xcenter)
                Neighbor_center[0] = (Neighbor_center[0] - min_xcenter) / float(max_xcenter - min_xcenter)
            if max_ycenter == min_ycenter:
                Seg_center[1] = 1
                Neighbor_center[1] =1
            else:
                Seg_center[1] = (Seg_center[1] - min_ycenter) / float(max_ycenter - min_ycenter)
                Neighbor_center[1] = (Neighbor_center[1] - min_ycenter) / float(max_ycenter - min_ycenter)

            #Comparison of Normalized Values
            comparison_length = abs(Neighbor_Length - Seg_length)
            comparison_angle = abs(Neighbor_angles - Seg_angle)
            comparison_xcenter = abs(Neighbor_center[0] - Seg_center[0])
            comparison_ycenter = abs(Neighbor_center[1] - Seg_center[1])
            #Score Value
            if comparison_angle <= 0.1 and comparison_length <= 0.3 and comparison_xcenter <= 0.1 and comparison_ycenter <= 0.1:
                Score_Value[i] = Score_Value[i] + 1


        elif Elements_Neighborhood>1:
            # Calculate the angle, lenght and center of the segments in the neighborhood
            Neighbor_angles = np.ones(Elements_Neighborhood)
            Neighbor_Length = np.ones(Elements_Neighborhood)
            Neighbor_center = np.ones((Elements_Neighborhood, 1, 2))
            for j in range(0, Elements_Neighborhood):
                x1 = Neighborhood[j, 0, 0]
                y1 = Neighborhood[j, 0, 1]
                x2 = Neighborhood[j, 0, 2]
                y2 = Neighborhood[j, 0, 3]
                Neighbor_Length[j] = math.hypot((x2 - x1), (y2 - y1))
                Neighbor_center[j, 0, 0] = (x1 + x2) / 2
                Neighbor_center[j, 0, 1] = (y1 + y2) / 2
                vertical_neighbor = (x2 - x1)
                if vertical_neighbor == 0:
                    Neighbor_angles[j] = math.pi/2
                else:
                    Neighbor_angles[j] = math.atan((y2 - y1) / float((x2 - x1)))


            max_angle = Neighbor_angles.max()
            min_angle = Neighbor_angles.min()
            max_length = Neighbor_Length.max()
            min_length = Neighbor_Length.min()
            max_xcenter = Neighbor_center[:, 0, 0].max()
            min_xcenter = Neighbor_center[:, 0, 0].min()
            max_ycenter = Neighbor_center[:, 0, 1].max()
            min_ycenter = Neighbor_center[:, 0, 1].min()
            for n in range(0, Elements_Neighborhood):
                Neighbor_angles[n] = (Neighbor_angles[n] - min_angle) / float((max_angle - min_angle))
                Neighbor_Length[n] = (Neighbor_Length[n] - min_length) / float((max_length - min_length))
                Neighbor_center[n, 0 , 0] = (Neighbor_center[n, 0 , 0] - min_xcenter) /float( (max_xcenter - min_xcenter))
                Neighbor_center[n, 0 , 1] = (Neighbor_center[n, 0 , 1] - min_ycenter) / float((max_ycenter - min_ycenter))

            # Normalized length, center and angle
            Seg_length = (Seg_length - min_length) / float((max_length - min_length))
            Seg_angle = (Seg_angle - min_angle) / float((max_angle - min_angle))
            Seg_center[0] = (Seg_center[0] - min_xcenter) / float((max_xcenter - min_xcenter))
            Seg_center[1] = (Seg_center[1] - min_ycenter) / float((max_ycenter - min_ycenter))

            # Obtained Score value
            comparison_length = np.ones(Elements_Neighborhood)
            comparison_angle = np.ones(Elements_Neighborhood)
            comparison_center = np.ones((Elements_Neighborhood, 1, 2))
            for m in range(0, Elements_Neighborhood):
                comparison_length[m] = abs(Neighbor_Length[m] - Seg_length)
                comparison_angle[m] = abs(Neighbor_angles[m] - Seg_angle)
                comparison_center[m,0,0] = abs(Neighbor_center[m, 0 , 0] - Seg_center[0])
                comparison_center[m, 0, 1] = abs(Neighbor_center[m, 0 , 1] - Seg_center[1])
                if comparison_angle[m] <= 0.1 and comparison_length[m] <= 0.3 and comparison_center[m,0,0] <= 0.1 and comparison_center[m,0,1] <= 0.1:
                    Score_Value[i] = Score_Value[i] + 1
    print "PLSD finished"
    max_Score = Score_Value.max()
    max_indexes = np.where(Score_Value == max_Score)
    max_toDisplay = max_indexes[0][0]
    max_segment = Segments[max_toDisplay]
    increase_barcode_cropping = math.hypot((max_segment[0, 0] - max_segment[0, 2]), (max_segment[0, 1] - max_segment[0, 3]))
    increase_barcode_cropping_decrease = int(round(increase_barcode_cropping  * 1))
    #print increase_barcode_cropping_decrease
    #print max_segment
    #print increase_barcode_cropping


    offset = [0]
    Bisector_coordinates = Bisector_offsets(max_toDisplay,Segments, barcode,offset)
    print ' Bisector finished'
    pixel_intensity = pix_intesity(offset,Bisector_coordinates,barcodeGray)
    print ' Pixel_intesity finished'
    sigma = begin_end(pixel_intensity,increase_barcode_cropping_decrease,count)
    print 'Sigma was calculated'
    reference_point = int(sigma.size/2)
    print reference_point
    start_end_position = start_end_index(sigma,reference_point,[400,5000],50)
    print 'start-end position obtained'
    print start_end_position
    start_end_position = np.array(start_end_position) * 2
    print start_end_position
    start = start_end_position[0]
    end = start_end_position[1]
    Bisector_coordinates_dimension = Bisector_coordinates[0].__len__()
    print Bisector_coordinates_dimension
    print Bisector_coordinates[0][start], Bisector_coordinates[0][end]
    box_area = barcode_area(offset, Bisector_coordinates,start_end_position[0],start_end_position[1], Segments, max_toDisplay,0)
    #print 'box area finished'
    Save_Images.draw_max_segment(barcode,Segments,max_toDisplay,count)
    Save_Images.draw_bisector_line(barcode,Bisector_coordinates,offset,count)
    # Save_Images.plot_intesity(pixel_intensity, offset, count)
    Save_Images.draw_bounding_box(barcode, box_area, count)



    # plt.plot(sigma)
    # plt.show()
    print count
    count = count + 1

