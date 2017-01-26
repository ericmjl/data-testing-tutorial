import pandas as pd 

class StationsValidator():

	def column_latitude_dtype(self, filepath):
		df = pd.read_csv(filepath, index_col=0)

		assert df['latitude'].dtype == float