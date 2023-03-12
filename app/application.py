from flask import Flask,jsonify,request
from flask_cors import CORS
from config import config
from flask_mysqldb import MySQL
import re
import sys

#saber si estamos utilizando el archivo como principal
app=Flask(__name__)


CORS(app, resources={r"/*":{"origins":'localhost'}})

conexion=MySQL(app)

# METODOS GET
#Listar personajes con filtro
@app.route("/personajes",methods=["GET"])
def listar_personajes():
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql=comprobar_get_personajes(request)
        cursor.execute(sql)
        ps_consulta=cursor.fetchall()
        personajes=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como json
        for fila in ps_consulta:
            personaje={
                'ID':fila[0],
                'Nombre':fila[1],
                'Apellidos':fila[2],
                'Edad':fila[3],
                'Descripcion':fila[4],
                'Padre':fila[5],
                'Madre':fila[6],
                'Especie':fila[7],
                'Genero':fila[8],
                'Imagen':fila[9],
                'Nacimiento':fila[10],
                'Localizacion':fila[11],
                'Aparicion':fila[12]
            }
            personajes.append(personaje)
            
        return jsonify({'Personajes':personajes,'mensaje':"Personajes listados."})
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})
    
    
#Listar localizaciones con filtro
@app.route("/localizaciones",methods=["GET"])
def listar_localizaciones():
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql=comprobar_get_localizaciones(request)
        cursor.execute(sql)
        lc_consulta=cursor.fetchall()
        localizaciones=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como json
        for fila in lc_consulta:
            localizacion={
                'ID':fila[0],
                'Coordenadas':fila[1],
                'Ciudad':fila[2],
                'Pais':fila[3],
                'Dimension':fila[4],
                'Descripcion':fila[5],
                'Poblacion':fila[6],
                'Moneda':fila[7]
            }
            localizaciones.append(localizacion)
        return jsonify({'Localizaciones':localizaciones,'mensaje':"Localizacines listadas."})
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})
    
#Listar generos con filtro
@app.route("/generos",methods=["GET"])
def listar_generos():
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql=comprobar_get_genero_especie(request,"generos")
        cursor.execute(sql)
        gn_consulta=cursor.fetchall()
        personajes=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como json
        for fila in gn_consulta:
            personaje={
                'ID':fila[0],
                'Nombre':fila[1],
                'Descripcion':fila[2]
            }
            personajes.append(personaje)
        return jsonify({'Generos':personajes,'mensaje':"Generos listados."})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})



#Listar especies con filtro
@app.route("/especies",methods=["GET"])
def listar_especies():
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql=comprobar_get_genero_especie(request,"especies")
        cursor.execute(sql)
        es_consulta=cursor.fetchall()
        personajes=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como json
        for fila in es_consulta:
            personaje={
                'ID':fila[0],
                'Nombre':fila[1],
                'Descripcion':fila[2]
            }
            personajes.append(personaje)
        return jsonify({'Personajes':personajes,'mensaje':"Especies listados."})
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})


   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funciones de ayuda metodo GET
#Comprobar filtros en el metodo get localizaciones
def comprobar_get_personajes(consulta:request):
        #Inicializamos sql para meter la consulta
    #Armamos la consulta dependiendo de los datos nos hayan pasado
    sql=""
    sql="SELECT * FROM personajes WHERE 1=1"
        #Recoger datos del enlace
     #utlizamos comprension de lista para pasar lo que nos han dado a una lista de numeros, nos aseguramos que solo mete los numeros con una clausula if
    ps_id=[int(i) for i in consulta.args.get('id',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_nombre=[i for i in consulta.args.get('nombre',"vacio",type=str).split(',') if i!="vacio"]
    ps_apellido=[i for i in consulta.args.get('apellido',"vacio",type=str).split(',') if i!="vacio"]
    ps_edad=[int(i) for i in consulta.args.get('edad',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_padre=[int(i) for i in consulta.args.get('padre',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_madre=[int(i) for i in consulta.args.get('madre',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_especie=[int(i) for i in consulta.args.get('especie',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_genero=[int(i) for i in consulta.args.get('genero',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_nacimiento=[int(i) for i in consulta.args.get('nacimiento',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_localizacion=[int(i) for i in consulta.args.get('localizacion',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    ps_aparicion=[int(i) for i in consulta.args.get('aparicion',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]


    #Creamos una lista que contengan el nombre de los campos y su valor
    datos_personaje = [
    ('ID', ps_id),
    ('Nombre', ps_nombre),
    ('Apellidos', ps_apellido),
    ('Padre', ps_padre),
    ('Madre', ps_madre),
    ('Especie', ps_especie),
    ('Genero', ps_genero),
    ('Nacimiento', ps_nacimiento),
    ('Localizacion', ps_localizacion),
    ('Aparicion', ps_aparicion)
    ]

    # Bucle para recorrer cada campo y valor
    for dato, valor in datos_personaje:
        if len(valor) != 0 and valor[0]!="": # Comprobar si hay valores para el campo
            # Añadimos el dato para filtrar si cumple la condicion
            if(all(isinstance(i,int) for i in valor)):
                sql += " AND {} IN ({})".format(dato, ','.join(str(i) for i in valor))
            else:
                sql+=  " AND {} IN ('{}')".format(dato, ','.join(i for i in valor))  

    if len(ps_edad)>1:#Consultamos si nos ha pasado el edad, en caso afirmativo lo añadimos a la consulta
        sql+=" AND Edad IN ({})".format(','.join(str(i) for i in ps_edad))#Volvemos a utilizar una compresion de lista para meter los datos en la consulta de manera correcta
    elif len(ps_edad)!=0:
        sql+=" AND Edad >={}".format(ps_edad[0])

        #devolvemos la consulta
    return sql

#Comprobar filtros en el metodo get localizaciones
def comprobar_get_localizaciones(consulta:request):
    #Inicializamos sql 
    #Armamos la consulta dependiendo de los datos nos hayan pasado
    sql="SELECT * FROM localizaciones WHERE 1=1"

        #Recoger datos del enlace
    #utlizamos comprension de lista para pasar lo que nos han dado a una lista de numeros, nos aseguramos que solo mete los numeros con una clausula if
    lc_id=[int(i) for i in consulta.args.get('id',"vacio",type=str).split(',') if i!="vacio" and i.isdigit()]
    lc_ciudad=[i for i in consulta.args.get('ciudad',"vacio",type=str).split(',') if i!="vacio"]
    lc_pais=[i for i in consulta.args.get('pais',"vacio",type=str).split(',') if i!="vacio"]
    lc_dimension=[i for i in consulta.args.get('dimension',"vacio",type=str).split(',') if i!="vacio"]
    lc_poblacion=consulta.args.get('poblacion',type=int) 
    lc_moneda=[i for i in consulta.args.get('moneda',"vacio",type=str).split(',') if i!="vacio"]

    datos_localizaciones= [
    ("ID",lc_id),
    ("Ciudad",lc_ciudad),
    ("Pais",lc_pais ),
    ("Dimension",lc_dimension),
    ("Moneda",lc_moneda)
    ]

    if lc_poblacion:#Consultamos si nos ha pasado la cantidad de poblacion, en caso afirmativo lo añadimos a la consulta
        sql+=" AND Poblacion>={0}".format(lc_poblacion)


    # Bucle para recorrer cada campo y valor
    for dato, valor in datos_localizaciones:
        if len(valor) != 0 and valor[0]!="": # Comprobar si hay valores para el campo
            # Añadimos el dato para filtrar si cumple la condicion
            if(all(isinstance(i,int) for i in valor)):
                sql += " AND {} IN ({})".format(dato, ','.join(str(i) for i in valor))
            else:
                sql+=  " AND {} IN ('{}')".format(dato, ','.join(i for i in valor))  

    #devolvemos la consulta
    return sql

#Comprobar filtros en el metodo get de generos y especies
def comprobar_get_genero_especie(consulta:request,tipo:str):
        #Recoger datos del enlace
    gn_id=[int(i) for i in consulta.args.get('id',"",type=str).split(',') if i.isdigit()]
    gn_nombre=[i for i in consulta.args.get('nombre',"",type=str).split(',')]
   
    #Inicializamos sql 
    #Armamos la consulta dependiendo de los datos nos hayan pasado
    if(tipo=="especies"):
        sql="SELECT * FROM especies WHERE 1=1"
    else:
        sql="SELECT * FROM generos WHERE 1=1"

    if len(gn_id)!=0:#Consultamos si nos ha pasado el id de lugar de aparicion, en caso afirmativo lo añadimos a la consulta
        sql+=" AND ID IN ({})".format(','.join(str(i) for i in gn_id))#Volvemos a utilizar una compresion de lista para meter los datos en la consulta de manera correcta


    if gn_nombre[0]!="" or len(gn_nombre)!=1:#Consultamos si nos ha pasado el nombre, en caso afirmativo lo añadimos a la consulta
        sql+=" AND Nombre IN ({})".format(','.join('"{}"'.format(i) for i in gn_nombre))#Volvemos a utilizar una compresion de lista para meter los datos en la consulta de manera correcta

  
    #devolvemos la consulta
    return sql     
################################################################~##########################################################################################################
#METODOS POST
#Registramos personajes
@app.route("/personajes",methods=["POST"])
def registrar_personajes():
    try:
        sql=comprobar_post_personajes(request)
        #comprobamos si nos ha pasado una lista con los valores que están vacios o en caso de ser numerico sea negativo
        if type(sql)==list:
            return jsonify({'mensaje':"No se ha podido registrar el personaje ya que los siguientes valores son nulos, cadena vacía y/o no cumplen con los requisitos. Compruebe estos parametros y vuelva a intentarlo: {}.".format(",".join(sql))})

        #Realizamos comprobacion si nos ha devuelto que algún dato que dependa de otra tabla esta introduciendo un valor invalido
        if len(sql.split())==1:
            return jsonify({'mensaje':"No se puede asignar el/la {} debido a que este dato depende de su existencia en la base de datos, ya sea de la misma tabla u otra de la que dependa.".format(sql)})

        #print(request.json)
        cursor=conexion.connection.cursor()

        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Personaje registrado"}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 
    
#Registramos localizaciones
@app.route("/localizaciones",methods=["POST"])
def registrar_localizaciones():
    try:
        #print(request.json)
        sql=comprobar_post_localizaciones(request)

        #comprobamos si nos ha pasado una lista con los valores que están vacios o en caso de ser numerico sea negativo
        if type(sql)==list:
            return jsonify({'mensaje':"No se ha podido registrar la localizacion ya que los siguientes valores son nulos, cadena vacía y/o no cumplen con los requisitos. Compruebe estos parametros y vuelva a intentarlo: {}.".format(",".join(sql))})

        cursor=conexion.connection.cursor()
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Localización registrada."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 

#Agregar Generos
@app.route("/generos",methods=["POST"])
def registrar_generos():
    try:
        #Conexion a base de datos
        cursor=conexion.connection.cursor()
        sql=comprobar_post_generos_especies(request,"generos")

        #comprobamos si nos ha pasado una lista con los valores que están vacios o en caso de ser numerico sea negativo
        if type(sql)==list:
            return jsonify({'mensaje':"No se ha podido el genero ya que los siguientes valores son nulos, cadena vacía y/o no cumplen con los requisitos. Compruebe estos parametros y vuelva a intentarlo: {}.".format(",".join(sql))})

        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 


        return jsonify({'mensaje':"Genero registrado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})
    
#Agregar Especies
@app.route("/especies",methods=["POST"])
def registrar_especies():
    try:
        #Conexion a base de datos
        cursor=conexion.connection.cursor()
        sql=comprobar_post_generos_especies(request,"especies")
        #comprobamos si nos ha pasado una lista con los valores que están vacios o en caso de ser numerico sea negativo
        if type(sql)==list:
            return jsonify({'mensaje':"No se ha podido registrar la especie ya que los siguientes valores son nulos, cadena vacía y/o no cumplen con los requisitos. Compruebe estos parametros y vuelva a intentarlo: {}.".format(",".join(sql))})

        #En caso contrario seguimos con la ejecucion
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 

        return jsonify({'mensaje':"Especie registrada."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
#Funciones de ayuda metodo POST
#Comprobar datos y realizar consulta personajes 
def comprobar_post_personajes(consulta:request):
    # Recuperar el cuerpo de la solicitud como un listado
    if consulta.is_json:
        datos = consulta.get_json()
    else:
        datos=consulta.form
    
        
    ps_nombre=datos.get('nombre')
    ps_apellido=datos.get('apellidos')
    ps_edad=datos.get('edad')
    ps_descripcion=datos.get('descripcion')
    ps_padre=datos.get('padre')
    ps_madre=datos.get('madre')
    ps_especie=datos.get('especie')
    ps_genero=datos.get('genero')
    ps_imagen=datos.get('imagen')
    ps_nacimiento=datos.get('nacimiento')
    ps_localizacion=datos.get('localizacion')
    ps_aparicion=datos.get('aparicion')

        #lista que rellenaremos con los datos que se han pasado vacios
    lista=[]
    #variable para comprobar si algún dato es cadenaa vacia
    confirmacion=False

    #Lista de los datos para realizar comprobaciones
    datos=[
    ('Nombre', ps_nombre),
    ('Apellidos', ps_apellido),
    ('Edad', ps_edad),  
    ('Descripcion', ps_descripcion),      
    ('Padre', ps_padre),
    ('Madre', ps_madre),
    ('Especie', ps_especie),
    ('Genero', ps_genero),
    ('Imagen', ps_imagen),
    ('Nacimiento', ps_nacimiento),
    ('Localizacion', ps_localizacion),
    ('Aparicion', ps_aparicion)
    ]

    #Comprobamos que los valores que dependen de su existecia en otra tabla son validos
    datos_comprobacion = [
        (ps_padre, "padre",get_dato_personajes('ID')),
        (ps_madre, "madre",get_dato_personajes('ID')),
        (ps_especie, "especie", get_id_especies()),
        (ps_genero, "genero", get_id_generos()),
        (ps_aparicion, "aparicion", get_id_localizaciones()),
        (ps_nacimiento, "nacimiento", get_id_localizaciones()),
        (ps_localizacion, "localizacion", get_id_localizaciones())
    ]

    for dato, tipo, funcion in datos_comprobacion:
        if dato is not None:
            if  dato.isdigit() and int(dato) not in funcion and dato not in ["0","-1"]:
                return tipo
                
    # Construir la consulta SQL con los datos que se hayan pasado
    parametros = []

    #Realizamos que los datos que ha pasado no sean cadena vacia y si es un valor que sea positivo
    for clave, valor in datos:
        if valor is not None:
            if valor!="":       
                 # Definimos el patrón de expresión regular para un número entero (segun San Google)
                patron = r'^-?\d+$'
                if bool(re.match(patron,valor)):
                    if int(valor)>0 or int(valor)==-1 and clave in ["Padre","Madre"]:
                        parametros.append("{1}".format(clave,valor))
                    else:
                        if not confirmacion:
                            confirmacion = True
                        lista.append(clave)
                else:
                    parametros.append("'{1}'".format(clave,valor))
            else:
                if not confirmacion:
                    confirmacion = True
                lista.append(clave)                    
        else:
            if not confirmacion:
                confirmacion = True
            lista.append(clave)                    
        
                        

    #comprobamos si hay algún valor con cadena vacía y o si es numerico que su valor sea negativo
    if confirmacion:
        return lista
    
    sql="INSERT INTO personajes(ID,Nombre,Apellidos,Edad,Descripcion,Padre,Madre,Especie,Genero,Imagen,Nacimiento,Localizacion,Aparicion) "
    sql+="VALUES (null,{})".format(", ".join(parametros))

    return sql

#Comprobar datos y realizar consulta Localizaciones 
def comprobar_post_localizaciones(consulta:request):
    # Recuperar el cuerpo de la solicitud como un listado
    if consulta.is_json:
        datos = consulta.get_json()
    else:
        datos=consulta.form

    lc_coordenadas=datos.get('coordenadas')
    lc_ciudad=datos.get('ciudad')
    lc_pais=datos.get('pais')
    lc_descripcion=datos.get('descripcion')
    lc_dimension=datos.get('dimension')
    lc_poblacion=datos.get('poblacion')
    lc_moneda=datos.get('moneda')

#lista que rellenaremos con los datos que se han pasado vacios
    lista=[]
    #variable para comprobar si algún dato es cadenaa vacia
    confirmacion=False

    #Lista de los datos para realizar comprobaciones
    datos=[
    ("Coordenadas",lc_coordenadas),    
    ("Ciudad",lc_ciudad),
    ("Pais",lc_pais ),
    ("Descripcion",lc_descripcion),
    ("Dimension",lc_dimension),    
    ("Poblacion",lc_poblacion),
    ("Moneda",lc_moneda)
    ]
 

    # Construir la consulta SQL con los datos que se hayan pasado
    parametros = []

    #Realizamos que los datos que ha pasado no sean cadena vacia y si es un valor que sea positivo
    for clave, valor in datos:
        if valor is not None:
            if valor!="":       
                 # Definimos el patrón de expresión regular para un número entero (segun San Google)
                patron = r'^-?\d+$'
                if bool(re.match(patron,str(valor))):
                    if int(valor)>0:
                        parametros.append("{1}".format(clave,valor))
                    else:
                        if not confirmacion:
                            confirmacion = True
                        lista.append(clave)
                else:
                    parametros.append("'{1}'".format(clave,valor))
            else:
                if not confirmacion:
                    confirmacion = True
                lista.append(clave)                    
        else:
            if not confirmacion:
                confirmacion = True
            lista.append(clave)   
                        

    #comprobamos si hay algún valor con cadena vacía y o si es numerico que su valor sea negativo
    if confirmacion:
        return lista

 
    sql="INSERT INTO localizaciones(ID,Coordenadas,Ciudad,Pais,Descripcion,Dimension,Poblacion,Moneda) "
    sql+="VALUES (null,{})".format(", ".join(parametros))

    return sql




#Comprobar datos genero post
def comprobar_post_generos_especies(consulta:request,tipo:str):
    # Recuperar el cuerpo de la solicitud como un listado
    if consulta.is_json:
        datos = consulta.json
    else:
        datos=consulta.form
        
    gn_nombre=datos.get('nombre')
    gn_descripcion=datos.get('descripcion')        
    
#lista que rellenaremos con los datos que se han pasado vacios
    lista=[]
    #variable para comprobar si algún dato es cadenaa vacia
    confirmacion=False

    #Lista de los datos para realizar comprobaciones
    datos=[
    ("Nombre",gn_nombre),    
    ("Descripcion",gn_descripcion)
    ]
 

    # Construir la consulta SQL con los datos que se hayan pasado
    parametros = []

    #Realizamos que los datos que ha pasado no sean cadena vacia y si es un valor que sea positivo
    for clave, valor in datos:
        if valor is not None:
            if valor!="":       
                 # Definimos el patrón de expresión regular para un número entero (segun San Google)
                patron = r'^-?\d+$'
                if bool(re.match(patron,str(valor))):
                    if int(valor)>0:
                        parametros.append("{1}".format(clave,valor))
                    else:
                        if not confirmacion:
                            confirmacion = True
                        lista.append(clave)
                else:
                    parametros.append("'{1}'".format(clave,valor))
            else:
                if not confirmacion:
                    confirmacion = True
                lista.append(clave)                    
        else:
            if not confirmacion:
                confirmacion = True
            lista.append(clave)   
                        

    #comprobamos si hay algún valor con cadena vacía y o si es numerico que su valor sea negativo
    if confirmacion:
        print("entra")
        return lista


    if tipo=="especies":
        sql="INSERT INTO especies(ID,Nombre,Descripcion) VALUES (null,{})".format(", ".join(parametros))
    else:
        sql="INSERT INTO generos(ID,Nombre,Descripcion) VALUES (null,{})".format(", ".join(parametros))

    return sql

###########################################################################################################################################################################
#METODOS PUT
#Modificar personajes
@app.route("/personajes/<id>",methods=["PUT"])
def modificar_personajes(id):
    #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_dato_personajes("ID"):
            return jsonify({'mensaje':"No existe ningún personaje con el id que ha especificado.Por favor, verifique que el id este relacionado a una especie existente y vuelva a intentarlo."})
        
    try:
        #print(request.json)
        sql=comprobar_put_personajes(request,int(id))
        #COmprobacion de si ha introducido todos los datos
        if sql=="insertar dato":
            return jsonify({'mensaje':"Tiene que insertar minimo un datos para poder modificar al personaje, intentelo de nuevo introduciendo un dato modificable.\nEntre los datos modificables tenemos nombre,apellidos,edad,descripcion,padre,madre,especie,imagen,nacimiento,localizacion,aparicion."})

        #comprobamos si nos ha pasado una lista con los valores que están vacios o en caso de ser numerico sea negativo
        if type(sql)==list:
            return jsonify({'mensaje':"Los siguientes valores que has pasado son cadena vacía o en caso de ser valor numerico son negativos: {}.".format(",".join(sql))})

        #Realizamos comprobacion si nos ha devuelto que algún dato que dependa de otra tabla esta introduciendo un valor invalido
        if len(sql.split())==1:
            return jsonify({'mensaje':"No se puede modificar el/la {} debido a que este dato depende de su existencia en la base de datos de la misma tabla u otra de la que dependa.".format(sql)})

        #Si todo va bien ejecutamos la consulta
        cursor=conexion.connection.cursor()       
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Personaje Actualizado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 

#Modificar localizaciones
@app.route("/localizaciones/<id>",methods=["PUT"])
def modificar_localizaciones(id):
    #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_id_localizaciones():
            return jsonify({'mensaje':"No existe ninguna localización con el id que ha especificado.Por favor, verifique que el id este relacionado a una especie existente y vuelva a intentarlo."})
        
    try:
        #print(request.json)
        sql=comprobar_put_localizaciones(request,int(id))
        #COmprobacion de si ha introducido todos los datos
        if sql=="insertar dato":
            return jsonify({'mensaje':"Tiene que insertar minimo un datos para poder modificar la localización, intentelo de nuevo introduciendo un dato modificable.\nEntre los datos modificables tenemos la coordenada, la ciudad, el pais, la descripcion, la dimension, la población y la moneda."})

        #comprobamos si nos ha pasado una lista con los valores que están vacios o en caso de ser numerico sea negativo
        if type(sql)==list:
            return jsonify({'mensaje':"Los siguientes valores que has pasado son cadena vacía o en caso de ser valor numerico son negativos: {}.".format(",".join(sql))})
        
        #Si todo va bien ejecutamos la consulta
        cursor=conexion.connection.cursor()       
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Localización Actualizado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 

#Modificar especies
@app.route("/especies/<id>",methods=["PUT"])
def modificar_especies(id):
    #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_id_especies():
            return jsonify({'mensaje':"No existe ninguna especie con el id que ha especificado.Por favor, verifique que el id este relacionado a un genero existente y vuelva a intentarlo."})
       
    try:
        #print(request.json)
        sql=comprobar_put_especies_generos(request,int(id),"especies")

        if sql=="insertar dato":
            return jsonify({'mensaje':"Tiene que insertar minimo un dato para poder modificar el genero, intentelo de nuevo introduciendo un dato modificable.\nEntre los datos modificables tenemos el nombre y la descripcion"})

        #Realizamos comprobacion si nos ha devuelto que algún dato que dependa de otra tabla esta introduciendo un valor invalido
        if len(sql.split())==1:
            return jsonify({'mensaje':"No se puede modificar el/la {} el dato reemplazante es cadena vacía.".format(sql)})

        #Realizamos la conexión si todo ha ido bien
        cursor=conexion.connection.cursor()       
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Especie Actualizado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})  

#Modificar generos  
@app.route("/generos/<id>",methods=["PUT"])
def modificar_generos(id):
    #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_id_generos():
            return jsonify({'mensaje':"No existe ningún genero con el id que ha especificado.Por favor, verifique que el id este relacionado a un genero existente y vuelva a intentarlo."})
            
    try:
        #Realizamos comprobaciones
        sql=comprobar_put_especies_generos(request,int(id),"generos")
        

        #Comprobamos que lo que nos han pasado respete las normas impuestas    
        if len(sql.split())==1:
            return jsonify({'mensaje':"No se puede modificar el/la {} el valor reemplazante es una cadena vacía.".format(sql)})

        #comprobamos si ha introducido al menos un dato a modificar, sino devuelve un mensaje
        if sql=="insertar dato":
            return jsonify({'mensaje':"Tiene que insertar minimo un dato para poder modificar el genero, intentelo de nuevo introduciendo un dato modificable.\nEntre los datos modificables tenemos el nombre y la descripcion"}) 


        #realizamos la conexiones
        cursor=conexion.connection.cursor()       
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Genero Actualizado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})     

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#metodos de ayuda METODO PUT
#Comprobar datos del PUT de especies y generos para devolver el error o la secuencia sql 
def comprobar_put_personajes(consulta:request,id:int):
    # Recuperar el cuerpo de la solicitud como un listado
    if consulta.is_json:
        datos = consulta.json
    else:
        datos=consulta.form


    ps_nombre=datos.get('nombre')
    ps_apellido=datos.get('apellidos')
    ps_edad=datos.get('edad')
    ps_descripcion=datos.get('descripcion')
    ps_padre=datos.get('padre')
    ps_madre=datos.get('madre')
    ps_especie=datos.get('especie')
    ps_genero=datos.get('genero')
    ps_imagen=datos.get('imagen')
    ps_nacimiento=datos.get('nacimiento')
    ps_localizacion=datos.get('localizacion')
    ps_aparicion=datos.get('aparicion')

    
    #lista que rellenaremos con los datos que se han pasado vacios
    lista=[]
    #variable para comprobar si algún dato es cadenaa vacia
    confirmacion=False

    #Lista de los datos para realizar comprobaciones
    datos=[
    ('Nombre', ps_nombre),
    ('Apellidos', ps_apellido),
    ('Padre', ps_padre),
    ('Madre', ps_madre),
    ('Especie', ps_especie),
    ('Descripcion', ps_descripcion),
    ('Edad', ps_edad),
    ('Imagen', ps_imagen),
    ('Genero', ps_genero),
    ('Nacimiento', ps_nacimiento),
    ('Localizacion', ps_localizacion),
    ('Aparicion', ps_aparicion)
    ]
    #Comprobar si al menos ha insertado un dato a modificar
    if all(dato is None for clave,dato in datos):  
        return "insertar dato"   



    #Comprobamos que los valores que dependen de su existecia en otra tabla son validos
    datos_comprobacion = [
        (ps_padre, "padre",get_dato_personajes('Padre')),
        (ps_madre, "madre",get_dato_personajes('Madre')),
        (ps_especie, "especie", get_id_especies()),
        (ps_genero, "genero", get_id_generos()),
        (ps_aparicion, "aparicion", get_id_localizaciones()),
        (ps_nacimiento, "nacimiento", get_id_localizaciones()),
        (ps_localizacion, "localizacion", get_id_localizaciones())
    ]

    for dato, tipo, funcion in datos_comprobacion:
        if dato is not None:
            if  dato.isdigit() and int(dato) not in funcion and dato!="-1":
                return tipo
                
    # Construir la consulta SQL con los datos que se hayan pasado
    parametros = []

    #Realizamos que los datos que ha pasado no sean cadena vacia y si es un valor que sea positivo
    for clave, valor in datos:
        if valor is not None:
            if valor!="":       
                 # Definimos el patrón de expresión regular para un número entero (segun San Google)
                patron = r'^-?\d+$'
                if bool(re.match(patron,valor)):
                    if int(valor)>0:
                        parametros.append("{0} = {1}".format(clave,valor))
                    else:
                        if not confirmacion:
                            confirmacion = True
                        lista.append(clave)
                else:
                    parametros.append("{0} = '{1}'".format(clave,valor))
            else:
                if not confirmacion:
                    confirmacion = True
                lista.append(clave)                    
        
                        

    #comprobamos si hay algún valor con cadena vacía y o si es numerico que su valor sea negativo
    if confirmacion:
        return lista

    #Comprobar si la localizacion existe
    sql="UPDATE personajes SET "
    sql += ", ".join(parametros) + " WHERE ID = {}".format(id)

    return sql



#Comprobar datos del PUT de especies y generos para devolver el error o la secuencia sql 
def comprobar_put_localizaciones(consulta:request,id:int):
    # Recuperar el cuerpo de la solicitud como un listado
    if consulta.is_json:
        datos = consulta.json
    else:
        datos=consulta.form

    lc_coordenas=datos.get('coordenadas')
    lc_ciudad=datos.get('ciudad')
    lc_pais=datos.get('pais')
    lc_descripcion=datos.get('descripcion')
    lc_dimension=datos.get('dimension')
    lc_poblacion=datos.get('poblacion')
    lc_moneda=datos.get('moneda')

    #lista que rellenaremos con los datos que se han pasado vacios
    lista=[]
    #variable para comprobar si algún dato es cadenaa vacia
    confirmacion=False

    #Lista de los datos para realizar comprobaciones
    datos=[
    ("Ciudad",lc_ciudad),
    ("Pais",lc_pais ),
    ("Descripcion",lc_descripcion),
    ("Poblacion",lc_poblacion),
    ("Dimension",lc_dimension),
    ("Moneda",lc_moneda)
    ]
    #Comprobar si al menos ha insertado un dato a modificar
    if all(dato is None for clave,dato in datos):  
        return "insertar dato"   

    # Construir la consulta SQL con los datos que se hayan pasado
    parametros = []

    #Realizamos que los datos que ha pasado no sean cadena vacia y si es un valor que sea positivo
    for clave, valor in datos:
        if valor is not None:
            if valor!="":       
                 # Definimos el patrón de expresión regular para un número entero (segun San Google)
                patron = r'^-?\d+$'
                if bool(re.match(patron,valor)):
                    if int(valor)>0:
                        parametros.append("{0} = {1}".format(clave,valor))
                    else:
                        if not confirmacion:
                            confirmacion = True
                        lista.append(clave)
                else:
                    parametros.append("{0} = '{1}'".format(clave,valor))
            else:
                if not confirmacion:
                    confirmacion = True
                lista.append(clave)                    
     
                        

    #comprobamos si hay algún valor con cadena vacía y o si es numerico que su valor sea negativo
    if confirmacion:
        return lista

    #Comprobar si la localizacion existe
    sql="UPDATE localizaciones SET "
    sql += ", ".join(parametros) + " WHERE ID = {}".format(id)

    return sql

#Comprobar datos del PUT de especies y generos para devolver el error o la secuencia sql 
def comprobar_put_especies_generos(consulta:request,id:int,tipo:str):
    # Recuperar el cuerpo de la solicitud como un listado
    if consulta.is_json:
        datos = consulta.json
    else:
        datos=consulta.form

    gn_nombre=datos.get('nombre')
    gn_descripcion=datos.get('descripcion')

    if gn_nombre is None and gn_descripcion is None:  
        return "insertar dato"   

    # Construir la consulta SQL
    parametros = []
    if gn_nombre is not None:
        if gn_nombre!="":
            parametros.append("Nombre = '{}'".format(gn_nombre))
        else:
            return "nombre"

    if gn_descripcion is not None:
        if gn_descripcion!="":
            parametros.append("Descripcion = '{}'".format(gn_descripcion))
        else:
            return "descripcion"

    #Ver el tipo de dato que tengo que modificar
    if tipo=="especies":
        sql="UPDATE especies SET "
        sql += ", ".join(parametros) + " WHERE ID = {}".format(id)
    else:
        sql="UPDATE generos SET "
        sql += ", ".join(parametros) + " WHERE ID = {}".format(id)

    return sql
###########################################################################################################################################################################
#METODOS DELETE
#Borrar personajes
@app.route("/personajes/<id>",methods=["DELETE"])
def eliminar_personajes(id):
  #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_dato_personajes("ID"):
            return jsonify({'mensaje':"No existe ningún personaje con el id que ha especificado. Por favor, verifique que el id esté relacionado un personaje existente y vuelva a intentarlo."})

    if int(id) in get_dato_personajes("Padre") or int(id) in get_dato_personajes("Madre"):
        return jsonify({'mensaje':"No se puede eliminar el personaje ya que es padre o madre de un personaje, modifique los personajes ante de volver a intentarlo."}) 

    try:
        sql="DELETE FROM personajes WHERE ID={0}".format(id)
        cursor=conexion.connection.cursor()
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Personaje eliminado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 


#Borrar localizaciones
@app.route("/localizaciones/<id>",methods=["DELETE"])
def eliminar_localizacion(id):
  #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_id_localizaciones():
            return jsonify({'mensaje':"No existe ninguna localización con el id que ha especificado.Por favor, verifique que el id este relacionado a una especie existente y vuelva a intentarlo."})
    
    #print(request.json)
    sql=comprobar_delete_localizaciones(int(id))

    #Comprobamos si la comprobacion nos devolvio un error de dependencia
    if sql=="Dependencia":
        return jsonify({'mensaje':"La localización que quiere eliminar lo tiene asignado un personaje. Por favor, asigne otro genero a los personajes que lo tienen asignado y luego vuelva a intentarlo."}) 
        
    try:
        cursor=conexion.connection.cursor()
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Localización eliminada."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 

#Borrar genero
@app.route("/generos/<id>",methods=["DELETE"])
def eliminar_genero(id):
  #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_id_generos():
            return jsonify({'mensaje':"No existe ningún género con el id que ha especificado.Por favor, verifique que el id este relacionado a una especie existente y vuelva a intentarlo."})
    
    #print(request.json)
    sql=comprobar_delete_especies_generos(int(id),"generos")

    #Comprobamos si la comprobacion nos devolvio un error de dependencia
    if sql=="Dependencia":
        return jsonify({'mensaje':"El genero que quiere eliminar lo tiene asignado un personaje. Por favor, asigne otro genero a los personajes que lo tienen asignado y luego vuelva a intentarlo."}) 
        
    try:
        cursor=conexion.connection.cursor()
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Genero eliminado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 
    
#Borrar especie
@app.route("/especies/<id>",methods=["DELETE"])
def eliminar_especies(id):
  #comprobamos que el id es un numero
    if not id.isdigit():
        return jsonify({'mensaje':"El id que tienes que introducir tiene que ser un valor numerico."}) 
    else:#si el id es numerico comprobar que exista una especie que cuadre con el id
        if int(id) not in get_id_especies():
            return jsonify({'mensaje':"No existe ninguna especie con el id que ha especificado.Por favor, verifique que el id este relacionado a una especie existente y vuelva a intentarlo."})
    
    #print(request.json)
    sql=comprobar_delete_especies_generos(int(id),"especies")

    #Comprobamos si la comprobacion nos devolvio un error de dependencia
    if sql=="Dependencia":
        return jsonify({'mensaje':"La especie que quiere eliminar lo tiene asignado un personaje. Por favor, asigne otro genero a los personajes que lo tienen asignado y luego vuelva a intentarlo."}) 
        
    try:
        cursor=conexion.connection.cursor()
        cursor.execute(sql)
        # Confirma la accion de insercción.
        conexion.connection.commit() 
        return jsonify({'mensaje':"Especie eliminado."}) 
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)})       
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funciones de ayuda DELETE 
#Comprobar datos del DELETE de especies y generos para devolver el error o la secuencia sql 
def comprobar_delete_localizaciones(id:int):
    #Preguntamos por si existe algún personaje que tiene asignado ese dato para no permitir borrarlo y evitar un fallo en la ejecucion de la sentencia
    if id in get_dato_personajes("Aparicion") or id in get_dato_personajes("Nacimiento") or id in get_dato_personajes("Localizacion"):
        return "Dependencia"
    else:
        return "DELETE FROM localizaciones WHERE ID={0}".format(id)


#Comprobar datos del DELETE de especies y generos para devolver el error o la secuencia sql 
def comprobar_delete_especies_generos(id:int,tipo:str):
    #comprobamos el tipo de dato que vamos a eliminar
    #Dentro preguntamos por si existe algún personaje que tiene asignado ese dato para no permitir borrarlo y evitar un fallo en la ejecucion de la sentencia
    if tipo=="especies":
        if id in get_dato_personajes("Especie"):
            return "Dependencia"
        else:
            return "DELETE FROM especies WHERE ID={0}".format(id)
    else:
        if id in get_dato_personajes("Genero"):
            return "Dependencia"
        else:
            return "DELETE FROM generos WHERE ID={0}".format(id)
        
 ###########################################################################################################################################################################   
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funciones generales
#Comprobamos si el dato tiene una logitud mayor a 1 y sea un numero o en caso de ser string que la longitud sea mayor a 1
def verificar_dato(dato):
    if dato is not None:
        dato=str(dato)
        return dato.isdigit() and int(dato)>0 or len(dato)>=1
    else:
        return False

#Recoger id de personajes para realizar comprobaciones
def get_dato_personajes(dato:str):
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql="SELECT DISTINCT {} FROM personajes".format(dato)
        cursor.execute(sql)
        ps_consulta=cursor.fetchall()
        personajes=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como array
        for fila in ps_consulta:
            personajes.append(fila[0])    
   
        return personajes
    except Exception as ex:
        return jsonify({'mensaje':"Error"})   
    
#Recoger id de localizaciones para realizar comprobaciones
def get_id_localizaciones():
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql="SELECT ID FROM localizaciones"
        cursor.execute(sql)
        lc_consulta=cursor.fetchall()
        localizaciones=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como json
        for fila in lc_consulta:
            localizaciones.append(fila[0]) 

        return localizaciones   
    except Exception as ex:
        return jsonify({'mensaje':"Error: {}".format(ex)}) 
    

#Recoger id de especies para realizar comprobaciones
def get_id_especies():
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql="SELECT ID FROM especies"
        cursor.execute(sql)
        es_consulta=cursor.fetchall()
        especies=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como json
        for fila in es_consulta:
            especies.append(fila[0])

        return especies   
    except Exception as ex:
        return jsonify({'mensaje':"Error: {}".format(ex)}) 
    

#Recoger id de generos para realizar comprobaciones
def get_id_generos():
    try:
        #Consulta sql
        cursor=conexion.connection.cursor()
        sql="SELECT ID FROM generos"
        cursor.execute(sql)
        gn_consulta=cursor.fetchall()
        generos=[]
        #Recorrer lo que devuelve y guardarlo en un array para luego lanzarlo como json
        for fila in gn_consulta:
            generos.append(fila[0])   

        return generos
    
    except Exception as ex:
        return jsonify({'mensaje':"Error {}".format(ex)}) 

def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe</h1>",404

def enlace_no_encontrada(error):
    return "<h1>El método no admite el enlace introducido </h1>",405

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.register_error_handler(405,enlace_no_encontrada)
    app.run()

    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa