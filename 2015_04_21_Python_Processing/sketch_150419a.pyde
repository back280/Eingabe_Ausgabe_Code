numberOfCircles = 6
circleList = []
circleSize = []
myColorList = []
myCanvasSize = []

def setup():

    noFill()
    stroke(255)

    for h in range(1):
        canvasBreite = int(random(600 / 2, 600))
        canvasHoehe = int(random(600 / 2, 600))
        myCanvasSize.append([canvasBreite, canvasHoehe])
        size(canvasBreite, canvasHoehe)
        print("myCanvasSize", myCanvasSize)

    for i in range(1):
        G = int(random(80, 200))
        myColorList.append(G)
        background(G)
        print("myColorList", myColorList)

    for j in range(0, numberOfCircles):  # fuer 0 bis sechs kreise
        x1 = int(random(50, width-50))  # x1 random zwischen 0 und breite
        y1 = int(random(50, height-50))  # y1 random zwischen 0 und hoehe
        circleList.append([x1, y1])  # anhang an liste
        print("circleList", circleList)  # liste ausgabe

    for k in range(0, len(circleList)):  # fuer null bis listenlaenge also 6
        breiteUndHoehe = int(random(10, 50))
        circleSize.append(breiteUndHoehe)
        print("circleSize", circleSize[k])
        ellipse(circleList[k][0], circleList[k][1], circleSize[k], circleSize[k])
        if k < len(circleList)-1:
            line(circleList[k][0], circleList[k][1], circleList[k+1][0], circleList[k+1][1])
            print("circleList", circleList[k])

