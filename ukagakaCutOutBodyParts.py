import sys
import os
import cv2
import glob



ReadMaskFile = "./Mask.png"
ReadFileDirectory = "./MaskIn"
OutputDirectory = "./MaskOut/"

if not os.path.exists( ReadFileDirectory ) :
    os.mkdir( ReadFileDirectory )
    sys.exit( "plz set picture : " + ReadFileDirectory )

if not os.path.exists( OutputDirectory ) :
    os.mkdir( OutputDirectory )


files = glob.glob( ReadFileDirectory + "/*.png" )
mask = cv2.imread( ReadMaskFile , cv2.IMREAD_UNCHANGED )


for file in files :
    img  = cv2.imread( file , cv2.IMREAD_UNCHANGED)
    if img.shape == mask.shape :
        create = cv2.bitwise_and( img , mask )
        file_name = os.path.basename( file )
        cv2.imwrite( OutputDirectory + file_name , create )

    else:
        print( "skip : plz check your mask size" )



print( "done" )


