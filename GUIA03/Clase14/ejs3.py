while True:
    print("1) Sumar 2) Restar 0) Salir")
    op = input("Opcion: ")

    if op == "0" :
        print("Adios")
        break
    
    if op in ("1", "2") :
        a = float(input("a: "))
        b = float(input("b: "))

        print(a+b if op == "1" else a-b)

    else :
        print("Opcion invalida")
        