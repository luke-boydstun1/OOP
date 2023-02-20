import CoinClass as c


def show_coin_status(coin_obj):
    print(f"This side is up {coin_obj.get_sideup()}")


def flip(coin_obj):
    coin_obj.toss()


def main():
    flip(instance)
    show_coin_status(instance)


instance = c.Coin()
main()
