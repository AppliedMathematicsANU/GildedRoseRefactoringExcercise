# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                quality_change = (
                    -item.quality if item.sell_in < 1
                    else 3 if item.sell_in < 6
                    else 2 if item.sell_in < 11
                    else 1
                )
            elif item.name == "Aged Brie":
                quality_change = 2 if item.sell_in < 1 else 1
            else:
                quality_change = -2 if item.sell_in < 1 else -1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
                item.quality = clamp(item.quality + quality_change, 0, 50)


def clamp(value, minimum, maximum):
    return min(maximum, max(minimum, value))


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
