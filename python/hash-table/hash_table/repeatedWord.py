from hash_table.hash_table import HashTable


def repeated_word(str_):
  if str_ == '' or type(str_) != str:
    raise ValueError('please enter a valid phrase')
  words = ' '.join(str_.split(','))
  splitted = words.split(' ')

  table = HashTable()
  for word in splitted:
    if table.contains(word.lower()):
      return word
    table.add(word.lower(),word.lower())



if __name__=='__main__':
  print(repeated_word('i am anas i am anas'))
  print(repeated_word(''))