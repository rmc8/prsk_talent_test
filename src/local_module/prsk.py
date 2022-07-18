from pprint import pprint
from typing import List, Tuple, Optional

import yaml


with open("./src/config.yml", mode="r", encoding="utf-8") as f:
    obj = yaml.safe_load(f)


def create_dict_of_char_rank(char_rank_dict):
    ret_dict: dict = {}
    for units in char_rank_dict.values():
        for k, v in units.items():
            ret_dict[k] = 0.050 if v >= 50 else v / 1000
    return ret_dict


class TALENT_CALC:
    CHARACTER_BONUS: dict = {
        k: sum(v) if type(v) is list else v
        for k, v in obj["bonus"]["area_item"]["character"].items()
    }
    UNIT_BONUS: dict = {k: sum(v) for k, v in obj["bonus"]["area_item"]["unit"].items()}
    TYPE_BONUS: dict = {k: sum(v) for k, v in obj["bonus"]["area_item"]["type"].items()}
    CHAR_RANK_BONUS: dict = create_dict_of_char_rank(obj["bonus"]["character_rank"])
    TRANSLATE_DICT: dict = {v: k for k, v in obj["translate"].items()}
    TITLE_BONUS: int = obj["bonus"]["title_bonus"]

    def __init__(self):
        self.characters_list: List[dict] = [
            {"character": None, "unit": None, "card_type": None, "talent": 0, "performance": 0 , "technic": 0, "stamina": 0, "skill": 0, },
            {"character": None, "unit": None, "card_type": None, "talent": 0, "performance": 0 , "technic": 0, "stamina": 0, "skill": 0, },
            {"character": None, "unit": None, "card_type": None, "talent": 0, "performance": 0 , "technic": 0, "stamina": 0, "skill": 0, },
            {"character": None, "unit": None, "card_type": None, "talent": 0, "performance": 0 , "technic": 0, "stamina": 0, "skill": 0, },
            {"character": None, "unit": None, "card_type": None, "talent": 0, "performance": 0 , "technic": 0, "stamina": 0, "skill": 0, },
        ]
        self.type_matched: bool = False
        self.unit_matched: bool = False
        self.area_item_bonus: int = 0
        self.character_rank_bonus: int = 0
        self.leader_skill: int = 0
        self.skill_total: int = 0
        self.skill_effect: float = 0

    def set_character(self, position: int , character_name: str, unit_name: str, card_type: str,
                      performance: int, technic: int, stamina: int, skill: Optional[int] = None,):
        oa_values: Tuple[int, int, int] = (performance, technic, stamina)
        self.characters_list[position - 1]["talent"] = sum(oa_values)
        character = {
            "character": character_name,
            "unit": unit_name,
            "card_type": card_type,
            "performance": performance,
            "technic": technic,
            "stamina": stamina,
            "skill": skill,
        }
        for key, val in character.items():
            self.characters_list[position - 1][key] = val

    def characters(self):
        print("=== Characters ===")
        pprint(self.characters_list)
        print()

    def _matched_switcher(self, item: str) -> bool:
        matched_check_set: set = {char[item] for char in self.characters_list}
        if len(matched_check_set) > 1:
            return False
        return True

    def _calc_area_item(self, character_name: str, unit: str, card_type: str,
                        talents: Tuple[int, int, int]) -> int:
        unit_key: str = self.TRANSLATE_DICT[unit]
        type_key : str = self.TRANSLATE_DICT[card_type]
        weight_dict: dict = {
            "character_bonus": self.CHARACTER_BONUS[character_name],
            "unit_bonus": self.UNIT_BONUS[unit_key],
            "type_bonus": self.TYPE_BONUS[type_key],
        }
        match_dict: dict = {
            "character_bonus": 1,
            "unit_bonus": 1 + self.unit_matched,
            "type_bonus": 1 + self.type_matched,
        }
        # adjustment = 0
        local = {0: [], 1: [], 2: []}
        for n, talent_value in enumerate(talents):
            for talent_cat, weight in weight_dict.items():
                talent = talent_value * weight
                local[n].append(talent * match_dict[talent_cat])
        self.area_item_bonus += sum([int(sum(val)) for val in local.values()])
        # print(character_name)
        # print(sum([int(sum(val)) for val in local.values()]))

    def _calc_character_rank(self, character_name: str, talents: Tuple[int, int, int]):
        weight: float = self.CHAR_RANK_BONUS[character_name]
        # print(sum([int(t * weight) for t in talents]))
        self.character_rank_bonus += sum([int(talent * weight) for talent in talents])

    def total_base_talent(self) -> int:
        return sum([character["talent"] for character in self.characters_list])

    def total_talent(self) -> int:
        return self.total_base_talent() \
            + self.area_item_bonus \
            + self.character_rank_bonus \
            + self.TITLE_BONUS

    def set_skill_effect(self):
        if [v for v in self.characters_list if v["skill"] is None]:
            return
        self.leader_skill = self.characters_list[0]["skill"]
        self.skill_total = sum([v["skill"] for v in self.characters_list])
        self.skill_effect = ((self.leader_skill + 100) + ((self.skill_total - self.leader_skill) / 5)) / 100

    def view_talent_details(self):
        status_dict = {
            "合計総合力": self.total_talent(),
            "総合力": self.total_base_talent(),
            "エリアアイテムボーナス": self.area_item_bonus,
            "キャラクターランクボーナス": self.character_rank_bonus,
            "称号ボーナス": self.TITLE_BONUS,
        }
        print()
        print("========== 総合力の計算結果 ===========")
        print()
        print(f"周回用：{self.total_talent()/10000:.1f}/{self.leader_skill}/{self.skill_total}({self.skill_effect})".rjust(33))
        print()
        for n, (key, value) in enumerate(status_dict.items()):
            item = key.rjust(14).replace(" ", "　")
            talent: str = f"{value:,}".rjust(7)
            print(f"{item}: {talent}")
            if not n:
                print("--------------------------------------")
        print()
        print("======================================")
        print()

    def calc(self):
        # Check to see if units and types match
        self.type_matched = self._matched_switcher("card_type")
        self.unit_matched = self._matched_switcher("unit")

        # Calculate the talent bonus for each character
        for character_dict in self.characters_list:
            talents: Tuple[int, int, int] = (character_dict["performance"], character_dict["technic"] , character_dict["stamina"])
            # Calc: Area item bonus
            self._calc_area_item(
                character_name=character_dict["character"],
                unit=character_dict["unit"],
                card_type=character_dict["card_type"],
                talents=talents,
            )
            # Calc: Character rank bonus
            self._calc_character_rank(
                character_name=character_dict["character"],
                talents=talents,
            )

        # Skill effect
        self.set_skill_effect()

        # Display calculation results
        self.view_talent_details()


if __name__ == "__main__":
    def fmt_print(name, data):
        print(f"=== {name} ===")
        pprint(data)
        print()

    CHARACTER_BONUS: dict = {
        k: sum(v) if type(v) is list else v
        for k, v in obj["bonus"]["area_item"]["character"].items()
    }
    UNIT_BONUS: dict = {k: sum(v) for k, v in obj["bonus"]["area_item"]["unit"].items()}
    TYPE_BONUS: dict = {k: sum(v) for k, v in obj["bonus"]["area_item"]["type"].items()}
    CHAR_RANK_BONUS: dict = create_dict_of_char_rank(obj["bonus"]["character_rank"])
    TRANSLATE_DICT: dict = {v: k for k, v in obj["translate"].items()}

    fmt_print("CHARACTER_BONUS", CHARACTER_BONUS)
    fmt_print("UNIT_BONUS", UNIT_BONUS)
    fmt_print("TYPE_BONUS", TYPE_BONUS)
    fmt_print("CHARACTER_RANK_BONUS", CHAR_RANK_BONUS)
    fmt_print("TRANSLATE", TRANSLATE_DICT)
