# Divvy_Stations_2013_corrupt

- `dpcapacity`: one station has an outlier number of `-999`
- `latitude`: 'hello'
- `longitude`: 'world'
- `latitude`: one value is 44.xyz; that is a latitude outlier given the distribution of values.
- `online date`: one of the months was swapped with the day, so it is now "day/month/year"

# smartphone_sanitization_corrupt

- `site`: has plurals.
- `colonies_post`: has `-999` value.
- `colonies_pre`: detection upper-limit is 100. Data entry error: 199 and 200.
- `year`: has one year from the future. Data entry error.
- `treatment`: one mis-spelled treatment name.

# applicant_information

- `Country of ...`: Mixed names for USA, Mexico; has `dfasd`
- `Financial Aid Need`: Needs downstream processing.

# boston_ei-corrupt

- `labor_force_part_rate`: has one value encoded as a percentage > 1.0 (e.g. 0.56 encoded as 56.)
