#changing the color of the image

def color():
    #importing PIL libaray for open and drawing image
    from PIL import Image,ImageDraw

    #importing numpy to get array that can manipulate to get results
    import numpy as np

    #importing os for error handling later in the program
    import os

    #taking path of image with format from user
    #image must be in directory
    path = input("\nWrite your image tittle with format :")

    #using os library to check if the file exist
    #it will remain in the loop unless the condition become true which happen when file succesfully open
    while os.path.exists(path) == False:

        #printing a statement to let the user know
            print("\nFile not Found, (e.g  = image.jpg)")

        #taking input again unless he gave valid image path
            path = input("\nWrite your image tittle with format :")
    #opening the image using Image.open from the library PIL
    input_image = Image.open(f"{path}","r")

    #Image is actually a three dimensional array containg height,width,channel
    #using numpy to convert image into three dimensional array which will manipulate later to make changes
    input_image_array=np.array(input_image)

    #we gonna have a complete array so using shape we gonna get the basic shape of the given image
    input_image_shape = input_image_array.shape

    #the above variable gonna have the height, width and channel in them, since we want to do the changes with the color
    #means we want to change the channel of the entire image while keeping the height and width constant
    #using indexing getting the zero index which is actually the height of the image
    height = input_image_shape[0]

    #using indexing getting the first index which is actually the width of the image
    width = input_image_shape[1]

    #creating a new image on the same dimension of the input image while keeping the mode RGB because we gonna deal in color
    output_image = Image.new("RGB" , (width,height))

    #using draw to create image
    draw = ImageDraw.Draw(output_image)

    #Since each pixels have their own r,g,b colors so if you want to change the colors we have to change the r,g,b of the image
    #Taking r,g,b values from user that he want to change, taking in the try block is for handling possible error occurs

    try:

        #taking red value from user, the value basically gonnna change the red channel later in the program
        red = int(input("Enter red (value should lies between 100 - 230 for best results) : "))

        #taking green value from user, the value basically gonnna change the green channel later in the program
        green = int (input("Enter green(value should lies between 100 - 230 for best results) : "))

        #taking blue value from user, the value basically gonnna change the blue channel later in the program
        blue = int(input("Enter blue(value should lies between 100 - 230 for best results) : "))

    #if user enter any other value except int then EXCEPT block will executes asking user gave to input again
    except:

        print("input value in int")
        red = int(input("Enter red(value should lies between 100 - 230 for best results) : "))
        green = int (input("Enter green(value should lies between 100 - 230 for best results) : "))
        blue = int(input("Enter blue(value should lies between 100 - 230 for best results) : "))

    #if you are little familiar with image editor you must be know that r,g,b have the highest value 255 which is white
    #the above exception only gonna deal with the data type not with the range so giving greater value gonna create a error
    #To handle error we gonna limit it to 255 if user enter 256 it gonna restart from 1

    if(red > 255 ):
        #if user input any value greater than 255 we gonna subtract that and restart the counter by 1 which means if user enter 256 it equals 1
        red = red - 255
        print(red)

    if(green > 255):
        #if user input any value greater than 255 we gonna subtract that and restart the counter by 1 which means if user enter 256 it equals 1
        green = green - 255
        print(green)

    if(blue > 255):
        #Same for blue : if user input any value greater than 255 we gonna subtract that and restart the counter by 1 which means if user enter 256 it equals 1
        blue = blue - 255
        print(blue)

    #Changing color can be done in two ways increasing or decreasing increasing means brighten up the color beacuse it goes close to the white
    #While the decreasing means darken up the color beacuse it goes close to the black

    #Asking user what he want to do
    #using try except module for error handling

    try:

        #printing the option and ask for the user input
        option = int(input("Do you want the RGB to be :  \nIncrease\"1\"\nDecrease\"2\" \n"))
    #if user  enter any value rather than integer data type then EXCEPT block gonna execute

    except:

        option = int(input("Do you want the RGB to be :  \nIncrease\"1\"\nDecrease\"2\" \n"))
    #looping it back to take input again and again unless user give valid input

        while ((option== '1') or (option=='2'))==False:
            option = input("Do you want the RGB to be :  \nIncrease\"1\"\nDecrease\"2\" \n")

    #threshold is uses to balance the changes since you already know we gonna change the r,g,b values but we gonna do it for the values
    #that are less than treshold so that image r,g,b would be balance. If you didn't use threshold so since we are increasing each pixel channel
    #by same number it would not change the color but brghten or darken the image beacuse same effect is applying to each pixel
    threshold = 220

    #printing the statement because below process gonna take some time if your pic is big
    print("\nWait for a sec until your image is ready")

    #the basic part of the program we already convert the image into three dimensional array using numpy and also find out the height and width of the image
    #using nested loop we can access each pixel of the image and then getting the channel of that pixela nd making changes
    for i in range(1,height):

    #outerloop running from 0 to given height

        for j in range(1,width):
        #innerloop run from o to given width
        #first loop work something like zero positon(height) and taking the eacha nd every pixel in horizontal line

        #since we already have three dimensional array fo the image and (index = 2) have the cahnnel of the image that is 3 (r,g,b)
            #using slicing to access to each pixel
            pixel = input_image_array[:i,:j,:]
            #channel gonna have r,g,b value at 0,1,2 that why they are fixed
            #getting each pixel by accessing the heigth and width of specified point
            r,g,b = pixel[i-1][j-1][0],pixel[i-1][j-1][1],pixel[i-1][j-1][2]

            #option have the user decison of either increase or decrease
            #if user input option (1) wich is increasing we just simply gonna multiply it with the some number whihc is defined below
            #incase user input "3" it gonna work on first one that is increase
            if (option==1 or option>2):

                #calculation to get the desired value of r,g,b so that it look good and won't become mess
                if ((red-r)**2,(green -g)**2,(blue-b)**2 < threshold**2):

                    #r value is multiply by 1.0 it is fixed,beacuse this is the value at which user get the best result
                    r = int(r *1.0)

                    #green value is high beacuse green give soothness to the image
                    g = int(g * 1.2)

                    #b value is multiply by 1.0 it is fixed,beacuse this is the value at which user get the best result
                    b = int(b * 1.0)

            #if user input option (2) wich is decreasing we just simply gonna divide it with the same number as above
            elif(option == 2):

                #calculation to get the desired value of r,g,b so that it look good and won't become mess
                if ((red-r)**2,(green -g)**2,(blue-b)**2 < threshold**2):

                    #r value is divide by 1.0 it is fixed,beacuse this is the value at which user get the best result
                    r = int(r /1.0)

                    #green value is high beacuse green give sooghten to the image
                    g = int(g / 1.2)

                    #b value is divide by 1.0 it is fixed,beacuse this is the value at which user get the best result
                    b = int(b / 1.0)

            #using draw to draw each point in the output image we created earlier of the sma dimension as input image
            draw.point((j-1,i-1),(r,g,b))

    #storing the format of the input image incase user don't want the format to be change
    path = path.split('.')

    print("\nYour image is ready\n")

    #asking user if he want the format to be change
    #using TryExcept block for error handling

    try:

        option = int(input("\nDo you want to change the format or go with the source format:\n\'1 for YES\'\n\'2 for No\'\nEnter : "))

    except:
        print("Enter either 1 or 2")
        option = int(input("Do you want to change the format or go with the source format:\n\'1 for YES\'\n\'2 for No\'\nEnter : "))

    #if user choose the option (1) which is to change the format
    if(option==1):

        #asking the user for the format of the output file he want to save
        format = input("\nEnter the format in which you want the image to be save: ")

        #if user enter the wrong input looping it until he get right input
        while ((format =='jpeg' or format == 'jpg' or format=='png')==False):

            print("Enter from : jpg . jpeg ,png")
            format = input("Enter the format in which you want the image to be save :")

    #if he chooose the option (2) which is to go with the input file format
    else:

        #we already split the path now we know that that format lies in the [1] index
        format = path[1]

    #asking user for input the filename he want the final image to be save
    filename = input("\nEnter File name : ")

    #finally saving the file so that user can get the modified pic :)
    output_image.save(f"{filename}.{format}")
    print("\nFile has been saved")

