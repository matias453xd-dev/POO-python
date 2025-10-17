from Actores import Profesor, Alumno, Persona
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
# Reprobar a alumno1

# Crear instancias
alumno1 = Alumno("Juan Perez", "12345678-9", "987654321", [5.5, 6.0])
profesor1 = Profesor("Maria Gonzalez", "98765432-1", "123456789")

# Mostrar datos del alumno
print(alumno1.MostrarDatos())
print("Notas iniciales:", alumno1.GetNotas())

# Agregar una nota
alumno1.AgregarNota(6.5)
print("Notas después de agregar una nota:", alumno1.GetNotas())

# Borrar una nota
alumno1.BorrarNota(5.5)
print("Notas después de borrar una nota:", alumno1.GetNotas())

# Agregar alumno al profesor
profesor1.AgregarAlumno(alumno1)

# Reprobar al alumno
profesor1.Reprobar(alumno1)
print("Estado de carrera del alumno después de reprobar:", alumno1.GetEstado())

# Aprobar al alumno
profesor1.Aprobar(alumno1)
print("Estado de carrera del alumno después de aprobar:", alumno1.GetEstado())