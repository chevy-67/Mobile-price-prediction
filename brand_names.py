def getBrand():
    brand_to_label = {
        'OnePlus': 43, 'Realme': 51, 'Apple': 3, 'LG': 28, 'Samsung': 52, 'Asus': 5, 'Xiaomi': 63,
        'Oppo': 44, 'Huawei': 20, 'Google': 15, 'Nokia': 40, 'HTC': 17, 'Motorola': 39, 'Honor': 19,
        'Yu': 65, 'Poco': 48, 'Vivo': 62, 'Nubia': 41, 'Black Shark': 7, 'Infinix': 22, 'Lenovo': 31,
        'Sony': 55, 'Coolpad': 13, 'Micromax': 36, 'Smartron': 54, 'LeEco': 30, 'BlackBerry': 8,
        'Gionee': 14, 'Meizu': 35, 'Panasonic': 45, 'Tecno': 60, 'InFocus': 21, 'Itel': 24, '10.or': 0,
        'Lava': 29, 'Cat': 10, 'Lyf': 33, 'Intex': 23, 'Xolo': 64, 'Acer': 1, 'Phicomm': 46, 'Spice': 56,
        'iVoomi': 72, 'Kult': 27, 'Nuu Mobile': 42, 'Karbonn': 26, 'Ziox': 68, 'Zopo': 69, 'ZTE': 66,
        'Microsoft': 37, 'iBall': 71, 'Mobiistar': 38, 'Comio': 12, 'Videocon': 61, 'Alcatel': 2,
        'Reach': 50, 'Zen': 67, 'Tambo': 59, 'Razer': 49, 'Homtom': 18, 'Lephone': 32, 'Aqua': 4,
        'Celkon': 11, 'Jivi': 25, 'Billion': 6, 'Swipe': 57, 'M-tech': 34, 'Sansui': 53, 'Zuk': 70,
        'TCL': 58, 'mPhone': 73, 'Blu': 9, 'HP': 16, 'Philips': 47
    }

    brand = input("Enter the brand name\t : ")

    label_number = brand_to_label.get(brand)
    if label_number is not None:
        return label_number
    else:
        return 0

def getOS():
    Os_type = {
        'Android':0,
        'Apple':6
    }
    ost = input("Enter OS (Android/Apple) : ")
    return Os_type.get(ost)