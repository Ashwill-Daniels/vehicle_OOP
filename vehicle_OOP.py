"""This program shows the basics of object oriented programming and 
inheritance through the parent class 'vehicle' and sub classes 'sedan', 
'bakkie', 'tractor', and 'lorry'.
"""


class Vehicle:
    """A class which serves as the blueprint for all sub classes."""

    def __init__(self):
        self.num_of_wheels = 4
        self.driven_wheels = "front-wheel-drive"
        self.fuel_type = "petrol"
        self.num_of_seats = 4


class Sedan(Vehicle):
    """This sub class will inherit all the default attributes of the 
    parent class.
    """
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Sedan"


class Bakkie(Vehicle):
    """This sub class will have modified 'driven_wheels' and 'fuel_type' 
    attributes.
    """
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Bakkie"
        self.driven_wheels = "four_wheel_drive"
        self.fuel_type = "diesel"


class Tractor(Vehicle):
    """This sub class will have modified 'driven_wheels', 'fuel_type', 
    and 'num_of_seats'attributes.
    """
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Tractor"
        self.driven_wheels = "rear_wheel_drive"
        self.fuel_type = "diesel"
        self.num_of_seats = 1
        

class Lorry(Vehicle):
    """This sub class will have modified 'driven_wheels', 'fuel_type', 
    'num_of_seats', and 'num_of_wheels' attributes.
    """
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Lorry"
        self.driven_wheels = "rear_wheel_drive"
        self.fuel_type = "diesel"
        self.num_of_seats = 2
        self.num_of_wheels = 8


# An instance of each sub class.
toyota_yaris = Sedan()
ford_ranger = Bakkie()
john_deere_648h = Tractor()
volvo_fh520 = Lorry()

# Store the objects in a list.
vehicle_list = [toyota_yaris, ford_ranger, john_deere_648h, volvo_fh520]

# Display all vehicle objects' attributes in a neat format.
print("Type\tNum_of_Wheels\tDriven_Wheels\t\tFuel_Type\tNum_of_Seats\t")
print("---------------------------------------------------------------------\
---------")
for vehicle_obj in vehicle_list:
    print(f"{vehicle_obj.vehicle_type}\t\t{vehicle_obj.num_of_wheels}\
\t{vehicle_obj.driven_wheels}\t{vehicle_obj.fuel_type}\
\t\t{vehicle_obj.num_of_seats}")