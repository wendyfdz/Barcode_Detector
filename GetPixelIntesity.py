import numpy as np
def Get_pix_intensity (Bisector_coordinates,barcodeGray):
    px_intesity = []
    Num_of_Points = Bisector_coordinates.shape[0] - 2
    for i in range(0,Num_of_Points):
        px_intesity.append(barcodeGray[int(round(Bisector_coordinates[i,1])),int(round(Bisector_coordinates[i,0]))])
    px_intesity = np.array(px_intesity)
    return px_intesity