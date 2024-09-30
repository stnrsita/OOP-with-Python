# main.py dengan inputan dinamis
from classess.subclass import Car, ElectricCar
from classess.other_class import Bicycle

def get_vehicle_info():
    """Mendapatkan input dari user untuk kendaraan konvensional."""
    brand = input("Masukkan brand kendaraan: ")
    model = input("Masukkan model kendaraan: ")
    max_speed = int(input("Masukkan kecepatan maksimum (km/h): "))
    engine_capacity = int(input("Masukkan kapasitas mesin (cc): "))
    fuel_type = input("Masukkan jenis bahan bakar (bensin/diesel): ")
    num_doors = int(input("Masukkan jumlah pintu: "))
    
    return Car(brand, model, max_speed, engine_capacity, fuel_type, num_doors)

def get_electric_car_info():
    """Mendapatkan input dari user untuk mobil listrik."""
    brand = input("Masukkan brand mobil listrik: ")
    model = input("Masukkan model mobil listrik: ")
    max_speed = int(input("Masukkan kecepatan maksimum (km/h): "))
    battery_capacity = int(input("Masukkan kapasitas baterai (kWh): "))
    charging_time = float(input("Masukkan waktu pengisian (jam): "))
    
    return ElectricCar(brand, model, max_speed, battery_capacity, charging_time)

def get_bicycle_info():
    """Mendapatkan input dari user untuk sepeda."""
    brand = input("Masukkan brand sepeda: ")
    type_bicycle = input("Masukkan tipe sepeda (misal: Mountain Bike, Road Bike): ")
    gear_count = int(input("Masukkan jumlah gigi: "))
    frame_material = input("Masukkan material rangka (misal: aluminium, carbon): ")
    
    return Bicycle(brand, type_bicycle, gear_count, frame_material)

def main():
    print("Pilih jenis kendaraan:")
    print("1. Mobil Konvensional")
    print("2. Mobil Listrik")
    print("3. Sepeda")
    
    choice = input("Masukkan pilihan Anda (1/2/3): ")
    
    if choice == '1':
        vehicle = get_vehicle_info()
    elif choice == '2':
        vehicle = get_electric_car_info()
    elif choice == '3':
        vehicle = get_bicycle_info()
    else:
        print("Pilihan tidak valid!")
        return
    
    # Menampilkan informasi kendaraan
    print(vehicle.display_info())

if __name__ == "__main__":
    main()
