from click import password_option


def main() -> str:
    print('Write your math problem bellow (e.g. 1 + 1)\nOr press "n + ENTER" to leave')
    #try:
    opstr = str(input("", password_option))
    #except NameError as err:
    #    print(f"Invalid input! {err}")
    #    main()
    if opstr == "n":
        exit()
    return operation(opstr)


def operation(math) -> None:
    try:
        print(f"\n{math} = {eval(math)}\n")
    except NameError as err:
        print(f"\nInvalid Input! {err}\n")
        main()
    return main()
    

if __name__ == "__main__":
    main()
