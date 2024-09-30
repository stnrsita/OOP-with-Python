class Bicycle:
    def __init__(self, brand, type_bicycle, gear_count, frame_material):
        self.brand = brand
        self.type_bicycle = type_bicycle
        self.gear_count = gear_count  # Jumlah gigi
        self.frame_material = frame_material  # Material rangka (misal: aluminium, carbon)

    def display_info(self):
        return f"Bicycle Brand: {self.brand}, Type: {self.type_bicycle}, Gear Count: {self.gear_count}, Frame Material: {self.frame_material}"