import argparse

def get_input_args():

    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """

    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type=str, default='pet_images',
                    help = 'path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', choices=['resnet', 'alexnet', 'vgg'], 
                    help = 'type of architecture for model')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                    help = 'path to file of dognames')
    
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    return parser.parse_args()


if __name__=="__main__":
    args = get_input_args()

    print(f'Path to image directory: {args.dir}')
    print(f'Using {args.arch} architecture')
    print(f'Path to dogfile: {args.dogfile}')









