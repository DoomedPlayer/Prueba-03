import csv

notebooks=[]

def prestar_notebook():

    while True:
        while True:
            rut=input("Ingrese el rut: ")
            if len(rut)>=8 and len(rut)<=10:
                break           
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")

        while True:
                documento=input("Ingrese el documento entregado (Carnet o Pase escolar): ")
                if documento=='Carnet':
                    break
                elif documento=='Pase escolar':
                    break
                else:
                    print("Ingrese Carnet o Pase escolar")

        while True:
            try:
                note_entregado=int(input("Ingrese el notebook entregado: "))
                if note_entregado>0 and note_entregado<30:
                    break
                else:
                    print("No existe ese notebook")
            except ValueError:
                print("Ingrese un numero")
        
        opc=input("Esta seguro de los datos ingresados (Si/No): ")
        if opc=='Si':
            break
        elif opc=='No':
            return
        else:
            print("Ingrese una Si o No")

    notebook={
       'rut':rut,
       'nombre':nombre,
       'apellido':apellido,
       'documento':documento,
       'note_entregado':note_entregado 
    }
    notebooks.append(notebook)
    print(f"Notebook {note_entregado} prestado")

def listar_notes():
    if not notebooks:
        print("No hay notebooks prestados")
    for notebook in notebooks:
        print(f"{notebook['rut']} - {notebook['nombre']} {notebook['apellido']} - Doc. Entregado: {notebook['documento']} - Not. Prestado: {notebook['note_entregado']}")
    print()

def modificar_prestamo():
    listar_notes()
    rut=input("Ingrese el RUT del pedido a modificar: ")
    for note in notebooks:
        if note['rut']==rut:
            notebooks[note['rut']]['note_entregado'] = input("Note. Prestado: ")
            print("Prestamo modificado.\n")
    else:
        print("Prestamo no encontrado.\n")

def devolver_note():
    listar_notes()
    rut = input("Ingrese el rut de la persona que devuelve")
    notebooks[:] = [notebook for notebook in notebooks if notebook.get('rut') != rut]

def imprimir_lista_prest():
    nombre_Docente=input("Ingrese su nombre: ")
    sigla=input("Ingrese la sigla del ramo: ")
    seccion=input("Ingrese la seccion: ")
    with open(f'{nombre_Docente} {sigla}-{seccion}.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['rut', 'nombre', 'apellido','documento', 'note_entregado'])
        writer.writeheader()
        writer.writerows(notebooks)
    print(f"Prestamos guardados en {nombre_Docente} {sigla}-{seccion}.csv\n")
        
def end():
    if len(notebooks)>0:
        print("No puede terminar la clase, hasta que devuelvan todos los notebooks")
    elif len(notebooks)==0:
        print("Clase terminada")
        end()

def main():
    print("Bienvenido docente")
    while True:
        print("Seleccione una opcion")
        print("1. Prestar Notebook")
        print("2. Devolver Notebooks")
        print("3. Modificar prestamo de Notebooks")
        print("4. Imprimir Lista de Notebooks Prestados")
        print("5. Terminar Clase")

        opcion=input("Ingrese una opcion: ")
        if opcion=='1':
            prestar_notebook()
        elif opcion=='2':
            devolver_note()
        elif opcion=='3':
            modificar_prestamo()
        elif opcion=='4':
            imprimir_lista_prest()
        elif opcion=='5':
            end            
        else:
            print("Esa opcion no esta")
main()