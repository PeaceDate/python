# Conditional operators
if __name__ == '__main__':
    vendor  = input("Enter vendor name: ")
    fridge_height = int(input("Enter fridge height: "))
    fridge_width = int(input("Enter fridge width: "))

    is_pass_trouhgt_door = fridge_height <= 210 and fridge_width <= 90
    is_pass_trouhgt_window = fridge_height <= 170 and fridge_width <= 320

    if vendor in ("Brrr", "SMF") and (is_pass_trouhgt_door or is_pass_trouhgt_window):
        print("It suits us")
    else:
        print("It doesn't suit us")