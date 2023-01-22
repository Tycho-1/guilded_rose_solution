# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items, max_quality=50, min_quality=0, step=1):
        self.items = items
        self.max_quality = max_quality
        self.min_quality = min_quality
        self.step = step

    def update_quality(self):
        def adjust_quality():
            if (not isinstance(item, ItemSpecial1)) and (not isinstance(item, ItemSpecial2)):
                if item.quality > self.min_quality :
                    if not isinstance(item, ItemSpecial_const):
                        item.quality = item.quality - self.step
                    if isinstance(item, ItemSpecial3):
                        item.quality = item.quality - self.step                        
            else:
                if item.quality < self.max_quality:
                    item.quality = item.quality + self.step
                    if isinstance(item, ItemSpecial2):
                        if item.sell_in <= item.threshold_1:
                            if item.quality < self.max_quality:
                                item.quality = item.quality + self.step
                        if item.sell_in < item.threshold_2:
                            if item.quality < self.max_quality:
                                item.quality = item.quality + self.step
                                
        def decrease_sellin_days():
            if not isinstance(item, ItemSpecial_const):
                item.sell_in = item.sell_in - self.step         
                
        def adjust_quality_when_negative_sellin():
            if item.sell_in < self.min_quality :
                if not isinstance(item, ItemSpecial1):
                    if not isinstance(item, ItemSpecial2):
                        if item.quality > self.min_quality:
                            if not isinstance(item, ItemSpecial_const):
                                item.quality = item.quality - self.step
                                
                            if isinstance(item, ItemSpecial3):
                                item.quality = item.quality - self.step                                   
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < self.max_quality:
                        item.quality = item.quality + self.step
                        
        for item in self.items:
            adjust_quality()    
            decrease_sellin_days()
            adjust_quality_when_negative_sellin()



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemSpecial1(Item):
    """"Special item number 1 
        will increase the quality when more days pass    
    """


class ItemSpecial2(Item):
    """"Special item number 1 
        will increase the quality for specific day range 10 days to event and 5 days to event   
    """  
    def __init__(self, name, sell_in, quality, threshold_1=10, threshold_2=5):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality        
        self.threshold_1 = threshold_1
        self.threshold_2 = threshold_2


class ItemSpecial_const(Item):
    """"Special item will stay constant through time
        both quality and sell ni proce
    """


class ItemSpecial3(Item):
    """
    Special item numbe 3 ; it will decrease in quality twice as fast as the other items
    """

    
