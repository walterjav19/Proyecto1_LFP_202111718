from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter.font import Font
from Cursos import Curso
from Cursos import lista_objetos
from Cursos import codis

filas=0

principal=tkinter.Tk()
global gestionar


def inicio():
    principal.title("Menu Principal")
    principal.geometry("500x500")


    curso=tkinter.Label(principal,text="Nombre del curso: Lab Lenguajes Formales y de Programacion")
    curso.place(x=10,y=10)


    nombre=tkinter.Label(principal,text="Nombre del estudiante: Walter Javier Santizo Mazariegos")
    nombre.place(x=10,y=50)

    carne=tkinter.Label(principal,text="Carne del estudiante: 202111718")
    carne.place(x=10,y=90)

    Cargar=tkinter.Button(principal,text="Cargar Archivos",command=ventana_ruta)
    Cargar.place(x=200,y=130)

    gestionar=tkinter.Button(principal,text="Gestionar Cursos",command=ventana_gestionar)
    gestionar.place(x=200,y=170)


    conteo=tkinter.Button(principal,text="Conteo de Creditos",command=ventana_conteo)
    conteo.place(x=190,y=210)



    salir=tkinter.Button(principal,text="Salir",command=funcion_salir)
    salir.place(x=230,y=250)

    principal.mainloop()
        

def ventana_ruta():
    principal.withdraw()
    ruta=tkinter.Tk()
    ruta.title("ruta")
    ruta.geometry("500x250")
    ru=tkinter.Label(ruta,text="Ruta")
    ru.place(x=100,y=75)
    txtRuta=tkinter.Entry(ruta)
    txtRuta.place(x=150,y=75,width=250,height=20)
    def funcion_leer():
        global filas
        global direc
        try:
            direc=txtRuta.get()
            print(Curso.leer_archivo(direc))
            filas=Curso.cantidad_cursos()
            txtRuta.delete(0,'end')
            messagebox.showinfo("Aviso","Archivo cargado correctamente")
        except PermissionError:
            messagebox.showerror("Error","compruebe la ruta de su archivo")
        except FileNotFoundError:
            if direc=="":
                messagebox.showwarning("Aviso","rellene el campo de texto")
            else:
                messagebox.showwarning("Aviso","Archivo no encontrado")                
    btnSeleccionar=tkinter.Button(ruta,text="Seleccionar",command=funcion_leer)
    btnSeleccionar.place(x=150,y=120)
    def regresar_de_ruta_principal():
        principal.deiconify()
        ruta.withdraw()
    btnRegresar=tkinter.Button(ruta,text="Regresar",command=regresar_de_ruta_principal)
    btnRegresar.place(x=240,y=120)

        
def ventana_listar_cursos():
    gestionar.withdraw()
    listar=tkinter.Tk()
    listar.title("Listar Curso")
    listar.geometry("700x500")


    def regresar_de_listar_gestionar():
        gestionar.deiconify()
        listar.withdraw()
        
    btnRegresar=tkinter.Button(listar,text="Regresar",command=regresar_de_listar_gestionar)
    btnRegresar.place(x=340,y=390)   


    arbol=ttk.Treeview(listar,columns=("#1","#2","#3","#4","#5","#6"))
    arbol.place(x=0,y=0,width=700)
    arbol.heading("#0",text="Codigo")
    arbol.column("#0",width=40)
    arbol.heading("#1",text="Nombre")
    arbol.column("#1",width=100)
    arbol.heading("#2",text="Pre requisitos")
    arbol.column("#2",width=40)
    arbol.heading("#3",text="Opcionalidad")
    arbol.column("#3",width=40)
    arbol.heading("#4",text="Semestre")
    arbol.column("#4",width=40)
    arbol.heading("#5",text="Creditos")
    arbol.column("#5",width=40)
    arbol.heading("#6",text="Estado")
    arbol.column("#6",width=40)

    
    for i in range (filas):
        opcionalidad=lista_objetos[i].obligatorio
        estado=lista_objetos[i].estado
        
        if int(estado)==0:
            estado="Aprobado"
        elif int(estado)==1:
            estado="Cursando"
        elif int(estado)==-1:
            estado="Pendiente"    

        if opcionalidad=="1":
            opcionalidad="Obligatorio"
        else:
            opcionalidad="Opcional"    
        arbol.insert("",END,text=lista_objetos[i].codigo,values=(lista_objetos[i].nombre,lista_objetos[i].pre_requisito,opcionalidad,lista_objetos[i].semestre,lista_objetos[i].creditos,estado))





 

def ventana_agregar_curso():
    gestionar.withdraw()
    agregar=tkinter.Tk()
    agregar.title("Agregar Curso")
    agregar.geometry("500x500")
    cod=tkinter.Label(agregar,text="Codigo")
    cod.place(x=20,y=30)
    txtCod=tkinter.Entry(agregar)
    txtCod.place(x=100,y=30,width=200)
    nom=tkinter.Label(agregar,text="Nombre")
    nom.place(x=20,y=60)
    txtnom=tkinter.Entry(agregar)
    txtnom.place(x=100,y=60,width=200)
    pre=tkinter.Label(agregar,text="Pre Requisito")
    pre.place(x=20,y=90)
    txtPre=tkinter.Entry(agregar)
    txtPre.place(x=100,y=90,width=200)
    sem=tkinter.Label(agregar,text="Semestre")
    sem.place(x=20,y=120)
    txtSem=tkinter.Entry(agregar)
    txtSem.place(x=100,y=120,width=200)
    opc=tkinter.Label(agregar,text="Opcionalidad")
    opc.place(x=20,y=150)
    txtOpc=tkinter.Entry(agregar)
    txtOpc.place(x=100,y=150,width=200)
    cred=tkinter.Label(agregar,text="Creditos")
    cred.place(x=20,y=180)
    txtCred=tkinter.Entry(agregar)
    txtCred.place(x=100,y=180,width=200)
    est=tkinter.Label(agregar,text="Estado")
    est.place(x=20,y=210)
    txtEst=tkinter.Entry(agregar)
    txtEst.place(x=100,y=210,width=200)
    def regresar_de_agregar_gestionar():
        gestionar.deiconify()
        agregar.withdraw()
    btnRegresar=tkinter.Button(agregar,text="Regresar",command=regresar_de_agregar_gestionar)
    btnRegresar.place(x=240,y=250)
    def btn_agregar():
        global filas,objetos
        p1=txtCod.get()
        p2=txtnom.get()
        p3=txtPre.get()
        p4=txtOpc.get()
        p5=txtSem.get()
        p6=txtCred.get()
        p7=txtEst.get()
        Curso.agregar_cursos(p1,p2,p3,p4,p5,p6,p7)
        filas=Curso.cantidad_cursos()


        txtCod.delete(0,'end')
        txtnom.delete(0,'end')
        txtEst.delete(0,'end')
        txtPre.delete(0,'end')
        txtSem.delete(0,'end')
        txtOpc.delete(0,'end')
        txtCred.delete(0,'end')
        txtEst.delete(0,'end')




    btnAgregar=tkinter.Button(agregar,text="Agregar",command=btn_agregar)
    btnAgregar.place(x=120,y=250)




def ventana_editar_curso():
    gestionar.withdraw()
    editar=tkinter.Tk()
    editar.title("Editar Curso")
    editar.geometry("500x500")
    cod=tkinter.Label(editar,text="Codigo")
    cod.place(x=20,y=30)
    txtCod=tkinter.Entry(editar)
    txtCod.place(x=100,y=30,width=200)
    nom=tkinter.Label(editar,text="Nombre")
    nom.place(x=20,y=60)
    txtnom=tkinter.Entry(editar)
    txtnom.place(x=100,y=60,width=200)
    pre=tkinter.Label(editar,text="Pre Requisito")
    pre.place(x=20,y=90)
    txtPre=tkinter.Entry(editar)
    txtPre.place(x=100,y=90,width=200)
    sem=tkinter.Label(editar,text="Semestre")
    sem.place(x=20,y=120)
    txtSem=tkinter.Entry(editar)
    txtSem.place(x=100,y=120,width=200)
    opc=tkinter.Label(editar,text="Opcionalidad")
    opc.place(x=20,y=150)
    txtOpc=tkinter.Entry(editar)
    txtOpc.place(x=100,y=150,width=200)
    cred=tkinter.Label(editar,text="Creditos")
    cred.place(x=20,y=180)
    txtCred=tkinter.Entry(editar)
    txtCred.place(x=100,y=180,width=200)
    est=tkinter.Label(editar,text="Estado")
    est.place(x=20,y=210)
    txtEst=tkinter.Entry(editar)
    txtEst.place(x=100,y=210,width=200)


    def Busqueda():
        try:
            indice=Curso.buscar_curso(txtCod.get())
            txtnom.delete(0,'end')
            txtEst.delete(0,'end')
            txtPre.delete(0,'end')
            txtSem.delete(0,'end')
            txtOpc.delete(0,'end')
            txtCred.delete(0,'end')
            txtEst.delete(0,'end')
            txtnom.insert(0,lista_objetos[indice].nombre)
            txtPre.insert(0,lista_objetos[indice].pre_requisito)
            txtSem.insert(0,lista_objetos[indice].semestre)
            txtOpc.insert(0,lista_objetos[indice].obligatorio)
            txtCred.insert(0,lista_objetos[indice].creditos)
            txtEst.insert(0,lista_objetos[indice].estado)
        except TypeError:
            messagebox.showwarning("Alerta","El Curso no Existe")    
    btnBuscar=tkinter.Button(editar,text="Buscar",command=Busqueda)
    btnBuscar.place(x=325,y=30)




    def regresar_de_editar_gestionar():
        gestionar.deiconify()
        editar.withdraw()
    btnRegresar=tkinter.Button(editar,text="Regresar",command=regresar_de_editar_gestionar)
    btnRegresar.place(x=240,y=250) 
    def btn_editar():
        if txtnom.get()=="" or txtEst.get()=="" or txtSem.get()=="" or txtOpc.get()=="" or txtCred.get()=="" or txtEst.get()=="":
            messagebox.showwarning("Alerta","Rellene los campos obligatorios")
        elif int(txtOpc.get())<0 or int(txtOpc.get())>1:
            messagebox.showwarning("Alerta","Ingrese obligatorio [1] u Opcional [0]")
        elif int(txtSem.get())<1 or int(txtSem.get())>10:
            messagebox.showwarning("Alerta","Ingrese un semestre entre el 1 al 10")
        elif int(txtCred.get())<0 or int(txtCred.get())>10:
            messagebox.showwarning("Alerta","Ingrese un rango de creditos validos 0-10")
        elif int(txtEst.get())<-1 or int(txtEst.get())>1:
            messagebox.showwarning("Alerta","Ingrese aprobado [0] o cursando [1] o pendiente [-1]")
        else:
            indice=Curso.buscar_curso(txtCod.get())
            lista_objetos[indice].nombre=txtnom.get()
            lista_objetos[indice].pre_requisito=txtPre.get()
            lista_objetos[indice].semestre=txtSem.get()
            lista_objetos[indice].obligatorio=txtOpc.get()
            lista_objetos[indice].creditos=txtCred.get()
            lista_objetos[indice].estado=txtEst.get()
            txtCod.delete(0,'end')
            txtnom.delete(0,'end')
            txtEst.delete(0,'end')
            txtPre.delete(0,'end')
            txtSem.delete(0,'end')
            txtOpc.delete(0,'end')
            txtCred.delete(0,'end')
            txtEst.delete(0,'end')
            messagebox.showinfo("Aviso","Cursos Actualizados Correctamente")      
    btnEditar=tkinter.Button(editar,text="Editar",command=btn_editar)
    btnEditar.place(x=120,y=250)

#version final
def ventana_eliminar_curso():
    gestionar.withdraw()
    eliminar=tkinter.Tk()
    eliminar.title("Eliminar Curso")
    eliminar.geometry("500x250")
    cod_curso=tkinter.Label(eliminar,text="Codigo del Curso")
    cod_curso.place(x=100,y=75)
    txtCod=tkinter.Entry(eliminar)
    txtCod.place(x=200,y=75,width=100,height=20)
    def eliminar_curso_boton():
        try:
            global filas
            codigo=txtCod.get()
            indice=Curso.buscar_curso(codigo)
            lista_objetos.remove(lista_objetos[indice])
            indice_lista_cod=Curso.borrar_codigo(codigo)
            codis.remove(codis[indice_lista_cod])
            messagebox.showinfo("Aviso","Curso Eliminado Correctamente")
            filas=Curso.cantidad_cursos()
            txtCod.delete(0,'end')
        except TypeError:
            messagebox.showwarning("Error","Registro Inexistente")
    btnEliminar=tkinter.Button(eliminar,text="Eliminar",command=eliminar_curso_boton)
    btnEliminar.place(x=150,y=120)
    def regresar_de_eliminar_principal():
        gestionar.deiconify()
        eliminar.withdraw()
    btnRegresar=tkinter.Button(eliminar,text="Regresar",command=regresar_de_eliminar_principal)
    btnRegresar.place(x=240,y=120)    

def ventana_gestionar():
    global gestionar
    principal.withdraw()
    gestionar=tkinter.Tk()
    gestionar.title("Gestionar")
    gestionar.geometry("500x500")
    btnListar=tkinter.Button(gestionar,text="Listar Cursos",command=ventana_listar_cursos)
    btnListar.place(x=200,y=100)
    btnAgregar=tkinter.Button(gestionar,text="Agregar Curso",command=ventana_agregar_curso)
    btnAgregar.place(x=200,y=150)
    btnEditar=tkinter.Button(gestionar,text="Editar Curso",command=ventana_editar_curso)
    btnEditar.place(x=200,y=200)
    btnEliminar=tkinter.Button(gestionar,text="Eliminar Curso",command=ventana_eliminar_curso)
    btnEliminar.place(x=200,y=250) 
    def funcion_regresar_gestionar_principal():
        principal.deiconify()
        gestionar.withdraw()
    Regresar=tkinter.Button(gestionar,text="Regresar",command=funcion_regresar_gestionar_principal)
    Regresar.place(x=200,y=300)        

def ventana_conteo():
    fuente=Font(family="Roboto Cn",size=14)
    principal.withdraw()
    conteo=tkinter.Tk()
    conteo.title("Conteo")
    conteo.geometry("500x500")
    titulo=tkinter.Label(conteo,text="Creditos aprobados, Cursando y pendientes Totales",font=fuente)
    titulo.place(x=30,y=20)
    aprobados=tkinter.Label(conteo,text="Creditos Aprobados: "+str(Curso.conteo_creditos_aprobados_totales()), font=fuente)
    aprobados.place(x=30,y=50)
    cursando=tkinter.Label(conteo,text="Creditos Cursando: "+str(Curso.conteo_creditos_cursando_totales()),font=fuente)
    cursando.place(x=30,y=80)
    pendientes=tkinter.Label(conteo,text="Creditos Pendientes: "+str(Curso.conteo_creditos_pendientes_totales()),font=fuente)
    pendientes.place(x=30,y=110)
    obligatorios=tkinter.Label(conteo,text="Creditos Aprobados hasta semestre N: ")
    obligatorios.place(x=30,y=140)
    txtCobligatorios=tkinter.Entry(conteo)
    txtCobligatorios.place(x=235,y=140,width=70,height=20)
    Semestre=tkinter.Label(conteo,text="Semestre")
    Semestre.place(x=60,y=180)
    spin1=ttk.Spinbox(conteo,width=10,from_=1,to=10,increment=1)
    spin1.place(x=135,y=180)
    def btn_contar_semestre_n():
        txtCobligatorios.delete(0,'end')
        semestre=spin1.get()
        obligatorios.config(text="Creditos Aprobados hasta semestre "+semestre+":")
        txtCobligatorios.insert(0,str(Curso.conteo_semestre_n(int(semestre))))
        
    btnContarObligatorios=tkinter.Button(conteo,text="Contar",command=btn_contar_semestre_n)
    btnContarObligatorios.place(x=235,y=180)
    creditos=tkinter.Label(conteo,text="creditos totales aprobados, cursando y pendientes")
    creditos.place(x=30,y=220)
    Semestre2=tkinter.Label(conteo,text="Semestre")
    Semestre2.place(x=60,y=260)
    txttotal=tkinter.Entry(conteo)
    txttotal.place(x=300,y=220,width=70,height=20)
    txttotal.insert(0,str(int(Curso.conteo_creditos_aprobados_totales())+int(Curso.conteo_creditos_cursando_totales())+int(Curso.conteo_creditos_pendientes_totales())))
    spin2=ttk.Spinbox(conteo,width=10,from_=1,to=10,increment=1)
    spin2.place(x=135,y=260)
    def btn_contar_creditos_s():
        txttotal.delete(0,'end')
        Semestre=spin2.get()
        aprobados.config(font=fuente,text="Creditos Aprobados: "+str(Curso.conteo_creditos_aprobados(int(Semestre))))
        cursando.config(font=fuente,text="Creditos Cursando: "+str(Curso.conteo_creditos_cursando(int(Semestre))))
        pendientes.config(font=fuente,text="Creditos Pendientes: "+str(Curso.conteo_creditos_pendientes(int(Semestre))))
        titulo.config(font=fuente,text="Creditos aprobados, Cursando y pendientes del Semestre "+Semestre)
        a=str(int(Curso.conteo_creditos_aprobados(int(Semestre)))+int(Curso.conteo_creditos_cursando(int(Semestre)))+int(Curso.conteo_creditos_pendientes(int(Semestre))))
        txttotal.insert(0,a)

    btnContarSemestre=tkinter.Button(conteo,text="Contar",command=btn_contar_creditos_s)
    btnContarSemestre.place(x=235,y=260)
    def funcion_regresar_conteo_principal():
        principal.deiconify()
        conteo.withdraw()
    Regresar=tkinter.Button(conteo,text="Regresar",command=funcion_regresar_conteo_principal)
    Regresar.place(x=400,y=400)   

def funcion_salir():
    quit()



inicio()