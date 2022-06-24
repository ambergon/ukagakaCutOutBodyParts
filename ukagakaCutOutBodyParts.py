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
    #img = cv2.imread( file , cv2.IMREAD_COLOR)
    #ch_Blue, ch_Green, ch_Red , ch_Alpha = cv2.split(img[:,:,:4])

    #ch_a = cv2.inRange(img, ( blue , green , red) , ( blue , green , red ) )
    #dst = cv2.merge((ch_Blue, ch_Green, ch_Red, cv2.bitwise_not(ch_a)))
    #cv2.imwrite( "./" + OutputDirectory + "/" + file_name , dst )

    create = cv2.bitwise_and( img , mask )
    #cv2.imshow( 'image' , create )
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    file_name = os.path.basename( file )
    cv2.imwrite( OutputDirectory + file_name , create )








print( "done" )


