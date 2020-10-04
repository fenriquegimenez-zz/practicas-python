def run():
    numeros = input('Por favor ingrese su número de cédula: ')
    pares = [x for x in numeros if int(x) % 2 == 0]
    impares = [x for x in numeros if int(x) % 2 != 0]

    print(f'Los números pares de tu CI son: {*pares}, y los impares: {(*impares, )}')

if __name__ == "__main__":
    run()