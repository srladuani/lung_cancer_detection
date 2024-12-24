from django.db import models

class XrayImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    prediction = models.BooleanField(default=False)  # False: non-cancerous, True: cancerous
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - Prediction: {self.prediction}"
