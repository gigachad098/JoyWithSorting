import unittest
import angular
from collections import deque

class TestSortingMethods(unittest.TestCase):

    def testBottomUpMerge(self):
        lista = [1,2,3,4,5,6]
        listb = [3,4,5,6]
        actual = angular.bottomupmerg(lista,listb)
        expected = [1,2,3,3,4,4,5,5,6,6]
        self.assertEqual(actual, expected)

    def testInsertionAtIndex(self):
        templist = [1,2,3,4,5,6]
        element = 4
        index = 2
        self.assertEqual(
            angular.insertatlistindex(templist, element, index),
            [1,2,4,3,4,5,6])

    def testInsertionSort(self):
        list = [1,2,4,5,6]
        element = 3
        self.assertEqual(
            angular.insertionsort(list, element),
            [1,2,3,4,5,6]
        )

    def testTimsortMerge(self):
        listoflist = deque()
        listoflist.appendleft([1,2,3])
        listoflist.appendleft([4,5,6])
        listoflist.appendleft([7,8,9])
        self.assertEqual(
            angular.timsortmerge(listoflist),
            [1,2,3,4,5,6,7,8,9]
        )