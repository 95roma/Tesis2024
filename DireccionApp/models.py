from django.db import models

# Create your models here.
class Departamento(models.Model):
    id= models.AutoField(primary_key=True)
    nombre_depto=models.CharField(max_length=70)
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
        db_table= 'Departamento'

    def __str__(self) :
        return self.nombre_depto
    
class Muni(models.Model):
    idmuni= models.AutoField(primary_key=True)
    nombre_muni=models.CharField(max_length=70)
    depto=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado=models.IntegerField()
    class Meta:
        verbose_name='Muni'
        verbose_name_plural='Munis'
        db_table= 'Muni'

    def __str__(self) :
        return self.nombre_muni
    
class Distrito(models.Model):
    id= models.AutoField(primary_key=True)
    distri=models.CharField(max_length=100)
    muni=models.ForeignKey(Muni, on_delete=models.CASCADE)
    estado=models.IntegerField()
    class Meta:
        verbose_name='Distrito'
        verbose_name_plural='Distritos'
        db_table= 'Distrito'

    def __str__(self) :
        return self.distri