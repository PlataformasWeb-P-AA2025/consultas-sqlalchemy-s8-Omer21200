# Consulta 03

#Obtener todas las tareas asignadas a los siguientes estudiantes 

#Jennifer Bolton 
#Elaine Perez
#Heather Henderson
#Charles Harris

# En función de cada tarea, presentar el número de entregas que tiene


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import  Tarea, Entrega, Estudiante

# Se crea el engine y la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta:
# Se hace join entre Tarea, Entrega y Estudiante para filtrar por los estudiantes especificados

tareas = session.query(Tarea).join(Entrega).join(Estudiante) \
    .filter(Estudiante.nombre.in_(["Jennifer Bolton", "Elaine Perez", "Heather Henderson", "Charles Harris"])) \
 .all()

# Presentación de resultados
for tarea in tareas:
    entregas_count = len(tarea.entregas)
    print(f"Tarea: {tarea.titulo}")
    print(f"Número de entregas: {entregas_count}")
    print("\n")


# Cerrar la sesión
session.close()

       
