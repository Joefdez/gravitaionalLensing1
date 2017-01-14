from source_generators import *     # includes numpy import, np
import matplotlib.pylab as plt

class modelSource ():
    'Source class to represent objects to be lensed'

    def __init__(self, name, stype, side, radius=0.0, aspectRatio = 1.0, maxLum = 1.0):
        """ Constructor method """
        self.name = name
        self.type = stype
        self.aspectRatio = aspectRatio
        self.maxLum = maxLum
        if aspectRatio == 1.0:
            self.xsize, self.ysize = side,  side
        else:
            self.xsize, self.ysize = side, side*aspectRatio

        self.radius = radius

        if stype == "square":
            self.view = square_source( radius, self.xsize, self.ysize, maxLum )
        elif stype == "circular":
            self.view = circular_source( radius, self.xsize, self.ysize)
        elif stype == "discs":
            self.view = discs_source( radius, self.xsize, self.ysize)

        self.lensedView = None

        print "Source array " + self.name + " generated."

    def plotSource(self):
        """ Plot the source """
        plt.figure('lens')						#Declare figure
        ax1=plt.axes()						#Declare axis
        ax1.xaxis.set_ticklabels([])				#Remove ticks
        ax1.yaxis.set_ticklabels([])
        #plt.figtext(-2.5, -2.5, pn)
        #plt.title(pn,loc='center')
        plt.imshow(self.view)



class imageSource():
    Class for handling actual images as sources

    def __init__(self, file ):

        #Remember to open and close properly
