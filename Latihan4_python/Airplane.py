from Vehicle import Vehicle

class Airplane(Vehicle):
    
    # class constructors
    def __init__(self, wingsSpan = 0, wingType = "", bodyType = "", engineModel = ""):
        self.__wingsSpan = wingsSpan
        self.__wingType = wingType
        self.__bodyType = bodyType
        self.__engineModel = engineModel
        
    # getter and setter
    def setWingsSpan(self, wingsSpan):
        self.__wingsSpan = wingsSpan
        
    def getWingsSpan(self):
        return self.__wingsSpan
    
    def setWingType(self, wingType):
        self.__wingType = wingType
    
    def getWingType(self):
        return self.__wingType
    
    def setEngineModel(self, engineModel):
        self.__engineModel = engineModel
        
    def getEngineModel(self):
        return self.__engineModel
    
    def setBodyType(self, bodyType):
        self.__bodyType = bodyType
    
    def getBodyType(self):
        return self.__bodyType
    
    # method for showing class
    def ShowClass(self):
        print("-------------------------------------------------")
        print("Airplane Name    : " + self.getModelName())
        print("Airplane Type    : " + self.getType())
        print("Wings Span       : " + str(self.__wingsSpan))
        print("Wings Type       : " + self.__wingType)
        print("Fuel Type        : " + self.getFuelType())
        print("Engine Model     : " + str(self.__engineModel))
        print("Body Type        : " + str(self.__bodyType))
        print("Max Passengers   : " + str(self.getMaxPassengers()))
        print("Age              : " + str(self.getAge()))
        self.Move()
        print("-------------------------------------------------")