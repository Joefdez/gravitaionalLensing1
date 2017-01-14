import numpy as np


def identity(source,scale,xl=8.,yl=4.):				#Function defining identity transformation: moves source to image plane

  """
  Identity transformation. Moves image on image plane to lens plane.
  Returns image array and magnification map array.
  """

  pn="Identity transformation"					#Name of figure
  plt.figure(pn)						#Open figure window
  ssize=len(source)						#Tuple with dimensions of source array
  imsize=ssize*scale						#Size of lens plane, as a multiple of that of the source plane
  image=np.zeros([imsize,imsize])				#Declare image plane array
  A=np.zeros([ssize,ssize])					#Amplification map matrix

  C=0.								#Set sky constant to 0

  xs=2.*xl/(imsize-1)						#Size of pixel in image
  ys=2.*yl/(ssize-1)						#Size of pixel in source

  for ii in range(imsize):					#Loop for filling in image plane pixel values
    for ji in range(imsize):
      x1=-xl+(ii-1)*xs						#Transform image pixels to coordinates
      x2=-xl+(ji-1)*xs
      y1=x1							#Identity transformation
      y2=x2
      fx=(y1+yl)/ys+1						#Transform coordinates into pixel values in source plane
      fy=(y2+yl)/ys+1

      if 0<=fx<ssize and 0<=fy<ssize:				#If pixels are inside limits of source, apply identity transformation: assign source value to image
	image[ii,ji]=source[fx,fy]
	A[fx,fy]=A[fx,fy]+1.

      else:
	  image[ii,ji]=C					#If pixels are not inside limits of source, assign sky value to image

  return image, A						#Return image array and magnification map array

def lens(ltype, dist, source, scale, x01, x02, xl=8., yl=4.,gamma=0.,plotr=0, rout=0):		#Gravitational lens. If ltype=1, point lens. If ltype=2, SIS lens. If gamma!=0, quadrupolar perturbation is included

    """
    Gravitational lensing.

    Function input parameters:

  	  ltype: Takes integer input. If value 1 is given, a point lens is chosen. If value 2 is given, a SIS lense is chosen
  	  Source: Array containing light source.
  	  Scale: Ratio of number of pixels in image plane to number of pixels in source plane
  	  x01, x01: Position of lens in lens plane, in scaled units
  	  xl, yl: Relative size of source and image plane in scaled units
  	  gamma: gamma parameter for quadrupolar perturbation to point or SIS lens
  	  plotr: If plotr=1, plot is generated and shown. If rout>1, error messaged is returned and null value returned.
  	  rout: If rout=0, only the lensed image plane is plotted. If rout=1, only the magnification plot is mapped. If rout=2, both are plotted. If rout>2, error message is given and null value returned.

     Output: Returns two arrays, lensed image array image, and magnification map A.

    """
    print yl
    if plotr>1:
      print('Invalid value of plotr variable')			#Error message for wrong value of plotr variable. Return to main.
      return
    if rout>2:
      print('Invalid value of rout variable')			#Error message for wrong value of rout variable. Return to main.
      return

    ssize=len(source)						#Tuple with dimensions of source array
    imsize=ssize*scale						#Size of lens plane, as a multiple of that of the source plane
    image=np.zeros([imsize,imsize])				#Declare image plane array
    A=np.zeros([ssize,ssize])					#Amplification map matrix
    """
    if ltype==1:							#Set distance function for point lens (square of distance)
      print('Point lens')
      def dist(x0,x,z0,z):
        d=(x-x0)**2+(z-z0)**2
        return d

    elif ltype==2:						#Set distance function for SIS lens (modulus)
      print('SIS lens')
      def dist(x0,x,z0,z):
        d=np.sqrt((x1-x01)**2+(x2-x02)**2)
        return d
    """
    C=0.								#Set sky constant to 0
    print xl ,yl, imsize, ssize
    xs=2.*xl/(imsize-1)						#Size of pixel in image
    ys=2.*yl/(ssize-1)						#Size of source in image


    for ii in range(imsize):
        for ji in range(imsize):
            x1=-xl+(ii-1)*xs						#Transform image pixels to coordinates
            x2=-xl+(ji-1)*xs

            d=dist(x1,x2)					#Calculate distance (denomiator in transformation, see guide)

            y1=x1*(1-gamma)-(x1-x01)/d				#Apply transformation from image to source
            y2=x2*(1+gamma)-(x2-x02)/d
            print y1, y2, ys
            fx=(y1+yl)/ys+1
            					#Transform coordinates into pixel values in source rays
            fy=(y2+yl)/ys+1

            if 0<=fx<ssize and 0<=fy<ssize:				#If pixels are inside limits of source, assign source value at these points to image plane in point ii,ji considered
  	         image[ii,ji]=source[fx,fy]
  	         A[fx,fy]=A[fx,fy]+1.

            else:							#If not, assign sky value
  	         image[ii,ji]=C


    """
    if gamma==0 and ltype==1:					#Set plot text
      pn="%s%0.2f%s%0.2f" % ("Point lens\nLens position: x01=",x01,",x02=",x02)
    elif gamma!=0 and ltype==1:
      pn="%s%0.2f%s%0.2f%s%0.2f" % ("Point lens with quadrupolar perturbation\nLens position: x01=",x01,",x02=",x02,", gamma=",gamma)
    elif gamma==0 and ltype==2:
      pn="%s%0.2f%s%0.2f" % ("SIS lens x01=",x01,",x02=",x02)
    elif gamma!=0 and ltype==2:
      pn="%s%0.2f%s%0.2f%s%0.2f" % ("SIS lens with quadrupolar perturbation\nLens position: x01=",x01,",x02=",x02,", gamma=",gamma)

    if plotr==1:

      if rout==0:
        plt.figure('lens')						#Declare figure
        ax1=plt.axes()						#Declare axis
        ax1.xaxis.set_ticklabels([])				#Remove ticks
        ax1.yaxis.set_ticklabels([])
        plt.figtext(-2.5, -2.5, pn)
        plt.title(pn,loc='center')
        plt.imshow(image)						#Plot using plt.imshow

      elif rout==1:
        plt.figure('magmap')
        ax2=plt.axes()						#Declare axis
        ax2.xaxis.set_ticklabels([])				#Remove ticks
        ax2.yaxis.set_ticklabels([])
        plt.title(pn,loc='center')
        plt.imshow(A)						#Plot using plt.imshow


      elif rout==2:
        #plt.figure('lens and magmap')
        plot,(ax1,ax2)=plt.subplots(1,2,sharex=False,sharey=False)
        ax1.xaxis.set_ticklabels([])				#Remove ticks
        ax1.yaxis.set_ticklabels([])
        ax2.xaxis.set_ticklabels([])				#Remove ticks
        ax2.yaxis.set_ticklabels([])
        plot.suptitle(pn,fontsize=15.,y=0.94,verticalalignment='top')
        ax1.imshow(image)
        ax2.imshow(A)

    """
    return image, A						#Return lensed image and magnification map


"""
  def binary_lens(source,scale,a,mr,theta, uu0, xl=8.,yl=4., plotr=0):


    Binary lens
  	  source:
  	  scale:
  	  a:
  	  mr:
  	  theta:
  	  uu0:
  	  xl:
  	  yl:
  	  plot:
    Function input parameters:lensed image array image, and magnification map A and coordinates in image plane of line at angle theta with the horizontal axis and at distance uu0 from origin.


    Output:



    ssize=len(source)						     #Tuple with dimensions of source array
    imsize=ssize*scale						    #Size of lens plane, as a multiple of that of the source plane
    image=np.zeros([imsize,imsize])				#Declare image plane array
    A=np.zeros([ssize,ssize])					#Amplification map matrix
    curve=np.zeros(ssize)
    print(imsize)


    ep1=mr/(mr+1.)
    ep2=1./(mr+1.)


    C=0.								#Set sky constant to 0

    xs=2.*xl/(imsize-1)						#Size of pixel in image
    ys=2.*yl/(ssize-1)						#Size of source in image

    pl1=np.array([-1*ep2*a,0])					#Position of lens 1
    pl2=np.array([ep1*a,0])					#Position of lens 2



    for ii in range(imsize):					#Loop for filling in image plane pixel values
      x1=-xl+(ii-1)*xs						#Transform image x pixels coor to coordinates
      for ji in range(imsize):
        x2=-xl+(ji-1)*xs						##Transform image y pixels coor to coordinates



        d12=(x1-pl1[0])**2+(x2-pl1[1])**2
        d22=(x1-pl2[0])**2+(x2-pl2[1])**2

        y1=x1-ep1*(x1-pl1[0])/d12-ep2*(x1-pl2[0])/d22		#Apply transformation from image to source
        y2=x2-ep1*(x2-pl1[1])/d12-ep2*(x2-pl2[1])/d22


        fx=(y1+yl)/ys+1						#Transform coordinates into pixel values in source rays
        fy=(y2+yl)/ys+1

        if 0<=fx<ssize and 0<=fy<ssize:				#If pixels are inside limits of source, assign source value at these points to image plane in point ii,ji considered

  	         #image[ii,ji]=source[fx,fy]
  	         A[fx,fy]=A[fx,fy]+1.

        #else:							#If not, assign sky value
  	#image[ii,ji]=C

    for jj in range(ssize):
      y1=-yl+(jj-1)*ys
      line_coo=np.tan(theta)*y1+uu0*(np.cos(theta)+np.sin(theta)*np.tan(theta))
      line_pix=(line_coo+yl)/ys+1
      curve[jj]=A[jj,line_pix]
    if plotr==0:							#Plotting routine
      fig=plt.figure('Plot')
      #ax1=fig.add_subplot(211)
      #ax1.xaxis.set_ticklabels([])
      #ax1.yaxis.set_ticklabels([])
      #ax2=fig.add_subplot(212)
      #ax2.xaxis.set_ticklabels([])
      #ax2.yaxis.set_ticklabels([])

      #ax1.imshow(A)
      #ax2.plot(curve)
      plt.plot(curve)
    return curve						#Return lensed image and magnification map
"""
