from collections import deque

def BreathSearch(graph, startVertex):

    distances = {i: None for i in graph}
    distances[startVertex] = 0

    queue = deque([startVertex])

    while queue:
        curVertex = queue.popleft()
        for neighVertex in graph[curVertex]:
            if distances[neighVertex] is None:
                distances[neighVertex] = distances[curVertex] + graph[curVertex][neighVertex]
                queue.append(neighVertex)

    return distances

def GetBestAvailableCities(startCity, availableCities, bestCitiesAmount=3 ):
    """
        Returns neighbour cities to the start city. Amount of neighbour cities can be changed with bestCitiesAmount value.
        Output: sorted by distances list of dictionaries which contains pairs City: Distance.
    """
    landMap = \
    {
        # Kyiv
        "Kyiv": {"Kharkiv": 490, "Lviv": 540, "Dnipro": 475, "Zaporizhia": 515, "Odessa": 475, "Donetsk": 725,
                 "KryvyiRih": 420, "Mykolaiv": 480, "Mariupol": 739, "Vinnytsia":270, "Poltava":345, "Chernihiv":145, "Sumy":335, "Rivne":330, "IvanoFrankivsk":605},
        # Kharkiv
        "Kharkiv": {"Kyiv": 490, "Lviv": 1025, "Dnipro": 215, "Zaporizhia": 300, "Odessa": 700, "Donetsk": 315,
                    "KryvyiRih": 370, "Mykolaiv": 565, "Mariupol": 420, "Vinnytsia": 755, "Poltava": 145, "Chernihiv": 510, "Sumy": 185,
                    "Rivne": 815, "IvanoFrankivsk": 1090},
        # Lviv
        "Lviv": {"Kyiv": 540, "Kharkiv": 1025, "Dnipro": 1010, "Zaporizhia": 1090, "Odessa": 780, "Donetsk": 1260,
                 "KryvyiRih": 950, "Mykolaiv": 800, "Mariupol": 1315, "Vinnytsia": 365, "Poltava": 880, "Chernihiv": 685, "Sumy": 875,
                 "Rivne": 210, "IvanoFrankivsk": 135},
        # Dnipro
        "Dnipro": {"Kyiv": 480, "Kharkiv": 220, "Lviv": 1015, "Zaporizhia": 85, "Odessa":475, "Donetsk": 250, "KryvyiRih": 150,
        "Mykolaiv": 350, "Mariupol": 310, "Vinnytsia": 575, "Poltava": 180, "Chernihiv": 540, "Sumy": 375, "Rivne": 805,
        "IvanoFrankivsk": 1080},
        # Zaporizhia
        "Zaporizhia": {"Kyiv": 515, "Kharkiv": 300, "Lviv": 1090, "Dnipro": 85, "Odessa": 525, "Donetsk": 230,
                     "KryvyiRih": 210, "Mykolaiv": 390, "Mariupol": 270, "Vinnytsia": 640, "Poltava": 270, "Chernihiv": 630,
                     "Sumy": 460, "Rivne": 890, "IvanoFrankivsk": 1168},
        # Odessa
        "Odessa": {"Kyiv": 475, "Kharkiv": 700, "Lviv": 780, "Dnipro": 475, "Zaporizhia": 525, "Donetsk": 730,
                   "KryvyiRih": 310,
                   "Mykolaiv": 135, "Mariupol": 620, "Vinnytsia": 425, "Poltava": 585, "Chernihiv": 610, "Sumy": 830,
                   "Rivne": 765,
                   "IvanoFrankivsk": 800},
        # Donetsk
        "Donetsk": {"Kyiv": 725, "Kharkiv": 315, "Lviv": 1260, "Dnipro": 250, "Zaporizhia": 230, "Odessa": 730,
                    "KryvyiRih": 435,
        "Mykolaiv": 600, "Mariupol": 115, "Vinnytsia": 865, "Poltava": 465, "Chernihiv": 830, "Sumy": 505, "Rivne": 1135,
        "IvanoFrankivsk": 1325},
        # KryvyiRih
        "KryvyiRih": {"Kyiv": 420, "Kharkiv": 370, "Lviv": 950, "Dnipro": 150, "Zaporizhia": 210, "Odessa": 310,
        "Donetsk": 435, "Mykolaiv": 200, "Mariupol": 480, "Vinnytsia": 445, "Poltava": 275, "Chernihiv": 545,
        "Sumy": 525, "Rivne": 740, "IvanoFrankivsk": 815},
        # Mykolaiv
        "Mykolaiv": {"Kyiv": 480, "Kharkiv": 565, "Lviv": 800, "Dnipro": 350, "Zaporizhia": 390,
                     "Odessa": 135, "Donetsk": 600,
        "KryvyiRih": 200, "Mariupol": 490, "Vinnytsia": 430, "Poltava": 430, "Chernihiv": 615, "Sumy": 605,
        "Rivne": 770, "IvanoFrankivsk": 805},
        # Mariupol
        "Mariupol": {"Kyiv":739,
                     "Kharkiv":420, "Lviv": 1315, "Dnipro": 310, "Zaporizhia": 270, "Odessa": 620, "Donetsk": 115,
        "KryvyiRih": 480, "Mykolaiv": 490, "Vinnytsia": 920, "Poltava": 495, "Chernihiv": 900, "Sumy": 620,
        "Rivne": 1165, "IvanoFrankivsk": 1290},
        # Vinnytsia
        "Vinnytsia": {"Kyiv": 270, "Kharkiv": 755, "Lviv": 365, "Dnipro": 575, "Zaporizhia": 640, "Odessa": 425,
                      "Donetsk": 865, "KryvyiRih": 445, "Mykolaiv": 430, "Mariupol": 920, "Poltava": 610, "Chernihiv": 410,
                      "Sumy": 600, "Rivne": 315, "IvanoFrankivsk": 365},
        # Poltava
        "Poltava": {"Kyiv": 345, "Kharkiv": 145, "Lviv": 880, "Dnipro": 180, "Zaporizhia": 270, "Odessa": 585,
                    "Donetsk": 465,
                    "KryvyiRih": 275, "Mykolaiv": 430, "Mariupol": 495, "Vinnytsia": 610, "Chernihiv": 405, "Sumy": 175,
                    "Rivne": 665, "IvanoFrankivsk": 945},
        # Chernihiv
        "Chernihiv": {"Donetsk": 830, "KryvyiRih": 545, "Mykolaiv": 615, "Mariupol": 900, "Vinnytsia": 410, "Poltava": 405,
                      "Sumy": 310, "Rivne": 470, "IvanoFrankivsk": 750},
        # Sumy
        "Sumy": {"Kyiv": 335, "Kharkiv": 185, "Lviv": 875,
                 "Dnipro": 375, "Zaporizhia": 460, "Odessa": 830, "Donetsk": 505, "KryvyiRih": 525,
        "Mykolaiv": 605, "Mariupol": 620, "Vinnytsia": 600, "Poltava": 175, "Chernihiv": 310, "Rivne": 665, "IvanoFrankivsk": 970},
        # Rivne
        "Rivne": {"Kyiv": 330, "Kharkiv": 815, "Lviv": 210, "Dnipro": 805, "Zaporizhia": 890, "Odessa": 765,
                  "Donetsk": 1135, "KryvyiRih": 740,
                  "Mykolaiv": 770,
                  "Mariupol": 1165, "Vinnytsia": 315, "Poltava": 665, "Chernihiv": 470, "Sumy": 665, "IvanoFrankivsk": 275},
        # IvanoFrankivsk
        "IvanoFrankivsk": {"Kyiv": 605, "Kharkiv": 1090, "Lviv": 135, "Dnipro": 1080, "Zaporizhia": 1168, "Odessa": 800,
                           "Donetsk": 1325, "KryvyiRih": 815, "Mykolaiv": 805, "Mariupol": 1290, "Vinnytsia": 365,
                           "Poltava": 945, "Chernihiv": 750, "Sumy": 970, "Rivne": 275}
    }

    curDistances = BreathSearch(landMap, startCity)

    bestAvailableCities = []

    for i in range(bestCitiesAmount):
        if len(bestAvailableCities) < len(availableCities):
            minValue, minKey = min(
                (v, k) for k, v in curDistances.items() if k in availableCities and k not in bestAvailableCities)
            bestAvailableCities.append(minKey)

    return bestAvailableCities


myBestCitiesAmount = 4
myAvailableCities = {'Kyiv', 'Kharkiv', 'Lviv', 'Dnipro', 'Zaporizhia', 'Odessa', 'Donetsk', 'KryvyiRih','Mykolaiv', 'Mariupol', 'Vinnytsia', 'Poltava', 'Chernihiv', 'Sumy', 'Rivne', 'IvanoFrankivsk'}

# myStartCity = "Zaporizhia"
# print(GetBestAvailableCities(myStartCity, myAvailableCities, myBestCitiesAmount))
