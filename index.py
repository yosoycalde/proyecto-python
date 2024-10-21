import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x300")

etiqueta = tkinter.Label(ventana, text="hola mundo" ,bg="red")
etiqueta.pack()
 

ventana.mainloop()

