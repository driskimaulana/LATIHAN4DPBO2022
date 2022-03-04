from lib2to3.pgen2 import driver
from Job import Job

class Driver(Job):
    
    # class constructors
    def __init__(self, licenseId = "", activeUntil = "", vehicleType = ""):
        self.__licenseId = licenseId
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    # getter and setter
    def setLicenseId(self, licenseId):
        self.__licenseId = licenseId
        
    def getLicenseId(self):
        return self.__licenseId
    
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    
    def getActiveUntil(self):
        return self.__activeUntil
    
    def setVehicleType(self, vehicleType):
        self.vehicleType = vehicleType
    
    def getVehicleType(self):
        return self.__vehicleType
    
    
