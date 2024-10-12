class India:
    
    def Capital(self):
        print("New Delhi is the Capital of Indian")
    
    def language(self):
        print("Hindi is the Most Widely Spoken Language of India")
    
    def type(self):
        print("India is  a Developing Country")   
    
class Bangladesh:
    
    def Capital(self):
        print("Dhaka is the Capital of Bangladesh")
        
    def language(self):
        print("Bengali is the Primary Language of Bangladesh")
        
    def type(self):
        print("Bangladesh is also a Developing Country")
        
objInd = India()
objBD = Bangladesh()

for country in (objInd, objBD):
    country.Capital()
    country.language()
    country.type()
     