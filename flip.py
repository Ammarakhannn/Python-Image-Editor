#flipping the image

def flip():

    #importing PIL libaray for open and drawing image
    from PIL import Image,ImageDraw

    #importing numpy to get array that can manipulate to get results
    import numpy as np

    #importing os for error handling later in the program
    import os

    #taking path of image with format from user
    #image must be in directory
    path = input("Write your image tittle with format :")

    #using os library to check if the file exist
    #it will remain in the loop unless the condition become true which happen when file succesfully open
    while os.path.exists(path) == False:

        #printing a statement to let the user know
            print("File not Found, (e.g  = image.jpg)")

        #taking input again unless he gave valid image path
            path = input("Write your image tittle with format :")

    #opening the image to flip
    img = Image.open(path)

    #changing the image in matrix
    img_data = np.array(img)

    #from image matrix taking the no of rows of image
    row = img_data.shape[0]

    #from image matrix taking the no of columns of image
    col = img_data.shape[1]

    #taking all the rows of the image matrix in reverse order and columns as before
    img = img_data[row-1: :-1, :]

    #saving the flipped image
    myimg = Image.fromarray(img)

    #spliting the file name and format
    path = path.split(".")

    #storing the format of the input image incase user don't want the format to be change

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
    myimg.save(f"{filename}.{format}")
    print("\nFile has been saved")
