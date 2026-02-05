import logging
logging.basicConfig(level=logging.INFO)

def calculator():
    action = int(input("""Podaj działanie, posługując się odpowiednią liczbą: 
    1 Dodawanie, 
    2 Odejmowanie, 
    3 Mnożenie, 
    4 Dzielenie: """))

    if action in [1, 3]:
        try:
            numbers = [float(n) for n in input("""Podaj składniki oddzielone przecinkiem: """).split(',')]
        except ValueError:
            logging.error("TO nie są liczby")
            exit(1)

        if action == 1:
            logging.info(f"Dodaję {numbers}")
            result = sum(numbers)

        else:
            logging.info(f"Mnożę {numbers}")
            result = 1
            for n in numbers:
                result *= n

    elif action in [2, 4]:
        
        try:
            number_1 = float(input("Podaj składnik 1."))
            number_2 = float(input("Podaj składnik 2."))
        except ValueError:
            logging.error("TO nie są liczby")
            exit(1)
        
        if action == 2:        
            logging.info(f"Odejmuję {number_1} i {number_2}")
            result = number_1 - number_2
            
        else:
            if number_2 == 0:
                logging.error("Nie można dzielić przez 0")
                exit(1)
            
            logging.info(f"Dzielę {number_1} i {number_2}")
            result = number_1 / number_2

    else:
        exit(1)

    print(f"Wynik to {result}")

if __name__ == "__main__":
    calculator()
