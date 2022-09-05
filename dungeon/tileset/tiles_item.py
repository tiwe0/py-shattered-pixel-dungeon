import pygame

from dungeon.dsprite import DSpriteSheetReader

tiles_item_path = "assets/sprites/items.png"
tiles_item_reader = DSpriteSheetReader(tiles_item_path, frame_width=16, frame_height=16)


def cr(c, r):
    return 16 * (c - 1) + (r - 1)


class TilesItems:
    size_dict = {}

    PLACEHOLDERS = cr(1, 1)
    SOMETHING = PLACEHOLDERS + 0
    WEAPON_HOLDER = PLACEHOLDERS + 1
    ARMOR_HOLDER = PLACEHOLDERS + 2
    MISSILE_HOLDER = PLACEHOLDERS + 3
    WAND_HOLDER = PLACEHOLDERS + 4
    RING_HOLDER = PLACEHOLDERS + 5
    ARTIFACT_HOLDER = PLACEHOLDERS + 6
    FOOD_HOLDER = PLACEHOLDERS + 7
    BOMB_HOLDER = PLACEHOLDERS + 8
    POTION_HOLDER = PLACEHOLDERS + 9
    SCROLL_HOLDER = PLACEHOLDERS + 11
    SEED_HOLDER = PLACEHOLDERS + 10
    STONE_HOLDER = PLACEHOLDERS + 12
    CATA_HOLDER = PLACEHOLDERS + 13
    ELIXIR_HOLDER = PLACEHOLDERS + 14
    SPELL_HOLDER = PLACEHOLDERS + 15

    size_dict[SOMETHING] = (8, 13)
    size_dict[WEAPON_HOLDER] = (14, 14)
    size_dict[ARMOR_HOLDER] = (14, 12)
    size_dict[MISSILE_HOLDER] = (15, 15)
    size_dict[WAND_HOLDER] = (14, 14)
    size_dict[RING_HOLDER] = (8, 10)
    size_dict[ARTIFACT_HOLDER] = (15, 15)
    size_dict[FOOD_HOLDER] = (15, 11)
    size_dict[BOMB_HOLDER] = (10, 13)
    size_dict[POTION_HOLDER] = (12, 14)
    size_dict[SEED_HOLDER] = (10, 10)
    size_dict[SCROLL_HOLDER] = (15, 14)
    size_dict[STONE_HOLDER] = (14, 12)
    size_dict[CATA_HOLDER] = (6, 15)
    size_dict[ELIXIR_HOLDER] = (12, 14)
    size_dict[SPELL_HOLDER] = (8, 16)

    UNCOLLECTIBLE = cr(2, 1)
    GOLD = UNCOLLECTIBLE + 0
    ENERGY = UNCOLLECTIBLE + 1

    DEWDROP = UNCOLLECTIBLE + 3
    PETAL = UNCOLLECTIBLE + 4
    SANDBAG = UNCOLLECTIBLE + 5
    SPIRIT_ARROW = UNCOLLECTIBLE + 6

    GUIDE_PAGE = UNCOLLECTIBLE + 8
    ALCH_PAGE = UNCOLLECTIBLE + 9

    TENGU_BOMB = UNCOLLECTIBLE + 11
    TENGU_SHOCKER = UNCOLLECTIBLE + 12

    size_dict[GOLD] = (15, 13)
    size_dict[ENERGY] = (16, 16)

    size_dict[DEWDROP] = (10, 10)
    size_dict[PETAL] = (8, 8)
    size_dict[SANDBAG] = (10, 10)
    size_dict[SPIRIT_ARROW] = (11, 11)

    size_dict[GUIDE_PAGE] = (10, 11)
    size_dict[ALCH_PAGE] = (10, 11)

    size_dict[TENGU_BOMB] = (10, 10)
    size_dict[TENGU_SHOCKER] = (10, 10)

    # 容器
    CONTAINERS = cr(3, 1)
    BONES = CONTAINERS + 0
    REMAINS = CONTAINERS + 1
    TOMB = CONTAINERS + 2
    GRAVE = CONTAINERS + 3
    CHEST = CONTAINERS + 4
    LOCKED_CHEST = CONTAINERS + 5
    CRYSTAL_CHEST = CONTAINERS + 6
    EBONY_CHEST = CONTAINERS + 7

    size_dict[BONES] = (14, 11)
    size_dict[REMAINS] = (14, 11)
    size_dict[TOMB] = (14, 15)
    size_dict[GRAVE] = (14, 15)
    size_dict[CHEST] = (16, 14)
    size_dict[LOCKED_CHEST] = (16, 14)
    size_dict[CRYSTAL_CHEST] = (16, 14)
    size_dict[EBONY_CHEST] = (16, 14)

    # 杂物
    MISC_CONSUMABLE = cr(4, 1)
    ANKH = MISC_CONSUMABLE + 0
    STYLUS = MISC_CONSUMABLE + 1
    SEAL = MISC_CONSUMABLE + 2
    TORCH = MISC_CONSUMABLE + 3
    BEACON = MISC_CONSUMABLE + 4
    HONEYPOT = MISC_CONSUMABLE + 5
    SHATTPOT = MISC_CONSUMABLE + 6
    IRON_KEY = MISC_CONSUMABLE + 7
    GOLDEN_KEY = MISC_CONSUMABLE + 8
    CRYSTAL_KEY = MISC_CONSUMABLE + 9
    SKELETON_KEY = MISC_CONSUMABLE + 10
    MASK = MISC_CONSUMABLE + 11
    CROWN = MISC_CONSUMABLE + 12
    AMULET = MISC_CONSUMABLE + 13
    MASTERY = MISC_CONSUMABLE + 14
    KIT = MISC_CONSUMABLE + 15

    size_dict[ANKH] = (10, 16)
    size_dict[STYLUS] = (12, 13)

    size_dict[SEAL] = (9, 15)
    size_dict[TORCH] = (12, 15)
    size_dict[BEACON] = (16, 15)

    size_dict[HONEYPOT] = (14, 12)
    size_dict[SHATTPOT] = (14, 12)
    size_dict[IRON_KEY] = (8, 14)
    size_dict[GOLDEN_KEY] = (8, 14)
    size_dict[CRYSTAL_KEY] = (8, 14)
    size_dict[SKELETON_KEY] = (8, 14)
    size_dict[MASK] = (11, 9)
    size_dict[CROWN] = (13, 7)
    size_dict[AMULET] = (16, 16)
    size_dict[MASTERY] = (13, 16)
    size_dict[KIT] = (16, 15)

    # 炸弹
    BOMBS = cr(5, 1)
    BOMB = BOMBS + 0
    DBL_BOMB = BOMBS + 1
    FIRE_BOMB = BOMBS + 2
    FROST_BOMB = BOMBS + 3
    REGROWTH_BOMB = BOMBS + 4
    FLASHBANG = BOMBS + 5
    SHOCK_BOMB = BOMBS + 6
    HOLY_BOMB = BOMBS + 7
    WOOLY_BOMB = BOMBS + 8
    NOISEMAKER = BOMBS + 9
    ARCANE_BOMB = BOMBS + 10
    SHRAPNEL_BOMB = BOMBS + 11

    size_dict[BOMB] = (10, 13)
    size_dict[DBL_BOMB] = (14, 13)
    size_dict[FIRE_BOMB] = (13, 12)
    size_dict[FROST_BOMB] = (13, 12)
    size_dict[REGROWTH_BOMB] = (13, 12)
    size_dict[FLASHBANG] = (13, 12)
    size_dict[SHOCK_BOMB] = (10, 13)
    size_dict[HOLY_BOMB] = (10, 13)
    size_dict[WOOLY_BOMB] = (10, 13)
    size_dict[NOISEMAKER] = (10, 13)
    size_dict[ARCANE_BOMB] = (10, 13)
    size_dict[SHRAPNEL_BOMB] = (10, 13)

    WEP_TIER1 = cr(7, 1)
    WORN_SHORTSWORD = WEP_TIER1 + 0
    CUDGEL = WEP_TIER1 + 1
    GLOVES = WEP_TIER1 + 2
    RAPIER = WEP_TIER1 + 3
    DAGGER = WEP_TIER1 + 4
    MAGES_STAFF = WEP_TIER1 + 5

    size_dict[WORN_SHORTSWORD] = (13, 13)
    size_dict[GLOVES] = (12, 16)
    size_dict[DAGGER] = (12, 13)
    size_dict[MAGES_STAFF] = (15, 16)

    WEP_TIER2 = cr(7, 9)
    SHORTSWORD = WEP_TIER2 + 0
    HAND_AXE = WEP_TIER2 + 1
    SPEAR = WEP_TIER2 + 2
    QUARTERSTAFF = WEP_TIER2 + 3
    DIRK = WEP_TIER2 + 4

    size_dict[SHORTSWORD] = (13, 13)
    size_dict[HAND_AXE] = (12, 14)
    size_dict[SPEAR] = (16, 16)
    size_dict[QUARTERSTAFF] = (16, 16)
    size_dict[DIRK] = (13, 14)

    WEP_TIER3 = cr(8, 1)
    SWORD = WEP_TIER3 + 0
    MACE = WEP_TIER3 + 1
    SCIMITAR = WEP_TIER3 + 2
    ROUND_SHIELD = WEP_TIER3 + 3
    SAI = WEP_TIER3 + 4
    WHIP = WEP_TIER3 + 5

    size_dict[SWORD] = (14, 14)
    size_dict[MACE] = (15, 15)
    size_dict[SCIMITAR] = (13, 16)
    size_dict[ROUND_SHIELD] = (16, 16)
    size_dict[SAI] = (16, 16)
    size_dict[WHIP] = (14, 14)

    WEP_TIER4 = cr(8, 9)
    LONGSWORD = WEP_TIER4 + 0
    BATTLE_AXE = WEP_TIER4 + 1
    FLAIL = WEP_TIER4 + 2
    RUNIC_BLADE = WEP_TIER4 + 3
    ASSASSINS_BLADE = WEP_TIER4 + 4
    CROSSBOW = WEP_TIER4 + 5

    size_dict[LONGSWORD] = (15, 15)
    size_dict[BATTLE_AXE] = (16, 16)
    size_dict[FLAIL] = (14, 14)
    size_dict[RUNIC_BLADE] = (14, 14)
    size_dict[ASSASSINS_BLADE] = (14, 15)
    size_dict[CROSSBOW] = (15, 15)

    WEP_TIER5 = cr(9, 1)
    GREATSWORD = WEP_TIER5 + 0
    WAR_HAMMER = WEP_TIER5 + 1
    GLAIVE = WEP_TIER5 + 2
    GREATAXE = WEP_TIER5 + 3
    GREATSHIELD = WEP_TIER5 + 4
    GAUNTLETS = WEP_TIER5 + 5

    size_dict[GREATSWORD] = (16, 16)
    size_dict[WAR_HAMMER] = (16, 16)
    size_dict[GLAIVE] = (16, 16)
    size_dict[GREATAXE] = (12, 16)
    size_dict[GREATSHIELD] = (12, 16)
    size_dict[GAUNTLETS] = (13, 15)

    MISSILE_WEP = cr(10, 1)
    SPIRIT_BOW = MISSILE_WEP + 0

    DART = MISSILE_WEP + 1
    THROWING_KNIFE = MISSILE_WEP + 2
    THROWING_STONE = MISSILE_WEP + 3

    FISHING_SPEAR = MISSILE_WEP + 4
    SHURIKEN = MISSILE_WEP + 5
    THROWING_CLUB = MISSILE_WEP + 6

    THROWING_SPEAR = MISSILE_WEP + 7
    BOLAS = MISSILE_WEP + 8
    KUNAI = MISSILE_WEP + 9

    JAVELIN = MISSILE_WEP + 10
    TOMAHAWK = MISSILE_WEP + 11
    BOOMERANG = MISSILE_WEP + 12

    TRIDENT = MISSILE_WEP + 13
    THROWING_HAMMER = MISSILE_WEP + 14
    FORCE_CUBE = MISSILE_WEP + 15

    size_dict[SPIRIT_BOW] = (16, 16)

    size_dict[DART] = (15, 15)
    size_dict[THROWING_KNIFE] = (12, 13)
    size_dict[THROWING_STONE] = (12, 10)

    size_dict[FISHING_SPEAR] = (11, 11)
    size_dict[SHURIKEN] = (12, 12)
    size_dict[THROWING_CLUB] = (12, 12)

    size_dict[THROWING_SPEAR] = (13, 13)
    size_dict[BOLAS] = (15, 14)
    size_dict[KUNAI] = (15, 15)

    size_dict[JAVELIN] = (16, 16)
    size_dict[TOMAHAWK] = (13, 13)
    size_dict[BOOMERANG] = (14, 14)

    size_dict[TRIDENT] = (16, 16)
    size_dict[THROWING_HAMMER] = (12, 12)
    size_dict[FORCE_CUBE] = (11, 12)

    # 箭矢
    TIPPED_DARTS = cr(11, 1)
    ROT_DART = TIPPED_DARTS + 0
    INCENDIARY_DART = TIPPED_DARTS + 1
    ADRENALINE_DART = TIPPED_DARTS + 2
    HEALING_DART = TIPPED_DARTS + 3
    CHILLING_DART = TIPPED_DARTS + 4
    SHOCKING_DART = TIPPED_DARTS + 5
    POISON_DART = TIPPED_DARTS + 6
    CLEANSING_DART = TIPPED_DARTS + 7
    PARALYTIC_DART = TIPPED_DARTS + 8
    HOLY_DART = TIPPED_DARTS + 9
    DISPLACING_DART = TIPPED_DARTS + 10
    BLINDING_DART = TIPPED_DARTS + 11

    for index in range(TIPPED_DARTS, BLINDING_DART+1):
        size_dict[index] = (15, 15)

    # 装备
    ARMOR = cr(12, 1)
    ARMOR_CLOTH = ARMOR + 0
    ARMOR_LEATHER = ARMOR + 1
    ARMOR_MAIL = ARMOR + 2
    ARMOR_SCALE = ARMOR + 3
    ARMOR_PLATE = ARMOR + 4
    ARMOR_WARRIOR = ARMOR + 5
    ARMOR_MAGE = ARMOR + 6
    ARMOR_ROGUE = ARMOR + 7
    ARMOR_HUNTRESS = ARMOR + 8

    size_dict[ARMOR_CLOTH] = (15, 12)
    size_dict[ARMOR_LEATHER] = (14, 13)
    size_dict[ARMOR_MAIL] = (14, 12)
    size_dict[ARMOR_SCALE] = (14, 11)
    size_dict[ARMOR_PLATE] = (12, 12)
    size_dict[ARMOR_WARRIOR] = (12, 12)
    size_dict[ARMOR_MAGE] = (15, 15)
    size_dict[ARMOR_ROGUE] = (14, 12)
    size_dict[ARMOR_HUNTRESS] = (13, 15)

    # 法杖
    WANDS = cr(14, 1)
    WAND_MAGIC_MISSILE = WANDS + 0
    WAND_FIREBOLT = WANDS + 1
    WAND_FROST = WANDS + 2
    WAND_LIGHTNING = WANDS + 3
    WAND_DISINTEGRATION = WANDS + 4
    WAND_PRISMATIC_LIGHT = WANDS + 5
    WAND_CORROSION = WANDS + 6
    WAND_LIVING_EARTH = WANDS + 7
    WAND_BLAST_WAVE = WANDS + 8
    WAND_CORRUPTION = WANDS + 9
    WAND_WARDING = WANDS + 10
    WAND_REGROWTH = WANDS + 11
    WAND_TRANSFUSION = WANDS + 12

    for index in range(WANDS, WAND_TRANSFUSION+1):
        size_dict[index] = (14, 14)

    # 戒指
    RINGS = cr(15, 1)
    RING_GARNET = RINGS + 0
    RING_RUBY = RINGS + 1
    RING_TOPAZ = RINGS + 2
    RING_EMERALD = RINGS + 3
    RING_ONYX = RINGS + 4
    RING_OPAL = RINGS + 5
    RING_TOURMALINE = RINGS + 6
    RING_SAPPHIRE = RINGS + 7
    RING_AMETHYST = RINGS + 8
    RING_QUARTZ = RINGS + 9
    RING_AGATE = RINGS + 10
    RING_DIAMOND = RINGS + 11

    for index in range(RINGS, RING_DIAMOND+1):
        size_dict[index] = (8, 10)

    # 神器
    ARTIFACTS = cr(16, 1)
    ARTIFACT_CLOAK = ARTIFACTS + 0
    ARTIFACT_ARMBAND = ARTIFACTS + 1
    ARTIFACT_CAPE = ARTIFACTS + 2
    ARTIFACT_TALISMAN = ARTIFACTS + 3
    ARTIFACT_HOURGLASS = ARTIFACTS + 4
    ARTIFACT_TOOLKIT = ARTIFACTS + 5
    ARTIFACT_SPELLBOOK = ARTIFACTS + 6
    ARTIFACT_BEACON = ARTIFACTS + 7
    ARTIFACT_CHAINS = ARTIFACTS + 8
    ARTIFACT_HORN1 = ARTIFACTS + 9
    ARTIFACT_HORN2 = ARTIFACTS + 10
    ARTIFACT_HORN3 = ARTIFACTS + 11
    ARTIFACT_HORN4 = ARTIFACTS + 12
    ARTIFACT_CHALICE1 = ARTIFACTS + 13
    ARTIFACT_CHALICE2 = ARTIFACTS + 14
    ARTIFACT_CHALICE3 = ARTIFACTS + 15
    ARTIFACT_SANDALS = ARTIFACTS + 16
    ARTIFACT_SHOES = ARTIFACTS + 17
    ARTIFACT_BOOTS = ARTIFACTS + 18
    ARTIFACT_GREAVES = ARTIFACTS + 19
    ARTIFACT_ROSE1 = ARTIFACTS + 20
    ARTIFACT_ROSE2 = ARTIFACTS + 21
    ARTIFACT_ROSE3 = ARTIFACTS + 22

    size_dict[ARTIFACT_CLOAK] = (9, 15)
    size_dict[ARTIFACT_ARMBAND] = (16, 13)
    size_dict[ARTIFACT_CAPE] = (16, 14)
    size_dict[ARTIFACT_TALISMAN] = (15, 13)
    size_dict[ARTIFACT_HOURGLASS] = (13, 16)
    size_dict[ARTIFACT_TOOLKIT] = (15, 13)
    size_dict[ARTIFACT_SPELLBOOK] = (13, 16)
    size_dict[ARTIFACT_BEACON] = (16, 16)
    size_dict[ARTIFACT_CHAINS] = (16, 16)
    size_dict[ARTIFACT_HORN1] = (15, 15)
    size_dict[ARTIFACT_HORN2] = (15, 15)
    size_dict[ARTIFACT_HORN3] = (15, 15)
    size_dict[ARTIFACT_HORN4] = (15, 15)
    size_dict[ARTIFACT_CHALICE1] = (12, 15)
    size_dict[ARTIFACT_CHALICE2] = (12, 15)
    size_dict[ARTIFACT_CHALICE3] = (12, 15)
    size_dict[ARTIFACT_SANDALS] = (16, 6)
    size_dict[ARTIFACT_SHOES] = (16, 6)
    size_dict[ARTIFACT_BOOTS] = (16, 9)
    size_dict[ARTIFACT_GREAVES] = (16, 14)
    size_dict[ARTIFACT_ROSE1] = (14, 14)
    size_dict[ARTIFACT_ROSE2] = (14, 14)
    size_dict[ARTIFACT_ROSE3] = (14, 14)

    # 卷轴
    SCROLLS = cr(19, 1)
    SCROLL_KAUNAN = SCROLLS + 0
    SCROLL_SOWILO = SCROLLS + 1
    SCROLL_LAGUZ = SCROLLS + 2
    SCROLL_YNGVI = SCROLLS + 3
    SCROLL_GYFU = SCROLLS + 4
    SCROLL_RAIDO = SCROLLS + 5
    SCROLL_ISAZ = SCROLLS + 6
    SCROLL_MANNAZ = SCROLLS + 7
    SCROLL_NAUDIZ = SCROLLS + 8
    SCROLL_BERKANAN = SCROLLS + 9
    SCROLL_ODAL = SCROLLS + 10
    SCROLL_TIWAZ = SCROLLS + 11

    for index in range(SCROLLS, SCROLL_TIWAZ+1):
        size_dict[index] = (15, 14)

    SCROLL_CATALYST = SCROLLS + 13
    ARCANE_RESIN = SCROLLS + 14

    size_dict[SCROLL_CATALYST] = (12, 11)
    size_dict[ARCANE_RESIN] = (12, 11)

    EXOTIC_SCROLLS = cr(20, 1)
    EXOTIC_KAUNAN = EXOTIC_SCROLLS + 0
    EXOTIC_SOWILO = EXOTIC_SCROLLS + 1
    EXOTIC_LAGUZ = EXOTIC_SCROLLS + 2
    EXOTIC_YNGVI = EXOTIC_SCROLLS + 3
    EXOTIC_GYFU = EXOTIC_SCROLLS + 4
    EXOTIC_RAIDO = EXOTIC_SCROLLS + 5
    EXOTIC_ISAZ = EXOTIC_SCROLLS + 6
    EXOTIC_MANNAZ = EXOTIC_SCROLLS + 7
    EXOTIC_NAUDIZ = EXOTIC_SCROLLS + 8
    EXOTIC_BERKANAN = EXOTIC_SCROLLS + 9
    EXOTIC_ODAL = EXOTIC_SCROLLS + 10
    EXOTIC_TIWAZ = EXOTIC_SCROLLS + 11

    for index in range(EXOTIC_SCROLLS, EXOTIC_TIWAZ+1):
        size_dict[index] = (15, 14)

    # 魔石
    STONES = cr(21, 1)
    STONE_AGGRESSION = STONES + 0
    STONE_AUGMENTATION = STONES + 1
    STONE_FEAR = STONES + 2
    STONE_BLAST = STONES + 3
    STONE_BLINK = STONES + 4
    STONE_CLAIRVOYANCE = STONES + 5
    STONE_SLEEP = STONES + 6
    STONE_DISARM = STONES + 7
    STONE_ENCHANT = STONES + 8
    STONE_FLOCK = STONES + 9
    STONE_INTUITION = STONES + 10
    STONE_SHOCK = STONES + 11

    for index in range(STONES, STONE_SHOCK+1):
        size_dict[index] = (14, 12)

    # 药剂
    POTIONS = cr(22, 1)
    POTION_CRIMSON = POTIONS + 0
    POTION_AMBER = POTIONS + 1
    POTION_GOLDEN = POTIONS + 2
    POTION_JADE = POTIONS + 3
    POTION_TURQUOISE = POTIONS + 4
    POTION_AZURE = POTIONS + 5
    POTION_INDIGO = POTIONS + 6
    POTION_MAGENTA = POTIONS + 7
    POTION_BISTRE = POTIONS + 8
    POTION_CHARCOAL = POTIONS + 9
    POTION_SILVER = POTIONS + 10
    POTION_IVORY = POTIONS + 11
    POTION_CATALYST = POTIONS + 13
    LIQUID_METAL = POTIONS + 14

    for index in range(POTIONS, POTION_IVORY+1):
        size_dict[index] = (12, 14)

    size_dict[POTION_CATALYST] = (6, 15)
    size_dict[LIQUID_METAL] = (8, 15)

    EXOTIC_POTIONS = cr(23, 1)
    EXOTIC_CRIMSON = EXOTIC_POTIONS + 0
    EXOTIC_AMBER = EXOTIC_POTIONS + 1
    EXOTIC_GOLDEN = EXOTIC_POTIONS + 2
    EXOTIC_JADE = EXOTIC_POTIONS + 3
    EXOTIC_TURQUOISE = EXOTIC_POTIONS + 4
    EXOTIC_AZURE = EXOTIC_POTIONS + 5
    EXOTIC_INDIGO = EXOTIC_POTIONS + 6
    EXOTIC_MAGENTA = EXOTIC_POTIONS + 7
    EXOTIC_BISTRE = EXOTIC_POTIONS + 8
    EXOTIC_CHARCOAL = EXOTIC_POTIONS + 9
    EXOTIC_SILVER = EXOTIC_POTIONS + 10
    EXOTIC_IVORY = EXOTIC_POTIONS + 11

    for index in range(EXOTIC_POTIONS, EXOTIC_IVORY+1):
        size_dict[index] = (12, 13)

    # 种子
    SEEDS = cr(24, 1)
    SEED_ROTBERRY = SEEDS + 0
    SEED_FIREBLOOM = SEEDS + 1
    SEED_SWIFTTHISTLE = SEEDS + 2
    SEED_SUNGRASS = SEEDS + 3
    SEED_ICECAP = SEEDS + 4
    SEED_STORMVINE = SEEDS + 5
    SEED_SORROWMOSS = SEEDS + 6
    SEED_MAGEROYAL = SEEDS + 7
    SEED_EARTHROOT = SEEDS + 8
    SEED_STARFLOWER = SEEDS + 9
    SEED_FADELEAF = SEEDS + 10
    SEED_BLINDWEED = SEEDS + 11

    for index in range(SEEDS, SEED_BLINDWEED+1):
        size_dict[index] = (10, 10)

    # 龙息
    BREWS = cr(25, 1)
    BREW_INFERNAL = BREWS + 0
    BREW_BLIZZARD = BREWS + 1
    BREW_SHOCKING = BREWS + 2
    BREW_CAUSTIC = BREWS + 3

    ELIXIRS = cr(25, 5)
    ELIXIR_HONEY = ELIXIRS + 0
    ELIXIR_AQUA = ELIXIRS + 1
    ELIXIR_MIGHT = ELIXIRS + 2
    ELIXIR_DRAGON = ELIXIRS + 3
    ELIXIR_TOXIC = ELIXIRS + 4
    ELIXIR_ICY = ELIXIRS + 5
    ELIXIR_ARCANE = ELIXIRS + 6

    for index in range(BREWS, ELIXIR_ARCANE+1):
        size_dict[index] = (12, 14)

    SPELLS = cr(27, 1)
    MAGIC_PORTER = SPELLS + 0
    PHASE_SHIFT = SPELLS + 1
    TELE_GRAB = SPELLS + 2
    WILD_ENERGY = SPELLS + 3
    RETURN_BEACON = SPELLS + 4
    SUMMON_ELE = SPELLS + 5

    AQUA_BLAST = SPELLS + 7
    FEATHER_FALL = SPELLS + 8
    RECLAIM_TRAP = SPELLS + 9

    CURSE_INFUSE = SPELLS + 11
    MAGIC_INFUSE = SPELLS + 12
    ALCHEMIZE = SPELLS + 13
    RECYCLE = SPELLS + 14

    size_dict[MAGIC_PORTER] = (12, 11)
    size_dict[PHASE_SHIFT] = (12, 11)
    size_dict[TELE_GRAB] = (12, 11)
    size_dict[WILD_ENERGY] = (8, 16)
    size_dict[RETURN_BEACON] = (8, 16)
    size_dict[SUMMON_ELE] = (8, 16)

    size_dict[AQUA_BLAST] = (11, 11)
    size_dict[FEATHER_FALL] = (11, 11)
    size_dict[RECLAIM_TRAP] = (11, 11)

    size_dict[CURSE_INFUSE] = (10, 15)
    size_dict[MAGIC_INFUSE] = (10, 15)
    size_dict[ALCHEMIZE] = (10, 15)
    size_dict[RECYCLE] = (10, 15)

    # 食物
    FOOD = cr(28, 1)
    MEAT = FOOD + 0
    STEAK = FOOD + 1
    STEWED = FOOD + 2
    OVERPRICED = FOOD + 3
    CARPACCIO = FOOD + 4
    RATION = FOOD + 5
    PASTY = FOOD + 6
    PUMPKIN_PIE = FOOD + 7
    CANDY_CANE = FOOD + 8
    MEAT_PIE = FOOD + 9
    BLANDFRUIT = FOOD + 10
    BLAND_CHUNKS = FOOD + 11
    BERRY = FOOD + 12

    size_dict[MEAT] = (15, 11)
    size_dict[STEAK] = (15, 11)
    size_dict[STEWED] = (15, 11)
    size_dict[OVERPRICED] = (14, 11)
    size_dict[CARPACCIO] = (15, 11)
    size_dict[RATION] = (16, 12)
    size_dict[PASTY] = (16, 11)
    size_dict[PUMPKIN_PIE] = (16, 12)
    size_dict[CANDY_CANE] = (13, 16)
    size_dict[MEAT_PIE] = (16, 12)
    size_dict[BLANDFRUIT] = (9, 12)
    size_dict[BLAND_CHUNKS] = (14, 6)
    size_dict[BERRY] = (9, 11)

    # 任务道具
    QUEST = cr(29, 1)
    SKULL = QUEST + 0
    DUST = QUEST + 1
    CANDLE = QUEST + 2
    EMBER = QUEST + 3
    PICKAXE = QUEST + 4
    ORE = QUEST + 5
    TOKEN = QUEST + 6
    BLOB = QUEST + 7
    SHARD = QUEST + 8

    size_dict[SKULL] = (16, 11)
    size_dict[DUST] = (12, 11)
    size_dict[CANDLE] = (12, 12)
    size_dict[EMBER] = (12, 11)
    size_dict[PICKAXE] = (14, 14)
    size_dict[ORE] = (15, 15)
    size_dict[TOKEN] = (12, 12)
    size_dict[BLOB] = (10, 9)
    size_dict[SHARD] = (8, 10)

    # 背包
    BAGS = cr(31, 1)
    WATERSKIN = BAGS + 0
    BACKPACK = BAGS + 1
    POUCH = BAGS + 2
    HOLDER = BAGS + 3
    BANDOLIER = BAGS + 4
    HOLSTER = BAGS + 5
    VIAL = BAGS + 6

    size_dict[WATERSKIN] = (16, 14)
    size_dict[BACKPACK] = (16, 16)
    size_dict[POUCH] = (14, 15)
    size_dict[HOLDER] = (16, 16)
    size_dict[BANDOLIER] = (15, 16)
    size_dict[HOLSTER] = (15, 16)
    size_dict[VIAL] = (12, 12)

    instance = None

    tiles_dict = {}

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.tileset = tiles_item_reader
        for code, size in self.size_dict.items():
            width, height = size
            surface = pygame.Surface((16, 16)).convert_alpha()
            surface.fill((0, 0, 0, 0))
            width_offset = (16-width) // 2
            height_offset = (16-height-1)
            surface.blit(self.tileset[code].subsurface(0, 0, width, height), (width_offset, height_offset))
            self.tiles_dict[code] = surface

    def __getitem__(self, item: int):
        return self.tiles_dict[item]


tiles_item = TilesItems()
