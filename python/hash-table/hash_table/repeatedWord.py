from hash_table import HashTable
import re

def repeated_word(str_):
  if str_ == '' or type(str_) != str:
    raise ValueError('please enter a valid phrase')
  words = ' '.join(str_.split(','))
  splitted = words.split(' ')
  table = HashTable()
  for word in splitted:
    if table.contains(word.lower()) and re.match('[a-z]', word.lower()):
      return word
    table.add(word.lower(),word.lower())



if __name__=='__main__':
  print(repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'))
