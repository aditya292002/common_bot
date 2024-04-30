import json

# Open the JSON file in read mode
with open('data.json', 'r') as file:
    data = json.load(file)

# Add a new person to the 'people' list
new_person = {
    "name": "Bob Johnson",
    "age": 42,
    "email": "bob.johnson@example.com"
}
data['people'].append(new_person)

# Open the JSON file in write mode and write the updated data
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2) 