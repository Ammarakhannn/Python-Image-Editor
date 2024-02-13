#making collage of given image

def collage():
    #importing PIL libaray for open and drawing image
    from PIL import Image,ImageDraw

    #importing numpy to get array that can manipulate to get results
    import numpy as np

    #importing os for error handling later in the program
    import os

    #giving option to the user of vertical or horizontal collage
    print("\nChoose from the options below that how you want to make the collage\n1.VERTICAL COLLAGE\n2.HORIZONTAL COLLAGE")

    print("\nNOTE: if you choose vertical then images should be in vertical and if you choose horizontal then should be in horizotal")

    #handling error in choice input if user input some wrong character
    while True:

        #taking input from user
        c=input("\nEnter your choice: ")

        #depending on user choice running the condition
        if c=="1" or c=="2":
            break  #breaking the loop if the input is correct

        else:
            print("Enter either 1 or 2")
            continue   #asking again if the input is wrong

    print("Enter the path of images of which you want to make a collage")
    #taking input the images file to make collage

    image1 = input("Write your first image tittle with format :")

    #using os library to check if the file exist
    #it will remain in the loop unless the condition become true which happen when file succesfully open
    while os.path.exists(image1) == False:

            #printing a statement to let the user know
            print("File not Found")

            #taking input again unless he gave valid image path
            image1 = input("Write your  first image tittle with format :")

    image2 = input("Write your second image tittle with format :")

    #using os library to check if the file exist
    #it will remain in the loop unless the condition become true which happen when file succesfully open
    while os.path.exists(image2) == False:

            #printing a statement to let the user know
            print("File not Found")

            #taking input again unless he gave valid image path
            image2 = input("Write your second image tittle with format :")

    #opening the images to work on
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    #Image is actually a three dimensional array containg height,width,channel
    #using numpy to convert image into three dimensional array which will manipulate later to make changes
    img1_data = np.array(img1)
    img2_data = np.array(img2)

    # taking height and width of first image from array
    height1 = img1_data.shape[0]
    width1 = img1_data.shape[1]

    # taking height and width of second image from array
    height2 = img2_data.shape[0]
    width2 = img2_data.shape[1]

    width = width1
    height = height1

    #cropping the height of first image if it is greater than the second
    if height1 > height2:

        #crooping image 1 by ending the height of image 1 in image matrix to the the height of image 1
        img1 = img1_data[:height2,:]
        img1 = Image.fromarray(img1)

        #adding the heights for collage
        n_height = height2+height2
        #adding width
        n_width = width1+width2
        height = height2

    #cropping the height of second image if it is greater than the first
    elif height2 > height1:

        #crooping image 2 by ending the height of image 2 in image matrix to the the height of image 1
        img2 = img2_data[:height1,:]
        img2 = Image.fromarray(img2)

        #adding height for collage
        n_height = height1+height1

        #adding width
        n_width = width1+width2
        height = height1

    #cropping the width of first image if it is greater than the second
    elif width1 > width2:

        #crooping image 1 by ending the width of image 1 in image matrix to the the width of image 2
        img1 = img1_data[::width2]
        img1 = Image.fromarray(img1)

        #adding heights
        n_height = height1+height2
        n_width = width2+width2

        #adding width
        width = width2

    #cropping the width of second image if it is greater than the first
    elif width2 > width1:

        #crooping image 2 by ending the width of image 2 in image matrix to the the width of image 1
        img2 = img2_data[:,:width1]
        img2 = Image.fromarray(img2)

        #adding heights
        n_height = height1+height2

        #adding width
        n_width = width1+width1
        width = width1

    #adding the height and width of the images to create a new image
    else:
        n_height = height1+height2
        n_width = width1+width2

    # working on vertical collage
    if c =="1":
        #creating a new white image of new width and height of first image
        img = Image.new(mode="RGB",size=(n_width,height),color="white")

        #pasting the first image on the new image
        img.paste(img1)

        #pasting the second image on the new image after the width of first image
        img.paste(img2,(width,0))

    if c=="2":
        #creating a new white image of new height and width of first image

        img = Image.new(mode="RGB",size=(width,n_height),color="white")

        #pasting the first image on the new image
        img.paste(img1)

        #pasting the second image on the new image after the height of first image
        img.paste(img2,(0,height))

    #spliting the file name and format
    path = image1.split(".")

    print("\nYour image is ready\n")

    #asking user if he want the format to be change
    #using TryExcept block fro error handling
    try:

        option = int(input("\nDo you want to change the format or go with the source format:\n\'1 for YES\'\n\'2 for No\'\nEnter : "))

    except:
        print("Enter either 1 or 2")
        option = int(input("Do you want to change the format or go with the source format:\n\'1 for YES\'\n\'2 for No\'\nEnter : "))

    #if user choose the option (1) which is to change the format
    if(option ==1):

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
    img.save(f"{filename}.{format}")
    print("\nFile has been saved")