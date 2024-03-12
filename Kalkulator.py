import logging
logging.basicConfig(level=logging.DEBUG)

def calc(calc_mode, first_number, second_number):
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
    calc_dict = {1: "Dodawanie", 2: "Odejmowanie", 3: "Mnożenie", 4: "Dzielenie"}
    calc_mode = int(input(f"Podaj działanie, posługując się odpowiednią liczbą {calc_dict}: "))
    first_number = float(input("Podaj pierwszy składnik: "))
    second_number = float(input("Podaj drugi składnik: "))
    logging.debug(f"Program wykonuje {calc_dict[calc_mode]} liczb {first_number} i {second_number}")
    operation_result = calc(calc_mode, first_number, second_number)
    print("Wynik: ", operation_result)
