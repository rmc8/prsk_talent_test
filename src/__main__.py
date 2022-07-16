from local_module.prsk import TALENT_CALC


def main():
    oc = TALENT_CALC()

    """
    # 1st
    oc.set_character(
        position=1,
        character_name="桐谷遥",
        unit_name="MORE MORE JUMP!",
        card_type="ミステリアス",
        performance=13138,
        technic=11988,
        stamina=12168,
        skill=130,
    )

    # 2nd
    oc.set_character(
        position=2,
        character_name="白石杏",
        unit_name="Vivid BAD SQUAD",
        card_type="ミステリアス",
        performance=12229,
        technic=11443,
        stamina=13620,
        skill=130,
    )

    # 3rd
    oc.set_character(
        position=3,
        character_name="東雲彰人",
        unit_name="Vivid BAD SQUAD",
        card_type="ミステリアス",
        performance=12379,
        technic=11957,
        stamina=12956,
        skill=105,
    )

    # 4th
    oc.set_character(
        position=4,
        character_name="小豆沢こはね",
        unit_name="Vivid BAD SQUAD",
        card_type="ミステリアス",
        performance=13379,
        technic=12138,
        stamina=11776,
        skill=130,
    )

    # 5th
    oc.set_character(
        position=5,
        character_name="青柳冬弥",
        unit_name="Vivid BAD SQUAD",
        card_type="ミステリアス",
        performance=13288,
        technic=11745,
        stamina=12257,
        skill=105,
    )
    """

    # 1st
    oc.set_character(
        position=1,
        character_name="MEIKO",
        unit_name="Vivid BAD SQUAD",
        card_type="ピュア",
        performance=13681,
        technic=11474,
        stamina=12138,
        skill=150,
    )

    # 2nd
    oc.set_character(
        position=2,
        character_name="初音ミク",
        unit_name="Vivid BAD SQUAD",
        card_type="ピュア",
        performance=13530,
        technic=12075,
        stamina=11685,
        skill=120,
    )

    # 3rd
    oc.set_character(
        position=3,
        character_name="白石杏",
        unit_name="Vivid BAD SQUAD",
        card_type="ピュア",
        performance=13256,
        technic=12257,
        stamina=11776,
        skill=130,
    )

    # 4th
    oc.set_character(
        position=4,
        character_name="小豆沢こはね",
        unit_name="Vivid BAD SQUAD",
        card_type="ピュア",
        performance=12018,
        technic=13102,
        stamina=12168,
        skill=130,
    )

    # 5th
    oc.set_character(
        position=5,
        character_name="青柳冬弥",
        unit_name="Vivid BAD SQUAD",
        card_type="ピュア",
        performance=13318,
        technic=12047,
        stamina=11932,
        skill=130,
    )

    # Characters
    oc.characters()

    # Calc
    oc.calc()


if __name__ == "__main__":
    main()
