import pandas as pd
import numpy as np
from functools import reduce

df=pd.read_csv("/content/drive/MyDrive/Dataset/BL-Flickr-Images-Book.csv")

df.shape

for col in df:
  print(col)

to_drop=["Edition Statement", "Corporate Author", "Corporate Contributors", "Former owner", "Engraver", "Contributors", "Issuance type", "Shelfmarks"]

df.drop(to_drop, inplace=True, axis=1)
df.head()

for col in df.columns:
  print(col)

df.set_index('Identifier', inplace=True)
df.head()

df['Date of Publication'].head(25)

unwanted_char=['[', '-', ',']

def clean_dates(item):
  dop=str(item.loc['Date of Publication'])

  if dop=='nan' or dop=='[':
    return np.NaN

  for character in unwanted_char:
    if character in dop:
      character_index=dop.find(character)
      dop=dop[:character_index]
  return dop

df['Date of Publication'] = df.apply(clean_dates, axis=1)
df['Date of Publication'].head(25)

def clean_title(title):
  if title=='nan':
    return 'NaN'

  if title[0]=='[':
    title=title[1: title.find(']')]

  if 'by' in title:
    title=title[:title.find('by')]
  elif 'By' in title:
    title=title[:title.find('By')]

  if '[' in title:
    title=title[:title.find('[')]

  title=title[:-2]

  title=list(map(str.capitalize, title.split()))
  return ' '.join(title)

df['Title']=df['Title'].apply(clean_title)
df.head()

