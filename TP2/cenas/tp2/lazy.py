import nltk
from nltk.corpus.util import LazyCorpusLoader


 
jeita = LazyCorpusLoader(
        'jeita', ChasenCorpusReader, r'.*chasen', encoding='utf-8')
  #  print '/'.join( jeita.words()[22100:22140] )
 
 
   # print '\nEOS\n'.join(['\n'.join("%s/%s" % (w[0],w[1].split('\t')[2]) for w in sent)
    #                      for sent in jeita.tagged_sents()[2170:2173]])
