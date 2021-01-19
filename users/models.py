from django.db import models
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one_to_one betyder hver user har en profile og cascade mener hvis en bruger bliver slettet så vil profilen også bliver slettet
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # har en defaul billede som er gemt under filen 'profile_pics'

    def __str__(self):
        return f'{self.user.username} Profile' # efter username vil program printe også profilen

    def save(self): # den del bliver tilføjet for at resize billede
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)