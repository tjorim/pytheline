from pytheline import deLijn


def test_delijn_halte():

    delijn_instance = deLijn()
    response = delijn_instance.convert_location(51.1, 5.1)
    print(response)

    response = delijn_instance.haltes_doorkomendelijnen(406472)
    print(response)

    response = delijn_instance.haltes_indebuurt(201220, 199130, 600)
    print(response)

    response = delijn_instance.haltes_titel(406472)
    print(response)

    response = delijn_instance.haltes_vertrekken(406472, 6)
    print(response)
