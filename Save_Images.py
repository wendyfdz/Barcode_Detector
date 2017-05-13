from skimage import io
import cv2
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler


def draw_max_segment(barcode,Segments, max_toDisplay,count):
    # ++++Display max segment++
    imagen = cv2.line(barcode, (Segments[max_toDisplay, 0, 0], Segments[max_toDisplay, 0, 1]),(Segments[max_toDisplay, 0, 2], Segments[max_toDisplay, 0, 3]), (255, 0, 0), 10)
    io.imsave("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + str(count) + "_max_segment.png",imagen)
    return None
def draw_bisector_line(barcode, Bisector_coordinates, offset, count):
    ##++++Display the bisector line to check result++
    Bisector_coordinates = np.array(Bisector_coordinates)
    offset = np.array(offset)
    Number_offset = offset.shape[0]
    color = [(0,255,0),(255,255,0),(0,255,0),(0,0,255),(255,0,255),(255,255,255),(0,255,255),(255,0,0),(255,255,0),(0,255,0),(0,0,255),(255,0,255),(255,255,255),(0,255,255)]
    for i in range(0, Number_offset):
        Bisector_last_row = Bisector_coordinates[i].__len__() - 1
        x0 = int(round(Bisector_coordinates[i][0][0]))
        y0 = int(round(Bisector_coordinates[i][0][1]))
        xf = int(round(Bisector_coordinates[i][Bisector_last_row][0]))
        yf = int(round(Bisector_coordinates[i][Bisector_last_row][1]))
        img = cv2.line(barcode,(x0, y0),(xf,yf),color[i],10)
    io.imsave("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + str(count) + "_bisector_line.png", img)
    return None

def plot_intesity(pixel_intesity, offset, count):
    # +++++plot intesity plot and save it+++++
    offset = np.array(offset)
    Number_offset = offset.shape[0]
    colors = ['r','b','g','y','m','r','b','g','y','m']
    plt.figure()
    for i in range(0, Number_offset):
        plt.subplot(Number_offset, 1, i + 1)
        plt.plot(pixel_intesity[i], color = colors[i])
        plt.axis('off')
    plt.savefig("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + str(count) +"_pixel_intesity.png")
    return None

def draw_bounding_box(barcode, box_area,count):
    # ++++++++print box_area and save it+++++++
    img_2 = cv2.line(barcode, (int(box_area[0, 0]), int(box_area[0, 1])), (int(box_area[1, 0]), int(box_area[1, 1])),(0, 0, 255), 12)
    img_2 = cv2.line(barcode, (int(box_area[1, 0]), int(box_area[1, 1])), (int(box_area[2, 0]), int(box_area[2, 1])), (0, 0, 255), 12)
    img_2 = cv2.line(barcode, (int(box_area[2, 0]), int(box_area[2, 1])), (int(box_area[3, 0]), int(box_area[3, 1])),(0, 0, 255), 12)
    img_2 = cv2.line(barcode, (int(box_area[3, 0]), int(box_area[3, 1])), (int(box_area[0, 0]), int(box_area[0, 1])), (0, 0, 255), 12)
    io.imsave("/Users/wendyfernandez/PycharmProjects/artelab_results_barcode_Area/" + str(count) + "_bounding_box.png", img_2)
    return None
