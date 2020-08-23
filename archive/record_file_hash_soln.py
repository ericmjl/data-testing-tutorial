from tinydb import TinyDB
from datetime import datetime
import datafuncs_soln as dfn


db = TinyDB('data_integrity/hashes.db')

f = 'Divvy_Stations_2013.csv'
filehash = dfn.hash_file(f'data/{f}')
record = dict()
record['filename'] = f'data/{f}'
record['hash'] = filehash
record['datetime_hashed'] = datetime.today().isoformat()
db.insert(record)
