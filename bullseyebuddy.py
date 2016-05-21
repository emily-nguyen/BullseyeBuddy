import json
import random 
import string
import urllib2

from bs4 import BeautifulSoup
from pydub import AudioSegment
from watson_developer_cloud import SpeechToTextV1, TextToSpeechV1


speech_to_text = SpeechToTextV1(
    username='26664ba5-62a0-4e3b-b070-816fa4a67837',
    password='kw44VBtY0T3P')

# sound = AudioSegment.from_file('cheese_pizza.wma')
# sound.export('test.wav', format='wav')

with open('french_toast_cinnamon.wav', 'rb') as audio_file:
	result = speech_to_text.recognize(audio_file, content_type='audio/wav')

	# TODO: Fix harcoding to access translated text 
	text = result['results'][0]['alternatives'][0]['transcript'].strip()

	print(text)

text = '%20'.join(text.split())

url_var = "http://www.target.com/s?category=0|All|matchallpartial|all+categories&searchTerm=%s" % text

req = urllib2.Request(url_var, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
soup = BeautifulSoup(con, "html.parser")

first_link = soup.find('a', class_="productClick")
url_first = first_link.get('href')
index = url_first.index('/A-') + 3
prod_id = url_first[index : index +8]
print url_first
print prod_id
prod_id = '12992579'

store_id = '1375'
api_key = 'Id8SS1KAXuFd2W7R60XC5AUTTGKbnU2U'

base_url = 'http://api.target.com/products/v3'
data = json.dumps({'key': api_key, 'product_id' : prod_id, 'store_id' : '1375', 'fields': 'in_store_locations', 'id_type' : 'tcin'})

url_locations ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, '1375', 'in_store_locations', 'tcin')
url_pricing ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, '1375', 'store_product_type_hierarchy', 'tcin')
url_nutrients ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, '1375', 'nutrients', 'tcin')


response_locations = urllib2.urlopen(url_locations)
data_locations = json.loads(response_locations.read())
array_locations= data_locations[u'product_composite_response'][u'items'][0]

response_pricing = urllib2.urlopen(url_pricing)
data_pricing = json.loads(response_pricing.read())
array_pricing= data_pricing[u'product_composite_response'][u'items'][0]

response_nutrients = urllib2.urlopen(url_nutrients)
data_nutrients = json.loads(response_nutrients.read())
array_nutrients= data_nutrients[u'product_composite_response'][u'items'][0]

print 'location info'
print array_locations
print 'pricing info'
print array_pricing
print 'nutrition info'
print array_nutrients

speech_location =  "Wuhf Bark. Item %s is located at aisle %s in block %s floor %s" % (array_locations['general_description'], array_locations['in_store_location'][0]['aisle'], array_locations['in_store_location'][0]['block'], array_locations['in_store_location'][0]['floor'])
speech_pricing =  "Ruff. Item %s is located at aisle %s in block %s floor %s" % (array_locations['general_description'], array_locations['in_store_location'][0]['aisle'], array_locations['in_store_location'][0]['block'], array_locations['in_store_location'][0]['floor'])

print speech_location

ALPHABET = string.ascii_lowercase

text_to_speech = TextToSpeechV1(
    username='c4fb92e9-8a5b-4b6a-9c7b-338ca22b9aae',
    password='QZ7UpoSxwb4j')


def random_word(length):
   return 'bullseye_output_' + \
   		''.join(random.choice(string.ascii_lowercase) for i in range(length))

with open('{0}.wav'.format(random_word(4)), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(
    	speech_location, accept='audio/wav', voice='en-US_AllisonVoice'))
