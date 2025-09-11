import sys
def test_python_version_print():
    v = sys.version
    print("Running on Python:",v)
    assert sys.version_info.major == 3
