class User:
    def __init__(self,name,link,carNum,telNum,currentCity,destinationCity,pricePerKilometer):
        self.name=name
        self.link=link
        self.carNum=carNum
        self.telNum=telNum
        self.currentCity=currentCity
        self.destinationCity=destinationCity
        self.pricePerKilometer=pricePerKilometer


class HashTable:
    def __init__(self,size):
        self.array=[]
        for i in range (0,size):
            a=[]
            self.array.append([])
        self.size=size

    def addUser(self,data):
        user=data
        string=user.currentCity+user.destinationCity
        valSum=0
        hashId=0
        for i in range(0,len(string)):
            valSum=ord(string[i])+valSum*i
            hashId=valSum % self.size
        self.array[hashId].append(user)

    def findDrivers(self,currentCity,destinationCity):
        string=currentCity+destinationCity
        valSum=0
        hashId=0
        for i in range(0,len(string)):
            valSum=ord(string[i])+valSum*i
            hashId=valSum % self.size
        return self.array[hashId]

    def updateDriver(self,driver,newCity,newDestination):
        user=driver
        string=user.currentCity+user.destinationCity
        valSum=0
        hashId=0
        for i in range(0,len(string)):
            valSum=ord(string[i])+valSum*i
            hashId=valSum % self.size
        user.currentCity = newCity
        user.currentDestination = newDestination
        self.array[hashId].remove(user)
        self.addUser(user)

    def deleteDriver(self,driver):
        user=driver
        string=user.currentCity+user.destinationCity
        valSum=0
        hashId=0
        for i in range(0,len(string)):
            valSum=ord(string[i])+valSum*i
            hashId=valSum % self.size
        self.array[hashId].remove(user)
