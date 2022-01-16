import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])
Image('filedestination changer.jpg')
output = reader.readtext('filedestination changer.jpg')
for x in output:
	print(x[-2])
