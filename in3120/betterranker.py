# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long

import math
from dataclasses import dataclass
from .ranker import Ranker
from .corpus import Corpus
from .posting import Posting
from .invertedindex import InvertedIndex


class BetterRanker(Ranker):
    """
    A ranker that does traditional TF-IDF ranking, possibly combining it with
    a static document score (if present). Basically does a weighted sum of the
    two factors to produce net-score(q, d):

        net-score(q, d) = c₁ * static-score(d) + c₂ * dynamic-score(q, d)

    Here, static-score(d) is what the textbook denotes g(d), and dynamic-score(q, d)
    is given by Equation 6.9 in the textbook with an additional query multiplicity
    factor thrown in for good measure. See Section 6.2.2 and Section 7.1.4 in
    https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf for details.
    """

    @dataclass
    class Options:
        """
        Configuration options for the ranker.
        """
        static_field: str = "static_quality_score"  # The named document field that holds g(d).
        static_default: float = 0.0                 # The default g(d) value, if absent.
        static_weight: float = 1.0                  # The constant c₁ above.
        dynamic_weight: float = 1.0                 # The constant c₂ above.

    def __init__(self, corpus: Corpus, inverted_index: InvertedIndex, options: Options | None = None):
        self._score = 0.0
        self._document_id: int | None = None
        self._corpus = corpus
        self._inverted_index = inverted_index
        self._options = options or self.Options()

    def reset(self, document_id: int) -> None:
        # set new self._document_id
        self._document_id = document_id

        opt = self._options
        document = self._corpus[self._document_id]
        #update the score from document with the fields in self_optiopns:
        self._score = document.get_field(opt.static_field, opt.static_default) * opt.static_weight
        
        #raise NotImplementedError("You need to implement this as part of the obligatory assignment.")

    def update(self, term: str, multiplicity: int, posting: Posting) -> None:
        assert self._document_id == posting.document_id

        N = len(self._corpus)
        dft = len(list(self._inverted_index[term])) if len(list(self._inverted_index[term])) > 0 else 0
        IDF = math.log(N / dft)
        
        opt = self._options
        document = self._corpus[self._document_id]

        static_score = document.get_field(opt.static_field, opt.static_default)
        dynamic_score = IDF * multiplicity * posting.term_frequency

        self._score = (opt.static_weight * static_score) + (opt.dynamic_weight * dynamic_score)

        #raise NotImplementedError("You need to implement this as part of the obligatory assignment.")

    def evaluate(self) -> float:
        return self._score
    
        #raise NotImplementedError("You need to implement this as part of the obligatory assignment.")