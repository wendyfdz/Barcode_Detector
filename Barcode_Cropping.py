#Obtain information of the Segment with max score to get the bisector center
max_segment = max_indexes[0][0]
Seg_coordinates = Segments[max_segment]
Seg_center = [(Seg_coordinates[0, 0] + Seg_coordinates[0, 2]) / 2, (Seg_coordinates[0, 1] + Seg_coordinates[0, 3]) / 2]
Seg_center = np.array(Seg_center)
vertical_segment=Seg_coordinates[0, 2] - Seg_coordinates[0, 0]

#Get the angle of the bisector
if vertical_segment == 0 :
    Seg_slope = float('nan')
    Seg_angle = math.pi/2
    Bisector_angle = Seg_angle + math.pi / 2
else :
     Seg_slope = (Seg_coordinates[0, 3] - Seg_coordinates[0, 1]) / float((Seg_coordinates[0, 2] - Seg_coordinates[0, 0]))
     Seg_angle = math.atan(Seg_slope)
     Bisector_angle = Seg_angle + math.pi / 2

# Get x and y coordinates of all the points in the trajectory of the bisector line based on the
# bisector angle with pixel_increment 10, there are four possible cases:
pixel_increment = 10
Bisector_coordinates = []

if Bisector_angle == 0 or Bisector_angle == math.pi: #The bisector is an horizontal line
    horizontal_image_size = barcode.shape[1]
    for i in range(0 , horizontal_image_size + 1, pixel_increment):
        Bisector_coordinates.append([i,Seg_center[0,1]])

elif Bisector_angle == math.pi/2 or Bisector_angle == 3*math.pi/2: #The bisector is a vertical line
    vertical_image_size = barcode.shape[0]
    for i in range(0 , vertical_image_size + 1, pixel_increment):
        Bisector_coordinates.append([Seg_center[0,0],i])

else:
    # Finding x and y intercept for the bisector line using the equation of the line y = mx + b and the Bisector center
    Bisector_slope = -1/float(Seg_slope)
    Bisector_y_intercept = Seg_center[0,1] - (Bisector_slope * Seg_center[0,0])
    x_max = barcode.shape[1] # Max x value of the input image
    y_max = barcode.shape[0] # Max y value of the input image
    y_at_x0 = Bisector_y_intercept
    y_at_xmax = (Bisector_slope * x_max) + Bisector_y_intercept
    x_at_y0 =  -Bisector_y_intercept/float(Bisector_slope)
    x_at_ymax = (y_at_xmax - Bisector_y_intercept)/float(Bisector_slope)

    # x and y increments
    Bisec_x_increment = pixel_increment * math.cos(Bisector_angle)
    Bisec_y_increment = pixel_increment * math.sin(Bisector_angle)

    if 0 < Bisector_angle < math.pi/2 or 3*math.pi < Bisector_angle < 2*math.pi: #The bisector angle is in the 1st or 4th quadrant
        #Posible cases of intercepts:
        if 0<=y_at_xmax<=y_max and 0<=y_at_x0<=y_max: # only y intercepts, iterate using x limits
            Bisector_coordinates.append([0,y_at_x0])
            for i in range(0,x_max):
                if Bisector_coordinates[i][0] < x_max:
                    Bisector_coordinates.append([Bisector_coordinates[i][0] + Bisec_x_increment , Bisector_coordinates[i][1] + Bisec_y_increment])
                else:
                    break
        elif 0<=x_at_y0<=x_max and 0<=x_at_ymax<=x_max: # only x intercepts, iterate using y limits
            Bisector_coordinates.append([x_at_y0,0])
            for i in range(0,y_max):
                if Bisector_coordinates[i][1] < y_max:
                    Bisector_coordinates.append([Bisector_coordinates[i][0] + Bisec_x_increment , Bisector_coordinates[i][1] + Bisec_y_increment])
                else:
                    break
        else: # Iterates using values of y and x
            if 0<=x_at_ymax<=x_max and 0<=y_at_xmax<=y_max
                Bisector_coordinates.append([x_at_ymax,y_max])
                for i in range(int(round(x_at_ymax)),x_max):
                    Bisector_coordinates.append([Bisector_coordinates[i][0] + Bisec_x_increment, Bisector_coordinates[i][1] + Bisec_y_increment])
                else:
                    break
            elif 0<=y_at_x0<=y_max and 0<=x_at_y0<=x_max:
                Bisector_coordinates.append([0,y_at_x0])
                for i range(0,int(round(x_at_y0))):
                    Bisector_coordinates.append(
                        [Bisector_coordinates[i][0] + Bisec_x_increment, Bisector_coordinates[i][1] + Bisec_y_increment])
                    else:
                        break
            elif 0<=x_at_y0<=x_max and 0<=y_at_xmax<=y_max:
                Bisector_coordinates.append([x_at_y0,0])
                for i range(0, int(round(x_at_y0))):
                      Bisector_coordinates.append([Bisector_coordinates[i][0] + Bisec_x_increment, Bisector_coordinates[i][1] + Bisec_y_increment])
                else:
                    break
            else:
                Bisector_coordinates.append([0,y_at_x0])
                for i range(0, int(round(x_at_y0))):
                    Bisector_coordinates.append([Bisector_coordinates[i][0] + Bisec_x_increment, Bisector_coordinates[i][1] + Bisec_y_increment])
                else:
                    break
    elif math.pi/2 < Bisector_angle < math.pi or math.pi< Bisector_angle < 3*math.pi/2: #The bisector angle is in the 2nd or 3rd quadrant  # Posible cases of intercepts:
        if 0 <= y_at_xmax <= y_max and 0 <= y_at_x0 <= y_max:  # only y intercepts, iterate using x limits
            Bisector_coordinates.append([0, y_at_x0])
            for i in range(0, x_max):
                if Bisector_coordinates[i][0] < x_max:
                    Bisector_coordinates.append([Bisector_coordinates[i][0] - Bisec_x_increment, Bisector_coordinates[i][1] - Bisec_y_increment])
                else:
                    break
        elif 0 <= x_at_y0 <= x_max and 0 <= x_at_ymax <= x_max:  # only x intercepts, iterate using y limits
            Bisector_coordinates.append([x_at_y0, 0])
            for i in range(0, y_max):
                if Bisector_coordinates[i][1] < y_max:
                    Bisector_coordinates.append([Bisector_coordinates[i][0] - Bisec_x_increment, Bisector_coordinates[i][1] - Bisec_y_increment])
                else:
                    break
        else:  # Iterates using values of y and x
            if 0 <= x_at_ymax <= x_max and 0 <= y_at_xmax <= y_max
                Bisector_coordinates.append([x_at_ymax, y_max])
                for i in range(int(round(x_at_ymax)), x_max):
                    Bisector_coordinates.append([Bisector_coordinates[i][0] - Bisec_x_increment, Bisector_coordinates[i][1] - Bisec_y_increment])
                else:
                    break
            elif 0 <= y_at_x0 <= y_max and 0 <= x_at_y0 <= x_max:
                Bisector_coordinates.append([0, y_at_x0])
                for i range(0, int(round(x_at_y0))):
                    Bisector_coordinates.append([Bisector_coordinates[i][0] - Bisec_x_increment, Bisector_coordinates[i][1] - Bisec_y_increment])
                    else:
                        break
        elif 0 <= x_at_y0 <= x_max and 0 <= y_at_xmax <= y_max:
            Bisector_coordinates.append([x_at_y0, 0])
            for i range(0, int(round(x_at_y0))):
                Bisector_coordinates.append([Bisector_coordinates[i][0] - Bisec_x_increment, Bisector_coordinates[i][1] - Bisec_y_increment])
            else:
                break
        else:
            Bisector_coordinates.append([0, y_at_x0])
            for i range(0, int(round(x_at_y0))):
                Bisector_coordinates.append([Bisector_coordinates[i][0] - Bisec_x_increment, Bisector_coordinates[i][1] - Bisec_y_increment])
            else:
                break