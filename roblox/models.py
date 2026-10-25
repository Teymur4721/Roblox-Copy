from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Oyunun Adı")
    creator = models.CharField(max_length=100, verbose_name="Yaradıcı (məs: @Teymur)")
    description = models.TextField(verbose_name="Oyun haqqında məlumat")
    likes = models.CharField(max_length=50, verbose_name="Bəyənmə (məs: 91% Rating)")
    image = models.ImageField(upload_to='game_images/', verbose_name="Oyunun Şəkli")

    def __str__(self):
        return self.title