from pytheline import deLijn


def test_delijn_halte():

    delijn_instance = deLijn()
    response = delijn_instance.convert_location(51.2, 17, 2)
    print(response)
