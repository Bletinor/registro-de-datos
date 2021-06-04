idNum = input("Ingrese su cédula: ")
name = input("Ingrese su(s) nombre(s): ")
lastName = input("Ingrese su(s) apellido(s): ")
age = input("Ingrese su edad: ")
save = input("Desea grabar? (Y/N): ")
if (save == "Y" or save == "y"):
    print("guardado")
    registro = open("registro.txt", "a")
    registro.writelines(f"\n {idNum}, {name}, {lastName}, {age}")
elif (save == "N" or save == "n"):
    print("no guardado")
else:
    exit