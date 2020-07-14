from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""
resultado=0
limpiarPantalla=False


# ========== PANTALLA ==================================

numeroPantalla=StringVar()


pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=5, pady=5, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

# numeroPantalla.set("0") ===ver si no es necesario

#===== PULSACIONES EN PANTALLA ========================

def numeroPulsado(num):
    
 
    global operacion
    global limpiarPantalla
    
    if limpiarPantalla!=False:
        
        numeroPantalla.set(num)
        limpiarPantalla=False

    else:
           
        numeroPantalla.set(numeroPantalla.get()+ num)
 

 
#===================== SUMA =========================   

def suma(num):
    
    global operacion
    global resultado
    global limpiarPantalla
    
    resultado+= int(num)
    
    operacion="suma"
    
    limpiarPantalla=True
    
    numeroPantalla.set(resultado)


#===================== RESTA =========================  
num1=0
contador_resta=0

def resta(num):
    
    global operacion
    global resultado
    global num1
    global contador_resta
    global limpiarPantalla
    

    if contador_resta==0:
        num1=int(num)
        
        resultado=num1
    
    else:

        if contador_resta==1:
            
            resultado=num1-int(num)
        
        else:
            
            resultado-= int(resultado)-int(num)
         
        numeroPantalla.set(resultado)
    
        resultado=numeroPantalla.get()   

    contador_resta=contador_resta+1
        
    operacion="resta"
        
    limpiarPantalla=True


#===================== RESULTADO =========================      
    
def elresultado():
    
    global resultado
    global operacion
    global contador_resta
    
    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
    
        resultado=0
    
    elif operacion=="resta":
        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
        
        resultado=0
        
        contador_resta=0
    
    
# ========== FILA 1 ==================================

boton7=Button(miFrame, text="7", width=10, command=lambda:numeroPulsado("7")).grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=10, command=lambda:numeroPulsado("8")).grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=10, command=lambda:numeroPulsado("9")).grid(row=2, column=3)

botonDiv=Button(miFrame, text="/", width=10).grid(row=2, column=4)

# ========== FILA 2 ==================================

boton4=Button(miFrame, text="4", width=10, command=lambda:numeroPulsado("4")).grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=10, command=lambda:numeroPulsado("5")).grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=10, command=lambda:numeroPulsado("6")).grid(row=3, column=3)

botonMul=Button(miFrame, text="x", width=10).grid(row=3, column=4)

# ========== FILA 3 ==================================

boton1=Button(miFrame, text="1", width=10, command=lambda:numeroPulsado("1")).grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=10, command=lambda:numeroPulsado("2")).grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=10, command=lambda:numeroPulsado("3")).grid(row=4, column=3)

botonRes=Button(miFrame, text="-", width=10, command=lambda:resta(numeroPantalla.get())).grid(row=4, column=4)

# ========== FILA 4 ==================================

botonComa=Button(miFrame, text=",", width=10, command=lambda:numeroPulsado(",")).grid(row=5, column=1)
boton0=Button(miFrame, text="0", width=10, command=lambda:numeroPulsado("0")).grid(row=5, column=2)
botonIgu=Button(miFrame, text="=", width=10, command=lambda:elresultado()).grid(row=5, column=3)

botonSum=Button(miFrame, text="+", width=10, command=lambda:suma(numeroPantalla.get())).grid(row=5, column=4)










raiz.mainloop()