from django.contrib import admin

# her kan vi Register vores model for at vises in vores admin page.

from .models import Post

admin.site.register(Post) # så bliver vi i stand til at se Post i admin page
