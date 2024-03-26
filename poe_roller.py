import dataclasses
import re
from typing import List, Tuple, Set

import ahkpy
import numpy as np
from collections import deque

import time

MIN_DELAY = 0.05
MAX_DELAY_VAR = 0.01
ALT_POS = (150, 345)
AUG_POS = (310, 415)
SCOUR_POS = (583, 678)
ALCH_POS = (650, 345)
CHAOS_POS = (730, 345)
VAAL_POS = (310, 580)
CHISEL_POS = (810, 250)
BLESS_POS = (225, 585)
JEWELER_POS = (160, 500)
FUSING_POS = (225, 500)
CHANCE_POS = (310, 345)
TRANSMUTE_POS = (70, 345)

MOUSE_MOVE_MAX_VAR = (19, 19)
TARGET_ITEM_POS = (420, 515)
MOUSE_SPEED = 1
INF = True

from enum import Enum, auto


class Orb(Enum):
    TRANSMUTE = auto()
    ALT = auto()
    ANNUL = auto()
    CHANCE = auto()
    EXALT = auto()
    REGAL = auto()
    ALCH = auto()
    AUG = auto()
    CHAOS = auto()
    VEILED_CHAOS = auto()
    DIVINE = auto()
    JEWELLER = auto()
    FUSING = auto()
    ARMOURER_SCRAP = auto()
    WHETSTONE = auto()
    CHISEL = auto()
    CHROMATIC = auto()
    SCOUR = auto()
    BLESSED = auto()
    VAAL = auto()
    CRUSADER_EXALT = auto()
    REDEEMER_EXALT = auto()
    WARLORD_EXALT = auto()
    HUNTER_EXALT = auto()
    HARBINGER = auto()
    HORIZON = auto()
    ENKINDLING = auto()
    INSTILLING = auto()
    BINDING = auto()
    ANCIENT = auto()
    SIMPLE_SEXTANT = auto()
    PRIME_SEXTANT = auto()
    AWAKENED_SEXTANT = auto()


# @ahkpy.hotkey("c")
def copy_paste():
    data = ahkpy.get_clipboard()
    print(data)


last_4_clicks = deque(maxlen=4)


@ahkpy.hotkey("RButton")
def save_rightclick_pos_and_send_rightclick():
    last_4_clicks.append(ahkpy.get_mouse_pos())
    ahkpy.mouse_press(button="right")
    ahkpy.mouse_release(button="right")


@ahkpy.hotkey("!x")
def get_xy():
    x = []
    y = []
    for click in last_4_clicks:
        x.append(click[0])
        y.append(click[1])
    print(x, y)
    print(np.average(x), np.average(y))
    print(np.std(x), np.std(y))


def use_orb(orb: Orb):
    POS = ()
    if orb == Orb.ALCH:
        POS = ALCH_POS
    if orb == Orb.AUG:
        POS = AUG_POS
    if orb == Orb.ALT:
        POS = ALT_POS
    if orb == Orb.CHISEL:
        POS = CHISEL_POS
    if orb == Orb.JEWELLER:
        POS = JEWELER_POS
    if orb == Orb.FUSING:
        POS = FUSING_POS
    if orb == Orb.CHAOS:
        POS = CHAOS_POS
    if orb == Orb.SCOUR:
        POS = SCOUR_POS
    if orb == Orb.VAAL:
        POS = VAAL_POS
    if orb == Orb.BLESSED:
        POS = BLESS_POS
    if orb == Orb.CHANCE:
        POS = CHANCE_POS
    if orb == Orb.TRANSMUTE:
        POS = TRANSMUTE_POS
    ahkpy.mouse_move(*POS + np.random.randint(10, size=2) / 10 * MOUSE_MOVE_MAX_VAR, relative_to="window",
                     speed=MOUSE_SPEED,
                     )
    ahkpy.mouse_press(button="right",
                      delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR
                      )
    ahkpy.sleep(MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_release(button="right",
                        )
    ahkpy.mouse_move(*TARGET_ITEM_POS + np.random.randint(10, size=2) / 10 * MOUSE_MOVE_MAX_VAR,
                     relative_to="window",
                     speed=MOUSE_SPEED,
                     )
    ahkpy.mouse_press(button="left",
                      delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR
                      )
    ahkpy.sleep(MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_release(button="left",
                        )


def alt_item():
    ahkpy.mouse_move(*ALT_POS + np.random.randint(10, size=2) / 10 * MOUSE_MOVE_MAX_VAR, relative_to="window",
                     speed=MOUSE_SPEED,
                     delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_press(button="right", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_release(button="right", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_move(*TARGET_ITEM_POS + np.random.randint(10, size=2) / 10 * MOUSE_MOVE_MAX_VAR, relative_to="window",
                     speed=MOUSE_SPEED,
                     delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_press(button="left", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_release(button="left", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)


def aug_item():
    ahkpy.mouse_move(*AUG_POS + np.random.randint(10, size=2) / 10 * MOUSE_MOVE_MAX_VAR, relative_to="window",
                     speed=MOUSE_SPEED,
                     delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_press(button="right", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_release(button="right", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_move(*TARGET_ITEM_POS + np.random.randint(10, size=2) / 10 * MOUSE_MOVE_MAX_VAR, relative_to="window",
                     speed=MOUSE_SPEED,
                     delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_press(button="left", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.mouse_release(button="left", delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)


def get_item_description():
    ahkpy.mouse_move(*TARGET_ITEM_POS, relative_to="window", speed=MOUSE_SPEED,
                    delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.sleep(0.05)
    ahkpy.send(keys="^!c", key_delay=MIN_DELAY + np.random.randint(100) / 100 * MAX_DELAY_VAR)
    ahkpy.sleep(0.05)
    return ahkpy.get_clipboard()


def check_prefix(item_description: str):
    return "prefix" in item_description


def check_suffix(item_description: str):
    return "suffix" in item_description


PAUSE = False


@ahkpy.hotkey("Esc")
def set_pause():
    global PAUSE
    PAUSE = True


@ahkpy.hotkey("!a")
def alch_scour():
    global PAUSE
    PAUSE = False
    old_description = ""
    mod_hit = False
    for i in range(100):
        if PAUSE:
            print("aborted")
            break
        if mod_hit:
            break
        print("alched")
        use_orb(Orb.SCOUR)
        # time.sleep(0.2)
        use_orb(Orb.ALCH)
        # time.sleep(0.2)
        description = get_item_description().lower()
        if old_description == description:
            print(old_description)
            print("old and new description was identical, breaking")
            break
        old_description = description
        # for t1_only_string in ["maraketh","templar","timeless"]: # glennach
        for t1_only_string in ["arrow"]:  # lira
            if t1_only_string.lower() in description:
                mod_hit = True
                break
            if t1_only_string.lower() in description and "tier: 1" in description:
                if description.count("of the hunt") >= 2:
                    print("win")
                    print(description)
                    mod_hit = True
                    break
        # for t2_and_t1_string in ["beyond"]: #glennach
        # for t2_and_t1_string in ["gambler"]: #lira
        #     if t2_and_t1_string.lower() in description and ("tier: 2" in description or "tier: 1" in description):
        #         print("win")
        #         print(description)
        #         break
        # for string in ["Archaeologist", "chayula","gambler","breachstone"]:
        if not mod_hit:
            print("boring", i)

    print(f"done {i}x")

@dataclasses.dataclass
class Mod:
    name: str
    tier: int

def get_mods() -> Tuple[List[Tuple[str,int]],List[Tuple[str,int]]]:
    description = get_item_description()
    prefixes = re.findall(r'Prefix Modifier "(.*)" \(Tier: (\d+)\)',description)
    suffixes = re.findall(r'Suffix Modifier "(.*)" \(Tier: (\d+)\)',description)
    #prefixes = re.findall(r'Prefix Modifier [^\}]* \}\n([^\r]*)(\r\n\{|\r\n-)', description, flags=re.DOTALL)
    #suffixes = re.findall(r'Suffix Modifier [^\}]* \}\n([^\r]*)(\r\n\{|\r\n-)', description, flags=re.DOTALL)
    # suffixes = [(re.findall(r'Suffix Modifier "(.*)"', description)[0], '0')]
    print(prefixes)
    #print(suffixes)
    return prefixes, suffixes
@ahkpy.hotkey("!1")
def roll_einhar_map():
    thresh = 100
    # chisel the map
    for i in range(4):
        use_orb(Orb.CHISEL)
    # while not above 100 quant:
    for i in range(20):  # at max use 20 bindings
        use_orb(Orb.ALCH)
        desc = get_item_description()
        quant = re.findall(r"Item Quantity: \+(\d+)",desc)
        if quant[0] > thresh:
            break
        use_orb(Orb.SCOUR)

    use_orb(Orb.VAAL)

@ahkpy.hotkey("!f")
def roll_flask():
    #required_suffix = set()
    #required_suffix = add_rolls(required_suffix, '(15-17)% increased Cast Speed during Effect', 17)
    #required_suffix = add_rolls(required_suffix, '((35-39)% less Duration Immunity to Bleeding and Corrupted Blood during Effect', 52)
    #required_suffix = add_rolls(required_suffix, '(12-14)% increased Movement Speed during Effect', 14)
    #required_suffix = add_rolls(required_suffix, '(42-45)% to Cold Resistance', 43)
    #required_suffix = {"of the Armadillo","of the Impala","of the Cheetah","of the Rainbow","of Draining","of Bloodletting","of the Dove","of the Horsefly","of Incision","of the Owl"}
    required_suffix = {}
    #required_prefix = {"Abecedarian's", "Dabbler's", "Alchemist's"}
    required_prefix = {"The Elder's", "The Shaper's"}
    roll_prefix_suffix(400, required_suffix ,required_prefix)

@ahkpy.hotkey("!h")
def roll_amulet():
    # required_suffix = {"of the Armadillo","of the Impala","of the Cheetah","of the Rainbow","of Draining","of Bloodletting","of the Dove","of the Horsefly","of Incision","of the Owl"}
    #required_suffix = {"of Destruction"}
    #required_prefix = {'(80-89) to maximum Life', '(90-99) to maximum Life', '(70-79) to maximum Life', '(60-69) to maximum Life', '(50-59) to maximum Life', '(40-49) to maximum Life', '(30-39) to maximum Life'}
    #required_prefix = {'Magnifier', 'Vast Power', 'Titanic Swings'}
    required_prefix = {}
    #required_prefix = {"Magister's"}
    # required_suffix = {"of Arcing"}
    # required_suffix = {"of Mastery"}
    # required_suffix = {"of Melting"}
    # required_prefix = {"Exalter's"}
    # required_suffix = {"of the Essence"}
    required_prefix = {"Powerful", "Glowing"}
    required_suffix = {"of the Prodigy", "of the Meteor"}
    # required_suffix = {"of the Meteor", "of the Bear"}
    #required_prefix = {"Dangerous", "Powerful"}
    #required_suffix = {"of the Bear", "of the Fox", "of the Prodigy", "of Mastery"}
    # required_prefix = {"Warlord's"}
    # required_suffix = {"of Potency"}
    # required_prefix = {"Piercing", "Vivid"}
    # required_suffix = {"of the Avalanche"}
    #required_suffix = {"of Eviction", "of Expulsion", "of the Falcon", "of the fox", "of the Comet", "of the Heavens", "of Exile", "of the Panther"}
    #required_suffix = {'+1 to Minimum Endurance Charges', '+2 to Minimum Endurance Charges'}
    #required_suffix = set()
    #required_suffix = add_rolls(required_suffix, '(46-48)% to Cold Resistance', 47)
    #required_suffix = add_rolls(required_suffix, '(36-41)% to Cold Resistance', 38)
    #equired_suffix = add_rolls(required_suffix, '(30-35)% to Cold Resistance', 33)
    #required_suffix = add_rolls(required_suffix, '(42-45)% to Cold Resistance', 43)
    """
    required_suffix = {r"Added Small Passive Skills also grant: 3% increased Attack and Cast Speed with Cold Skills", 
                       r"Added Small Passive Skills also grant: 2% increased Attack and Cast Speed with Cold Skills", 
                       r"Added Small Passive Skills also grant: 1% increased Attack and Cast Speed with Cold Skills", 
                       r"Added Small Passive Skills also grant: +4% to all Elemental Resistances",
                       r"Added Small Passive Skills also grant: +3% to all Elemental Resistances",
                       r"Added Small Passive Skills also grant: +2% to all Elemental Resistances"}
    required_prefix = {r"Added Small Passive Skills have 25% increased Effect",
                       r"Added Small Passive Skills have 35% increased Effect", 
                       r"Added Small Passive Skills also grant: 4% increased Damage", 
                       r"Added Small Passive Skills also grant: 3% increased Damage",
                       r"Added Small Passive Skills also grant: 2% increased Damage"}
    """
    #required_suffix = {"of Overflowing"}
    #required_prefix = {"Condensing", "Magnifying"}
    #required_suffix = {r'20(16-20)% chance to Avoid Elemental Ailments', r'(21-25)% chance to Avoid Elemental Ailments', r'(26-30)% chance to Avoid Elemental Ailments', r'(31-35)% chance to Avoid Elemental Ailments'}
    #required_suffix = {r'Added Small Passive Skills also grant: 1% increased Area of Effect', r'Added Small Passive Skills also grant: 2% increased Area of Effect', r'Added Small Passive Skills also grant: 3% increased Area of Effect'}
    roll_prefix_suffix(2500,required_suffix,required_prefix)


@ahkpy.hotkey("!j")
def chance_scour():
    global PAUSE
    PAUSE = False
    while True:
        if PAUSE:
            print("aborted")
            break
        use_orb(Orb.CHANCE)
        time.sleep(0.05)
        use_orb(Orb.SCOUR)
        time.sleep(0.05)

@ahkpy.hotkey("!w")
def roll_whisper_cloak():

    required_suffix  = {"of Planning","of Choreography"}
    required_prefix = {}
    roll_prefix_suffix(300,required_suffix,required_prefix)

def add_rolls(required_mods: Set[str], mod: str, min_roll: int) -> Set[str]:
    max_roll = int(mod.split('-')[1].split(')')[0])
    for i in range(min_roll, max_roll + 1):
        required_mods.add(f"{i}{mod}")
    return required_mods


DESC_WAIT_TIME = 0.1
def roll_prefix_suffix(max_rolls:int, required_suffix, required_prefix):
    """
    basic idea: when a required prefix/suffix isnt there -> no need to aug
    :return:
    """
    global PAUSE
    PAUSE = False
    global DESC_WAIT_TIME
    old_prefixes, old_suffixes = {}, {}
    prefixes, suffixes = {}, {}
    mod_hit = False
    for i in range(max_rolls):
        if DESC_WAIT_TIME > 0.01:

            DESC_WAIT_TIME -= 0.01
            print(f"decreasing DESC_WAIT_TIME to {DESC_WAIT_TIME}")
        if PAUSE:
            print("aborted")
            break
        if mod_hit:
            break
        print("alted...",end="")
        alt_item()
        time.sleep(DESC_WAIT_TIME)
        prefixes, suffixes = get_mods()
        if prefixes == old_prefixes and suffixes == old_suffixes:
            print("old and new description was identical, pausing")
            time.sleep(0.1)
            prefixes, suffixes = get_mods()
            if not (prefixes == old_prefixes and suffixes == old_suffixes):
                # item description was actually outdated,
                print("item desc was actually outdated, resetting DESC_WAIT_TIME")
                DESC_WAIT_TIME = 0.1
                pass
            # mods were identical
        old_prefixes,old_suffixes = prefixes,suffixes
        has_suffix = len(suffixes)
        has_prefix = len(prefixes)

        # if prefix on item, check if any required pref available, else skip to alting in next round
        if has_prefix:
            if not has_req_prefix(prefixes,required_prefix):
                print("bad prefix")
                continue
        # if suffix on item, check if any required suffix available, else skip this round
        if has_suffix:
            if not has_req_suffix(suffixes,required_suffix):
                print("bad suffix")
                continue

        # if still here, at least prefix or suffix is desired
        # now check if only a pref/suffix is here, then add it via aug then proceed
        if not has_suffix or not has_prefix:
            aug_item()
            print("auged...",end="")
            time.sleep(DESC_WAIT_TIME)
            prefixes, suffixes = get_mods()
            if not (len(prefixes) and len(suffixes)):
                # either failed to add mod, or didnt grab desc correctly
                time.sleep(0.1)
                prefixes, suffixes = get_mods()
                if not (len(prefixes) and len(suffixes)):
                    print("failed to aug, breaking")
                    break

                # now grabbed desc properly
                DESC_WAIT_TIME = 0.1

            old_prefixes,old_suffixes = prefixes,suffixes

            #if pref was added -> check prefixes
            if not has_prefix:
                if not has_req_prefix(prefixes,required_prefix):
                    print("bad prefix")
                    continue
            #if suff was added -> check suffixes
            if not has_suffix:
                if not has_req_suffix(suffixes,required_suffix):
                    print("bad suffix")
                    continue
        # now item has full pref/suffix, and wasnt skipped so far -> desired outcome
        print("hit")
        mod_hit = True

def has_req_prefix(prefixes, required_prefixes):
    if len(required_prefixes) == 0:
        return True
    has = False
    for r_pref in required_prefixes:
        for pref in prefixes:
            if r_pref in pref[0]:
                has = True
    return has

def has_req_suffix(suffixes,required_suffixes):
    if len(required_suffixes) == 0:
        return True
    has = False
    for r_suff in required_suffixes:
        for suff in suffixes:
            if r_suff in suff[0]:
                has = True
    return has


@ahkpy.hotkey("!b")
def reroll_prefix():
    global PAUSE
    PAUSE = False
    interesting_descriptions = []
    old_description = ""
    mod_hit = False
    for i in range(50):
        if PAUSE:
            print("aborted")
            break
        if mod_hit:
            break
        print("alted")
        alt_item()
        time.sleep(0.1)
        description = get_item_description().lower()
        # print(description)
        if "Prefix".lower() not in description:
            print("using aug, as no prefix")
            aug_item()
            time.sleep(0.1)
            description = get_item_description().lower()
        else:
            print("has prefix")
        if old_description == description:
            print(old_description)
            print("old and new description was identical, breaking")
            break
        old_description = description
        # for t1_only_string in ["maraketh","templar","timeless"]: # glennach
        # for t1_only_string in ["chayula", "Archaeologist", "breachstone"]:  # lira
        # for t1_only_string in ["Charges when you are Hit by an Enemy"]:  # lira
        # for t1_only_string in ["1 to Level of all Jobs for Heists","1 to Deception Level for Heists"]:  # lira
        for t1_only_string in ["grace"]:  # lira
            # if t1_only_string.lower() in description and "tier: 1" in description:
            if t1_only_string.lower() in description:
                print("win")
                print(description)
                mod_hit = True
                break
        # for t2_and_t1_string in ["beyond"]: #glennach
        # for t2_and_t1_string in ["gambler"]:  # lira
        #     if t2_and_t1_string.lower() in description and ("tier: 2" in description or "tier: 1" in description):
        #         print("win")
        #         print(description)
        #         mod_hit = True
        #         break
        # for string in ["Archaeologist", "chayula","gambler","breachstone"]:
        if not mod_hit:
            print("boring", i)

    print(f"done {i}x")
