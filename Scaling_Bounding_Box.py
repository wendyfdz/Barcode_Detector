import math
def scaling_box (box_area,scaling_percent, seg_slope):
    scaling_factor = scaling_percent / float(100)
    width = math.hypot(box_area[0][0]-box_area[1][0],box_area[0][1]-box_area[1][1])
    height = math.hypot(box_area[1][0] - box_area[2][0], box_area[1][1] - box_area[2][1])
    w_h_ratio = width / height
    area = height * width
    new_area = area * (scaling_factor + 1)
    new_height = math.sqrt(new_area / w_h_ratio)
    new_width = w_h_ratio * math.sqrt(new_area / w_h_ratio)
    width_increase = new_width - width
    height_increase = new_height - height

    if math.isnan(seg_slope) or seg_slope == 0:
        box_area[0] = [box_area[0][0] - width_increase, box_area[0][1] + height_increase]
        box_area[1] = [box_area[1][0] + width_increase, box_area[1][1] + height_increase]
        box_area[2] = [box_area[2][0] + width_increase, box_area[2][1] - height_increase]
        box_area[3] = [box_area[3][0] - width_increase, box_area[3][1] - height_increase]
    elif seg_slope > 0:  # Clockwise direction
        seg_angle = math.atan(seg_slope)
        x_plus_increase = abs(width_increase * math.cos(seg_angle)) + abs(height_increase * math.sin(seg_angle))
        x_minus_increase = abs(width_increase * math.cos(seg_angle)) - abs(height_increase * math.sin(seg_angle))
        y_plus_increase = abs(height_increase * math.cos(seg_angle)) + abs(width_increase * math.sin(seg_angle))
        y_minus_increase = abs(height_increase * math.cos(seg_angle)) - abs(width_increase * math.sin(seg_angle))

        box_area[0] = [box_area[0][0] - x_plus_increase, box_area[0][1] + y_minus_increase ]
        box_area[1] = [box_area[1][0] + x_minus_increase, box_area[1][1] + y_plus_increase]
        box_area[2] = [box_area[2][0] + x_plus_increase, box_area[2][1] - y_minus_increase]
        box_area[3] = [box_area[3][0] - x_minus_increase, box_area[3][1] - y_plus_increase]
    elif seg_slope < 0:
        seg_angle = math.atan(seg_slope)
        x_plus_increase = abs(width_increase * math.cos(seg_angle)) + abs(height_increase * math.sin(seg_angle))
        x_minus_increase = abs(width_increase * math.cos(seg_angle)) - abs(height_increase * math.sin(seg_angle))
        y_plus_increase = abs(width_increase * math.sin(seg_angle)) + abs(height_increase * math.cos(seg_angle))
        y_minus_increase = abs(width_increase * math.sin(seg_angle)) - abs(height_increase * math.cos(seg_angle))

        box_area[0] = [box_area[0][0] - x_minus_increase, box_area[0][1] + y_plus_increase]
        box_area[1] = [box_area[1][0] + x_plus_increase, box_area[1][1] - y_minus_increase]
        box_area[2] = [box_area[2][0] + x_minus_increase, box_area[2][1] - y_plus_increase]
        box_area[3] = [box_area[3][0] - x_plus_increase, box_area[3][1] + y_minus_increase]

    return box_area