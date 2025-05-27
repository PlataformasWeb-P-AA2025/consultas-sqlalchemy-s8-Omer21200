# Consulta 01

#1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, 
# nombre de instructor y nombre del departamento

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

# Se crea el engine y la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta:
# Se hace join entre Entrega, Tarea, Curso, Departamento para filtrar por Arte
# y también se hace join con Estudiante e Instructor para obtener los datos del estudiante asi como su calidicacion.

entregas = session.query(Entrega).\
    join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento).join(Entrega.estudiante).join(Curso.instructor).filter(Departamento.nombre == "Arte").all()

# Presentación de resultados

for entrega in entregas:
    print(f"Tarea: {entrega.tarea.titulo}")
    print(f"Estudiante: {entrega.estudiante.nombre}")
    print(f"Calificación: {entrega.calificacion}")
    print(f"Instructor: {entrega.tarea.curso.instructor.nombre}")
    print(f"Departamento: {entrega.tarea.curso.departamento.nombre}")
    print("\n")
       
