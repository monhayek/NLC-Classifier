pip install --upgrade watson-developer-cloud

#Replace your service username and your password with your credentials

from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='',
  password='')
  
#Example request
import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='',
  password='')

with open('../path/todata/csv/TicketClass.train.csv', 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name='Ticket Class',
    language='en'
  )
print(json.dumps(classifier, indent=2))
