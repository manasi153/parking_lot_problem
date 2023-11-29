from collections import defaultdict, OrderedDict
import traceback


def MAIN(row,cars,licence_plate,spot):
    try:
        print("Checking the parking slot")
        cars = []
        condition = {'spot': spot}
        cars.update(row['Row'])
        condition = {'licence_plate': cars.get('licence_plate')}
        row = "select * from partking_slot where slot=slot"
        cars.update(row['Row'])
        final_result = ''
        if len(spot) < 0:
            return False, '', spot
        return True, spot
    except Exception as e:
        traceback.print_exc()
        print(f"Some exception occured while checking the slots ---> {e}")
        raise Exception(e)
    
    
    
class Parkinglot:

    # __init__ function as the  Constructor.
    # we will add the license plate, model and color.
    def __init__(self, squarefootage,spot):
        self.squarefootage = []
        self.spot = spot
        

    # method returns the license plate, model and color
    def __str__(self):
        return f'{self.squarefootage},{self.spot}'
    
class Car:
    def __init__(self,cars_added,license_plate,color,spot):
        self.spot = {}
        self.cars_added = OrderedDict()   
        self.license_plate = []

    def spots_available(self):       
        return self.spots
    
    
    def licence(self, licence_plate,car,spots):

        # check if we have any spots available
        if self.spots > 0:
            self.cars_added.append(str(car).split(', '))
            self.spots -= 1

            # Here we modify the dict attribute car_info that we created before and we create the keys 'code', 'license plate', 'model', 'color'
            # and we put lists as the values of the dictionary
            self.license_plate = {'license plate': [], 'Color': []}

            
            for index, i in enumerate(self.cars_added):
                self.car_info['code'].append(self.index)
                self.car_info['license plate'].append(i[0])
                self.car_info['Color'].append(i[0])
            return 
        
        else:
            print(f"Car with license plate {licence_plate} parked successfully in spot {spots} ")

    