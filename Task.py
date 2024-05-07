# Define the categories
categories = ['Red', 'Yellow', 'Green', 'TimeActive', 'Time']

# Initialize a counter for 'Red' = '1'
red_counter = 0
yellow_counter = 0
green_counter = 0


# Open the file in read mode
with open(r'C:\Users\Testuotojas\Downloads\Python_task_qdev_Jnr\task\data.txt', 'r') as file:
    # Read all lines in the file
    data = file.readlines()

# Now, 'data' is a list where each element is a line from 'filename.txt'
for line in data:
    # Split the line into numbers
    numbers = line.strip().split(',')
    # Combine the categories and numbers into a dictionary
    parsed_data = dict(zip(categories, numbers))
    # If 'Red' is '1', increment the counter
    if parsed_data['Red'] == '1':
        red_counter += 1
    if parsed_data['Yellow'] == '1':
        yellow_counter +=1
    if parsed_data['Green'] == '1':
        green_counter +=1
print ("Times when all lights were active:")
print(f"'Red' = {red_counter} ")
print(f"'Yellow' = {yellow_counter} ")
print(f"'Green' = {green_counter} ")
