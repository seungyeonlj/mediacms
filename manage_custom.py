#!/usr/bin/env python3
import os
import django

# point to your settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
django.setup()

from files.models import Media

read_only_fields = (
            "friendly_token",
            "user",
            "add_date",
            "views",
            "media_type",
            "state",
            "duration",
            "encoding_status",
            "views",
            "likes",
            "dislikes",
            "reported_times",
            "size",
            "video_height",
            "is_reviewed",
        )
# video = Media.objects.get(id=20)
videos = Media.objects.filter(category=2)
for video in videos:
    video.views += 2000
    video.likes += 400
    video.dislikes += 100
    video.category.set([1,2])
    video.add_date = "2024-07-24 12:24"
    tag_names = ["tag", "sample_tag"]
    from files.models import Tag
    tags = [Tag.objects.get_or_create(title=name)[0] for name in tag_names]
    video.tags.set(tags)    
    """
    video.tags.set([tag1, tag2])         # tag1, tag2 are Tag instances
    # or
    video.tags.set([1, 2, 3])            # 1, 2, 3 are Tag IDs
    """
    video.save()
    print(f"Updated video {video.id} views to {video.views}")
    break


# fields
print([f.name for f in video._meta.fields])
