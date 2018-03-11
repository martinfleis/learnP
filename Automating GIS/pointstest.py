from shapely.geometry import Point, LineString, Polygon

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)

point_type = type(point1)
print(point1)
print(point3D)
print(type(point1))

point_coords = point1.coords
type(point_coords)

xy = point_coords.xy
x = point1.x
y = point1.y

print(xy)
print(x)
print(y)

points_dist = point1.distance(point2)
print('Distance between the points is {0:.2f} decimal degrees'.format(points_dist))

line = LineString([point1, point2, point3])
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
print(line)

lxy = line.xy
print(lxy)

line_x = lxy[0]
line_y = line.xy[1]
print(line_x)
print(line_y)

l_lenght = line.length
l_centorid = line.centroid
centroid_type = type(l_centorid)
print('Lenght of our line is {0:.2f}'.format(l_lenght))
print('Centroid is: ', l_centorid)
print('Type of the cetroid:', centroid_type)

poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])
poly_type = poly.geom_type
poly_type2 = type(poly)
print(poly)
print(poly2)
print("Geometry type as text:", poly_type)
print("Geometry how Python shows it:", poly_type2)

world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 90)]]
world = Polygon(shell=world_exterior)
world_has_hole = Polygon(shell=world_exterior, holes=hole)
print(world)
print(world_has_hole)
type(world_has_hole)

world_centroid = world.centroid
world_area = world.area
world_bbox = world.bounds
world_ext = world.exterior
world_ext_lenght = world_ext.length

print('Centroid is:', world_centroid)
print('Area:', world_area)
print('Bounding box:', world_bbox)
print('Exterior:', world_ext)
print('Exterior lenght:', world_ext_lenght)

world_hull = world.convex_hull.area
