from .nlp import spacy_ext
from .nlp.utils import document_factory, get_compound_verb, get_compound_noun, detect_tense
from .processors import doc_to_relations_df, doc_to_svos_df, doc_to_tokens_df, get_all_relations

__author__ = 'Szymon Talaga'
__email__ = 'stalaga@protonmail.com'
__version__ = '0.0.0'
