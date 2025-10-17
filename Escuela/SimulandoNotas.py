from Actores import Profesor, Alumno
# Crear alumnos
alumno1 = Alumno("Matias", "21343323-9", 34819403, [6.5, 5.7, 5.0])
alumno2 = Alumno("Juan", "30414234-k", 15467323, [6.6, 4.2, 6.0])  
alumno3 = Alumno("Pedro", "28947321-3", 47165109, [3.4, 6.8, 4.9])    
# Crear profesor
profe = Profesor("José", "10347708-6", 74191704)
profe.AgregarAlumno(alumno1)
profe.AgregarAlumno(alumno2)
profe.AgregarAlumno(alumno3)

print(alumno1.MostrarDatos())
print("Estado: "+alumno1.GetEstado)
