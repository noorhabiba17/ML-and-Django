from django.db import models

# Create your models here.

from django.db import models

class ParticlePrediction(models.Model):
    # The 10 features from the MAGIC dataset
    fLength = models.FloatField(help_text="Major axis of ellipse [mm]")
    fWidth = models.FloatField(help_text="Minor axis of ellipse [mm]")
    fSize = models.FloatField(help_text="10-log of sum of content of all pixels [photons]")
    fConc = models.FloatField(help_text="Ratio of sum of two highest pixels over fSize")
    fConc1 = models.FloatField(help_text="Ratio of highest pixel over fSize")
    fAsym = models.FloatField(help_text="Distance from highest pixel to center, projected onto major axis [mm]")
    fM3Long = models.FloatField(help_text="3rd root of third moment along major axis [mm]")
    fM3Trans = models.FloatField(help_text="3rd root of third moment along minor axis [mm]")
    fAlpha = models.FloatField(help_text="Angle of major axis with vector to origin [deg]")
    fDist = models.FloatField(help_text="Distance from origin to center of ellipse [mm]")

    # Prediction Result
    # We store 'gamma' or 'hadron'
    prediction_label = models.CharField(max_length=10)
    # We can also store the probability score if your SVM is configured for it
    confidence_score = models.FloatField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction_label} detected at {self.created_at}"
