import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name in players.keys():
        race_name = players[name]["race"]["name"]
        race_description = players[name]["race"]["description"]

        race_object, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        guild_object = None

        if players[name]["race"]["skills"]:
            for skill in players[name]["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_object
                )

        if players[name]["guild"] is not None:
            guild_name = players[name]["guild"]["name"]
            guild_description = players[name]["guild"]["description"]
            guild_object, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        Player.objects.create(
            nickname=name,
            email=players[name]["email"],
            bio=players[name]["bio"],
            race=race_object,
            guild=guild_object
        )


if __name__ == "__main__":
    main()
