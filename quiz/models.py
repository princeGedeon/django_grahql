from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    title=models.CharField(max_length=255,default=_("Nouveau Quiz"))
    category=models.ForeignKey(Category,default=1,on_delete=models.DO_NOTHING)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    SCALE=(
        (0,_('BASIQUE')),
        (1,_('DEBUTANT')),
        (2,_('INTERMEDIAIRE')),
        (3,_('Avancé')),
        (4,_('Expert'))
    )

    TYPE=(
        (0,_('Choix multiple'))
    )

    quiz=models.ForeignKey(Quizzes,related_name="question",on_delete=models.DO_NOTHING)
    technique=models.IntegerField(default=0,verbose_name=_("Type de question"))
    title=models.CharField(max_length=255,verbose_name=_("Title"))
    difficulty=models.BooleanField(default=0,verbose_name=_("Difficulté"))
    date_created = models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False,verbose_name=_("Statut active"))

class Answer(models.Model):
    question=models.ForeignKey(Question,related_name='answer',on_delete=models.DO_NOTHING)
    answer_text=models.CharField(max_length=255,verbose_name=_("Réponse texte"))
    is_right=models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
