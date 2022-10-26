import csv
import datetime
from faker import Faker

fake = Faker()
MAX_RANGE = 50000

with open('gen_data.csv', 'w') as csvfile:
    field_names = ['author', 'content']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for i in range(0, MAX_RANGE):
        writer.writerow({
            'author': fake.name(),
            'content': fake.sentence(nb_words=16, variable_nb_words=True),
        })