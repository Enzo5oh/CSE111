from madlib import get_determiner, get_noun, get_verb, get_preposition, get_indirect_object, get_direct_object
import pytest

def test_get_determiner():
    singular_determiners = ["the", "a"]
    for i in range(2):
        word = get_determiner(1)
        assert word in singular_determiners

    plural_determiners = ["many", "some"]
    for i in range(2):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    nouns = ['I','vacation','job','Book or Mormon', 'butterfly','dog','homework','home''people','years','days','things','you','we']
    for i in range(2):
        word = get_noun()
        assert word in nouns

def test_get_verb_0():
    verb_0 = ['am','was','will be','have','had','will have','see','saw','will see','know','knew','will know','want','wanted','will want']
    for i in range(2):
        word = get_verb(0)
        assert word in verb_0

def test_get_verb_1():
    verb_1 = ['is','was','will be','has','had','will have','sees','saw','will see','knows','knew','will know','wants','wanted','will want']
    for i in range(2):
        word = get_verb(1)
        assert word in verb_1
 
def test_get_verb_2():
    verb_2 = ['are','were','will be','have','had','will have','see','saw','will see','know','knew','will know','want','wanted','will want']
    for i in range(2):
        word = get_verb(2)
        assert word in verb_2

def test_get_preposition():
    preposition = ["above", "across", "after", "around", "at", "before", "below", "beyond", "by", "except", "for","from", "in", "into", "near","off", "on", "onto", "over", "under", "with", "without"]
    for i in range(2):
        word = get_preposition()
        assert word in preposition

def test_get_indirect_object():
    ind_object = ['the raisins','the landscapes','the sea','Aj','him','the policy','the librarian','traveling','cats']
    for i in range(2):
        word = get_indirect_object()
        assert word in ind_object

def test_get_direct_object():
    d_object = ['it','them','him','her','you']
    for i in range(2):
        word = get_direct_object()
        assert word in d_object


pytest.main(["-v", "--tb=line", "-rN", "prove_assignment6.py"])
