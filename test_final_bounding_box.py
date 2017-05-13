import numpy as np
import math
from Scaling_Bounding_Box import scaling_box
def barcode_area(offset,Bisector_coordinates,start,end,Segments,max_segment_index, scaling_percent):
    offset = offset
    offset = np.array(offset)
    num_offset = offset.shape[0]
    barcode_start_average = 0
    barcode_end_average = 0
    coordinates = np.array(Bisector_coordinates)
    # for i in range(0, num_offset):
    #     barcode_start_average += barcode_start_average + coordinates[i][start]
    #     barcode_end_average = barcode_end_average + Bisector_coordinates[i][end]
    # barcode_start_average = barcode_start_average / (num_offset)
    # barcode_end_average = barcode_end_average / (num_offset)
    Seg_coordinates = [coordinates[0][start],coordinates[0][end]]
    Seg_coordinates = np.array(Seg_coordinates)
    Seg_coordinates = np.reshape(Seg_coordinates,(2,1,2))
    max_seg_coordinates = Segments[max_segment_index]
    Max_seg_length = math.hypot((max_seg_coordinates[0, 0] - max_seg_coordinates[0, 2]),(max_seg_coordinates[0, 1] - max_seg_coordinates[0, 3]))
    seg_increase = Max_seg_length/2
    vertical_segment = Seg_coordinates[1,0,0] - Seg_coordinates[0,0,0]
    print Seg_coordinates

    if vertical_segment == 0:
        Seg_slope = float('nan')
        Seg_angle = math.pi / 2
    elif vertical_segment != 0:
        Seg_slope = (Seg_coordinates[1,0,1] - Seg_coordinates[0,0, 1]) / float((Seg_coordinates[1,0,0] - Seg_coordinates[0,0,0]))
        Seg_angle = math.atan(Seg_slope)
    # Seg_perp_angle = Seg_angle + math.pi / 2
    # x_increase = abs(seg_increase * math.cos(Seg_perp_angle))
    # y_increase = abs(seg_increase * math.sin(Seg_perp_angle))
    box = np.zeros([4, 2])

    # # Create bounding box according to the slope
    if math.isnan(Seg_slope):
        Seg_perp_angle = Seg_angle + math.pi/2
        x_increase = abs(seg_increase * math.cos(Seg_perp_angle))
        box[1] = [Seg_coordinates[0,0,0] + (x_increase), Seg_coordinates[0,0,1]]
        box[0] = [Seg_coordinates[0,0,0] - (x_increase), Seg_coordinates[0,0,1]]
        box[2] = [Seg_coordinates[1,0,0] + (x_increase), Seg_coordinates[1,0,1]]
        box[3] = [Seg_coordinates[1,0,0] - (x_increase), Seg_coordinates[1,0,1]]
    elif Seg_slope == 0:
        Seg_perp_angle = Seg_angle + math.pi/2
        y_increase = abs(seg_increase * math.sin(Seg_perp_angle))
        box[0] = [Seg_coordinates[0,0,0], Seg_coordinates[0,0,1] + y_increase]
        box[3] = [Seg_coordinates[0,0,0], Seg_coordinates[0,0,1] - y_increase]
        box[1] = [Seg_coordinates[1,0,0], Seg_coordinates[1,0,1] + y_increase]
        box[2] = [Seg_coordinates[1,0,0], Seg_coordinates[1,0,1] - y_increase]
    elif Seg_slope > 0: #Clockwise direction
        Seg_perp_angle = Seg_angle + math.pi/2
        x_increase = abs(seg_increase * math.cos(Seg_perp_angle))
        y_increase = abs(seg_increase * math.sin(Seg_perp_angle))
        box[0] = [Seg_coordinates[0,0,0] - x_increase, Seg_coordinates[0,0,1] + y_increase]
        box[1] = [Seg_coordinates[1,0,0] - x_increase, Seg_coordinates[1,0,1] + y_increase]
        Seg_perp_angle = math.pi /2 - Seg_angle
        x_increase = abs(seg_increase * math.cos(Seg_perp_angle))
        y_increase = abs(seg_increase * math.sin(Seg_perp_angle))
        box[2] = [Seg_coordinates[1,0,0] + x_increase, Seg_coordinates[1,0,1] - y_increase]
        box[3] = [Seg_coordinates[0,0,0] + x_increase, Seg_coordinates[0,0,1] - y_increase]
    elif Seg_slope < 0:
        Seg_perp_angle = Seg_angle - math.pi/2
        x_increase = abs(seg_increase * math.cos(Seg_perp_angle))
        y_increase = abs(seg_increase * math.sin(Seg_perp_angle))
        box[0] = [Seg_coordinates[0,0,0] + x_increase, Seg_coordinates[0,0,1] + y_increase]
        box[1] = [Seg_coordinates[1,0,0] + x_increase, Seg_coordinates[1,0,1] + y_increase]
        Seg_perp_angle = Seg_angle + math.pi / 2
        x_increase = abs(seg_increase * math.cos(Seg_perp_angle))
        y_increase = abs(seg_increase * math.sin(Seg_perp_angle))
        box[2] = [Seg_coordinates[1,0,0] - x_increase, Seg_coordinates[1,0,1] - y_increase]
        box[3] = [Seg_coordinates[0,0,0] - x_increase, Seg_coordinates[0,0,1] - y_increase]

    #box_area = scaling_box(box,scaling_percent,Seg_slope)
    return box