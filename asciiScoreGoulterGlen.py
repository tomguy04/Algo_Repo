#!/bin/python
import math
import os
import random
import re
import sys
import json

def find_common_ascii_score(data):
  """
  TODO: Fill in this function
  NOTE: To find the ASCII value, use n = ord(character)
  Finds the common ASCII score across collections of strings
  :param data JSON object with collections of strings
  :return: Single score across all collections, or if none exists -1
  """
#   print data
  sum = 0
  str = ''
  h={}
  arr=[]
  class myDict():
      word = ''
      score = 0
      key=''
  keyArr=[]
  for key in data:
    # print key
    str = data.get(key)
    for word in str:
        for ch in word:
            n = ord(ch)
            sum+=n
        # print word, 'sum is', sum
        c1 = myDict()
        c1.score = sum
        c1.word = word
        c1.key = key
        print c1.word, c1.score
        if c1.score not in h:
            # print c1.score, c1.word, 'not found'
            h[c1.score]=[]
            h[c1.score].append(c1)
        else:
            print c1.score, c1.word, 'found'
            h[c1.score].append(c1)
            for obj in h[c1.score]:
                if obj.key != c1.key :
                    return c1.score
        sum = 0
  return -1
       

thisDict={ "MyStringArray" : ["one1","Glen Goulter"],  "MyStringArray2" : ["one", "Glen"] }
thisDict2={"pixar":["BuzzLightyear","Dash","Dory","EdnaMode","Elastigirl","Frozone","Jack-JackParr","JamesP.Sullivan","Mr.PotatoHead","Nemo","Marlin","MikeWazowski","Mr.Incredible","RandallBoggs","Syndrome","VioletParr","Woody"],
"starwars":["AnakinSkywalker","BB-8","Chewbacca","DarthVader","Finn","GalenErso","HanSolo","JynErso","KyloRen","LeiaOrgana","LukeSkywalker","LyraErso","PoeDameron","Rey","R2-D2","Snoke","Yoda"],
"princesses":["Ariel","Belle","Cinderella","Esmeralda","Giselle","Moana","Mulan","Pocahontas","PrincessAnna","PrincessAurora","PrincessElsa","PrincessJasmine","PrincessMerida","Rapunzel","SleepingBeauty","SnowWhite","Tiana"]}

print find_common_ascii_score(thisDict2)
