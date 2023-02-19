if __name__ == '__main__':
    text = "---Hello, World!---"


     #** strip methods - remove spaces from the beginning and the end of the string
        # lstrip - remove spaces from the beginning of the string
        # rstrip - remove spaces from the end of the string
        # strip - remove spaces from the beginning and the end of the string
    
    print(text.lstrip("-")) # Hello, World!---
    print(text.rstrip("-")) # ---Hello, World!
    print(text.strip("-"))  # Hello, World!

    #** case methods - change the case of the string
        # lower - change the case of the string to lower
        # upper - change the case of the string to upper
        # capitalize - change the case of the string to capitalize
        # title - change the case of the string to title
    text = "case methods"

    print(text.lower()) # case methods
    print(text.upper()) # CASE METHODS
    print(text.capitalize()) # Case methods
    print(text.title()) # Case Methods

    #** replace method - replace the string with another string
    text = "Hello, World!"

    print(text.replace("World", "Andrii")) # Hello, Andrii!

    #** split method - split the string into a list
    text = "Hello, World!"

    print(text.split(",")) # ['Hello', ' World!']

    #** join method - join the list into a string 
    text = ["Hello", "World"]

    print(" ".join(text)) # Hello World

    #** cut method - cut the string [A:B]
    text = "Hello, World!"

    print(text[0:5]) # Hello [A:B - A is included, B is not included]
    print(text[7:]) # World! [A: till the end of the string]
    print(text[:5]) # Hello  [:B - from the beginning of the string till B]

    # cut with step method - cut the string [A:B:C]
    text = "123456789"

    print(text[0:9:2]) # 13579 [A:B:C - A is included, B is not included, C is a step]
    print(text[::2]) # 13579 [A:B:C - from the beginning of the string till the end of the string with a step]
    print(text[1::2]) # 2468 [A:B:C - from the beginning of the string till the end of the string with a step]

    #** find method - find the index of the string. if the string is not found, the method returns -1
    text = "Hello, World!"

    print(text.find("World")) # 7
    print(text.find("Andrii")) # -1

    #** Task 1
    # Create a string "Hello, my name is <name>, I am <occupation>, please contact me on <email>"
        # By the rules name should be capitalized and without any symbols at the beginning and at the end
        # Also occupation should be lower case
        # In email symbol "@" should be replaced with "at"
        # UPD Stakeholder left us secret values, we need to concatenate them to the one string and place it in the end of the string

    name = "           ~~~~andrii~~~~"
    occupation = "QA EnGiNeEr"
    email = "my_valid_email@gmail.com"

    secret_value_first_part = "wetdsg4605"
    secret_value_second_part = "w5w3e3h2"
    secret_code = chr(int(secret_value_first_part[6:]) + int(secret_value_second_part[1::2]))

    print(secret_code)

    result = f"Hello, my name is {name.strip(' ~').capitalize()}, I am {occupation.lower()}, please contact me on {email.replace('@', ' at ')}, {secret_code}"

    print(result)