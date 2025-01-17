from bittranslate import Exams, XQuAD, PeerSum,  GermanQuAD
import pytest
from langdetect import detect

def test_peer_sum():
    peer_sum = PeerSum()
    result = peer_sum.sample_case("en")
    assert type(result) == str
    lang = detect(result)
    assert lang == "en"

    with pytest.raises(ValueError):
        result = peer_sum.sample_case("pl")

def test_german_quad():
    german_quad = GermanQuAD()
    result = german_quad.sample_case("de")
    lang = detect(result)
    assert lang == "de"
    assert type(result) == str
    with pytest.raises(ValueError):
        result = german_quad.sample_case("en")

def test_exams():
    exams = Exams()
    valid_langs= ["bg", "hu", "it", "pl", "pt", "tr", "vi"]
    for expect_lang in valid_langs:
        result = exams.sample_case(expect_lang)
        assert type(result) == str
        got_lang = detect(result)
        assert expect_lang == got_lang

    with pytest.raises(ValueError):
        result = exams.sample_case("en")

def test_xquad():
    xquad = XQuAD()
    valid_langs = ['ar', 'de', 'el', 'en', 'es', 'hi', 'ro', 'ru', 'th', 'tr', 'vi']

    for expect_lang in valid_langs:
        result = xquad.sample_case(expect_lang)
        assert type(result) == str
        got_lang = detect(result)
        assert expect_lang == got_lang
    with pytest.raises(ValueError):
        result = xquad.sample_case("pl")
