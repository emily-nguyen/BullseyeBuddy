import json
import random 
import string
import urllib2

from bs4 import BeautifulSoup
from pydub import AudioSegment
from watson_developer_cloud import SpeechToTextV1, TextToSpeechV1


# speech_to_text = SpeechToTextV1(
#     username='26664ba5-62a0-4e3b-b070-816fa4a67837',
#     password='kw44VBtY0T3P')

# print(json.dumps(speech_to_text.models(), indent=2))

# sound = AudioSegment.from_file('.wma')
# sound.export('test.wav', format='wav')

# with open('test.wav', 'rb') as audio_file:
# 	result = speech_to_text.recognize(audio_file, content_type='audio/wav')
# 	print(result)    

# 	# TODO: Fix harcoding to access translated text 
# 	text = result['results'][0]['alternatives'][0]['transcript'].strip()
# 	print(text)
text  =  'french%20toast%20cinnamon'



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

store_id = '1375'
api_key = 'Id8SS1KAXuFd2W7R60XC5AUTTGKbnU2U'

base_url = 'http://api.target.com/products/v3'
data = json.dumps({'key': api_key, 'product_id' : prod_id, 'store_id' : '1375', 'fields': 'in_store_locations', 'id_type' : 'tcin'})

url='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, '1375', 'in_store_locations', 'tcin')


response = urllib2.urlopen(url)
data = json.loads(response.read())
a= data[u'product_composite_response'][u'items'][0]


print "item %s is located at aisle %s in block %s floor %s" % (a['general_description'], a['in_store_location'][0]['aisle'], a['in_store_location'][0]['block'], a['in_store_location'][0]['floor'])

# ALPHABET = string.ascii_lowercase

# text_to_speech = TextToSpeechV1(
#     username='c4fb92e9-8a5b-4b6a-9c7b-338ca22b9aae',
#     password='QZ7UpoSxwb4j')

# print(json.dumps(text_to_speech.voices(), indent=2))

# def random_word(length):
#    return 'bullseye_output_' + \
#    		''.join(random.choice(string.ascii_lowercase) for i in range(length))

# with open('{0}.wav'.format(random_word(4)), 'wb') as audio_file:
#     audio_file.write(text_to_speech.synthesize(
#     	'Wuhf Bark. Lucky Charms is on Aisle 3', accept='audio/wav', voice='en-US_AllisonVoice'))