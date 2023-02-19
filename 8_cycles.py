# Cycle in python
if __name__ == '__main__':
    last_humidity = None
    while last_humidity is None:
        input_data = input("Enter last humidity: ")
        if input_data.isdigit():
            last_humidity = int(input_data)


    workroom_humidity = (45, 50, 55, 60, 65, 70, 75, 80, 85, 90, last_humidity)

    sum_of_humidity = 0

    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    for i in range(5):
        print(sum_of_humidity / len(workroom_humidity))
