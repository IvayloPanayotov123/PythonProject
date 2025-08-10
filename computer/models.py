from django.db import models

class Computer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ram = models.ForeignKey('rams.RAM', on_delete=models.CASCADE)
    gpu = models.ForeignKey('gpus.GPU', on_delete=models.CASCADE)
    cpu = models.ForeignKey('cpus.CPU', on_delete=models.CASCADE)
    creator = models.ForeignKey('accounts.AppUser', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        total_score = self.ram.score + self.gpu.score + self.cpu.score
        self.price = total_score * 1.2
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name