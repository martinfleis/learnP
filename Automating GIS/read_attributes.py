from shapely.geometry import Point, LineString, Polygon


def getCentroid(geom):
    return(geom.centroid)


def getArea(geom):
    return(geom.area)


def getLength(geom):
    if type(geom) == LineString:
        return(geom.length)
    elif type(geom) == Polygon:
        return(geom.exterior.length)
    else:
        print('Invalid geometry.')

poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

print(getCentroid(poly))
print(getCentroid(line2))
print(getArea(poly))
print(getArea(line2))
print(getLength(poly))
print(getLength(line2))

point1 = Point(2.2, 4.2)
print(getCentroid(point1))
print(getArea(point1))
print(getLength(point1))
