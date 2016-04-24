"""
Test the module `cheeseshop`.
"""

import pytest
import numpy as np
import cheeseshop

def test_basicanswer():
    "Teste la fonction `basicanswer`."
    assert cheeseshop.basicanswer() == "No."
    assert cheeseshop.basicanswer("Cheddar?") == "No."

def test_elaborateanswer():
    "Teste la fonction `elaborateanswer`."
    assert cheeseshop.elaborateanswer("Cheddar?") == "No."
    assert cheeseshop.elaborateanswer("Cheddar.") == "<Nods.>"

def test_stochasticanswer():
    "Teste la fonction `stochasticanswer`."
    np.random.seed(12)
    answers = ["No.", "Normally, sir, yes. Today the van broke down.",
               "The cat's eaten it."]
    expected0 = "The cat's eaten it."
    assert cheeseshop.stochasticanswer("Cheddar?", answers=answers) == expected0
    expected1 = "Normally, sir, yes. Today the van broke down."
    assert cheeseshop.stochasticanswer("Cheddar?", answers=answers) == expected1
    expected2 = "Normally, sir, yes. Today the van broke down."
    assert cheeseshop.stochasticanswer("Cheddar?", answers=answers) == expected2

def test_dialog():
    "Teste la fonction `dialog`."
    cheeses = ['%s?' % x for x in cheeseshop.cheesesdata.cheese.iloc[:2]]
    text = cheeseshop.dialog(cheeses, cheeseshop.basicanswer)
    expected = '\n'.join(["Customer: Red Leicester?", "Owner: No.",
                          "Customer: Tilsit?", "Owner: No.",
                          "Customer: <Kill the owner.>"])
    assert text == expected
