from tri import Tri 
def setup():
    tri1 = Tri(PVector(10,10),PVector(30,30),PVector(10,30))
    tri2 = Tri(tri1.p3,tri1.p2,PVector(50,50))
    
    tri1.display_lines(0)
    tri2.display_lines(0)
    
    tri1.display_ellipse(255)
    # executed once
#def draw():
    # executed all the time
    
    
