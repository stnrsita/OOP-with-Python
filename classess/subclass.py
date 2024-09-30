from .base_class import Vehicle

class Car(Vehicle):  # Inheritance dari Vehicle
    def __init__(self, brand, model, max_speed, engine_capacity, fuel_type, num_doors):
        super().__init__(brand, model, max_speed, engine_capacity)  # Menggunakan super untuk memanggil constructor parent class
        self.fuel_type = fuel_type  # Jenis bahan bakar (bensin/diesel)
        self.num_doors = num_doors  # Jumlah pintu

    def display_info(self):
        return f"{self.general_info()}, Fuel Type: {self.fuel_type}, Doors: {self.num_doors}"

class ElectricCar(Car):  # Multilevel inheritance
    def __init__(self, brand, model, max_speed, battery_capacity, charging_time):
        super().__init__(brand, model, max_speed, 0, "Electric", 4)
        self.battery_capacity = battery_capacity  # Kapasitas baterai (kWh)
        self.charging_time = charging_time  # Waktu pengisian (jam)

    def display_info(self):
        return f"{self.general_info()}, Battery Capacity: {self.battery_capacity} kWh, Charging Time: {self.charging_time} hours"