===============================================================
Relation Extraction for Russian. Narcy-based
===============================================================

This is a study project to create a module for extracting relations from texts in Russian. This project is based on the Narcy project.
For original Narcy project, please refer to https://github.com/sztal/narcy.git

Installation
============

.. code-block:: bash

    pip install git+https://github.com/pdpetrova/ru-relation-extraction.git
    python -m spacy download ru_core_news_sm


Usage
=====

Currently there are two workhorse functions that converts documents
into tidy data frames that describe all relations extracted from the text.

``doc_to_tokens_df``
    Dumps *spacy* ``Doc`` objects to *padas* data frames describing all
    tokens from a given document.

``doc_to_relations``
    Dumps *spacy* ``Doc`` objects to *pandas* data frames
    describing all relation or relation reducts (see following sections).

``doc_to_svos``
    Dumps *spacy* ``Doc`` objects to *pandas* data frames
    describing all subject-verb-object triplets.

``get_all_relations``
    Get all possible relations from texts. Available for Russian only. Gets only SVOs for English. 

Example
-------

First, load *Spacy* and prepare function for converting texts to parsed documents
(at the same time *Spacy* is extended with *Narcy* extension attributes).
Also import other functions that will be used later.

At this stage it also required to load a language models and setup a function
for converting texts to documents.
Better models - like ``'en_core_web_md'`` - may be necessary for proper word vectors.

.. code-block:: python

    import spacy
    from narcy import document_factory
    from narcy import doc_to_relations_df, doc_to_svos_df, doc_to_tokens_df

    # Load NLP object with language model.
    nlp = spacy.load('en_core_web_sm')
    # Create function for converting texts to documents
    make_doc = document_factory(nlp)

Next, load text of some documen.


.. code-block:: python

    text = load_text()
    # Make document object with automatic normalization
    doc = make_doc(text)

Now, tidy data may be extracted from the document.

.. code-block:: python

    relations_df = doc_to_relations_df(doc)
    relation_reducts_df = doc_to_relations_df(doc, reduced=True)
    svos_df = doc_to_svos_df(doc)
    tokens_df = doc_to_tokens_df(doc)

Voila!





.. _Spacy: https://spacy.io/
