from shapely.geometry import Point, LineString, Polygon


def createPointGeom(x_coord, y_coord):
    return(Point(x_coord, y_coord))

x = 2.1
y = 3.5
pointA = createPointGeom(x, y)
print(pointA)


def createLineGeom(coords):
    return(LineString(coords))


carabody = [(2.1, 3.5), (6.7, 8.9)]
cara = createLineGeom(carabody)
print(cara)


def createPolyGeom(body):
    if type(body) == list:
        return(Polygon(body))
    else:
        print('Wrong geometry.')


polybody = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]
polypoints = createPolyGeom(polybody)
print(polypoints)
