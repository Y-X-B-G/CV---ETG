""" Opencv and numpy library import"""
from collections import defaultdict
from copy import deepcopy
import os
import cv2 as cv
import numpy as np


class BulkImageLoader():
    """ 
    This class loads all images in a folder and all subfolders 
    and organizes them into a dict by the name of the folder or 
    subfolder that contained the images
    """
    #longestImageDim: tuple[int, int] = (0,0) #If I need to get the dim of the largest possible length and width
    #shortestImageDim: tuple[int, int] = (0,0) #If I need to get the dim of the smallest lengths and width
    keys: list[str] = []
    dictImage: defaultdict[str, list[np.ndarray]] = defaultdict(list)

    def __init__(self, file_path: str):
        """Take an arugment of the folder you store your image in and returns all image files 
            @Arguments: file path of the folder that contains the images: string
            @Returns: dictionary of image: dict
        """
        #Finds all the files in the file path you specify
        for root, dirs, files in os.walk(file_path, topdown=True):
            for file in files:
                path: os.path = os.path.join(root, file)
                if os.path.exists(path):
                    image_data: np.ndarray = cv.imread(str(path))
                    if image_data is not None:
                        self.dictImage[root].append(image_data)
                        if root not in self.keys:
                            self.keys.append(root)

    @property
    def get_all_images(self) -> defaultdict:
        """Returns a deep copy of our image set
            @Arguments: self
            @Returns: dictionary of image: dict
        """
        return deepcopy(self.dictImage)

    @property
    def get_keys(self) -> list[str]:
        """Returns a list of all keys
            @Arguments: self
            @Returns: List of all keys: list[str]
        """
        return deepcopy(self.keys)

    def get_image(self, key, index) -> list[np.ndarray]:
        """Gets a single image"""
        assert key in self.keys, "This is not a valid key"
        assert index < len(self.dictImage[key]), "This is not a valid index"
        return deepcopy(self.dictImage[key][index])

def main():
    """Main testing function"""
    print("This should only run when its being tested")
    test: BulkImageLoader = BulkImageLoader("DUMPsprites")
    print(test.get_keys)
    print(test.get_image(test.get_keys[0], 0))

if __name__ == "__main__":
    main()
