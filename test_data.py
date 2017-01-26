from stations_validator import StationsValidator

data_file = 'data/Divvy_Stations_2013.csv'
data_corrupt_file = 'data/Divvy_stations_2013_corrupt.csv'



sv = StationsValidator()

sv.column_latitude_dtype(data_file)
sv.column_latitude_dtype(data_corrupt_file)

