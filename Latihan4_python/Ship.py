from tabnanny import check
from Vehicle import Vehicle

class Ship(Vehicle):
    
    # class constructors
    def __init__(self, countryOfManufacture = "", length = 0, beam = 0, currentPosition = ""):
        self.__countryOfManufacture = countryOfManufacture
        self.__length = length
        self.__beam = beam
        self.__currentPosition = currentPosition
        
    # getter and setter
    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
    
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture
    
    def setLength(self, length):
        self.__length = length
    
    def getLength(self):
        return self.__length
    
    def setBeam(self, beam):
        self.__beam = beam
    
    def getBeam(self):
        return self.__beam
    
    def setCurrentPosition(self, currentPosition):
        self.__currentPosition = currentPosition
    
    def getCurrentPosition(self):
        return self.__currentPosition
    
    # method for checking location
    def checkCurrentPosition(self):
        print("Status                   : On the way to " + self.__currentPosition)
    
    # method for showing class
    def ShowClass(self):
        print("-------------------------------------------------")
        print("Ship Name                : " + self.getModelName())
        print("Ship Type                : " + self.getType())
        print("Country of Manufacture   : " + self.__countryOfManufacture)
        print("Fuel Type                : " + self.getFuelType())
        print("Length                   : " + str(self.__length))
        print("Beam                     : " + str(self.__beam))
        print("Max Passengers           : " + str(self.getMaxPassengers()))
        print("Age                      : " + str(self.getAge()))
        self.Move()
        self.checkCurrentPosition()
        print("-------------------------------------------------")