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

with open('cheese_pizza.wav', 'rb') as audio_file:
  result = speech_to_text.recognize(audio_file, content_type='audio/wav')
  # TODO: Fix harcoding to access translated text 
  text = result['results'][0]['alternatives'][0]['transcript'].strip()
  text = 'cartwheel deals'
  if 'cartwheel' in text:
    url_var = "https://cartwheel-secure.target.com/browse"
    req = urllib2.Request(url_var, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    soup = BeautifulSoup(con, "html.parser")

    all_offers = soup.findAll('div', class_="large-3")
    print all_offers
    first_offer = all_offers[0]
    second_offer = all_offers[1]
    third_offer = all_offers[2]
    prod_id = url_first[5 : 10
    first_offer = all_offers[0]]


    pass
  else:
    text = '%20'.join(text.split())

    url_var = "http://www.target.com/s?category=0|All|matchallpartial|all+categories&searchTerm=%s" % text

    req = urllib2.Request(url_var, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    soup = BeautifulSoup(con, "html.parser")

    first_link = soup.find('a', class_="productClick")
    url_first = first_link.get('href')
    index = url_first.index('/A-') + 3
    prod_id = url_first[index : index +8]
    # print url_first
    # print prod_id
    id_type = 'tcin'
    store_id = '1375'
    api_key = 'Id8SS1KAXuFd2W7R60XC5AUTTGKbnU2U'

    base_url = 'http://api.target.com/products/v3'
    data = json.dumps({'key': api_key, 'product_id' : prod_id, 'store_id' : store_id, 'fields': 'in_store_locations', 'id_type' : id_type})

    url_locations ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, store_id, 'in_store_locations', id_type)
    url_pricing ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, store_id, 'pricing', id_type)
    # url_nutrients ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, store_id, 'nutrients', id_type)


    response_locations = urllib2.urlopen(url_locations)
    data_locations = json.loads(response_locations.read())
    array_locations= data_locations[u'product_composite_response'][u'items'][0]

    response_pricing = urllib2.urlopen(url_pricing)
    data_pricing = json.loads(response_pricing.read())
    array_pricing= data_pricing[u'product_composite_response'][u'items'][0]

    # response_nutrients = urllib2.urlopen(url_nutrients)
    # data_nutrients = json.loads(response_nutrients.read())
    # array_nutrients= data_nutrients[u'product_composite_response'][u'items'][0]

    # print 'location info'
    # print array_locations
    # print 'pricing info'
    print array_pricing
    # print 'nutrition info'
    # print array_nutrients



    if 'in_store_location' in array_locations:
      if 'percentage_saved' in array_pricing:
        useful_locations = array_locations["in_store_location"][0]
        useful_pricing = array_pricing["online_price"]
        speech =  "Wuhf Bark. Item %s is located at aisle %s in block %s floor %s. You will save %s percent on this item." % (array_locations['general_description'], useful_locations['aisle'], useful_locations['block'], useful_locations['floor'], useful_pricing['percentage_saved'])
      else:
        useful_locations = array_locations["in_store_location"][0]
        speech =  "Wuhf Bark. Item %s is located at aisle %s in block %s floor %s. Target does not currently have any discounts on this item." % (array_locations['general_description'], useful_locations['aisle'], useful_locations['block'], useful_locations['floor'])

    else:
      speech= "Item %s is not found in this location. Please visit target.com." % (array_locations['general_description'])
    pass



print speech

ALPHABET = string.ascii_lowercase

text_to_speech = TextToSpeechV1(
    username='c4fb92e9-8a5b-4b6a-9c7b-338ca22b9aae',
    password='QZ7UpoSxwb4j')


def random_word(length):
   return 'bullseye_output_' + \
   		''.join(random.choice(string.ascii_lowercase) for i in range(length))

with open('{0}.wav'.format(random_word(4)), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(
    	speech, accept='audio/wav', voice='en-US_AllisonVoice'))
