import nltk
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader.chasen import ChasenCorpusReader

jeita = LazyCorpusLoader("jeita", ChasenCorpusReader, r".*chasen", encoding="utf-8")

print(type(jeita))

assert isinstance(jeita.tagged_words()[0][1], compat.string_types)
