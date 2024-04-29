import re
import mwparserfromhell as mw

from yew.utils.api import fetch_wikicode

regex = re.compile("[^a-zA-Z0-9 ]")


def parse_npc(wikicode: str):
    npc = {}
    infobox = ""

    templates = mw.parse(wikicode).filter_templates()
    print(templates)
    for template in templates:
        if "Infobox" in template.name:
            infobox = template

    print(infobox)
    npc["name"] = regex.sub("", infobox.get("name").value.strip())
    npc["members"] = True if infobox.get("members").value.strip() == "Yes" else False
    npc["race"] = regex.sub("", infobox.get("race").value.strip())
    npc["examine"] = regex.sub("", infobox.get("examine").value.strip())
    npc["id"] = regex.sub("", infobox.get("id").value.strip())
    npc["gender"] = regex.sub("", infobox.get("gender").value.strip())
    npc["location"] = regex.sub("", infobox.get("location").value.strip())
    print(npc)


wikicode = fetch_wikicode("Zanik")
parse_npc(wikicode)
