def main() -> str:
    print('Write your math problem bellow (e.g. 1 + 1)\nOr press "n + ENTER" to leave')
    opstr: str = str(input(""))
    if opstr == "n":
        exit()
    return operation(opstr)


def operation(math: str) -> None:
    math = "".join(math)
    try:
        print(f"\n{math} = {eval(math)}\n")
    except NameError as err:
        print(f"\nInvalid Input! {err}\n")
        main()
    return main()
    

if __name__ == "__main__":
    main()
