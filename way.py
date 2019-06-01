from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path



graph = Graph([
#Kyiv
("Kyiv", "Kharkiv",490), ("Kyiv", "Lviv", 540), ("Kyiv", "Dnipro", 475), ("Kyiv", "Zaporizhia", 515), ("Kyiv", "Odessa", 475), ("Kyiv", "Donetsk", 725), ("Kyiv", "KryvyiRih", 420),
("Kyiv", "Mykolaiv", 480), ("Kyiv", "Mariupol", 739), ("Kyiv", "Vinnytsia", 270), ("Kyiv", "Poltava", 345), ("Kyiv", "Chernihiv", 145), ("Kyiv", "Sumy", 335), ("Kyiv", "Rivne", 330),
("Kyiv", "IvanoFrankivsk", 605),
#Kharkiv
("Kharkiv", "Kyiv", 490), ("Kharkiv", "Lviv", 1025), ("Kharkiv", "Dnipro", 215), ("Kharkiv", "Zaporizhia", 300), ("Kharkiv", "Odessa", 700), ("Kharkiv", "Donetsk", 315), ("Kharkiv", "KryvyiRih", 370),
("Kharkiv", "Mykolaiv", 565), ("Kharkiv", "Mariupol", 420), ("Kharkiv", "Vinnytsia", 755), ("Kharkiv", "Poltava", 145), ("Kharkiv", "Chernihiv", 510), ("Kharkiv", "Sumy", 185),
("Kharkiv", "Rivne", 815), ("Kharkiv", "IvanoFrankivsk", 1090),
#Lviv
("Lviv", "Kyiv", 540), ("Lviv", "Kharkiv", 1025), ("Lviv", "Dnipro", 1010), ("Lviv", "Zaporizhia", 1090), ("Lviv", "Odessa", 780), ("Lviv", "Donetsk", 1260), ("Lviv", "KryvyiRih", 950),
("Lviv", "Mykolaiv", 800), ("Lviv", "Mariupol", 1315), ("Lviv", "Vinnytsia", 365), ("Lviv", "Poltava", 880), ("Lviv", "Chernihiv", 685), ("Lviv", "Sumy", 875), ("Lviv", "Rivne", 210),
("Lviv", "IvanoFrankivsk", 135),
#Dnipro
("Dnipro", "Kyiv", 480), ("Dnipro", "Kharkiv", 220), ("Dnipro", "Lviv", 1015), ("Dnipro", "Zaporizhia", 85), ("Dnipro", "Odessa", 475), ("Dnipro", "Donetsk", 250), ("Dnipro", "KryvyiRih", 150),
("Dnipro", "Mykolaiv", 350), ("Dnipro", "Mariupol", 310), ("Dnipro", "Vinnytsia", 575), ("Dnipro", "Poltava", 180), ("Dnipro", "Chernihiv", 540), ("Dnipro", "Sumy",375), ("Dnipro", "Rivne", 805),
("Dnipro", "IvanoFrankivsk", 1080),
#Zaporizhia
("Zaporizhia", "Kyiv", 515), ("Zaporizhia", "Kharkiv", 300), ("Zaporizhia", "Lviv", 1090), ("Zaporizhia", "Dnipro", 85), ("Zaporizhia", "Odessa", 525), ("Zaporizhia", "Donetsk", 230),
("Zaporizhia", "KryvyiRih", 210), ("Zaporizhia", "Mykolaiv", 390), ("Zaporizhia", "Mariupol", 270), ("Zaporizhia", "Vinnytsia", 640), ("Zaporizhia", "Poltava", 270), ("Zaporizhia", "Chernihiv", 630),
("Zaporizhia", "Sumy", 460), ("Zaporizhia", "Rivne", 890), ("Zaporizhia", "IvanoFrankivsk", 1168),
#Odessa
("Odessa", "Kyiv", 475), ("Odessa", "Kharkiv", 700), ("Odessa", "Lviv", 780), ("Odessa", "Dnipro", 475), ("Odessa", "Zaporizhia", 525), ("Odessa", "Donetsk", 730), ("Odessa", "KryvyiRih", 310),
("Odessa", "Mykolaiv", 135),  ("Odessa", "Mariupol", 620),  ("Odessa", "Vinnytsia", 425), ("Odessa", "Poltava", 585), ("Odessa", "Chernihiv", 610), ("Odessa", "Sumy", 830), ("Odessa", "Rivne", 765),
("Odessa", "IvanoFrankivsk", 800),
#Donetsk
("Donetsk", "Kyiv", 725), ("Donetsk", "Kharkiv", 315), ("Donetsk", "Lviv", 1260), ("Donetsk", "Dnipro", 250), ("Donetsk", "Zaporizhia", 230), ("Donetsk", "Odessa", 730), ("Donetsk", "KryvyiRih",435),
("Donetsk", "Mykolaiv", 600), ("Donetsk", "Mariupol", 115), ("Donetsk", "Vinnytsia", 865), ("Donetsk", "Poltava", 465), ("Donetsk", "Chernihiv", 830), ("Donetsk", "Sumy", 505), ("Donetsk", "Rivne", 1135),
("Donetsk", "IvanoFrankivsk", 1325),
#KryvyiRih
("KryvyiRih", "Kyiv", 420), ("KryvyiRih", "Kharkiv", 370), ("KryvyiRih", "Lviv", 950), ("KryvyiRih", "Dnipro", 150), ("KryvyiRih", "Zaporizhia", 210), ("KryvyiRih", "Odessa", 310),
("KryvyiRih", "Donetsk", 435), ("KryvyiRih", "Mykolaiv", 200), ("KryvyiRih", "Mariupol", 480), ("KryvyiRih", "Vinnytsia", 445), ("KryvyiRih", "Poltava", 275), ("KryvyiRih", "Chernihiv", 545),
("KryvyiRih", "Sumy", 525), ("KryvyiRih", "Rivne", 740), ("KryvyiRih", "IvanoFrankivsk", 815),
#Mykolaiv
("Mykolaiv", "Kyiv", 480), ("Mykolaiv", "Kharkiv", 565), ("Mykolaiv", "Lviv", 800), ("Mykolaiv", "Dnipro", 350), ("Mykolaiv", "Zaporizhia", 390), ("Mykolaiv", "Odessa", 135), ("Mykolaiv", "Donetsk", 600),
("Mykolaiv", "KryvyiRih", 200), ("Mykolaiv", "Mariupol", 490), ("Mykolaiv", "Vinnytsia", 430), ("Mykolaiv", "Poltava", 430), ("Mykolaiv", "Chernihiv", 615), ("Mykolaiv", "Sumy", 605),
("Mykolaiv", "Rivne", 770), ("Mykolaiv", "IvanoFrankivsk", 805),
#Mariupol
("Mariupol", "Kyiv", 739), ("Mariupol", "Kharkiv", 420), ("Mariupol", "Lviv", 1315), ("Mariupol", "Dnipro", 310), ("Mariupol", "Zaporizhia", 270), ("Mariupol", "Odessa", 620), ("Mariupol", "Donetsk", 115),
("Mariupol", "KryvyiRih", 480), ("Mariupol", "Mykolaiv", 490), ("Mariupol", "Vinnytsia", 920), ("Mariupol", "Poltava", 495), ("Mariupol", "Chernihiv", 900), ("Mariupol", "Sumy", 620),
("Mariupol", "Rivne", 1165), ("Mariupol", "IvanoFrankivsk", 1290),
#Vinnytsia
("Vinnytsia", "Kyiv", 270), ("Vinnytsia", "Kharkiv", 755), ("Vinnytsia", "Lviv", 365), ("Vinnytsia", "Dnipro", 575), ("Vinnytsia", "Zaporizhia", 640), ("Vinnytsia", "Odessa", 425),
("Vinnytsia", "Donetsk", 865), ("Vinnytsia", "KryvyiRih", 445), ("Vinnytsia", "Mykolaiv", 430), ("Vinnytsia", "Mariupol", 920), ("Vinnytsia", "Poltava", 610), ("Vinnytsia", "Chernihiv", 410),
("Vinnytsia", "Sumy", 600), ("Vinnytsia", "Rivne", 315), ("Vinnytsia", "IvanoFrankivsk", 365),
#Poltava
("Poltava", "Kyiv", 345), ("Poltava", "Kharkiv", 145), ("Poltava", "Lviv", 880), ("Poltava", "Dnipro", 180), ("Poltava", "Zaporizhia", 270), ("Poltava", "Odessa", 585), ("Poltava", "Donetsk", 465),
("Poltava", "KryvyiRih", 275), ("Poltava", "Mykolaiv", 430), ("Poltava", "Mariupol", 495), ("Poltava", "Vinnytsia", 610), ("Poltava", "Chernihiv", 405), ("Poltava", "Sumy", 175),
("Poltava", "Rivne", 665), ("Poltava", "IvanoFrankivsk", 945),
#Chernihiv
("Chernihiv", "Kyiv", 145), ("Chernihiv", "Kharkiv", 510), ("Chernihiv", "Lviv", 685), ("Chernihiv", "Dnipro", 540), ("Chernihiv", "Zaporizhia", 630), ("Chernihiv", "Odessa", 610),
("Chernihiv", "Donetsk", 830), ("Chernihiv", "KryvyiRih", 545), ("Chernihiv", "Mykolaiv", 615), ("Chernihiv", "Mariupol", 900), ("Chernihiv", "Vinnytsia", 410), ("Chernihiv", "Poltava", 405),
("Chernihiv", "Sumy", 310), ("Chernihiv", "Rivne", 470), ("Chernihiv", "IvanoFrankivsk", 750),
#Sumy
("Sumy", "Kyiv", 335), ("Sumy", "Kharkiv", 185), ("Sumy", "Lviv", 875), ("Sumy", "Dnipro", 375), ("Sumy", "Zaporizhia", 460), ("Sumy", "Odessa", 830), ("Sumy", "Donetsk", 505), ("Sumy", "KryvyiRih", 525),
("Sumy", "Mykolaiv", 605), ("Sumy", "Mariupol", 620), ("Sumy", "Vinnytsia", 600), ("Sumy", "Poltava", 175), ("Sumy", "Chernihiv", 310), ("Sumy", "Rivne", 665), ("Sumy", "IvanoFrankivsk", 970),
#Rivne
("Rivne", "Kyiv", 330), ("Rivne", "Kharkiv", 815), ("Rivne", "Lviv", 210), ("Rivne", "Dnipro", 805), ("Rivne", "Zaporizhia", 890), ("Rivne", "Odessa", 765), ("Rivne", "Donetsk", 1135), ("Rivne", "KryvyiRih", 740),
("Rivne", "Mykolaiv", 770), ("Rivne", "Mariupol", 1165), ("Rivne", "Vinnytsia", 315), ("Rivne", "Poltava", 665), ("Rivne", "Chernihiv", 470), ("Rivne", "Sumy", 665), ("Rivne", "IvanoFrankivsk", 275),
#IvanoFrankivsk
("IvanoFrankivsk", "Kyiv", 605), ("IvanoFrankivsk", "Kharkiv", 1090), ("IvanoFrankivsk", "Lviv", 135), ("IvanoFrankivsk", "Dnipro", 1080), ("IvanoFrankivsk", "Zaporizhia", 1168), ("IvanoFrankivsk", "Odessa", 800),
("IvanoFrankivsk", "Donetsk", 1325), ("IvanoFrankivsk", "KryvyiRih", 815), ("IvanoFrankivsk", "Mykolaiv", 805), ("IvanoFrankivsk", "Mariupol", 1290), ("IvanoFrankivsk", "Vinnytsia", 365),
("IvanoFrankivsk", "Poltava", 945), ("IvanoFrankivsk", "Chernihiv", 750), ("IvanoFrankivsk", "Sumy", 970), ("IvanoFrankivsk", "Rivne", 275)
])

#print(graph.dijkstra("Rivne", "Donetsk"))

"""
destinationCity = 'KryvyiRih'
currentCity = "Kyiv"
towsForWay = graph.dijkstra(currentCity, destinationCity)
print(towsForWay)

"""
'''message = input("current")
messaga = input("go")

if (messaga == '1'):
    destinationCity = 'Kyiv'
elif (messaga == '2'):
    destinationCity = 'Kharkiv'
elif (messaga == '3'):
    destinationCity = 'Lviv'
elif (messaga == '4'):
    destinationCity = 'Dnipro'
elif (messaga == '5'):
    destinationCity = 'Zaporizhia'
elif (messaga == '6'):
    destinationCity = 'Odessa'
elif (messaga == '7'):
    destinationCity = 'Donetsk'
elif (messaga == '8'):
    destinationCity = 'KryvyiRih'
elif (messaga == '9'):
    destinationCity = 'Mykolaiv'
elif (messaga == '10'):
    destinationCity = 'Mariupol'
elif (messaga == '11'):
    destinationCity = 'Vinnytsia'
elif (messaga == '12'):
    destinationCity = 'Poltava'
elif (messaga == '13'):
    destinationCity = 'Chernihiv'
elif (messaga == '14'):
    destinationCity = 'Sumy'
elif (messaga == '15'):
    destinationCity = 'Rivne'
elif (messaga == '16'):
    destinationCity = 'IvanoFrankivsk'
else:
    print("fuck")


if (message == '1'):
    currentCity = 'Kyiv'
elif (message == '2'):
    currentCity = 'Kharkiv'
elif (message == '3'):
    currentCity = 'Lviv'
elif (message == '4'):
    currentCity = 'Dnipro'
elif (message == '5'):
    currentCity = 'Zaporizhia'
elif (message == '6'):
    currentCity = 'Odessa'
elif (message == '7'):
    currentCity = 'Donetsk'
elif (message == '8'):
    currentCity = 'KryvyiRih'
elif (message == '9'):
    currentCity = 'Mykolaiv'
elif (message == '10'):
    currentCity = 'Mariupol'
elif (message == '11'):
    currentCity = 'Vinnytsia'
elif (message == '12'):
    currentCity = 'Poltava'
elif (message == '13'):
    currentCity = 'Chernihiv'
elif (message == '14'):
    currentCity = 'Sumy'
elif (message == '15'):
    currentCity = 'Rivne'
elif (message == '16'):
    currentCity = 'IvanoFrankivsk'
else:
    print("fuck")

towsForWay = graph.dijkstra(currentCity, destinationCity)
print(towsForWay)

'''