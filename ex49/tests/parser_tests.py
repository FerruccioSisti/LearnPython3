#Tester file for the parser
from nose.tools import *
from ex49 import parser

def test_instantiate():
    x = parser.Sentence(("noun", "bear"), ("verb", "eat"), ("noun", "honey"))
    assert_equal(x.subject, "bear")
    assert_equal(x.verb, "eat")
    assert_equal(x.object, "honey")

def test_peek():
    x = parser.peek([("noun", "bear")])
    assert_equal(x, "noun")

def test_match():
    x = parser.match([("noun", "bear")], "noun")
    assert_equal(x, ("noun", "bear"))

def test_bad_match():
    x = parser.match([("noun", "bear")], "verb")
    assert_equal(x, None)

def test_skip():
    x = parser.skip([("stop", "the"), ("noun", "bear")], 'stop')
    #Should return none because the thing at index 0
    #Won't match stop
    assert_equal(x, None)

def test_parse_verb():
    x = parser.parse_verb([("verb", "eat")])
    assert_equal(x, ("verb", "eat"))

def test_parse_notverb():
    assert_raises(parser.ParserError, parser.parse_verb, [("noun", "bear")])

def test_parse_object():
    x = parser.parse_object([("noun", "bear")])
    assert_equal(x, ("noun", "bear"))

    y = parser.parse_object([("direction", "north")])
    assert_equal(y, ("direction", "north"))

def test_parse_notanobject():
    assert_raises(parser.ParserError, parser.parse_object, [("verb", "eat")])

def test_parse_subject():
    x = parser.parse_subject([("noun", "bear")])
    assert_equal(x, ("noun", "bear"))

    y = parser.parse_subject([("verb", "eat")])
    assert_equal(y, ("noun", "player"))

def test_parse_notsubject():
    assert_raises(parser.ParserError, parser.parse_subject, [("direction", "north")])
    
def test_parse_sentence():
    word_list = [("noun", "bear"), ("stop", "the"), ("verb", "eat"), ("noun", "honey")]
    subj = parser.parse_subject(word_list)
    verb = parser.parse_verb(word_list)
    obj = parser.parse_object(word_list)

    x = parser.Sentence(subj, verb, obj)
    y = parser.Sentence(("noun", "bear"), ("verb", "eat"), ("noun", "honey"))

    assert_equal(x.subject, y.subject)
    assert_equal(x.object, y.object)
    assert_equal(x.verb, y.verb)
