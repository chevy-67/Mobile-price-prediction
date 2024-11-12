import requests
import brand_names

url = 'http://127.0.0.1:5000/predict'

brand = brand_names.getBrand()
bat = int(input("Enter Battery Capacity\t : "))
sc_size = float(input("Enter Screen size(inches)\t : "))
x_res = int(input("Enter Width\t : "))
y_res = int(input("Enter Height\t : "))
processor = int(input("Enter Processor\t\t : "))
ram = int(input("Enter RAM in MB\t\t : "))
rom = int(input("Enter ROM in GB\t\t : "))
r_cam = float(input("Enter Rear Camera(MP)\t : "))
f_cam = float(input("Enter Front Camera(MP)\t : "))
os_type = brand_names.getOS()
sim = int(input("ENter No of sims\t : "))


input_data = {
    'brand':brand,
    'battery_capacity_(mah)': bat,
    'screen_size_(inches)': sc_size,
    'resolution_x': x_res,
    'resolution_y': y_res,
    'processor':processor,
    'RAM_(MB)': ram,
    'internal_storage_(GB)': rom,
    'rear_camera': r_cam,
    'front_camera': f_cam,
    'OS': os_type,
    'number_of_sims': sim
}

response = requests.post(url, json=input_data)
print("Predicted Price:", response.json()['predicted_price'])
