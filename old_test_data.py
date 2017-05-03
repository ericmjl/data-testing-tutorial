import pandas as pd 

data = pd.read_csv('data/Divvy_Stations_2013.csv', index_col=0)
data_corrupt = pd.read_csv('data/Divvy_stations_2013_corrupt.csv', index_col=0)

def test_column_latitude_dtype():
	"""
	Checks that the dtype of the 'Latitude' column is a float.
	"""
	def column_latitude_dtype(df):

		assert df['latitude'].dtype == float

	column_latitude_dtype(data)
	column_latitude_dtype(data_corrupt)