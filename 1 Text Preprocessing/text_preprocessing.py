# -*- coding: utf-8 -*-
"""Text Preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/114lpDrrUUMyCBjCMQCB8kHEtKB46RUkM
"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/IMDB Dataset.csv')
df.head()

df.shape

"""## Lowercasing"""

df['review'][1].lower()

df['review'] = df['review'].str.lower()

df

"""## Remove HTML Tags"""

import re
def remove_html_tags(text):
  pattern = re.compile('<.*?>')
  return pattern.sub(r'', text)

text = "A wonderful little production. <br /><br />The filming technique is very unassuming- very old-time-BBC fashion and gives a comforting, and sometimes discomforting, sense of realism to the entire piece. <br /><br />The actors are extremely well chosen- Michael Sheen not only \"has got all the polari\" but he has all the voices down pat too! You can truly see the seamless editing guided by the references to Williams' diary entries, not only is it well worth the watching but it is a terrificly written and performed piece. A masterful production about one of the great master's of comedy and his life. <br /><br />The realism really comes home with the little things: the fantasy of the guard which, rather than use the traditional 'dream' techniques remains solid then disappears. It plays on our knowledge and our senses, particularly with the scenes concerning Orton and Halliwell and the sets (particularly of their flat with Halliwell's murals decorating every surface) are terribly well done."

remove_html_tags(text)

df['review'] = df['review'].apply(remove_html_tags)

df['review'][3]

"""## Remove URL's"""

def remove_url(text):
  pattern = re.compile(r'https?://\S+|www\.\S+')
  return pattern.sub(r'', text)

text1 = 'Check out my notebook https://www.kaggle.com/campusx/notebook00123'
text2 = 'Check out my notebook http://www.kaggle.com/campusx/notebook99'
text3 = 'Google search here www.google.com'
text4 = 'For notebook click https://www.kaggle.com/campusx/notebook948 to search check www.google.com'

remove_url(text4)

"""## Removing Punctuations"""

import string, time
string.punctuation

exclude = string.punctuation

def remove_punc(text):
  for char in exclude:
    text = text.replace(char, '')
  return text

text = 'string. With. Punctuation?'

start = time.time()
print(remove_punc(text))
time1 = time.time() - start
print(time1)

def remove_punc1(text):
  return text.translate(str.maketrans('', '', exclude))

start = time.time()
print(remove_punc(text))
time2 = time.time() - start
print(time2)

time1/time2

df['review'] = df['review'].apply(remove_punc1)

df['review'][2]

"""## Chat Word Treatment"""

internet_slang_dict = {
    "AFAIK": "As Far As I Know",
    "AFK": "Away From Keyboard",
    "ASAP": "As Soon As Possible",
    "ATK": "At The Keyboard",
    "ATM": "At The Moment",
    "A3": "Anytime, Anywhere, Anyplace",
    "BAK": "Back At Keyboard",
    "BBL": "Be Back Later",
    "BBS": "Be Back Soon",
    "BFN": "Bye For Now",
    "B4N": "Bye For Now",
    "BRB": "Be Right Back",
    "BRT": "Be Right There",
    "BTW": "By The Way",
    "B4": "Before",
    "CU": "See You",
    "CUL8R": "See You Later",
    "CYA": "See You",
    "FAQ": "Frequently Asked Questions",
    "FC": "Fingers Crossed",
    "FWIW": "For What It's Worth",
    "FYI": "For Your Information",
    "GAL": "Get A Life",
    "GG": "Good Game",
    "GN": "Good Night",
    "GMTA": "Great Minds Think Alike",
    "GR8": "Great!",
    "G9": "Genius",
    "IC": "I See",
    "ICQ": "I Seek you (also a chat program)",
    "ILU": "I Love You",
    "IMHO": "In My Honest/Humble Opinion",
    "IMO": "In My Opinion",
    "IOW": "In Other Words",
    "IRL": "In Real Life",
    "KISS": "Keep It Simple, Stupid",
    "LDR": "Long Distance Relationship",
    "LMAO": "Laugh My A.. Off",
    "LOL": "Laughing Out Loud",
    "LTNS": "Long Time No See",
    "L8R": "Later",
    "MTE": "My Thoughts Exactly",
    "M8": "Mate",
    "NRN": "No Reply Necessary",
    "OIC": "Oh I See",
    "PITA": "Pain In The A..",
    "PRT": "Party",
    "PRW": "Parents Are Watching",
    "QPSA?": "Que Pasa?",
    "ROFL": "Rolling On The Floor Laughing",
    "ROFLOL": "Rolling On The Floor Laughing Out Loud",
    "ROTFLMAO": "Rolling On The Floor Laughing My A.. Off",
    "SK8": "Skate",
    "STATS": "Your sex and age",
    "ASL": "Age, Sex, Location",
    "THX": "Thank You",
    "TTFN": "Ta-Ta For Now!",
    "TTYL": "Talk To You Later",
    "U": "You",
    "U2": "You Too",
    "U4E": "Yours For Ever",
    "WB": "Welcome Back",
    "WTF": "What The F...",
    "WTG": "Way To Go!",
    "WUF": "Where Are You From?",
    "W8": "Wait...",
    "7K": "Sick:-D Laugher",
    "TFW": "That feeling when",
    "MFW": "My face when",
    "MRW": "My reaction when",
    "IFYP": "I feel your pain",
    "TNTL": "Trying not to laugh",
    "JK": "Just kidding",
    "IDC": "I don’t care",
    "ILY": "I love you",
    "IMU": "I miss you",
    "ADIH": "Another day in hell",
    "ZZZ": "Sleeping, bored, tired",
    "WYWH": "Wish you were here",
    "TIME": "Tears in my eyes",
    "BAE": "Before anyone else",
    "FIMH": "Forever in my heart",
    "BSAAW": "Big smile and a wink",
    "BWL": "Bursting with laughter",
    "BFF": "Best friends forever",
    "CSL": "Can’t stop laughing"
}

print("LOL means:", internet_slang_dict["LOL"])

def chat_conversion(text):
  new_text = []
  for w in text.split():
    if w.upper() in internet_slang_dict:
      new_text.append(internet_slang_dict[w.upper()])
    else:
      new_text.append(w)
  return " ".join(new_text)

chat_conversion('IMHO he is the best')

df['review'] = df['review'].apply(chat_conversion)

df['review'][8]

"""## Spelling Correction"""

from textblob import TextBlob

incorrect_text = 'ceertain conditiona are eligibol for loan.'
textBlb = TextBlob(incorrect_text)
textBlb.correct().string

#from concurrent.futures import ThreadPoolExecutor

#def correct_spelling(review):
    #if isinstance(review, str):
        #return str(TextBlob(review).correct())
    #return review

# Parallel processing
#with ThreadPoolExecutor() as executor:
    #df['review'] = list(executor.map(correct_spelling, df['review']))

#df.to_csv("corrected_movies_dataset.csv", index=False)
#print("Completed with parallel processing.")

#df['review'][8]

"""## Removing Stop Words"""

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

stopwords.words('english')

def remove_stopwords(text):
  new_text = []

  for word in text.split():
    if word in stopwords.words('english'):
      new_text.append('')
    else:
      new_text.append(word)
  x = new_text[:]
  new_text.clear()
  return " ".join(x)

remove_stopwords('this is by far the worst of the nine (so far) movies. Even the chance to watch the well known characters interact in another movie can\'t save this movie - including the goofy scenes with Kirk, Spock and McCoy at Yosemite.<br /><br />I would say this movie is not worth a rental, and hardly worth watching, however for the True Fan who needs to see all the movies, renting this movie is about the only way you\'ll see it - even the cable channels avoid this movie.')

df['review'] = df['review'].apply(remove_stopwords)

df['review'][8]

"""# Handling Emojis"""

import re

def remove_emojis(text): # delete
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

remove_emojis("Hello 😃! Let's grab some 🍕 and 🍦!")

# Replace
def replace_emojis(text, replacement="*"):
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(replacement, text)

text = "I love 🥑 and 🏖️!"
print(replace_emojis(text, "[EMOJI]"))

#df['review'] = df['review'].apply(replace_emojis)

#df['review'][8]

"""## Tokenization

1. Using the split function
"""

# word tokenization
sent1 = 'I am going to delhi'
sent1.split()

# sentence tokenization
sent2 = 'I am going to delhi. I will stay there for 3 days. Let\'s hope the trip to be great'
sent2.split('.')

# problem with split function
sent3 = 'I am going to delhi!'
sent3.split()

sent4 = 'Where do you think I should go? I have 3 day holiday.'
sent4.split('.')

"""2. Regular Expression"""

import re
sent3 = 'I am going to delhi!'
tokens = re.findall("[\w']+", sent3)
tokens

text = """I thought this movie did a down right good job. It wasn't as creative or original as the first, but who was expecting it to be. It was a whole lotta fun. the more i think about it the more i like it, and when it comes out on DVD I'm going to pay the money for it very proudly, every last cent. Sharon Stone is great, she always is, even if her movie is horrible(Catwoman), but this movie isn't, this is one of those movies that will be underrated for its lifetime, and it will probably become a classic in like 20 yrs. Don't wait for it to be a classic, watch it now and enjoy it. Don't expect a maste."""
sentences = re.compile('[.,!?]').split(text)
sentences

"""3. NLTK"""

import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize, sent_tokenize

sent1 = 'I am going to visit delhi!'
word_tokenize(sent1)

text = """ to be. It was a whole lotta fun. the more i think about it the more i like it, and when it comes out on DVD I'm going to pay the money for it very proudly, every last cent. Sharon Stone is great, she always is, even if her movie is horrible(Catwoman), but this movie isn't, this is one of those movies that will be underrated for its lifetime, and it will probably become a classic in like 20 yrs. Don't wait for it to be a classic, watch it now and enjoy it. Don't expect a masterpiece, or something thats gripping and soul touching"""
sent_tokenize(text)

sent5 = 'I have a Ph.D in A.I'
sent6 = "We're here to help! mail us john.rutledge@examplepetstore.comcom"
sent7 = 'A 5km ride cost $10.50'

word_tokenize(sent5)

word_tokenize(sent5)

word_tokenize(sent6)

word_tokenize(sent7)

"""4. Spacy"""

import spacy
nlp = spacy.load('en_core_web_sm')

doc1 = nlp(sent5)
doc2 = nlp(sent6)
doc3 = nlp(sent7)
doc1 = nlp(sent1)

for token in doc2:
  print(token)

#df['review'] = df['review'].apply(lambda x: word_tokenize(x))

#df['review'][8]

"""## Stemming

is the process of reducing inflection in words to their root forms such as mapping a group of words to the same stem even if the stem itself is not a valid word in the language.
"""

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
def stem_words(text):
  return "".join([ps.stem(word) for word in text.split()])

sample = "walk walks walking walked"
stem_words(sample)

text = 'He was running and eating at the same time. He has bad habit of swimming after playing long hours in the sun'
print(text)

stem_words(text)

"""## Lemmatization"""

import nltk
from nltk.stem import WordNetLemmatizer

# Download the 'wordnet' dataset
nltk.download('wordnet')

wordet_lemmatizer = WordNetLemmatizer()

sentence = "He was running and eating at the same time. He has bad habit of swimming after playing long hours in the sun"
punctuations = "?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
  if word in punctuations:
    sentence_words.remove(word)

sentence_words
print("{0:20}{1:20}".format("Word", "Lemma"))
for word in sentence_words:
  print("{0:20}{1:20}".format(word, wordet_lemmatizer.lemmatize(word, pos="v")))