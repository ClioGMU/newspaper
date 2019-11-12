from django.db import models


class NameInput(models.Model):
    raw = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.raw[:25]

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)  # Call the "real" save() method.

        names = self.raw.split(",")
        # Just for demonstration
        for name in names:
            print(name)

        # Create Name objects
        for name in names:
            Name.objects.create(name=name, source=self)


class Name(models.Model):
    name = models.CharField(max_length=200)
    source = models.ForeignKey(NameInput, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
