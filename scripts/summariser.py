import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter

def extract_keywords(text, num_keywords=5, min_length=4):
    nlp=spacy.load('en_core_web_sm')
    doc = nlp(text)
    keywords = []
    pos_tag = ['PROPN', 'NOUN', 'ADJ']
    for token in doc:
        if len(token.text) >= min_length and token.text not in nlp.Defaults.stop_words and not token.is_punct and not token.is_space and token.pos_ in pos_tag:
            keywords.append(token.text)
    return Counter(keywords).most_common(num_keywords)

def summarise(files):
  stopwords = list(STOP_WORDS)
  nlp=spacy.load('en_core_web_sm')
  file=open(files+".txt","r")
  texts=file.read()
  doc= nlp(text)
  mytokens = [token.text for token in doc]
  texts=texts.split('\n')
  ini=0
  for fin in range(0,len(texts),50):
      text=texts[ini,fin]
      word_frequencies = {}
      for word in doc:
        if word.text not in stopwords:
          if word.text not in word_frequencies.keys():
            word_frequencies[word.text] = 1
          else:
            word_frequencies[word.text] += 1
      maximum_frequency = max(word_frequencies.values())
      for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
      sentence_list = [ sentence for sentence in doc.sents ]
      sentence_scores = {}
      for sent in sentence_list:
        for word in sent:
          if word.text.lower() in word_frequencies.keys():
            if len(sent.text.split(' ')) < 30:
                                  if sent not in sentence_scores.keys():
                                      sentence_scores[sent] = word_frequencies[word.text.lower()]
                                  else:
                                      sentence_scores[sent] += word_frequencies[word.text.lower()]
      file.close()
      Threshold =0
      count=0
      total=0
      for i in sentence_scores:
          total+=sentence_scores[i]
          count+=1

      Threshold=0.1
      print (Threshold)
      keywords=extract_keywords(text,10)
      final=open(files+"1.txt","w+")
      for i in sentence_scores:
          if(sentence_scores[i] > Threshold):
              final.write(str(i))
              print("done")
      final.write("\n")
      for i in keywords:
          final.write(i[0]+" ")
      final.close()
      ini=fin
if __name__=="__main__":
    summarise("eng1")