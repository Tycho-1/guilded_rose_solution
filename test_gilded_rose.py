# -*- coding: utf-8 -*-
import unittest

from gilded_rose import *


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [ItemSpecial3("foo", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals(4, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
