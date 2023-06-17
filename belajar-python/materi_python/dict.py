customer = [
    {"Name": "Fariz", "Age": "20", "Address": "Subang"},
    {"Name": "John", "Age": "20", "Address": "Sukabumi"},
    {"Name": "Benedict", "Age": "20", "Address": "Tasikmalaya"}
]

for data in customer:
    name = data["Name"]
    age = data["Age"]
    address = data["Address"]
    data["Company"] = "FMA MEDIA"
    data["Name"] = "Fariz Muhammad Aditya"
    del data["Company"]

for data in customer:
    for key, value in data.items():
        print(f"{key}: {value}")
    print()