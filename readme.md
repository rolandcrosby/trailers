# New York City Trailer Data

Semi-truck combinations longer than 55 feet total [are illegal on all streets in New York City](https://www1.nyc.gov/html/dot/html/motorist/sizewt.shtml). Therefore, 48- and 53-foot trailers are impossible to legally tow on city streets, since all tractors (even the European-style cab-over types) extend more than 7 feet beyond the front of the trailer.

Truck operators disregard these rules throughout the city on a daily basis. In fact, NYC businesses have brazenly registered illegal oversize trailers in all five boroughs.

This project is an attempt to understand the scale of this last problem.

## Data Sources

Data on trailers registered in New York City comes from the New York State [Vehicle, Snowmobile, and Boat Registrations dataset](https://data.ny.gov/Transportation/Trailers-Registered-in-New-York-City/rcmm-pc7d).

Trailer length was determined where possible based on trailer VINs using the [NHTSA Vehicle API](https://vpic.nhtsa.dot.gov/api/).

## Results as of 2019-07-04

Count | Description
-|-
13,259 | Total trailers registered in New York City
7,732 | Trailers for which the NHTSA has length data
833 | NHTSA-verified trailers 48' or longer
357 | NHTSA-verified trailers 53' or longer

## Future work

- Extrapolate lengths of trailers for which the NHTSA has no length data, perhaps based on patterns in registered weight data
