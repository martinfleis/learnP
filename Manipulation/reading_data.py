'''
Reading shapefile using geopandas, adding column, calculating simple geometrical
value (area) and saving back into the file.
'''

# import geopandas and matplotlib.
import geopandas as gpd
import matplotlib.pyplot as plt


# set path to shapefile
path = "/Users/martin/Strathcloud/Personal Folders/Test data/Royston/buildings.shp"
buildings = gpd.read_file(path)  # load file into geopandas
# check type of buildings variable
type(buildings)
# show first lines of dataframe
buildings.head()
# it should plot file with matplotlib, but it is not working for some reason. but no error
buildings.plot(column='area')
# save plot to file
plt.savefig('map.pdf')
# check crs of shapefile
buildings.crs
# select only first ten lines from shp
selection = buildings[0:10]
# print areas of polygons for first 10 lines. row 'geometry' is probably gpd thing
for index, row in selection.iterrows():
    building_area = row['geometry'].area
    print("The area of building id {0} is {1:.1f} square meters.".format(index, building_area))
# define new column called 'area'
buildings['area'] = None
# fill new column with the value of area, iterating over rows one by one
for index, row in buildings.iterrows():
    buildings.loc[index, 'area'] = row['geometry'].area
# get min and max values
max_area = buildings['area'].max()
min_area = buildings['area'].min()
# print values into text using placeholders. .2f means 2 numbers behind 0.
print("Smallest building in Royston is {0:.2f} square meters large, while the biggest is {1:.2f} square meters large.".format(min_area, max_area))

mean_area = buildings['area'].mean()
mean_area

# save dataframe back to file
buildings.to_file(path)
