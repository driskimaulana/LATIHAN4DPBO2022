class Vehicle:
    
    # class constructors
    def __init__(self, modelName = "", fuelType = "", maxPassenger = 0, age = 0, tipe = ""):
        self.__modelName = modelName
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassenger
        self.__age = age
        self.__type = tipe
        
    # getter and setter
    def setModelName(self, modelName):
        self.__modelName = modelName
    
    def getModelName(self):
        return self.__modelName
    
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
    
    def getFuelType(self):
        return self.__fuelType

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
    
    def getMaxPassengers(self):
        return self.__maxPassengers
    
    def setAge(self, age):
        self.__age = age
    
    def getAge(self):
        return self.__age
    
    def setType(self, tipe):
        self.__type = tipe
    
    def getType(self):
        return self.__type
    
    # move method 
    def Move(self):
        print(self.__modelName + " is moving.")
    