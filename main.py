from fastapi import FastAPI
import csv

app = FastAPI()


@app.get("/cities")
async def cities(country, region):
    with open('world.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        list_of_cities = ['Other city']
        for row in reader:
            if row['country'] == country:
                if row['subcountry'] == region:
                    list_of_cities.append(row['name'])
        print(list_of_cities)
        return list_of_cities