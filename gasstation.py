class FuelStation():
    """
    Class for FuelStation with different type of vehicals
    """
    def __init__(self,diesel:int, petrol:int, electric:int):
        """
        initializing open fuel slots
        """
        self.diesel = diesel
        self.petrol = petrol
        self.electric= electric

        self.diesel_slot = diesel
        self.petrol_slot = petrol
        self.electric_slot = electric

    def fuel_vehicle(self,fuel_type:str):
        """
            looks up whether there is an open slot that can provide fuel_type.
            A vehicle can only be fueled in a slot space of its fuel_type.
            If there is no slot free, return false, else put the vehicle in that fuel slot and return true.
        """
        if fuel_type == 'diesel':
            if self.diesel_slot > 0:
                self.diesel_slot -= 1
                return True
            else:
                return False
        elif fuel_type == 'petrol':
            if self.petrol_slot > 0:
                self.petrol_slot -= 1
                return True
            else:
                return False
        elif fuel_type == 'electric':
            if self.electric_slot > 0:
                self.electric_slot -= 1
                return True
            else:
                return False
        else:
            return False

    def open_fuel_slot(self,fuel_type:str):

        if fuel_type == 'diesel':
            if self.diesel_slot < self.diesel:
                self.diesel_slot += 1
                return True
            else:
                return f"only {self.diesel } slot available at fuel station"
        elif fuel_type == 'petrol':
            if self.petrol_slot < self.petrol :
                self.petrol_slot += 1
                return True
            else:
                return f"only {self.petrol } slot available at fuel station"
        elif fuel_type == 'electric':
            if self.electric_slot < self.electric:
                self.electric_slot += 1
                return True
            else:
                return f"only {self.electric} slot available at fuel station"
        else:
            return False

fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("petrol"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))
