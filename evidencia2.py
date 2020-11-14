import pandas as pd
import datetime
import csv
import os

ListaDeVentas = []
DatosDeVenta = []

Salir = False

Total = 0
PiezasCollar = 0
PiezasBolso = 0
PiezasBroche = 0
PiezasPendientes = 0
PiezasPinzas = 0

while Salir == False:
       
    with open('registros.csv', newline= '') as File:  
        reader = csv.reader(File)   
        
        for row in reader:
            DatosDeVenta.append(row)      
    ListaDeVentas.append(DatosDeVenta)
    DatosDeVenta = []
    
    
    print('======== MENU ========\n')

    print('1- REGISTRAR UNA VENTA')
    print('2- CONSULTAR UNA VENTA')
    print('3- SALIR')

    Opcion = int(input('Elige una opción: '))
    
    print('\n======================\n')

# REGISTRAR UNA NUEVA VENTA

    if Opcion == 1:
        Finalizar = False
        SubTotal= 0
        while Finalizar == False:
            
            print('===== NUEVA VENTA =====\n')
        
            print('1- Collar de piedras          -  $920 ')
            print('2- Bolso de terciopelo        -  $600')
            print('3- Kit de broches             -  $850')
            print('4- Pendientes de acero        -  $50')
            print('5- Pinzas P/ Armar bisuteria  -  $80')
                        
            Articulo = int(input('Elige un articulo: '))
 ## Articulo 1========================================================================================       
            if Articulo == 1:
                
                Cantidad = int(input('¿Cuantas piezas deseas?: '))                         
                PiezasCollar = PiezasCollar + Cantidad
                SubTotal = SubTotal + (920 * Cantidad) 
                
                print(f'Subtotal: ${SubTotal}')
                print('1- Seguir comprando     2- Finalizar la compra')
                              
                o = int(input('¿Que deseas hacer?: '))
                
                if o == 1:
                    pass
                elif o == 2:
                    
                    Fecha = datetime.date.today()
                    print(Fecha)
                    
                    Total = SubTotal
                    
                    registro = {
                    'Descripcion':['Collar de piedras','Bolso/terciopelo', 'Kit de broches','Pendientes/acero','Pinzas P/bisuteria'],
                    'Precio': ['920','600','850','50','80'],
                    'Piezas': [PiezasCollar,PiezasBolso,PiezasBroche,PiezasPendientes,PiezasPinzas],
                    'Total': ['-','-',Total,'-','-'],
                    'Fecha de venta': ['-', '-', '-' , '-' , Fecha]
                    }    
                    df = pd.DataFrame(data = registro)
                    
             
                    print('\n                ===TICKET===               \n') 
                    print(df)            
                        
                    df.to_csv('registros.csv', index = False)   
                   
                    print(f'\nMONTO A PAGAR: {Total}')
                                    
                    Finalizar = True
    
                else:
                    pass
    
## Articulo 2========================================================================================       
            if Articulo == 2:
                
                Cantidad = int(input('¿Cuantas piezas deseas?: '))                         
                PiezasBolso = PiezasBolso + Cantidad
                SubTotal = SubTotal + (600 * Cantidad) 
                
                print(f'Subtotal: ${SubTotal}')
                print('1- Seguir comprando     2- Finalizar la compra')
                              
                o = int(input('¿Que deseas hacer?: '))
                
                if o == 1:
                    pass
                elif o == 2:
                    
                    Fecha = datetime.date.today()
                    print(Fecha)
                    
                    Total = SubTotal
                    
                    registro = {
                    'Descripcion':['Collar de piedras','Bolso/terciopelo', 'Kit de broches','Pendientes/acero','Pinzas P/bisuteria'],
                    'Precio': ['920','600','850','50','80'],
                    'Piezas': [PiezasCollar,PiezasBolso,PiezasBroche,PiezasPendientes,PiezasPinzas],
                    'Total': ['-','-',Total,'-','-'],
                    'Fecha de venta': ['-', '-', '-' , '-' , Fecha]
                    }    
                    df = pd.DataFrame(data = registro)
                    
             
                    print('\n                ===TICKET===               \n') 
                    print(df)            
                        
                    df.to_csv('registros.csv', index = False)   
                   
                    print(f'\nMONTO A PAGAR: {Total}')
                                        
                    Finalizar = True
    
                else:
                    pass
            
            ## Articulo 3========================================================================================       
            if Articulo == 3:
                
                Cantidad = int(input('¿Cuantas piezas deseas?: '))                         
                PiezasBroche = PiezasBroche + Cantidad
                SubTotal = SubTotal + (850 * Cantidad) 
                
                print(f'Subtotal: ${SubTotal}')
                print('1- Seguir comprando     2- Finalizar la compra')
                              
                o = int(input('¿Que deseas hacer?: '))
                
                if o == 1:
                    pass
                elif o == 2:
                    
                    Fecha = datetime.date.today()
                    print(Fecha)
                    
                    Total = SubTotal
                    
                    registro = {
                    'Descripcion':['Collar de piedras','Bolso/terciopelo', 'Kit de broches','Pendientes/acero','Pinzas P/bisuteria'],
                    'Precio': ['920','600','850','50','80'],
                    'Piezas': [PiezasCollar,PiezasBolso,PiezasBroche,PiezasPendientes,PiezasPinzas],
                    'Total': ['-','-',Total,'-','-'],
                    'Fecha de venta': ['-', '-', '-' , '-' , Fecha]
                    }    
                    df = pd.DataFrame(data = registro)
                    
             
                    print('\n                ===TICKET===               \n') 
                    print(df)            
                        
                    df.to_csv('registros.csv', index = False)   
                   
                    print(f'\nMONTO A PAGAR: {Total}')
                                       
                    Finalizar = True
    
                else:
                    pass
    ##Articulo 4=============================================================            
                
            if Articulo == 4:
                
                Cantidad = int(input('¿Cuantas piezas deseas?: '))                         
                PiezasPendientes = PiezasPendientes + Cantidad
                SubTotal = SubTotal + (50 * Cantidad) 
                
                print(f'Subtotal: ${SubTotal}')
                print('1- Seguir comprando     2- Finalizar la compra')
                              
                o = int(input('¿Que deseas hacer?: '))
                
                if o == 1:
                    pass
                elif o == 2:
                    
                    Fecha = datetime.date.today()
                    print(Fecha)
                    
                    Total = SubTotal
                    
                    registro = {
                    'Descripcion':['Collar de piedras','Bolso/terciopelo', 'Kit de broches','Pendientes/acero','Pinzas P/bisuteria'],
                    'Precio': ['920','600','850','50','80'],
                    'Piezas': [PiezasCollar,PiezasBolso,PiezasBroche,PiezasPendientes,PiezasPinzas],
                    'Total': ['-','-',Total,'-','-'],
                    'Fecha de venta': ['-', '-', '-' , '-' , Fecha]
                    }    
                    df = pd.DataFrame(data = registro)
                    
             
                    print('\n                ===TICKET===               \n') 
                    print(df)            
                        
                    df.to_csv('registros.csv', index = False)   
                   
                    print(f'\nMONTO A PAGAR: {Total}')
                               
                    Finalizar = True
    
                else:
                    pass 
##Articulo 5===============================================
            if Articulo == 5:
                
                Cantidad = int(input('¿Cuantas piezas deseas?: '))                         
                PiezasPinzas = PiezasPinzas + Cantidad
                SubTotal = SubTotal + (80 * Cantidad) 
                
                print(f'Subtotal: ${SubTotal}')
                print('1- Seguir comprando     2- Finalizar la compra')
                              
                o = int(input('¿Que deseas hacer?: '))
                
                if o == 1:
                    pass
                elif o == 2:
                    
                    Fecha = datetime.date.today()
                    print(Fecha)
                    
                    Total = SubTotal
                    
                    registro = {
                    'Descripcion':['Collar de piedras','Bolso/terciopelo', 'Kit de broches','Pendientes/acero','Pinzas P/bisuteria'],
                    'Precio': ['920','600','850','50','80'],
                    'Piezas': [PiezasCollar,PiezasBolso,PiezasBroche,PiezasPendientes,PiezasPinzas],
                    'Total': ['-','-',Total,'-','-'],
                    'Fecha de venta': ['-', '-', '-' , '-' , Fecha]
                    }    
                    df = pd.DataFrame(data = registro)
                    
             
                    print('\n                ===TICKET===               \n') 
                    print(df)            
                        
                    df.to_csv('registros.csv', index = False)   
                   
                    print(f'\nMONTO A PAGAR: {Total}')             
                    
                    Finalizalr = True
    
                else:
                    pass

            ##Consultar datos por medio de fecha
            
    elif Opcion == 2:
        
        print('\n===CONSULTA DE VENTAS===\n')
        
        Año = str(input('Año: '))
        Mes = str(input('Mes: ' ))
        Dia = str(input('Dia: ' ))
        
        FechaIngresada = (f'{Año}-{Mes}-{Dia}')
           
        for fila in ListaDeVentas:
            FechaDeVenta = (fila[5][4])
            
            if FechaIngresada == FechaDeVenta:
                
                filapd = pd.DataFrame(data = fila)
                
                print('===============================================================')
                print(filapd)
                print('===============================================================')
            else:
                print('No existen ventas en la fecha ingresada')
    
    ## Salir del sistema
    elif Opcion == 3:
        
        Salir = True
        
        
            
    
            
        
        
        
        