
import numpy as np

def square_source(rr, xsize, ysize, lum=0):

    source = np.zeros([xsize, ysize])
    xhalf,yhalf = xsize/2., ysize/2.

    for ii in range(xsize):
        for jj in range(ysize):
            if abs(xhalf - ii)<=rr and abs(yhalf - jj)<=rr:
                source[ii,jj] = lum

    return source

def circular_source(rr, xsize, ysize, lum=0):

    source = np.zeros([xsize, ysize])
    r2=r**2						                    #Calculate square of radius of source
    xhalf,yhalf=xsize/2.,ysize/2.				    #Calculate coordinates of center
    for i in range(xsize):			              	#Scan through frame to find points which are to be included in source
        for j in range(ysize):
            if (xhalf-i)**2+(yhalf-j)**2<r2:
	               source[i,j]=1.					#Change zeros to ones in source
    return source						            #Return desired source


def discs_source(rr, xsize, ysize, lum=0):

    source = np.zeros([xsize, ysize])

    space = rr/ndiscs
    rrs = np.arange( space, (rr + rr/ndiscs) , rr/ndiscs)
    rr2 = rrs*rrs
    lums = np.zeros(ndiscs)
    for ii=0, ndiscs:
        lums[ii]= 2**ii
      xhalf,yhalf=xsize/2.,ysize/2.				#Calculate cooridinates of center
    for i in range(xsize):				#Scan through frame to find points to be included in source
        for j in range(ysize):
            if (xhalf-i)**2+(yhalf-j)**2<=rr2[0]:
	               source[i,j]=64.
            elif (xhalf-i)**2+(yhalf-j)**2>rr2[0] and (xhalf-i)**2+(yhalf-j)**2<=rr2[1]:
	               source[i,j]=32.
            elif (xhalf-i)**2+(yhalf-j)**2>rr2[1] and (xhalf-i)**2+(yhalf-j)**2<=rr2[2]:
	               source[i,j]=8.
            elif (xhalf-i)**2+(yhalf-j)**2>rr2[2] and (xhalf-i)**2+(yhalf-j)**2<=rr2[3]:
	               source[i,j]=2.
            elif (xhalf-i)**2+(yhalf-j)**2>rr2[3] and (xhalf-i)**2+(yhalf-j)**2<=rr2[4]:
	               source[i,j]=1.


    return source
