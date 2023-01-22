# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print ("Start!")
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             ItemSpecial1(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             ItemSpecial_const(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             ItemSpecial_const(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             ItemSpecial2(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             ItemSpecial2(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             ItemSpecial2(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             ItemSpecial3(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 5
    max_quality = 50
    step = 1
    min_quality = 0
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
        if len(sys.argv)>2:
            max_quality = int(sys.argv[2])
            if len(sys.argv)>3:
                step = int(sys.argv[3])
                if len(sys.argv)>4:
                    min_quality = int(sys.argv[4])
                    
    print("Parameters used in current calculation are : \
          days {}, max quality {}, min quality {}, step {}". \
              format(days, max_quality, min_quality, step) )  
              
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items=items, 
                   max_quality=max_quality, 
                   step=step, 
                   min_quality = min_quality).update_quality()


