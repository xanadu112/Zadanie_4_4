def calc(calc_mode, first_number, second_number):
    result = None
    if calc_mode == 1:
        result = first_number + second_number
    elif calc_mode == 2:
        result = first_number - second_number
    elif calc_mode == 3:
        result = first_number * second_number
    elif calc_mode == 4:
        result = first_number / second_number
    return result


if __name__ == "__main__":
    calc_mode = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    get_first_number = input("Podaj składnik 1")
    get_second_number = input("Podaj składnik 2")
    calc()
