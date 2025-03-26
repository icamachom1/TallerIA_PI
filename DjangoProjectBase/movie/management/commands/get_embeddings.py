import os
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Get embedding from a random movie "

    def handle(self, *args, **kwargs):

        random_movie = Movie.objects.order_by("?").first()  # Obtener película al azar
        embedding_vector = np.frombuffer(random_movie.emb, dtype=np.float32)
        print("🎦 Película aleatoria: ", random_movie.title, ", Primeros valores del embedding: ", embedding_vector[:5])  # Muestra los primeros valores

