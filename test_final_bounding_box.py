import numpy as np
import math
def barcode_area(Bisector_coordinates,start,end,Segments,max_segment_index):
    Seg_coordinates = [Bisector_coordinates[start], Bisector_coordinates[end]]
    Seg_coordinates = np.array(Seg_coordinates)
    max_seg_coordinates = Segments[max_segment_index]
    Max_seg_length = math.hypot((max_seg_coordinates[0, 0] - max_seg_coordinates[0, 2]),(max_seg_coordinates[0, 1] - max_seg_coordinates[0, 3]))
    seg_increase = Max_seg_length/2
    vertical_segment = Seg_coordinates[1,0,0] - Seg_coordinates[0,0,0]

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
        box[0] = [Seg_coordinates[0,0,0] + (x_increase), Seg_coordinates[0,0,1]]
        box[1] = [Seg_coordinates[0,0,0] - (x_increase), Seg_coordinates[0,0,1]]
        box[2] = [Seg_coordinates[1,0,0] + (x_increase), Seg_coordinates[1,0,1]]
        box[3] = [Seg_coordinates[1,0,0] - (x_increase), Seg_coordinates[1,0,1]]
    elif Seg_slope == 0:
        Seg_perp_angle = Seg_angle + math.pi/2
        y_increase = abs(seg_increase * math.sin(Seg_perp_angle))
        box[0] = [Seg_coordinates[0,0,0], Seg_coordinates[0,0,1] + y_increase]
        box[1] = [Seg_coordinates[0,0,0], Seg_coordinates[0,0,1] - y_increase]
        box[2] = [Seg_coordinates[1,0,0], Seg_coordinates[1,0,1] + y_increase]
        box[3] = [Seg_coordinates[1,0,0], Seg_coordinates[1,0,1] - y_increase]
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
    return box
