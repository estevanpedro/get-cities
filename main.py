from fastapi import FastAPI
import csv

app = FastAPI()


@app.get("/city/{country}/{region}")
async def city(country, region):
    with open('world.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        list_of_cities = ['Other city']
        for row in reader:
            if row['country'] == country:
                if row['subcountry'] == region:
                    list_of_cities.append(row['name'])
        return list_of_cities