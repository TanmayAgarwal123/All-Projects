import numpy as np
import pylab
import mahotas as mh
from skimage import measure
sky=mh.imread('sky.jpg')
pylab.imshow(sky)
t=mh.thresholding.otsu(sky.astype('uint8'))
labeled,stars = mh.label(sky>t)
print (stars)
pylab.imshow(labeled)
pylab.jet()
pylab.show()