from django.db import models

class PredictedParagraph(models.Model):
    CATEGORY_CHOICES = (
        ('POLITIQUE', 'POLITIQUE'),
        ('ECONOMIE', 'ECONOMIE'),
        ('SPORT', 'SPORT'),
        ('AUTRE', 'AUTRE'),
    )
    
    text = models.TextField()
    fake_p = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    true_p = models.DecimalField(max_digits=9, decimal_places=4, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    titre = models.CharField(max_length=200, default='titre')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='autre')

    def __str__(self):
        return self.titre
