from django.db import models


class Review(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=(
            (1, "1 - Ruim"),
            (2, "2 - Regular"),
            (3, "3 - Bom"),
            (4, "4 - Muito Bom"),
            (5, "5 - Excelente"),
        )
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.book} por {self.user}"
