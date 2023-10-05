# -*- coding: utf-8 -*-

from enum import Enum

class Products(Enum):
    BackstagePass = "Backstage passes to a TAFKAL80ETC concert"
    Sulfuras = "Sulfuras, Hand of Ragnaros"
    Brie = "Aged Brie"
    Other = ""


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self, max_quality=50, quality_cutoff_short=5, quality_cutoff_long=10):
        for item in self.items:
            if item.name != Products.Brie.value and item.name != Products.BackstagePass.value:
                if item.name != Products.Sulfuras.value:
                    self.decrement_quality(item)
            else:
                self.increment_quality(item, max_quality)
                if item.quality < max_quality:
                    if item.name == Products.BackstagePass.value:
                        if item.sell_in < quality_cutoff_long + 1:
                            self.increment_quality(item, max_quality)
                        if item.sell_in < quality_cutoff_short + 1:
                            self.increment_quality(item, max_quality)
            if item.name != Products.Sulfuras.value:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self.expired(max_quality, item)

    def increment_quality(self, item, max_quality):
        if item.quality < max_quality:
            item.quality = item.quality + 1

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def expired(self, max_quality, item):
        if item.name != Products.Brie.value:
            if item.name != Products.BackstagePass.value:
                if item.quality > 0:
                    if item.name != Products.Sulfuras.value:
                        self.decrement_quality(item)
            else:
                item.quality = item.quality - item.quality
        else:
            self.increment_quality(item, max_quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
