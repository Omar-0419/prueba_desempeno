#diccionario global llamado 'estudiantes' 
estudiantes = {
    1 : {
    "id": 1,    
    "nombre": "Omar",
    "apellido": "Vizcaino",
    "edad": 21,
    "programa": "Frontend",
    "estado": "active"
    },

    2 : {
    "id": 2,
    "nombre": "Ana",
    "apellido": "Perez",
    "edad": 24,
    "programa": "Frontend",
    "estado": "active"
    }

}

#función para mostrar los estudiantes registrados
def mostrar_estudiantes():

    #Ciclo for para navegar en el diccionario 'estudiantes' 
    for llave, estudiante in estudiantes.items():

        #Mostramos información de los estudiantes registrados
        print(estudiante["id"], "-", estudiante["nombre"], "-", estudiante["apellido"], "-", estudiante["edad"], "-", estudiante["programa"], "-", estudiante["estado"])


#función para agregar un estudiante
def agregar_estudiante(nombre:str, apellido:str, edad:int, programa:str, estado:str, nuevo:int):

            #Verificamos que la información del estado sea correcta
            if estado != "active" and estado != "inactive":
                print("Incorrect status, please verify that the status is active or inactive.")

            else:

                #Agregamos información de nuevo estudiante
                estudiantes[nuevo] = {"id": nuevo,"nombre": nombre, "apellido": apellido,"edad": edad, "programa": programa, "estado": estado}


#función para buscar un estudiante por su ID
def buscar_estudiante(busqueda_id:int):
    encontrado = False

    #Ciclo for para navegar en el diccionario 'estudiantes'
    for llave, estudiante in estudiantes.items():

        #Validamos si el ID del estudiante es igual al que el usuario busca
        if estudiante["id"] == busqueda_id:
            print(estudiante["id"], "-", estudiante["nombre"], "-", estudiante["apellido"], "-", estudiante["edad"], "-", estudiante["programa"], "-", estudiante["estado"])
            encontrado = True
    
    #Le informamos al usuario que el ID no se encuentra registrado
    if encontrado == False:
        print(f"There are no students registered with ID: {busqueda_id}")



#función para eliminar un estudiante buscandolo por su ID    
def eliminar_estudiante(eliminar:int):

    encontrado = False

    #Ciclo for para navegar en el diccionario 'estudiantes'
    for llave, estudiante in estudiantes.items():

        #Validamos si el ID del estudiante es igual al que el usuario busca
        if estudiante["id"] == eliminar:
                eliminar = llave
                id_eliminado = estudiante["id"]
                encontrado = True

    if encontrado == True:

        #Eliminamos al estudiante con la función pop()  
        estudiantes.pop(eliminar)
        print(f"You have removed the student with ID: {id_eliminado}")

    else:
        print(f"There are no students registered with ID: {eliminar}")


#función para actualizar un estudiante buscandolo por su ID 
def actualizar_estudiante(busqueda_id:int):
    estudiante_encontrado = None
    encontrar = False

    #Ciclo for para navegar en el diccionario 'estudiantes'
    for llave, estudiante in estudiantes.items():
        
        #Validamos si el ID del estudiante es igual al que el usuario busca
        if estudiante["id"] == busqueda_id:

            estudiante_encontrado = estudiante

            #Mostramos información del estudiante
            print(estudiante["id"], "-", estudiante["nombre"], "-", estudiante["apellido"], "-", estudiante["edad"], "-", estudiante["programa"], "-", estudiante["estado"])

            #Solicitamos al usuario lo que quiere actualizar del estudiante
            dato = input(f"What information would you like to update about the student {estudiante_encontrado['nombre']}?: ").lower()

            encontrar = True

            #Validamos que el usuario haya ingresado 'name'
            if dato == "name":
                nuevo_dato = input("Enter student name to update: ")
                estudiante_encontrado["nombre"] = nuevo_dato
            
            #Validamos que el usuario haya ingresado 'last name'
            elif dato == "last name":
                nuevo_dato = input("Enter student last name to update: ")
                estudiante_encontrado["apellido"] = nuevo_dato
            
            #Validamos que el usuario haya ingresado 'age'
            elif dato == "age":
                nuevo_dato = int(input("Enter student age to update: "))
                estudiante_encontrado["edad"] = nuevo_dato
            
            #Validamos que el usuario haya ingresado 'program'
            elif dato == "program":
                nuevo_dato = input("Enter student program to update: ")
                estudiante_encontrado["programa"] = nuevo_dato

            #Validamos que el usuario haya ingresado una opción válida
            else:
                print("The information does not exist.")
    
    #Le informamos al usuario que el ID no se encuentra registrado
    if encontrar == False:
        print("The ID entered is not registered.")


#Variable 'selec' inicia vacía 
selec = ""


#Ciclo while que repite el menú hasta que el usuario ingrese la opción 'exit'
while selec != "exit" and selec != "6":
    
    
    #Mostrar menú
    print("\n1. View registered students\n2. Add student\n3. Search for student\n4. Delete student\n5. Update student information\n6. Exit\n")

    id = 0

    #Solicitamos al usuario que escoja una opción
    selec = input("Choose an option: ").lower()
    print()
    

    #Validar que el usuario haya seleccionado la opción 1
    if selec == "view registered students" or selec == "1":

        #Validamos si el diccionario está vacío o no
        if len(estudiantes) > 0:

            #Llamamos a la función mostrar_estudiantes
            mostrar_estudiantes()
        
        else:
            print("There are no registered students.")
    

    #Validar que el usuario haya seleccionado la opción 2
    elif selec == "add student" or selec == "2":
        try:

            #Solicitamos datos para registrar estudiante
            nombre = input("Name: ")
            apellido = input("Last name: ")
            edad = int(input("Age: "))
            programa = input("Program: ")
            estado = input("State (active/inactive): ")
            nuevo = len(estudiantes) + 1

            #Llamamos a la función agregar_estudiantes e ingresamos sus debidos parámetros
            agregar_estudiante(nombre, apellido, edad, programa, estado, nuevo)


        #Mostramos mensaje en caso de que el usuario ingrese un valor inválido
        except ValueError:
            print("Incorrect value, please verify that the data entered matches the request")
    

    #Validar que el usuario haya seleccionado la opción 3
    elif selec == "search for student" or selec == "3":

        #Validamos si el diccionario está vacío o no
        if len(estudiantes) > 0:

            try:

                #Solicitamos al usuario que ingrese ID del estudiante
                busqueda_id = int(input("Enter the ID you wish to search for: "))

                #Llamamos a la función buscar_estudiantes e ingresamos sus debidos parámetros
                buscar_estudiante(busqueda_id)


            #Mostramos mensaje en caso de que el usuario ingrese un valor inválido
            except ValueError:
                print("Incorrect value, please verify that the data entered matches the request")
        
        else:
            print("There are no registered students.")
    

    #Validar que el usuario haya seleccionado la opción 4
    elif selec == "delete student" or selec == "4":

        #Validamos si el diccionario está vacío o no   
        if len(estudiantes) > 0:

            try:

                #Solicitamos al usuario que ingrese ID del estudiante
                eliminar = int(input("Enter the ID you wish delete: "))

                #Llamamos a la función eliminar_estudiantes e ingresamos sus debidos parámetros
                eliminar_estudiante(eliminar)
            

            #Mostramos mensaje en caso de que el usuario ingrese un valor inválido
            except ValueError:
                print("Incorrect value, please verify that the data entered matches the request")

        else:
            print("There are no registered students.")
    

    #Validar que el usuario haya seleccionado la opción 5
    elif selec == "update student information" or selec == "5":
        
        #Validamos si el diccionario está vacío o no
        if len(estudiantes) > 0:
            busqueda_id = int(input("Enter the ID you wish to search for: "))

            #Llamamos a la función actualizar_estudiante e ingresamos sus debidos parámetros
            actualizar_estudiante(busqueda_id)
        
        else:
            print("There are no registered students.")
    

    #Validar que el usuario haya seleccionado la opción 6
    elif selec == "exit" or selec == "6":

        #Le informamos al usuario que acaba de salir del programa
        print("You have left the program")


    #Validar que el usuario haya seleccionado una opción válida
    else:
        print("Invalid option.")