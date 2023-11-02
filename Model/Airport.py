class Airpor:
    def __init__(self, cod, nam,locat,cit,coun,web,phon,operators):
        self.code = cod
        self.name = nam
        self.location = locat
        self.city = cit
        self.country = coun
        self.website = web
        self.phone = phon
        self.flightOperators = operators
    
    def setCod(self,cod):
        self.code =cod
    
    def getCod(self):
        return self.code
    
    def setName(self,nam):
        self.name =nam
    
    def getNAme(self):
        return self.name
    
    def setLocation(self,loc):
        self.location =loc
    
    def getLocation(self):
        return self.location
    
    def setCity(self,cit):
        self.city =cit
    
    def getCity(self):
        return self.city
    
    def setCountry(self,coun):
        self.country =coun
    
    def getCountry(self):
        return self.country
    
    def setWebsite(self,web):
        self.website =web
    
    def getWebsite(self):
        return self.website

    def setPhone(self,pho):
        self.phone =pho
    
    def getPhone(self):
        return self.phone
    
    def setFlightOperators(self,operators):
        self.flightOperators =operators
    
    def getFlightOperators(self):
        return self.flightOperators
    