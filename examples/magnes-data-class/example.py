#!/usr/bin/env python3 -d
"""!
    Example
    =======

    @author C. Mangiante
    @copyright Magnes AG, (C) 2024.
"""
import dataclasses

from magnesDataClass import magnes_dataclass


@magnes_dataclass
class Point:
    x: float
    y: float
    z: float


# @magnes_dataclass
# class Rectangle:
#    l1: float
#    l2: float
#
#    def get_area(self):
#        return self.l1 * self.l2
#
#
# @magnes_dataclass
# class Circle:
#    radius: float = dataclasses.field(default=5.6)
#
#
# @magnes_dataclass
# class Line:
#    start: Point = dataclasses.field(default_factory=Point)
#    stop: Point = dataclasses.field(default_factory=Point)


def main():
    # point is a valid data class
    p = Point(4.3, 4.5, 2.4)

    # we can iterate over the data fields
    for i, coord in enumerate(p):
        print(f"Coordinate n.{i}: {coord}")

    # rectangle is not valid, it has methods
    # r = Rectangle(2.2, 3.3)

    # circl is not, it has defaults
    # c = Circle()


if __name__ == "__main__":
    main()
