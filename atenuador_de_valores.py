ids = []
nombres = []
valores_iniciales = []
porcentajes = []
valores_finales = []
categorias = []
estados = []
fechas = []
descripciones = []
#-----------------------------------------#
#--|menu_principal_atenuador_de_valores|--#
#-----------------------------------------#
while True:
    print("menu principal atenuador de valores")
    print("1) registrar valor")
    print("2) editar valor")
    print("3) eliminar valor")
    print("4) buscar valor")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #---------------------#
    #--|registrar_valor|--#
    #---------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_valor = 1
        else:
            id_valor = ids[-1] + 1
        nombre = input("nombre: ")
        valor_inicial = float(input("valor inicial: "))
        porcentaje = float(input("porcentaje de atenuación: "))
        categoria = input("categoría: ")
        fecha = input("fecha: ")
        descripcion = input("descripción: ")
        valor_final = valor_inicial - (
            valor_inicial * porcentaje / 100
        )
        if valor_final >= 0:
            estado = "procesado"
        else:
            estado = "valor inválido"
        ids.append(id_valor)
        nombres.append(nombre)
        valores_iniciales.append(valor_inicial)
        porcentajes.append(porcentaje)
        valores_finales.append(valor_final)
        categorias.append(categoria)
        estados.append(estado)
        fechas.append(fecha)
        descripciones.append(descripcion)
        print("valor registrado correctamente.")
        print("id:", id_valor)
        print("valor inicial:", valor_inicial)
        print("atenuación:", porcentaje, "%")
        print("valor final:", valor_final)
    #------------------#
    #--|editar_valor|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen valores registrados.")
        else:
            print("editar valor")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | {nombres[i]} | "
                    f"{valores_iniciales[i]} | "
                    f"{porcentajes[i]}% | "
                    f"{valores_finales[i]}"
                )
            id_buscar = int(input("ingrese la id del valor: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("valor inicial:", valores_iniciales[posicion])
                print("atenuación:", porcentajes[posicion], "%")
                print("valor final:", valores_finales[posicion])
                nombres[posicion] = input("nuevo nombre: ")
                valores_iniciales[posicion] = float(
                    input("nuevo valor inicial: ")
                )
                porcentajes[posicion] = float(
                    input("nuevo porcentaje de atenuación: ")
                )
                categorias[posicion] = input("nueva categoría: ")
                fechas[posicion] = input("nueva fecha: ")
                descripciones[posicion] = input("nueva descripción: ")
                valores_finales[posicion] = (
                    valores_iniciales[posicion]
                    - (
                        valores_iniciales[posicion]
                        * porcentajes[posicion]
                        / 100
                    )
                )
                if valores_finales[posicion] >= 0:
                    estados[posicion] = "procesado"
                else:
                    estados[posicion] = "valor inválido"
                print("valor actualizado correctamente.")
                print("nuevo valor final:", valores_finales[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_valor|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen valores registrados.")
        else:
            print("eliminar valor")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | {nombres[i]} | "
                    f"{valores_iniciales[i]} | "
                    f"{valores_finales[i]}"
                )
            id_buscar = int(input("ingrese la id del valor: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("valor inicial:", valores_iniciales[posicion])
                print("valor final:", valores_finales[posicion])
                confirmacion = input(
                    "¿desea eliminar este valor? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    valores_iniciales.pop(posicion)
                    porcentajes.pop(posicion)
                    valores_finales.pop(posicion)
                    categorias.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    descripciones.pop(posicion)
                    print("valor eliminado correctamente.")
                else:
                    print("el valor no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_valor|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen valores registrados.")
        else:
            print("buscar valor")
            id_buscar = int(input("ingrese la id del valor: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("valor inicial:", valores_iniciales[posicion])
                print("porcentaje de atenuación:", porcentajes[posicion], "%")
                print("valor final:", valores_finales[posicion])
                print("categoría:", categorias[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("descripción:", descripciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen valores registrados.")
        else:
            valor_inicial_total = 0
            valor_final_total = 0
            atenuacion_total = 0
            porcentaje_total = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | {nombres[i]} | "
                    f"{valores_iniciales[i]} | "
                    f"{porcentajes[i]}% | "
                    f"{valores_finales[i]} | "
                    f"{estados[i]}"
                )
                valor_inicial_total += valores_iniciales[i]
                valor_final_total += valores_finales[i]
                atenuacion_total += (
                    valores_iniciales[i] - valores_finales[i]
                )
                porcentaje_total += porcentajes[i]
            promedio_porcentaje = porcentaje_total / len(ids)
            print("estadísticas atenuador de valores")
            print("cantidad de registros:", len(ids))
            print("valor inicial acumulado:", valor_inicial_total)
            print("valor final acumulado:", valor_final_total)
            print("atenuación total:", atenuacion_total)
            print("promedio de atenuación:", promedio_porcentaje, "%")
            #---------------------------#
            #--|atenuacion_progresiva|--#
            #---------------------------#
            print("atenuación progresiva")
            valor = float(
                input("ingrese el valor que desea atenuar: ")
            )
            cantidad = int(
                input("¿cuántas atenuaciones desea aplicar?: ")
            )
            valor_inicial_proceso = valor
            for i in range(cantidad):
                porcentaje_proceso = float(
                    input(
                        f"porcentaje de atenuación nivel {i + 1}: "
                    )
                )
                reduccion = valor * porcentaje_proceso / 100
                valor = valor - reduccion
                print(
                    f"nivel {i + 1}: "
                    f"-{porcentaje_proceso}% → {valor}"
                )
            reduccion_total = (
                valor_inicial_proceso - valor
            )
            print("proceso de atenuación")
            print("valor inicial:", valor_inicial_proceso)
            print("valor final:", valor)
            print("reducción total:", reduccion_total)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el atenuador de valores.")
        break
    else:
        print("opción no válida.")