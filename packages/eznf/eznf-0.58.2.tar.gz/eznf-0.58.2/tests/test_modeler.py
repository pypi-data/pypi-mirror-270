from src.eznf.modeler import Modeler


def test_variable_addition():
    Z = Modeler()
    Z.add_var("x", "x")
    assert Z.v("x") == 1


def test_qbf_basic_encoding():
    Z = Modeler()
    Z.add_existential_var("x")
    Z.add_universal_var("y")
    assert Z.v("y") == 2
