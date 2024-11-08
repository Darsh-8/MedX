from django.db import models


class BrainTumourImage(models.Model):
    image = models.ImageField(
        upload_to='uploads/')  # Update path for Vultr cloud storage if needed
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Placeholder for cloud-based storage:
    # Adjust 'upload_to' to your cloud storage path or use a file field that integrates with cloud storage solutions
    # image = models.ImageField(upload_to='your-cloud-path/')

    # Ensure 'uploads' or cloud storage path is configured in settings.py
