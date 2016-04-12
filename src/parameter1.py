from __future__ import division

def distance_between_cars(speed, response_time=1):
	'''Returns the average distance between 2 vehicles.

	Parameters
	==========

	speed : Speed in km/hr units
	response_time : Response time to be given in seconds.
	    Assumed to be 1 second for our purpose.

	Returns
	=======

	min_distance : a float value in kms corresponding to the minimum safe distance between
	two vehicles given a path with specified speed limit and a response time.

	'''
	speed_units = (5 * speed) / 18
	# the minimum safe distance needed to avoid any mishap
	min_distance = speed_units * response_time  
    return min_distance/1000

def density_of_cars(route, cars=None):
	'''Calculates the density of cars on a given route.

    Parameters
    ==========

    route : the route on which we are interested to measure this feature.

    cars : optional argument corresponding to the number of cars on the route

    Output
    ======

    car_density : returns a float value
        If the number of cars are not specified, the threshold value for the route
        is returned. In all other cases, the value returned is the number of cars
        per km running on the concerned path.

	'''
	path_length = route.length
	speed = route.speed_limit
	lanes = route.lanes
    # The avaerage length between 2 cars is assumed to be 4.5 m
    avg_length = 0.0045
    if cars is None:
        min_distance = distance_between_cars(speed)
        total_length  = min_distance + avg_length
        # Just to make the logic clearer
        car_density = ((path_length / total_length) * lanes)/ path_length
    else:
    	car_density = cars / path_length
    return car_density

def _threshold_check(car_density, threshold):
	'''Compares particular car density level with the threshold value.

	Reeturns True if the number of cars on a paritcular road is more than
	the threshold set for the particular road.

	'''
	if threshold <= cars_density:
		return True
	else:
		return False

def check_parameter1(route):
	'''Checks whether the car density on a path is more than the threshold
	value or not. 

	Parameter
	=========
	route : the concerned route

	'''
	car_den = route.car_density
	threshold = route.threshold
	parameter = route.parameter1
	if _threshold_check(car_dens, threshold):
		parameter = True
	else:
		parameter = False
