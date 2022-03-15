
print('_____________________________________________________________')
def saludo(nombre):
    print()
    print('Hola {}'.format(nombre),', bienvenido.')
    
x = input('Ingrese su nombre: ')
saludo(x)

consumo_energia = {
    'Coca Codo Sinclair': {
        'Quito': { 'consumos':(400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300 , 213),'tarifa': 65},
        'Guayaquil': { 'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
    },
}
op = 0
def menu():
    print()
    print()
    print("ESCOJA UNA OPCIÓN DISPONIBLE:")
    print('<1> Total de MWH por dicha Planta y Ciudad.')
    print('<2> Total de MWH por cada Planta')
    print('<3> Total de dinero recaudado por cada región')
    print('<4> SALIR')
    print('_____________________________________________________________')

while op!= 1:
    menu()
    ops = int(input('Ingrese una opcion:'))
    if ops == 1 :
      while op != 1:
          print()
          print('Plantas: COCA CODO SINCLAIR / SOPLADORA')
          print()
          print('Ciudades: GUAYAQUIL / QUITO / LOJA')
          print()

        
          
          p = str(input('Ingrese el nombre de la Planta (En mayúscula escriba): '))
          c = str(input('Ingrese el nombre de la Ciudad (En mayúscula escriba): '))
          print('_____________________________________________________________')
          if p == 'COCA CODO SINCLAIR' and c =='QUITO':
            #COCA QUITO
            tarifa_coca_quito = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']
            print('Consumo Total:', sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos']),'MWh')
            break 
         

          elif p == 'COCA CODO SINCLAIR' and c == 'GUAYAQUIL':
            #COCA GUAYAQUIL
            tarifa_coca_guayaquil = consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa']
            print('Consumo Total:', sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']),'MWh')
            break
         

          elif p == 'SOPLADORA' and c == 'GUAYAQUIL':
            #SOPLADORA GUAYAQUIL
            tarifa_sopladora_guayaquil = consumo_energia['Sopladora']['Guayaquil']['tarifa']
            print('Consumo Total:', sum(consumo_energia['Sopladora']['Guayaquil']['consumos']),'MWh')
            break
          

          elif p == 'SOPLADORA' and c == 'QUITO':
            #SOPLADORA QUITO
            tarifa_sopladora_quito = consumo_energia['Sopladora']['Quito']['tarifa']
            print('Consumo total:', sum(consumo_energia['Sopladora']['Quito']['consumos']),'MWh')
            break
          

          elif p == 'SOPLADORA' and c == 'LOJA':
            #SOPLADORA LOJA
            tarifa_sopladora_loja = consumo_energia['Sopladora']['Loja']['tarifa']
            print('Consumo total:', sum(consumo_energia['Sopladora']['Loja']['consumos']),'MWh')
            break
          

          else:
           print('¡DATOS INCORRECTOS!\nINGRESE NUEVAMENTE LA INFORMACIÓN DE LA PLANTA Y LA CIUDAD')
      

    elif ops == 2:

      while op !=2:
        print()
        print('QUITO / GUAYAQUIL / LOJA')
        print()
        print('_____________________________________________________________')
        

          
        plantas = {
        'Quito': ('Coca Codo Sinclair', 'Sopladora'),
        'Guayaquil': ('Coca Codo Sinclair', 'Sopladora'),
        'Loja': ('Sopladora')
        }
        c = str(input('Ingrese el nombre de la ciudad(mayus): '))
        if c == 'QUITO':
            print('Las plantas que producen energia en esta ciudad son', plantas['Quito'])
            print('COCA CODO SINCLAIR:', sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos']),'MWh')
            print('SOPLADORA:', sum(consumo_energia['Sopladora']['Quito']['consumos']),'MWh')
            break
        elif c == 'GUAYAQUIL':
            print('Las plantas que producen energia en esta ciudad son', plantas['Guayaquil'])
            print('COCA CODO SINCLAIR:', sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']),'MWh')
            print('SOPLADORA:', sum(consumo_energia['Sopladora']['Guayaquil']['consumos']),'MWh')
            break    
        elif c == 'LOJA':
            print('Las plantas que producen energia en esta ciudad son', plantas['Loja'])
            print('SOPLADORA:', sum(consumo_energia['Sopladora']['Loja']['consumos']),'MWh')
            break
        else:
             print('¡LA CIUDAD DE LA QUE DESEA OBTENER INFORMACION NO ENTREGA ENERGIA!')
        
    elif ops == 3:
     while op!=4:
        print()
        print('REGIONES: COSTA / SIERRA / ORIENTE')
        print()
        print('_____________________________________________________________')

        informacion = {
        'costa': ('Guayaquil', 'Manta'),
        'sierra': ('Quito', 'Ambato', 'Loja'),
        'oriente': ('Tena', 'Nueva Loja')
        }
        r = str(input('Ingrese el nombre de una region(mayus): '))
        if r == 'SIERRA':
              qui_consu_a = sum(consumo_energia['Coca Codo Sinclair']['Quito']['consumos'])
              qui_consu_b = sum(consumo_energia['Sopladora']['Quito']['consumos'])
              qui_tarf_a = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']
              qui_tarf_b = consumo_energia['Sopladora']['Quito']['tarifa']
              lo_cons_a = sum(consumo_energia['Sopladora']['Loja']['consumos'])
              lo_tarf_b = consumo_energia['Sopladora']['Loja']['tarifa']
              print('Los ingresos de la region SIERRA:', '$',((qui_consu_a*qui_tarf_a) + (qui_consu_b*qui_tarf_b)) + (lo_cons_a*lo_tarf_b))
              break
        elif r == 'COSTA':
             gua_consu_a = sum(consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos'])
             gua_consu_b = sum(consumo_energia['Sopladora']['Guayaquil']['consumos'])
             gua_tarf_a = consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa']
             gua_tarf_b = consumo_energia['Sopladora']['Guayaquil']['tarifa']
             print('Los ingresos de la region COSTA:',((gua_consu_a * gua_tarf_a) + (gua_consu_b * gua_tarf_b)))
             break
        else :
            print('LA REGION ASIGNADA NO CONSTA EN EL SISTEMA.')

    elif ops == 4:
        quit()
