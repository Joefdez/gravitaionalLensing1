
import numpy as np
from source_generators import *

class Source ():
    'Source class to represent objects to be lensed'

    def __init__(self, name, stype, side, radius=0.0, aspectRatio = 1.0, maxLum = 1.0):

        self.name = name
        self.type = ltype
        self.aspectRatio = aspectRatio
        self.maxLum = maxLum
        if aspectRatio == 1.0:
            self.xsize, self.ysize = pixels, pixels
        else:
            self.xsize, self.ysize = pixels, pixels*aspectRatio

        self.radius = radius

        if stype == "square":
            self.view = square_source( radius, xsize, ysize, maxLum )
        elif stype == "circular":
            self.view = circular_source( radius, xsize, ysize)
        elif stype == "discs":
            self.view = discs_source( radius, xsize, ysize)

        self.lensedView = None

    def plotSource(self):



        print "Source array for " + self.name + "generated."



class Lense():
    'Lense class to represent lensing object.'

    def __init__(self, name, ltype, x01, x02):

        self.name = name
        self.name = ltype
        self.x01, self.x02 = x01, x02

        if ltype == "point":                                        # Define the distance metric for each type of lens
            def dist(self, x1, x2):
                dd = x1-self.x01)**2+(x2-self.x02)**2
                return dd
        elif ltype == "sis":
            def dist(self, x1, x2):
                dd = np.sqrt((x1-self.x01)**2+(x2-self.x02)**2)
                return dd

        print "Lense generated. \n Type: %s, Name: %s \
                                    \n Position in lens plane: %d, %d" % (self.name, self.ltype, self.x01, self.x02)

        def lensedImage(self, source):


            return
