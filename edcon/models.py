from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from sistema.models import Estado, Ciudad, Colonia


# Create your models here.

# class Alumno(Usuario):
#     ESTUDIANTE = 1
#     EGRESADO = 2
#     EXTERNO = 3
#     ROLE_CHOICES = (
#         (ESTUDIANTE, 'Estudiante UTS'),
#         (EGRESADO, 'Egresado UTS'),
#         (EXTERNO, 'Persona Externa'),
#     )
#     telefono = models.CharField(max_length=15, null=True, blank=True)
#     estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, related_name='estado_alumno')
#     ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, blank=True, related_name='ciudad_alumno')
#     colonia = models.ForeignKey(Colonia, on_delete=models.CASCADE, null=True, blank=True, related_name='colonia_alumno')
#     calle = models.CharField(max_length=60, null=True, blank=True)
#     num_exterior = models.CharField(max_length=15, null=True, blank=True)
#     num_interior = models.CharField(max_length=15, null=True, blank=True)
#     tipo_usuario = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
#     avatar = models.ImageField(default='default.png', upload_to='avatar', null=True, blank=True)

#     class Meta:
#         verbose_name = "Alumno"
#         verbose_name_plural = "Alumnos"


#     def __str__(self):
#         if self.apellido_paterno is None and self.apellido_materno is None:
#             return f'{self.nombre}'
#         elif self.apellido_paterno is None:
#             return f'{self.nombre} {self.apellido_materno}'
#         elif self.apellido_materno is None:
#             return f'{self.nombre} {self.apellido_paterno}'
#         else:
#             return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'

# class Profesor(Usuario):
#     telefono = models.CharField(max_length=15, null=True, blank=True)
#     avatar = models.ImageField(default='default.png', upload_to='avatar', null=True, blank=True)

#     class Meta:
#         verbose_name = "Profesor"
#         verbose_name_plural = "Profesores"


#     def __str__(self):
#         if self.apellido_paterno is None and self.apellido_materno is None:
#             return f'{self.nombre}'
#         elif self.apellido_paterno is None:
#             return f'{self.nombre} {self.apellido_materno}'
#         elif self.apellido_materno is None:
#             return f'{self.nombre} {self.apellido_paterno}'
#         else:
#             return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'


class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    precio_estudiante_uts = models.DecimalField(_('Precio Estudiante UTS'), max_digits=6, decimal_places=2)
    precio_persona_externa = models.DecimalField(_('Precio Persona Externa'), max_digits=6, decimal_places=2)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(default='default-image-curso-620x600.jpg', upload_to='cursos', blank=True, null=True)
    fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre

# class Periodo(models.Model):
#     nombre = models.CharField(max_length=100, unique=True)
#     fecha_inicio = models.DateField()
#     fecha_fin = models.DateField()
#     activo = models.BooleanField(default=True)
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     def __str__(self):
#         return self.nombre

# class CursoAlumno(models.Model):
#     alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
#     periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
#     inscrito = models.BooleanField(default=False)
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     class Meta:
#         verbose_name = 'Curso Alumno'
#         verbose_name_plural = 'Cursos Alumnos'

#     def __str__(self):
#         return self.alumno.nombre + ' - ' + self.curso.nombre + ' - ' + self.periodo.nombre

# class CalificacionCurso(models.Model):
#     curso_alumno = models.OneToOneField(CursoAlumno, on_delete=models.CASCADE)
#     primer_examen = models.DecimalField(_('Primer Examen'), max_digits=6, decimal_places=2, default=0)
#     segundo_examen = models.DecimalField(_('Segundo Examen'), max_digits=6, decimal_places=2, default=0)
#     calificacion_final = models.DecimalField(_('Calificación Final'), max_digits=6, decimal_places=2, default=0)
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     def save(self):
#         self.calificacion_final = (self.primer_examen + self.segundo_examen) / 2
#         return super(CalificacionCurso, self).save()

#     class Meta:
#         verbose_name = 'Calificacion'
#         verbose_name_plural = 'Calificaciones'
    


# class Grupo(models.Model):
#     nombre = models.CharField(max_length=100)
#     codigo = models.CharField(max_length=6, unique=True)
#     profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
#     periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
#     aula = models.ForeignKey('Aula', on_delete=models.CASCADE)
#     alumnos = models.ManyToManyField(Alumno,)
#     # alumnos = ChainedManyToManyField(
#     #     CursoAlumno,
#     #     related_name='grupo_alumnos',
#     #     horizontal=True,
#     #     chained_field='curso',
#     #     chained_model_field='curso',
#     # )
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     class Meta:
#         verbose_name = 'Grupo'
#         verbose_name_plural = 'Grupos'

#     def __str__(self):
#         return self.nombre

# class Aula(models.Model):
#     edificio = models.CharField(max_length=10)
#     num_aula = models.CharField(_('Número de aula'), max_length=10)
#     fecha_creacion = models.DateTimeField(_('Fecha de creación'), auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(_('Fecha de actualización'), auto_now=True)

#     class Meta:
#         verbose_name = 'Aula'
#         verbose_name_plural = 'Aulas'

#     def __str__(self):
#         return self.edificio + '-' + self.num_aula