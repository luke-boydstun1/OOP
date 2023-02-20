import InsectClass as I


def main():
    mosquito = I.Insect("mosquito", 2, 4)
    housefly = I.Insect("housefly", 2, 4)
    mosquito.set_flight()
    housefly.set_flight()
    print(f"The {mosquito.get_name()} can fly {mosquito.get_flight()} miles.")
    print(f"The {housefly.get_name()} can fly {housefly.get_flight()} miles.")


main()
