vectors = []
vectors2 = []

def setup():
    size(600, 600)
    noFill()

    for k in range(0, 6):#6 koordinatenpaare
        vectors.append(PVector(random(width),random(height)))
        
    for l in range(0,len(vectors)):
        v = vectors[l]
        ellipse(v.x, v.y, 30, 30)
        

    beginShape()
    for m in range(0,len(vectors)-3):# for m in range(0,len(vectors)): verbindet alle 
        V = vectors[m]
        vertex(V.x, V.y)
    endShape(CLOSE)
    print(vectors)
    






