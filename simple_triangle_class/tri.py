class Tri(object):
    p1 = PVector(0,0)
    p2 = PVector(0,0)
    p3 = PVector(0,0)
    w = 10
    h = 10
    def __init__(self, _p1, _p2, _p3):
        #constructor
        self.p1 = _p1
        self.p2 = _p2
        self.p3 = _p3

    def display_lines(self, col):
        # method of class display
        fill(col)
        beginShape()
        vertex(self.p1.x,self.p1.y)
        vertex(self.p2.x,self.p2.y)
        vertex(self.p3.x,self.p3.y)
        endShape(CLOSE)
    def display_ellipse(self, col):
        # method of class display
        fill(col)
        ellipse(self.p1.x, self.p1.y, self.w, self.h)
        ellipse(self.p2.x, self.p2.y, self.w, self.h)
        ellipse(self.p3.x, self.p3.y, self.w, self.h)
