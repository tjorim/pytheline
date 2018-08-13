from pytheline import deLijn


def test_delijn_halte():

    delijn_instance = deLijn()
    response = delijn_instance.convert_location(51.1, 5.1)
    print(response)

    response = delijn_instance.haltes_doorkomendelijnen(51.1, 5.1)
    print(response)

    response = delijn_instance.haltes_indebuurt(51.1, 5.1, 300)
    print(response)

    response = delijn_instance.haltes_titel(51.1, 5.1)
    print(response)

    response = delijn_instance.haltes_vertrekken(401474, 8)
    print(response)
