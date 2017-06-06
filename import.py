# -*- coding: UTF-8 -*-
import csv
import os
import re
from datetime import datetime
from pymongo import MongoClient
import json
import cyrtranslit

# Connect to defualt local instance of MongoClient
client = MongoClient()

# Get database and collection
db = client.istanbul
collection = db.tenders


def get_city_name(city_code):
    city_names = [
        {
            "IdOpstine": "70017",
            "Name": "ALEKSANDROVAC"
        },
        {
            "IdOpstine": "70025",
            "Name": "Aleksinac"
        },
        {
            "IdOpstine": "70033",
            "Name": "ARANĐELOVAC"
        },
        {
            "IdOpstine": "70041",
            "Name": "ARILJE"
        },
        {
            "IdOpstine": "70050",
            "Name": "BABUŠNICA"
        },
        {
            "IdOpstine": "70068",
            "Name": "Bjelovar"
        },
        {
            "IdOpstine": "70076",
            "Name": "BATOČINA"
        },
        {
            "IdOpstine": "70084",
            "Name": "Bela Palanka"
        },
        {
            "IdOpstine": "70092",
            "Name": "BARAJEVO"
        },
        {
            "IdOpstine": "70106",
            "Name": "VOŽDOVAC"
        },
        {
            "IdOpstine": "70114",
            "Name": "VRAČAR"
        },
        {
            "IdOpstine": "70122",
            "Name": "GROCKA"
        },
        {
            "IdOpstine": "70149",
            "Name": "ZVEZDARA"
        },
        {
            "IdOpstine": "70157",
            "Name": "Zemun"
        },
        {
            "IdOpstine": "70165",
            "Name": "LAZAREVAC"
        },
        {
            "IdOpstine": "70173",
            "Name": "MLADENOVAC"
        },
        {
            "IdOpstine": "70181",
            "Name": "NEW BELGRADE"
        },
        {
            "IdOpstine": "70190",
            "Name": "Obrenovac"
        },
        {
            "IdOpstine": "70203",
            "Name": "PALILULA"
        },
        {
            "IdOpstine": "70211",
            "Name": "Rakovica"
        },
        {
            "IdOpstine": "70220",
            "Name": "SAVSKI VENAC"
        },
        {
            "IdOpstine": "70238",
            "Name": "SOPOT"
        },
        {
            "IdOpstine": "70246",
            "Name": "STARI GRAD"
        },
        {
            "IdOpstine": "70254",
            "Name": "ČUKARICA"
        },
        {
            "IdOpstine": "70262",
            "Name": "Blace"
        },
        {
            "IdOpstine": "70289",
            "Name": "BOGATIĆ"
        },
        {
            "IdOpstine": "70297",
            "Name": "BOJNIK"
        },
        {
            "IdOpstine": "70319",
            "Name": "BOLJEVAC"
        },
        {
            "IdOpstine": "70327",
            "Name": "BOR"
        },
        {
            "IdOpstine": "70335",
            "Name": "BOSILEGRAD"
        },
        {
            "IdOpstine": "70343",
            "Name": "Brus"
        },
        {
            "IdOpstine": "70351",
            "Name": "Bujanovac"
        },
        {
            "IdOpstine": "70360",
            "Name": "Valjevo"
        },
        {
            "IdOpstine": "70378",
            "Name": "VARVARIN"
        },
        {
            "IdOpstine": "70386",
            "Name": "Velika Plana"
        },
        {
            "IdOpstine": "70394",
            "Name": "Veliko Gradiste"
        },
        {
            "IdOpstine": "70408",
            "Name": "VLADIMIRCI"
        },
        {
            "IdOpstine": "70416",
            "Name": "Vladicin Han"
        },
        {
            "IdOpstine": "70424",
            "Name": "VLASOTINCE"
        },
        {
            "IdOpstine": "70432",
            "Name": "Vranje"
        },
        {
            "IdOpstine": "70459",
            "Name": "Vrnjacka Banja"
        },
        {
            "IdOpstine": "70467",
            "Name": "GADŽIN HAN"
        },
        {
            "IdOpstine": "70475",
            "Name": "GOLUBAC"
        },
        {
            "IdOpstine": "70483",
            "Name": "Gornji Milanovac"
        },
        {
            "IdOpstine": "70491",
            "Name": "DESPOTOVAC"
        },
        {
            "IdOpstine": "70505",
            "Name": "DIMITROVGRAD"
        },
        {
            "IdOpstine": "70513",
            "Name": "DOLJEVAC"
        },
        {
            "IdOpstine": "70521",
            "Name": "ŽABARI"
        },
        {
            "IdOpstine": "70530",
            "Name": "ŽAGUBICA"
        },
        {
            "IdOpstine": "70548",
            "Name": "ŽITORAĐA"
        },
        {
            "IdOpstine": "70556",
            "Name": "Zajecar"
        },
        {
            "IdOpstine": "70564",
            "Name": "IVANJICA"
        },
        {
            "IdOpstine": "70572",
            "Name": "KLADOVO"
        },
        {
            "IdOpstine": "70599",
            "Name": "KNIĆ"
        },
        {
            "IdOpstine": "70602",
            "Name": "KNJAŽEVAC"
        },
        {
            "IdOpstine": "70629",
            "Name": "KOSJERIĆ"
        },
        {
            "IdOpstine": "70637",
            "Name": "KOCELJEVA"
        },
        {
            "IdOpstine": "70645",
            "Name": "KRAGUJEVAC - GRAD"
        },
        {
            "IdOpstine": "70653",
            "Name": "ROYAL"
        },
        {
            "IdOpstine": "70661",
            "Name": "KRUPANJ"
        },
        {
            "IdOpstine": "70670",
            "Name": "Krusevac"
        },
        {
            "IdOpstine": "70688",
            "Name": "KURŠUMLIJA"
        },
        {
            "IdOpstine": "70696",
            "Name": "KUČEVO"
        },
        {
            "IdOpstine": "70700",
            "Name": "LAJKOVAC"
        },
        {
            "IdOpstine": "70718",
            "Name": "LEBANE"
        },
        {
            "IdOpstine": "70726",
            "Name": "Leskovac"
        },
        {
            "IdOpstine": "70734",
            "Name": "Loznica"
        },
        {
            "IdOpstine": "70742",
            "Name": "LUČANI"
        },
        {
            "IdOpstine": "70769",
            "Name": "LJIG"
        },
        {
            "IdOpstine": "70777",
            "Name": "LJUBOVIJA"
        },
        {
            "IdOpstine": "70785",
            "Name": "MAJDANPEK"
        },
        {
            "IdOpstine": "70793",
            "Name": "Mali Zvornik"
        },
        {
            "IdOpstine": "70807",
            "Name": "RETAIL CRNIĆE"
        },
        {
            "IdOpstine": "70815",
            "Name": "MEDVEĐA"
        },
        {
            "IdOpstine": "70823",
            "Name": "MEROŠINA"
        },
        {
            "IdOpstine": "70831",
            "Name": "MIONICA"
        },
        {
            "IdOpstine": "70840",
            "Name": "NEGOTIN"
        },
        {
            "IdOpstine": "70866",
            "Name": "Nova Varos"
        },
        {
            "IdOpstine": "70874",
            "Name": "Novi Pazar"
        },
        {
            "IdOpstine": "70882",
            "Name": "OSEČINA"
        },
        {
            "IdOpstine": "70904",
            "Name": "Paracin"
        },
        {
            "IdOpstine": "70912",
            "Name": "PETROVAC"
        },
        {
            "IdOpstine": "70939",
            "Name": "PIROT"
        },
        {
            "IdOpstine": "70947",
            "Name": "POŽAREVAC"
        },
        {
            "IdOpstine": "70955",
            "Name": "POŽEGA"
        },
        {
            "IdOpstine": "70963",
            "Name": "Presevo"
        },
        {
            "IdOpstine": "70971",
            "Name": "PRIBOJ"
        },
        {
            "IdOpstine": "70980",
            "Name": "PRIJEPOLJE"
        },
        {
            "IdOpstine": "70998",
            "Name": "Prokuplje"
        },
        {
            "IdOpstine": "71005",
            "Name": "RAŽANJ"
        },
        {
            "IdOpstine": "71013",
            "Name": "RACA"
        },
        {
            "IdOpstine": "71021",
            "Name": "RAŠKA"
        },
        {
            "IdOpstine": "71030",
            "Name": "REKOVAC"
        },
        {
            "IdOpstine": "71048",
            "Name": "Jagodina"
        },
        {
            "IdOpstine": "71056",
            "Name": "SVILAJNAC"
        },
        {
            "IdOpstine": "71064",
            "Name": "SVRLJIG"
        },
        {
            "IdOpstine": "71072",
            "Name": "SJENICA"
        },
        {
            "IdOpstine": "71099",
            "Name": "Smederevo"
        },
        {
            "IdOpstine": "71102",
            "Name": "Smederevska Palanka"
        },
        {
            "IdOpstine": "71129",
            "Name": "SOKOBANJA"
        },
        {
            "IdOpstine": "71137",
            "Name": "Surdulica"
        },
        {
            "IdOpstine": "71145",
            "Name": "Uzice"
        },
        {
            "IdOpstine": "71153",
            "Name": "Poplar"
        },
        {
            "IdOpstine": "71161",
            "Name": "TRGOVIŠTE"
        },
        {
            "IdOpstine": "71170",
            "Name": "TRSTENIK"
        },
        {
            "IdOpstine": "71188",
            "Name": "TUTIN"
        },
        {
            "IdOpstine": "71196",
            "Name": "ĆIĆEVAC"
        },
        {
            "IdOpstine": "71200",
            "Name": "ĆUPRIJA"
        },
        {
            "IdOpstine": "71218",
            "Name": "UB"
        },
        {
            "IdOpstine": "71226",
            "Name": "Crna Trava"
        },
        {
            "IdOpstine": "71234",
            "Name": "ČAJETINA"
        },
        {
            "IdOpstine": "71242",
            "Name": "ČAČAK"
        },
        {
            "IdOpstine": "71269",
            "Name": "Sabac"
        },
        {
            "IdOpstine": "71277",
            "Name": "LAPOVO"
        },
        {
            "IdOpstine": "71285",
            "Name": "Niska Banja"
        },
        {
            "IdOpstine": "71293",
            "Name": "SURČIN"
        },
        {
            "IdOpstine": "71307",
            "Name": "PANTELEJ"
        },
        {
            "IdOpstine": "71315",
            "Name": "RED CROSS"
        },
        {
            "IdOpstine": "71323",
            "Name": "PALILULA"
        },
        {
            "IdOpstine": "71331",
            "Name": "MEDIANA"
        },
        {
            "IdOpstine": "80012",
            "Name": "ADA"
        },
        {
            "IdOpstine": "80039",
            "Name": "ALIBUNAR"
        },
        {
            "IdOpstine": "80047",
            "Name": "APATIN"
        },
        {
            "IdOpstine": "80055",
            "Name": "BAČ"
        },
        {
            "IdOpstine": "80063",
            "Name": "Backa Palanka"
        },
        {
            "IdOpstine": "80071",
            "Name": "Backa Topola"
        },
        {
            "IdOpstine": "80080",
            "Name": "Backi Petrovac"
        },
        {
            "IdOpstine": "80098",
            "Name": "WHITE CHURCH"
        },
        {
            "IdOpstine": "80101",
            "Name": "BEOČIN"
        },
        {
            "IdOpstine": "80110",
            "Name": "BEČEJ"
        },
        {
            "IdOpstine": "80128",
            "Name": "Vrsac"
        },
        {
            "IdOpstine": "80136",
            "Name": "ŽABALJ"
        },
        {
            "IdOpstine": "80144",
            "Name": "ŽITIŠTE"
        },
        {
            "IdOpstine": "80152",
            "Name": "Zrenjanin"
        },
        {
            "IdOpstine": "80179",
            "Name": "INĐIJA"
        },
        {
            "IdOpstine": "80187",
            "Name": "IRIG"
        },
        {
            "IdOpstine": "80195",
            "Name": "KANJIŽA"
        },
        {
            "IdOpstine": "80209",
            "Name": "Kikinda"
        },
        {
            "IdOpstine": "80217",
            "Name": "KOVAČICA"
        },
        {
            "IdOpstine": "80225",
            "Name": "METALS"
        },
        {
            "IdOpstine": "80,233",
            "Name": "KULA"
        },
        {
            "IdOpstine": "80241",
            "Name": "Mali Iđoš"
        },
        {
            "IdOpstine": "80250",
            "Name": "NEW CRNJA"
        },
        {
            "IdOpstine": "80268",
            "Name": "NEW BEČEJ"
        },
        {
            "IdOpstine": "80276",
            "Name": "NEW KNEŽEVAC"
        },
        {
            "IdOpstine": "80284",
            "Name": "NOVI SAD - CITY"
        },
        {
            "IdOpstine": "80292",
            "Name": "OPOVO"
        },
        {
            "IdOpstine": "80306",
            "Name": "ODŽACI"
        },
        {
            "IdOpstine": "80314",
            "Name": "Pancevo"
        },
        {
            "IdOpstine": "80322",
            "Name": "PEĆINCI"
        },
        {
            "IdOpstine": "80349",
            "Name": "PLANDIŠTE"
        },
        {
            "IdOpstine": "80357",
            "Name": "RUMA"
        },
        {
            "IdOpstine": "80365",
            "Name": "Senta"
        },
        {
            "IdOpstine": "80373",
            "Name": "SEČANJ"
        },
        {
            "IdOpstine": "80381",
            "Name": "Sombor"
        },
        {
            "IdOpstine": "80390",
            "Name": "SRBOBRAN"
        },
        {
            "IdOpstine": "80403",
            "Name": "Sremska Mitrovica"
        },
        {
            "IdOpstine": "80411",
            "Name": "Sremski Karlovci"
        },
        {
            "IdOpstine": "80420",
            "Name": "Stara Pazova"
        },
        {
            "IdOpstine": "80438",
            "Name": "Subotica"
        },
        {
            "IdOpstine": "80446",
            "Name": "TEMERIN"
        },
        {
            "IdOpstine": "80462",
            "Name": "Vrbas"
        },
        {
            "IdOpstine": "80489",
            "Name": "ČOKA"
        },
        {
            "IdOpstine": "80497",
            "Name": "SID"
        },
        {
            "IdOpstine": "90018",
            "Name": "Vitina"
        },
        {
            "IdOpstine": "90026",
            "Name": "VUČITRN"
        },
        {
            "IdOpstine": "90034",
            "Name": "GLOGOVAC"
        },
        {
            "IdOpstine": "90042",
            "Name": "GJILAN"
        },
        {
            "IdOpstine": "90069",
            "Name": "DEČANI"
        },
        {
            "IdOpstine": "90085",
            "Name": "ĐAKOVICA"
        },
        {
            "IdOpstine": "90093",
            "Name": "Zubin Potok"
        },
        {
            "IdOpstine": "90107",
            "Name": "EAST"
        },
        {
            "IdOpstine": "90115",
            "Name": "KAÇANIK"
        },
        {
            "IdOpstine": "90123",
            "Name": "KLINA"
        },
        {
            "IdOpstine": "90131",
            "Name": "Kosovo Polje"
        },
        {
            "IdOpstine": "90140",
            "Name": "Kosovska Kamenica"
        },
        {
            "IdOpstine": "90158",
            "Name": "LEPOSAVIĆ"
        },
        {
            "IdOpstine": "90166",
            "Name": "LIPLJAN"
        },
        {
            "IdOpstine": "90182",
            "Name": "NOVO BRDO"
        },
        {
            "IdOpstine": "90204",
            "Name": "OBILIĆ"
        },
        {
            "IdOpstine": "90212",
            "Name": "Orahovac"
        },
        {
            "IdOpstine": "90239",
            "Name": "Pec"
        },
        {
            "IdOpstine": "90247",
            "Name": "PODUJEVA"
        },
        {
            "IdOpstine": "90255",
            "Name": "Prizren"
        },
        {
            "IdOpstine": "90263",
            "Name": "PRISTINA"
        },
        {
            "IdOpstine": "90271",
            "Name": "SKENDERAJ"
        },
        {
            "IdOpstine": "90280",
            "Name": "Suva Reka"
        },
        {
            "IdOpstine": "90298",
            "Name": "KOSOVSKA MITROVICA"
        },
        {
            "IdOpstine": "90301",
            "Name": "Ferizaj"
        },
        {
            "IdOpstine": "90310",
            "Name": "SHTIME"
        },
        {
            "IdOpstine": "90328",
            "Name": "ŠTRPCE"
        },
        {
            "IdOpstine": "90336",
            "Name": "GORA"
        },
        {
            "IdOpstine": "90352",
            "Name": "ZVEČAN"
        }
    ]
    for city in city_names:
        print city['IdOpstine']
        print city_code
        if city['IdOpstine'] == str(city_code):
            return city['Name']


def get_procedure_type(code):
    procurement_type = [
        {
            " Name": "Open procedure",
            "IdVrstaPostupka": 1
        },
        {
            " Name": "Restricted procedure",
            "IdVrstaPostupka": 2
        },
        {
            " Name": "The negotiated procedure without publication of a call for proposals",
            "IdVrstaPostupka": 3
        },
        {
            " Name": "The negotiated procedure with publication of a call for proposals",
            "IdVrstaPostupka": 4
        },
        {
            " Name": "Design contest",
            "IdVrstaPostupka": 5
        },
        {
            " Name": "A method qualification",
            "IdVrstaPostupka": 6
        },
        {
            " Name": "The procedure of public procurement of low value",
            "IdVrstaPostupka": 7
        },
        {
            " Name": "Competitive dialogue",
            "IdVrstaPostupka": 8
        }
    ]
    for item in procurement_type:
        if item['IdVrstaPostupka'] == code:
            return item[' Name']


def get_activity(code):
    activities = [
        {
            "IdDelatnost": 0,
            " Name": " unknown"
        },
        {
            "IdDelatnost": 111,
            " Name": " \"Cultivation of cereals (except rice)"
        },
        {
            "IdDelatnost": 112,
            " Name": " Growing rice"
        },
        {
            "IdDelatnost": 113,
            " Name": " \"Growing of vegetables and melons"
        },
        {
            "IdDelatnost": 114,
            " Name": " Growing sugar cane"
        },
        {
            "IdDelatnost": 115,
            " Name": " Growing Tobacco"
        },
        {
            "IdDelatnost": 116,
            " Name": " Plant cultivation for the production of fibers"
        },
        {
            "IdDelatnost": 119,
            " Name": " Growing of other perennial crops"
        },
        {
            "IdDelatnost": 121,
            " Name": " Growing grapes"
        },
        {
            "IdDelatnost": 122,
            " Name": " Growing of tropical and subtropical fruits"
        },
        {
            "IdDelatnost": 123,
            " Name": " Growing citrus"
        },
        {
            "IdDelatnost": 124,
            " Name": " Growing of pome fruits and stone fruits"
        },
        {
            "IdDelatnost": 125,
            " Name": " \"Growing of other tree and bush fruits and nuts\""
        },
        {
            "IdDelatnost": 126,
            " Name": " oil fruits Growing"
        },
        {
            "IdDelatnost": 127,
            " Name": " Growing plants beverage"
        },
        {
            "IdDelatnost": 128,
            " Name": " \"Growing of spices"
        },
        {
            "IdDelatnost": 129,
            " Name": " Growing of other perennial crops"
        },
        {
            "IdDelatnost": 130,
            " Name": " Plant propagation"
        },
        {
            "IdDelatnost": 141,
            " Name": " Raising of dairy cattle"
        },
        {
            "IdDelatnost": 142,
            " Name": " Raising of other cattle and buffaloes"
        },
        {
            "IdDelatnost": 143,
            " Name": " Raising of horses and other equines"
        },
        {
            "IdDelatnost": 144,
            " Name": " Raising of camels and lamas"
        },
        {
            "IdDelatnost": 145,
            " Name": " sheep and goat farming"
        },
        {
            "IdDelatnost": 146,
            " Name": " Pig"
        },
        {
            "IdDelatnost": 147,
            " Name": " Raising of poultry"
        },
        {
            "IdDelatnost": 149,
            " Name": " Raising of other animals"
        },
        {
            "IdDelatnost": 150,
            " Name": " Mixed farming"
        },
        {
            "IdDelatnost": 161,
            " Name": " Support activities for crop production"
        },
        {
            "IdDelatnost": 162,
            " Name": " auxiliary activities in animal husbandry"
        },
        {
            "IdDelatnost": 163,
            " Name": " post-harvest activities"
        },
        {
            "IdDelatnost": 164,
            " Name": " seed"
        },
        {
            "IdDelatnost": 170,
            " Name": " \"Hunting"
        },
        {
            "IdDelatnost": 210,
            " Name": " Silviculture and other forestry activities"
        },
        {
            "IdDelatnost": 220,
            " Name": " logging"
        },
        {
            "IdDelatnost": 230,
            " Name": " collection of forest fruits"
        },
        {
            "IdDelatnost": 240,
            " Name": " Service activities related to forestry"
        },
        {
            "IdDelatnost": 311,
            " Name": " Sea fishing"
        },
        {
            "IdDelatnost": 312,
            " Name": " Freshwater fishing"
        },
        {
            "IdDelatnost": 321,
            " Name": " Marine aquaculture"
        },
        {
            "IdDelatnost": 322,
            " Name": " Freshwater aquaculture"
        },
        {
            "IdDelatnost": 510,
            " Name": " exploitation of coal and anthracite"
        },
        {
            "IdDelatnost": 520,
            " Name": " The exploitation of lignite and brown coal"
        },
        {
            "IdDelatnost": 610,
            " Name": " Crude Oil"
        },
        {
            "IdDelatnost": 620,
            " Name": " The exploitation of natural gas"
        },
        {
            "IdDelatnost": 710,
            " Name": " Mining of iron"
        },
        {
            "IdDelatnost": 721,
            " Name": " Mining of uranium and thorium"
        },
        {
            "IdDelatnost": 729,
            " Name": " \"Mining of other ferrous"
        },
        {
            "IdDelatnost": 811,
            " Name": " \"The exploitation of ornamental and building stone"
        },
        {
            "IdDelatnost": 812,
            " Name": " \"Operation of gravel and sand pits\""
        },
        {
            "IdDelatnost": 891,
            " Name": " \"The exploitation of minerals"
        },
        {
            "IdDelatnost": 892,
            " Name": " Peat extraction"
        },
        {
            "IdDelatnost": 893,
            " Name": " Operation of sodium chloride"
        },
        {
            "IdDelatnost": 899,
            " Name": " exploitation of other mining and quarrying"
        },
        {
            "IdDelatnost": 910,
            " Name": " Service activities related to the exploration and exploitation of oil and gas"
        },
        {
            "IdDelatnost": 990,
            " Name": " Service activities related to the exploration and exploitation of other ores"
        },
        {
            "IdDelatnost": 1011,
            " Name": " Processing and preserving of meat"
        },
        {
            "IdDelatnost": 1012,
            " Name": " Processing and preserving of poultry meat"
        },
        {
            "IdDelatnost": 1013,
            " Name": " production of meat products"
        },
        {
            "IdDelatnost": 1020,
            " Name": " \"Processing and preserving of fish"
        },
        {
            "IdDelatnost": 1031,
            " Name": " Processing and preserving of potatoes"
        },
        {
            "IdDelatnost": 1032,
            " Name": " production of fruit and vegetables"
        },
        {
            "IdDelatnost": 1039,
            " Name": " Other processing and preserving of fruit and vegetables"
        },
        {
            "IdDelatnost": 1041,
            " Name": " Production of oils and fats"
        },
        {
            "IdDelatnost": 1042,
            " Name": " Manufacture of margarine and similar edible fats"
        },
        {
            "IdDelatnost": 1051,
            " Name": " dairies and cheese"
        },
        {
            "IdDelatnost": 1052,
            " Name": " Manufacture of ice cream"
        },
        {
            "IdDelatnost": 1061,
            " Name": " grain mill products"
        },
        {
            "IdDelatnost": 1062,
            " Name": " Production of starch and starch products"
        },
        {
            "IdDelatnost": 1071,
            " Name": " \"Manufacture of fresh pastry goods and cakes\""
        },
        {
            "IdDelatnost": 1072,
            " Name": " \"Manufacture of rusks and biscuits"
        },
        {
            "IdDelatnost": 1073,
            " Name": " \"Manufacture of macaroni"
        },
        {
            "IdDelatnost": 1081,
            " Name": " Sugar"
        },
        {
            "IdDelatnost": 1082,
            " Name": " \"Manufacture of cocoa"
        },
        {
            "IdDelatnost": 1083,
            " Name": " Processing of tea and coffee"
        },
        {
            "IdDelatnost": 1084,
            " Name": " Production of spices and other food additives"
        },
        {
            "IdDelatnost": 1085,
            " Name": " production of ready meals"
        },
        {
            "IdDelatnost": 1086,
            " Name": " Manufacture of homogenised food preparations and dietetic food"
        },
        {
            "IdDelatnost": 1089,
            " Name": " Manufacture of other food products"
        },
        {
            "IdDelatnost": 1091,
            " Name": " Manufacture of prepared feeds for farm animals"
        },
        {
            "IdDelatnost": 1092,
            " Name": " Manufacture of prepared pet foods"
        },
        {
            "IdDelatnost": 1101,
            " Name": " \"Distilling"
        },
        {
            "IdDelatnost": 1102,
            " Name": " Manufacture of wine from grape"
        },
        {
            "IdDelatnost": 1103,
            " Name": " production of beverages and other fruit wines"
        },
        {
            "IdDelatnost": 1104,
            " Name": " Manufacture of other non-distilled fermented beverages"
        },
        {
            "IdDelatnost": 1105,
            " Name": " beer production"
        },
        {
            "IdDelatnost": 1106,
            " Name": " production of malt"
        },
        {
            "IdDelatnost": 1107,
            " Name": " \"Manufacture of soft drinks"
        },
        {
            "IdDelatnost": 1200,
            " Name": " Manufacture of tobacco products"
        },
        {
            "IdDelatnost": 1310,
            " Name": " Preparation and spinning of textile fibers"
        },
        {
            "IdDelatnost": 1320,
            " Name": " fabric production"
        },
        {
            "IdDelatnost": 1330,
            " Name": " Finishing of textiles"
        },
        {
            "IdDelatnost": 1391,
            " Name": " Manufacture of knitted and crocheted fabrics"
        },
        {
            "IdDelatnost": 1392,
            " Name": " \"Production of finished textile products"
        },
        {
            "IdDelatnost": 1393,
            " Name": " Manufacture of carpets and rugs"
        },
        {
            "IdDelatnost": 1394,
            " Name": " \"Manufacture of cordage"
        },
        {
            "IdDelatnost": 1395,
            " Name": " \"The production of non-wovens and articles made from it"
        },
        {
            "IdDelatnost": 1396,
            " Name": " Manufacture of other technical and industrial textiles"
        },
        {
            "IdDelatnost": 1399,
            " Name": " Manufacture of other textiles"
        },
        {
            "IdDelatnost": 1411,
            " Name": " Manufacture of leather clothes"
        },
        {
            "IdDelatnost": 1412,
            " Name": " Manufacture of workwear"
        },
        {
            "IdDelatnost": 1413,
            " Name": " Manufacture of other outerwear"
        },
        {
            "IdDelatnost": 1414,
            " Name": " Production facilities"
        },
        {
            "IdDelatnost": 1419,
            " Name": " Manufacture of other wearing apparel and accessories"
        },
        {
            "IdDelatnost": 1420,
            " Name": " Manufacturing of fur"
        },
        {
            "IdDelatnost": 1431,
            " Name": " Manufacture of knitted and crocheted hosiery"
        },
        {
            "IdDelatnost": 1439,
            " Name": " Manufacture of other knitted and crocheted apparel"
        },
        {
            "IdDelatnost": 1511,
            " Name": " Tanning and dressing of leather; dressing and dyeing of fur"
        },
        {
            "IdDelatnost": 1512,
            " Name": " \"Manufacture of luggage"
        },
        {
            "IdDelatnost": 1520,
            " Name": " Manufacture of footwear"
        },
        {
            "IdDelatnost": 1610,
            " Name": " Sawmilling and planing of wood"
        },
        {
            "IdDelatnost": 1621,
            " Name": " Manufacture of veneer sheets and wood"
        },
        {
            "IdDelatnost": 1622,
            " Name": " production of parquet"
        },
        {
            "IdDelatnost": 1623,
            " Name": " Manufacture of other builders' carpentry and joinery"
        },
        {
            "IdDelatnost": 1624,
            " Name": " Manufacture of wooden containers"
        },
        {
            "IdDelatnost": 1629,
            " Name": " \"Manufacture of other products of wood"
        },
        {
            "IdDelatnost": 1711,
            " Name": " Production of cellulose fibers"
        },
        {
            "IdDelatnost": 1712,
            " Name": " Manufacture of paper and paperboard"
        },
        {
            "IdDelatnost": 1721,
            " Name": " Manufacture of corrugated paper and paperboard and containers of paper and paperboard"
        },
        {
            "IdDelatnost": 1722,
            " Name": " production of paper for personal and domestic use"
        },
        {
            "IdDelatnost": 1723,
            " Name": " production of paper"
        },
        {
            "IdDelatnost": 1724,
            " Name": " Production wallpaper"
        },
        {
            "IdDelatnost": 1729,
            " Name": " Production of other paper and paperboard"
        },
        {
            "IdDelatnost": 1811,
            " Name": " Printing of newspapers"
        },
        {
            "IdDelatnost": 1812,
            " Name": " Other printing"
        },
        {
            "IdDelatnost": 1813,
            " Name": " media services"
        },
        {
            "IdDelatnost": 1814,
            " Name": " Binding and related services"
        },
        {
            "IdDelatnost": 1820,
            " Name": " Reproduction of recorded media"
        },
        {
            "IdDelatnost": 1910,
            " Name": " Production of coke oven products"
        },
        {
            "IdDelatnost": 1920,
            " Name": " Production of petroleum products"
        },
        {
            "IdDelatnost": 2011,
            " Name": " Manufacture of industrial gases"
        },
        {
            "IdDelatnost": 2012,
            " Name": " Production of the preparation of dyes and pigments"
        },
        {
            "IdDelatnost": 2013,
            " Name": " Manufacture of other inorganic basic chemicals"
        },
        {
            "IdDelatnost": 2014,
            " Name": " Manufacture of other organic basic chemicals"
        },
        {
            "IdDelatnost": 2015,
            " Name": " Production of fertilizers and nitrogen compounds"
        },
        {
            "IdDelatnost": 2016,
            " Name": " Manufacture of plastics in primary forms"
        },
        {
            "IdDelatnost": 2017,
            " Name": " synthetic rubber production in primary forms"
        },
        {
            "IdDelatnost": 2020,
            " Name": " Manufacture of pesticides and chemicals for agriculture"
        },
        {
            "IdDelatnost": 2030,
            " Name": " \"Manufacture of paints"
        },
        {
            "IdDelatnost": 2041,
            " Name": " \"Manufacture of soap and detergents"
        },
        {
            "IdDelatnost": 2042,
            " Name": " Manufacture of perfumes and toilet preparations"
        },
        {
            "IdDelatnost": 2051,
            " Name": " Manufacture of explosives"
        },
        {
            "IdDelatnost": 2052,
            " Name": " Production of bonding"
        },
        {
            "IdDelatnost": 2053,
            " Name": " production of essential oils"
        },
        {
            "IdDelatnost": 2059,
            " Name": " production of other chemical products"
        },
        {
            "IdDelatnost": 2060,
            " Name": " production of artificial fibers"
        },
        {
            "IdDelatnost": 2110,
            " Name": " Manufacture of basic pharmaceutical products"
        },
        {
            "IdDelatnost": 2120,
            " Name": " Production of pharmaceutical preparations"
        },
        {
            "IdDelatnost": 2211,
            " Name": " \"Manufacture of rubber tires and tubes; retreading tires for vehicles\""
        },
        {
            "IdDelatnost": 2219,
            " Name": " Manufacture of other rubber products"
        },
        {
            "IdDelatnost": 2221,
            " Name": " \"Manufacture of plastic plates"
        },
        {
            "IdDelatnost": 2222,
            " Name": " Manufacture of plastic packing"
        },
        {
            "IdDelatnost": 2223,
            " Name": " Production of plastic"
        },
        {
            "IdDelatnost": 2229,
            " Name": " Manufacture of other plastic products"
        },
        {
            "IdDelatnost": 2311,
            " Name": " Manufacture of flat glass"
        },
        {
            "IdDelatnost": 2312,
            " Name": " Shaping and processing of flat glass"
        },
        {
            "IdDelatnost": 2313,
            " Name": " Manufacture of hollow glass"
        },
        {
            "IdDelatnost": 2314,
            " Name": " Manufacture of glass fibers"
        },
        {
            "IdDelatnost": 2319,
            " Name": " \"Production and processing of other glass"
        },
        {
            "IdDelatnost": 2320,
            " Name": " Manufacture of refractory products"
        },
        {
            "IdDelatnost": 2331,
            " Name": " production of ceramic tiles"
        },
        {
            "IdDelatnost": 2332,
            " Name": " \"Manufacture of bricks"
        },
        {
            "IdDelatnost": 2341,
            " Name": " Manufacture of ceramic household and ornamental articles"
        },
        {
            "IdDelatnost": 2342,
            " Name": " Production of sanitary ceramic products"
        },
        {
            "IdDelatnost": 2343,
            " Name": " production of insulators and insulating fittings of ceramics"
        },
        {
            "IdDelatnost": 2344,
            " Name": " Manufacture of other technical ceramic products"
        },
        {
            "IdDelatnost": 2349,
            " Name": " Manufacture of other ceramic products"
        },
        {
            "IdDelatnost": 2351,
            " Name": " Cement production"
        },
        {
            "IdDelatnost": 2352,
            " Name": " Manufacture of lime and plaster"
        },
        {
            "IdDelatnost": 2361,
            " Name": " Manufacture of concrete products for construction"
        },
        {
            "IdDelatnost": 2362,
            " Name": " Manufacture of plaster products for construction purposes"
        },
        {
            "IdDelatnost": 2363,
            " Name": " Production of fresh concrete"
        },
        {
            "IdDelatnost": 2364,
            " Name": " Manufacture of plaster"
        },
        {
            "IdDelatnost": 2365,
            " Name": " Manufacture of fiber cement"
        },
        {
            "IdDelatnost": 2369,
            " Name": " \"Manufacture of other articles of concrete"
        },
        {
            "IdDelatnost": 2370,
            " Name": " \"cutting"
        },
        {
            "IdDelatnost": 2391,
            " Name": " Production of abrasive products"
        },
        {
            "IdDelatnost": 2399,
            " Name": " Manufacture of other non-metallic minerals"
        },
        {
            "IdDelatnost": 2410,
            " Name": " \"The production of pig iron"
        },
        {
            "IdDelatnost": 2420,
            " Name": " \"Steel pipes"
        },
        {
            "IdDelatnost": 2431,
            " Name": " Cold rolling rods"
        },
        {
            "IdDelatnost": 2432,
            " Name": " Cold rolling of flat products"
        },
        {
            "IdDelatnost": 2433,
            " Name": " Cold forming"
        },
        {
            "IdDelatnost": 2434,
            " Name": " Cold drawing of wire"
        },
        {
            "IdDelatnost": 2441,
            " Name": " Precious metals"
        },
        {
            "IdDelatnost": 2442,
            " Name": " Aluminum production"
        },
        {
            "IdDelatnost": 2443,
            " Name": " \"Lead"
        },
        {
            "IdDelatnost": 2444,
            " Name": " copper production"
        },
        {
            "IdDelatnost": 2445,
            " Name": " production of non-ferrous metals"
        },
        {
            "IdDelatnost": 2446,
            " Name": " production of nuclear fuel"
        },
        {
            "IdDelatnost": 2451,
            " Name": " Casting of iron"
        },
        {
            "IdDelatnost": 2452,
            " Name": " Casting of steel"
        },
        {
            "IdDelatnost": 2453,
            " Name": " Casting of light metal"
        },
        {
            "IdDelatnost": 2454,
            " Name": " Casting of other non-ferrous metals"
        },
        {
            "IdDelatnost": 2511,
            " Name": " Manufacture of metal structures and parts of structures"
        },
        {
            "IdDelatnost": 2512,
            " Name": " production of metal doors and windows"
        },
        {
            "IdDelatnost": 2521,
            " Name": " Production of boilers and radiators for central heating"
        },
        {
            "IdDelatnost": 2529,
            " Name": " \"Manufacture of other tanks"
        },
        {
            "IdDelatnost": 2530,
            " Name": " \"Manufacture of steam generators"
        },
        {
            "IdDelatnost": 2540,
            " Name": " Manufacture of weapons and ammunition"
        },
        {
            "IdDelatnost": 2550,
            " Name": " \"Forging"
        },
        {
            "IdDelatnost": 2561,
            " Name": " Treatment and coating of metals"
        },
        {
            "IdDelatnost": 2562,
            " Name": " Machining"
        },
        {
            "IdDelatnost": 2571,
            " Name": " Manufacture of cutlery"
        },
        {
            "IdDelatnost": 2572,
            " Name": " Manufacture of locks and hinges"
        },
        {
            "IdDelatnost": 2573,
            " Name": " Manufacture of tools"
        },
        {
            "IdDelatnost": 2591,
            " Name": " Manufacture of steel drums and similar containers"
        },
        {
            "IdDelatnost": 2592,
            " Name": " Manufacture of light metal"
        },
        {
            "IdDelatnost": 2593,
            " Name": " \"Manufacture of wire products"
        },
        {
            "IdDelatnost": 2594,
            " Name": " production of fasteners and screw machine products"
        },
        {
            "IdDelatnost": 2599,
            " Name": " production of other metal products"
        },
        {
            "IdDelatnost": 2611,
            " Name": " Manufacture of electronic components"
        },
        {
            "IdDelatnost": 2612,
            " Name": " production of printed circuit boards"
        },
        {
            "IdDelatnost": 2620,
            " Name": " Manufacture of computers and peripheral equipment"
        },
        {
            "IdDelatnost": 2630,
            " Name": " Manufacture of communication equipment"
        },
        {
            "IdDelatnost": 2640,
            " Name": " production of electronic devices for consumer"
        },
        {
            "IdDelatnost": 2651,
            " Name": " \"Manufacture of measuring"
        },
        {
            "IdDelatnost": 2652,
            " Name": " Production of watches"
        },
        {
            "IdDelatnost": 2660,
            " Name": " \"Manufacture of irradiation"
        },
        {
            "IdDelatnost": 2670,
            " Name": " Manufacture of optical instruments and photographic equipment"
        },
        {
            "IdDelatnost": 2680,
            " Name": " Manufacture of magnetic and optical media"
        },
        {
            "IdDelatnost": 2711,
            " Name": " \"Manufacture of electric motors"
        },
        {
            "IdDelatnost": 2712,
            " Name": " Manufacture of electricity distribution and control electricity"
        },
        {
            "IdDelatnost": 2720,
            " Name": " ��܉��Manufacture of batteries and accumulators"
        },
        {
            "IdDelatnost": 2731,
            " Name": " production of fiber optic cables"
        },
        {
            "IdDelatnost": 2732,
            " Name": " Manufacture of other electronic and electric wires and cables"
        },
        {
            "IdDelatnost": 2733,
            " Name": " Production equipment for connecting wires and cables"
        },
        {
            "IdDelatnost": 2740,
            " Name": " Production of electric lighting equipment"
        },
        {
            "IdDelatnost": 2751,
            " Name": " production of electrical household appliances"
        },
        {
            "IdDelatnost": 2752,
            " Name": " production of non-electrical household appliances"
        },
        {
            "IdDelatnost": 2790,
            " Name": " Manufacture of other electrical equipment"
        },
        {
            "IdDelatnost": 2811,
            " Name": " \"Manufacture of engines and turbines"
        },
        {
            "IdDelatnost": 2812,
            " Name": " Manufacture of fluid power equipment"
        },
        {
            "IdDelatnost": 2813,
            " Name": " Manufacture of other pumps and compressors"
        },
        {
            "IdDelatnost": 2814,
            " Name": " Manufacture of other taps and valves"
        },
        {
            "IdDelatnost": 2815,
            " Name": " \"Manufacture of bearings"
        },
        {
            "IdDelatnost": 2821,
            " Name": " Manufacture of industrial furnaces and burners"
        },
        {
            "IdDelatnost": 2822,
            " Name": " Manufacture of lifting and handling equipment"
        },
        {
            "IdDelatnost": 2823,
            " Name": " \"Manufacture of office machinery and equipment"
        },
        {
            "IdDelatnost": 2824,
            " Name": " Production of hand drive apparatus with mechanisms"
        },
        {
            "IdDelatnost": 2825,
            " Name": " \"Manufacture of cooling and ventilation equipment"
        },
        {
            "IdDelatnost": 2829,
            " Name": " Production of other machines and devices for general purpose"
        },
        {
            "IdDelatnost": 2830,
            " Name": " Manufacture of agricultural and forestry"
        },
        {
            "IdDelatnost": 2841,
            " Name": " Production of metal processing machines"
        },
        {
            "IdDelatnost": 2849,
            " Name": " Manufacture of other machine tools"
        },
        {
            "IdDelatnost": 2891,
            " Name": " Manufacture of machinery for metallurgy"
        },
        {
            "IdDelatnost": 2892,
            " Name": " \"Manufacture of machinery for mining"
        },
        {
            "IdDelatnost": 2893,
            " Name": " \"Manufacture of machinery for food"
        },
        {
            "IdDelatnost": 2894,
            " Name": " \"Manufacture of machinery for textile"
        },
        {
            "IdDelatnost": 2895,
            " Name": " Manufacture of machinery for paper and paperboard production"
        },
        {
            "IdDelatnost": 2896,
            " Name": " Manufacture of machinery for the production of plastics and rubber"
        },
        {
            "IdDelatnost": 2899,
            " Name": " Manufacture of other special-purpose"
        },
        {
            "IdDelatnost": 2910,
            " Name": " Manufacture of motor vehicles"
        },
        {
            "IdDelatnost": 2920,
            " Name": " \"Manufacture of bodies for motor vehicles"
        },
        {
            "IdDelatnost": 2931,
            " Name": " Manufacture of electrical and electronic equipment for motor vehicles"
        },
        {
            "IdDelatnost": 2932,
            " Name": " Manufacture of other parts and accessories for motor vehicles"
        },
        {
            "IdDelatnost": 3011,
            " Name": " Building of ships and floating structures"
        },
        {
            "IdDelatnost": 3012,
            " Name": " Production boats for sport and leisure"
        },
        {
            "IdDelatnost": 3020,
            " Name": " Production of locomotives and rolling stock"
        },
        {
            "IdDelatnost": 3030,
            " Name": " Manufacture of air and spacecraft and related equipment"
        },
        {
            "IdDelatnost": 3040,
            " Name": " Production of military combat vehicles"
        },
        {
            "IdDelatnost": 3091,
            " Name": " production of motorcycles"
        },
        {
            "IdDelatnost": 3092,
            " Name": " Manufacture of bicycles and invalid carriages"
        },
        {
            "IdDelatnost": 3099,
            " Name": " Manufacture of other transport equipment"
        },
        {
            "IdDelatnost": 3101,
            " Name": " Manufacture of office and shop furniture"
        },
        {
            "IdDelatnost": 3102,
            " Name": " Manufacture of kitchen furniture"
        },
        {
            "IdDelatnost": 3103,
            " Name": " production of mattresses"
        },
        {
            "IdDelatnost": 3109,
            " Name": " Manufacture of other furniture"
        },
        {
            "IdDelatnost": 3211,
            " Name": " mintage"
        },
        {
            "IdDelatnost": 3212,
            " Name": " Manufacture of jewelery and related items"
        },
        {
            "IdDelatnost": 3213,
            " Name": " Manufacture of imitation jewelery and related articles"
        },
        {
            "IdDelatnost": 3220,
            " Name": " Production of musical instruments"
        },
        {
            "IdDelatnost": 3230,
            " Name": " Manufacture of sports goods"
        },
        {
            "IdDelatnost": 3240,
            " Name": " Manufacture of games and toys"
        },
        {
            "IdDelatnost": 3250,
            " Name": " Manufacture of medical and dental instruments and supplies"
        },
        {
            "IdDelatnost": 3291,
            " Name": " Manufacture of brooms and brushes"
        },
        {
            "IdDelatnost": 3299,
            " Name": " Other manufacturing nec"
        },
        {
            "IdDelatnost": 3311,
            " Name": " repair of metal products"
        },
        {
            "IdDelatnost": 3312,
            " Name": " repair machines"
        },
        {
            "IdDelatnost": 3313,
            " Name": " Repair of electronic and optical equipment"
        },
        {
            "IdDelatnost": 3314,
            " Name": " repair of electrical equipment"
        },
        {
            "IdDelatnost": 3315,
            " Name": " repair and maintenance of ships and boats"
        },
        {
            "IdDelatnost": 3316,
            " Name": " repair and maintenance of aircraft and spacecraft"
        },
        {
            "IdDelatnost": 3317,
            " Name": " Repair and maintenance of other transport equipment"
        },
        {
            "IdDelatnost": 3319,
            " Name": " Repair of other equipment"
        },
        {
            "IdDelatnost": 3320,
            " Name": " Installation of industrial machinery and equipment"
        },
        {
            "IdDelatnost": 3511,
            " Name": " electricity production"
        },
        {
            "IdDelatnost": 3512,
            " Name": " Transmission of electricity"
        },
        {
            "IdDelatnost": 3513,
            " Name": " Distribution of electricity"
        },
        {
            "IdDelatnost": 3514,
            " Name": " Electricity trade"
        },
        {
            "IdDelatnost": 3521,
            " Name": " gas production"
        },
        {
            "IdDelatnost": 3522,
            " Name": " Distribution of gaseous fuels through mains"
        },
        {
            "IdDelatnost": 3523,
            " Name": " Trade of gas through mains"
        },
        {
            "IdDelatnost": 3530,
            " Name": " steam and air conditioning supply"
        },
        {
            "IdDelatnost": 3600,
            " Name": " \"Collection"
        },
        {
            "IdDelatnost": 3700,
            " Name": " Sewage"
        },
        {
            "IdDelatnost": 3811,
            " Name": " Collection of non-hazardous waste"
        },
        {
            "IdDelatnost": 3812,
            " Name": " Collection of hazardous waste"
        },
        {
            "IdDelatnost": 3821,
            " Name": " Treatment and disposal of non-hazardous waste"
        },
        {
            "IdDelatnost": 3822,
            " Name": " Treatment and disposal of hazardous waste"
        },
        {
            "IdDelatnost": 3831,
            " Name": " Dismantling of wrecks"
        },
        {
            "IdDelatnost": 3832,
            " Name": " Recovery of sorted materials"
        },
        {
            "IdDelatnost": 3900,
            " Name": " \"Remediation activities and other waste management '"
        },
        {
            "IdDelatnost": 4110,
            " Name": " Development of building projects"
        },
        {
            "IdDelatnost": 4120,
            " Name": " Construction of residential and non-residential buildings"
        },
        {
            "IdDelatnost": 4211,
            " Name": " Construction of roads and motorways"
        },
        {
            "IdDelatnost": 4212,
            " Name": "Construction of railways and underground railways"
        },
        {
            "IdDelatnost": 4213,
            " Name": " construction of bridges and tunnels"
        },
        {
            "IdDelatnost": 4221,
            " Name": " Construction of pipelines"
        },
        {
            "IdDelatnost": 4222,
            " Name": " construction of electrical and telecommunication lines"
        },
        {
            "IdDelatnost": 4291,
            " Name": " Construction of water projects"
        },
        {
            "IdDelatnost": 4299,
            " Name": " Construction of other civil engineering projects nec"
        },
        {
            "IdDelatnost": 4311,
            " Name": " Demolition"
        },
        {
            "IdDelatnost": 4312,
            " Name": " Site preparation"
        },
        {
            "IdDelatnost": 4313,
            " Name": " Test drilling and boring"
        },
        {
            "IdDelatnost": 4321,
            " Name": " Electrical installations"
        },
        {
            "IdDelatnost": 4322,
            " Name": " \"Plumbing"
        },
        {
            "IdDelatnost": 4329,
            " Name": "Other construction installation"
        },
        {
            "IdDelatnost": 4331,
            " Name": " Plastering"
        },
        {
            "IdDelatnost": 4332,
            " Name": " Joinery"
        },
        {
            "IdDelatnost": 4333,
            " Name": " Floor and wall coverings"
        },
        {
            "IdDelatnost": 4334,
            " Name": " Painting and glazing"
        },
        {
            "IdDelatnost": 4339,
            " Name": " Other finishing work"
        },
        {
            "IdDelatnost": 4391,
            " Name": " Roof works"
        },
        {
            "IdDelatnost": 4399,
            " Name": " Other specialized construction activities nec"
        },
        {
            "IdDelatnost": 4511,
            " Name": " Sale of cars and light motor vehicles"
        },
        {
            "IdDelatnost": 4519,
            " Name": " Sale of other motor vehicles"
        },
        {
            "IdDelatnost": 4520,
            " Name": " Maintenance and repair of motor vehicles"
        },
        {
            "IdDelatnost": 4531,
            " Name": " Wholesale trade of parts and accessories for motor vehicles"
        },
        {
            "IdDelatnost": 4532,
            " Name": " Retail sale of parts and accessories for motor vehicles"
        },
        {
            "IdDelatnost": 4540,
            " Name": " \"Trade motorcycles"
        },
        {
            "IdDelatnost": 4611,
            " Name": " \"involved in the sale of agricultural raw materials"
        },
        {
            "IdDelatnost": 4612,
            " Name": " \"involved in the sale of fuels"
        },
        {
            "IdDelatnost": 4613,
            " Name": " involved in the sale of timber and building materials"
        },
        {
            "IdDelatnost": 4614,
            " Name": " \"involved in the sale of machinery"
        },
        {
            "IdDelatnost": 4615,
            " Name": " \"involved in the sale of furniture"
        },
        {
            "IdDelatnost": 4616,
            " Name": " \"involved in the sale of textiles"
        },
        {
            "IdDelatnost": 4617,
            " Name": " \"involved in the sale of food"
        },
        {
            "IdDelatnost": 4618,
            " Name": " Agents specialized in the sale of particular products"
        },
        {
            "IdDelatnost": 4619,
            " Name": " Agents involved in the sale of various products"
        },
        {
            "IdDelatnost": 4621,
            " Name": " \"Wholesale of grain"
        },
        {
            "IdDelatnost": 4622,
            " Name": " Wholesale of flowers and plants"
        },
        {
            "IdDelatnost": 4623,
            " Name": " Wholesale trade of animals"
        },
        {
            "IdDelatnost": 4624,
            " Name": " \"Wholesale of hides"
        },
        {
            "IdDelatnost": 4631,
            " Name": " Wholesale of fruit and vegetables"
        },
        {
            "IdDelatnost": 4632,
            " Name": " Wholesale of meat and meat products"
        },
        {
            "IdDelatnost": 4633,
            " Name": " \"Wholesale dairy products"
        },
        {
            "IdDelatnost": 4634,
            " Name": " Wholesale of beverages"
        },
        {
            "IdDelatnost": 4635,
            " Name": " Wholesale of tobacco products"
        },
        {
            "IdDelatnost": 4636,
            " Name": " \"Wholesale of sugar and chocolate and sugar confectionery\""
        },
        {
            "IdDelatnost": 4637,
            " Name": " \"Wholesale coffee"
        },
        {
            "IdDelatnost": 4638,
            " Name": " \"Wholesale of other food"
        },
        {
            "IdDelatnost": 4639,
            " Name": " \"Non-specialized wholesale of food"
        },
        {
            "IdDelatnost": 4641,
            " Name": " wholesale trade"
        },
        {
            "IdDelatnost": 4642,
            " Name": " Wholesale of clothing and footwear"
        },
        {
            "IdDelatnost": 4643,
            " Name": " Wholesale of electrical household appliances"
        },
        {
            "IdDelatnost": 4644,
            " Name": " \"Wholesale of china and glassware and cleaning\""
        },
        {
            "IdDelatnost": 4645,
            " Name": " Wholesale of perfume and cosmetics"
        },
        {
            "IdDelatnost": 4646,
            " Name": " Wholesale of pharmaceutical goods"
        },
        {
            "IdDelatnost": 4647,
            " Name": " \"Wholesale of furniture"
        },
        {
            "IdDelatnost": 4648,
            " Name": " Wholesale of watches and jewelery"
        },
        {
            "IdDelatnost": 4649,
            " Name": " Wholesale of other household goods"
        },
        {
            "IdDelatnost": 4651,
            " Name": " \"Wholesale of computers"
        },
        {
            "IdDelatnost": 4652,
            " Name": " Wholesale of electronic and telecommunications equipment and parts"
        },
        {
            "IdDelatnost": 4661,
            " Name": " \"Wholesale of agricultural machinery"
        },
        {
            "IdDelatnost": 4662,
            " Name": " Wholesale of machine tools"
        },
        {
            "IdDelatnost": 4663,
            " Name": " Wholesale of mining and construction machinery"
        },
        {
            "IdDelatnost": 4664,
            " Name": " Wholesale of machinery for the textile industry and sewing machines and knitting"
        },
        {
            "IdDelatnost": 4665,
            " Name": " Wholesale of office furniture"
        },
        {
            "IdDelatnost": 4666,
            " Name": " Wholesale of other office machinery and equipment"
        },
        {
            "IdDelatnost": 4669,
            " Name": " Wholesale of other machinery and equipment"
        },
        {
            "IdDelatnost": 4671,
            " Name": " \"Wholesale of solid"
        },
        {
            "IdDelatnost": 4672,
            " Name": " Wholesale of metals and metal ores"
        },
        {
            "IdDelatnost": 4673,
            " Name": " \"Wholesale of wood"
        },
        {
            "IdDelatnost": 4674,
            " Name": " \"Wholesale of hardware"
        },
        {
            "IdDelatnost": 4675,
            " Name": " Wholesale of chemical products"
        },
        {
            "IdDelatnost": 4676,
            " Name": " Wholesale of other intermediate products"
        },
        {
            "IdDelatnost": 4677,
            " Name": " Wholesale of waste and scrap"
        },
        {
            "IdDelatnost": 4690,
            " Name": " specialized wholesale trade"
        },
        {
            "IdDelatnost": 4711,
            " Name": " \"Retail sale in non-specialized stores with food"
        },
        {
            "IdDelatnost": 4719,
            " Name": " Other retail sale in non-specialized stores"
        },
        {
            "IdDelatnost": 4721,
            " Name": " Retail sale of fruit and vegetables in specialized stores"
        },
        {
            "IdDelatnost": 4722,
            " Name": " Retail sale of meat and meat products in specialized stores"
        },
        {
            "IdDelatnost": 4723,
            " Name": " \"Retail sale of fish"
        },
        {
            "IdDelatnost": 4724,
            " Name": " \"Retail sale of bread"
        },
        {
            "IdDelatnost": 4725,
            " Name": " Retail sale of beverages in specialized stores"
        },
        {
            "IdDelatnost": 4726,
            " Name": " Retail sale of tobacco products in specialized stores"
        },
        {
            "IdDelatnost": 4729,
            " Name": " Other retail sale of food in specialized stores"
        },
        {
            "IdDelatnost": 4730,
            " Name": " Retail sale of automotive fuel in specialized stores"
        },
        {
            "IdDelatnost": 4741,
            " Name": " \"Retail sale of computers"
        },
        {
            "IdDelatnost": 4742,
            " Name": " Retail sale of telecommunications equipment in specialized stores"
        },
        {
            "IdDelatnost": 4743,
            " Name": " Retail sale of audio and video equipment in specialized stores"
        },
        {
            "IdDelatnost": 4751,
            " Name": " Retail sale of textiles in specialized stores"
        },
        {
            "IdDelatnost": 4752,
            " Name": " \"Retail sale of hardware"
        },
        {
            "IdDelatnost": 4753,
            " Name": " \"Retail sale of carpets"
        },
        {
            "IdDelatnost": 4754,
            " Name": " Retail sale of electrical household appliances in specialized stores"
        },
        {
            "IdDelatnost": 4759,
            " Name": " \"Retail sale of furniture"
        },
        {
            "IdDelatnost": 4761,
            " Name": " Retail sale of books in specialized stores"
        },
        {
            "IdDelatnost": 4762,
            " Name": " Retail sale of newspapers and stationery in specialized stores"
        },
        {
            "IdDelatnost": 4763,
            " Name": " Retail sale of music and video recordings in specialized stores"
        },
        {
            "IdDelatnost": 4764,
            " Name": " Retail sale of sporting equipment in specialized stores"
        },
        {
            "IdDelatnost": 4765,
            " Name": " Retail sale of games and toys in specialized stores"
        },
        {
            "IdDelatnost": 4771,
            " Name": " Retail sale of clothing in specialized stores"
        },
        {
            "IdDelatnost": 4772,
            " Name": " Retail sale of footwear and leather goods in specialized stores"
        },
        {
            "IdDelatnost": 4773,
            " Name": " Retail sale of pharmaceutical goods in specialized stores - pharmacies"
        },
        {
            "IdDelatnost": 4774,
            " Name": " Retail sale of medical and orthopedic goods in specialized stores"
        },
        {
            "IdDelatnost": 4775,
            " Name": " Retail sale of cosmetic and toilet articles in specialized stores"
        },
        {
            "IdDelatnost": 4776,
            " Name": " \"Retail sale of flowers"
        },
        {
            "IdDelatnost": 4777,
            " Name": " Retail sale of watches and jewelery in specialized stores"
        },
        {
            "IdDelatnost": 4778,
            " Name": " Other retail sale of new goods in specialized stores"
        },
        {
            "IdDelatnost": 4779,
            " Name": " Retail sale of second-hand goods in stores"
        },
        {
            "IdDelatnost": 4781,
            " Name": " \"Retail sale of food"
        },
        {
            "IdDelatnost": 4782,
            " Name": " \"Retail sale of textiles"
        },
        {
            "IdDelatnost": 4789,
            " Name": " Retail sale of other goods via stalls and markets"
        },
        {
            "IdDelatnost": 4791,
            " Name": " Retail sale via mail order houses or via Internet"
        },
        {
            "IdDelatnost": 4799,
            " Name": " \"Other retail sale not in stores"
        },
        {
            "IdDelatnost": 4910,
            " Name": " \"Passenger rail transport"
        },
        {
            "IdDelatnost": 4920,
            " Name": " Train freight"
        },
        {
            "IdDelatnost": 4931,
            " Name": " Urban and suburban passenger land transport"
        },
        {
            "IdDelatnost": 4932,
            " Name": " transportation costs"
        },
        {
            "IdDelatnost": 4939,
            " Name": " Other passenger land transport"
        },
        {
            "IdDelatnost": 4941,
            " Name": " Road transport"
        },
        {
            "IdDelatnost": 4942,
            " Name": " Removal services"
        },
        {
            "IdDelatnost": 4950,
            " Name": " Transport via pipeline"
        },
        {
            "IdDelatnost": 5010,
            " Name": " Sea and coastal passenger"
        },
        {
            "IdDelatnost": 5020,
            " Name": " Sea and coastal freight water transport"
        },
        {
            "IdDelatnost": 5030,
            " Name": " Passenger transport by inland waterways"
        },
        {
            "IdDelatnost": 5040,
            " Name": " Transport of Goods by Inland Waterways"
        },
        {
            "IdDelatnost": 5110,
            " Name": " Passenger air transport"
        },
        {
            "IdDelatnost": 5121,
            " Name": " air freight"
        },
        {
            "IdDelatnost": 5122,
            " Name": " spacecraft traffic"
        },
        {
            "IdDelatnost": 5210,
            " Name": " Storage"
        },
        {
            "IdDelatnost": 5221,
            " Name": " Support activities for land transport"
        },
        {
            "IdDelatnost": 5222,
            " Name": " Service activities incidental to water transportation"
        },
        {
            "IdDelatnost": 5223,
            " Name": " Service activities incidental to air transportation"
        },
        {
            "IdDelatnost": 5224,
            " Name": " Cargo handling"
        },
        {
            "IdDelatnost": 5229,
            " Name": " Other transportation support activities"
        },
        {
            "IdDelatnost": 5310,
            " Name": " postal public service activities"
        },
        {
            "IdDelatnost": 5320,
            " Name": " postal and courier activities"
        },
        {
            "IdDelatnost": 5510,
            " Name": " Hotels and similar accommodation"
        },
        {
            "IdDelatnost": 5520,
            " Name": " Holiday and other short-stay accommodation"
        },
        {
            "IdDelatnost": 5530,
            " Name": " \"activity camps"
        },
        {
            "IdDelatnost": 5590,
            " Name": " Specialty Lodging"
        },
        {
            "IdDelatnost": 5610,
            " Name": " Restaurants and mobile food service"
        },
        {
            "IdDelatnost": 5621,
            " Name": " Kettering"
        },
        {
            "IdDelatnost": 5629,
            " Name": " Other services serving food"
        },
        {
            "IdDelatnost": 5630,
            " Name": " serving drinks"
        },
        {
            "IdDelatnost": 5811,
            " Name": " Book publishing"
        },
        {
            "IdDelatnost": 5812,
            " Name": " Publishing of directories and address books"
        },
        {
            "IdDelatnost": 5813,
            " Name": " Newspaper publishing"
        },
        {
            "IdDelatnost": 5814,
            " Name": " Publishing of journals and periodicals"
        },
        {
            "IdDelatnost": 5819,
            " Name": " Other publishing activities"
        },
        {
            "IdDelatnost": 5821,
            " Name": " Publishing of computer games"
        },
        {
            "IdDelatnost": 5829,
            " Name": " Other software publishing"
        },
        {
            "IdDelatnost": 5911,
            " Name": " \"Motion picture"
        },
        {
            "IdDelatnost": 5912,
            " Name": " Activities The following phase after recording Motion picture and television program"
        },
        {
            "IdDelatnost": 5913,
            " Name": " \"Motion picture"
        },
        {
            "IdDelatnost": 5914,
            " Name": " activity Motion picture"
        },
        {
            "IdDelatnost": 5920,
            " Name": " recording and publishing of sound recordings and music"
        },
        {
            "IdDelatnost": 6010,
            " Name": " Radio broadcasting"
        },
        {
            "IdDelatnost": 6020,
            " Name": " Production and broadcasting of television programs"
        },
        {
            "IdDelatnost": 6110,
            " Name": " Wired telecommunications activities"
        },
        {
            "IdDelatnost": 6120,
            " Name": " Wireless Telecommunications"
        },
        {
            "IdDelatnost": 6130,
            " Name": " Satellite Communications"
        },
        {
            "IdDelatnost": 6190,
            " Name": " Other telecommunications activities"
        },
        {
            "IdDelatnost": 6201,
            " Name": " Computer Programming"
        },
        {
            "IdDelatnost": 6202,
            " Name": " consultancy activities in the field of information technology"
        },
        {
            "IdDelatnost": 6203,
            " Name": " Computer facilities management"
        },
        {
            "IdDelatnost": 6209,
            " Name": " Other information technology"
        },
        {
            "IdDelatnost": 6311,
            " Name": " \"Data processing"
        },
        {
            "IdDelatnost": 6312,
            " Name": " Web portals"
        },
        {
            "IdDelatnost": 6391,
            " Name": " News agency activities"
        },
        {
            "IdDelatnost": 6399,
            " Name": " Other information service activities nec"
        },
        {
            "IdDelatnost": 6411,
            " Name": " the Central Bank"
        },
        {
            "IdDelatnost": 6419,
            " Name": " Other monetary intermediation"
        },
        {
            "IdDelatnost": 6420,
            " Name": " Activities of holding companies"
        },
        {
            "IdDelatnost": 6430,
            " Name": " \"Trust funds (trusts)"
        },
        {
            "IdDelatnost": 6491,
            " Name": " Financial leasing"
        },
        {
            "IdDelatnost": 6492,
            " Name": " Other credit granting"
        },
        {
            "IdDelatnost": 6499,
            " Name": " \"Other financial services"
        },
        {
            "IdDelatnost": 6511,
            " Name": " Life Insurance"
        },
        {
            "IdDelatnost": 6512,
            " Name": " Non-life insurance"
        },
        {
            "IdDelatnost": 6520,
            " Name": " Reinsurance"
        },
        {
            "IdDelatnost": 6530,
            " Name": " Pension funds"
        },
        {
            "IdDelatnost": 6611,
            " Name": " Financial and Commodity Exchange"
        },
        {
            "IdDelatnost": 6612,
            " Name": " brokerage of securities and stock exchange goods"
        },
        {
            "IdDelatnost": 6619,
            " Name": " \"Other activities auxiliary to financial services"
        },
        {
            "IdDelatnost": 6621,
            " Name": " processing damage claims and assessing risk and damage"
        },
        {
            "IdDelatnost": 6622,
            " Name": " Industry representatives and insurance brokers"
        },
        {
            "IdDelatnost": 6629,
            " Name": " Other activities auxiliary to insurance and pension funding"
        },
        {
            "IdDelatnost": 6630,
            " Name": " Fund management"
        },
        {
            "IdDelatnost": 6810,
            " Name": " Buying and selling of own real estate"
        },
        {
            "IdDelatnost": 6820,
            " Name": " rental of own or leased real estate and management"
        },
        {
            "IdDelatnost": 6831,
            " Name": " Real estate agencies"
        },
        {
            "IdDelatnost": 6832,
            " Name": " Property management for a fee"
        },
        {
            "IdDelatnost": 6910,
            " Name": " Legal Affairs"
        },
        {
            "IdDelatnost": 6920,
            " Name": " \"Accounting"
        },
        {
            "IdDelatnost": 7010,
            " Name": " of head offices"
        },
        {
            "IdDelatnost": 7021,
            " Name": " communication activities and public relations"
        },
        {
            "IdDelatnost": 7022,
            " Name": " consultancy activities Business and other management"
        },
        {
            "IdDelatnost": 7111,
            " Name": " Architectural activities"
        },
        {
            "IdDelatnost": 7112,
            " Name": " Engineering activities and related technical consultancy"
        },
        {
            "IdDelatnost": 7120,
            " Name": " Technical testing and analysis"
        },
        {
            "IdDelatnost": 7211,
            " Name": " Research and experimental development on biotechnology"
        },
        {
            "IdDelatnost": 7219,
            " Name": " Research and experimental development on natural sciences and engineering sciences"
        },
        {
            "IdDelatnost": 7220,
            " Name": " Research and development on social sciences and humanities"
        },
        {
            "IdDelatnost": 7311,
            " Name": " Advertising agencies"
        },
        {
            "IdDelatnost": 7312,
            " Name": " Media representation"
        },
        {
            "IdDelatnost": 7320,
            " Name": " Market research and public opinion polling"
        },
        {
            "IdDelatnost": 7410,
            " Name": " Specialized design activities"
        },
        {
            "IdDelatnost": 7420,
            " Name": " Photographic Services"
        },
        {
            "IdDelatnost": 7430,
            " Name": " Translation and interpretation"
        },
        {
            "IdDelatnost": 7490,
            " Name": " \"Other professional"
        },
        {
            "IdDelatnost": 7500,
            " Name": " Veterinary activities"
        },
        {
            "IdDelatnost": 7711,
            " Name": " rental and leasing of cars and light motor vehicles"
        },
        {
            "IdDelatnost": 7712,
            " Name": " rental and leasing of trucks"
        },
        {
            "IdDelatnost": 7721,
            " Name": " Renting and leasing of recreational and sport"
        },
        {
            "IdDelatnost": 7722,
            " Name": " rental video cassettes and compact discs"
        },
        {
            "IdDelatnost": 7729,
            " Name": " Renting and leasing of other personal and household goods"
        },
        {
            "IdDelatnost": 7731,
            " Name": " Renting and leasing of agricultural machinery and equipment"
        },
        {
            "IdDelatnost": 7732,
            " Name": " rental and leasing of machinery and equipment for construction"
        },
        {
            "IdDelatnost": 7733,
            " Name": " rental and leasing of office machinery and equipment (including computers)"
        },
        {
            "IdDelatnost": 7734,
            " Name": " Renting and leasing of water transport"
        },
        {
            "IdDelatnost": 7735,
            " Name": " rental and leasing of air transport"
        },
        {
            "IdDelatnost": 7739,
            " Name": " \"Renting and leasing of other machinery  equipment and tangible goods'"
        },
        {
            "IdDelatnost": 7740,
            " Name": " \"Leasing of intellectual property and similar products  of copyright works and objects of related rights'"
        },
        {
            "IdDelatnost": 7810,
            " Name": " Employment agencies"
        },
        {
            "IdDelatnost": 7820,
            " Name": " agencies for temporary employment"
        },
        {
            "IdDelatnost": 7830,
            " Name": " Other human resources"
        },
        {
            "IdDelatnost": 7911,
            " Name": " Travel agency activities"
        },
        {
            "IdDelatnost": 7912,
            " Name": " Activities of tour operators"
        },
        {
            "IdDelatnost": 7990,
            " Name": " Other reservation service and related activities"
        },
        {
            "IdDelatnost": 8010,
            " Name": " Private security activities"
        },
        {
            "IdDelatnost": 8020,
            " Name": " Security systems service"
        },
        {
            "IdDelatnost": 8030,
            " Name": " Investigation activities"
        },
        {
            "IdDelatnost": 8110,
            " Name": " Maintenance of buildings"
        },
        {
            "IdDelatnost": 8121,
            " Name": " General cleaning of buildings"
        },
        {
            "IdDelatnost": 8122,
            " Name": " Other cleaning buildings and equipment"
        },
        {
            "IdDelatnost": 8129,
            " Name": " Other cleaning"
        },
        {
            "IdDelatnost": 8130,
            " Name": " Landscape service environment"
        },
        {
            "IdDelatnost": 8211,
            " Name": " Combined office administrative services"
        },
        {
            "IdDelatnost": 8219,
            " Name": " \"Photocopying  document preparation and other specialized office support\""
        },
        {
            "IdDelatnost": 8220,
            " Name": " Activities of call centers"
        },
        {
            "IdDelatnost": 8230,
            " Name": " Organization of conventions and trade shows"
        },
        {
            "IdDelatnost": 8291,
            " Name": " Activities of collection agencies and credit bureaus"
        },
        {
            "IdDelatnost": 8292,
            " Name": " Packaging services"
        },
        {
            "IdDelatnost": 8299,
            " Name": " Other business support service activities"
        },
        {
            "IdDelatnost": 8411,
            " Name": " activity of state bodies"
        },
        {
            "IdDelatnost": 8412,
            " Name": " \"Edit activities of providing health care  education cultural services and other social services except compulsory social security\""
        },
        {
            "IdDelatnost": 8413,
            " Name": " Arrangement of business and contribution to more efficient operation in the field of economy"
        },
        {
            "IdDelatnost": 8421,
            " Name": " External Affairs"
        },
        {
            "IdDelatnost": 8422,
            " Name": " Defense Construction"
        },
        {
            "IdDelatnost": 8423,
            " Name": " Justice and judicial activities"
        },
        {
            "IdDelatnost": 8424,
            " Name": " ensuring public order and safety"
        },
        {
            "IdDelatnost": 8425,
            " Name": " Fire service activities"
        },
        {
            "IdDelatnost": 8430,
            " Name": " compulsory social security"
        },
        {
            "IdDelatnost": 8510,
            " Name": " Preschool"
        },
        {
            "IdDelatnost": 8520,
            " Name": " Primary education"
        },
        {
            "IdDelatnost": 8531,
            " Name": " General secondary education"
        },
        {
            "IdDelatnost": 8532,
            " Name": " Secondary vocational education"
        },
        {
            "IdDelatnost": 8541,
            " Name": " Education after secondary non-tertiary"
        },
        {
            "IdDelatnost": 8542,
            " Name": " Higher education"
        },
        {
            "IdDelatnost": 8551,
            " Name": " Sports and recreation education"
        },
        {
            "IdDelatnost": 8552,
            " Name": " Cultural education"
        },
        {
            "IdDelatnost": 8553,
            " Name": " Driving school activities"
        },
        {
            "IdDelatnost": 8559,
            " Name": " Other education"
        },
        {
            "IdDelatnost": 8560,
            " Name": " Educational support activities"
        },
        {
            "IdDelatnost": 8610,
            " Name": " Hospital activities"
        },
        {
            "IdDelatnost": 8621,
            " Name": " General medical practice"
        },
        {
            "IdDelatnost": 8622,
            " Name": " Specialist medical practice"
        },
        {
            "IdDelatnost": 8623,
            " Name": " Dental Practice"
        },
        {
            "IdDelatnost": 8690,
            " Name": " Other human health"
        },
        {
            "IdDelatnost": 8710,
            " Name": " Categories accommodation nursing care"
        },
        {
            "IdDelatnost": 8720,
            " Name": " \"Social Welfare in accommodation facilities for persons with disabilities  the mentally ill and people with addictions\""
        },
        {
            "IdDelatnost": 8730,
            " Name": " Residential care activities for the elderly and persons with special needs"
        },
        {
            "IdDelatnost": 8790,
            " Name": " Other residential care activities"
        },
        {
            "IdDelatnost": 8810,
            " Name": " Social work activities without accommodation for the elderly and persons with special needs"
        },
        {
            "IdDelatnost": 8891,
            " Name": " Activities of daily childcare"
        },
        {
            "IdDelatnost": 8899,
            " Name": " Other unspecified civil social work without accommodation"
        },
        {
            "IdDelatnost": 9001,
            " Name": " Performing Arts"
        },
        {
            "IdDelatnost": 9002,
            " Name": " Other artistic activities within the performing arts"
        },
        {
            "IdDelatnost": 9003,
            " Name": " Artistic creation"
        },
        {
            "IdDelatnost": 9004,
            " Name": " Operation of arts facilities"
        },
        {
            "IdDelatnost": 9101,
            " Name": " Libraries and Archives"
        },
        {
            "IdDelatnost": 9102,
            " Name": " activity of the museum and gallery collections"
        },
        {
            "IdDelatnost": 9103,
            " Name": " \"The protection and maintenance of immovable cultural property  cultural and historical sites and buildings and similar visitor attractions\""
        },
        {
            "IdDelatnost": 9104,
            " Name": " Botanical and zoological gardens and protection of natural values"
        },
        {
            "IdDelatnost": 9200,
            " Name": " Gambling and betting"
        },
        {
            "IdDelatnost": 9311,
            " Name": " Operation of sports facilities"
        },
        {
            "IdDelatnost": 9312,
            " Name": " Activities of sports clubs"
        },
        {
            "IdDelatnost": 9313,
            " Name": " activity fitness clubs"
        },
        {
            "IdDelatnost": 9319,
            " Name": " Other sports activities"
        },
        {
            "IdDelatnost": 9321,
            " Name": " Activities of amusement parks and theme parks"
        },
        {
            "IdDelatnost": 9329,
            " Name": " Other amusement and recreation activities"
        },
        {
            "IdDelatnost": 9411,
            " Name": " Categories business associations and employers' associations"
        },
        {
            "IdDelatnost": 9412,
            " Name": " Activities of professional organizations"
        },
        {
            "IdDelatnost": 9420,
            " Name": " Activities of trade unions"
        },
        {
            "IdDelatnost": 9491,
            " Name": " Activities of religious organizations"
        },
        {
            "IdDelatnost": 9492,
            " Name": " Activities of political organizations"
        },
        {
            "IdDelatnost": 9499,
            " Name": " Activities of other membership organizations"
        },
        {
            "IdDelatnost": 9511,
            " Name": " Repair of computers and peripheral equipment"
        },
        {
            "IdDelatnost": 9512,
            " Name": " Repair of communication equipment"
        },
        {
            "IdDelatnost": 9521,
            " Name": " repair of electronic appliances for wide use"
        },
        {
            "IdDelatnost": 9522,
            " Name": " repair of household appliances and home and garden equipment"
        },
        {
            "IdDelatnost": 9523,
            " Name": " Repair of footwear and leather goods"
        },
        {
            "IdDelatnost": 9524,
            " Name": " Maintenance and repair of furniture"
        },
        {
            "IdDelatnost": 9525,
            " Name": " clocks and jewelery"
        },
        {
            "IdDelatnost": 9529,
            " Name": " Repair of other personal and household goods"
        },
        {
            "IdDelatnost": 9601,
            " Name": " cleaning of textile and fur products"
        },
        {
            "IdDelatnost": 9602,
            " Name": " Hairdressing and other beauty treatment"
        },
        {
            "IdDelatnost": 9603,
            " Name": " Funeral and related activities"
        },
        {
            "IdDelatnost": 9604,
            " Name": " Physical well-being"
        },
        {
            "IdDelatnost": 9609,
            " Name": " Other personal service activities"
        },
        {
            "IdDelatnost": 9700,
            " Name": " Activities of households as employers of domestic"
        },
        {
            "IdDelatnost": 9810,
            " Name": " Activities of households that produce goods for their own use"
        },
        {
            "IdDelatnost": 9820,
            " Name": " Activities of households that provide services to their own needs"
        },
        {
            "IdDelatnost": 9900,
            " Name": " Activities of extraterritorial organizations and bodies"
        }
    ]
    for item in activities:
        if item['IdDelatnost'] == code:
            return item[' Name']


def get_category(code):
    categories = [
      {
        " Name": " government bodies",
        "IdKategorija": 1
      },
      {
        " Name": " Justice",
        "IdKategorija": 2
      },
      {
        " Name": " Health",
        "IdKategorija": 3
      },
      {
        " Name": " culture",
        "IdKategorija": 4
      },
      {
        " Name": " education",
        "IdKategorija": 5
      },
      {
        " Name": " the state public enterprises",
        "IdKategorija": 6
      },
      {
        " Name": " public companies-local government",
        "IdKategorija": 7
      },
      {
        " Name": " city and municipal administration",
        "IdKategorija": 8
      },
      {
        " Name": "  Others",
        "IdKategorija": 9
      }
    ]

    for item in categories:
        if item['IdKategorija'] == code:
            return item[' Name']
def parse():
    collection.remove({})

    print "Importing Data"
    datafile = os.path.dirname(os.path.realpath(__file__)) + '/data/OpenData_2016.csv'

    with open(datafile, "r") as f:
        reader = csv.reader(f, delimiter=',')
        # Save the header of the CSV file which usually
        # contains the keys(descriptions or columns)
        header = reader.next()
        print('Importing data.')
        # Iterate the file line by line, not including first line
        # because we called .next() on the header and it skiped 1'st line
        for row in reader:

            # Create a dictionary to build the document
            dictionary = {}

            # Attach each element of the header list with the
            # elements of the row list
            for h, v in zip(header, row):
                if h == 'IdOpstina':
                    print v
                    dictionary[h] = get_city_name(str(v))
                elif h == 'IdVrstaPostupka':
                    dictionary[h] = get_procedure_type(int(v))
                elif h == 'IdDelatnost':
                    dictionary[h] = get_activity(int(v))
                elif h == 'IdKategorija':
                    dictionary[h] = get_category(int(v))

                else:
                    # print h + " : " + cyrtranslit.to_latin(v)
                    dictionary[h] = cyrtranslit.to_latin(v)

                if h == 'DatumPoslednjeIzmene':
                    try:
                        dictionary[h] = datetime.strptime(v, "%m/%d/%y %H:%M:%S %p")
                    except:
                        pass
            # Add document to MongoDB
            collection.insert(dictionary)
        print('.')


parse()
