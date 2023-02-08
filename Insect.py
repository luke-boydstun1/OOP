import InsectClass as ic


def main():
    insect = ic.Insect()
    insect.set_flight()
    print(f"The insect can fly {insect.get_flight()} miles.")


main()
