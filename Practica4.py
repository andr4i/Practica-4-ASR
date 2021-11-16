from telnetlib import Telnet
import getpass
import pexpect
from ftplib import FTP
from os import system

def conexiontelnet(): #Funcion para conectarse mediante telnet
    direccion = input("Introduce la direccion del host: ")
    host = direccion    #Especificamos la direccion del host
    user = input("Introduce tu nombre de usuario: ")  #Introducimos ususario y contraseña
    password = getpass.getpass()
    uno = pexpect.spawn("telnet "+direccion)
    uno.expect("User: ")
    uno.sendline(user+"\n")
    uno.expect("Password: ")
    uno.sendline(password+"\n")
    uno.sendline("en\n")
    uno.sendline("config\n")
    uno.sendline("copy run start\n")
    uno.sendline("exit\n")
    uno.sendline("exit\n")
    # tn = Telnet(host)   #Instanciamos una clase Telnet
    # tn.read_until(b'User: ')
    # tn.write(user.encode("utf-8"))
    # tn.write(b"\r")
    # tn.read_until(b'Password: ')
    # tn.write(password.encode("utf-8"))    #Validamos credenciales
    # tn.write(b"\r")
    # tn.write((b"en"+b"\r"))
    # tn.write((b"config"+b"\r"))
    # tn.write((b"copy run start"+b"\r"))     #Ejecutamos el comando especificado
    # tn.write((b"exit"+b"\r"))

def servicioftp(tipopeticion):
    direccion = input("Introduce una dirección para validar la información: ")
    usuario = input("Introduce el nombre de usuario: ")
    password = getpass.getpass()
    if(tipopeticion == "get"):
        ftp = FTP(direccion)
        ftp.login(usuario,password)
        with open("config"+direccion,"wb") as f:
            ftp.retrbinary("RETR startup-config",f.write)
        ftp.quit()
    elif(tipopeticion == "put"):
        ftp = FTP(direccion)
        ftp.login(usuario,password)
        with open("config"+direccion,"rb") as f:
            ftp.storbinary("STOR startup-config",f)
        ftp.quit()


while 1:
    system("clear")
    print("Practica 4-Gestor de archivos de configuración")
    print("1) Actualizar el archivo de configuración (Telnet)")
    print("2) Solicitar arhivo de configuración (FTP)")
    print("3) Enviar archivo de configuración (FTP)")
    a = int(input(""))
    if(a==1):
        conexiontelnet()
    elif(a==2):
        servicioftp("get")
    elif(a==3):
        servicioftp("put")
            