# A program that organizes photos by their location title


# TO DO: - Add Path so that the program runs from any place
#          and not only on 'organize_photos'
#         -Eliminate global variable - pass them as arguments to functions



import os
import sys

if len(sys.argv) < 2:
    print("\n\tUsage: python3 organize_photos2.py [Directory]"
          "- copy phrase text\n\n"
          "\tif you are using Frodriguez9's repository [Directory] = Photos\n")
    sys.exit()

directory_to_be_manipulated = sys.argv[1]


def extract_place(filename):
    return filename.split("_")[1]


def make_place_directory():
    for file in originals:
        try:
            os.mkdir(extract_place(file))
            places.append(extract_place(file))
        except FileExistsError:
            continue


def move_files():
    for place in places:
        for file in originals:
            if extract_place(file) == place:
                os.rename(file, os.path.join(place, file))
            else:
                continue


                
def organize_photos(directory):
    os.chdir(directory)
    global originals
    global places
    places = []
    originals = os.listdir()
    make_place_directory()
    move_files()


if __name__ == '__main__':
    organize_photos(directory_to_be_manipulated)

''' Use this in the command line to reorganize the 'Photos' directory
as it was before running this program (cd to the Photos directory)

$ mv ./Berlin/*.jpg .; rmdir ./Berlin; mv ./Brooklyn/*.jpg .;
rmdir ./Brooklyn; mv ./Cancun/*.jpg .; rmdir ./Cancun; mv ./Firenze/*.jpg .;
rmdir ./Firenze; mv ./Kyoto/*.jpg .; rmdir ./Kyoto; mv ./Oahu/*.jpg .;
rmdir ./Oahu; mv ./Scotland/*.jpg .; rmdir ./Scotland; mv ./Yosemite/*.jpg .;
rmdir ./Yosemite'''
