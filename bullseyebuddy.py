import urllib2
import json

from bs4 import BeautifulSoup


prod_id = '003-05-0451'
store_id = '1375'
api_key = 'Id8SS1KAXuFd2W7R60XC5AUTTGKbnU2U'

base_url = 'http://api.target.com/products/v3'
data = json.dumps({'key': api_key, 'product_id' : prod_id, 'store_id' : '1375', 'fields': 'in_store_locations', 'id_type' : 'dpci'})

url='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, '1375', 'in_store_locations', 'dpci')


response = urllib2.urlopen(url)
data = json.loads(response.read())
a= data[u'product_composite_response'][u'items'][0]



print '\n'
'''{
	'imn_identifier': 11060366,
	'is_circular_publish': True,
	'identifier':
		[
			{u'source': u'Online and Store',
			u'is_primary': None,
			u'id_type': u'DPCI',
			u'id': u'003-05-0451'},
			
			{u'source': u'Online', u'is_primary': None, u'id_type': u'TCIN', u'id': u'12972711'}
		],
	'dpci': u'003-05-0451',
	'business_process_status':
		[
			{u'process_status':
				{u'operation_description': u'assortment ready',
				u'operation_code': u'PAAP', u'is_ready': True
				}
			},

			{
				u'process_status':
				{u'operation_description': u'import ready',
				u'operation_code': u'PIPT',
				u'is_ready': False
				}
			},

			{u'process_status':
				{
					u'operation_description': u'order ready',
					u'operation_code': u'PORD',
					u'is_ready': True
				}
			},

			{u'process_status':
				{
					u'operation_description': u'presentation ready',
					u'operation_code': u'PPRS',
					u'is_ready': True
				}
			},

			{u'process_status':
				{u'operation_description': u'project ready',
				u'operation_code': u'PCMT',
				u'is_ready': True
				}
			},

			{
				u'process_status':
					{u'operation_description': u'replenishment ready',
					u'operation_code': u'PRPL',
					u'is_ready': True
					}
			},

			{u'process_status': 
				{u'operation_description': u'scale ready',
				u'operation_code': u'PSCL',
				u'is_ready': False}
			},

			{u'process_status':
				{u'operation_description': u'target.com ready',
				u'operation_code': u'PTGT',
				u'is_ready': True}
			}],

	'general_description': u'Windex Blue Refill 2L',
	'class_id': 5,
	'in_store_location':
		[
			{u'aisle': 23,
			u'smart_schematic': u'4-1-4.90',
			u'floor': u'01',
			u'block_aisle': u'Q-23',
			u'section': 3, u'block': u'Q'}
		],

	'relation_description': u'Stand Alone',
	'relation': u'SA',
	'store_product':
		[
			{u'location_data':
				{u'location_id': 1375}
			}
		],
	'item_id': 451,
	'data_page_link': u'http://www.target.com/p/windex-original-glass-cleaner-refill-67-6-oz/-/A-12972711',
	'is_sellable': True,
	'is_orderable': True,
	'department_id': 3}'''

#print a['in_store_location']
#print a['in_store_location']

print "item #%s is located at aisle %s in block %s floor %s" % (prod_id, a['in_store_location'][0]['aisle'], a['in_store_location'][0]['block'], a['in_store_location'][0]['floor'])





