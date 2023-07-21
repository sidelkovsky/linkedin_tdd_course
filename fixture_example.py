import pytest


@pytest.fixture()
# @pytest.fixture(autouse=True)
def setup():
    print("\nSetup")
    yield
    print("Teardown!")


@pytest.fixture()
def setup3():
    print("\nSetup 3!")
    yield
    print("\nTeardown 3!")


@pytest.fixture()
def setup4(request):
    print("\nSetup 4!")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup):
    print("Executing test1!")
    assert True


@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2!")
    assert True


def test3(setup3):
    print("Executing test 3!")
    assert True


def test4(setup4):
    print("Executing test 4!")
    assert True
