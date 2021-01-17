f = 6
c = 3

matriz_main = []

f_m = 4
c_m = 2

m_l = []
m_k = []
m_m = []
m_j = []
m_v = []
m_s = []

f_p = 6
c_p = 6

m_p = []

class Menus:
    for i in range(f_m):
        m_l.append(['vacio']*c_m)
    for i in range(f_m):
        m_k.append(['vacio']*c_m)
    for i in range(f_m):
        m_m.append(['vacio']*c_m)
    for i in range(f_m):
        m_j.append(['vacio']*c_m)
    for i in range(f_m):
        m_v.append(['vacio']*c_m)
    for i in range(f_m):
        m_s.append(['vacio']*c_m)
        
    m_l[0][0] = 'Combo 1'
    m_l[0][1] = '1000'
    m_l[1][0] = 'Combo 2'
    m_l[1][1] = '2000'
    m_l[2][0] = 'Combo 3'
    m_l[2][1] = '4000'
    m_l[3][0] = 'Combo 4'
    m_l[3][1] = '4000'

    m_k[0][0] = 'Combo 1'
    m_k[0][1] = '1000'
    m_k[1][0] = 'Combo 2'
    m_k[1][1] = '2000'
    m_k[2][0] = 'Combo 3'
    m_k[2][1] = '4000'
    m_k[3][0] = 'Combo 3'
    m_k[3][1] = '4000'

    m_m[0][0] = 'Combo 1'
    m_m[0][1] = '1000'
    m_m[1][0] = 'Combo 2'
    m_m[1][1] = '2000'
    m_m[2][0] = 'Combo 3'
    m_m[2][1] = '4000'
    m_m[3][0] = 'Combo 3'
    m_m[3][1] = '4000'

    for i in range(f_p):
        m_p.append(['vacio']*c_p)
        
    def ingresarmenu(self, tipomatriz):
        if tipomatriz in ('lunes','Lunes','LUNES'):
            for i in range (f_m):
                print ('\n\nDigite Menu del Food Truck.\n')
                combo = str(input('Digite nombre del combo: '))
                m_l[i][0] = combo
                precio = str(input('Digite precio: '))
                m_l[i][1] = precio
                print()
                    
        if tipomatriz in ('martes','Martes','MARTES'):
            for i in range (f_m):
                print ('\n\nDigite Menu del Food Truck.\n')
                combo = str(input('Digite nombre del combo: '))
                m_k[i][0] = combo
                precio = str(input('Digite precio: '))
                m_k[i][1] = precio
                print()

        if tipomatriz in ('miercoles','Miercoles','MIERCOLES'):
            for i in range (f_m):
                print ('\n\nDigite Menu del Food Truck.\n')
                combo = str(input('Digite nombre del combo: '))
                m_m[i][0] = combo
                precio = str(input('Digite precio: '))
                m_m[i][1] = precio
                print()
                    
        if tipomatriz in ('jueves','Jueves','JUEVES'):
            for i in range (f_m):
                print ('\n\nDigite Menu del Food Truck.\n')
                combo = str(input('Digite nombre del combo: '))
                m_j[i][0] = combo
                precio = str(input('Digite precio: '))
                m_j[i][1] = precio
                print()

        if tipomatriz in ('viernes','Viernes','VIERNES'):
            for i in range (f_m):
                print ('\n\nDigite Menu del Food Truck.\n')
                combo = str(input('Digite nombre del combo: '))
                m_v[i][0] = combo
                precio = str(input('Digite precio: '))
                m_v[i][1] = precio
                print()

        if tipomatriz in ('sabado','Sabado','SABADO'):
            for i in range (f_m):
                print ('\n\nDigite Menu del Food Truck.\n')
                combo = str(input('Digite nombre del combo: '))
                m_s[i][0] = combo
                precio = str(input('Digite precio: '))
                m_s[i][1] = precio
                print()
                    
    def imprimirmenu(self,tipomatriz):
               
        print('\n\nMenu - Precio')
        
        if tipomatriz in ('lunes','Lunes','LUNES'):
            for i in m_l:
                for j in i:
                    print ('[ ',j,' ]',end=' ')
                print ()
            print ()
            
        if tipomatriz in ('martes','Martes','MARTES'):
            for i in m_k:
                for j in i:
                    print ('[ ',j,' ]',end=' ')
                print ()
            print ()

        if tipomatriz in ('miercoles','Miercoles','MIERCOLES'):
            for i in m_m:
                for j in i:
                    print ('[ ',j,' ]',end=' ')
                print ()
            print ()

        if tipomatriz in ('jueves','Jueves','JUEVES'):
            for i in m_j:
                for j in i:
                    print ('[ ',j,' ]',end=' ')
                print ()
            print ()

        if tipomatriz in ('viernes','Viernes','VIERNES'):
            for i in m_v:
                for j in i:
                    print ('[ ',j,' ]',end=' ')
                print ()
            print ()

        if tipomatriz in ('sabado','Sabado','SABADO'):
            for i in m_s:
                for j in i:
                    print ('[ ',j,' ]',end=' ')
                print ()
            print ()

    def modificarmenu(self,tipomatriz):
        tipocombo = str(input('\nDigite combo que desea modificar: '))
        limpiar()
        for i in range (f_m):
            for j in range (c_m):
                if tipomatriz in ('lunes','Lunes','LUNES'):
                    if m_l[i][j] == tipocombo:
                        tipodato = int(input('\t1. Nombre del Combo.'+
                                             '\t2. Precio.'+
                                             '\n'+
                                             '\nDigite dato que sea modificar: '))
                        limpiar()
                        if tipodato == 1:
                            m_l[i][0] = str(input('\nDigite nombre: '))
                            Menus.imprimirmenu(None,tipomatriz)
                        else:
                            m_l[i][1] = str(input('\nDigite precio: '))
                            Menus.imprimirmenu(None,tipomatriz)
                            
                if tipomatriz in ('martes','Martes','MARTES'):
                    if m_k[i][j] == tipocombo:
                        tipodato = int(input('\t1. Nombre del Combo.'+
                                             '\t2. Precio.'+
                                             '\n'+
                                             '\nDigite dato que sea modificar: '))
                        limpiar()
                        if tipodato == 1:
                            m_k[i][0] = str(input('\nDigite nombre: '))
                            Menus.imprimirmenu(None,tipomatriz)
                        else:
                            m_k[i][1] = str(input('\nDigite precio: '))
                            Menus.imprimirmenu(None,tipomatriz)
                            
                if tipomatriz in ('miercoles','Miercoles','MIERCOLES'):
                    if m_m[i][j] == tipocombo:
                        tipodato = int(input('\t1. Nombre del Combo.'+
                                             '\t2. Precio.'+
                                             '\n'+
                                             '\nDigite dato que sea modificar: '))
                        limpiar()
                        if tipodato == 1:
                            m_m[i][0] = str(input('\nDigite nombre: '))
                            Menus.imprimirmenu(None,tipomatriz)
                        else:
                            m_m[i][1] = str(input('\nDigite precio: '))
                            Menus.imprimirmenu(None,tipomatriz)

                if tipomatriz in ('jueves','Jueves','JUEVES'):
                    if m_j[i][j] == tipocombo:
                        tipodato = int(input('\t1. Nombre del Combo.'+
                                             '\t2. Precio.'+
                                             '\n'+
                                             '\nDigite dato que sea modificar: '))
                        limpiar()
                        if tipodato == 1:
                            m_j[i][0] = str(input('\nDigite nombre: '))
                            Menus.imprimirmenu(None,tipomatriz)
                        else:
                            m_j[i][1] = str(input('\nDigite precio: '))
                            Menus.imprimirmenu(None,tipomatriz)

                if tipomatriz in ('viernes','Viernes','VIERNES'):
                    if m_v[i][j] == tipocombo:
                        tipodato = int(input('\t1. Nombre del Combo.'+
                                             '\t2. Precio.'+
                                             '\n'+
                                             '\nDigite dato que sea modificar: '))
                        limpiar()
                        if tipodato == 1:
                            m_v[i][0] = str(input('\nDigite nombre: '))
                            Menus.imprimirmenu(None,tipomatriz)
                        else:
                            m_v[i][1] = str(input('\nDigite precio: '))
                            Menus.imprimirmenu(None,tipomatriz)
                

    def eliminarmenu(self,tipomatriz):
        for i in range (f_m):
            for j in range (c_m):
                if tipomatriz in ('lunes','Lunes','LUNES'):
                    for i_1 in range (f_m):
                        for j_1 in range (c_m):
                            m_l[i_1][j_1] = 'vacio'
                            
                if tipomatriz in ('martes','Martes','MARTES'):
                    for i_1 in range (f_m):
                        for j_1 in range (c_m):
                            m_k[i_1][j_1] = 'vacio'
                            
                if tipomatriz in ('miercoles','Miercoles','MIERCOLES'):
                    for i_1 in range (f_m):
                        for j_1 in range (c_m):
                            m_m[i_1][j_1] = 'vacio'
                            
                if tipomatriz in ('jueves','Jueves','JUEVES'):
                    for i_1 in range (f_m):
                        for j_1 in range (c_m):
                            m_j[i_1][j_1] = 'vacio'
                            
                if tipomatriz in ('viernes','Viernes','VIERNES'):
                    for i_1 in range (f_m):
                        for j_1 in range (c_m):
                            m_v[i_1][j_1] = 'vacio'
                            
                if tipomatriz in ('sabado','Sabado','SABADO'):
                    for i_1 in range (f_m):
                        for j_1 in range (c_m):
                            m_s[i_1][j_1] = 'vacio'

    def pedido(self):
        print ("\n\nIngrese los siguientes datos:")
        nuevo = 1
        i = 0
        while nuevo == 1:
            if m_p[i][0] == 'vacio':
                print()
                combo = str(input('Digite Combo: '))
                nombre = str(input('Digite Nombre Completo: '))
                numero = str(input('Digite Numero Telefonico: '))
                ubicacion = str(input('Digite su Ubicacion de Entrega: '))
                
                des_hora = str(input('Desea programar hora de entrega? Si/No: '))
                if des_hora == 'Si':
                    hora = str(input('Digite hora de entrega: '))
                elif des_hora == 'No':
                    hora = 'Inmediatamente'
                    
                pago = str(input('Digite Forma de Pago Efectivo/Tarjeta: '))
            
                m_p[i][0] = combo
                m_p[i][1] = nombre
                m_p[i][2] = numero
                m_p[i][3] = ubicacion
                m_p[i][4] = hora
                m_p[i][5] = pago
                print ()
                Menus.imprimirpedido(self)
                print('\n\nDesea realizar otro pedido? Si/No: ',end='')
                new = str(input())
            
                if new == 'Si':
                    nuevo = 1
                    i = i + 1
                elif new == 'No':
                    nuevo = 0
            else:
                i = i + 1
                    
        
        print()
        print('\n\nEl pedido se ha realizado con exito....\n\n')
        print('Dentro de apoximadamente 20 minutos sera entregado su pedido.')
        
    def imprimirpedido(self):
        for i in m_p:
            for j in i:
                if j != 'vacio':
                    print (j,' - ',end=' ')

            if j != 'vacio':
                print ()
        print ()
        
mat = Menus()
                
class Matrices:
    for i in range(f):
        matriz_main.append(['vacio']*c)
            
    matriz_main[0][0] = 'La ricura (Comida tipica)'
    matriz_main[0][1] = 'Lunes'
    matriz_main[0][2] = '10 a.m. - 9 p.m.'
    matriz_main[1][0] = 'Master Che (Argentino)'
    matriz_main[1][1] = 'Martes'
    matriz_main[1][2] = '10 a.m. - 9 p.m.'
    matriz_main[2][0] = 'Mr Shawarma (Libanesa)'
    matriz_main[2][1] = 'Miercoles'
    matriz_main[2][2] = '10 a.m. - 9 p.m.'
    
    def ingresarfoodtruck(self):
        nuevo = 1
        i = 0
        while nuevo == 1:
            if matriz_main[i][0] == 'vacio':
                    
                print ('\n\nDigite Food Truck numero '+str(i+1)+' de la semana.\n')
                nombrefoodt = str(input('Digite nombre del Food Truck: '))
                diafoodt = str(input('Digite dia restante del Food Truck: '))
                horafoodt = str(input('Digite horario del Food Truck: '))
                matriz_main[i][0] = nombrefoodt
                matriz_main[i][1] = diafoodt
                matriz_main[i][2] = horafoodt
                        
                Menus.ingresarmenu(None,diafoodt)
                Menus.imprimirmenu(None,diafoodt)
                print('Desea ingresar otro Food Truck Si/No: ',end='')
                new = str(input())

                if new == 'Si':
                    nuevo = 1
                    i = i + 1
                elif new == 'No':
                    nuevo = 0
            else:
                i = i + 1

                    
    def imprimir(self):
        print ('\n\nFOOD TRUCK - DIA - HORARIO')
        print()
        for i in matriz_main:
            for j in i:
                if j != 'vacio':
                    print (j,' - ',end=' ')

            if j != 'vacio':
                print ()
        print ()

    def modificar(self):
        x.imprimir()
        tipofood = str(input('\nDigite el DIA del Food Truck que desea modificar: '))
        limpiar()
        print ("\n\nSelecciona una opción\n")
        print ("\t1. Modificar Food Truck.")
        print ("\t2. Modifcar Menu.")
        opcionfood = int(input('\nDigite opcion: '))
        limpiar()
        if opcionfood == 1:
            for i in range (f):
                for j in range (c):
                    if matriz_main[i][j] == tipofood:
                        tipodato = int(input('\t1. Nombre del Food Truck.'+
                                             '\t2. Horario de atencion.'+
                                             '\n'+
                                             '\nDigite dato que sea modificar: '))
                        limpiar()
                        if tipodato == 1:
                            matriz_main[i][0] = str(input('\nDigite nombre: '))
                            x.imprimir()
                        else:
                            matriz_main[i][2] = str(input('\nDigite horario: '))
                            x.imprimir()
        else:
            Menus.imprimirmenu(None,tipofood)
            Menus.modificarmenu(None,tipofood)
            
    def eliminar(self):
        x.imprimir()
        tipofood = str(input('\nDigite dia del Food Truck que desea eliminar: '))
        for i in range (f):
            for j in range (c):
                if matriz_main[i][j] == tipofood:
                    for j_1 in range (c):
                        matriz_main[i][j_1] = 'vacio'
                        Menus.eliminarmenu(None,tipofood)
        
x = Matrices()

def menu_principal():
    print ("Selecciona una opción\n")
    print ("\t1. Food Trucks de la semana")
    print ("\t2. Salir")

def menu_op1_0():
    print ("Selecciona una opción\n")
    print ("\t1. Selecionar Food Truck")
    print ("\t2. Ver Pedidos")
    print ("\t3. Añadir Food Truck")
    print ("\t4. Modificar Food Truck")
    print ("\t5. Eliminar Food Truck")
    print ('')
    print ("\t6. Salir")
    
def menu_op1_5():
    opcion_op1_5 = 0
    while(opcion_op1_5 != 7):
        #print ("\nDigite un Food Truck para ver el menu.\n")
        op = 0
        op1 = 0
        op2 = 0
        op3 = 0
        op4 = 0
        op5 = 0
        op6 = 0
        op7 = 0
        
        if matriz_main[0][0] != 'vacio':
            op = op + 1
            op1 = op
            print ("\t"+str(op1)+". "+str(matriz_main[0][0]))
        
        if matriz_main[1][0] != 'vacio':
            op = op + 1
            op2 = op
            print ("\t"+str(op2)+". "+str(matriz_main[1][0]))
        
        if matriz_main[2][0] != 'vacio':
            op = op + 1
            op3 = op
            print ("\t"+str(op3)+". "+str(matriz_main[2][0]))
        
        if matriz_main[3][0] != 'vacio':
            op = op + 1
            op4 = op
            print ("\t"+str(op4)+". "+str(matriz_main[3][0]))
        
        if matriz_main[4][0] != 'vacio':
            op = op + 1
            op5 = op
            print ("\t"+str(op5)+". "+str(matriz_main[4][0]))
        
        if matriz_main[5][0] != 'vacio':
            op = op + 1
            op6 = op
            print ("\t"+str(op6)+". "+str(matriz_main[5][0]))
        
        print ('')
        op = op + 1
        op7 = op
        
        print ("\t"+str(op7)+". Salir")

        print ("\nDigite una opcion: ",end='')
        opcion_op1_5 = input()
        
        if opcion_op1_5 == (str(op1)):
            limpiar()
            Menus.imprimirmenu(None,'Lunes')
            menu_op2()
            opcion_op2 = input()
                
            if opcion_op2 in ('si','Si','SI'):
                Menus.pedido(None)
            else:
                limpiar()
                    
        elif opcion_op1_5 == (str(op2)):
            limpiar()
            Menus.imprimirmenu(None,'Martes')
            menu_op2()
            opcion_op2 = input()
                
            if opcion_op2 in ('si','Si','SI'):
                Menus.pedido(None)
            else:
                limpiar()
                    
        elif opcion_op1_5 == (str(op3)):
            limpiar()
            Menus.imprimirmenu(None,'Miercoles')
            menu_op2()
            opcion_op2 = input()
                
            if opcion_op2 in ('si','Si','SI'):
                Menus.pedido(None)
            else:
                limpiar()
                    
        elif opcion_op1_5 == (str(op4)):
            limpiar()
            Menus.imprimirmenu(None,'Jueves')
            menu_op2()
            opcion_op2 = input()
                
            if opcion_op2 in ('si','Si','SI'):
                Menus.pedido(None)
            else:
                limpiar()
                
        elif opcion_op1_5 == (str(op5)):
            limpiar()
            Menus.imprimirmenu(None,'Viernes')
            menu_op2()
            opcion_op2 = input()
                
            if opcion_op2 in ('si','Si','SI'):
                Menus.pedido(None)
            else:
                limpiar()
                
        elif opcion_op1_5 == (str(op6)):
            limpiar()
            Menus.imprimirmenu(None,'Sabado')
            menu_op2()
            opcion_op2 = input()
                
            if opcion_op2 in ('si','Si','SI'):
                Menus.pedido(None)
            else:
                limpiar()
                
        elif opcion_op1_5 == (str(op7)):
            break
    

def menu_op2():
    print ("\nDesea realizar un pedido? Si/No: ",end='')
    
def limpiar():
    print ("\n" * 50)

limpiar()
menu_principal()
print ("\nDigite una opcion: ",end='')
opcion_principal = input()

while True:
    if opcion_principal == '1':
        limpiar()
        x.imprimir()
        menu_op1_0()
        print ("\nDigite una opcion: ",end='')
        opcion_op1_0 = input()
        
        if opcion_op1_0 == '1':
            limpiar()
            menu_op1_5()
            
        elif opcion_op1_0 == '2':
            limpiar()
            if m_p[0][0] == 'vacio':
                print ("\n\nNo hay pedidos...")
            else:
                print('\n\n')
                Menus.imprimirpedido(None)
            
        elif opcion_op1_0 == '3':
            limpiar()
            x.ingresarfoodtruck()
            x.imprimir()
            
            print('\nTodos los espacios estan llenos...\n')
            
            menu_op1_5()
            opcion_op1_5 = input('\nDigite una opcion: ')
            
            if opcion_op1_5 == '1':
                limpiar()
                Menus.imprimirmenu(None,'Lunes')
                
            elif opcion_op1_5 == '2':
                limpiar()
                Menus.imprimirmenu(None,'Martes')
                
            elif opcion_op1_5 == '3':
                limpiar()
                Menus.imprimirmenu(None,'Miercoles')
                
            elif opcion_op1_5 == '4':
                limpiar()
                Menus.imprimirmenu(None,'Jueves')
                
            elif opcion_op1_5 == '5':
                limpiar()
                Menus.imprimirmenu(None,'Viernes')
                
            elif opcion_op1_5 == '6':
                limpiar()
                Menus.imprimirmenu(None,'Sabado')
                
            elif opcion_op1_5 == '7':
                break

                
        elif opcion_op1_0 == '4':
            limpiar()
            x.modificar()
                
        elif opcion_op1_0 == '5':
            limpiar()
            x.eliminar()
                
        elif opcion_op1_0 == '6':
            limpiar()
            break
        
    elif opcion_principal == '2':
        limpiar()
        break
        
    elif opcion_principal in ('1','2'):
        print('Favor ingresar valor valido.')