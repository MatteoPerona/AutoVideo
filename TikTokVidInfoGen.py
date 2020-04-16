import datetime
from random import randint

today = datetime.datetime.today()
monthYear = today.strftime("%B %Y")

def title(tag):
    initial = 'TikToks That Make Me '
    subsequent = ['Internally Combust', 'Bang my Head on the Wall', "Question God's Existence", 'Do Homework Really Fast', "Glad I'm Alive", 'Quite Flustered', 'A Better Gamer']
    final = ' | Top '+tag+' TikToks Compilation of '+monthYear+'!'
    return initial + subsequent[randint(0,len(subsequent)-1)] + final

def description(tag, email):
    descript = 'Watch the Top '+tag+' TikToks Right Here!'
    promo = '\nGet the best and cheapest LEDs: https://icystarleds.com/?ref=2n3zrfpffm9'
    plug = '\nGo follow all the creators in the video on TikTok, and LiKe+suB to my channel if you love your mom (no like + no sub = no love mom) ¯\_(ツ)_/¯'
    disclaimer = '\n\nIf your TikTok is in this compilation and you want it to be removed or have business inquiries, please email: '+email+' \n\nCopyright Disclaimer: Under Section 107 of the Copyright Act 1976 this video is protected under fair use.'
    return descript+promo+plug+disclaimer
    