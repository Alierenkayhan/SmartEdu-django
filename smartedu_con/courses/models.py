from django.db import models
from teachers.models import Teacher

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name='Kurs Adı', 
        help_text="Kurs adını yazınız."
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True)  # Correct definition without null=True
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Açıklama', 
        help_text="Kurs açıklamasını yazınız."
    )
    image = models.ImageField(
        upload_to='courses/%Y/%m/%d/', 
        default="courses/default_courses_image.jpg", 
        verbose_name='Kurs Resmi', 
        help_text="Kurs resmini yükleyiniz."
    )
    date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Oluşturulma Tarihi', 
        help_text="Kursun oluşturulma tarihini gösterir."
    )
    available = models.BooleanField(
        default=True, 
        verbose_name='Kullanılabilirlik', 
        help_text="Kursun kullanılabilir olup olmadığını belirtir."
    )

    def __str__(self):
        return self.name
