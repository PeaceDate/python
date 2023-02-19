# List is a collection which is ordered and changeable. Allows duplicate members.
# Diference between list and tuple is that list is mutable and tuple is immutable and list is slower than tuple.
# List methods:
    # append - add element to the end of the list
    # clear - clear the list
    # copy - copy the list
    # count - count the number of elements in the list
    # extend - add elements from another list to the end of the list
    # index - find the index of the element in the list
    # insert - insert the element to the list
    # pop - remove the element from the list
    # remove - remove the element from the list
    # reverse - reverse the list
    # sort - sort the list

if __name__ == '__main__':
    workroom_humidity = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90] 

    while True:
        input_data = input("Enter last humidity: ")
        if input_data.isdigit():
            workroom_humidity.append(int(input_data))
        elif  "," in input_data:
            workroom_humidity.extend(map(int, input_data.split(",")))
        elif input_data == "":
            break 
        else:
            print("You need to enter number")

    workroom_humidity.sort()
    print(workroom_humidity)
    sum_of_humidity = 0

    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    for i in range(5):
        print(sum_of_humidity / len(workroom_humidity))

     
