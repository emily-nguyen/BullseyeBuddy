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

ALPHABET = string.ascii_lowercase

text_to_speech = TextToSpeechV1(
 username='c4fb92e9-8a5b-4b6a-9c7b-338ca22b9aae',
 password='QZ7UpoSxwb4j')

def random_word(length):
  return 'bullseye_output_' + \
  ''.join(random.choice(string.ascii_lowercase) for i in range(length))

  

search_strings = ['cartwheel.wav', 'french_toast_cinnamon.wav', 'cheese_pizza.wav', 'toothbrush.wav', 'pink_shirt.wav', 'asdfghjkl.wav']
for sound_file in search_strings:
  with open(sound_file, 'rb') as audio_file:
    result = speech_to_text.recognize(audio_file, content_type='audio/wav')

    text = result['results'][0]['alternatives'][0]['transcript'].strip()

    print text
    text = '%20'.join(text.split())

    url_var = "http://www.target.com/s?category=0|All|matchallpartial|all+categories&searchTerm=%s" % text

    cart_url = "https://cartwheel-secure.target.com/browse"

    req_item = urllib2.Request(url_var, headers={'User-Agent' : "Magic Browser"}) 
    con_item = urllib2.urlopen( req_item )
    soup_item = BeautifulSoup(con_item, "html.parser")


    req_cart = urllib2.Request(cart_url, headers={'User-Agent' : "Magic Browser"}) 
    con_cart = urllib2.urlopen( req_cart )
    soup_cart = BeautifulSoup(con_cart, "html.parser")

    if 'cartwheel' in text:
      all_offers = soup_cart.findAll('h3', class_="card--name_back")
      index1 = str(all_offers[0]).index('</h3>')
      index2 = str(all_offers[0]).index('>') + 1
      first_offer = str(all_offers[0])[index2 : index1]
      index1 = str(all_offers[1]).index('</h3>')
      index2 = str(all_offers[1]).index('>') + 1
      second_offer = str(all_offers[1])[index2 : index1]
      second_offer = second_offer.replace("&amp;", ", and, ")
      print second_offer
      index1 = str(all_offers[2]).index('</h3>')
      index2 = str(all_offers[2]).index('>') + 1
      third_offer = str(all_offers[2])[index2 : index1]
      
      speech= "Arf. Today's trending Cartwheel deals are on %s, %s, and %s. Bark" % (first_offer, second_offer, third_offer)

      pass
    else:
      first_link = soup_item.find('a', class_="productClick")
      if first_link:  # if first_link is not None, i.e. if target.com has SOME result for our query
        url_first = first_link.get('href')
        index = url_first.index('/A-') + 3
        prod_id = url_first[index : index +8]

        id_type = 'tcin'
        store_id = '1375'
        api_key = 'Id8SS1KAXuFd2W7R60XC5AUTTGKbnU2U'

        base_url = 'http://api.target.com/products/v3'
        data_l = json.dumps({'key': api_key, 'product_id' : prod_id, 'store_id' : store_id, 'fields': 'in_store_locations', 'id_type' : id_type})
        data_p = json.dumps({'key': api_key, 'product_id' : prod_id, 'store_id' : store_id, 'fields': 'pricing', 'id_type' : id_type})

        url_locations ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, store_id, 'in_store_locations', id_type)
        url_pricing ='http://api.target.com/products/v3?key=%s&product_id=%s&store_id=%s&fields=%s&id_type=%s' % (api_key, prod_id, store_id, 'pricing', id_type)


        response_locations = urllib2.urlopen(url_locations)
        data_locations = json.loads(response_locations.read())
        array_locations= data_locations[u'product_composite_response'][u'items'][0]

        response_pricing = urllib2.urlopen(url_pricing)
        data_pricing = json.loads(response_pricing.read())
        array_pricing= data_pricing[u'product_composite_response'][u'items'][0]

        if 'in_store_location' in array_locations:
          if 'percentage_saved' in array_pricing['online_price']:
            useful_locations = array_locations["in_store_location"][0]
            useful_pricing = array_pricing["online_price"]
            speech =  "Wuhf Bark. Item %s is located at aisle %s in block %s floor %s. You will save %s percent on this item." % (array_locations['general_description'], useful_locations['aisle'], useful_locations['block'], useful_locations['floor'], useful_pricing['percentage_saved'])
          else:
            useful_locations = array_locations["in_store_location"][0]
            speech =  "Wuhf Bark. Item %s is located at aisle %s in block %s floor %s. Target does not currently have any discounts on this item." % (array_locations['general_description'], useful_locations['aisle'], useful_locations['block'], useful_locations['floor'])
        else:
          speech= "Bark! Item %s is not found in this location. Please visit target.com." % (array_locations['general_description'])
          pass
      else:
        speech = "Rufff! Sorry! We could not find an item with that name."
  print speech
  random_word(4);
  with open('{0}.wav'.format(random_word(4)), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(
    speech, accept='audio/wav', voice='en-US_AllisonVoice'))
  raw_input()
