class Job:
    
    # class constructors
    def __init__(self, nip = "", companyName = "", position = ""):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position
    
    # getter and setter
    def setNip(self, nip):
        self.__nip = nip
    
    def getNip(self):
        return self.__nip
    
    def setCompanyName(self, companyName):
        self.__companyName = companyName
    
    def getCompanyName(self):
        return self.__companyName
    
    def setPosition(self, position):
        self.__position = position
    
    def getPosition(self):
        return self.__position
    