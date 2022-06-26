===============================================================
Relation Extraction for Russian. Narcy-based
===============================================================

This is a study project for creating a module for extracting relations from texts in Russian. This project is based on the Narcy project.
For original Narcy project, please refer to https://github.com/sztal/narcy.git

Installation
============

.. code-block:: bash

    pip install git+https://github.com/pdpetrova/ru-relation-extraction.git
    pip install transformers
    python -m spacy download ru_core_news_sm


Usage
=====

There are several original functions that convert documents
into data frames that describe all relations extracted from the text.
For detailed description, see original Narcy project.

The current module provides three original functions for Russian:

``doc_to_tokens_df``
    Dumps *spacy* ``Doc`` objects to *padas* data frames describing all
    tokens from a given document.

``doc_to_relations``
    Dumps *spacy* ``Doc`` objects to *pandas* data frames
    describing all relation or relation reducts (see following sections).

``doc_to_svos``
    Dumps *spacy* ``Doc`` objects to *pandas* data frames
    describing all subject-verb-object triplets.

And one function for Russian texts only:

``get_all_relations``
    Get all possible relations from texts. Gets only SVOs for English. 

Example
-------


.. code-block:: python

    import spacy
    from narcy import document_factory
    from narcy import doc_to_relations_df, doc_to_svos_df, doc_to_tokens_df, get_all_relations

    # Load NLP object with language model.
    nlp = spacy.load('ru_core_news_sm')
    # Create function for converting texts to documents
    make_doc = document_factory(nlp)


.. code-block:: python

    relations_df = doc_to_relations_df(doc)
    relation_reducts_df = doc_to_relations_df(doc, reduced=True)
    svos_df = doc_to_svos_df(doc)
    tokens_df = doc_to_tokens_df(doc)
    all_relations_df = get_all_relations(doc)






.. _Spacy: https://spacy.io/
