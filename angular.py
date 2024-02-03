import math
import sys
from collections import deque


class Point:
    """
        Point class is used to represent points on the plane
    """

    def __init__(self, x, y):
        """

        :param x: The x value on the plane
        :param y: The y value on the plane
        """
        self.angle = xytoangle(x, y)
        self.x = x
        self.y = y

    def __cmp__(self, other):
        """

        :param other: The other point object
        :return: 1 if the angle is greater than the other, 0 if equal,
        -1 if less.
        """
        if self.angle < other.angle:
            return -1
        elif self.angle == other.angle:
            return 0
        else:
            return 1

    def __str__(self):
        return f"{self.x}, {self.y}"


def timsort(unsortedlist, minrun=32):
    """
    Sorting algorithm

    :param unsortedlist:
    :param minrun: min value of run before adding to stack
    :return: sorted list
    """
    runstack = deque()
    currrun = []
    for i in range(unsortedlist):
        if len(currrun) > 0 and unsortedlist[i] < currrun[-1]:
            currrun = insertionsort(currrun, unsortedlist[i])
            if len(currrun) >= minrun:
                runstack.appendleft(currrun)
                currrun = []
        else:
            currrun.append(unsortedlist[i])
        # I still don't know how to do the invariance but it would go here lol


def timsortmerge(runstack):
    """
    This function is used to merge the runstack produced by timsort

    :param runstack: the stack of runs
    :return: merged list
    """
    while True:
        tempstack = deque()
        while len(runstack) >= 2:
            a = runstack.popleft()
            b = runstack.popleft()
            tempstack.appendleft(bottomupmerg(a, b))
        while len(tempstack) > 0:
            runstack.appendleft(tempstack.popleft())
        if len(runstack) == 1:
            return runstack.popleft()


def bottomupmerg(lista, listb):
    """
    This function is used to merge two already sorted lists

    :param lista:
    :param listb:
    :return: merged list
    """
    n = len(lista) + len(listb)
    newlist = []
    i = 0
    j = 0
    for k in range(n):
        if j > len(listb) - 1:
            newlist.extend(lista[i:])
            return newlist
        if i > len(lista) - 1:
            newlist.extend(listb[j:])
            return newlist
        if lista[i] > listb[j]:
            newlist.append(listb[j])
            j += 1
        elif lista[i] < listb[j]:
            newlist.append(lista[i])
            i += 1
        else:
            newlist.append(lista[i])
            newlist.append(listb[j])
            i += 1
            j += 1
    return newlist


def insertionsort(list, insertion):
    """
    Standard insertion sort helper for timsort

    :param list: the list to scan
    :param insertion: the thing to insert
    :return: modified list
    """
    for i in range(len(list)):
        if insertion < list[i]:
            return insertatlistindex(list, insertion, i)
    return list.extend([insertion])


def insertatlistindex(list: [], insertion, index):
    """
    Inserts element at list index

    :param list: original list
    :param insertion: the element to insert
    :param index: the index to insert at
    :return: the modified list
    """
    templist = list[:index]
    templist.append(insertion)
    templist.extend(list[index:])
    return templist


def xytoangle(x, y):
    """
    Used to convert x,y coordinates to degrees

    :param x: The x value of the point
    :param y: The y value of the point
    :return: The angle of the point with respect to 0 (0 - 360)
    """
    theta = math.acos(x / (math.sqrt(x * x + y * y)))
    if y < 0:
        theta = 2 * math.pi - theta
    return theta


def getinput(inputfilepath):
    """

    :param inputfilepath: the input file
    : return the point array or null if no file found
    """
    try:
        with open(inputfilepath, 'r') as f:
            points = []
            for i in range(int(f.readline())):
                xy = f.readline().split()
                points.append(Point(int(xy[0]), int(xy[1])))
        f.close()
        return points
    except FileNotFoundError:
        print("File not found")
        return


def main(inputfile):
    """

    :param inputfile: the file of points for the input
    """
    getinput(inputfile)


if __name__ == "__Main__":
    main(sys.argv[1])
