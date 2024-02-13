#changing the image into grayscale

def grayscale():
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
            print("File not Found, (e.g  = image.jpg)")

        #taking input again unless he gave valid image path
            path = input("Write your image tittle with format :")

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

            #Well the basic formula for getting gray is adding r,g,b and divide by 3 but that gonna return you black image no the grayscale
            #The rule is to keep the value of red the minium
            #green should be the highest because it provide soothness tot he image
            #blue can be in range between red and green
            r = r *0.3
            g = g * 0.59
            b = b * 0.11

            gray = int(r + g + b)
        #using draw to draw each point in the output image we created earlier of the sma dimension as input image
            draw.point((j-1,i-1),(gray,gray,gray))

   #storing the format of the input image incase user don't want the format to be change
    path = path.split('.')

    print("\nYour image is ready\n")

    #asking user if he want the format to be change
    #using TryExcept block fro error handling
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