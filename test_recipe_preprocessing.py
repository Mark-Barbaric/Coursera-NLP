
import recipe_preprocessing


def test_preprocess_word():
    w1 = "One"
    assert recipe_preprocessing.preprocess_word(w1) == "1"
    w2 = "red"    
    assert recipe_preprocessing.preprocess_word(w2) == "red"
    w3 = "¼-½"
    assert recipe_preprocessing.preprocess_word(w3) == "0.25"
    w3 = "1/4"
    assert recipe_preprocessing.preprocess_word(w3) == "0.25"
