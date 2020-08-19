# -*- coding: utf-8 -*-
"""OCR + Language Translation + Text to Speech.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yVunnmMjTsqZOPvbHazKk3bJOK9-Dy_U
"""

!pip install googletrans

!pip install pillow

!pip install gtts

!pip install ipython

!pip install easyocr

!wget https://i.stack.imgur.com/mk1jX.jpg

from googletrans import Translator

from gtts import gTTS

import easyocr

from IPython.display import Audio

reader=easyocr.Reader(['ta'])
reader = easyocr.Reader(['ta','en'])
translator = Translator()

import PIL
from PIL import ImageDraw
i = PIL.Image.open("mk1jX.jpg.2")
i

#reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
#result = reader.readtext('mk1jX.jpg.2')

#bounds = reader.readtext('mk1jX.jpg.2', add_margin= 0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch', blocklist='=.'
#bounds

bounds = reader.readtext('mk1jX.jpg.2')
bounds

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(i, bounds)

#text_list = reader.readtext('mk1jX.jpg.2', add_margin= 0.55, width_ths=0.7,link_threshold=0.8,decoder='beamsearch',blocklist=':
#text_list
#reader.readtext('chinese.jpg', detail = 0)

text_list = reader.readtext('mk1jX.jpg.2',detail= 0)
text_list

text_comb=' '.join(text_list)
text_comb

print(translator.detect(text_comb,src='ta'))

text_en = translator.translate(text_comb, src ='ta')
print(text_en.text)

ta_tts=gTTS(text_en.text)
ta_tts.save('trans.mp3')

Audio('trans.mp3',autoplay=True)



text_hi =translator.translate(text_comb,src='ta',dest='hi')
print(text_hi.text)

ta_tts_hi=gTTS(text_hi.text,lang='hi')
ta_tts_hi.save('trans_hi.mp3')



Audio('trans_hi.mp3',autoplay=True)

text_fr=translator.translate(text_comb,src='ta',dest='fr')
print(text_fr.text)

ta_tts_fr=gTTS(text_fr.text,lang='fr')
ta_tts_fr.save('trans_fr.mp3')

Audio('trans_fr.mp3',autoplay=True)

