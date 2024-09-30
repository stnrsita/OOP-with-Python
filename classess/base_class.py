class Vehicle:
    def __init__(self, brand, model, max_speed, engine_capacity):
        self.__brand = brand  # Private attribute
        self.model = model    # Public attribute
        self.max_speed = max_speed  # Kecepatan maksimum (km/h)
        self.engine_capacity = engine_capacity  # Kapasitas mesin (cc)

    def get_brand(self):
        return self.__brand  # Getter untuk private attribute

    def set_brand(self, brand):
        self.__brand = brand  # Setter untuk private attribute

    def fuel_efficiency(self, distance, fuel_used):
        """Menghitung efisiensi bahan bakar (km per liter)."""
        return distance / fuel_used

    def general_info(self):
        return f"Brand: {self.__brand}, Model: {self.model}, Max Speed: {self.max_speed} km/h, Engine Capacity: {self.engine_capacity} cc"
