from mapbox import Static
from mapbox import Geocoder
import mapbox

'''
export MAPBOX_ACCESS_TOKEN="pk.eyJ1IjoidGVzdGVybWlzbyIsImEiOiJja2VkY3RjbncwcW53MnNydmQ2ZjJhZXZ5In0.xquJPYqw4t4Mjsq06Nw66Q"
'''
if __name__ == '__main__':
	
	service = Static()
	portland = {
		'type': 'Feature',
		'properties': {'name': 'Portland, OR'},
		'geometry': {
			'type': 'Point',
			'coordinates': [-3.6803, 40.4067]}
		}
	
	bend = {
		'type': 'Feature',
		'properties': {'name': 'Bend, OR'},
		'geometry': {
			'type': 'Point',
			'coordinates': [-3.7703, 40.4067]}
		}
	
	response = service.image('mapbox.satellite', lon=portland['geometry']['coordinates'][0], lat=portland['geometry']['coordinates'][1], z=15, features=[portland])	

	#response = service.image('mapbox.satellite', features=[portland, bend])
	print(response)
	with open('./map.png', 'wb') as output:
		 _ = output.write(response.content)
	'''
	df = pd.read_csv('./data/farmacia.csv', header=0, delimiter=',', encoding='latin1')

	col = df.iloc[:, 6]
	print('ALKSJGFALSDJFALSKJGF')
	print(col.dtype)
	
	if col.type == 'float64': #and not all(x.is_integer() for x in col):
	field['db_type'] = 'decimal(10,8)'
	field['entity_type'] = 'sys.number'
	elif col.dtype in ('int64', 'float64'):
	field['db_type'] = 'integer'
	field['entity_type'] = 'sys.number'
	elif col.dtype in ('object', 'string_', 'unicode_'):
	col = col.astype(str)
	maxlen = max(col.apply(len))
	field['db_type'] = 'varchar(' + str(maxlen) + ')'
	field['entity_type'] = 'None'
	elif col.dtype == 'datetime64':
	field['db_type'] = 'date'
	field['entity_type'] = 'sys.date'
	
	'''
