from __future__ import division

from src.fuzzy import get_parameter1
from src.alternatives import get_parameter2

def csv_data_reader(self, filename):
    columns = defaultdict(list)
    with open(filename) as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)
    return columns

def data(columns, x, y):
	target = 0
	for i in len(columns[0]):
        if columns[2][i] == 1:
    	    source = columns[0][i]
    	    destination = columns[1][i]
    	else:
    		source = columns[1][i]
    	    destination = columns[0][i]
    	
	    if source == x and destination == y and columns[3][i] == 'Sat':
	        target = columns[12][i+3]
            columns[22][i+3] == columns[23][i+3] = None
    dataset = list(list(columns[22][i], columns[23][i]) if all(columns[22][i], columns[23][i]) is not None for i in len(columns[0])):
    return (dataset, target)

def process(city, traffic_data_filename):
    new_city = city.copy()
    columns = csv_data_reader(str(traffic_data_filename))
    for i in len(columns[0]):
    	if columns[2][i] == 1:
    	    source = columns[0][i]
    	    destination = columns[1][i]
    	else:
    		source = columns[1][i]
    	    destination = columns[0][i]
    	route = new_city[source][destination]
    	car_density = route['car_density']
        car_density = density_of_cars(new_city, (source, destination), columns[3][i])
        
        if not route['special_A']:
        	parameter1 = get_parameter1(new_city, (source, destination))
        	parameter2 = get_parameter2(new_city, (source, destination))
        	# a method to write 2 columns in the csv with column index 22, 23
        	with open(filename) as f:
                writer = csv.writer(f)
                for row in reader:
                for (i,v) in enumerate(row):
                    columns[i].append(v)
    x, target = data(columns)
    y = NN_model(x, target)
    print y
    # data method to extract data
    # target method to determine target
    #

    # use source destination as shown above
    # and color the graph accordingly 
    # return new_city which has edges colored green and destination nodes colored red
