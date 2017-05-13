import numpy as np
import math
def Cal_pix_intensity (Bisector_coordinates, barcodeGray):
    px_intesity = []
    Bisector_coordinates = np.array(Bisector_coordinates)
    Num_of_Points = Bisector_coordinates.shape[0]
    dimensions = barcodeGray.shape
    x_max = dimensions[1]
    y_max = dimensions[0]
    for i in range(0,Num_of_Points,2):
        if(Bisector_coordinates[i,1] < y_max and Bisector_coordinates[i,0] < x_max):
            px_intesity.append(barcodeGray[int(math.floor(Bisector_coordinates[i,1])),int(math.floor(Bisector_coordinates[i,0]))])
    px_intesity = np.array(px_intesity)
    return px_intesity