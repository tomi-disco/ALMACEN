from almacen import Almacen
from carrito import Carrito
from deposito import Deposito
from gondola import Gondola
from inventario import Inventario
from proovedor import Proovedor

from gondolas.galletitas import Galletitas
from gondolas.gaseosa import Gaseosa
from gondolas.perfumeria import Perfumeria
from gondolas.alcohol import Alcohol
from gondolas.verduleria import Verduleria
from gondolas.carniceria import Carniceria
from gondolas.golosinas import Golosina
from gondolas.panaderia import Panaderia

almacen = Almacen()
carrito = Carrito()
proovedor=Proovedor()
inventario=Inventario(proovedor)

gondola_galletitas = Gondola("galletitas", 20)
gondola_gaseosa = Gondola("gaseosa", 20)
gondola_perfumeria = Gondola("perfumeria", 20)
gondola_alcohol = Gondola("alcohol", 20)
gondola_verduleria = Gondola("verduleria", 20)
gondola_carniceria=Gondola("carniceria",20)
gondola_panaderia=Gondola("panaderia",20)
gondola_golosinas=Gondola("golosinas",20)

deposito_galletitas = Deposito("galletitas", 25)
deposito_gaseosa = Deposito("gaseosa", 25)
deposito_perfumeria = Deposito("perfumeria", 25)
deposito_alcohol = Deposito("alcohol", 25)
deposito_verduleria = Deposito("verduleria", 25)
deposito_carniceria=Deposito("carniceria",25)
deposito_panaderia=Deposito("panaderia",25)
deposito_golosinas=Deposito("golosinas",25)


oreo = Galletitas(gondola_galletitas, "001", "Oreo", "Oreo", 118, 1000)
pepitos = Galletitas(gondola_galletitas, "002", "Pepitos", "Pepitos", 120, 800)
don_satur= Galletitas(gondola_galletitas, "003", "Don-Satur", "salados",200, 500)

coca = Gaseosa(gondola_gaseosa, "004", "Coca Cola", "Coca", 2.25, 2000)
sprite = Gaseosa(gondola_gaseosa, "005", "Sprite", "Sprite", 2.25, 1500)
paso= Gaseosa(gondola_gaseosa, "006", "Paso de los toros", "Pomelo", 1.5, 1000)

shampoo = Perfumeria(gondola_perfumeria, "007", "Dove", "Shampoo", 400, "ml", 2500)
jabon = Perfumeria(gondola_perfumeria, "008", "Rexona", "Jabon", 125, "gr", 1000)
acondicionador= Perfumeria(gondola_perfumeria, "009", "Dove", "Acondicionador", 400, "ml", 3000)

corona = Alcohol(gondola_alcohol, "010", "", "Corona", 1, 1800)
quilmes = Alcohol(gondola_alcohol, "011", "", "Quilmes", 1, 1400)
jagger= Alcohol(gondola_alcohol, "012", "", "Jaggermeister", 1, 2500)

manzana = Verduleria(gondola_verduleria, "013", "Tropical", "Manzana", 1, 1200)
banana = Verduleria(gondola_verduleria, "014", "Tropical", "Banana", 1, 900)
uva= Verduleria(gondola_verduleria, "015", "Tropical", "Uva", 1, 900)

asado= Carniceria(gondola_carniceria,"016","La Estancia","Asado",1,5000)
morcilla= Carniceria(gondola_carniceria,"017","La Estancia","Morcilla",0.2,500)
chorizo= Carniceria(gondola_carniceria,"018","La Estancia","Chorizo",0.25,600)

lactal=Panaderia(gondola_panaderia,"019","Bimbo","Lactal",0.5,500)
medialuna=Panaderia(gondola_panaderia,"020","","Medialunas",0.1,100)
vigilante=Panaderia(gondola_panaderia,"021","","Vigilante",0.15,150)

dientitos=Golosina(gondola_golosinas,"022","Arcor","Dientitos",50,250)
moritas=Golosina(gondola_golosinas,"023","Arcor","Moritas",50,250)
sapito=Golosina(gondola_golosinas,"024","Arcor","Sapito",10,150)


def cargar_varios(gondola, producto, cantidad):
    for i in range(cantidad):
        gondola.agregar(producto)

cargar_varios(gondola_galletitas,oreo,50)
cargar_varios(gondola_galletitas,pepitos,50)
cargar_varios(gondola_galletitas,don_satur,50)

cargar_varios(gondola_gaseosa,coca,50)
cargar_varios(gondola_gaseosa,sprite,50)
cargar_varios(gondola_gaseosa,paso,50)

cargar_varios(gondola_perfumeria,shampoo,50)
cargar_varios(gondola_perfumeria,jabon,50)
cargar_varios(gondola_perfumeria,acondicionador,50)

cargar_varios(gondola_alcohol,corona,50)
cargar_varios(gondola_alcohol,quilmes,50)
cargar_varios(gondola_alcohol,jagger,50)

cargar_varios(gondola_verduleria,manzana,50)
cargar_varios(gondola_verduleria,banana,50)
cargar_varios(gondola_verduleria,uva,50)

cargar_varios(gondola_carniceria,asado,50)
cargar_varios(gondola_carniceria,morcilla,50)
cargar_varios(gondola_carniceria,chorizo,50)

cargar_varios(gondola_panaderia,lactal,50)
cargar_varios(gondola_panaderia,medialuna,50)
cargar_varios(gondola_panaderia,vigilante,50)

cargar_varios(gondola_golosinas,dientitos,50)
cargar_varios(gondola_golosinas,moritas,50)
cargar_varios(gondola_golosinas,sapito,50)

def cargar_varios_deposito(deposito, producto, cantidad):
    for i in range(cantidad):
        deposito.agregar(producto)

cargar_varios_deposito(deposito_galletitas, oreo, 60)
cargar_varios_deposito(deposito_galletitas, pepitos, 60)
cargar_varios_deposito(deposito_galletitas, don_satur, 60)

cargar_varios_deposito(deposito_gaseosa, coca, 60)
cargar_varios_deposito(deposito_gaseosa, sprite, 60)
cargar_varios_deposito(deposito_gaseosa, paso, 60)

cargar_varios_deposito(deposito_perfumeria, shampoo, 60)
cargar_varios_deposito(deposito_perfumeria, jabon, 60)
cargar_varios_deposito(deposito_perfumeria, acondicionador, 60)

cargar_varios_deposito(deposito_alcohol, corona, 60)
cargar_varios_deposito(deposito_alcohol, quilmes, 60)
cargar_varios_deposito(deposito_alcohol, jagger, 60)

cargar_varios_deposito(deposito_verduleria, manzana, 60)
cargar_varios_deposito(deposito_verduleria, banana, 60)
cargar_varios_deposito(deposito_verduleria, uva, 60)

cargar_varios_deposito(deposito_carniceria, asado, 60)
cargar_varios_deposito(deposito_carniceria, morcilla, 60)
cargar_varios_deposito(deposito_carniceria, chorizo, 60)

cargar_varios_deposito(deposito_golosinas, dientitos, 60)
cargar_varios_deposito(deposito_golosinas, moritas, 60)
cargar_varios_deposito(deposito_golosinas, sapito, 60)

cargar_varios_deposito(deposito_panaderia, lactal, 60)
cargar_varios_deposito(deposito_panaderia, medialuna, 60)
cargar_varios_deposito(deposito_panaderia, vigilante, 60)


productos_galletitas = [oreo, pepitos,don_satur]
productos_gaseosa = [coca, sprite,paso]
productos_perfumeria = [shampoo, jabon,acondicionador]
productos_alcohol = [corona, quilmes,jagger]
productos_verduleria = [manzana, banana,uva]
productos_carniceria = [asado, morcilla, chorizo]
productos_golosinas = [dientitos, moritas,sapito]
productos_panaderia = [lactal, medialuna, vigilante]

def mostrar_menu_principal():
    print("\n===== SUPERMERCADO =====")
    print("a. Ir a góndola de alcohol (PROMO! 30% en la segunda unidad)")
    print("b. Ir a góndola de carniceria")
    print("c. Ir a góndola de galletitas (PROMO! 2x1 en cualquier marca)")
    print("d. Ir a góndola de gaseosa")
    print("e. Ir a góndola de golosinas")
    print("f. Ir a góndola de panaderia (PROMO! Todo al 50%)")
    print("g. Ir a góndola de perfumeria")
    print("h. Ir a góndola de verduleria")
    print("i. Ver stock de todas las góndolas")
    #print("j. Ver total del carrito")
    print("k. Finalizar compra")
    print("===================================")

def obtener_deposito(gondola):
    g=gondola._nombre_gondola.lower()
    if g == "galletitas":
        return deposito_galletitas
    elif g == "gaseosa":
        return deposito_gaseosa
    elif g == "perfumeria":
        return deposito_perfumeria
    elif g == "alcohol":
        return deposito_alcohol
    elif g == "verduleria":
        return deposito_verduleria
    elif g == "carniceria":
        return deposito_carniceria
    elif g == "panaderia":
        return deposito_panaderia
    elif g == "golosinas":
        return deposito_golosinas


def mostrar_producto(productos):
    i=0
    for producto in productos:
        nombre=producto._get_nombre()
        marca=producto._get_marca()
        print(str(i+1) + "." + marca + " " + nombre)
        if i==0:
            producto1=producto
        elif i==1:
            producto2=producto
        elif i==2:
            producto3=producto
        i+=1
        
    print("0. Volver")
    opcion=input("Ingrese que producto desea:")
    while True:
        try:
            if opcion=="1":
                p=producto1._get_gondola()
                deposito = obtener_deposito(p)
                carrito.leer_codigo(producto1,producto1._get_gondola(),inventario,almacen,deposito)
                break
            elif opcion=="2":
                p=producto2._get_gondola()
                deposito = obtener_deposito(p)
                carrito.leer_codigo(producto2,producto2._get_gondola(),inventario,almacen,deposito)
                break
            elif opcion=="3":
                p=producto3._get_gondola()
                deposito = obtener_deposito(p)
                carrito.leer_codigo(producto3,producto3._get_gondola(),inventario,almacen,deposito)
                break
        except ValueError:
            print("Ingrese un valor valido")

def ver_stock():
    print(f"{gondola_alcohol}: {gondola_alcohol.mostrar_stock()}")
    print(f"{gondola_carniceria}: {gondola_carniceria.mostrar_stock()}")
    print(f"{gondola_galletitas}: {gondola_galletitas.mostrar_stock()}")
    print(f"{gondola_gaseosa}: {gondola_gaseosa.mostrar_stock()}")
    print(f"{gondola_golosinas}: {gondola_golosinas.mostrar_stock()}")
    print(f"{gondola_panaderia}: {gondola_panaderia.mostrar_stock()}")
    print(f"{gondola_perfumeria}: {gondola_perfumeria.mostrar_stock()}")
    print(f"{gondola_verduleria}: {gondola_verduleria.mostrar_stock()}")

def total():
    print("\n===== TOTAL A PAGAR =====")
    print(f"\n Descuentos de galletitas: {almacen.descuento_galletas(carrito)}")
    print(f"\n Descuentos de bebidas: {almacen.descuento_bebidas(carrito)}")
    print(f"\n Descuentos de perfumeria: {almacen.descuento_perfumeria(carrito)}")
    print(almacen.total_a_pagar(carrito))


    
    

            
            




