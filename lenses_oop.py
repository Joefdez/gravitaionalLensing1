from transformations import *

class simpleLense():
    'Lense class to represent lensing object.'

    def __init__(self, name, ltype, x01, x02):
        """ Constructor method """
        self.name = name
        self.ltype = ltype
        self.x01, self.x02 = x01, x02

        print "Lense generated. \n Type: %s, Name: %s \
                                    \n Position in lens plane: %d, %d" % (self.name, self.ltype, self.x01, self.x02)


        def __chooseMetric__(self):
            if self.ltype == "point":                                        # Define the distance metric for each type of lens
                def distance(x1,x2):
                    dd = (x1-self.x01)**2+(x2-self.x02)**2
                    return dd
            elif self.ltype == "sis":
                def distace(x1,x2):
                    dd = np.sqrt((x1-self.x01)**2+(x2-self.x02)**2)
                    return dd

            return distance

        self.dist = __chooseMetric__(self)


    def lensedImage(self, source, scale, xl=8., yl=4., gamma=0.):
        """ Takes an input light source object and gives the lensed image"""
        image, magMap = lens(self.ltype, self.dist, source, self.x01, self.x02, xl, yl, gamma)

        return image, magMap
