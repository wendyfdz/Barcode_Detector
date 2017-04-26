 def bisector_offset(barcodeGray, bisector_coordinates):
    import math
    from GetPixelIntesity import Get_pix_intensity
    Bisector_coordinates = bisector_coordinates
    Bisector_lastRow = Bisector_coordinates.shape[0] - 1
    vertical_segment = Bisector_coordinates[0,0] - Bisector_coordinates[Bisector_lastRow,0]
    Bisector_plus30 = []
    Bisector_minus30 = []
    Bisector_plus15 = []
    Bisector_minus15 = []

    if vertical_segment == 0:
        Bisector_Slope = float('nan')
    else:
        Bisector_Slope = (Bisector_coordinates[Bisector_lastRow,1] - Bisector_coordinates[0,1]) / float(Bisector_coordinates[Bisector_lastRow,0] - Bisector_coordinates[0,0])
        Bisector_angle = math.atan(Bisector_Slope)
    if math.isnan(Bisector_Slope):
        for i in range(0,Bisector_lastRow + 1):
            increase_30 =  Bisector_coordinates[i,0] * 0.30
            increase_15 =  Bisector_coordinates[i, 0] * 0.15

            Bisector_plus30.append([Bisector_coordinates[i,0] + increase_30,Bisector_coordinates[i,1]])
            Bisector_minus30.append([Bisector_coordinates[i, 0] - increase_30, Bisector_coordinates[i, 1]])
            Bisector_plus15.append([Bisector_coordinates[i,0] + increase_15], Bisector_coordinates[i,1])
            Bisector_minus15.append([Bisector_coordinates[i, 0] - increase_15], Bisector_coordinates[i, 1])
    elif Bisector_Slope == 0 :
        for i in range(0, Bisector_lastRow + 1):
            increase_30 = Bisector_coordinates[i, 1] * 0.30
            increase_15 = Bisector_coordinates[i, 1] * 0.15

            Bisector_plus30.append([Bisector_coordinates[i, 0], Bisector_coordinates[i, 1] + increase_30])
            Bisector_minus30.append([Bisector_coordinates[i, 0], Bisector_coordinates[i, 1] - increase_30])
            Bisector_plus15.append([Bisector_coordinates[i, 0], Bisector_coordinates[i, 1] + increase_15])
            Bisector_minus15.append([Bisector_coordinates[i, 0], Bisector_coordinates[i, 1] - increase_15])
    elif Bisector_Slope > 0:
        for i in range(0, Bisector_lastRow + 1):
            plus_x_increase_30 = Bisector_coordinates[i,0] * 0.30 * math.cos(Bisector_angle + (math.pi/2))
            plus_y_increase_30 = Bisector_coordinates[i,0] * 0.30 * math.sin(Bisector_angle + (math.pi/2))
            Bisector_plus30.append([Bisector_coordinates[i, 0] - plus_x_increase_30, Bisector_coordinates[i, 1] + plus_y_increase_30])

            plus_x_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.cos(Bisector_angle + (math.pi / 2))
            plus_y_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.sin(Bisector_angle + (math.pi / 2))
            Bisector_plus15.append([Bisector_coordinates[i, 0] - plus_x_increase_15, Bisector_coordinates[i, 1] + plus_y_increase_15])

            minus_x_increase_30 = Bisector_coordinates[i, 0] * 0.30 * math.cos((math.pi / 2) - Bisector_angle)
            minus_y_increase_30 = Bisector_coordinates[i, 0] * 0.30 * math.sin((math.pi / 2) - Bisector_angle)
            Bisector_minus30.append([Bisector_coordinates[i, 0] + minus_x_increase_30, Bisector_coordinates[i, 1] - minus_y_increase_30])

            minus_x_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.cos((math.pi / 2) - Bisector_angle)
            minus_y_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.sin((math.pi / 2) - Bisector_angle)
            Bisector_minus15.append([Bisector_coordinates[i, 0] + minus_x_increase_15, Bisector_coordinates[i, 1] - minus_y_increase_15])

    else:
        for i in range(0, Bisector_lastRow + 1):
            plus_x_increase_30 = Bisector_coordinates[i, 0] * 0.30 * math.cos(Bisector_angle - (math.pi / 2))
            plus_y_increase_30 = Bisector_coordinates[i, 0] * 0.30 * math.sin(Bisector_angle - (math.pi / 2))
            Bisector_plus30.append([Bisector_coordinates[i, 0] + plus_x_increase_30, Bisector_coordinates[i, 1] + plus_y_increase_30])

            plus_x_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.cos(Bisector_angle - (math.pi / 2))
            plus_y_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.sin(Bisector_angle - (math.pi / 2))
            Bisector_plus15.append([Bisector_coordinates[i, 0] + plus_x_increase_15, Bisector_coordinates[i, 1] + plus_y_increase_15])

            minus_x_increase_30 = Bisector_coordinates[i, 0] * 0.30 * math.cos((math.pi / 2) + Bisector_angle)
            minus_y_increase_30 = Bisector_coordinates[i, 0] * 0.30 * math.sin((math.pi / 2) + Bisector_angle)
            Bisector_minus30.append([Bisector_coordinates[i, 0] - minus_x_increase_30, Bisector_coordinates[i, 1] - minus_y_increase_30])

            minus_x_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.cos((math.pi / 2) + Bisector_angle)
            minus_y_increase_15 = Bisector_coordinates[i, 0] * 0.15 * math.sin((math.pi / 2) + Bisector_angle)
            Bisector_minus15.append([Bisector_coordinates[i, 0] - minus_x_increase_15, Bisector_coordinates[i, 1] - minus_y_increase_15])

            #     pixel_intensity = Get_pix_intensity(Bisector_coordinates, barcodeGray)
    # return pixel_intensity