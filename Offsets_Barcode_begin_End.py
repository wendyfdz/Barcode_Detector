import numpy as np
from Calc_barcode_begin_end import begin_end
def Offset_begin_end(offsets, pixel_intensity, increase, count):
    number_offsets = pixel_intensity.__len__()
    print number_offsets
    sigma = []
    for i in range(0,number_offsets):
        globals()['sigma_offset_' + str(offsets[i])] = begin_end(pixel_intensity[i], increase, count)
        sigma.append(globals()['sigma_offset_' + str(offsets[i])])
    sigma = np.array(sigma)
    return sigma