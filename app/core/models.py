from django.db import models


class Base(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)
    active = models.BooleanField('Is Active?', default=True)

    class Meta:
        abstract = True


class Person(Base):
    name = models.CharField('Name', max_length=100)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
    
    def __str__(self):
        return self.name


class TimesISaved(Base):
    when = models.DateField('When?')
    how = models.TextField('How?', max_length=255)
    thanks = models.ManyToManyField(Person, verbose_name="Who I thank for")

    def get_thanks(self):
        return ", ".join([p.name for p in self.thanks.all()])

    class Meta:
        verbose_name = 'Time I saved'
        verbose_name_plural = 'Times I saved'


class TimesYouSaved(Base):
    when = models.DateField('When?')
    how = models.TextField('How?', max_length=255)
    thanks = models.ManyToManyField(Person, verbose_name="Thanks to?")

    def get_thanks(self):
        return ", ".join([p.name for p in self.thanks.all()])

    class Meta:
        verbose_name = 'Time you saved'
        verbose_name_plural = 'Times you saved'

