# Project by Mehwish Alam and Ammara Khan
"""
Project Requiments:

Third Party Library Use :

	PIL

	numpy

	os(use for error handling)

Main File:

	main file containa six of file in order to run the file properly  make sure you have all the above library
installed and each file is in directory
	/Main File have :

	* Color
	* Crop
	* Collage
	* Grayscale
	* Bright
 	* Flip

Image  PAth :

	Make sure that the image title you given aso contain format (e.g : image.jpeg) and it must be in the directory.
	The file also gonna saved in your directory from where it import the image.


Image Size:

	Well we have six chooses available right now : For working color,bright, and grayscale make sure that your pic don't have big dimension
	if your image have big dimesnion it gonna take some point since in these three option we are dealing with each and every pixel.

End :
	That all you need to know before starting. Welcome to mini editor made by us......:)
"""

#importing the subfiles to main file for working

import crop
import collage
import flip
import bright
import color
import grayscale


#printing the available service we have now or the list of choice he can make from
print("\t\t\t-------------------------------- W E L C O M E    T O   E d i P r o ---------------------------------------\t\t")
print("\n\t\t\t\t\t\t\t\t\t\t\t    Created by Mehwish and Ammara")
#print("\n\n Choose from the options what you want to do on your image")
#print("\n1.CROP\n\n2.FLIP\n\n3.COLLAGE\n\n4.COLOR\n\n5.GRAY SCALE\n\n6.BRIGHT")

#Using function so we can use it late if user want to continue editing
def choice():
    print("\n\n Choose from the options what you want to do on your image")
    print("\n1.CROP\n\n2.FLIP\n\n3.COLLAGE\n\n4.COLOR\n\n5.GRAY SCALE\n\n6.BRIGHT")
    #handling error in input
    while True:
        #taking input from user
        option = input("\nEnter option no: ")
        #if option is from the given choice list
        if option in "123456":
            break
        #if user input anything rather than the voice it will ask user again and again
        else:
            print("\nPlease enter number of the above options")
            continue

    #calling the function from file according to user demand
    if option=="1":
        crop.crop()
    elif option=="2":
        flip.flip()
    elif option=="3":
        collage.collage()
    elif option=="4":
        color.color()
    elif option=="5":
        grayscale.grayscale()
    elif option=="6":
        bright.bright()

choice()
#Asking user if he/she wants to edit more
while True:
    input1 = input("\n\nDo you want to edit more(y/n)?: ")
    input1 = input1 .lower()

    if input1 =="y":
        #if yes then calling the choice function again to ask choice and call the function from other file according to user demand
        choice()
        continue

    else:
        #breaking the loop if user don't wants to edit more
        break