#######################################
# --------------------------------------
#######################################
import re
import string as stringfunc
import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
import os
import random
# Dictionaries
# Generation Dictionary
generations_dict = {
    "Generation 1": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Nidoran", "Nidorano",
                     "Zubat",
                     "Oddish", "Poliwag", "Abra", "Machop", "Bellsprout", "Geodude", "Magnemite", "Gastly", "Rhyhorn",
                     "Horsea",
                     "Porygon", "Dratini", ],
    "Generation 2": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Pichu", "Nidoran",
                     "Cleffa",
                     "Igglybuff", "Zubat", "Oddish", "Poliwag", "Abra", "Machop", "Bellsprout", "Geodude", "Magnemite",
                     "Gastly",
                     "Rhyhorn", "Happiny", "Horsea", "Elekid", "Magby", "Porygon", "Dratini", "Chikorita", "Cyndaquil",
                     "Totodile",
                     "Togepi", "Mareep", "Azurill", "Hoppip", "Swinub", "Larvitar", ],
    "Generation 3": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Pichu", "Nidoran",
                     "Cleffa",
                     "Igglybuff", "Zubat", "Oddish", "Poliwag", "Abra", "Machop", "Bellsprout", "Geodude", "Magnemite",
                     "Gastly",
                     "Rhyhorn", "Happiny", "Horsea", "Elekid", "Magby", "Porygon", "Dratini", "Chikorita", "Cyndaquil",
                     "Totodile",
                     "Togepi", "Mareep", "Azurill", "Hoppip", "Swinub", "Larvitar", "Treecko", "Torchic", "Mudkip",
                     "Wurmple",
                     "Lotad", "Seedot", "Ralts", "Slakoth", "Whismur", "Aron", "Budew", "Trapinch", "Duskull", "Spheal",
                     "Bagon",
                     "Beldum", ],
    "Generation 4": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Pichu", "Nidoran",
                     "Cleffa",
                     "Igglybuff", "Zubat", "Oddish", "Poliwag", "Abra", "Machop", "Bellsprout", "Geodude", "Magnemite",
                     "Gastly",
                     "Rhyhorn", "Happiny", "Horsea", "Elekid", "Magby", "Porygon", "Dratini", "Chikorita", "Cyndaquil",
                     "Totodile",
                     "Togepi", "Mareep", "Azurill", "Hoppip", "Swinub", "Larvitar", "Treecko", "Torchic", "Mudkip",
                     "Wurmple",
                     "Lotad", "Seedot", "Ralts", "Slakoth", "Whismur", "Aron", "Budew", "Trapinch", "Duskull", "Spheal",
                     "Bagon",
                     "Beldum", "Turtwig", "Chimchar", "Piplup", "Starly", "Shinx", "Gible", ],
    "Generation 5": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Pichu", "Nidoran",
                     "Cleffa",
                     "Igglybuff", "Zubat", "Oddish", "Poliwag", "Abra", "Machop", "Bellsprout", "Geodude", "Magnemite",
                     "Gastly",
                     "Rhyhorn", "Happiny", "Horsea", "Elekid", "Magby", "Porygon", "Dratini", "Chikorita", "Cyndaquil",
                     "Totodile",
                     "Togepi", "Mareep", "Azurill", "Hoppip", "Swinub", "Larvitar", "Treecko", "Torchic", "Mudkip",
                     "Wurmple",
                     "Lotad", "Seedot", "Ralts", "Slakoth", "Whismur", "Aron", "Budew", "Trapinch", "Duskull", "Spheal",
                     "Bagon",
                     "Beldum", "Turtwig", "Chimchar", "Piplup", "Starly", "Shinx", "Gible", "Snivy", "Tepig",
                     "Oshawott",
                     "Lillipup", "Pidove", "Roggenrola", "Timburr", "Tympole", "Sewaddle", "Venipede", "Sandile",
                     "Gothita",
                     "Solosis", "Vanillite", "Klink", "Tynamo", "Litwick", "Axew", "Deino", ],
    "Generation 6": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Pichu", "Nidoran",
                     "Cleffa",
                     "Igglybuff", "Zubat", "Oddish", "Poliwag", "Abra", "Machop", "Bellsprout", "Geodude", "Magnemite",
                     "Gastly",
                     "Rhyhorn", "Happiny", "Horsea", "Elekid", "Magby", "Porygon", "Dratini", "Chikorita", "Cyndaquil",
                     "Totodile",
                     "Togepi", "Mareep", "Azurill", "Hoppip", "Swinub", "Larvitar", "Treecko", "Torchic", "Mudkip",
                     "Wurmple",
                     "Lotad", "Seedot", "Ralts", "Slakoth", "Whismur", "Aron", "Budew", "Trapinch", "Duskull", "Spheal",
                     "Bagon",
                     "Beldum", "Turtwig", "Chimchar", "Piplup", "Starly", "Shinx", "Gible", "Snivy", "Tepig",
                     "Oshawott",
                     "Lillipup", "Pidove", "Roggenrola", "Timburr", "Tympole", "Sewaddle", "Venipede", "Sandile",
                     "Gothita",
                     "Solosis", "Vanillite", "Klink", "Tynamo", "Litwick", "Axew", "Deino", "Chespin", "Fennekin",
                     "Froakie",
                     "Fletchling", "Scatterbug", "Flabébé", "Honedge", "Goomy", ],
    "Generation 7": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Pichu", "Nidoran",
                     "Cleffa",
                     "Igglybuff", "Zubat", "Oddish", "Poliwag", "Abra", "Machop", "Bellsprout", "Geodude", "Magnemite",
                     "Gastly",
                     "Rhyhorn", "Happiny", "Horsea", "Elekid", "Magby", "Porygon", "Dratini", "Chikorita", "Cyndaquil",
                     "Totodile",
                     "Togepi", "Mareep", "Azurill", "Hoppip", "Swinub", "Larvitar", "Treecko", "Torchic", "Mudkip",
                     "Wurmple",
                     "Lotad", "Seedot", "Ralts", "Slakoth", "Whismur", "Aron", "Budew", "Trapinch", "Duskull", "Spheal",
                     "Bagon",
                     "Beldum", "Turtwig", "Chimchar", "Piplup", "Starly", "Shinx", "Gible", "Snivy", "Tepig",
                     "Oshawott",
                     "Lillipup", "Pidove", "Roggenrola", "Timburr", "Tympole", "Sewaddle", "Venipede", "Sandile",
                     "Gothita",
                     "Solosis", "Vanillite", "Klink", "Tynamo", "Litwick", "Axew", "Deino", "Chespin", "Fennekin",
                     "Froakie",
                     "Fletchling", "Scatterbug", "Flabébé", "Honedge", "Goomy", "Rowlet", "Litten", "Popplio",
                     "Pikipek",
                     "Grubbin", "Bounsweet", "Jangmo-o", "Cosmog", ],
}
# Pokemon Types
type_list = {
    "bug": ["Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Paras", "Parasect", "Venonat",
            "Venomoth", "Scyther", "Scizor", "Pinsir", "Ledyba", "Ledian", "Spinarak", "Ariados", "Yanma", "Pineco",
            "Forretress", "Shuckle", "Heracross", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Surskit",
            "Masquerain", "Nincada", "Ninjask", "Shedinja", "Volbeat", "Illumise", "Anorith", "Armaldo", "Kricketot",
            "Kricketune", "Burmy", "Wormadam", "Mothim", "Combee", "Vespiquen", "Skorupi", "Yanmega", "Sewaddle",
            "Swadloon", "Leavanny", "Venipede", "Whirlipede", "Scolipede", "Dwebble", "Crustle", "Karrablast",
            "Escavalier", "Joltik", "Galvantula", "Shelmet", "Accelgor", "Durant", "Larvesta", "Volcarona", "Genesect",
            "Scatterbug", "Spewpa", "Vivillon", "Grubbin", "Charjabug", "Vikavolt", "Cutiefly", "Ribombee", "Dewpider",
            "Araquanid", "Wimpod", "Golisopod", "Nihilego", "Buzzwole", "Pheromosa", ],
    "dark": ["Eevee", "Umbreon", "Murkrow", "Sneasel", "Houndour", "Houndoom", "Larvitar", "Pupitar", "Tyranitar",
             "Poochyena", "Mightyena", "Seedot", "Nuzleaf", "Shiftry", "Sableye", "Carvanha", "Sharpedo", "Cacnea",
             "Cacturne", "Corphish", "Crawdaunt", "Absol", "Honchkrow", "Stunky", "Skuntank", "Spiritomb", "Skorupi",
             "Drapion", "Weavile", "Darkrai", "Purrloin", "Liepard", "Sandile", "Krokorok", "Krookodile", "Scraggy",
             "Scrafty", "Zorua", "Zoroark", "Pawniard", "Bisharp", "Vullaby", "Mandibuzz", "Deino", "Zweilous",
             "Hydreigon", "Froakie", "Frogadier", "Greninja", "Pancham", "Pangoro", "Inkay", "Malamar", "Yveltal",
             "Hoopa", "Litten", "Torracat", "Incineroar", "Guzzlord", "Rattata (Forme 1)", "Raticate (Forme 1)",
             "Meowth (Forme 1)", "Persian (Forme 1)", "Grimer (Forme 1)", "Muk (Forme 1)", ],
    "dragon": ["Horsea", "Seadra", "Kingdra", "Dratini", "Dragonair", "Dragonite", "Trapinch", "Vibrava", "Flygon",
               "Swablu", "Altaria", "Bagon", "Shelgon", "Salamence", "Latias", "Latios", "Rayquaza", "Gible", "Gabite",
               "Garchomp", "Dialga", "Palkia", "Giratina", "Axew", "Fraxure", "Haxorus", "Druddigon", "Deino",
               "Zweilous", "Hydreigon", "Reshiram", "Zekrom", "Kyurem", "Skrelp", "Dragalge", "Tyrunt", "Tyrantrum",
               "Goomy", "Sliggoo", "Goodra", "Noibat", "Noivern", "Zygarde", "Turtonator", "Drampa", "Jangmo-o",
               "Hakamo-o", "Kommo-o", "Guzzlord", "Poipole", "Naganadel", "Exeggutor (Forme 1)", ],
    "electric": ["Pichu", "Pikachu", "Raichu", "Raichu (Forme 1)", "Magnemite", "Magneton", "Voltorb", "Electrode",
                 "Elekid", "Electabuzz",
                 "Eevee", "Jolteon", "Zapdos", "Chinchou", "Lanturn", "Mareep", "Flaaffy", "Ampharos", "Raikou",
                 "Electrike", "Manectric", "Plusle", "Minun", "Shinx", "Luxio", "Luxray", "Pachirisu", "Magnezone",
                 "Electivire", "Rotom", "Blitzle", "Zebstrika", "Emolga", "Joltik", "Galvantula", "Tynamo", "Eelektrik",
                 "Eelektross", "Stunfisk", "Thundurus", "Zekrom", "Helioptile", "Heliolisk", "Dedenne", "Grubbin",
                 "Charjabug", "Vikavolt", "Oricorio", "Togedemaru", "Tapu Koko", "Xurkitree", "Zeraora",
                 "Geodude (Forme 1)", "Graveler (Forme 1)", "Golem (Forme 1)", ],
    "fairy": ["Clefairy", "Clefable", "Ninetales (Forme 1)", "Jigglypuff", "Wigglytuff", "Mr. Mime", "Ralts", "Kirlia",
              "Gardevoir", "Azurill", "Mawile", "Mime Jr.", "Togekiss", "Cottonee", "Whimsicott", "Flabébé", "Floette",
              "Florges", "Spritzee", "Aromatisse", "Swirlix", "Slurpuff", "Sylveon", "Dedenne", "Carbink", "Klefki",
              "Xerneas", "Diancie", "Primarina", "Cutiefly", "Ribombee", "Morelull", "Shiinotic", "Comfey", "Mimikyu",
              "Tapu Koko", "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Magearna", ],
    "fighting": ["Mankey", "Primeape", "Poliwag", "Poliwhirl", "Poliwrath", "Machop", "Machoke", "Machamp", "Tyrogue",
                 "Hitmonlee", "Hitmonchan", "Hitmontop", "Heracross", "Torchic", "Combusken", "Blaziken", "Shroomish",
                 "Breloom", "Makuhita", "Hariyama", "Meditite", "Medicham", "Chimchar", "Monferno", "Infernape",
                 "Riolu", "Lucario", "Croagunk", "Toxicroak", "Gallade", "Tepig", "Pignite", "Emboar", "Timburr",
                 "Gurdurr", "Conkeldurr", "Throh", "Sawk", "Scraggy", "Scrafty", "Mienfoo", "Mienshao", "Cobalion",
                 "Terrakion", "Virizion", "Keldeo", "Meloetta", "Chespin", "Quilladin", "Chesnaught", "Pancham",
                 "Pangoro", "Hawlucha", "Crabrawler", "Crabominable", "Stufful", "Bewear", "Passimian", "Jangmo-o",
                 "Hakamo-o", "Kommo-o", "Buzzwole", "Pheromosa", "Marshadow", ],
    "fire": ["Charmander", "Charmeleon", "Charizard", "Vulpix", "Ninetales", "Growlithe", "Arcanine", "Ponyta",
             "Rapidash", "Magby", "Magmar", "Eevee", "Flareon", "Moltres", "Cyndaquil", "Quilava", "Typhlosion",
             "Slugma", "Magcargo", "Houndour", "Houndoom", "Entei", "Ho-Oh", "Torchic", "Combusken", "Blaziken",
             "Numel", "Camerupt", "Torkoal", "Chimchar", "Monferno", "Infernape", "Magmortar", "Rotom", "Heatran",
             "Victini", "Tepig", "Pignite", "Emboar", "Pansear", "Simisear", "Darumaka", "Darmanitan", "Darmanitan",
             "Litwick", "Lampent", "Chandelure", "Heatmor", "Larvesta", "Volcarona", "Reshiram", "Fennekin", "Braixen",
             "Delphox", "Fletchling", "Fletchinder", "Talonflame", "Litleo", "Pyroar", "Volcanion", "Litten",
             "Torracat", "Incineroar", "Oricorio", "Salandit", "Salazzle", "Turtonator", "Blacephalon",
             "Marowak (Forme 1)", ],
    "flying": ["Charmander", "Charmeleon", "Charizard", "Caterpie", "Metapod", "Butterfree", "Pidgey", "Pidgeotto",
               "Pidgeot", "Spearow", "Fearow", "Zubat", "Golbat", "Crobat", "Farfetch", "Doduo", "Dodrio", "Scyther",
               "Magikarp", "Gyarados", "Aerodactyl", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair",
               "Dragonite", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Togepi", "Togetic", "Natu", "Xatu", "Hoppip",
               "Skiploom", "Jumpluff", "Yanma", "Murkrow", "Gligar", "Delibird", "Mantine", "Skarmory", "Lugia",
               "Ho-Oh", "Wurmple", "Silcoon", "Beautifly", "Taillow", "Swellow", "Wingull", "Pelipper", "Surskit",
               "Masquerain", "Nincada", "Ninjask", "Swablu", "Altaria", "Tropius", "Bagon", "Shelgon", "Salamence",
               "Rayquaza", "Starly", "Staravia", "Staraptor", "Burmy", "Mothim", "Combee", "Vespiquen", "Drifloon",
               "Drifblim", "Honchkrow", "Chatot", "Mantyke", "Togekiss", "Yanmega", "Gliscor", "Rotom", "Shaymin",
               "Pidove", "Tranquill", "Unfezant", "Unfezant", "Woobat", "Swoobat", "Sigilyph", "Archen", "Archeops",
               "Ducklett", "Swanna", "Emolga", "Rufflet", "Braviary", "Vullaby", "Mandibuzz", "Tornadus", "Thundurus",
               "Landorus", "Fletchling", "Fletchinder", "Talonflame", "Scatterbug", "Spewpa", "Vivillon", "Hawlucha",
               "Noibat", "Noivern", "Yveltal", "Rowlet", "Dartrix", "Pikipek", "Trumbeak", "Toucannon", "Oricorio",
               "Minior", "Celesteela", ],
    "ghost": ["Gastly", "Haunter", "Gengar", "Misdreavus", "Nincada", "Shedinja", "Sableye", "Shuppet", "Banette",
              "Duskull", "Dusclops", "Drifloon", "Drifblim", "Mismagius", "Spiritomb", "Dusknoir", "Froslass", "Rotom",
              "Giratina", "Yamask", "Cofagrigus", "Frillish", "Frillish", "Jellicent", "Jellicent", "Litwick",
              "Lampent", "Chandelure", "Golett", "Golurk", "Honedge", "Doublade", "Aegislash", "Phantump", "Trevenant",
              "Pumpkaboo", "Gourgeist", "Hoopa", "Rowlet", "Dartrix", "Decidueye", "Oricorio", "Sandygast", "Palossand",
              "Mimikyu", "Dhelmise", "Cosmog", "Cosmoem", "Lunala", "Marshadow", "Marowak (Forme 1)"],
    "grass": ["Bulbasaur", "Ivysaur", "Venusaur", "Oddish", "Gloom", "Vileplume", "Bellossom", "Paras", "Parasect",
              "Bellsprout", "Weepinbell", "Victreebel", "Exeggcute", "Exeggutor", "Exeggutor (Forme 1)", "Tangela",
              "Chikorita", "Bayleef",
              "Meganium", "Hoppip", "Skiploom", "Jumpluff", "Sunkern", "Sunflora", "Celebi", "Treecko", "Grovyle",
              "Sceptile", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Shroomish", "Breloom",
              "Roselia", "Cacnea", "Cacturne", "Lileep", "Cradily", "Tropius", "Turtwig", "Grotle", "Torterra", "Budew",
              "Roserade", "Burmy", "Wormadam", "Cherubi", "Cherrim", "Carnivine", "Snover", "Abomasnow", "Tangrowth",
              "Leafeon", "Eevee", "Rotom", "Shaymin", "Snivy", "Servine", "Serperior", "Pansage", "Simisage",
              "Sewaddle", "Swadloon", "Leavanny", "Cottonee", "Whimsicott", "Petilil", "Lilligant", "Maractus",
              "Deerling", "Sawsbuck", "Foongus", "Amoonguss", "Ferroseed", "Ferrothorn", "Virizion", "Chespin",
              "Quilladin", "Chesnaught", "Skiddo", "Gogoat", "Phantump", "Trevenant", "Pumpkaboo", "Gourgeist",
              "Rowlet", "Dartrix", "Decidueye", "Fomantis", "Lurantis", "Morelull", "Shiinotic", "Bounsweet", "Steenee",
              "Tsareena", "Dhelmise", "Tapu Bulu", ],
    "ground": ["Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidorino", "Nidoking", "Diglett",
               "Dugtrio", "Diglett (Forme 1)", "Dugtrio (Forme 1)", "Geodude", "Graveler", "Golem", "Onix", "Steelix",
               "Cubone", "Marowak", "Rhyhorn", "Rhydon",
               "Wooper", "Quagsire", "Gligar", "Swinub", "Piloswine", "Phanpy", "Donphan", "Larvitar", "Pupitar",
               "Mudkip", "Marshtomp", "Swampert", "Nincada", "Numel", "Camerupt", "Trapinch", "Vibrava", "Flygon",
               "Barboach", "Whiscash", "Baltoy", "Claydol", "Groudon", "Turtwig", "Grotle", "Torterra", "Burmy",
               "Wormadam", "Shellos", "Gastrodon", "Gible", "Gabite", "Garchomp", "Hippopotas", "Hippowdon",
               "Rhyperior", "Gliscor", "Mamoswine", "Drilbur", "Excadrill", "Palpitoad", "Seismitoad", "Sandile",
               "Krokorok", "Krookodile", "Stunfisk", "Golett", "Golurk", "Bunnelby", "Diggersby", "Zygarde", "Mudbray",
               "Mudsdale", "Sandygast", "Palossand", ],
    "ice": ["Seel", "Dewgong", "Shellder", "Cloyster", "Smoochum", "Jynx", "Lapras", "Articuno", "Sneasel", "Swinub",
            "Piloswine", "Delibird", "Snorunt", "Glalie", "Spheal", "Sealeo", "Walrein", "Regice", "Snover",
            "Abomasnow", "Weavile", "Glaceon", "Eevee", "Mamoswine", "Froslass", "Rotom", "Vanillite", "Vanillish",
            "Vanilluxe", "Cubchoo", "Beartic", "Cryogonal", "Kyurem", "Amaura", "Aurorus", "Bergmite", "Avalugg",
            "Crabrawler", "Crabominable", "Sandshrew (Forme 1)", "Sandslash (Forme 1)", "Vulpix (Forme 1)", ],
    "normal": ["Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Igglybuff", "Jigglypuff",
               "Wigglytuff", "Meowth", "Persian", "Farfetch", "Doduo", "Dodrio", "Lickitung", "Chansey", "Blissey",
               "Kangaskhan", "Tauros", "Ditto", "Eevee", "Porygon", "Porygon2", "Snorlax", "Sentret", "Furret",
               "Hoothoot", "Noctowl", "Azurill", "Aipom", "Girafarig", "Dunsparce", "Teddiursa", "Ursaring", "Stantler",
               "Smeargle", "Miltank", "Zigzagoon", "Linoone", "Taillow", "Swellow", "Slakoth", "Vigoroth", "Slaking",
               "Whismur", "Loudred", "Exploud", "Skitty", "Delcatty", "Spinda", "Swablu", "Zangoose", "Castform",
               "Kecleon", "Starly", "Staravia", "Staraptor", "Bidoof", "Bibarel", "Aipom", "Ambipom", "Buneary",
               "Lopunny", "Glameow", "Purugly", "Happiny", "Chatot", "Munchlax", "Lickilicky", "Porygon-Z", "Regigigas",
               "Arceus", "Patrat", "Watchog", "Lillipup", "Herdier", "Stoutland", "Pidove", "Tranquill", "Unfezant",
               "Unfezant", "Audino", "Minccino", "Cinccino", "Deerling", "Sawsbuck", "Bouffalant", "Rufflet",
               "Braviary", "Meloetta", "Meloetta", "Bunnelby", "Diggersby", "Fletchling", "Litleo", "Pyroar", "Furfrou",
               "Helioptile", "Heliolisk", "Pikipek", "Trumbeak", "Toucannon", "Yungoos", "Gumshoos", "Stufful",
               "Bewear", "Oranguru", "Type: Null", "Silvally", "Komala", "Drampa", ],
    "poison": ["Bulbasaur", "Ivysaur", "Venusaur", "Weedle", "Kakuna", "Beedrill", "Ekans", "Arbok", "Nidoran",
               "Nidorina", "Nidoqueen", "Nidorino", "Nidoking", "Zubat", "Golbat", "Crobat", "Oddish", "Gloom",
               "Vileplume", "Venonat", "Venomoth", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel",
               "Grimer", "Muk", "Grimer (Forme 1)", "Muk (Forme 1)", "Gastly", "Haunter", "Gengar", "Koffing",
               "Weezing", "Spinarak", "Ariados", "Qwilfish",
               "Wurmple", "Cascoon", "Dustox", "Roselia", "Gulpin", "Swalot", "Seviper", "Budew", "Roserade", "Stunky",
               "Skuntank", "Skorupi", "Drapion", "Croagunk", "Toxicroak", "Venipede", "Whirlipede", "Scolipede",
               "Trubbish", "Garbodor", "Foongus", "Amoonguss", "Skrelp", "Dragalge", "Mareanie", "Toxapex", "Salandit",
               "Salazzle", "Nihilego", "Poipole", "Naganadel", ],
    "psychic": ["Abra", "Kadabra", "Alakazam", "Slowpoke", "Slowbro", "Slowking", "Drowzee", "Hypno", "Exeggcute",
                "Exeggcutor", "Staryu", "Starmie", "Mime", "Smoochum", "Jynx", "Eevee", "Espeon", "Mewtwo", "Mew",
                "Natu", "Xatu", "Unown", "Wynaut", "Wobbuffet", "Girafarig", "Lugia", "Celebi", "Ralts", "Kirlia",
                "Gardevoir", "Meditite", "Medicham", "Spoink", "Grumpig", "Lunatone", "Solrock", "Baltoy", "Claydol",
                "Chimecho", "Beldum", "Metang", "Metagross", "Latias", "Latios", "Jirachi", "Deoxys", "Chingling",
                "Bronzor", "Bronzong", "Mime Jr.", "Gallade", "Uxie", "Mesprit", "Azelf", "Cresselia", "Victini",
                "Munna", "Musharna", "Woobat", "Swoobat", "Darmanitan", "Sigilyph", "Gothita", "Gothorita",
                "Gothitelle", "Solosis", "Duosion", "Reuniclus", "Elgyem", "Beheeyem", "Meloetta", "Fennekin",
                "Braixen", "Delphox", "Espurr", "Meowstic", "Inkay", "Malamar", "Hoopa", "Oricorio", "Oranguru",
                "Bruxish", "Tapu Lele", "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Necrozma", "Raichu (Forme 1)", ],
    "rock": ["Geodude", "Graveler", "Golem", "Onix", "Rhyhorn", "Rhydon", "Omanyte", "Omastar", "Kabuto", "Kabutops",
             "Aerodactyl", "Sudowoodo", "Shuckle", "Slugma", "Magcargo", "Corsola", "Larvitar", "Pupitar", "Tyranitar",
             "Nosepass", "Aron", "Lairon", "Aggron", "Lunatone", "Solrock", "Lileep", "Cradily", "Anorith", "Armaldo",
             "Relicanth", "Regirock", "Cranidos", "Rampardos", "Bonsly", "Rhyperior", "Probopass", "Roggenrola",
             "Boldore", "Gigalith", "Dwebble", "Crustle", "Tirtouga", "Carracosta", "Archen", "Archeops", "Terrakion",
             "Binacle", "Barbaracle", "Tyrunt", "Tyrantrum", "Amaura", "Aurorus", "Carbink", "Diancie", "Rockruff",
             "Lycanroc", "Minior", "Nihilego", "Stakataka", ],
    "steel": ["Magnemite", "Magneton", "Onix", "Steelix", "Scyther", "Scizor", "Pineco", "Forretress", "Skarmory",
              "Mawile", "Aron", "Lairon", "Aggron", "Beldum", "Metang", "Metagross", "Registeel", "Jirachi", "Piplup",
              "Prinplup", "Empoleon", "Shieldon", "Bastiodon", "Burmy", "Wormadam", "Bronzor", "Bronzong", "Riolu",
              "Lucario", "Magnezone", "Probopass", "Dialga", "Heatran", "Drilbur", "Excadrill", "Karrablast",
              "Escavalier", "Ferroseed", "Ferrothorn", "Klink", "Klang", "Klinklang", "Pawniard", "Bisharp", "Durant",
              "Cobalion", "Genesect", "Honedge", "Doublade", "Aegislash", "Klefki", "Togedemaru", "Cosmog", "Cosmoem",
              "Solgaleo", "Celesteela", "Kartana", "Magearna", "Stakataka", "Sandshrew (Forme 1)",
              "Sandslash (Forme 1)",
              "Diglett (Forme 1)", "Dugtrio (Forme 1)", ],
    "water": ["Squirtle", "Wartortle", "Blastoise", "Psyduck", "Golduck", "Poliwag", "Poliwhirl", "Poliwrath",
              "Politoed", "Tentacool", "Tentacruel", "Tentacruel", "Slowpoke", "Slowbro", "Slowking", "Seel", "Dewgong",
              "Shellder", "Cloyster", "Krabby", "Kingler", "Horsea", "Seadra", "Kingdra", "Goldeen", "Seaking",
              "Staryu", "Starmie", "Magikarp", "Gyarados", "Lapras", "Eevee", "Vaporeon", "Omanyte", "Omastar",
              "Kabuto", "Kabutops", "Totodile", "Croconaw", "Feraligatr", "Chinchou", "Lanturn", "Azurill", "Marill",
              "Azumarill", "Wooper", "Quagsire", "Qwilfish", "Corsola", "Remoraid", "Octillery", "Mantine", "Suicune",
              "Mudkip", "Marshtomp", "Swampert", "Lotad", "Lombre", "Ludicolo", "Wingull", "Pelipper", "Surskit",
              "Carvanha", "Sharpedo", "Wailmer", "Wailord", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Feebas",
              "Milotic", "Spheal", "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc",
              "Kyogre", "Piplup", "Prinplup", "Empoleon", "Bidoof", "Bibarel", "Buizel", "Floatzel", "Shellos",
              "Gastrodon", "Finneon", "Lumineon", "Mantyke", "Rotom", "Palkia", "Phione", "Manaphy", "Oshawott",
              "Dewott", "Samurott", "Panpour", "Simipour", "Tympole", "Palpitoad", "Seismitoad", "Basculin", "Basculin",
              "Tirtouga", "Carracosta", "Ducklett", "Swanna", "Frillish", "Frillish", "Jellicent", "Jellicent",
              "Alomomola", "Keldeo", "Froakie", "Frogadier", "Greninja", "Binacle", "Barbaracle", "Skrelp", "Clauncher",
              "Clawitzer", "Volcanion", "Popplio", "Brionne", "Primarina", "Wishiwashi", "Mareanie", "Toxapex",
              "Dewpider", "Araquanid", "Wimpod", "Golisopod", "Pyukumuku", "Bruxish", "Tapu Fini", ],
}
# Type Names
pkmntype_list = [
    "Bug",
    "Dark",
    "Dragon",
    "Electric",
    "Fairy",
    "Fairy",
    "Fighting",
    "Fire",
    "Flying",
    "Ghost",
    "Grass",
    "Ground",
    "Ice",
    "Normal",
    "Poison",
    "Psychic",
    "Rock",
    "Steel",
    "Water",
]
# Pokemon Games
game_list = [
    "Red",
    "Blue",
    "Yellow",
    "Gold",
    "Silver",
    "Crystal",
    "Ruby",
    "Sapphire",
    "Emerald",
    "FireRed",
    "LeafGreen",
    "Diamond",
    "Pearl",
    "Platinum",
    "HeartGold",
    "SoulSilver",
    "Black",
    "White",
    "Black 2",
    "White 2",
    "X",
    "Y",
    "Omega Ruby",
    "Alpha Sapphire",
    "Sun",
    "Moon",
    "Ultra Sun",
    "Ultra Moon",
]
# Generation List
generation_list = [
    'Generation 1',
    'Generation 2',
    'Generation 3',
    'Generation 4',
    'Generation 5',
    'Generation 6',
    'Generation 7',
]
# Route lists for each game
routes_rby = [
    "Route 1 ", "Route 22", "Route 2 ", "Viridian Forest", "Route 3", "Mt.Moon", "Route 4", "Route 24",
    "Route 25", "Route 5", "Route 6", "Route 11", "Diglett\'s Cave", "Route 9", "Route 10", "Rock Tunnel",
    "Route 7", "Route 8", "[poké]mon tower", "Route 16", "Route 17", "Route 18", "Safari Zone", "Route 12",
    "Route 13", "Route 14", "Route 15", "Sea Route 19", "Sea Route 20",
    "Seafoam Islands",
    "[pk] Mansion", "Route 21", "Route 23", "Victory Road", 'Static Pokemon'
]
routes_gsc = [
    "New Bark Town", "Route 29", "Cherrygrove City", "Route 30", "Route 31", "Violet City", "Sprout Tower",
    "Route 36", "Route 32", "Ruins of Alph", "Union Cave", "Route 33", "Slowpoke Well", "Ilex Forest",
    "Route 34", "Route 35", "National Park", "Route 36", "Route 37", "Ecruteak City", "Burned Tower",
    "Route 38", "Route 39", "Olivine City", "Route 40", "Route 41", "Cianwood City",
    "Route 42", "Mt.Mortar", "Route 43", "Lake of Rage",
    "Route 44", "Ice Path", "Blackthorn City", 'Dragon\'s Den', "Route 45", "Route 46",
    "Whirl Islands", "Route 27", "Tohjo Falls", "Route 26", "Victory Road", "Vermilion City", "Route 6", "Route 8",
    "Route 10", "Rock Tunnel", "Route 9", "Cerulean City", "Route 24", "Route 25", "Route 5", "Route 7",
    "Celadon City", "Route 16", "Route 17", "Route 18", "Fuchsia City", "Route 15", "Route 14", "Route 13",
    "Route 12", "Route 11", "Diglett\'s Cave", "Route 2", "Route 3", "Mt.Moon", "Route 4", "Viridian City",
    "Route 22", "Route 1", "Pallet Town", "Route 21", "Cinnabar Island", "Route 20",
    "Route 19", "Cerulean City", "Route 28", "Silver Cave", 'Static Pokemon'
]
routes_hgss = [
    "New Bark Town", "Route 29", "Cherrygrove City", "Route 30", "Route 31", "Violet City",
    "Sprout Tower",
    "Route 36", "Route 32", "Ruins of Alph", "Union Cave", "Route 33", "Slowpoke Well", "Ilex Forest",
    "Route 34", "Route 35", "National Park", "Route 36", "Route 37", "Ecruteak City", "Burned Tower",
    "Route 38", "Route 39", "Olivine City", "Route 40", "Route 41", "Cianwood City", "Cliff Edge Gate",
    "Cliff Cave", "Route 47", "Route 48", "Safari Zone", "Route 42", "Mt. Mortar", "Route 43",
    "Lake of Rage",
    "Route 44", "Ice Path", "Blackthorn City", 'Dragon’s Den', "Route 45", "Route 46", "Bell Tower",
    "Whirl Islands", "Route 27", "Tohjo Falls", "Route 26", "Victory Road", "Vermilion City", "Route 6", "Route 8",
    "Route 10", "Rock Tunnel", "Route 9", "Cerulean City", "Route 24", "Route 25", "Route 5", "Route 7",
    "Celadon City", "Route 16", "Route 17", "Route 18", "Fuchsia City", "Route 15", "Route 14", "Route 13",
    "Route 12", "Route 11", "Diglett’s Cave", "Route 2", "Route 3", "Mt. Moon", "Route 4", "Viridian City",
    "Route 22", "Route 1", "Pallet Town", "Route 21", "Cinnabar Island", "Route 20", "Seafoam Islands",
    "Route 19", "Cerulean City", "Route 28", "Mt. Silver", 'Static Pokemon'
]
routes_rse = [
    "Route 101", "Route 103", "Route 104", "Petalburg Woods", "Route 116", "Rusturf Tunnel",
    "Dewford",
    "Granite Cave", 'SLATEPORT', "Safari Zone", "Route 110", "Route 117",
    "Route 112", "Fiery Path", "Route 113", "Route 114", "Meteor Falls", "Jagged Pass",
    "Route 111", 'PETALBURG', "Route 118", "Route 119", 'LILYCOVE',
    "Route 120",
    "Route 121", "Route 122", "Mt. Pyre", "Route 123", 'MOSSDEEP',
    "Route 124", "Route 127", "Route 128", "Seafloor Cavern", "Route 126", "Cave of Origin",
    'SOOTOPOLIS', "Victory Road", "Route 129", "Route 130", "Route 131", "Route 132",
    "Route 133",
    "Route 134", "New Mauville", "Shoal Cave", "Abandoned Ship", 'Static Pokemon'
]
routes_frlg = [
    "Route 1 ", "Viridian City", "Route 22", "Route 2 ", "Viridian Forest", "Route 3", "Mt. Moon", "Route 4",
    "Cerulean City", "Route 24", "Route 25", "Route 5", "Route 6", "Vermilion City", "S.S. Anne", "Route 11",
    "Diglett’s Cave", "Route 9", "Route 10", "Rock Tunnel", "Route 8", "Route 7",
    "Celadon City", "Route 16", "Pokémon Tower", "Route 17", "Route 18", "Route 12", "Route 13", "Route 14",
    "Route 15", "Fuchsia City", "Safari Zone", "Route 21", "Route 19", "Route 20", "Seafoam Islands", "Cinnabar Island",
    "Pokémon Mansion", "One Island",
    "Cape Brink", "Berry Forest", "Bond Bridge", "Three Isle Port", "Power Plant", "Viridian City", "Route 23",
    "Victory Road", 'Static Pokemon'
]
routes_dpp = [
    "Route 201", "Route 202", "Lake Verity", "Route 203", "Oreburgh Gate", "Oreburgh Mine", "Route 204", "Ravaged Path",
    "Valley Windworks", "Route 205", "Eterna Forest", "Route 206", "Wayward Cave", "Route 207", "Mt. Coronet",
    "Route 208",
    "Route 209", "Solaceon Ruins", "Route 210", "Route 215", "Route 214", "Maniac Tunnel", "Route 212", "Trophy Garden",
    "Great Marsh", "Route 213", "Valor Lakefront", "Route 219", "Route 220", "Route 221", "Route 218", "Iron Island",
    "Lake Valor", "Route 211", "Route 216", "Route 217", "Acuity Lakefront", "Lake Acuity", "Sendoff Spring",
    "Route 222", "Route 223", "Victory Road", 'Static Pokemon'
]
routes_bw = [
    "Route 1", "Route 2", "Dreamyard", "Route 3", "Wellspring Cave", "Pinwheel Forest", "Route 4",
    "Desert Resort", "Relic Castle", "Route 5", "Driftveil Drawbridge", "Cold Storage", "Route 6", "Chargestone Cave",
    "Route 7", "Celestial Tower", "Route 17", "Route 18", "Twist Mountain", "Icirrus City", "Dragonspiral Tower",
    "Route 8", "Moor of Icirrus", "Route 9", "Route 10", "Victory Road", 'Static Pokemon'
]
routes_bw2 = [
    'Route 19', 'Route 20', 'Floccesy Ranch', 'Virbank Complex', 'Castelia Sewers', 'Route 4',
    'Desert Resort', 'Relic Castle', 'Route 16', 'Lostlorn Forest', 'Route 5', 'Driftveil Drawbridge', 'Relic Passage',
    'Route 6', 'Mistralton Cave', 'Chargestone Cave', 'Route 7', 'Celestial Tower', 'Strange House',
    'Reversal Mountain', 'Undella Bay', 'Route 13', 'Route 12', 'Village Bridge', 'Route 11', 'Route 9', 'Route 22',
    'Route 21', 'Seaside Cave', 'Giant Chasm', 'Route 23', 'Static Pokemon'
]
routes_oras = [
    "Map 023 - Route 101", "Map 025 - Route 103", "Map 024 - Route 102", "Map 013 - Petalburg City",
    "Map 026 - Route 104", "Map 082 - Petalburg Woods", "Map 027 - Route 104", "Map 043 - Route 116",
    "Map 075 - Rusturf Tunnel", "Map 008 - Dewford Town", "Map 029 - Route 106", "Map 078 - Granite Cave",
    "Map 079 - Granite Cave", "Map 080 - Granite Cave", "Map 032 - Route 109", "Map 014 - Slateport City",
    "Map 033 - Route 110", "Map 045 - Route 118", "Map 044 - Route 117", "Map 035 - Route 111", "Map 037 - Route 111",
    "Map 038 - Route 112", "Map 085 - Fiery Path", "Map 039 - Route 112", "Map 040 - Route 113", "Map 041 - Route 114",
    "Map 071 - Meteor Falls", "Map 072 - Meteor Falls", "Map 073 - Meteor Falls", "Map 074 - Meteor Falls",
    "Map 084 - Jagged Pass", "Map 052 - Route 123", "Map 046 - Route 119", "Map 047 - Route 119", "Map 048 - Route 120",
    "Map 049 - Route 120", "Map 164 - Scorched Slab", "Map 165 - Scorched Slab", "Map 166 - Scorched Slab",
    "Map 167 - Scorched Slab", "Map 050 - Route 121", "Map 219 - Safari Zone", "Map 220 - Safari Zone",
    "Map 221 - Safari Zone", "Map 222 - Safari Zone", "Map 018 - Lilycove City", "Map 051 - Route 122",
    "Map 086 - Mt. Pyre", "Map 087 - Mt. Pyre", "Map 088 - Mt. Pyre", "Map 089 - Mt. Pyre", "Map 090 - Mt. Pyre",
    "Map 091 - Mt. Pyre", "Map 169 - Team Magma Hideout", "Map 092 - Team Aqua Hideout", "Map 053 - Route 124",
    "Map 065 - Route 124", "Map 019 - Mossdeep City", "Map 056 - Route 127", "Map 057 - Route 128",
    "Map 068 - Route 128", "Map 099 - Seafloor Cavern", "Map 100 - Seafloor Cavern", "Map 101 - Seafloor Cavern",
    "Map 102 - Seafloor Cavern", "Map 103 - Seafloor Cavern", "Map 104 - Seafloor Cavern", "Map 105 - Seafloor Cavern",
    "Map 106 - Seafloor Cavern", "Map 107 - Seafloor Cavern", "Map 108 - Seafloor Cavern", "Map 109 - Seafloor Cavern",
    "Map 055 - Route 126", "Map 066 - Route 126", "Map 534 - Sootopolis City", "Map 112 - Cave of Origin",
    "Map 113 - Cave of Origin", "Map 114 - Cave of Origin", "Map 115 - Cave of Origin", "Map 116 - Cave of Origin",
    "Map 058 - Route 129", "Map 069 - Route 129", "Map 059 - Route 130", "Map 070 - Route 130", "Map 060 - Route 131",
    "Map 012 - Pacifidlog Town", "Map 061 - Route 132", "Map 062 - Route 133", "Map 063 - Route 134",
    "Map 162 - Sealed Chamber", "Map 028 - Route 105", "Map 145 - Sea Mauville", "Map 146 - Sea Mauville",
    "Map 151 - Sea Mauville", "Map 156 - Sea Mauville", "Map 139 - New Mauville", "Map 021 - Ever Grande City",
    "Map 123 - Victory Road", "Map 124 - Victory Road", "Map 125 - Victory Road", "Map 126 - Victory Road",
]
routes_xy = [
    "Map 259 - Route 2", "Map 286 - Santalune Forest", "Map 260 - Route 3", "Map 285 - Route 22", "Map 261 - Route 4",
    "Map 262 - Route 5", "Map 334 - Connecting Cave", "Map 266 - Route 8",
    "Map 267 - Route 9", "Map 303 - Glittering Cave", "Map 304 - Glittering Cave", "Map 268 - Route 10",
    "Map 269 - Route 11", "Map 305 - Reflection Cave", "Map 306 - Reflection Cave", "Map 307 - Reflection Cave",
    "Map 308 - Reflection Cave", "Map 270 - Route 12", "Map 357 - Azure Bay", "Map 272 - Route 13",
    "Map 273 - Route 14", "Map 200 - Laverre City", "Map 275 - Route 15",
    "Map 349 - Lost Hotel", "Map 276 - Route 16", "Map 313 - Frost Cavern", "Map 314 - Frost Cavern",
    "Map 315 - Frost Cavern", "Map 316 - Frost Cavern", "Map 317 - Frost Cavern", "Map 278 - Route 17",
    "Map 279 - Route 18", "Map 343 - Terminus Cave", "Map 344 - Terminus Cave", "Map 345 - Terminus Cave",
    "Map 347 - Terminus Cave", "Map 348 - Terminus Cave", "Map 281 - Route 19", "Map 282 - Route 20",
    "Map 318 - Pokémon Village", "Map 283 - Route 21", "Map 322 - Victory Road", "Map 324 - Victory Road",
    "Map 326 - Victory Road", "Map 327 - Victory Road", "Map 328 - Victory Road",
]
routes_usm = [
    "Map: 000 - Route 1 (Hau’oli Outskirts) / 003 - Route 1 / 010 - Melemele Sea",
    "Map: 001 - Route 1 (Hau’oli Outskirts) / 005 - Route 1", "Map: 006 - Route 3 / 008 - Kala’e Bay",
    "Map: 007 - Route 2", "Map: 009 - Melemele Sea / 012 - Hau’oli City (Beachfront)",
    "Map: 013 - Hau’oli City (Shopping District) / 014 - Hau’oli City (Marina)", "Map: 026 - Ten Carat Hill",
    "Map: 027 - Ten Carat Hill (Farthest Hollow)", "Map: 028 - Hau’oli Cemetery", "Map: 029 - Melemele Meadow",
    "Map: 030 - Seaward Cave", "Map: 031 - Berry Fields", "Map: 032 - Sandy Cave",
    "Map: 033 - Verdant Cavern (Trial Site)", "Map: 062 - Route 1 (Trainers’ School)", "Map: 080 - Route 4",
    "Map: 081 - Route 5", "Map: 082 - Route 6", "Map: 083 - Route 7", "Map: 084 - Route 8",
    "Map: 085 - Route 9", "Map: 086 - Hano Grand Resort / 087 - Hano Beach", "Map: 089 - Paniola Town",
    "Map: 093 - Dividing Peak Tunnel", "Map: 097 - Memorial Hill / 098 - Akala Outskirts",
    "Map: 099 - Diglett.s Tunnel", "Map: 100 - Wela Volcano Park",
    "Map: 102 - Brooklet Hill / 103 - Brooklet Hill", "Map: 104 - Brooklet Hill (Totem’s Den)",
    "Map: 105 - Lush Jungle", "Map: 106 - Lush Jungle", "Map: 107 - Lush Jungle", "Map: 109 - Lush Jungle",
    "Map: 150 - Paniola Ranch", "Map: 151 - Paniola Ranch", "Map: 164 - Route 10", "Map: 165 - Route 11",
    "Map: 166 - Ula’ula Beach", "Map: 167 - Route 13", "Map: 168 - Tapu Village / 169 - Route 14",
    "Map: 170 - Route 15 / 171 - Route 16", "Map: 172 - Route 17", "Map: 173 - Route 12",
    "Map: 174 - Malie City / 175 - Malie City (Outer Cape)",
    "Map: 177 - Haina Desert / 178 - Haina Desert / 179 - Haina Desert / 180 - Haina Desert",
    "Map: 181 - Haina Desert / 182 - Haina Desert / 183 - Haina Desert / 184 - Haina Desert",
    "Map: 185 - Ula’ula Meadow", "Map: 186 - Malie Garden", "Map: 187 - Mount Hokulani",
    "Map: 188 - Blush Mountain", "Map: 189 - Ruins of Abundance", "Map: 200 - Mount Lanakila",
    "Map: 201 - Mount Lanakila", "Map: 202 - Mount Lanakila", "Map: 204 - Mount Lanakila",
    "Map: 205 - Mount Lanakila", "Map: 206 - Mount Lanakila", "Map: 222 - Thrifty Megamart (Abandoned Site)",
    "Map: 264 - Poni Wilds", "Map: 265 - Ancient Poni Path / 266 - Poni Breaker Coast",
    "Map: 267 - Poni Grove", "Map: 268 - Poni Plains", "Map: 269 - Poni Coast", "Map: 270 - Poni Gauntlet",
    "Map: 272 - Seafolk Village", "Map: 273 - Poni Meadow", "Map: 274 - Vast Poni Canyon",
    "Map: 275 - Vast Poni Canyon", "Map: 276 - Vast Poni Canyon", "Map: 277 - Vast Poni Canyon",
    "Map: 278 - Vast Poni Canyon", "Map: 287 - Resolution Cave", "Map: 288 - Resolution Cave",
    "Map: 290 - Exeggutor Island",
]
routes_sm = [
    "Map: 000 - Route 1 (Hau’oli Outskirts) / 001 - Route 1 / 006 - Melemele Sea",
    "Map: 053 - Route 1 (Hau’oli Outskirts)", "Map: 002 - Route 3 / 004 - Kala’e Bay",
    "Map: 007 - Route 2", "Map: 005 - Melemele Sea / 007 - Hau’oli City (Beachfront)",
    "Map: 008 - Hau’oli City (Shopping District) / 009 - Hau’oli City (Marina)", "Map: 018 - Ten Carat Hill",
    "Map: 019 - Ten Carat Hill (Farthest Hollow)", "Map: 020 - Hau’oli Cemetery", "Map: 021 - Melemele Meadow",
    "Map: 022 - Seaward Cave", "Map: 023 - Berry Fields",
    "Map: 024 - Verdant Cavern (Trial Site)", "Map: 068 - Route 4",
    "Map: 069 - Route 5", "Map: 070 - Route 6", "Map: 71 - Route 7", "Map: 072 - Route 8",
    "Map: 073 - Route 9", "Map: 074 - Hano Grand Resort / 075 - Hano Beach", "Map: 76 - Paniola Town",
    "Map: 083 - Memorial Hill / 084 - Akala Outskirts",
    "Map: 085 - Diglett’s Tunnel", "Map: 086 - Wela Volcano Park",
    "Map: 088 - Brooklet Hill / 089 - Brooklet Hill", "Map: 90 - Brooklet Hill (Totem’s Den)",
    "Map: 091 - Lush Jungle", "Map: 92 - Lush Jungle", "Map: 093 - Lush Jungle", "Map: 095 - Lush Jungle",
    "Map: 076 - Paniola Town", "Map: 131 - Paniola Ranch", "Map: 132 - Paniola Ranch", "Map: 140 - Route 10",
    "Map: 141 - Route 11",
    "Map: 143 - Route 13", "Map: 144 - Tapu Village / 145 - Route 14",
    "Map: 146 - Route 15 / 147 - Route 16", "Map: 147 - Route 17", "Map: 142 - Secluded Shore / 149 - Route 12",
    "Map: 150 - Malie City / 151 - Malie City (Outer Cape)",
    "Map: 153 - Haina Desert / 154 - Haina Desert / 155 - Haina Desert / 156 - Haina Desert",
    "Map: 157 - Haina Desert / 158 - Haina Desert / 159 - Haina Desert / 160 - Haina Desert",
    "Map: 161 - Ula’ula Meadow", "Map: 162 - Malie Garden", "Map: 163 - Mount Hokulani",
    "Map: 164 - Blush Mountain", "Map: 165 - Ruins of Abundance", "Map: 177 - Mount Lanakila",
    "Map: 178 - Mount Lanakila", "Map: 180 - Mount Lanakila",
    "Map: 194 - Thrifty Megamart (Abandoned Site)",
    "Map: 231 - Poni Wilds", "Map: 232 - Ancient Poni Path / 233 - Poni Breaker Coast",
    "Map: 234 - Poni Grove", "Map: 235 - Poni Plains", "Map: 236 - Poni Coast", "Map: 237 - Poni Gauntlet",
    "Map: 238 - Seafolk Village", "Map: 239 - Poni Meadow", "Map: 240 - Vast Poni Canyon",
    "Map: 241 - Vast Poni Canyon", "Map: 242 - Vast Poni Canyon", "Map: 243 - Vast Poni Canyon",
    "Map: 244 - Vast Poni Canyon", "Map: 253 - Resolution Cave", "Map: 254 - Resolution Cave",
    "Map: 255 - Exeggutor Island",
]
routelist = []
#######################################
# --------------------------------------
#######################################
# Functions


# Ensure proper game title


# Ensure proper type


SETTINGS_FILE = os.path.join(os.path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'output_log_folder': None, 'default game': 'Red', 'theme': sg.theme(), 'default type': 'Bug'}
# "Map" from the settings dictionary keys to the window's element keys
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'output_log_folder': '-OUTPUT FOLDER-', 'default game': '-GAME-', 'theme': '-THEME-',
                                 'default type': '-PKTYPE-'}


##################### Load/Save Settings File #####################
def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True,
                               background_color='white', text_color='black')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:  # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')


##################### Make a settings window #####################
def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text):
        return sg.Text(text + ':', justification='r', )

    layout = [[sg.Text('Settings', font='Any 15')],
              [TextLabel('Default Output Folder'), sg.Input(key='-OUTPUT FOLDER-'),
               sg.FolderBrowse(target='-OUTPUT FOLDER-')],
              [TextLabel('Default Pokémon Game'), sg.Combo(game_list, key='-GAME-')],
              [TextLabel('Default Pokémon Type'), sg.Combo(pkmntype_list, key='-PKTYPE-')],
              [TextLabel('Theme'), sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
              [sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


##################### Main Program Window & Event Loop #####################
def create_main_window(settings):
    # ------ Menu Definition ------ #
    menu_def = [['File', ['Settings', 'Exit']],
                ['Help', 'About...'], ]

    sg.theme(settings['theme'])

    layout = [[sg.Menu(menu_def, )],
              [sg.Text('Progress'), sg.ProgressBar(len(routelist), orientation='h', size=(40, 20), key='progbar'),
               sg.Checkbox('Gen Restriction?', tooltip='Use this only if '
                                                       'you\'re playing a '
                                                       'remake with generation '
                                                       'restrictions\n(Ex: '
                                                       'Omega Ruby with Gen 3 '
                                                       'only)\nThis is only for '
                                                       'generating starters',
                           key='checkbox',
                           enable_events=True),
               ],
              [sg.Text('Pokémon Type'), sg.Combo(pkmntype_list, default_value=settings['default type'], key='-PKTYPE-'),
               sg.Text('Game'), sg.Combo(game_list, default_value=settings['default game'], key='-GAME-'),
               sg.B('Run'), sg.B('Choose Starters'),
               sg.Combo(generation_list, visible=False, key='-GENLIST-', default_value=''),
               ],
              [sg.Text('Output Folder'), sg.Input(default_text=settings['output_log_folder'], key='-OUTPUT FOLDER-'),
               sg.FolderBrowse(target='-OUTPUT FOLDER-'),
               sg.Text('Starters Output', pad=(60, 0), justification='center')],
              [sg.Text('Open Log'), sg.Input(key='-LOG-', default_text='Select Log File To Check'), sg.FileBrowse(),
               sg.Output((35, 1))],

              ]

    return sg.Window('Monolocke Text Parser', layout)


def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS)
    while True:  # Event Loop
        if window is None:
            window = create_main_window(settings)

        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'checkbox' and values['checkbox']:
            game = values['-GAME-']
            game_gen = ''
            if game in ["Red", "Blue", "Yellow"]:
                game_gen = 'Generation 1'
            elif game in ["Gold", "Silver", "Crystal"]:
                game_gen = 'Generation 2'
            elif game in ["Ruby", "Sapphire", "Emerald", "FireRed", "LeafGreen"]:
                game_gen = 'Generation 3'
            elif game in ["Diamond", "Pearl", "Platinum", "HeartGold", "SoulSilver"]:
                game_gen = 'Generation 4'
            elif game in ["Black", "White", "Black 2", "White 2"]:
                game_gen = 'Generation 5'
            elif game in ["X", "Y", "Omega Ruby", "Alpha Sapphire"]:
                game_gen = 'Generation 6'
            elif game in ["Sun", "Moon", "Ultra Sun", "Ultra Moon"]:
                game_gen = 'Generation 7'

            window.Element('-GENLIST-').Update(visible=True, value=game_gen)
        if event == 'checkbox' and not values['checkbox']:
            window.Element('-GENLIST-').Update(visible=False)
        if event == 'About...':
            sg.popup('About this program', 'Version 1.0', 'Outputs a log of Pokémon locations without revealing names',
                     'Also can help choose starters for your selected type with 3 evolutions'
                     )
        if event == 'Choose Starters':
            game = values['-GAME-']
            pkmntype = values['-PKTYPE-']
            game_gen = ''
            if not values['checkbox']:
                if game in ["Red", "Blue", "Yellow"]:
                    game_gen = 'Generation 1'
                elif game in ["Gold", "Silver", "Crystal"]:
                    game_gen = 'Generation 2'
                elif game in ["Ruby", "Sapphire", "Emerald", "FireRed", "LeafGreen"]:
                    game_gen = 'Generation 3'
                elif game in ["Diamond", "Pearl", "Platinum", "HeartGold", "SoulSilver"]:
                    game_gen = 'Generation 4'
                elif game in ["Black", "White", "Black 2", "White 2"]:
                    game_gen = 'Generation 5'
                elif game in ["X", "Y", "Omega Ruby", "Alpha Sapphire"]:
                    game_gen = 'Generation 6'
                elif game in ["Sun", "Moon", "Ultra Sun", "Ultra Moon"]:
                    game_gen = 'Generation 7'
            else:
                game_gen = values['-GENLIST-']
            gen_list = generations_dict.get(game_gen)
            pkmn_list = type_list[pkmntype.lower()]
            i = 0
            count = 0
            starter = random.sample(gen_list, k=3)
            while i < 1:
                if any(mon in starter for mon in pkmn_list):
                    i += 1
                    print(f'{starter[0]}, {starter[1]}, {starter[2]}')
                elif count == 100:
                    i += 1
                    print("Not in generation")
                else:
                    starter.clear()
                    starter = random.sample(gen_list, k=3)
                    count += 1
        if event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)
        if event == 'Run':
            game = values['-GAME-']
            pkmntype = values['-PKTYPE-']
            pkmn_list = type_list[pkmntype.lower()]
            f = 'none'
            try:
                filename = "%s/%s/%s-%s.txt" % (values['-OUTPUT FOLDER-'], game, game, pkmntype)
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                f = open(filename, "w+")
            except PermissionError:
                sg.popup('Select an Output folder for your logs')
            if game in ["Red", "Blue", "Yellow"]:
                routelist = routes_rby
            elif game in ["Gold", "Silver", "Crystal"]:
                routelist = routes_gsc
            elif game in ["Ruby", "Sapphire", "Emerald"]:
                routelist = routes_rse
            elif game in ["FireRed", "LeafGreen"]:
                routelist = routes_frlg
            elif game in ["Diamond", "Pearl", "Platinum"]:
                routelist = routes_dpp
            elif game in ["HeartGold", "SoulSilver"]:
                routelist = routes_hgss
            elif game in ["Black", "White"]:
                routelist = routes_bw
            elif game in ["Black 2", "White 2"]:
                routelist = routes_bw2
            elif game in ["X", "Y"]:
                routelist = routes_xy
            elif game in ["Omega Ruby", "Alpha Sapphire"]:
                routelist = routes_oras
            elif game in ["Sun", "Moon", ]:
                routelist = routes_sm
            elif game in ["Ultra Sun", "Ultra Moon", ]:
                routelist = routes_usm

            def remove_values_from_list(the_list, val):
                return [value for value in the_list if value != val]

            # Functions for Red, Blue and Yellow logs
            def extr_enc_rby(string):
                level = ""

                clipped_string = string[string.find(") - ") + 4:]

                capital_string = stringfunc.capwords(clipped_string)

                enclist = re.findall(r'[A-z]{3,20}', capital_string)

                raritylist = []

                raritynumbers = []

                for mon in enclist:
                    if mon in pkmn_list:
                        raritylist.append(mon)
                        raritynumbers.append(str(enclist.index(mon) + 1) + "/" + str(len(enclist)))
                if len(raritylist) == 0:
                    return

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                if len(raritylist) == 0:
                    hastype = "NO"
                else:
                    hastype = "YES"

                fishing_percent = []

                walking_percent = []

                floors = [
                    # B1
                    ['ROCK TUNNEL (3)', 'MT.MOON (2)', 'SEAFOAM ISLANDS (2)'],
                    # B2
                    ['MT.MOON (3)', 'SEAFOAM ISLANDS (3)'],
                    # B3
                    ['SEAFOAM ISLANDS (4)'],
                    # B4
                    ['SEAFOAM ISLANDS (5)'],
                    # F1
                    ['MT.MOON (1)', 'VICTORY ROAD (1)', '[PK] MANSION (1)', 'CERULEAN CAVE (1)', 'SEAFOAM ISLANDS (1)'],
                    # F2
                    ['ROCK TUNNEL (3)', 'VICTORY ROAD (2)', '[PK] MANSION (2)', 'CERULEAN CAVE (2)',
                     '[PK] MANSION (2)'],
                    # F3
                    ['VICTORY ROAD (3)', '[POKÉ]MON TOWER (3)', '[PK] MANSION (3)'],
                    # F4
                    ['[POKÉ]MON TOWER (4)', '[PK] MANSION (4)'],
                    # F5
                    ['[POKÉ]MON TOWER (5)'],
                    # F6
                    ['[POKÉ]MON TOWER (6)'],
                    # F7
                    ['[POKÉ]MON TOWER (7)'],
                    # Zone 2
                    ['SAFARI ZONE (2)'],
                    # Zone 3
                    ['SAFARI ZONE (3)'],
                    # Zone 4
                    ['SAFARI ZONE (4)'],
                    # Zone 5
                    ['SAFARI ZONE (5)'],
                ]

                for x in floors:
                    for y in x:
                        if y in string:
                            if floors.index(x) == 0:
                                level = "B1F - "
                            elif floors.index(x) == 1:
                                level = "B2F - "
                            elif floors.index(x) == 2:
                                level = "B3F - "
                            elif floors.index(x) == 3:
                                level = "B4F - "
                            elif floors.index(x) == 4 and 'Route 23 ' not in string:
                                level = "1F - "
                            elif floors.index(x) == 5 and 'Route 23 ' not in string:
                                level = "2F - "
                            elif floors.index(x) == 6:
                                level = "3F - "
                            elif floors.index(x) == 7:
                                level = "4F - "
                            elif floors.index(x) == 8:
                                level = "5F - "
                            elif floors.index(x) == 9:
                                level = "6F - "
                            elif floors.index(x) == 10:
                                level = "7F - "
                            elif floors.index(x) == 11:
                                level = "Zone 2 - "
                            elif floors.index(x) == 12:
                                level = "Zone 3 - "
                            elif floors.index(x) == 13:
                                level = "Zone 4 - "
                            elif floors.index(x) == 14:
                                level = "Zone 5 - "

                if "Grass/Cave" in string or "Surfing" in string:
                    for x in raritynumbers:
                        if x in ["1/10", "2/10"]:
                            walking_percent.append("20%")
                        elif x in ["3/10"]:
                            walking_percent.append("15%")
                        elif x in ["4/10", "5/10", "6/10"]:
                            walking_percent.append("10%")
                        elif x in ["7/10", "8/10"]:
                            walking_percent.append("5%")
                        elif x in ["9/10"]:
                            walking_percent.append("4%")
                        elif x in ["10/10"]:
                            walking_percent.append("1%")

                elif "Old Rod" in string or "Good Rod" in string or "Super Rod" in string or "Fishing" in string:
                    for x in raritynumbers:
                        if x in ["1/1"]:
                            fishing_percent.append("100%")
                        elif x in ["2/2", "1/2"]:
                            fishing_percent.append('50%')
                        elif x in ["1/4", "2/4", "3/4", "4/4"]:
                            fishing_percent.append("25%")

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(level + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Surfing" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Old Rod" in string:
                        f.write(level + "Old Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Good Rod" in string:
                        f.write(level + "Good Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Super Rod" in string:
                        f.write(level + "Super Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Fishing" in string:
                        f.write(level + "Fishing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

            # Functions for FireRed and LeafGreen logs
            def extr_enc_frlg(string):
                level = ""

                clipped_string = string[string.find(") - ") + 4:]

                capital_string = stringfunc.capwords(clipped_string)

                enclist = re.findall(r'[A-z]{3,20}|Ho-Oh', capital_string)
                enclist = remove_values_from_list(enclist, 'Lvs')

                raritylist = []

                raritynumbers = []

                for mon in enclist:
                    if mon in pkmn_list and mon != 'Lvs':
                        raritylist.append(mon)
                        raritynumbers.append(str(enclist.index(mon) + 1) + "/" + str(len(enclist)))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                if len(raritylist) == 0:
                    return
                else:
                    hastype = "YES"

                floors = [
                    # B1
                    ['Set #10 - MT. MOON', 'Set #16 - VICTORY ROAD', 'Set #48 - SEAFOAM ISLANDS',
                     'Set #21 - POKéMON MANSION', ],
                    # B2
                    ['Set #11 - MT. MOON', 'Set #17 - VICTORY ROAD', 'Set #49 - SEAFOAM ISLANDS', ],
                    # B3
                    ['Set #50 - SEAFOAM ISLANDS', 'Set #51 - SEAFOAM ISLANDS', 'Set #52 - SEAFOAM ISLANDS', ],
                    # B4
                    ['Set #53 - SEAFOAM ISLANDS', 'Set #54 - SEAFOAM ISLANDS', 'Set #55 - SEAFOAM ISLANDS', ],
                    # F1
                    ['Set #9 - MT. MOON', 'Set #15 - VICTORY ROAD', 'Set #47 - SEAFOAM ISLANDS',
                     'Set #18 - POKéMON MANSION', ],
                    # F2
                    ['Set #19 - POKéMON MANSION', ],
                    # F3
                    ['Set #56 - POKéMON TOWER', 'Set #20 - POKéMON MANSION', ],
                    # F4
                    ['Set #57 - POKéMON TOWER', ],
                    # F5
                    ['Set #58 - POKéMON TOWER', ],
                    # F6
                    ['Set #59 - POKéMON TOWER', ],
                    # F7
                    ['Set #60 - POKéMON TOWER', ],
                    # Summit
                    [],
                    # East
                    ['Set #25 - SAFARI ZONE', 'Set #26 - SAFARI ZONE', 'Set #27 - SAFARI ZONE', ],
                    # North
                    ['Set #28 - SAFARI ZONE', 'Set #29 - SAFARI ZONE', 'Set #30 - SAFARI ZONE', ],
                    # South
                    ['Set #22 - SAFARI ZONE', 'Set #23 - SAFARI ZONE', 'Set #24 - SAFARI ZONE', ],
                    # West
                    ['Set #31 - SAFARI ZONE', 'Set #32 - SAFARI ZONE', 'Set #33 - SAFARI ZONE', ],
                ]
                for x in floors:
                    for y in x:
                        if y in string:
                            if floors.index(x) == 0:
                                level = "B1F - "
                            elif floors.index(x) == 1:
                                level = "B2F - "
                            elif floors.index(x) == 2:
                                level = "B3F - "
                            elif floors.index(x) == 3:
                                level = "B4F - "
                            elif floors.index(x) == 4:
                                level = "1F - "
                            elif floors.index(x) == 5:
                                level = "2F - "
                            elif floors.index(x) == 6:
                                level = "3F - "
                            elif floors.index(x) == 7:
                                level = "4F - "
                            elif floors.index(x) == 8:
                                level = "5F - "
                            elif floors.index(x) == 9:
                                level = "6F - "
                            elif floors.index(x) == 10:
                                level = "7F - "
                            elif floors.index(x) == 11:
                                level = "Summit - "
                            elif floors.index(x) == 12:
                                level = "East - "
                            elif floors.index(x) == 13:
                                level = "North-West - "
                            elif floors.index(x) == 14:
                                level = "South-East - "
                            elif floors.index(x) == 15:
                                level = "South-West - "
                            elif floors.index(x) == 16:
                                level = "1F-2 - "
                            elif floors.index(x) == 17:
                                level = "1F-3 - "
                            elif floors.index(x) == 18:
                                level = "B1F-2 - "
                            elif floors.index(x) == 19:
                                level = "Inner Room - "
                            elif floors.index(x) == 20:
                                level = "Stairs Room - "
                            elif floors.index(x) == 21:
                                level = "Lower Room - "
                            elif floors.index(x) == 22:
                                level = "Ice Room - "

                fishing_percent = []

                surfing_percent = []

                rock_smash_percent = []

                walking_percent = []

                if "Grass/Cave" in string:
                    for x in raritynumbers:
                        if x in ["1/12", "2/12"]:
                            walking_percent.append("20%")
                        elif x in ["3/12", "4/12", "5/12", "6/12"]:
                            walking_percent.append("10%")
                        elif x in ["7/12", "8/12"]:
                            walking_percent.append("5%")
                        elif x in ["9/12", "10/12"]:
                            walking_percent.append("4%")
                        elif x in ["11/12", "12/12"]:
                            walking_percent.append("1%")

                elif "Surfing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            surfing_percent.append("60%")
                        elif x == "2/5":
                            surfing_percent.append('30%')
                        elif x == "3/5":
                            surfing_percent.append("5%")
                        elif x == "4/5":
                            surfing_percent.append("4%")
                        elif x == "5/5":
                            surfing_percent.append("1%")

                elif "Fishing" in string:
                    for x in raritynumbers:
                        if x == "1/10":
                            fishing_percent.append("70%")
                        elif x == "2/10":
                            fishing_percent.append('30%')
                        elif x == "3/10":
                            fishing_percent.append("60%")
                        elif x == "4/10":
                            fishing_percent.append("20%")
                        elif x == "5/10":
                            fishing_percent.append("20%")
                        elif x == "6/10":
                            fishing_percent.append("40%")
                        elif x == "7/10":
                            fishing_percent.append("40%")
                        elif x == "8/10":
                            fishing_percent.append("15%")
                        elif x == "9/10":
                            fishing_percent.append("4%")
                        elif x == "10/10":
                            fishing_percent.append("1%")

                if "Rock Smash" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            rock_smash_percent.append("60%")
                        elif x == "2/5":
                            rock_smash_percent.append("30%")
                        elif x == "3/5":
                            rock_smash_percent.append("5%")
                        elif x == "4/5":
                            rock_smash_percent.append("4%")
                        elif x == "5/5":
                            rock_smash_percent.append("1%")

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(level + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Surfing" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            surfing_percent) + "\n")

                    elif "Fishing" in string:
                        f.write(level + "Fishing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Rock Smash" in string:
                        f.write(level + "Rock Smash" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            rock_smash_percent) + "\n")

            # Functions for Ruby, Sapphire and Emerald logs
            def extr_enc_rse(string):
                level = ""

                clipped_string = string[string.find(") - ") + 4:]

                capital_string = stringfunc.capwords(clipped_string)

                enclist = re.findall(r'[A-z]{3,20}|Ho-Oh', capital_string)
                enclist = remove_values_from_list(enclist, 'Lvs')

                raritylist = []

                raritynumbers = []

                for mon in enclist:
                    if mon in pkmn_list and mon != 'Lvs':
                        raritylist.append(mon)
                        raritynumbers.append(str(enclist.index(mon) + 1) + "/" + str(len(enclist)))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                if len(raritylist) == 0:
                    return
                else:
                    hastype = "YES"

                floors = [
                    # B1
                    ['Set #27 - GRANITE CAVE', 'Set #38 - GRANITE CAVE', 'Set #19 - METEOR FALLS',
                     'Set #20 - METEOR FALLS',
                     'Set #21 - METEOR FALLS', 'Set #148 - METEOR FALLS', 'Set #149 - METEOR FALLS',
                     'Set #150 - METEOR FALLS',
                     'Set #58 - CAVE OF ORIGIN', 'Set #62 - VICTORY ROAD', 'Set #63 - VICTORY ROAD',
                     'Set #137 - VICTORY ROAD',
                     'Set #138 - VICTORY ROAD', 'Set #63 - NEW MAUVILLE', ],
                    # B2
                    ['Set #28 - GRANITE CAVE', 'Set #30 - GRANITE CAVE', 'Set #45 - GRANITE CAVE',
                     'Set #46 - GRANITE CAVE',
                     'Set #59 - CAVE OF ORIGIN', 'Set #64 - VICTORY ROAD',
                     'Set #65 - VICTORY ROAD', 'Set #66 - VICTORY ROAD', 'Set #139 - VICTORY ROAD',
                     'Set #140 - VICTORY ROAD',
                     'Set #141 - VICTORY ROAD', ],
                    # B3
                    ['Set #60 - CAVE OF ORIGIN', ],
                    # Entrance
                    ['Set #56 - CAVE OF ORIGIN', 'Set #76 - NEW MAUVILLE', 'Set #67 - SHOAL CAVE Grass/Cave',
                     'Set #68 - SHOAL CAVE Surfing', 'Set #69 - SHOAL CAVE Fishing', 'Set #153 - SHOAL CAVE',
                     'Set #154 - SHOAL CAVE', 'Set #155 - SHOAL CAVE', ],
                    # F1
                    ['Set #26 - GRANITE CAVE', 'Set #37 - GRANITE CAVE', 'Set #13 - METEOR FALLS',
                     'Set #14 - METEOR FALLS',
                     'Set #15 - METEOR FALLS', 'Set #142 - METEOR FALLS', 'Set #143 - METEOR FALLS',
                     'Set #144 - METEOR FALLS',
                     'Set #34 - MT. PYRE', 'Set #39 - MT. PYRE', 'Set #57 - CAVE OF ORIGIN', 'Set #61 - VICTORY ROAD',
                     'Set #77 - NEW MAUVILLE',
                     'Set #40 - VICTORY ROAD', 'Set #128 - NEW MAUVILLE', ],
                    # F2
                    ['Set #35 - MT. PYRE', 'Set #78 - MT. PYRE', ],
                    # F3
                    ['Set #36 - MT. PYRE', 'Set #79 - MT. PYRE', ],
                    # F4
                    ['Set #37 - MT. PYRE', 'Set #80 - MT. PYRE', ],
                    # F5
                    ['Set #38 - MT. PYRE', 'Set #81 - MT. PYRE', ],
                    # F6
                    ['Set #39 - MT. PYRE', 'Set #82 - MT. PYR', ],
                    # Outside
                    ['Set #40 - MT. PYRE', 'Set #83 - MT. PYRE', ],
                    # Summit
                    ['Set #41 - MT. PYRE', 'Set #84 - MT. PYRE', ],
                    # North-East
                    ['Set #168 - SAFARI ZONE', 'Set #169 - SAFARI ZONE', ],
                    # North-West
                    ['Set #165 - SAFARI ZONE', 'Set #166 - SAFARI ZONE', 'Set #167 - SAFARI ZONE', ],
                    # South-East
                    ['Set #173 - SAFARI ZONE', ],
                    # South-West
                    ['Set #170 - SAFARI ZONE', 'Set #171 - SAFARI ZONE', 'Set #172 - SAFARI ZONE', ],
                    # 1F-2
                    ['Set #30 - GRANITE CAVE', 'Set #85 - GRANITE CAVE', 'Set #16 - METEOR FALLS',
                     'Set #17 - METEOR FALLS',
                     'Set #18 - METEOR FALLS', 'Set #145 - METEOR FALLS', 'Set #146 - METEOR FALLS',
                     'Set #147 - METEOR FALLS', ],
                    # 1F-3
                    ['Set #209 - METEOR FALLS', ],
                    # BF1-2
                    ['Set #22 - METEOR FALLS', 'Set #23 - METEOR FALLS', 'Set #24 - METEOR FALLS',
                     'Set #48 - METEOR FALLS',
                     'Set #49 - METEOR FALLS', 'Set #50 - METEOR FALLS', ],
                    # Inner Room
                    ['Set #70 - SHOAL CAVE', 'Set #71 - SHOAL CAVE', 'Set #72 - SHOAL CAVE', 'Set #156 - SHOAL CAVE',
                     'Set #157 - SHOAL CAVE', 'Set #158 - SHOAL CAVE', ],
                    # Stairs Room
                    ['Set #73 - SHOAL CAVE', 'Set #151 - SHOAL CAVE', ],
                    # Lower Room
                    ['Set #74 - SHOAL CAVE', 'Set #152 - SHOAL CAVE', ],
                    # Ice Room
                    ['Set #75 - SHOAL CAVE', 'Set #174 - SHOAL CAVE', ],
                ]
                for x in floors:
                    for y in x:
                        if y in string:
                            if floors.index(x) == 0:
                                level = "B1F - "
                            elif floors.index(x) == 1:
                                level = "B2F - "
                            elif floors.index(x) == 2:
                                level = "B3F - "
                            elif floors.index(x) == 3:
                                level = "Entrance - "
                            elif floors.index(x) == 4:
                                level = "1F - "
                            elif floors.index(x) == 5:
                                level = "2F - "
                            elif floors.index(x) == 6:
                                level = "3F - "
                            elif floors.index(x) == 7:
                                level = "4F - "
                            elif floors.index(x) == 8:
                                level = "5F - "
                            elif floors.index(x) == 9:
                                level = "6F - "
                            elif floors.index(x) == 10:
                                level = "Outside - "
                            elif floors.index(x) == 11:
                                level = "Summit - "
                            elif floors.index(x) == 12:
                                level = "North-East - "
                            elif floors.index(x) == 13:
                                level = "North-West - "
                            elif floors.index(x) == 14:
                                level = "South-East - "
                            elif floors.index(x) == 15:
                                level = "South-West - "
                            elif floors.index(x) == 16:
                                level = "1F-2 - "
                            elif floors.index(x) == 17:
                                level = "1F-3 - "
                            elif floors.index(x) == 18:
                                level = "BF1-2 - "
                            elif floors.index(x) == 19:
                                level = "Inner Room - "
                            elif floors.index(x) == 20:
                                level = "Stairs Room - "
                            elif floors.index(x) == 21:
                                level = "Lower Room - "
                            elif floors.index(x) == 22:
                                level = "Ice Room - "

                fishing_percent = []

                surfing_percent = []

                rock_smash_percent = []

                walking_percent = []

                if "Grass/Cave" in string:
                    for x in raritynumbers:
                        if x in ["1/12", "2/12"]:
                            walking_percent.append("20%")
                        elif x in ["3/12", "4/12", "5/12", "6/12"]:
                            walking_percent.append("10%")
                        elif x in ["7/12", "8/12"]:
                            walking_percent.append("5%")
                        elif x in ["9/12", "10/12"]:
                            walking_percent.append("4%")
                        elif x in ["11/12", "12/12"]:
                            walking_percent.append("1%")

                elif "Surfing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            surfing_percent.append("60%")
                        elif x == "2/5":
                            surfing_percent.append('30%')
                        elif x == "3/5":
                            surfing_percent.append("5%")
                        elif x == "4/5":
                            surfing_percent.append("4%")
                        elif x == "5/5":
                            surfing_percent.append("1%")

                elif "Fishing" in string:
                    for x in raritynumbers:
                        if x == "1/10":
                            fishing_percent.append("70%")
                        elif x == "2/10":
                            fishing_percent.append('30%')
                        elif x == "3/10":
                            fishing_percent.append("60%")
                        elif x == "4/10":
                            fishing_percent.append("20%")
                        elif x == "5/10":
                            fishing_percent.append("20%")
                        elif x == "6/10":
                            fishing_percent.append("40%")
                        elif x == "7/10":
                            fishing_percent.append("40%")
                        elif x == "8/10":
                            fishing_percent.append("15%")
                        elif x == "9/10":
                            fishing_percent.append("4%")
                        elif x == "10/10":
                            fishing_percent.append("1%")

                if "Rock Smash" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            rock_smash_percent.append("60%")
                        elif x == "2/5":
                            rock_smash_percent.append("30%")
                        elif x == "3/5":
                            rock_smash_percent.append("5%")
                        elif x == "4/5":
                            rock_smash_percent.append("4%")
                        elif x == "5/5":
                            rock_smash_percent.append("1%")

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(level + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Surfing" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            surfing_percent) + "\n")

                    elif "Fishing" in string:
                        f.write(level + "Fishing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Rock Smash" in string:
                        f.write(level + "Rock Smash" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            rock_smash_percent) + "\n")

            # Functions for HeartGold and SoulSilver logs
            def extr_enc_hgss(string):
                clipped_string = string[string.find(") - ") + 4:]

                capital_string = stringfunc.capwords(clipped_string)

                enclist = re.findall(r'[A-z]{3,20}|Ho-Oh', capital_string)
                enclist = remove_values_from_list(enclist, 'Lvs')

                raritylist = []

                raritynumbers = []

                for mon in enclist:
                    if mon in pkmn_list and mon != 'Lvs':
                        raritylist.append(mon)
                        raritynumbers.append(str(enclist.index(mon) + 1) + "/" + str(len(enclist)))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                if len(raritylist) == 0:
                    return
                else:
                    hastype = "YES"

                blacklist = {"Set #55 - Ruins of Alph Hoenn/Sinnoh Radio ", "Set #56 - Ruins of Alph Swarms",
                             "Set #57 - Ruins of Alph Grass/Cave",
                             "Set #58 - Ruins of Alph Hoenn/Sinnoh Radio",
                             "Set #59 - Ruins of Alph Swarms", "Set #60 - Ruins of Alph Grass/Cave",
                             "Set #61 - Ruins of Alph Hoenn/Sinnoh Radio",
                             "Set #62 - Ruins of Alph Swarms",
                             "Set #63 - Ruins of Alph Grass/Cave", "Set #64 - Ruins of Alph Hoenn/Sinnoh Radio",
                             "Set #65 - Ruins of Alph Swarms",
                             "Set #73 - Ruins of Alph Morning Grass/Cave", "Set #74 - Ruins of Alph Day Grass/Cave",
                             "Set #75 - Ruins of Alph Night Grass/Cave",
                             "Set #76 - Ruins of Alph Hoenn/Sinnoh Radio", "Set #77 - Ruins of Alph Swarms",
                             "Set #78 - Ruins of Alph Morning Grass/Cave",
                             "Set #79 - Ruins of Alph Day Grass/Cave", "Set #80 - Ruins of Alph Night Grass/Cave",
                             "Set #81 - Ruins of Alph Hoenn/Sinnoh Radio",
                             "Set #82 - Ruins of Alph Swarms", "Set #83 - Ruins of Alph Morning Grass/Cave",
                             "Set #84 - Ruins of Alph Day Grass/Cave",
                             "Set #85 - Ruins of Alph Night Grass/Cave", "Set #86 - Ruins of Alph Hoenn/Sinnoh Radio",
                             "Set #87 - Ruins of Alph Swarms", }

                for x in blacklist:
                    if x in string:
                        return

                level = ""

                floors = [
                    # B1F
                    ["Set #145 - Burned Tower", "Set #146 - Burned Tower", "Set #147 - Burned Tower",
                     "Set #195 - Burned Tower", "Set #196 - Burned Tower", "Set #197 - Burned Tower",
                     "Set #198 - Burned Tower", "Set #199 - Burned Tower", "Set #645 - Cerulean Cave",
                     "Set #646 - Cerulean Cave", "Set #647 - Cerulean Cave", "Set #648 - Cerulean Cave",
                     "Set #649 - Cerulean Cave", "Set #650 - Cerulean Cave", "Set #651 - Cerulean Cave",
                     "Set #652 - Cerulean Cave", "Set #865 - Cerulean Cave", "Set #866 - Cerulean Cave",
                     "Set #867 - Cerulean Cave", "Set #868 - Cerulean Cave", "Set #869 - Cerulean Cave",
                     "Set #870 - Cerulean Cave", "Set #871 - Cerulean Cave", "Set #872 - Cerulean Cave",
                     "Set #873 - Cerulean Cave", "Set #874 - Cerulean Cave", "Set #272 - Ice Path",
                     "Set #273 - Ice Path",
                     "Set #274 - Ice Path", "Set #368 - Ice Path", "Set #369 - Ice Path", "Set #370 - Ice Path",
                     "Set #371 - Ice Path", "Set #372 - Ice Path", "Set #243 - Mt. Mortar", "Set #244 - Mt. Mortar",
                     "Set #245 - Mt. Mortar", "Set #246 - Mt. Mortar", "Set #247 - Mt. Mortar", "Set #248 - Mt. Mortar",
                     "Set #249 - Mt. Mortar", "Set #331 - Mt. Mortar", "Set #332 - Mt. Mortar", "Set #333 - Mt. Mortar",
                     "Set #334 - Mt. Mortar", "Set #335 - Mt. Mortar", "Set #336 - Mt. Mortar", "Set #337 - Mt. Mortar",
                     "Set #338 - Mt. Mortar", "Set #339 - Mt. Mortar", "Set #501 - Rock Tunnel",
                     "Set #502 - Rock Tunnel",
                     "Set #503 - Rock Tunnel", "Set #504 - Rock Tunnel", "Set #659 - Rock Tunnel",
                     "Set #660 - Rock Tunnel",
                     "Set #661 - Rock Tunnel", "Set #662 - Rock Tunnel", "Set #663 - Rock Tunnel",
                     "Set #664 - Rock Tunnel",
                     "Set #336 - Seafoam Islands", "Set #337 - Seafoam Islands", "Set #338 - Seafoam Islands",
                     "Set #450 - Seafoam Islands", "Set #451 - Seafoam Islands", "Set #452 - Seafoam Islands",
                     "Set #453 - Seafoam Islands", "Set #454 - Seafoam Islands", "Set #97 - SLOWPOKE Well",
                     "Set #98 - SLOWPOKE Well", "Set #99 - SLOWPOKE Well", "Set #100 - SLOWPOKE Well",
                     "Set #101 - SLOWPOKE Well", "Set #102 - SLOWPOKE Well", "Set #103 - SLOWPOKE Well",
                     "Set #129 - SLOWPOKE Well", "Set #130 - SLOWPOKE Well", "Set #131 - SLOWPOKE Well",
                     "Set #132 - SLOWPOKE Well", "Set #133 - SLOWPOKE Well", "Set #134 - SLOWPOKE Well",
                     "Set #135 - SLOWPOKE Well", "Set #136 - SLOWPOKE Well", "Set #137 - SLOWPOKE Well",
                     "Set #73 - Union Cave", "Set #74 - Union Cave", "Set #75 - Union Cave", "Set #76 - Union Cave",
                     "Set #77 - Union Cave", "Set #78 - Union Cave", "Set #79 - Union Cave", "Set #97 - Union Cave",
                     "Set #98 - Union Cave", "Set #99 - Union Cave", "Set #100 - Union Cave", "Set #101 - Union Cave",
                     "Set #102 - Union Cave", "Set #103 - Union Cave", "Set #104 - Union Cave", "Set #105 - Union Cave",
                     "Set #200 - Whirl Islands", "Set #201 - Whirl Islands", "Set #202 - Whirl Islands",
                     "Set #274 - Whirl Islands", "Set #275 - Whirl Islands", "Set #276 - Whirl Islands",
                     "Set #277 - Whirl Islands", "Set #278 - Whirl Islands", ],
                    # B2F
                    ["Set #275 - Ice Path", "Set #276 - Ice Path", "Set #277 - Ice Path", "Set #373 - Ice Path",
                     "Set #374 - Ice Path", "Set #375 - Ice Path", "Set #376 - Ice Path", "Set #377 - Ice Path",
                     "Set #339 - Seafoam Islands", "Set #340 - Seafoam Islands", "Set #341 - Seafoam Islands",
                     "Set #455 - Seafoam Islands", "Set #456 - Seafoam Islands", "Set #457 - Seafoam Islands",
                     "Set #458 - Seafoam Islands", "Set #459 - Seafoam Islands", "Set #80 - Union Cave",
                     "Set #81 - Union Cave", "Set #82 - Union Cave", "Set #83 - Union Cave", "Set #84 - Union Cave",
                     "Set #85 - Union Cave", "Set #86 - Union Cave", "Set #106 - Union Cave", "Set #107 - Union Cave",
                     "Set #108 - Union Cave", "Set #109 - Union Cave", "Set #110 - Union Cave", "Set #111 - Union Cave",
                     "Set #112 - Union Cave", "Set #113 - Union Cave", "Set #114 - Union Cave",
                     "Set #203 - Whirl Islands",
                     "Set #204 - Whirl Islands", "Set #205 - Whirl Islands", "Set #206 - Whirl Islands",
                     "Set #207 - Whirl Islands", "Set #208 - Whirl Islands", "Set #209 - Whirl Islands",
                     "Set #279 - Whirl Islands", "Set #280 - Whirl Islands", "Set #281 - Whirl Islands",
                     "Set #282 - Whirl Islands", "Set #283 - Whirl Islands", "Set #284 - Whirl Islands",
                     "Set #285 - Whirl Islands", "Set #286 - Whirl Islands", "Set #287 - Whirl Islands", ],
                    # B3F
                    ["Set #278 - Ice Path", "Set #279 - Ice Path", "Set #280 - Ice Path", "Set #378 - Ice Path",
                     "Set #379 - Ice Path", "Set #380 - Ice Path", "Set #381 - Ice Path", "Set #382 - Ice Path",
                     "Set #342 - Seafoam Islands", "Set #343 - Seafoam Islands", "Set #344 - Seafoam Islands",
                     "Set #460 - Seafoam Islands", "Set #461 - Seafoam Islands", "Set #462 - Seafoam Islands",
                     "Set #463 - Seafoam Islands", "Set #464 - Seafoam Islands", "Set #210 - Whirl Islands",
                     "Set #211 - Whirl Islands", "Set #212 - Whirl Islands", "Set #288 - Whirl Islands",
                     "Set #289 - Whirl Islands", "Set #290 - Whirl Islands", "Set #291 - Whirl Islands",
                     "Set #292 - Whirl Islands", ],
                    # B4F
                    ["Set #345 - Seafoam Islands", "Set #346 - Seafoam Islands", "Set #347 - Seafoam Islands",
                     "Set #348 - Seafoam Islands", "Set #349 - Seafoam Islands", "Set #350 - Seafoam Islands",
                     "Set #351 - Seafoam Islands", "Set #465 - Seafoam Islands", "Set #466 - Seafoam Islands",
                     "Set #467 - Seafoam Islands", "Set #468 - Seafoam Islands", "Set #469 - Seafoam Islands",
                     "Set #470 - Seafoam Islands", "Set #471 - Seafoam Islands", "Set #472 - Seafoam Islands",
                     "Set #473 - Seafoam Islands", ],
                    # 1F
                    ["Set #33 - Sprout Tower", "Set #34 - Sprout Tower", "Set #35 - Sprout Tower",
                     "Set #39 - Sprout Tower",
                     "Set #40 - Sprout Tower", "Set #41 - Sprout Tower", "Set #42 - Sprout Tower",
                     "Set #43 - Sprout Tower",
                     "Set #66 - Union Cave", "Set #67 - Union Cave", "Set #68 - Union Cave", "Set #69 - Union Cave",
                     "Set #70 - Union Cave", "Set #71 - Union Cave", "Set #72 - Union Cave", "Set #88 - Union Cave",
                     "Set #89 - Union Cave", "Set #90 - Union Cave", "Set #91 - Union Cave", "Set #92 - Union Cave",
                     "Set #93 - Union Cave", "Set #94 - Union Cave", "Set #95 - Union Cave", "Set #96 - Union Cave",
                     "Set #90 - SLOWPOKE Well", "Set #91 - SLOWPOKE Well", "Set #92 - SLOWPOKE Well",
                     "Set #93 - SLOWPOKE Well", "Set #94 - SLOWPOKE Well", "Set #95 - SLOWPOKE Well",
                     "Set #96 - SLOWPOKE Well", "Set #120 - SLOWPOKE Well", "Set #121 - SLOWPOKE Well",
                     "Set #122 - SLOWPOKE Well", "Set #123 - SLOWPOKE Well", "Set #124 - SLOWPOKE Well",
                     "Set #125 - SLOWPOKE Well", "Set #126 - SLOWPOKE Well", "Set #127 - SLOWPOKE Well",
                     "Set #128 - SLOWPOKE Well", "Set #142 - Burned Tower", "Set #143 - Burned Tower",
                     "Set #144 - Burned Tower", "Set #190 - Burned Tower", "Set #191 - Burned Tower",
                     "Set #192 - Burned Tower", "Set #193 - Burned Tower", "Set #194 - Burned Tower",
                     "Set #148 - Bell Tower",
                     "Set #149 - Bell Tower", "Set #150 - Bell Tower", "Set #200 - Bell Tower", "Set #201 - Bell Tower",
                     "Set #202 - Bell Tower", "Set #203 - Bell Tower", "Set #204 - Bell Tower",
                     "Set #193 - Whirl Islands",
                     "Set #194 - Whirl Islands", "Set #195 - Whirl Islands", "Set #196 - Whirl Islands",
                     "Set #197 - Whirl Islands", "Set #198 - Whirl Islands", "Set #199 - Whirl Islands",
                     "Set #265 - Whirl Islands", "Set #266 - Whirl Islands", "Set #267 - Whirl Islands",
                     "Set #268 - Whirl Islands", "Set #269 - Whirl Islands", "Set #270 - Whirl Islands",
                     "Set #271 - Whirl Islands", "Set #272 - Whirl Islands", "Set #273 - Whirl Islands",
                     "Set #226 - Mt. Mortar", "Set #227 - Mt. Mortar", "Set #228 - Mt. Mortar", "Set #229 - Mt. Mortar",
                     "Set #230 - Mt. Mortar", "Set #231 - Mt. Mortar", "Set #232 - Mt. Mortar", "Set #308 - Mt. Mortar",
                     "Set #309 - Mt. Mortar", "Set #310 - Mt. Mortar", "Set #311 - Mt. Mortar", "Set #312 - Mt. Mortar",
                     "Set #313 - Mt. Mortar", "Set #314 - Mt. Mortar", "Set #315 - Mt. Mortar", "Set #316 - Mt. Mortar",
                     "Set #269 - Ice Path", "Set #270 - Ice Path", "Set #271 - Ice Path", "Set #363 - Ice Path",
                     "Set #364 - Ice Path", "Set #365 - Ice Path", "Set #366 - Ice Path", "Set #367 - Ice Path",
                     "Set #407 - Dark Cave", "Set #408 - Dark Cave", "Set #409 - Dark Cave", "Set #410 - Dark Cave",
                     "Set #411 - Dark Cave", "Set #412 - Dark Cave", "Set #413 - Dark Cave", "Set #414 - Dark Cave",
                     "Set #415 - Dark Cave", "Set #416 - Dark Cave",
                     "Set #333 - Seafoam Islands", "Set #334 - Seafoam Islands", "Set #335 - Seafoam Islands",
                     "Set #445 - Seafoam Islands", "Set #446 - Seafoam Islands", "Set #447 - Seafoam Islands",
                     "Set #448 - Seafoam Islands", "Set #449 - Seafoam Islands", "Set #352 - Mt. Silver Cave",
                     "Set #353 - Mt. Silver Cave", "Set #354 - Mt. Silver Cave", "Set #355 - Mt. Silver Cave",
                     "Set #356 - Mt. Silver Cave", "Set #357 - Mt. Silver Cave", "Set #358 - Mt. Silver Cave",
                     "Set #474 - Mt. Silver Cave", "Set #475 - Mt. Silver Cave", "Set #476 - Mt. Silver Cave",
                     "Set #477 - Mt. Silver Cave", "Set #478 - Mt. Silver Cave", "Set #479 - Mt. Silver Cave",
                     "Set #480 - Mt. Silver Cave", "Set #481 - Mt. Silver Cave", "Set #482 - Mt. Silver Cave",
                     "Set #359 - Mt. Silver Cave", "Set #360 - Mt. Silver Cave", "Set #361 - Mt. Silver Cave",
                     "Set #362 - Mt. Silver Cave", "Set #363 - Mt. Silver Cave", "Set #364 - Mt. Silver Cave",
                     "Set #365 - Mt. Silver Cave", "Set #483 - Mt. Silver Cave", "Set #484 - Mt. Silver Cave",
                     "Set #485 - Mt. Silver Cave", "Set #486 - Mt. Silver Cave", "Set #487 - Mt. Silver Cave",
                     "Set #488 - Mt. Silver Cave", "Set #489 - Mt. Silver Cave", "Set #490 - Mt. Silver Cave",
                     "Set #491 - Mt. Silver Cave", "Set #492 - Mt. Moon", "Set #493 - Mt. Moon", "Set #494 - Mt. Moon",
                     "Set #644 - Mt. Moon", "Set #645 - Mt. Moon", "Set #646 - Mt. Moon", "Set #647 - Mt. Moon",
                     "Set #648 - Mt. Moon", "Set #630 - Cerulean Cave", "Set #631 - Cerulean Cave",
                     "Set #632 - Cerulean Cave",
                     "Set #633 - Cerulean Cave", "Set #634 - Cerulean Cave", "Set #635 - Cerulean Cave",
                     "Set #636 - Cerulean Cave", "Set #637 - Cerulean Cave", "Set #846 - Cerulean Cave",
                     "Set #847 - Cerulean Cave", "Set #848 - Cerulean Cave", "Set #849 - Cerulean Cave",
                     "Set #850 - Cerulean Cave", "Set #851 - Cerulean Cave", "Set #852 - Cerulean Cave",
                     "Set #853 - Cerulean Cave", "Set #854 - Cerulean Cave", "Set #855 - Cerulean Cave", ],
                    # 2F
                    ["Set #638 - Cerulean Cave", "Set #639 - Cerulean Cave", "Set #640 - Cerulean Cave",
                     "Set #641 - Cerulean Cave", "Set #642 - Cerulean Cave", "Set #643 - Cerulean Cave",
                     "Set #644 - Cerulean Cave", "Set #856 - Cerulean Cave", "Set #857 - Cerulean Cave",
                     "Set #858 - Cerulean Cave", "Set #859 - Cerulean Cave", "Set #860 - Cerulean Cave",
                     "Set #861 - Cerulean Cave", "Set #862 - Cerulean Cave", "Set #863 - Cerulean Cave",
                     "Set #864 - Cerulean Cave", "Set #392 - Mt. Silver Cave", "Set #393 - Mt. Silver Cave",
                     "Set #394 - Mt. Silver Cave", "Set #395 - Mt. Silver Cave", "Set #396 - Mt. Silver Cave",
                     "Set #397 - Mt. Silver Cave", "Set #398 - Mt. Silver Cave", "Set #36 - Sprout Tower",
                     "Set #37 - Sprout Tower", "Set #38 - Sprout Tower", "Set #44 - Sprout Tower",
                     "Set #45 - Sprout Tower",
                     "Set #46 - Sprout Tower", "Set #47 - Sprout Tower", "Set #48 - Sprout Tower",
                     'Set #148 - Bell Tower',
                     'Set #149 - Bell Tower', 'Set #150 - Bell Tower', 'Set #200 - Bell Tower', 'Set #201 - Bell Tower',
                     'Set #202 - Bell Tower', 'Set #203 - Bell Tower', 'Set #204 - Bell Tower',
                     ],
                    # 3F
                    ["Set #402 - Mt. Silver Cave", "Set #403 - Mt. Silver Cave", "Set #404 - Mt. Silver Cave",
                     'Set #151 - Bell Tower', 'Set #152 - Bell Tower', 'Set #153 - Bell Tower', 'Set #205 - Bell Tower',
                     'Set #206 - Bell Tower', 'Set #207 - Bell Tower', 'Set #208 - Bell Tower', 'Set #209 - Bell Tower',
                     ],
                    # 4F
                    ["Set #366 - Mt. Silver Cave", "Set #367 - Mt. Silver Cave", "Set #368 - Mt. Silver Cave",
                     "Set #369 - Mt. Silver Cave", "Set #370 - Mt. Silver Cave", "Set #371 - Mt. Silver Cave",
                     "Set #372 - Mt. Silver Cave", "Set #492 - Mt. Silver Cave", "Set #493 - Mt. Silver Cave",
                     "Set #494 - Mt. Silver Cave", "Set #495 - Mt. Silver Cave", "Set #496 - Mt. Silver Cave",
                     "Set #497 - Mt. Silver Cave", "Set #498 - Mt. Silver Cave", "Set #499 - Mt. Silver Cave",
                     "Set #500 - Mt. Silver Cave", 'Set #154 - Bell Tower', 'Set #155 - Bell Tower',
                     'Set #156 - Bell Tower',
                     'Set #210 - Bell Tower', 'Set #211 - Bell Tower', 'Set #212 - Bell Tower', 'Set #213 - Bell Tower',
                     'Set #214 - Bell Tower',
                     ],
                    # 5F
                    ['Set #157 - Bell Tower', 'Set #158 - Bell Tower', 'Set #159 - Bell Tower', 'Set #215 - Bell Tower',
                     'Set #216 - Bell Tower', 'Set #217 - Bell Tower', 'Set #218 - Bell Tower', 'Set #219 - Bell Tower',
                     ],
                    # 6F
                    ['Set #160 - Bell Tower', 'Set #161 - Bell Tower', 'Set #162 - Bell Tower', 'Set #220 - Bell Tower',
                     'Set #221 - Bell Tower', 'Set #222 - Bell Tower', 'Set #223 - Bell Tower', 'Set #224 - Bell Tower',
                     ],
                    # 7F
                    ['Set #163 - Bell Tower', 'Set #164 - Bell Tower', 'Set #165 - Bell Tower', 'Set #225 - Bell Tower',
                     'Set #226 - Bell Tower', 'Set #227 - Bell Tower', 'Set #228 - Bell Tower', 'Set #229 - Bell Tower',
                     ],
                    # 8F
                    ['Set #166 - Bell Tower', 'Set #167 - Bell Tower', 'Set #168 - Bell Tower', 'Set #230 - Bell Tower',
                     'Set #231 - Bell Tower', 'Set #232 - Bell Tower', 'Set #233 - Bell Tower', 'Set #234 - Bell Tower',
                     ],
                    # 9F
                    ['Set #169 - Bell Tower', 'Set #170 - Bell Tower', 'Set #171 - Bell Tower', 'Set #235 - Bell Tower',
                     'Set #236 - Bell Tower', 'Set #237 - Bell Tower', 'Set #238 - Bell Tower', 'Set #239 - Bell Tower',
                     ],
                    # 10F
                    ['Set #382 - Bell Tower', 'Set #383 - Bell Tower', 'Set #384 - Bell Tower', 'Set #512 - Bell Tower',
                     'Set #513 - Bell Tower', 'Set #514 - Bell Tower', 'Set #515 - Bell Tower',
                     'Set #516 - Bell Tower', ],
                    # Outside
                    ['Set #58 - Ruins of Alph Morning Grass/Cave', 'Set #59 - Ruins of Alph Day Grass/Cave',
                     'Set #60 - Ruins of Alph Night Grass/Cave', 'Set #61 - Ruins of Alph Hoenn/Sinnoh Radio',
                     'Set #62 - Ruins of Alph Surfing', 'Set #63 - Ruins of Alph Rock Smash',
                     'Set #64 - Ruins of Alph Old Rod',
                     'Set #65 - Ruins of Alph Good Rod', 'Set #66 - Ruins of Alph Super Rod',
                     'Set #67 - Ruins of Alph Swarm',
                     'Set #46 - Ruins of Alph Grass/Cave', 'Set #47 - Ruins of Alph Hoenn/Sinnoh Radio',
                     'Set #48 - Ruins of Alph Surfing', 'Set #49 - Ruins of Alph Rock Smash',
                     'Set #50 - Ruins of Alph Old Rod',
                     'Set #51 - Ruins of Alph Good Rod', 'Set #52 - Ruins of Alph Super Rod',
                     'Set #53 - Ruins of Alph Swarms',
                     "Set #323 - Mt. Moon", "Set #324 - Mt. Moon",
                     "Set #325 - Mt. Moon", "Set #326 - Mt. Moon", "Set #327 - Mt. Moon", "Set #435 - Mt. Moon",
                     "Set #436 - Mt. Moon", "Set #437 - Mt. Moon", "Set #438 - Mt. Moon", "Set #439 - Mt. Moon", ],
                    # Inside
                    ['Set #54 - Ruins of Alph Grass/Cave', 'Set #68 - Ruins of Alph Morning Grass/Cave',
                     'Set #69 - Ruins of Alph Day Grass/Cave', 'Set #70 - Ruins of Alph Night Grass/Cave',
                     'Set #644 - Mt. Moon',
                     'Set #645 - Mt. Moon', 'Set #646 - Mt. Moon', 'Set #647 - Mt. Moon', 'Set #648 - Mt. Moon',
                     'Set #649 - Mt. Moon', 'Set #650 - Mt. Moon', 'Set #651 - Mt. Moon', 'Set #652 - Mt. Moon',
                     'Set #653 - Mt. Moon', 'Set #492 - Mt. Moon', 'Set #493 - Mt. Moon', 'Set #494 - Mt. Moon',
                     'Set #495 - Mt. Moon', 'Set #496 - Mt. Moon', 'Set #497 - Mt. Moon', ],
                    # Route 31
                    ["Set #301 - Dark Cave", "Set #302 - Dark Cave", "Set #303 - Dark Cave", "Set #304 - Dark Cave",
                     "Set #305 - Dark Cave", "Set #306 - Dark Cave", "Set #307 - Dark Cave", "Set #308 - Dark Cave",
                     'Set #407 - Dark Cave', 'Set #408 - Dark Cave', 'Set #409 - Dark Cave', 'Set #410 - Dark Cave',
                     'Set #411 - Dark Cave', 'Set #412 - Dark Cave', 'Set #413 - Dark Cave', 'Set #414 - Dark Cave',
                     'Set #415 - Dark Cave', 'Set #416 - Dark Cave',
                     ],
                    # Route 45
                    ['Set #309 - Dark Cave', 'Set #310 - Dark Cave', 'Set #311 - Dark Cave', 'Set #312 - Dark Cave',
                     'Set #313 - Dark Cave', 'Set #314 - Dark Cave', 'Set #315 - Dark Cave', 'Set #417 - Dark Cave',
                     'Set #418 - Dark Cave', 'Set #419 - Dark Cave', 'Set #420 - Dark Cave', 'Set #421 - Dark Cave',
                     'Set #422 - Dark Cave', 'Set #423 - Dark Cave', 'Set #424 - Dark Cave', 'Set #425 - Dark Cave', ],
                ]
                for x in floors:
                    for y in x:
                        if y in string:
                            if floors.index(x) == 0:
                                level = "B1F - "
                            elif floors.index(x) == 1:
                                level = "B2F - "
                            elif floors.index(x) == 2:
                                level = "B3F - "
                            elif floors.index(x) == 3:
                                level = "B4F - "
                            elif floors.index(x) == 4:
                                level = "1F - "
                            elif floors.index(x) == 5:
                                level = "2F - "
                            elif floors.index(x) == 6:
                                level = "3F - "
                            elif floors.index(x) == 7:
                                level = "4F - "
                            elif floors.index(x) == 8:
                                level = "5F - "
                            elif floors.index(x) == 9:
                                level = "6F - "
                            elif floors.index(x) == 10:
                                level = "7F - "
                            elif floors.index(x) == 11:
                                level = "8F - "
                            elif floors.index(x) == 12:
                                level = "9F - "
                            elif floors.index(x) == 13:
                                level = "10F - "
                            elif floors.index(x) == 14:
                                level = "Outside - "
                            elif floors.index(x) == 15:
                                level = "Inside - "
                            elif floors.index(x) == 16:
                                level = "Route 31 - "
                            elif floors.index(x) == 17:
                                level = "Route 45 - "

                time_of_day = ""

                fishing_percent = []

                surfing_percent = []

                rock_smash_percent = []

                walking_percent = []

                if "Grass/Cave" in string:
                    for x in raritynumbers:
                        if x in ["1/12", "2/12"]:
                            walking_percent.append("20%")
                        elif x in ["3/12", "4/12", "5/12", "6/12"]:
                            walking_percent.append("10%")
                        elif x in ["7/12", "8/12"]:
                            walking_percent.append("5%")
                        elif x in ["9/12", "10/12"]:
                            walking_percent.append("4%")
                        elif x in ["11/12", "12/12"]:
                            walking_percent.append("1%")

                elif "Surfing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            surfing_percent.append("60%")
                        elif x == "2/5":
                            surfing_percent.append('30%')
                        elif x == "3/5":
                            surfing_percent.append("5%")
                        elif x == "4/5":
                            surfing_percent.append("4%")
                        elif x == "5/5":
                            surfing_percent.append("1%")

                elif "Old Rod" or "Good Rod" or "Super Rod" or "Fishing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            fishing_percent.append("40%")
                        elif x == "2/5":
                            fishing_percent.append('30%')
                        elif x == "3/5":
                            fishing_percent.append("15%")
                        elif x == "4/5":
                            fishing_percent.append("10%")
                        elif x == "5/5":
                            fishing_percent.append("5%")

                if "Rock Smash" in string:
                    for x in raritynumbers:
                        if x == "1/2":
                            rock_smash_percent.append("90%")
                        elif x == "2/2":
                            rock_smash_percent.append("10%")

                if "Morning" in string:
                    time_of_day = "Morning "
                elif "Day" in string:
                    time_of_day = "Day "
                elif "Night" in string:
                    time_of_day = "Night "

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(
                            level + time_of_day + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " +
                            str(walking_percent) + "\n")

                    elif "Surfing" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            surfing_percent) + "\n")

                    elif "Old Rod" in string:
                        f.write(level + "Old Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Good Rod" in string:
                        f.write(level + "Good Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Super Rod" in string:
                        f.write(level + "Super Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Fishing" in string:
                        f.write(level + "Fishing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Swarm" in string:
                        f.write(level + "Swarm, Check Prof. Oak Radio" + "\n")

                    elif "Radio" in string:
                        f.write(level + "Check Hoenn/Sinnoh Radio" + "\n")

                    elif "Rock Smash" in string:
                        f.write(level + "Rock Smash" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            rock_smash_percent) + "\n")

            # Functions for Diamond, Pearl and Platinum logs
            def extr_enc_dpp(string):
                blacklist = {}

                for x in blacklist:
                    if x in string:
                        return

                level = ""
                if game == "Platinum":
                    floors = [
                        # B1F
                        ["Set #317", "Set #318", "Set #319", "Set #320", "Set #71 ", "Set #72 ", "Set #177", "Set #178",
                         "Set #23 ",
                         "Set #24 ", "Set #301", "Set #302", "Set #153", "Set #154", "Set #159", "Set #160",
                         ],
                        # B2F
                        ["Set #321", "Set #322", "Set #323", "Set #324",
                         ],
                        # B3F
                        ["Set #325", "Set #326",
                         ],
                        # B4F
                        [
                        ],
                        # 1F
                        ["Set #315", "Set #316", "Set #175", "Set #176", "Set #21 ", "Set #22 ", "Set #299", "Set #300",
                         "Set #165",
                         "Set #166", "Set #167", "Set #168", "Set #149", "Set #150",
                         ],
                        # 2F
                        ["Set #45 ", "Set #46 ", "Set #151", "Set #152",
                         ],
                        # 3F
                        ["Set #47 ", "Set #48 ",
                         ],
                        # 4F
                        ["Set #53 ", "Set #54 ",
                         ],
                        # 5F
                        ["Set #59 ", "Set #60 ",
                         ],
                        # 6F
                        ["Set #61 ", "Set #62 ",
                         ],
                        # 7F
                        ["Set #63 ", "Set #64 ",
                         ],
                        # 8F
                        [
                        ],
                        # 9F
                        [
                        ],
                        # 10F
                        [
                        ],
                        # Outside
                        ["Set #311", "Set #312", "Set #313", "Set #314",
                         ],
                        # Inside
                        [
                        ],
                        # Great Marsh 1
                        ["Set #77 ", "Set #78 ", "Set #79 ", "Set #80 ", "Set #81 ", "Set #82 ",
                         ],
                        # Great Marsh 2
                        ["Set #83 ", "Set #84 ", "Set #85 ", "Set #86 ", "Set #87 ", "Set #88 ",
                         ],
                        # Great Marsh 3
                        ["Set #89 ", "Set #90 ", "Set #91 ", "Set #92 ", "Set #93 ", "Set #94 ",
                         ],
                        # Great Marsh 4
                        ["Set #95 ", "Set #96 ", "Set #97 ", "Set #98 ", "Set #99 ", "Set #100",
                         ],
                        # Great Marsh 5
                        ["Set #101", "Set #102", "Set #103", "Set #104", "Set #105", "Set #106",
                         ],
                        # Great Marsh 6
                        ["Set #107", "Set #108", "Set #109", "Set #110", "Set #111", "Set #112",
                         ],
                        # Mt. Coronet Route 211
                        ["Set #69 ", "Set #70 ",
                         ],
                        # Mt. Coronet Route 207
                        ["Set #39 ", "Set #40 ",
                         ],
                        # Mt. Coronet Route 216
                        ["Set #67 ", "Set #68 ",
                         ],
                        # Mt. Coronet snow
                        ["Set #51 ", "Set #52 ",
                         ],
                        # Lake Verity Before Galactic
                        ["Set #347", "Set #348", "Set #349", "Set #350", "Set #351", "Set #352",
                         ],

                    ]
                    for x in floors:
                        for y in x:
                            if y in string:
                                if floors.index(x) == 0:
                                    level = "B1F - "
                                elif floors.index(x) == 1:
                                    level = "B2F - "
                                elif floors.index(x) == 2:
                                    level = "B3F - "
                                elif floors.index(x) == 3:
                                    level = "B4F - "
                                elif floors.index(x) == 4:
                                    level = "1F - "
                                elif floors.index(x) == 5:
                                    level = "2F - "
                                elif floors.index(x) == 6:
                                    level = "3F - "
                                elif floors.index(x) == 7:
                                    level = "4F - "
                                elif floors.index(x) == 8:
                                    level = "5F - "
                                elif floors.index(x) == 9:
                                    level = "6F - "
                                elif floors.index(x) == 10:
                                    level = "7F - "
                                elif floors.index(x) == 11:
                                    level = "8F - "
                                elif floors.index(x) == 12:
                                    level = "9F - "
                                elif floors.index(x) == 13:
                                    level = "10F - "
                                elif floors.index(x) == 14:
                                    level = "Outside - "
                                elif floors.index(x) == 15:
                                    level = "Inside - "
                                elif floors.index(x) == 16:
                                    level = "Great Marsh 1 - "
                                elif floors.index(x) == 17:
                                    level = "Great Marsh 2 - "
                                elif floors.index(x) == 18:
                                    level = "Great Marsh 3 - "
                                elif floors.index(x) == 19:
                                    level = "Great Marsh 4 - "
                                elif floors.index(x) == 20:
                                    level = "Great Marsh 5 - "
                                elif floors.index(x) == 21:
                                    level = "Great Marsh 6 - "
                                elif floors.index(x) == 22:
                                    level = "Mt. Coronet Route 211 - "
                                elif floors.index(x) == 23:
                                    level = "Mt. Coronet Route 207 - "
                                elif floors.index(x) == 24:
                                    level = "Mt. Coronet Route 216 - "
                                elif floors.index(x) == 25:
                                    level = "Mt. Coronet Snow - "
                                elif floors.index(x) == 26:
                                    level = "Lake Verity Before Galactic - "
                else:
                    floors = [
                        # B1F
                        ["Set #313", "Set #314", "Set #315", "Set #316", "Set #71 ", "Set #72 ", "Set #173", "Set #174",
                         "Set #23 ",
                         "Set #24 ", "Set #297", "Set #298", "Set #149", "Set #150", "Set #155", "Set #156",
                         ],
                        # B2F
                        ["Set #321", "Set #322", "Set #323", "Set #324",
                         ],
                        # B3F
                        ["Set #325", "Set #326",
                         ],
                        # B4F
                        [
                        ],
                        # 1F
                        ["Set #317", "Set #318", "Set #171", "Set #172", "Set #21 ", "Set #22 ", "Set #295", "Set #296",
                         "Set #161",
                         "Set #162", "Set #163", "Set #164", "Set #145", "Set #146",
                         ],
                        # 2F
                        ["Set #45 ", "Set #46 ", "Set #147", "Set #148",
                         ],
                        # 3F
                        ["Set #47 ", "Set #48 ",
                         ],
                        # 4F
                        ["Set #53 ", "Set #54 ",
                         ],
                        # 5F
                        ["Set #59 ", "Set #60 ",
                         ],
                        # 6F
                        ["Set #61 ", "Set #62 ",
                         ],
                        # 7F
                        ["Set #63 ", "Set #64 ",
                         ],
                        # 8F
                        [
                        ],
                        # 9F
                        [
                        ],
                        # 10F
                        [
                        ],
                        # Outside
                        ["Set #307", "Set #308", "Set #309", "Set #310",
                         ],
                        # Inside
                        [
                        ],
                        # Great Marsh 1
                        ["Set #77 ", "Set #78 ", "Set #79 ", "Set #80 ", "Set #81 ", "Set #82 ",
                         ],
                        # Great Marsh 2
                        ["Set #83 ", "Set #84 ", "Set #85 ", "Set #86 ", "Set #87 ", "Set #88 ",
                         ],
                        # Great Marsh 3
                        ["Set #89 ", "Set #90 ", "Set #91 ", "Set #92 ", "Set #93 ", "Set #94 ",
                         ],
                        # Great Marsh 4
                        ["Set #95 ", "Set #96 ", "Set #97 ", "Set #98 ", "Set #99 ", "Set #100",
                         ],
                        # Great Marsh 5
                        ["Set #101", "Set #102", "Set #103", "Set #104", "Set #105", "Set #106",
                         ],
                        # Great Marsh 6
                        ["Set #107", "Set #108", "Set #109", "Set #110", "Set #111", "Set #112",
                         ],
                        # Mt. Coronet Route 211
                        ["Set #69 ", "Set #70 ",
                         ],
                        # Mt. Coronet Route 207
                        ["Set #39 ", "Set #40 ",
                         ],
                        # Mt. Coronet Route 216
                        ["Set #67 ", "Set #68 ",
                         ],
                        # Mt. Coronet snow
                        ["Set #51 ", "Set #52 ",
                         ],
                        # Lake Verity Before Galactic
                        ["Set #343", "Set #344", "Set #345", "Set #346", "Set #347", "Set #348",
                         ],

                    ]
                    for x in floors:
                        for y in x:
                            if y in string:
                                if floors.index(x) == 0:
                                    level = "B1F - "
                                elif floors.index(x) == 1:
                                    level = "B2F - "
                                elif floors.index(x) == 2:
                                    level = "B3F - "
                                elif floors.index(x) == 3:
                                    level = "B4F - "
                                elif floors.index(x) == 4:
                                    level = "1F - "
                                elif floors.index(x) == 5:
                                    level = "2F - "
                                elif floors.index(x) == 6:
                                    level = "3F - "
                                elif floors.index(x) == 7:
                                    level = "4F - "
                                elif floors.index(x) == 8:
                                    level = "5F - "
                                elif floors.index(x) == 9:
                                    level = "6F - "
                                elif floors.index(x) == 10:
                                    level = "7F - "
                                elif floors.index(x) == 11:
                                    level = "8F - "
                                elif floors.index(x) == 12:
                                    level = "9F - "
                                elif floors.index(x) == 13:
                                    level = "10F - "
                                elif floors.index(x) == 14:
                                    level = "Outside - "
                                elif floors.index(x) == 15:
                                    level = "Inside - "
                                elif floors.index(x) == 16:
                                    level = "Great Marsh 1 - "
                                elif floors.index(x) == 17:
                                    level = "Great Marsh 2 - "
                                elif floors.index(x) == 18:
                                    level = "Great Marsh 3 - "
                                elif floors.index(x) == 19:
                                    level = "Great Marsh 4 - "
                                elif floors.index(x) == 20:
                                    level = "Great Marsh 5 - "
                                elif floors.index(x) == 21:
                                    level = "Great Marsh 6 - "
                                elif floors.index(x) == 22:
                                    level = "Mt. Coronet Route 211 - "
                                elif floors.index(x) == 23:
                                    level = "Mt. Coronet Route 207 - "
                                elif floors.index(x) == 24:
                                    level = "Mt. Coronet Route 216 - "
                                elif floors.index(x) == 25:
                                    level = "Mt. Coronet Snow - "
                                elif floors.index(x) == 26:
                                    level = "Lake Verity Before Galactic - "

                clipped_string = string.lower()[string.find(") - ") + 4:]

                enclist = clipped_string.split(", ")

                encdict = {}

                n = 0
                while n < len(enclist):
                    for x in enclist:
                        n += 1
                        encdict[n] = x

                raritylist = []

                for x, y in encdict.items():
                    for z in pkmn_list:
                        if z.lower() in y:
                            raritylist.append(x)

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                raritynumbers = []

                for x in raritylist:
                    raritynumbers.append(str(x) + "/" + str(len(enclist)))

                if len(raritylist) == 0:
                    hastype = "NO"
                else:
                    hastype = "YES"

                fishing_percent = []

                surfing_percent = []

                walking_percent = []

                if "Grass/Cave" in string:
                    for x in raritynumbers:
                        if x in ["1/12", "2/12"]:
                            walking_percent.append("20%")
                        elif x in ["3/12", "4/12", "5/12", "6/12"]:
                            walking_percent.append("10%")
                        elif x in ["7/12", "8/12"]:
                            walking_percent.append("5%")
                        elif x in ["9/12", "10/12"]:
                            walking_percent.append("4%")
                        elif x in ["11/12", "12/12"]:
                            walking_percent.append("1%")

                elif "Surfing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            surfing_percent.append("60%")
                        elif x == "2/5":
                            surfing_percent.append('30%')
                        elif x == "3/5":
                            surfing_percent.append("5%")
                        elif x == "4/5":
                            surfing_percent.append("4%")
                        elif x == "5/5":
                            surfing_percent.append("1%")

                elif "Old Rod" or "Good Rod" or "Super Rod" or "Fishing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            fishing_percent.append("40%")
                        elif x == "2/5":
                            fishing_percent.append('30%')
                        elif x == "3/5":
                            fishing_percent.append("15%")
                        elif x == "4/5":
                            fishing_percent.append("10%")
                        elif x == "5/5":
                            fishing_percent.append("5%")

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(level + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Surfing" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            surfing_percent) + "\n")

                    elif "Old Rod" in string:
                        f.write(level + "Old Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Good Rod" in string:
                        f.write(level + "Good Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Super Rod" in string:
                        f.write(level + "Super Rod" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Fishing" in string:
                        f.write(level + "Fishing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Swarm" in string:
                        f.write(level + "Swarm/Radar/GBA" + "\n")

            # Functions for Black and White logs
            def extr_enc_bw(string):
                level = ""

                clipped_string = string[string.find(") - ") + 4:]

                capital_string = stringfunc.capwords(clipped_string)

                enclist = re.findall(r'[A-z]{3,20}|Ho-Oh', capital_string)
                enclist = remove_values_from_list(enclist, 'Lvs')

                raritylist = []

                raritynumbers = []

                for mon in enclist:
                    if mon in pkmn_list and mon != 'Lvs':
                        raritylist.append(mon)
                        raritynumbers.append(str(enclist.index(mon) + 1) + "/" + str(len(enclist)))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                if len(raritylist) == 0:
                    return
                else:
                    hastype = "YES"

                floors = [
                    # B1F
                    ['Set #236', 'Set #237', 'Set #66', 'Set #67', 'Set #31', 'Set #59',
                     ],
                    # B2F
                    ['Set #238', 'Set #239', 'Set #240', 'Set #241', 'Set #242', 'Set #243', 'Set #68', 'Set #69',
                     'Set #32',
                     'Set #58',
                     ],
                    # B3F
                    ['Set #33', 'Set #57',
                     ],
                    # B4F
                    ['Set #34', 'Set #56',
                     ],
                    # B5F
                    ['Set #35', 'Set #55',
                     ],
                    # B6F
                    ['Set #54',
                     ],
                    # 1F
                    ['Set #234', 'Set #235', 'Set #64', 'Set #65', 'Set #87', 'Set #30', 'Set #60', 'Set #90',
                     'Set #91',
                     'Set #92',
                     'Set #93', 'Set #94', 'Set #95', 'Set #104', 'Set #105', 'Set #106', 'Set #107', 'Set #108',
                     'Set #109',
                     'Set #112', 'Set #113',
                     ],
                    # 2F
                    ['Set #217', 'Set #88', 'Set #96', 'Set #97', 'Set #102', 'Set #103',
                     ],
                    # 3F
                    ['Set #218', 'Set #110', 'Set #111', 'Set #114', 'Set #115',
                     ],
                    # 4F
                    ['Set #219', 'Set #122', 'Set #123', 'Set #116', 'Set #117',
                     ],
                    # 5F
                    ['Set #118', 'Set #119',
                     ],
                    # 6F
                    ['Set #120', 'Set #121',
                     ],
                    # 7F
                    ['Set #124', 'Set #125',
                     ],
                    # Outside
                    ['Set #15', 'Set #16', 'Set #29', 'Set #80', 'Set #81', 'Set #82', 'Set #83', 'Set #84', 'Set #85',
                     'Set #86',
                     'Set #14', 'Set #128', 'Set #129', 'Set #130', 'Set #18', 'Set #19', 'Set #20', 'Set #89',
                     ],
                    # Inside
                    ['Set #28', 'Set #17', 'Set #131', 'Set #132', 'Set #133', 'Set #134', 'Set #135', 'Set #136',
                     'Set #21',
                     'Set #22', 'Set #23', 'Set #24', 'Set #25', 'Set #26', 'Set #27',
                     ],
                    # Celestial Tower Summit
                    ['Set #220'
                     ],
                    # Giant Chasm Plains
                    ['Set #137', 'Set #138', 'Set #139',
                     ],
                    # Entrance
                    ['Set #78', 'Set #79',
                     ],
                    # Inner Cave
                    ['Set #140', 'Set #141', 'Set #142', 'Set #143', 'Set #144', 'Set #145',
                     ],
                    # Relic Castle Lowest Floor
                    ['Set #36', 'Set #37', 'Set #38', 'Set #39', 'Set #40', 'Set #41', 'Set #42', 'Set #43', 'Set #44',
                     'Set #45',
                     'Set #46', 'Set #47', 'Set #48', 'Set #49', 'Set #50', 'Set #51', 'Set #52',
                     'Set #53',
                     ],

                ]
                for x in floors:
                    for y in x:
                        if y in string:
                            if floors.index(x) == 0:
                                if y == 'Set #59':
                                    level = "B1F (West) - "
                                else:
                                    level = "B1F - "
                            elif floors.index(x) == 1:
                                if y == 'Set #58':
                                    level = "B2F (West) - "
                                else:
                                    level = "B2F - "
                            elif floors.index(x) == 2:
                                if y == 'Set #57':
                                    level = "B3F (West) - "
                                else:
                                    level = "B3F - "
                            elif floors.index(x) == 3:
                                if y == 'Set #56':
                                    level = "B4F (West) - "
                                else:
                                    level = "B4F - "
                            elif floors.index(x) == 3:
                                if y == 'Set #55':
                                    level = "B5F (West) - "
                                else:
                                    level = "B5F - "
                            elif floors.index(x) == 3:
                                if y == 'Set #54':
                                    level = "B6F (West) - "
                                else:
                                    level = "B6F - "
                            elif floors.index(x) == 4:
                                if y == 'Set #60':
                                    level = "1F (West) - "
                                elif y in ['Set #104', 'Set #105', 'Set #106', 'Set #107', 'Set #108', 'Set #109', ]:
                                    level = "1F (Right Side)"
                                elif y in ['Set #112', 'Set #113']:
                                    level = "1F (Right Side)"
                                else:
                                    level = "1F - "
                            elif floors.index(x) == 5:
                                if y in ['Set #102', 'Set #103']:
                                    level = "2F (Right Side)"
                                else:
                                    level = "2F - "
                            elif floors.index(x) == 6:
                                if y in ['Set #110', 'Set #111']:
                                    level = "3F (Right Side)"
                                elif y in ['Set #114', 'Set #115']:
                                    level = "3F (Left Side)"
                                else:
                                    level = "3F - "
                            elif floors.index(x) == 7:
                                if y in ['Set #116', 'Set #117']:
                                    level = "4F (Left Side)"
                                elif y in ['Set #122', 'Set #123']:
                                    level = "4F (Right Side)"
                                else:
                                    level = "4F - "
                            elif floors.index(x) == 8:
                                level = "5F - "
                            elif floors.index(x) == 9:
                                level = "6F - "
                            elif floors.index(x) == 10:
                                level = "7F - "
                            elif floors.index(x) == 14:
                                level = "Outside - "
                            elif floors.index(x) == 15:
                                level = "Inside - "
                            elif floors.index(x) == 16:
                                level = "Celestial Tower Summit - "
                            elif floors.index(x) == 17:
                                level = "Giant Chasm Plains - "
                            elif floors.index(x) == 18:
                                level = "Entrance - "
                            elif floors.index(x) == 19:
                                level = "Inner Cave - "
                            elif floors.index(x) == 20:
                                if y == 'Set #53':
                                    level = "Relic Castle Lowest Floor (West) - "
                                elif y == 'Set #36':
                                    level = "Relic Castle Lowest Floor (East) - "
                                else:
                                    level = "Relic Castle Lowest Floor - "

                fishing_percent = []

                surfing_percent = []

                walking_percent = []

                if any(re.findall('Grass/Cave|Shaking Spots|Doubles Grass', string, re.IGNORECASE)):
                    for x in raritynumbers:
                        if x in ["1/12", "2/12"]:
                            walking_percent.append("20%")
                        elif x in ["3/12", "4/12", "5/12", "6/12"]:
                            walking_percent.append("10%")
                        elif x in ["7/12", "8/12"]:
                            walking_percent.append("5%")
                        elif x in ["9/12", "10/12"]:
                            walking_percent.append("4%")
                        elif x in ["11/12", "12/12"]:
                            walking_percent.append("1%")
                elif "Surfing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            surfing_percent.append("60%")
                        elif x == "2/5":
                            surfing_percent.append('30%')
                        elif x == "3/5":
                            surfing_percent.append("5%")
                        elif x == "4/5":
                            surfing_percent.append("4%")
                        elif x == "5/5":
                            surfing_percent.append("1%")
                elif "Fishing" in string:
                    for x in raritynumbers:
                        if x == "1/5" or "2/5":
                            fishing_percent.append("40%")
                        elif x == "3/5":
                            fishing_percent.append("15%")
                        elif x == "4/5":
                            fishing_percent.append("4%")
                        elif x == "5/5":
                            fishing_percent.append("1%")

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(level + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Surfing (" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            surfing_percent) + "\n")

                    elif "Fishing (" in string:
                        f.write(level + "Fishing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Shaking Spots" in string:
                        f.write(level + "Shaking Spots" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Double Grass" in string:
                        f.write(level + "Double Grass" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Fishing Spots" in string:
                        f.write(
                            level + "Fishing Ripples" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                                fishing_percent) + "\n")

            # Functions for Black 2 and White 2 logs
            def extr_enc_bw2(string):
                level = ""

                clipped_string = string[string.find(") - ") + 4:]

                capital_string = stringfunc.capwords(clipped_string)

                enclist = re.findall(r'[A-z]{3,20}|Ho-Oh', capital_string)
                enclist = remove_values_from_list(enclist, 'Lvs')

                raritylist = []

                raritynumbers = []

                for mon in enclist:
                    if mon in pkmn_list and mon != 'Lvs':
                        raritylist.append(mon)
                        raritynumbers.append(str(enclist.index(mon) + 1) + "/" + str(len(enclist)))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                if len(raritylist) == 0:
                    return
                else:
                    hastype = "YES"

                floors = [
                    # B1F
                    ['Set #51', 'Set #52', 'Set #42', 'Set #179', 'Set #181', 'Set #272', 'Set #273',
                     ],
                    # B2F
                    ['Set #53', 'Set #54', 'Set #41',
                     ],
                    # 1F
                    ['Set #49', 'Set #50', 'Set #41', 'Set #338', 'Set #339', 'Set #178', 'Set #185', 'Set #183',
                     'Set #180',
                     'Set #184', 'Set #266', 'Set #267', 'Set #268', 'Set #269', 'Set #270', 'Set #271',
                     ],
                    # 2F
                    ['Set #347', 'Set #340', 'Set #341', 'Set #187', 'Set #186', 'Set #182'
                     ],
                    # 3F
                    ['Set #348',
                     ],
                    # 4F
                    ['Set #349',
                     ],
                    # Outside
                    ['Set #142', 'Set #143', 'Set #144', 'Set #145', 'Set #146', 'Set #147',
                     ],
                    # Inside
                    ['Set #148', 'Set #149', 'Set #40',
                     ],
                    # Celestial Tower Summit
                    ['Set #350',
                     ],
                    # Giant Chasm
                    ['Set #76', 'Set #77', 'Set #78', 'Set #79', 'Set #80', 'Set #81', 'Set #82', 'Set #83', 'Set #84',
                     'Set #85',
                     'Set #86', 'Set #87', 'Set #88', 'Set #89', 'Set #90', 'Set #91', 'Set #92', 'Set #93', 'Set #94',
                     'Set #95',
                     'Set #96',
                     ],
                    # Entrance
                    ['Set #39',
                     ],
                    # Relic Castle Lowest Floor
                    ['Set #43', 'Set #44', 'Set #45', 'Set #46', 'Set #47', 'Set #48',
                     ],
                    # Sewer Main
                    ['Set #97', 'Set #98', 'Set #99', 'Set #100', 'Set #101', 'Set #102', 'Set #103', 'Set #104',
                     'Set #105',
                     'Set #106', 'Set #112', 'Set #113', 'Set #114', 'Set #115', 'Set #116', 'Set #117', 'Set #118',
                     'Set #119',
                     'Set #120', 'Set #121', 'Set #107', 'Set #108', 'Set #109', 'Set #110', 'Set #111',
                     ],
                    # Relic Passage
                    ['Set #230', 'Set #231', 'Set #232', 'Set #233', 'Set #234', 'Set #235', 'Set #236', 'Set #237',
                     'Set #238',
                     'Set #239',
                     ],
                    # Reversal Mountain
                    ['Set #151', 'Set #152', 'Set #153', 'Set #154', 'Set #155', 'Set #156', 'Set #157', 'Set #158',
                     'Set #159',
                     'Set #160', 'Set #161', 'Set #162', 'Set #163', 'Set #164', 'Set #165', 'Set #166', 'Set #167',
                     'Set #168',
                     'Set #169', 'Set #170', 'Set #171', 'Set #172', 'Set #173', 'Set #174', 'Set #175', 'Set #176',
                     'Set #177',
                     ],

                ]
                for x in floors:
                    for y in x:
                        if y in string:
                            if floors.index(x) == 0:
                                if y == 'Set #181':
                                    level = "Library top rooms open - "
                                else:
                                    level = "B1F - "
                            elif floors.index(x) == 1:
                                if y == 'Set #58':
                                    level = "B2F (West) - "
                                else:
                                    level = "B2F - "
                            elif floors.index(x) == 2:
                                if y == 'Set #60':
                                    level = "1F (West) - "
                                elif y in ['Set #185', ]:
                                    level = "1F (Right Side) - "
                                elif y in ['Set #184', ]:
                                    level = "1F (Left Side) - "
                                elif y in ['Set #183', ]:
                                    level = "Lobby with top rooms open - "
                                elif y in ['Set #180', ]:
                                    level = "Lobby with bottom rooms open - "
                                else:
                                    level = "1F - "
                            elif floors.index(x) == 3:
                                if y in ['Set #187']:
                                    level = "2F (Right Side) - "
                                elif y in ['Set #186']:
                                    level = "2F (Left Side) - "
                                elif y in ['Set #182']:
                                    level = "2F (Middle) - "
                                else:
                                    level = "2F - "
                            elif floors.index(x) == 4:
                                if y in []:
                                    level = "3F (Right Side) - "
                                elif y in []:
                                    level = "3F (Left Side) - "
                                else:
                                    level = "3F - "
                            elif floors.index(x) == 5:
                                if y in []:
                                    level = "4F (Left Side) - "
                                elif y in []:
                                    level = "4F (Right Side) - "
                                else:
                                    level = "4F - "
                            elif floors.index(x) == 6:
                                level = "Outside - "
                            elif floors.index(x) == 7:
                                level = "Inside - "
                            elif floors.index(x) == 8:
                                level = "Summit - "
                            elif floors.index(x) == 9:
                                if y in ['Set #79', 'Set #80', 'Set #81', 'Set #82', 'Set #83', 'Set #84', ]:
                                    level = 'Cave - '
                                elif y in ['Set #76', 'Set #77', 'Set #78']:
                                    level = 'Entrance - '
                                elif y in ['Set #85', 'Set #86', 'Set #87']:
                                    level = 'Plains - '
                                else:
                                    level = "Cave Depths - "
                            elif floors.index(x) == 10:
                                level = "Entrance - "
                            elif floors.index(x) == 11 and 'Relic Castle' in string:
                                if y == 'Set #46':
                                    level = "Lowest Floor (Room 1) - "
                                elif y == 'Set #43':
                                    level = "Lowest Floor (Room 2) - "
                                elif y == 'Set #47':
                                    level = "Lowest Floor (Room 3) - "
                                elif y == 'Set #48':
                                    level = "Lowest Floor (Room 6) - "
                                elif y == 'Set #44':
                                    level = "Lowest Floor (Room 4) - "
                                elif y == 'Set #45':
                                    level = "Lowest Floor (North Room) - "
                                else:
                                    level = "Relic Castle Lowest Floor - "
                            elif floors.index(x) == 12:
                                if y in ['Set #102', 'Set #103', 'Set #104', 'Set #105', 'Set #106', ]:
                                    level = "West Door - "
                                elif y in ['Set #112', 'Set #113', 'Set #114', 'Set #115', 'Set #116', ]:
                                    level = "North-West Door - "
                                elif y in ['Set #117', 'Set #118', 'Set #119', 'Set #120', 'Set #121', ]:
                                    level = "Center Door - "
                                elif y in ['Set #107', 'Set #108', 'Set #109', 'Set #110', 'Set #111', ]:
                                    level = "East Door - "
                                else:
                                    level = ""
                            elif floors.index(x) == 13:
                                if y in ['Set #232', 'Set #233', 'Set #234', 'Set #235', 'Set #236', 'Set #237']:
                                    level = "Middle - "
                                elif y in ['Set #238', 'Set #239']:
                                    level = "Driftveil Exit - "
                                else:
                                    level = "Castelia Exit - "
                            elif floors.index(x) == 14:
                                if y in ['Set #151', 'Set #152', 'Set #153']:
                                    level = 'Outside Lentimas Town - '
                                else:
                                    level = "Unknown(Spots shuffle based on season) - "

                fishing_percent = []

                surfing_percent = []

                walking_percent = []

                if 'Grass/Cave' in string or 'Shaking Spots' in string or 'Doubles Grass' in string:
                    for x in raritynumbers:
                        if x in ["1/12", "2/12"]:
                            walking_percent.append("20%")
                        elif x in ["3/12", "4/12", "5/12", "6/12"]:
                            walking_percent.append("10%")
                        elif x in ["7/12", "8/12"]:
                            walking_percent.append("5%")
                        elif x in ["9/12", "10/12"]:
                            walking_percent.append("4%")
                        elif x in ["11/12", "12/12"]:
                            walking_percent.append("1%")
                elif "Surfing" in string:
                    for x in raritynumbers:
                        if x == "1/5":
                            surfing_percent.append("60%")
                        elif x == "2/5":
                            surfing_percent.append('30%')
                        elif x == "3/5":
                            surfing_percent.append("5%")
                        elif x == "4/5":
                            surfing_percent.append("4%")
                        elif x == "5/5":
                            surfing_percent.append("1%")
                elif "Fishing" in string:
                    for x in raritynumbers:
                        if x == "1/5" or "2/5":
                            fishing_percent.append("40%")
                        elif x == "3/5":
                            fishing_percent.append("15%")
                        elif x == "4/5":
                            fishing_percent.append("4%")
                        elif x == "5/5":
                            fishing_percent.append("1%")

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(level + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Surfing (" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            surfing_percent) + "\n")

                    elif "Fishing (" in string:
                        f.write(level + "Fishing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            fishing_percent) + "\n")

                    elif "Shaking Spots" in string:
                        f.write(level + "Shaking Spots" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Double Grass" in string:
                        f.write(level + "Double Grass" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            walking_percent) + "\n")

                    elif "Fishing Spots" in string:
                        f.write(
                            level + "Fishing Ripples" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                                fishing_percent) + "\n")

            # Functions for Gold, Silver and Crystal logs
            def extr_enc_gsc(string):
                level = ""

                clipped_string = string[string.find(") - ") + 4:]

                capital_string = stringfunc.capwords(clipped_string)

                enclist = re.findall(r'[A-z]{3,20}|Ho-Oh', capital_string)
                enclist = remove_values_from_list(enclist, 'Lvs')

                raritylist = []

                raritynumbers = []

                for mon in enclist:
                    if mon in pkmn_list and mon != 'Lvs':
                        raritylist.append(mon)
                        raritynumbers.append(str(enclist.index(mon) + 1) + "/" + str(len(enclist)))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                if len(raritylist) == 0:
                    return
                else:
                    hastype = "YES"

                floors = [
                    # B1
                    ['Set #34 - BURNED TOWER Grass/Cave (Morning)', 'Set #35 - BURNED TOWER Grass/Cave (Day)',
                     'Set #36 - BURNED TOWER Grass/Cave (Night)', 'Set #49 - UNION CAVE Grass/Cave (Morning)',
                     'Set #50 - UNION CAVE Grass/Cave (Day)', 'Set #51 - UNION CAVE Grass/Cave (Night)',
                     'Set #58 - SLOWPOKE WELL Grass/Cave (Morning)', 'Set #59 - SLOWPOKE WELL Grass/Cave (Day)',
                     'Set #60 - SLOWPOKE WELL Grass/Cave (Night)', 'Set #73 - MT.MORTAR Grass/Cave (Morning)',
                     'Set #74 - MT.MORTAR Grass/Cave (Day)', 'Set #75 - MT.MORTAR Grass/Cave (Night)',
                     'Set #100 - WHIRL ISLANDS Grass/Cave (Morning)', 'Set #101 - WHIRL ISLANDS Grass/Cave (Day)',
                     'Set #102 - WHIRL ISLANDS Grass/Cave (Night)', 'Set #106 - WHIRL ISLANDS Grass/Cave (Morning)',
                     'Set #107 - WHIRL ISLANDS Grass/Cave (Day)', 'Set #108 - WHIRL ISLANDS Grass/Cave (Night)',
                     'Set #12 - BURNED TOWER', 'Set #17 - UNION CAVE', 'Set #20 - SLOWPOKE WELL',
                     'Set #25 - MT.MORTAR Grass/Cave',
                     'Set #36 - WHIRL ISLANDS', 'Set #34 - WHIRL ISLANDSSet #34 - WHIRL ISLANDS', "Set #27 - ICE PATH",
                     'Set #79 - ICE PATH Grass/Cave (Morning)',
                     'Set #80 - ICE PATH Grass/Cave (Day)', 'Set #81 - ICE PATH Grass/Cave (Night)', ],
                    # B2
                    ['Set #52 - UNION CAVE Grass/Cave (Morning)', 'Set #53 - UNION CAVE Grass/Cave (Day)',
                     'Set #54 - UNION CAVE Grass/Cave (Night)', 'Set #82 - ICE PATH Grass/Cave (Morning)',
                     'Set #83 - ICE PATH Grass/Cave (Day)', 'Set #84 - ICE PATH Grass/Cave (Night)',
                     'Set #103 - WHIRL ISLANDS Grass/Cave (Morning)', 'Set #104 - WHIRL ISLANDS Grass/Cave (Day)',
                     'Set #105 - WHIRL ISLANDS Grass/Cave (Night)', 'Set #109 - WHIRL ISLANDS Grass/Cave (Morning)',
                     'Set #110 - WHIRL ISLANDS Grass/Cave (Day)', 'Set #111 - WHIRL ISLANDS Grass/Cave (Night)',
                     'Set #112 - WHIRL ISLANDS Grass/Cave (Morning)', 'Set #113 - WHIRL ISLANDS Grass/Cave (Day)',
                     'Set #114 - WHIRL ISLANDS Grass/Cave (Night)', 'Set #37 - WHIRL ISLANDS',
                     'Set #38 - WHIRL ISLANDS',
                     'Set #28 - ICE PATH Grass/Cave', ],
                    # B3
                    ['Set #85 - ICE PATH Grass/Cave (Morning)', 'Set #86 - ICE PATH Grass/Cave (Day)',
                     'Set #87 - ICE PATH Grass/Cave (Night)', 'Set #88 - ICE PATH Grass/Cave (Morning)',
                     'Set #89 - ICE PATH Grass/Cave (Day)',
                     'Set #90 - ICE PATH Grass/Cave (Night)', 'Set #29 - ICE PATH Grass/Cave',
                     'Set #30 - ICE PATH Grass/Cave', ],
                    # B4
                    [],
                    # F1
                    ["Set #1 - SPROUT TOWER Grass/Cave ", "Set #2 - SPROUT TOWER Grass/Cave",
                     "Set #3 - SPROUT TOWER Grass/Cave (Night)",
                     "Set #7 - TIN TOWER Grass/Cave (Morning)", "Set #8 - TIN TOWER Grass/Cave (Day)",
                     "Set #9 - TIN TOWER Grass/Cave (Night)", 'Set #31 - BURNED TOWER Grass/Cave (Morning)',
                     'Set #32 - BURNED TOWER Grass/Cave (Day)', 'Set #33 - BURNED TOWER Grass/Cave (Night)',
                     'Set #46 - UNION CAVE Grass/Cave (Morning)', 'Set #47 - UNION CAVE Grass/Cave (Day)',
                     'Set #48 - UNION CAVE Grass/Cave (Night)', 'Set #55 - SLOWPOKE WELL Grass/Cave (Morning)',
                     'Set #56 - SLOWPOKE WELL Grass/Cave (Day)', 'Set #57 - SLOWPOKE WELL Grass/Cave (Night)',
                     'Set #65 - MT.MORTAR Grass/Cave (Day)', 'Set #66 - MT.MORTAR Grass/Cave (Night)',
                     'Set #67 - MT.MORTAR Grass/Cave (Morning)', 'Set #68 - MT.MORTAR Grass/Cave (Day)',
                     'Set #69 - MT.MORTAR Grass/Cave (Night)', 'Set #70 - MT.MORTAR Grass/Cave (Morning)',
                     'Set #71 - MT.MORTAR Grass/Cave (Day)', 'Set #72 - MT.MORTAR Grass/Cave (Night)',
                     'Set #76 - ICE PATH Grass/Cave (Morning)', 'Set #77 - ICE PATH Grass/Cave (Day)',
                     'Set #78 - ICE PATH Grass/Cave (Night)',
                     'Set #91 - WHIRL ISLANDS Grass/Cave (Morning)', 'Set #92 - WHIRL ISLANDS Grass/Cave (Day)',
                     'Set #93 - WHIRL ISLANDS Grass/Cave (Night)', 'Set #94 - WHIRL ISLANDS Grass/Cave (Morning)',
                     'Set #95 - WHIRL ISLANDS Grass/Cave (Day)', 'Set #96 - WHIRL ISLANDS Grass/Cave (Night)',
                     'Set #97 - WHIRL ISLANDS Grass/Cave (Morning)', 'Set #98 - WHIRL ISLANDS Grass/Cave (Day)',
                     'Set #99 - WHIRL ISLANDS Grass/Cave (Night)', 'Set #3 - TIN TOWER', 'Set #11 - BURNED TOWER',
                     'Set #16 - UNION CAVE', 'Set #19 - SLOWPOKE WELL', 'Set #22 - MT.MORTAR', 'Set #23 - MT.MORTAR',
                     'Set #24 - MT.MORTAR', 'Set #26 - ICE PATH', 'Set #31 - WHIRL ISLANDS', 'Set #32 - WHIRL ISLANDS',
                     'Set #33 - WHIRL ISLANDS', ],
                    # F2
                    ["Set #10 - TIN TOWER Grass/Cave (Morning)", 'Set #11 - TIN TOWER Grass/Cave (Day)',
                     'Set #12 - TIN TOWER Grass/Cave (Night)', 'Set #2 - SPROUT TOWER', 'Set #4 - TIN TOWER',
                     ],
                    # F3
                    ['Set #13 - TIN TOWER Grass/Cave (Morning)', 'Set #14 - TIN TOWER Grass/Cave (Day)',
                     'Set #15 - TIN TOWER Grass/Cave (Night)', 'Set #5 - TIN TOWER', ],
                    # F4
                    ['Set #16 - TIN TOWER Grass/Cave (Morning)', 'Set #17 - TIN TOWER Grass/Cave (Day)',
                     'Set #18 - TIN TOWER Grass/Cave (Night)', 'Set #6 - TIN TOWER', ],
                    # F5
                    ['Set #19 - TIN TOWER Grass/Cave (Morning)', 'Set #20 - TIN TOWER Grass/Cave (Day)',
                     'Set #21 - TIN TOWER Grass/Cave (Night)', 'Set #7 - TIN TOWER', ],
                    # F6
                    ['Set #22 - TIN TOWER Grass/Cave (Morning)', 'Set #23 - TIN TOWER Grass/Cave (Day)',
                     'Set #24 - TIN TOWER Grass/Cave (Night)', 'Set #8 - TIN TOWER', ],
                    # F7
                    ['Set #25 - TIN TOWER Grass/Cave (Morning)', 'Set #26 - TIN TOWER Grass/Cave (Day)',
                     'Set #27 - TIN TOWER Grass/Cave (Night)', 'Set #9 - TIN TOWER', ],
                    # f8
                    ['Set #28 - TIN TOWER Grass/Cave (Morning)', 'Set #29 - TIN TOWER Grass/Cave (Day)',
                     'Set #30 - TIN TOWER Grass/Cave (Night)', 'Set #10 - TIN TOWER', ],
                    # Entrance
                    ['Set #115 - SILVER CAVE Grass/Cave (Morning)', 'Set #116 - SILVER CAVE Grass/Cave (Day)',
                     'Set #117 - SILVER CAVE Grass/Cave (Night)', 'Set #39 - SILVER CAVE', ],
                    # Inside
                    ['Set #118 - SILVER CAVE Grass/Cave (Morning)', 'Set #119 - SILVER CAVE Grass/Cave (Day)',
                     'Set #120 - SILVER CAVE Grass/Cave (Night)', 'Set #40 - SILVER CAVE', ],
                    # Outside
                    ['Set #181 - SILVER CAVE Grass/Cave (Morning)', 'Set #182 - SILVER CAVE Grass/Cave (Day)',
                     'Set #183 - SILVER CAVE Grass/Cave (Night)', 'Set #61 - SILVER CAVE', ],
                    # Deepest
                    ['Set #121 - SILVER CAVE Grass/Cave (Morning)', 'Set #122 - SILVER CAVE Grass/Cave (Day)',
                     'Set #123 - SILVER CAVE Grass/Cave (Night)', 'Set #41 - SILVER CAVE', ],
                    # Waterfall
                    ['Set #124 - SILVER CAVE Grass/Cave (Morning)', 'Set #125 - SILVER CAVE Grass/Cave (Day)',
                     'Set #126 - SILVER CAVE Grass/Cave (Night)', 'Set #42 - SILVER CAVE', ],
                    # Route 31
                    ['Set #127 - DARK CAVE Grass/Cave (Morning)', 'Set #128 - DARK CAVE Grass/Cave (Day)',
                     'Set #129 - DARK CAVE Grass/Cave (Night)', 'Set #43 - DARK CAVE', ],
                    # Route 45
                    ['Set #130 - DARK CAVE Grass/Cave (Morning)', 'Set #131 - DARK CAVE Grass/Cave (Day)',
                     'Set #132 - DARK CAVE Grass/Cave (Night)', 'Set #44 - DARK CAVE', ],

                ]
                for x in floors:
                    for y in x:
                        if y in string:
                            if floors.index(x) == 0:
                                level = "B1F - "
                            elif floors.index(x) == 1:
                                level = "B2F - "
                            elif floors.index(x) == 2:
                                level = "B3F - "
                            elif floors.index(x) == 3:
                                level = "B4F - "
                            elif floors.index(x) == 4:
                                level = "1F - "
                            elif floors.index(x) == 5:
                                level = "2F - "
                            elif floors.index(x) == 6:
                                level = "3F - "
                            elif floors.index(x) == 7:
                                level = "4F - "
                            elif floors.index(x) == 8:
                                level = "5F - "
                            elif floors.index(x) == 9:
                                level = "6F - "
                            elif floors.index(x) == 10:
                                level = "7F - "
                            elif floors.index(x) == 11:
                                level = "8F - "
                            elif floors.index(x) == 12:
                                level = "Entrance - "
                            elif floors.index(x) == 13:
                                level = "Inside - "
                            elif floors.index(x) == 14:
                                level = "Outside - "
                            elif floors.index(x) == 15:
                                level = "Deepest - "
                            elif floors.index(x) == 16:
                                level = "Waterfall - "
                            elif floors.index(x) == 17:
                                level = "Route 31 - "
                            elif floors.index(x) == 18:
                                level = "Route 45 - "

                time_of_day = ""

                surfing_percent = []

                walking_percent = []

                if "Grass/Cave" in string:
                    for x in raritynumbers:
                        if x in ["1/7", "2/7"]:
                            walking_percent.append("30%")
                        elif x == "3/7":
                            walking_percent.append("20%")
                        elif x == "4/7":
                            walking_percent.append("10%")
                        elif x == "5/7":
                            walking_percent.append("5%")
                        elif x == "6/7":
                            walking_percent.append("4%")
                        elif x == "7/7":
                            walking_percent.append("1%")

                elif "Surfing" in string:
                    for x in raritynumbers:
                        if x == "1/3":
                            surfing_percent.append("60%")
                        elif x == "2/3":
                            surfing_percent.append('30%')
                        elif x == "3/3":
                            surfing_percent.append("10%")

                if "Morning" in string:
                    time_of_day = "Morning "
                elif "Day" in string:
                    time_of_day = "Day "
                elif "Night" in string:
                    time_of_day = "Night "

                if hastype == "YES":
                    if "Grass/Cave" in string:
                        f.write(
                            level + time_of_day + "Grass/Cave" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                                walking_percent) + "\n")

                    elif "Surfing" in string:
                        f.write(level + "Surfing" + ": " + "Frequency: " + frequencynumber + " | Rarity: " + str(
                            surfing_percent) + "\n")

            # Functions for X and Y logs
            def extr_enc6(string):
                clipped_string = string[string.find(": ") + 2:]

                route_names = re.findall("(.*?):", string, re.I)[0]

                enclist = clipped_string.split("), ")

                encdict = {}

                n = 0
                while n < len(enclist):
                    for x in enclist:
                        n += 1
                        encdict[n] = x

                raritylist = []

                for x, y in encdict.items():
                    for z in pkmn_list:
                        if z in y:
                            raritylist.append(encdict.get(x))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enclist))

                raritynumbers = []

                for x in raritylist:
                    if "Swarm" in route_names:
                        raritynumbers.append(re.findall(r'\?%', x)[0])

                    elif "Horde" not in route_names:
                        raritynumbers.append(re.findall(r'\d{1,3}%', x)[0])

                if len(raritylist) == 0:
                    hastype = "NO"
                else:
                    hastype = "YES"

                if hastype == "YES" and "Horde" not in route_names:
                    f.write(
                        str(route_names) + ": Frequency: " + frequencynumber + " | Rarity: " + str(
                            raritynumbers) + "\n")
                elif hastype == "YES":
                    f.write(str(route_names) + ": Frequency: " + frequencynumber + "\n")

            # Function for Sun and Moon logs
            def extr_enc_sm(string):
                level_range = re.findall(r'\(Levels \d{1,2}-\d{1,2}\)', string)[0]
                table_name = re.findall(r'Table \d{1,2} \(.*\)', string)[0]
                clipped_string = re.findall(r'\d\): (.*)', string)[0]
                enc_list = clipped_string.split(", ")
                enc_dict = {}

                n = 0
                while n < len(enc_list):
                    for x in enc_list:
                        n += 1
                        enc_dict[n] = x

                raritylist = []

                for x, y in enc_dict.items():
                    for z in pkmn_list:
                        if z in y:
                            raritylist.append(enc_dict.get(x))

                frequencynumber = str(len(raritylist)) + "/" + str(len(enc_list))

                raritynumbers = []

                for x in raritylist:
                    raritynumbers.append(re.findall(r'\(\d{1,3}%\)', x)[0])

                if len(raritylist) == 0:
                    hastype = "NO"
                else:
                    hastype = "YES"

                if hastype == "YES":
                    f.write(
                        table_name + level_range + ": Frequency: " + frequencynumber + " | Rarity: " + str(
                            raritynumbers) + '\n')

            def parser(parse_routelist, encounterfunc):
                window['progbar'].update_bar(0, max=len(routelist) - 1)
                try:
                    log = open(values['-LOG-'], encoding="utf8")
                except FileNotFoundError:
                    sg.popup('Select a log to Parse')
                    f.close()
                    os.remove(filename)
                    return
                lines = log.read()
                log.close()
                i = 0
                # Create Header For File
                file_title = f'{game} - {pkmntype} Encounters'
                file_header = f'\n' + '=' * 86 + '\n' + file_title.center(86, " ") + '\n' + '=' * 86 + '\n'
                f.write(file_header)

                def static(string):
                    separate = string.split(" => ")
                    encounter = separate[0]
                    catch = separate[1]
                    encounter = encounter.capitalize()
                    catch = catch.capitalize()
                    if catch in pkmn_list:
                        f.write(encounter + '\n')

                if game in ["Red", "Blue", "Gold", "Silver", "Crystal", "Yellow", "Ruby", "Sapphire", "Emerald",
                            "FireRed",
                            "LeafGreen", "Diamond", "Pearl", "Platinum", "HeartGold", "SoulSilver", "Black", "White",
                            "Black 2",
                            "White 2"]:
                    while i < len(parse_routelist):
                        window['progbar'].update_bar(i)
                        route = parse_routelist[i]
                        route_header = f'\n' + '=' * 86 + '\n' + route.center(86, " ") + '\n' + '=' * 86 + '\n'
                        pattern = re.findall(r'.*' + re.escape(route) + r'.*', lines, re.I)
                        pattern_lower = pattern[0].lower()
                        if route.lower() in pattern_lower and route != 'Static Pokemon':
                            if route == 'Set #22 - Surfing on SEA ROUTE 19':
                                route = 'Sea Route 19'
                            elif route == 'Set #23 - Surfing on SEA ROUTE 20':
                                route = 'Sea Route 20'
                            elif route == 'Dewford':
                                route = 'Dewford Town'
                            elif route == 'Diglett\'s Cave':
                                route = "Diglett's Cave"
                            elif route == 'Dragon\'s Den':
                                route = "Dragon’s Den"
                            elif route == 'SLATEPORT':
                                route = 'Slateport City'
                            elif route == 'PETALBURG':
                                route = 'Petalburg City'
                            elif route == 'LILYCOVE':
                                route = 'Lilycove City'
                            elif route == 'MOSSDEEP':
                                route = 'Mossdeep City'
                            elif route == '[pk] Mansion':
                                route = "Pk Mansion"
                            elif route == '[poké]mon tower':
                                route = "Pokémon Tower"
                            elif route == 'SOOTOPOLIS':
                                route = 'Sootopolis City'
                            route_header = f'\n' + '=' * 86 + '\n' + route.center(86, " ") + '\n' + '=' * 86 + '\n'
                            f.write(route_header)
                            for match in pattern:
                                encounterfunc(match)
                            else:
                                i += 1
                        else:
                            if route == 'Static Pokemon':
                                f.write(route_header)
                                if game == 'Emerald':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){26})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1
                                elif game == 'Crystal':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){41})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1
                                elif game == 'Ruby' or 'Sapphire':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){18})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1
                                elif game == 'FireRed' or 'LeafGreen' or 'Diamond' or 'Pearl' or 'Platinum':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){26})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1
                                elif game == 'Gold' or 'Silver':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){29})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1
                                elif game == 'HeartGold' or 'SoulSilver':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){46})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1
                                elif game == 'Black' or 'White':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){31})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1
                                elif game == 'Black 2' or 'White 2':
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){31})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)
                                    else:
                                        i += 1

                                else:
                                    static_enc = re.findall(r'static pokemon.*\n((?:.*\n){33})', lines.lower(), re.I)
                                    static_split = static_enc[0].split('\n')
                                    for match in static_split:
                                        if match == '':
                                            i += 1
                                            break
                                        else:
                                            static(match)

                elif game in ['X', 'Y', 'Omega Ruby', 'Alpha Sapphire']:
                    while i < len(parse_routelist):
                        window['progbar'].update_bar(i)
                        pattern = re.findall(parse_routelist[i] + r'.*\n(?:.*\n){12}', lines)
                        route = parse_routelist[i][10:]
                        route_check = parse_routelist[i][:7]
                        encounters = pattern[0].split('\n')
                        encounters = encounters[2:13]
                        route1 = ''

                        route1_list = []
                        route2_list = []
                        route3_list = []
                        route4_list = []
                        route5_list = []
                        route6_list = []
                        route7_list = []
                        route8_list = []
                        route9_list = []
                        route10_list = []
                        route11_list = []
                        route12_list = []

                        if game in ['X', 'Y']:
                            route1_list = ["Map 303", "Map 305", "Map 313", "Map 343", "Map 322"]
                            route2_list = ["Map 304", "Map 306", "Map 314", "Map 344", ]
                            route3_list = ["Map 307", "Map 315", "Map 345", "Map 324", ]
                            route4_list = ["Map 308", "Map 316", ]
                            route5_list = ["Map 307", "Map 317", "Map 347", "Map 326", ]
                            route6_list = ["Map 348", "Map 327", ]
                            route7_list = ["Map 328", ]
                        elif game in ['Omega Ruby', 'Alpha Sapphire']:
                            route1_list = ['Map 026', 'Map 078', 'Map 035', 'Map 038', 'Map 071', 'Map 046', 'Map 048',
                                           'Map 164',
                                           'Map 219',
                                           'Map 086', 'Map 053', 'Map 057', 'Map 055', 'Map 112', 'Map 058', 'Map 059',
                                           'Map 145',
                                           'Map 123', ]
                            route2_list = ['Map 027', 'Map 079', 'Map 039', 'Map 072', 'Map 047', 'Map 049', 'Map 165',
                                           'Map 220',
                                           'Map 087',
                                           'Map 065', 'Map 068', 'Map 099', 'Map 066', 'Map 113', 'Map 069', 'Map 070',
                                           'Map 146',
                                           'Map 124', ]
                            route3_list = ['Map 080', 'Map 037', 'Map 073', 'Map 166', 'Map 221', 'Map 088', 'Map 100',
                                           'Map 114',
                                           'Map 125', ]
                            route4_list = ['Map 074', 'Map 167', 'Map 222', 'Map 089', 'Map 101', 'Map 115',
                                           'Map 126', ]
                            route5_list = ['Map 090', 'Map 102', 'Map 116', ]
                            route6_list = ['Map 091', 'Map 103', ]
                            route7_list = ['Map 104', 'Map 151', ]
                            route8_list = ['Map 105', ]
                            route9_list = ['Map 106', ]
                            route10_list = ['Map 107', ]
                            route11_list = ['Map 108', ]
                            route12_list = ['Map 109', 'Map 156', ]

                        if route_check in route1_list:
                            route1 = route + " (1)"
                        elif route_check in route2_list:
                            route1 = route + " (2)"
                        elif route_check in route3_list:
                            route1 = route + " (3)"
                        elif route_check in route4_list:
                            route1 = route + " (4)"
                        elif route_check in route5_list:
                            route1 = route + " (5)"
                        elif route_check in route6_list:
                            route1 = route + " (6)"
                        elif route_check in route7_list:
                            route1 = route + " (7)"
                        elif route_check in route8_list:
                            route1 = route + " (8)"
                        elif route_check in route9_list:
                            route1 = route + " (9)"
                        elif route_check in route10_list:
                            route1 = route + " (10)"
                        elif route_check in route11_list:
                            route1 = route + " (11)"
                        elif route_check in route12_list:
                            route1 = route + " (12)"

                        if route1 != '':
                            route_header = f'\n' + '=' * 86 + '\n' + route1.center(86, " ") + '\n' + '=' * 86 + '\n'
                            f.write(route_header)
                            for e in encounters:
                                encounterfunc(e)
                            else:
                                i += 1
                        elif route in parse_routelist[i]:
                            route_header = f'\n' + '=' * 86 + '\n' + route.center(86, " ") + '\n' + '=' * 86 + '\n'
                            f.write(route_header)
                            for encounter1 in encounters:
                                encounterfunc(encounter1)
                            else:
                                i += 1
                        else:
                            i += 1
                elif game in ["Sun", "Moon", "Ultra Sun", "Ultra Moon", ]:
                    while i < len(parse_routelist):
                        window['progbar'].update_bar(i)
                        pattern = re.findall(re.escape(parse_routelist[i]) + r'.*?Map', lines, re.S)
                        matches = ''.join(pattern)
                        day_tables = re.findall(r'Table \d{1,2} \(Day\):\n.*', matches)
                        night_tables = re.findall(r'Table \d{1,2} \(Night\):\n.*', matches)
                        route = re.findall(r'.*', matches)[0]
                        f.write('\n' + '=' * 86 + '\n' + route.center(86, " ") + '\n' + '=' * 86 + '\n')
                        for tables in day_tables:
                            extr_enc_sm(tables)
                        for tables in night_tables:
                            extr_enc_sm(tables)
                        else:
                            i += 1

            if game in ["Red", "Blue", "Yellow"]:
                parser(routelist, extr_enc_rby)
            elif game in ["Gold", "Silver", "Crystal"]:
                parser(routelist, extr_enc_gsc)
            elif game in ["Ruby", "Sapphire", "Emerald"]:
                parser(routelist, extr_enc_rse)
            elif game in ["FireRed", "LeafGreen"]:
                parser(routelist, extr_enc_frlg)
            elif game in ["Diamond", "Pearl", "Platinum"]:
                parser(routelist, extr_enc_dpp)
            elif game in ["HeartGold", "SoulSilver"]:
                parser(routelist, extr_enc_hgss)
            elif game in ["Black", "White"]:
                parser(routelist, extr_enc_bw)
            elif game in ["Black 2", "White 2"]:
                parser(routelist, extr_enc_bw2)
            elif game in ["X", "Y"]:
                parser(routelist, extr_enc6)
            elif game in ["Omega Ruby", "Alpha Sapphire"]:
                parser(routelist, extr_enc6)
            elif game in ["Sun", "Moon", ]:
                parser(routelist, extr_enc_sm)
            elif game in ["Ultra Sun", "Ultra Moon", ]:
                parser(routelist, extr_enc_sm)
            if f != 'none':
                f.close()
    window.close()


main()
