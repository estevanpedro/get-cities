from fastapi import FastAPI
from iris.router import iris_classifier_router
import csv

app = FastAPI()
app.include_router(iris_classifier_router.router, prefix='/iris')


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