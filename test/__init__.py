"""Main module for tests."""
import os
import pandas as pd
import en_core_web_sm
from narcy.nlp.utils import Relation, document_factory
from narcy.processors import reduce_relations
from narcy.processors import doc_to_relations_df, doc_to_svos_df
from narcy.processors import doc_to_tokens_df

_dirpath = os.path.join(os.path.split(__file__)[0], 'data')

def get_docs():
    make_doc = document_factory(en_core_web_sm.load())
    documents = []
    for text in os.listdir(_dirpath):
        with open(os.path.join(_dirpath, text)) as stream:
            doc = make_doc(stream.read().strip())
        documents.append(doc)
    return documents

def _test_relations(doc, reduced):
    relations = doc._.relations
    if reduced:
        relations = reduce_relations(relations)
    for relation in relations:
        assert isinstance(relation, Relation)

def _test_doc_to_relations_df(doc, reduced):
    df = doc_to_relations_df(doc, reduced=reduced)
    assert isinstance(df, pd.DataFrame)
    assert df.shape != (0, 0)

def _test_doc_to_svos_df(doc):
    df = doc_to_svos_df(doc)
    assert isinstance(df, pd.DataFrame)
    assert df.shape != (0, 0)

def _test_doc_to_tokens_df(doc):
    df = doc_to_tokens_df(doc)
    assert isinstance(df, pd.DataFrame)
    assert df.shape != (0, 0)
