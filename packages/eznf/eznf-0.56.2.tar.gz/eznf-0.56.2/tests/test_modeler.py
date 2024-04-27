from eznf import modeler
from eznf import universal_existential_form

def test_variable_addition():
    Z = modeler.Modeler()
    Z.add_var("x", "x")
    assert Z.v("x") == 1


def test_qbf_basic_encoding():
    Z = modeler.Modeler()
    Z.add_existential_var("x")
    Z.add_universal_var("y")
    assert Z.v("y") == 2



