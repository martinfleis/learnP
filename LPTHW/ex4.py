# set nr of cars
cars = 100
# define space
space_in_a_car = 4
# amount of drivers
drivers = 30
# number of passengers
passengers = 90
# how many cars will stay
cars_not_driven = cars - drivers
# how many cars will ride
cars_driven = drivers
# how many people will fit
carpool_capacity = cars_driven * space_in_a_car
# how many people will be in each car approx.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
