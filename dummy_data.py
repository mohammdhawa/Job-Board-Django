import os
import django

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Initialize Django setup
django.setup()

from faker import Faker
import random
from django.contrib.auth.models import User

# Import models after Django setup
from cities_light.models import City  # Ensure this import is correct
from job.models import Job, Category

# Print to check everything is running fine
print("Hello World")

# Your logic for fake data generation (as an example)
fake = Faker()

def seed_project(n):
    print("\n\n******************* HELLO - 1 **************************\n\n")
    users = User.objects.all()
    job_type = ['full time', 'part time']
    categories = Category.objects.all()
    cities = City.objects.all()
    print("\n\n******************* HELLO **************************\n\n")
    for _ in range(n):
        city = random.choice(cities)
        print(f"Selected city: {city}")
        images = [
            '1.jpg', '1.png', '2.png', '2.webp', '3.jpeg', '4.jpeg', '5.png',
            '6.jpg', '7.png', '8.png', '9.png', '10.png', '11.png', '13.jpg',
            '14.jpg', '15.jpeg', '16.jpg', '17.jpg', '18.jpg', '19.jpg',
            '20.jpg'
        ]
        Job.objects.create(
            owner=random.choice(users),
            title=fake.name(),
            city=city,
            job_type=random.choice(job_type),
            description=fake.text(max_nb_chars=250),
            vacancy=random.randint(1, 10),
            salary=random.randint(10000, 99999),
            category=random.choice(categories),
            experience=random.randint(1, 10),
            image=f"jobs/{random.choice(images)}"
        )

def delete_all():
    jobs = Job.objects.order_by('-id')[:5]
    for job in jobs:
        job.delete()
    print("successfully deleted all jobs")

seed_project(500)
# delete_all()