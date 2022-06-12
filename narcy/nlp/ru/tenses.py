"""RUSSIAN: Tense detectors and related utilities."""
# pylint: disable=E0611
from ..tenses import PRESENT, PAST, FUTURE, MODAL, NORMAL


_TAGS_PAST = ('VBD', 'VBN')

#_WORDS_HAVE = ('have', 'has', 'had')
#_WORDS_PAST = ('did', 'was', 'were')
#_WORDS_FUTURE = ('will', 'shall')
#_WORDS_MODAL = (
    #'should', 'would', 'may', 'might', 'can', 'could',
    #'must', 'ought', 'need', 'needs', 'want', 'wants'
#)
_WORDS_FUTURE = ("буду", "будешь", "будет", "будем", "будете", "будут")

def detect_tense(verb):
    """Detect main tense of a compound verb.

    Parameters
    ----------
    verb : spacy.tokens.Span
        Compound verb.
    """
    tense = PRESENT
    mode = NORMAL
    if not verb:
        return tense, mode
    first = verb[0]
    first_text = first.text.lower()
    # Check tense
    try:
        second = first.nbor(1)
    except IndexError:
        second = None
    is_second_to = second
    first_text = first.text.lower()
    if first_text in _WORDS_FUTURE:
        tense = FUTURE
    elif first.morph.get('Tense')[0] == 'Pres':
        tense = PRESENT
    elif first.morph.get('Tense')[0] == 'Fut':
        tense = FUTURE
    elif first.morph.get('Tense')[0] == 'Past':
        tense = PAST
    return tense, mode
