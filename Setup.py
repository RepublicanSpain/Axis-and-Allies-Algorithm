##############################################################################
# This will be the function to set up the game
#  - Instantiate each power
#  - Insantiate each territory along with its adjacent territories
#  - Put each territory into its respective power
#  - Put units in their respective territories
##############################################################################

import Powers
import Territories as t
import Units as u

def setup():
    isValid = False
    while not isValid:
        player = input("Which Power would you like to play as?\nUSSR\nGermany\nUK\nJapan\nUS")
        if player == "USSR" or player == "Germany" or player == "UK" or player == "Japan" or player == "US":
            isValid = True

#Create Powers
    if player == 'USSR':
        USSR = Powers.Power("Allies", [], 24, "USSR", True)
    else:
        USSR = Powers.Power("Allies", [], 24, "USSR", False)

    if player == 'Germany':
        Germany = Powers.Power("Axis", [], 32, "Germany", True)
    else:
        Germany = Powers.Power("Axis", [], 32, "Germany", False)

    if player == 'UK':
        UK = Powers.Power("Allies", [], 30, "UK", True)
    else:
        UK = Powers.Power("Allies", [], 30, "UK", False)

    if player == 'Japan':
        Japan = Powers.Power("Axis", [], 25, "Japan", True)
    else:
        Japan = Powers.Power("Axis", [], 25, "Japan", False)

    if player == 'US':
        US = Powers.Power("Allies", [], 36, "US", True)
    else:
        US = Powers.Power("Allies", [], 36, "US", False)

    neutral = Powers.Power("neutral", [], 0, "neutral", False)
    
#Create Territories with their units (without adj territories)
    #Create Land Territories
    eastern_canada = t.Land("UK", [], [u.Tank(power=UK)], "Eastern Canada", 3, 0, False)
    eastern_usa = t.Land("US", [], [u.Infantry(power=US) for x in range(2)] + [u.Bomber(power=US), u.Fighter(power=US), u.Tank(power=US), u.AntiAircraft(power=US)], "Eastern USA", 12, 2, True)
    west_indies = t.Land("US", [], [], "West Indies", 1, 0, False)
    panama = t.Land("US", [], [], "Panama", 1, 0, False)
    venezuela = t.Land("neutral", [], [], "Venezuela", 0, 0, False)
    peru = t.Land("neutral", [], [], "Peru", 0, 0, False)
    argentina = t.Land("neutral", [], [], "Argentina", 0, 0, False)
    brazil = t.Land("US", [], [], "Brazil", 3, 0, False)
    united_kingdom = t.Land("UK", [], [u.Infantry(power=UK) for x in range(2)] + [u.Tank(power=UK), u.AntiAircraft(power=UK)] + [u.Fighter(power=UK) for x in range(2)] + [u.Bomber(power=UK)], "United Kingdom", 8, 2, True)
    spain = t.Land("neutral", [], [], "Spain", 0, 0, False)
    gibraltar = t.Land("UK", [], [], "Gibraltar", 0, 0, False)
    western_europe = t.Land("Germany", [], [u.Infantry(power=Germany) for x in range(2)] + [u.Tank(power=Germany) for x in range(2)] + [u.Fighter(power=Germany), u.AntiAircraft(power=Germany)], "Western Europe", 6, 0, True)
    switz = t.Land("neutral", [], [], "Switz", 0, 0, False)
    finland = t.Land("Germany", [], [u.Infantry(power=Germany) for x in range(3)] + [u.Tank(power=Germany), u.Fighter(power=Germany)], "Finland", 2, 0, False)
    sweden = t.Land("neutral", [], [], "Sweden", 0, 0, False)
    germany = t.Land("Germany", [], [u.Infantry(power=Germany) for x in range(4)] + [u.Tank(power=Germany) for x in range(2)] + [u.Fighter(power=Germany), u.Bomber(power=Germany), u.AntiAircraft(power=Germany)], "Germany", 10, 2, True)
    southern_europe = t.Land("Germany", [], [u.Infantry(power=Germany) for x in range(2)] + [u.Tank(power=Germany), u.AntiAircraft(power=Germany)], "Southern Europe", 6, 2, False)
    eastern_europe = t.Land("Germany", [], [u.Infantry(power=Germany) for x in range(3)] + [u.Tank(power=Germany), u.Fighter(power=Germany)], "Eastern Europe", 3, 0, False)
    ukraine = t.Land("Germany", [], [u.Infantry(power=Germany) for x in range(3)] + [u.Tank(power=Germany) for x in range(2)] + [u.Fighter(power=Germany)], "Ukraine", 3, 0, False)
    algeria = t.Land("Germany", [], [u.Infantry(power=Germany)], "Algeria", 1, 0, False)
    libya = t.Land("Germany", [], [u.Infantry(power=Germany), u.Tank(power=Germany)], "Libya", 1, 0, False)
    west_africa = t.Land("UK", [], [], "West Africa", 1, 0, False)
    equatorial_africa = t.Land("UK", [], [], "Equatorial Africa", 1, 0, False)
    egypt = t.Land("UK", [], [u.Infantry(power=UK), u.Tank(power=UK)], "Egypt", 2, 0, False)
    congo = t.Land("UK", [], [], "Congo", 1, 0, False)
    east_africa = t.Land("UK", [], [], "East Africa", 1, 0, False)
    angola = t.Land("neutral", [], [], "Angola", 0, 0, False)
    kenya = t.Land("UK", [], [], "Kenya", 1, 0, False)
    south_africa = t.Land("UK", [], [u.Infantry(power=UK)], "South Africa", 2, 0, False)
    mozambique = t.Land("neutral", [], [], "Mozambique", 0, 0, False)
    madagascar = t.Land("UK", [], [], "Madagascar", 1, 0, False)
    karelia = t.Land("USSR", [], [u.Infantry(power=USSR) for x in range(3)] + [u.Tank(power=USSR), u.Fighter(power=USSR), u.AntiAircraft(power=USSR)], "Karelia", 3, 2, False)
    caucasus = t.Land("USSR", [], [u.Infantry(power=USSR) for x in range(5)], "Caucasus", 3, 0, False)
    turkey = t.Land("neutral", [], [], "Turkey", 0, 0, False)
    syria = t.Land("UK", [], [u.Infantry(power=UK)], "Syria", 1, 0, False)
    persia = t.Land("UK", [], [], "Persia", 1, 0, False)
    saudi_arabia = t.Land("neutral", [], [], "Saudi Arabia", 0, 0, False)
    russia = t.Land("USSR", [], [u.Infantry(power=USSR) for  x in range(4)] + [u.Tank(power=USSR) for x in range(2)] + [u.Fighter(power=USSR), u.AntiAircraft(power=USSR)], "Russia", 8, 2, True)
    kazakh = t.Land("USSR", [], [], "Kazakh", 2, 0, False)
    afghan = t.Land("neutral", [], [], "Afghan", 0, 0, False)
    india = t.Land("UK", [], [u.Infantry(power=UK) for x in range(2)] + [u.Fighter(power=UK)], "India", 3, 0, False)
    evenki = t.Land("USSR", [], [u.Infantry(power=USSR) for x in range(2)], "Evenki", 2, 0, False)
    novosibirsk = t.Land("USSR", [], [], "Novosibirsk", 2, 0, False)
    sinkiang = t.Land("US", [], [u.Infantry(power=US) for x in range(2)], "Sinkiang", 2, 0, False)
    yakut = t.Land("USSR", [], [u.Infantry(power=Japan) for x in range(3)], "Yakut", 2, 0, False)
    mongolia = t.Land("neutral", [], [], "Mongolia", 0, 0, False)
    china = t.Land("US", [], [u.Infantry(power=Japan) for x in range(2)] + [u.Fighter(power=US)], "China", 2, 0, False)
    indochina = t.Land("Japan", [], [u.Infantry(power=Japan) for x in range(2)] + [u.Fighter(power=Japan)], "Indochina", 3, 0, False)
    kwangtung = t.Land("Japan", [], [u.Infantry(power=Japan) for x in range(2)], "Kwantung", 3, 0, False)
    manchuria = t.Land("Japan", [], [u.Infantry(power=Japan) for x in range(3)] + [u.Fighter(power=Japan)], "Manchuria", 3, 0, False)
    soviet_east = t.Land("USSR", [], [u.Infantry(power=USSR) for x in range(2)] + [u.Tank(power=USSR)], "Soviet East", 2, 0, False)
    east_indies = t.Land("Japan", [], [u.Infantry(power=Japan)], "East Indies", 2, 0, False)
    borneo = t.Land("Japan", [], [u.Infantry(power=Japan)], "Borneo", 1, 0, False)
    philippine_islands = t.Land("Japan", [], [u.Infantry(power=Japan) for x in range(2)] + [u.Fighter(power=Japan)], "Philippine Islands", 3, 0, False)
    australia = t.Land("UK", [], [u.Infantry(power=UK) for x in range(2)], "Australia", 2, 0, False)
    new_guinea = t.Land("Japan", [], [u.Infantry(power=Japan)], "New Guinea", 1, 0, False)
    caroline_islands = t.Land("Japan", [], [u.Infantry(power=Japan)], "Caroline Islands", 0, 0, False)
    new_zealand = t.Land("UK", [], [], "New Zealand", 1, 0, False)
    solomon_islands = t.Land("Japan", [], [u.Infantry(power=Japan)], "Solomon Island", 0, 0, False)
    okinawa = t.Land("Japan", [], [u.Infantry(power=Japan)], "Okinawa", 0, 0, False)
    wake_island = t.Land("Japan", [], [u.Infantry(power=Japan)], "Wake Island", 0, 0, False)
    japan = t.Land("Japan", [], [u.Infantry(power=Japan) for x in range(3)] + [u.Tank(power=Japan), u.AntiAircraft(power=Japan)], "Japan", 8, 0, True)
    alaska = t.Land("US", [], [u.Infantry(power=US)], "Alaska", 2, 0, False)
    midway_island = t.Land("US", [], [u.Infantry(power=US)], "Midway Island", 0, 0, False)
    hawaiian_islands = t.Land("US", [], [u.Infantry(power=US)], "Hawaiian Islands", 1, 0, False)
    western_canada = t.Land("UK", [], [u.Infantry(power=UK)], "Wester Canada", 1, 0, False)
    western_usa = t.Land("US", [], [u.Infantry(power=US) for x in range(2)] + [u.Fighter(power=US)], "Western USA", 10, 2, False)
    mexico = t.Land("US", [], [], "Mexico", 2, 0, False)
    
    
    #Create Sea Territories
    zone_1 = t.Sea("neutral", [], [], "zone_1", 0)
    zone_2 = t.Sea("US", [], [u.Transport(power=US)], "zone_2", 0)
    zone_3 = t.Sea("neutral", [], [], "zone_3", 0)
    zone_4 = t.Sea("neutral", [], [], "zone_4", 0)
    zone_5 = t.Sea("neutral", [], [], "zone_5", 0)
    zone_6 = t.Sea("UK", [], [u.Transport(power=UK)], "zone_6", 0)
    zone_7 = t.Sea("neutral", [], [], "zone_7", 0)
    zone_8 = t.Sea("neutral", [], [], "zone_8", 0)
    zone_9 = t.Sea("neutral", [], [], "zone_9", 0)
    zone_10 = t.Sea("UK", [], [u.Transport(power=UK), u.Battleship(power=UK)], "zone_10", 0)
    zone_11 = t.Sea("Germany", [], [u.Submarine(power=Germany)], "zone_11", 0)
    zone_12 = t.Sea("neutral", [], [], "zone_12", 0)
    zone_13 = t.Sea("neutral", [], [], "zone_13", 0)
    zone_14 = t.Sea("neutral", [], [], "zone_14", 0)
    zone_15 = t.Sea("neutral", [], [], "zone_15", 0)
    zone_16 = t.Sea("USSR", [], [u.Transport(power=USSR), u.Submarine(power=USSR)], "zone_16", 0)
    zone_17 = t.Sea("Germany", [], [u.Transport(power=Germany), u.Submarine(power=Germany)], "zone_17", 0)
    zone_18 = t.Sea("UK", [], [u.Battleship(power=UK)], "zone_18", 0)
    zone_19 = t.Sea("Germany", [], [u.Transport(power=Germany), u.Battleship(power=Germany)], "zone_19", 0)
    zone_20 = t.Sea("neutral", [], [], "zone_20", 0)
    zone_21 = t.Sea("UK", [], [u.Submarine(power=UK)], "zone_21", 0)
    zone_22 = t.Sea("neutral", [], [], "zone_22", 0)
    zone_23 = t.Sea("neutral", [], [], "zone_23", 0)
    zone_24 = t.Sea("neutral", [], [], "zone_24", 0)
    zone_25 = t.Sea("neutral", [], [], "zone_25", 0)
    zone_26 = t.Sea("neutral", [], [], "zone_26", 0)
    zone_27 = t.Sea("UK", [], [u.Transport(power=UK)], "zone_27", 0)
    zone_28 = t.Sea("neutral", [], [], "zone_28", 0)
    zone_29 = t.Sea("neutral", [], [], "zone_29", 0)
    zone_30 = t.Sea("neutral", [], [], "zone_30", 0)
    zone_31 = t.Sea("neutral", [], [], "zone_31", 0)
    zone_32 = t.Sea("neutral", [], [], "zone_32", 0)
    zone_33 = t.Sea("Japan", [], [u.Transport(power=Japan)], "zone_33", 0)
    zone_34 = t.Sea("neutral", [], [], "zone_34", 0)
    zone_35 = t.Sea("neutral", [], [], "zone_35", 0)
    zone_36 = t.Sea("Japan", [], [u.Transport(power=Japan), u.Battleship(power=Japan)], "zone_36", 0)
    zone_37 = t.Sea("neutral", [], [], "zone_37", 0)
    zone_38 = t.Sea("Japan", [], [u.Battleship(power=Japan), u.Carrier(power=Japan).add_cargo(u.Fighter(power=Japan))], "zone_38", 0)
    zone_39 = t.Sea("neutral", [], [], "zone_39", 0)
    zone_40 = t.Sea("neutral", [], [], "zone_40", 0)
    zone_41 = t.Sea("neutral", [], [], "zone_41", 0)
    zone_42 = t.Sea("neutral", [], [], "zone_42", 0)
    zone_43 = t.Sea("neutral", [], [], "zone_43", 0)
    zone_44 = t.Sea("Japan", [], [u.Submarine(power=Japan)], "zone_44", 0)
    zone_45 = t.Sea("neutral", [], [], "zone_45", 0)
    zone_46 = t.Sea("neutral", [], [], "zone_46", 0)
    zone_47 = t.Sea("neutral", [], [], "zone_47", 0)
    zone_48 = t.Sea("US", [], [u.Transport(power=US), u.Battleship(power=US)], "zone_48", 0)
    zone_49 = t.Sea("US", [], [u.Submarine(power=US), u.Carrier(power=US).add_cargo(u.Fighter(power=US))], "zone_49", 0)
    zone_50 = t.Sea("neutral", [], [], "zone_50", 0)
    zone_51 = t.Sea("neutral", [], [], "zone_51", 0)
    zone_52 = t.Sea("neutral", [], [], "zone_52", 0)
    zone_53 = t.Sea("neutral", [], [], "zone_53", 0)
    zone_54 = t.Sea("neutral", [], [], "zone_54", 0)
    zone_55 = t.Sea("neutral", [], [], "zone_55", 0)
    zone_56 = t.Sea("neutral", [], [], "zone_56", 0)
    zone_57 = t.Sea("neutral", [], [], "zone_57", 0)
    zone_58 = t.Sea("neutral", [], [], "zone_58", 0)
    
#Define adjacent territories
    #Land Territories
    eastern_canada.add_adj([western_canada, eastern_usa, zone_1, zone_6])
    eastern_usa.add_adj([eastern_canada, western_usa, zone_1, zone_2])
    west_indies.add_adj([zone_3])
    panama.add_adj([venezuela, mexico, zone_3])
    venezuela.add_adj([panama, peru, brazil, zone_3])
    peru.add_adj([venezuela, brazil, argentina, zone_4])
    argentina.add_adj([peru, brazil, zone_4, zone_5])
    brazil.add_adj([venezuela, peru, argentina, zone_8, zone_9])
    united_kingdom.add_adj([zone_10])
    spain.add_adj([western_europe, gibraltar, zone_11, zone_18])
    gibraltar.add_adj([spain, zone_18])
    western_europe.add_adj([spain, germany, switz, southern_europe, zone_10, zone_11, zone_18])
    switz.add_adj([western_europe, southern_europe, germany])
    finland.add_adj([karelia, sweden, zone_10, zone_17])
    sweden.add_adj([finland, zone_17])
    germany.add_adj([western_europe, eastern_europe, switz, southern_europe, zone_17])
    southern_europe.add_adj([western_europe, germany, switz, eastern_europe, zone_19])
    eastern_europe.add_adj([germany, southern_europe, karelia, ukraine, zone_17, zone_20])
    ukraine.add_adj([eastern_europe, karelia, caucasus, zone_20])
    algeria.add_adj([west_africa, equatorial_africa, libya, zone_11, zone_18])
    libya.add_adj([algeria, equatorial_africa, egypt, zone_19])
    west_africa.add_adj([algeria, equatorial_africa, zone_12])
    equatorial_africa.add_adj([west_africa, algeria, libya, egypt, congo, zone_13])
    egypt.add_adj([libya, equatorial_africa, congo, kenya, east_africa, zone_21, zone_24])
    congo.add_adj([equatorial_africa, egypt, kenya, angola, zone_13])
    east_africa.add_adj([egypt, kenya, zone_24])
    angola.add_adj([congo, kenya, south_africa, zone_22])
    kenya.add_adj([congo, egypt, east_africa, mozambique, south_africa, angola, zone_25])
    south_africa.add_adj([angola, kenya, mozambique, zone_22, zone_25, zone_55])
    mozambique.add_adj([kenya, south_africa, zone_25])
    madagascar.add_adj([zone_25, zone_26, zone_55, zone_56])
    karelia.add_adj([finland, eastern_europe, ukraine, caucasus, russia, zone_16, zone_17])
    caucasus.add_adj([ukraine, karelia, russia, turkey, persia, zone_20, zone_23])
    turkey.add_adj([caucasus, persia, syria, zone_20, zone_21])
    syria.add_adj([turkey, persia, saudi_arabia, zone_21, zone_24])
    persia.add_adj([turkey, caucasus, kazakh, afghan, india, saudi_arabia, syria, zone_23, zone_24])
    saudi_arabia.add_adj([syria, persia, zone_24])
    russia.add_adj([karelia, caucasus, kazakh, novosibirsk, evenki, zone_23])
    kazakh.add_adj([russia, novosibirsk, sinkiang, afghan, persia, zone_23])
    afghan.add_adj([kazakh, sinkiang, india, persia])
    india.add_adj([persia, afghan, sinkiang, indochina, zone_27])
    evenki.add_adj([russia, novosibirsk, yakut])
    novosibirsk.add_adj([russia, evenki, yakut, mongolia, sinkiang, kazakh])
    sinkiang.add_adj([kazakh, novosibirsk, mongolia, china, indochina, india, afghan])
    yakut.add_adj([evenki, novosibirsk, mongolia, manchuria, soviet_east])
    mongolia.add_adj([novosibirsk, yakut, manchuria, china, sinkiang])
    china.add_adj([sinkiang, mongolia, manchuria, kwangtung, indochina])
    indochina.add_adj([india, sinkiang, china, kwangtung, zone_29])
    kwangtung.add_adj([china, manchuria, indochina, zone_32])
    manchuria.add_adj([kwangtung, china, mongolia, yakut, soviet_east, zone_36])
    soviet_east.add_adj([yakut, manchuria, zone_35])
    east_indies.add_adj([zone_30])
    borneo.add_adj([zone_34])
    philippine_islands.add_adj([zone_33])
    australia.add_adj([zone_31, zone_40, zone_58])
    new_guinea.add_adj([zone_39])
    caroline_islands.add_adj([zone_38])
    new_zealand.add_adj([zone_45])
    solomon_islands.add_adj([zone_44])
    okinawa.add_adj([zone_37])
    wake_island.add_adj([zone_43])
    japan.add_adj([zone_36])
    alaska.add_adj([western_canada, zone_41, zone_46])
    midway_island.add_adj([zone_47])
    hawaiian_islands.add_adj([zone_49])
    western_canada.add_adj([eastern_canada, alaska, western_usa, zone_46, zone_48])
    western_usa.add_adj([western_canada, mexico, zone_52, zone_48])
    mexico.add_adj([western_usa, panama, zone_53, zone_52])
    
    
    #Sea Territories
    zone_1.add_adj([eastern_usa, eastern_canada])
    zone_2.add_adj([eastern_usa, zone_3, zone_6, zone_7])
    zone_3.add_adj([west_indies, panama, venezuela, zone_2, zone_7, zone_8, zone_52, zone_53])
    zone_4.add_adj([peru, argentina, zone_3, zone_5, zone_54])
    zone_5.add_adj([argentina, zone_4, zone_14, zone_15, zone_51])
    zone_6.add_adj([eastern_canada, zone_2, zone_7, zone_10, zone_11])
    zone_7.add_adj([zone_2, zone_3, zone_6, zone_8, zone_11, zone_12])
    zone_8.add_adj([brazil, zone_3, zone_7, zone_9, zone_12])
    zone_9.add_adj([brazil, zone_4, zone_8, zone_12, zone_13, zone_14])
    zone_10.add_adj([united_kingdom, western_europe, finland, zone_6, zone_11, zone_16, zone_17])
    zone_11.add_adj([spain, western_europe, algeria, zone_6, zone_7, zone_10, zone_12, zone_18])
    zone_12.add_adj([west_africa, zone_7, zone_8, zone_9, zone_11, zone_13])
    zone_13.add_adj([equatorial_africa, congo, zone_9, zone_12, zone_14, zone_22])
    zone_14.add_adj([zone_4, zone_5, zone_9, zone_13, zone_15, zone_22])
    zone_15.add_adj([zone_5, zone_14, zone_22])
    zone_16.add_adj([karelia, zone_10])
    zone_17.add_adj([finland, sweden, western_europe, germany, eastern_europe, karelia, zone_10])
    zone_18.add_adj([gibraltar, spain, western_europe, algeria, zone_11, zone_19])
    zone_19.add_adj([southern_europe, libya, zone_18, zone_20, zone_21])
    zone_20.add_adj([eastern_europe, ukraine, caucasus, turkey, zone_19, zone_21])
    zone_21.add_adj([turkey, syria, egypt, zone_19, zone_20, zone_24])
    zone_22.add_adj([angola, south_africa, zone_13, zone_14, zone_15, zone_55])
    zone_23.add_adj([caucasus, russia, kazakh, persia])
    zone_24.add_adj([syria, saudi_arabia, egypt, east_africa, zone_21, zone_25, zone_26, zone_27])
    zone_25.add_adj([kenya, mozambique, madagascar, zone_24, zone_26, zone_55])
    zone_26.add_adj([madagascar, zone_24, zone_25, zone_27, zone_28, zone_56, zone_57])
    zone_27.add_adj([india, zone_24, zone_26, zone_28, zone_29, zone_30])
    zone_28.add_adj([zone_26, zone_27, zone_30, zone_31, zone_57, zone_58])
    zone_29.add_adj([indochina, zone_27, zone_30, zone_32, zone_33, zone_34])
    zone_30.add_adj([east_indies, zone_27, zone_28, zone_29, zone_31, zone_34, zone_40])
    zone_31.add_adj([australia, zone_28, zone_30, zone_40, zone_58])
    zone_32.add_adj([kwangtung, zone_29, zone_33, zone_36])
    zone_33.add_adj([philippine_islands, zone_29, zone_32, zone_34, zone_36, zone_37, zone_38])
    zone_34.add_adj([borneo, zone_29, zone_30, zone_33, zone_38, zone_39, zone_40])
    zone_35.add_adj([soviet_east, zone_36, zone_41, zone_42])
    zone_36.add_adj([japan, manchuria, zone_32, zone_33, zone_35, zone_37, zone_42, zone_43])
    zone_37.add_adj([okinawa, zone_33, zone_36, zone_38, zone_43])
    zone_38.add_adj([caroline_islands, zone_33, zone_34, zone_37, zone_39, zone_43, zone_44])
    zone_39.add_adj([new_guinea, zone_34, zone_38, zone_40, zone_44])
    zone_40.add_adj([australia, zone_30, zone_31, zone_34, zone_39, zone_58])
    zone_41.add_adj([alaska, western_canada, zone_35, zone_42, zone_46, zone_47])
    zone_42.add_adj([zone_35, zone_36, zone_41, zone_43, zone_47, zone_49])
    zone_43.add_adj([wake_island, zone_36, zone_37, zone_38, zone_42, zone_44, zone_49])
    zone_44.add_adj([solomon_islands, zone_38, zone_39, zone_40, zone_43, zone_45, zone_49, zone_50])
    zone_45.add_adj([new_zealand, zone_40, zone_44, zone_50, zone_51, zone_58])
    zone_46.add_adj([alaska, western_canada, zone_41, zone_47, zone_48])
    zone_47.add_adj([midway_island, zone_41, zone_42, zone_46, zone_48, zone_49])
    zone_48.add_adj([western_canada, western_usa, zone_46, zone_47, zone_49, zone_53])
    zone_49.add_adj([hawaiian_islands, zone_42, zone_43, zone_44, zone_47, zone_48, zone_50, zone_53])
    zone_50.add_adj([zone_44, zone_45, zone_49, zone_51, zone_53, zone_54])
    zone_51.add_adj([zone_45, zone_50, zone_54, zone_5])
    zone_52.add_adj([western_usa, mexico, zone_2, zone_3])
    zone_53.add_adj([mexico, zone_48, zone_49, zone_50, zone_54, zone_3])
    zone_54.add_adj([zone_50, zone_51, zone_53, zone_4])
    zone_55.add_adj([south_africa, madagascar, zone_22, zone_25, zone_56])
    zone_56.add_adj([madagascar, zone_26, zone_55, zone_57])
    zone_57.add_adj([zone_26, zone_28, zone_56, zone_58])
    zone_58.add_adj([australia, zone_28, zone_31, zone_40, zone_45, zone_57])
    
#Put territories in powers
    #Land territories
    UK.gain_territory(eastern_canada)
    US.gain_territory(eastern_usa)
    US.gain_territory(west_indies)
    US.gain_territory(panama)
    neutral.gain_territory(venezuela)
    neutral.gain_territory(peru)
    neutral.gain_territory(argentina)
    US.gain_territory(brazil)
    UK.gain_territory(united_kingdom)
    neutral.gain_territory(spain)
    UK.gain_territory(gibraltar)
    Germany.gain_territory(western_europe)
    neutral.gain_territory(switz)
    Germany.gain_territory(finland)
    neutral.gain_territory(sweden)
    Germany.gain_territory(germany)
    Germany.gain_territory(southern_europe)
    Germany.gain_territory(eastern_europe)
    Germany.gain_territory(ukraine)
    Germany.gain_territory(algeria)
    Germany.gain_territory(libya)
    UK.gain_territory(west_africa)
    UK.gain_territory(equatorial_africa)
    UK.gain_territory(egypt)
    UK.gain_territory(congo)
    UK.gain_territory(east_africa)
    neutral.gain_territory(angola)
    UK.gain_territory(kenya)
    UK.gain_territory(south_africa)
    neutral.gain_territory(mozambique)
    UK.gain_territory(madagascar)
    USSR.gain_territory(karelia)
    USSR.gain_territory(caucasus)
    neutral.gain_territory(turkey)
    UK.gain_territory(syria)
    UK.gain_territory(persia)
    neutral.gain_territory(saudi_arabia)
    USSR.gain_territory(russia)
    USSR.gain_territory(kazakh)
    neutral.gain_territory(afghan)
    UK.gain_territory(india)
    USSR.gain_territory(evenki)
    USSR.gain_territory(novosibirsk)
    US.gain_territory(sinkiang)
    USSR.gain_territory(yakut)
    neutral.gain_territory(mongolia)
    US.gain_territory(china)
    Japan.gain_territory(indochina)
    Japan.gain_territory(kwangtung)
    Japan.gain_territory(manchuria)
    USSR.gain_territory(soviet_east)
    Japan.gain_territory(east_indies)
    Japan.gain_territory(borneo)
    Japan.gain_territory(philippine_islands)
    UK.gain_territory(australia)
    Japan.gain_territory(new_guinea)
    Japan.gain_territory(caroline_islands)
    UK.gain_territory(new_zealand)
    Japan.gain_territory(solomon_islands)
    Japan.gain_territory(okinawa)
    Japan.gain_territory(wake_island)
    Japan.gain_territory(japan)
    US.gain_territory(alaska)
    US.gain_territory(midway_island)
    US.gain_territory(hawaiian_islands)
    UK.gain_territory(western_canada)
    US.gain_territory(western_usa)
    US.gain_territory(mexico)
    
    
    #Sea Territories
    neutral.gain_territory(zone_1)
    US.gain_territory(zone_2)
    neutral.gain_territory(zone_3)
    neutral.gain_territory(zone_4)
    neutral.gain_territory(zone_5)
    UK.gain_territory(zone_6)
    neutral.gain_territory(zone_7)
    neutral.gain_territory(zone_8)
    neutral.gain_territory(zone_9)
    UK.gain_territory(zone_10)
    Germany.gain_territory(zone_11)
    neutral.gain_territory(zone_12)
    neutral.gain_territory(zone_13)
    neutral.gain_territory(zone_14)
    neutral.gain_territory(zone_15)
    USSR.gain_territory(zone_16)
    Germany.gain_territory(zone_17)
    UK.gain_territory(zone_18)
    Germany.gain_territory(zone_19)
    neutral.gain_territory(zone_20)
    UK.gain_territory(zone_21)
    neutral.gain_territory(zone_22)
    neutral.gain_territory(zone_23)
    neutral.gain_territory(zone_24)
    neutral.gain_territory(zone_25)
    neutral.gain_territory(zone_26)
    UK.gain_territory(zone_27)
    neutral.gain_territory(zone_28)
    neutral.gain_territory(zone_29)
    neutral.gain_territory(zone_30)
    neutral.gain_territory(zone_31)
    neutral.gain_territory(zone_32)
    Japan.gain_territory(zone_33)
    neutral.gain_territory(zone_34)
    neutral.gain_territory(zone_35)
    Japan.gain_territory(zone_36)
    neutral.gain_territory(zone_37)
    Japan.gain_territory(zone_38)
    neutral.gain_territory(zone_39)
    neutral.gain_territory(zone_40)
    neutral.gain_territory(zone_41)
    neutral.gain_territory(zone_42)
    neutral.gain_territory(zone_43)
    Japan.gain_territory(zone_44)
    neutral.gain_territory(zone_45)
    neutral.gain_territory(zone_46)
    neutral.gain_territory(zone_47)
    US.gain_territory(zone_48)
    US.gain_territory(zone_49)
    neutral.gain_territory(zone_50)
    neutral.gain_territory(zone_51)
    neutral.gain_territory(zone_52)
    neutral.gain_territory(zone_53)
    neutral.gain_territory(zone_54)
    neutral.gain_territory(zone_55)
    neutral.gain_territory(zone_56)
    neutral.gain_territory(zone_57)
    neutral.gain_territory(zone_58)
    
    
    return(USSR, Germany, UK, Japan, US, neutral)

if __name__ == '__main__':
    powers = setup()
    print(powers)
    
    