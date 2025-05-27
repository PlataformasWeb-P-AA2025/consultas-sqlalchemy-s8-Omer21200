#Consulta 05

#5. 
#5.1 En una consulta, obtener todos los cursos.
#5.2 Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso (con otra consulta), 
#y presentar el promedio de calificaciones de las entregas

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Curso, Tarea, Entrega

# Crear engine y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los cursos
cursos = session.query(Curso).all()

# Recorrer cada curso y calcular el promedio de sus entregas
for curso in cursos:
    # Hacemos join de Entrega y Tarea para poder filtrar por curso_id
    promedio = session.query(func.avg(Entrega.calificacion)) \
        .join(Tarea) \
        .filter(Tarea.curso_id == curso.id) \
        .scalar()

    print(f"Curso: {curso.titulo}")
    if promedio is not None:
        print(f"Promedio de calificaciones: {promedio:.2f}\n")
# Cerrar sesión
session.close()
