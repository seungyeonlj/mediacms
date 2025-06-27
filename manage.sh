#!/usr/bin/env python3
import os
import django

# point to your settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
django.setup()

from files.models import Media

video = Media.objects.get(id=1)
video.views = 2345
video.save()
print(f"Updated video {video.id} views to {video.views}")


# fields
print([f.name for f in video._meta.fields])
