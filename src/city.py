"""Module for base city class."""

import networkx as nx

class City(nx.DiGraph):
    """Base class for a city represented by NetworkX Directed Graph class.

    Parameters
    ----------
    name : string
        Name of the city.

    """
    def __init__(self, name=None):
        super(City, self).__init__()
        self.name = name

    def add_vertex(self, index, coordinates, name=None):
        """Add a junction of roads as a node to the graph.

        A junction is defined where three or more roads meet.

        Parameters
        ----------
        index : int
            Index of the junction starting from 1.

        coordinates : tuple of float
            A tuple of x and y coordinates of the junction respectively.

        name : string, optional
            Name of the junction.

        """

        self.add_node(index, coordinates=coordinates, name=name)

    def add_route(self, vertex_A, vertex_B, lanes, length, threshold=0,
                  special_A=False, special_B=False, time_B=None,
                  speed_limit=30, car_density=None):
        """Add a route between one vertex to another.

        This is a directed edge so adding route from A to B does not create
        route from B to A.

        Parameters
        ----------
        vertex_A : node
            The entry point of the route.

        vertex_B : node
            The exit point of the route.

        lanes : int
            The number of lanes present in the route from vertex A to B.

        length : float
            Total length of the route.

        threshold : int
            The minimum number of difference of influx and outflux of vehicles
            in the route. If the difference is below the threshold value, then
            the route is not considered for one way evaluation.

        special_A : bool, default False
            True if the route has Type A special buildings alongside it.

        special_B : bool, default False
            True if the route has Type B special buildings alongside it.

        time_B : List of tuples
            A list of time ranges when the special_B buildings have vehicle
            incoming or outgoing as tuples.

        speed_limit : int
            The speed limit of vehicles in the route. Value in km/hour.

        car_density : float
            The maximum number of cars per unit of length (km). This value
            denotes the maximum value of the parameter threshold.

        """
        self.add_edge(vertex_A, vertex_B, lanes=lanes, length=length,
                      threshold=threshold, special_A=special_A,
                      special_B=special_B, time_B=time_B,
                      speed_limit=speed_limit, car_density=car_density)
