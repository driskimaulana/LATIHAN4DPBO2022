from Driver import Driver

class Person:
    
    # class constructors
    def __init__(self, nik = "", name = "", gender = "", driver = Driver()):
        self.__nik = nik
        self.__name = name
        self.__gender = gender
        self.__driver = driver
    
    # getter and setter
    def setNik(self, nik):
        self.__nik = nik
    
    def getNik(self):
        return self.__nik
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setGender(self, gender):
        self.__gender = gender
    
    def getGender(self):
        return self.__gender

    def setDriver(self, driver):
        self.__driver = driver
    
    def getDriver(self):
        return self.__driver
    
    # persons Sleep method
    def Sleep(self):
        print(self.__name + "is on the sleep now")
    
    # show class method
    def ShowClass(self):
        print("-------------------------------------------------")
        print("NIK              : " + self.__nik)
        print("Name             : " + self.__name)
        print("Gender           : " + self.__gender)
        print("Driver License   : " + self.__driver.getLicenseId())
        print("Active Until     : " + self.__driver.getActiveUntil())
        print("Vehicle Type     : " + self.__driver.getVehicleType())
        print("NIP              : " + self.__driver.getNip())
        print("Company Name     : " + self.__driver.getCompanyName())
        print("Position         : " + self.__driver.getPosition())
        self.Sleep()
        print("-------------------------------------------------")