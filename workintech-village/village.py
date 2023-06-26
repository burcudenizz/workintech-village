import math

class Silo:
    #constructor
    def __init__(self,radius,height,name,material,ingredient):
        self._radius = radius
        self._height = height
        self._name = name
        self._material = material
        self._ingredient = ingredient
       


#getter&setter
    def get_radius(self):
        return self._radius
    
    def set_radius(self,radius):
        self._radius = radius

    def get_height(self):
        return self._height
    
    def set_height(self,height):
        self.height = height

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name = name

    def get_material(self):
        return self._material
    
    def set_material(self,material):
        self._material = material

    def get_ingredient(self):
        return self._ingredient
    
    def set_ingredient(self,ingredient):
        self._ingredient = ingredient

    def getArea(self):
        return self._radius * self._radius *  math.pi


    def getVolume(self):
        return self.getArea() * self._height
    
    def get_perimeter(self):
        return  2 * self._radius * math.pi 


    def __str__(self):
        return f'{self._name} isimli Silo oluşturuldu. \n Özellikler: \n  Yarıçap: {self._radius} Yükseklik: {self._height} \n Malzeme:{self._material} İçerik:{self._ingredient} \n Alan:{self.getArea()} Hacim:{self.getVolume()} Çevre: {self.get_perimeter()} '
    

def main():

    silo = Silo(50,100,"Workintech Silo","çelik","buğday")
    print(silo)
    area= silo.getArea()
    print(f'Silo Alanı:{area}')
    volume= silo.getVolume()
    print(f'Silo Hacmi:{volume}')
    perimeter= silo.get_perimeter()
    print(f'Silo Çevresi:{perimeter}')

main()