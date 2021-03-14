import os

def extract_place(filename):
    return filename.split("_")[1]


def make_place_directories(places):
    for place in places:
        os.mkdir(place)


def organize_photos(directory):
    # First, extract place names
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    # Second, make place directories
    make_place_directories(places)

    # Finally, move files to directories
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


organize_photos("Photos")