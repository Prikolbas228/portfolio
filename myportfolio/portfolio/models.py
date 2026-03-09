from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=200,help_text='разделяй теги запятыми ')
    image_icon = models.CharField(max_length=50, default="fas fa-code")  # Иконка FontAwesome
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(',')]

class ContactMessage(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        subject = models.CharField(max_length=200)
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        is_read = models.BooleanField(default=False)

        def __str__(self):
            return f"{self.name} - {self.subject}"
class Certificate(models.Model):
    title = models.CharField(max_length=100,verbose_name="Название сертификата")
    issuer = models.CharField(max_length=200,verbose_name='Организация')
    date = models.DateField(verbose_name='Дата получение')
    credential_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID сертификата")
    credential_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на сертификат")
    image = models.ImageField(upload_to='certificates/', blank=True, null=True, verbose_name="Изображение")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
        ordering = ['-date']