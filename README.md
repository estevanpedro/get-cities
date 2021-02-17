# get-cities

Heroku
https://find-cities.herokuapp.com/cities

// How to use with Axios

```
import axios from 'axios'

const URL: string = 'https://find-cities.herokuapp.com/cities'

export const findCities = async (country: string, region: string) => {
  try {
    const response = await axios.get(URL, {
      params: {
        country,
        region,
      },
    })
    if (!response.data) {
      return ['Other']
    }
    return response.data
  } catch (error) {
    return ['Other']
  }
}
```
