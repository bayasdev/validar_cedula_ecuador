# Función que valida si una CI ecuatoriana es válida
# 2021 Victor Bayas

def validar_cedula(cedula):
    longitud = len(cedula)
    # Validar que la CI contenga exactamente 10 dígitos
    if longitud == 10:
        provincia = int(cedula[0:2])  # dos primeros dígitos de la CI
        # Validar provincia (1-24)
        if 1 <= provincia <= 24:
            tercer_digito = int(cedula[2])
            # El tercer dígito debe estar entre 0 y 6
            if 0 <= tercer_digito <= 6:
                validador = int(cedula[9])
                coeficientes = (2, 1, 2, 1, 2, 1, 2, 1, 2)  # coeficientes del módulo 10
                suma = 0
                for i in range(0, len(coeficientes)):
                    multip = (int(cedula[i])*coeficientes[i])
                    # Si una multiplicación es >= 10 se le debe restar 9
                    if multip >= 10:
                        multip -= 9
                    # print(f'Digito {int(cedula[i])}, multiplicacion {multip}')
                    suma += multip
                decena_superior = round(suma/10.)*10  # calculamos la decena superior de la suma
                resta = decena_superior - suma  # calculamos el último digito según la suma menos decena superior
                # Validar que el resultado de la resta y el dígito validador sean iguales
                if resta == validador:
                    print(f'La cédula {cedula} es válida')
                else:
                    print(f'La cédula {cedula} no es válida')
            else:
                print('El tercer dígito no es válido')
        else:
            print('El código de provincia no es válido')
    else:
        print('Un número de cédula debe tener 10 dígitos')


# Uso: validar_cedula(nro_cedula), pasar valor como un string
nro_cedula = input('Ingrese un número de cédula: ')
validar_cedula(nro_cedula)
