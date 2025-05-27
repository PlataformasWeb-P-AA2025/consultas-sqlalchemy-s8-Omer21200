# Consulta 02

#2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 .
#  En función de los departamentos, presentar el nombre del departamento y 
# el número de cursos que tiene cada departamento

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Departamento, Curso, Tarea, Entrega

# Se crea el engine y la sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta:
# Se hace join entre Departamento, Curso, Tarea y Entrega para filtrar por calificaciones menores o iguales a 0.3

departamentos = session.query(Departamento ).join(Departamento.cursos) \
 .join(Curso.tareas) \
 .join(Tarea.entregas) \
 .filter(Entrega.calificacion <= 0.3) \
 .group_by(Departamento.id) \
 .all()

# Presentación de resultados

for departamento in departamentos:
    num_cursos = session.query(Curso).filter(Curso.departamento_id == departamento.id).count()
    print(f"Departamento: {departamento.nombre}")
    print(f"Número de cursos: {num_cursos}")
    print("\n")

       
