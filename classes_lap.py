
class Vehicle:

    def __init__(self, brand, name, color, capacity, plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    
    def drive(self):
        print(f"{self.__name} is driving!")
    
    def drift(self):
        print(f"{self.__name} is drifting !!")
    
    def carry_cargo(self):
        print(f"{self.__name} is carrying cargo !!")

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color
    
    def set__capacity(self,capacity ):
        self.__capacity = capacity

    def get__capacity(self):
        return self.__capacity

    def set__plate_number(self, plate_number):
        self.__plate_number = plate_number

    def get_(self):
        return self.__plate_number



# override the methods as needed for each subclass of vehicle. 


class Bus(Vehicle):
    def drift(self):
        print(f"{self.get_name()} is a bus it cannot drift")
    def carry_cargo(self):
        print(f"{self.get_name()} is a bus cannot carry cargo")


class Truck(Vehicle):
     def drift(self):
        print(f"{self.get_name()} is a truck it cannot drift")
        
        
bus= Bus('Higer Bus','Higer H4E','red',30,'CCC123')
bus.drive()
bus.drift()
bus.carry_cargo()

truck= Truck('Isuzu','fvz','black',2,'BBA444')
truck.drive()
truck.drift()
truck.carry_cargo()