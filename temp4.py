

import cv2 as cv
import numpy as np
import os
from PIL import Image
import os.path, sys

path = r"C:\Users\AYESHA\Desktop\img"
dirs = os.listdir(path)




def match():
    for item in dirs:
        fullpath = os.path.join(path,item)        
        if os.path.isfile(fullpath):


            main_img = cv.imread(fullpath, cv.IMREAD_UNCHANGED)
            template_img = cv.imread('vsmall.jpeg', cv.IMREAD_UNCHANGED)
            
            f, e = os.path.splitext(fullpath)

            result = cv.matchTemplate(main_img, template_img, cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            print('Best match top left position: %s' % str(max_loc))
            print('Best match confidence: %s' % max_val)

            threshold = 0.8
            if max_val >= threshold:
                print('template matched.')


                template_w = template_img.shape[1]
                template_h = template_img.shape[0]

    
                top_left = max_loc
                bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
                cv.imshow('Result', main_img)
                cv.waitKey()
            else:
                print("template not matched")
                os.remove(fullpath)


                
                
match()

 