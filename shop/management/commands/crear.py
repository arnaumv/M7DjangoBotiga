# crear.py

from django.core.management.base import BaseCommand
from faker import Faker
from faker_vehicle import VehicleProvider
from shop.models import Categoria, Tag, Producte, Cistella, Compra, DetallCompra, User
import random

class Command(BaseCommand):
    help = 'Creates fake data for Botiga models'

    def handle(self, *args, **kwargs):
        # Create a Faker instance
        fake = Faker()
        fake.add_provider(VehicleProvider)

        # Generate and insert fake data for User
        for _ in range(10):  # Change this number to the amount of data you want to generate
            user = User(username=fake.user_name(), email=fake.email())
            user.save()

        # Generate and insert fake data for Categoria
        for _ in range(10):  # Change this number to the amount of data you want to generate
            categoria = Categoria(nom=fake.vehicle_make(), descripcio=fake.text())
            categoria.save()

        # Generate and insert fake data for Tag
        for _ in range(10):
            tag = Tag(nom=fake.vehicle_model())
            tag.save()

        # Get all categories and tags
        categories = Categoria.objects.all()
        tags = Tag.objects.all()

        # Generate and insert fake data for Producte
        for _ in range(10):
            producte = Producte(
                nom=fake.vehicle_year_make_model(),
                descripcio=fake.text(),
                preu=fake.random_number(digits=2, fix_len=True),
                categoria=random.choice(categories),
                quantitat_disponible=fake.random_int(min=1, max=100)
            )
            producte.save()
            producte.tags.set(random.choices(tags, k=fake.random_int(min=1, max=5)))

        # Get all users and products
        users = User.objects.all()
        products = Producte.objects.all()

        # Generate and insert fake data for Cistella
        for _ in range(10):
            cistella = Cistella(usuari=random.choice(users), quantitat=fake.random_int(min=1, max=10))
            cistella.save()
            cistella.producte.set(random.choices(products, k=fake.random_int(min=1, max=5)))

        # Generate and insert fake data for Compra and DetallCompra
        for _ in range(10):
            compra = Compra(
                usuari=random.choice(users),
                data_compra=fake.date_time_this_year(),
                preu_total=fake.random_number(digits=2, fix_len=True)
            )
            compra.save()
            for _ in range(fake.random_int(min=1, max=5)):
                detall_compra = DetallCompra(
                    producte=random.choice(products),
                    compra=compra,
                    quantitat=fake.random_int(min=1, max=10),
                    preu_unitari=fake.random_number(digits=2, fix_len=True)
                )
                detall_compra.save()

        self.stdout.write(self.style.SUCCESS('Successfully created fake data for Botiga models'))