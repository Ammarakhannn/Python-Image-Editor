#cropping the image

def crop():
     #importing PIL libaray for open and drawing image
    from PIL import Image,Image

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
            path = input("\nWrite your image tittle with format :")

    #opening the image using Image.open from the library PIL
    img = Image.open(path)

    #opening the image in array
    img_data = np.array(img)

    #Taking height and width from array
    height = img_data.shape[0]
    width = img_data.shape[1]

    #telling user the height of users image
    print("\nThe actual height of the image is",height,"and actual width of the image is", width)

    #giving 4 options to user to crop the image
    print("\nSelect from the options below from where you want to crop the image")
    print("\n1.From left and bottom\n2.From right and top\n3.from top and bottom\n4.from left and right")

    #handling error in users choice
    while True:
        #taking the input of choice
        choice=input("Enter your choice: ")

        #checking that the user has choose the options above or not
        if choice == "1" or choice=="2" or choice=="3" or choice=="4" :
            break        #breaking the loop if choice is correct

        else:
            #if user input other than the choices then asking again
            print(" please choose 1 or 2 try again")
            continue       #countinuing the loop until user input the right


    #error handling in input of height and width if choice is one or two
    if choice == "1" or choice == "2":

        while True:

            try:
                #taking input heigth and width from user to crop the image
                new_h = int(input("Enter the height of the image: "))
                new_w = int(input("Enter the width of the image: "))

                #handling error if user input height greater than the actual height
                if new_h>height:
                    #telling user that he is exceeding the actual height
                    print("You are exceeding the actual height try again")

                    while True:

                        #taking input again if height is greater
                        new_h = int(input("Enter the height of the image: "))

                        # if again height is greater asking again
                        if new_h > height:
                            continue

                        #breaking the loop if input height is correct
                        else:
                            break

                #handling error if user input width greater than the actual width
                if new_w > width:

                    #if input width is greater telling user to try again
                    print("\nYou are exceeding the actual width try again")

                    #asking for width
                    while True:
                        new_w = int(input("\nEnter the width of the image: "))

                        #asking again if width is greater
                        if new_w > width:
                            continue

                        #breaking loop if width is correct
                        else:
                            break
                    break

                #breaking the loop if heigth and width are correct
                else:
                    break

            #handling error if user input value other than digit
            except ValueError:
                #asking user to try agin
                print("Invalid input please enter only digits")
                continue

    #cropping the image
    if choice == "1":

        #cropping the image to the heigth and width given by user from left and bottom ending the array upto desire heigth and width
        new_image=img_data[:new_h,:new_w]

        #saving the cropped image
        myimg=Image.fromarray(new_image)
    #cropping
    if choice == "2":

        #cropping the image to the heigth and width given by user from right and top starting the array upto desire heigth and width
        new_image = img_data[height-new_h:,width-new_w:]

        #saving the cropped image
        myimg = Image.fromarray(new_image)

    #handling error in choice 3 in height
    if choice == "3":
        while True:
            try:

                #taking input heigth and width from user to crop the image
                new_h = int(input("\nEnter the height of the image: "))

                #handling error if user input height greater than the actual height
                if new_h > height:

                    #telling that input height is greater
                    print("You are exceeding the actual height try again")
                    continue
                #breaking the loop if it is correct
                else:
                    break
                break

            #handling error if user input characters other than digits
            except ValueError:

                print("Invalid input please enter only digits")
                #continuing the loop for input
                continue

    #crooping the image
    if choice == "3":

        #cropping the image to the heigth given by user from top and bottom
        new_image = img_data[(height-new_h)//2:(height+new_h)//2,:width]

        #saving the cropped image
        myimg = Image.fromarray(new_image)

    #Handling error in choice 4
    if choice == "4":
        while True:
            try:

                #taking input width from user to crop the image
                new_w = int(input("\nEnter the width  of the image: "))

                #handling error if user input height greater than the actual width
                if new_w > width:

                    #telling the user that input width is greater and asking again
                    print("You are exceeding the actual width try again")
                    continue

                #breaking the loop if input is correct
                else:
                    break
                break

            #handling error if user input other than digits
            except ValueError:

                #asking again for width
                print("\nInvalid input please enter only digits")
                continue

    #cropping the image
    if choice == "4":

        #cropping the image to the width given by user from left and right
        new_image = img_data[:height,(width-new_w)//2:(width+new_w)//2]

        #saving the cropped image
        myimg = Image.fromarray(new_image)

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
    myimg.save(f"{filename}.{format}")
    print("\nFile has been saved")

