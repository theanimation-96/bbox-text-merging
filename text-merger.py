__title__ = "Text Merger"
__author__ = "Animesh Mandal"
__copyright__ = "Copyright (C) 2021 Animesh Mandal"

import math

TOLERANCE = 50
"""
Tolerance can be vary according to the inclination or slant level of the image. But I am assuming that the input image
have 0deg orientation or minimal orientation.
if image is not aligned(perpendicular) then it might happen that the text merging is not working properly.
TOLERANCE should be less than the difference between pixels of two lines.
"""


class inLineText:
    def __init__(self, bbox, listOfCenterCords, listOfUniqueCord, TextAndCenter, TEXT, bounding_box):
        self.bbox = bbox
        self.listOfCenterCords = listOfCenterCords
        self.listOfUniqueCord = listOfUniqueCord
        self.TextAndCenter = TextAndCenter
        self.TEXT = TEXT
        self.bounding_box = bounding_box

    @staticmethod
    def getLines(bounding_box):
        # Main method, just call this function and pass your bounding boxes with text #
        """
        merging all the methods here and calling at once for getting text-lines from an image
        @param bounding_box: bounding boxes and text.
        @return: text-line from the image, text-line from left-to-right sequence.
        """
        listOfCenterCords, TextAndCenter = inLineText.findCenterCord(bounding_box)
        unique_cords = inLineText.findNearerBox(listOfCenterCords)
        TEXT = inLineText.getSingleLineText(unique_cords, TextAndCenter)
        sort_lines = inLineText.SortLineText(TEXT)
        return [x[1] for x in sort_lines]

    @staticmethod
    def findCenterCord(bbox):
        """
        This will calculate the left-center of the bounding box, this will give us a common coordinate for horizontal
        text that lies in a line within the width of the image.
        @param bbox: bounding box and text
        @return: a list of center cords and a list with text, center and coordinates of left-top for sorting the text
        to left-to-right(horizontally) and top-to-down(vertically).
        """
        listOfCenterCords = []
        TextAndCenter = []
        for enum, box in enumerate(bbox):
            text = box[2]
            tl = box[0]
            tx, ty = tl[0], tl[1]
            br = box[1]
            bx, by = br[0], br[1]
            H = by - ty
            center = ty + (H / 2)
            listOfCenterCords.append(center)
            TextAndCenter.append([text, center, [tx, ty]])

        return [listOfCenterCords, TextAndCenter]

    @staticmethod
    def findNearerBox(listOfCenterCords):
        """
        The function will loop through the center cords for twice and it will find the matching coordinates with each
        other with a tolerance of 10-pixels and put it in a key-value manner in the dictionary.
        then it will again loop through the dictionary values and will find the unique values of the center cords.

        @note - tolerance of 10 px is there due to variation of the text boxes
        @param listOfCenterCords: list of the center coordinates.
        @return: unique list of the center coordinates.
        """
        dicts = {}
        unique_center = []
        for num1 in listOfCenterCords:
            for num2 in listOfCenterCords:
                if math.isclose(num1, num2, abs_tol=TOLERANCE):
                    dicts[num1] = num2

        for key in dicts:
            unique_center.append(dicts[key])

        return list(set(unique_center))

    @staticmethod
    def getSingleLineText(listOfUniqueCord, TextAndCenter):
        """
        This function will evaluate the text in a single line(horizontally) within the width of the image.
        @param listOfUniqueCord: unique coordinates of the center coordinates.
        @param TextAndCenter: a list with text, center and coordinates of left-top for sorting the text
        to left-to-right(horizontally) and top-to-down(vertically).
        @return:
        """
        TEXT = []
        for unique in listOfUniqueCord:
            line = []
            for tup in TextAndCenter:
                if math.isclose(unique, tup[1], abs_tol=TOLERANCE):
                    line.append([tup[2][0], tup[2][1], tup[0]])
            TEXT.append(line)
        return TEXT

    @staticmethod
    def SortLineText(TEXT):
        """
        this method will sort the the text in left-to-right (horizontally) and then top-to-bottom (vertically).
        @param TEXT: text with left-top coordinates
        @return: sorted text as it is on image, i.e. line-to-line text from left to right within the width of image.
        """
        sorted_T2D = []  # sorting the text in top-to-bottom
        for lines in TEXT:
            sorted_L2R = sorted(lines)  # sorting the text in left-to-right sequence.
            sorted_L2R = [[x[1], x[2]] for x in sorted_L2R]
            to_T2D = [min([x[0] for x in sorted_L2R]), " ".join([x[1] for x in sorted_L2R])]
            sorted_T2D.append(to_T2D)

        return sorted(sorted_T2D)
