#!/usr/bin/env python

'''Buffer class to obtain buffer object from LineSegment2 of euclid library'''

from Libraries.euclidNEW import *

class Buffer_LineSegment2(Geometry):
    __slots__ = ['segment','side1','side2','c1','c2','size']
    def __init__(self, *args):
        if len(args) == 1:
          assert isinstance(args[0], LineSegment2)
          self.segment = args[0].copy()
          self.size=0.1
        elif len(args) == 2:
          assert isinstance(args[0],LineSegment2) and type(args[1])==float
          self.segment = args[0].copy()
          self.size = args[1]
        else:
            raise AttributeError('%r' % (args,))

        self.c1 = Circle(self.segment.p1,self.size)
        self.c2 = Circle(self.segment.p2,self.size)
        a=Line2(self.c1.c,self.segment.v.cross()).intersect(self.c1)
        b=Line2(self.c2.c,self.segment.v.cross()).intersect(self.c2)
        self.side1 = a.p1.connect(b.p1)
        self.side2 = a.p2.connect(b.p2)

    def _intersect_line2(self, other):
        if self.c1.intersect(other) or self.c2.intersect(other) or\
            self.side1.intersect(other) or self.side2.intersect(other):
            return True
        else:
            return False

    # def __repr__(self):
    #     return 'Buffer_LineSegment2(%,%,%,%)' \
    #         (self.c1, self.c2, self.side1, self.side2)