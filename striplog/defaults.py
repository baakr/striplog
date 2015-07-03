#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines some default values for parsing cuttings descriptions.

:copyright: 2015 Agile Geoscience
:license: Apache 2.0
"""

LEGEND = """colour, width, comp lithology, comp colour, comp grainsize
#F7E9A6, 3, Sandstone, Grey, VF-F
#FF99CC, 2, Anhydrite, ,
#DBD6BC, 3, Heterolithic, Grey,
#FF4C4A, 2, Volcanic, ,
#86F0B6, 5, Conglomerate, ,
#FF96F6, 2, Halite, ,
#F2FF42, 4, Sandstone, Grey, F-M
#DBC9BC, 3, Heterolithic, Red,
#A68374, 2, Siltstone, Grey,
#A657FA, 3, Dolomite, ,
#FFD073, 4, Sandstone, Red, C-M
#A6D1FF, 3, Limestone, ,
#FFDBBA, 3, Sandstone, Red, VF-F
#FFE040, 4, Sandstone, Grey, C-M
#A1655A, 2, Siltstone, Red,
#363434, 1, Coal, ,
#664A4A, 1, Mudstone, Red,
#666666, 1, Mudstone, Grey, """

LEXICON = {'lithology': [r'overburden', r'sandstone', r'siltstone', r'shale',
                         r'mudstone', r'limestone', r'dolomite',
                         r'salt', r'halite', r'anhydrite', r'gypsum',
                         r'sylvite',
                         r'clay', r'mud', r'silt', r'sand', r'gravel',
                         r'boulders',
                         ],
           'amount': [r'streaks?', r'veins?', r'stringers?',
                      r'interbed(?:s|ded)?',
                      r'blotch(?:es)?', r'bands?', r'fragments?',
                      r'impurit(?:y|ies)',
                      r'minor', r'some', r'abundant', r'rare', r'flakes?',
                      r'[-\.\d]+%'
                      ],
           'grainsize': [r'vf(?:-)?', r'f(?:-)?', r'm(?:-)?', r'c(?:-)?',
                         r'vc',
                         r'very fine(?: to)?', r'fine(?: to)?',
                         r'medium(?: to)?', r'coarse(?: to)?', r'very coarse',
                         r'v fine(?: to)?', r'med(?: to)?', r'med.(?: to)?',
                         r'v coarse',
                         r'grains?', r'granules?', r'pebbles?', r'cobbles?',
                         r'boulders?',
                         ],
           'colour': [r"red(?:dish)?",
                      r"gray(?:ish)?",
                      r"grey(?:ish)?",
                      r"black(?:ish)?",
                      r"whit(?:e|ish)",
                      r"blu(?:e|ish)",
                      r"purpl(?:e|ish)",
                      r"yellow(?:ish)?",
                      r"green(?:ish)?",
                      r"brown(?:ish)?",
                      r"light", "dark",
                      r"sandy"
                      ],
           'synonyms': {'Overburden': ['Drift'],
                        'Anhydrite': ['Gypsum'],
                        'Salt': ['Halite', 'Sylvite'],
                        },
           'parts_of_speech': {'noun': ['lithology'],
                               'adjective': ['colour', 'grainsize'],
                               'subordinate': ['amount'],
                               },
           'abbreviations': {"gt": "gritty", "dist": "distillate", "gr": "grained", "LSD": "legal subdivision", "ptg": "parting", "alg": "algal", "mnr": "minor", "Assem": "Assem", "Vad": "vadose", "MCW": "mud cut water", "Pch": "patch", "gd": "good", "/": "with", "ga": "gauged", "bulb": "bulbous", "Var": "variation", "gn": "green", "alt": "altering", "Gil": "gilsonite", "Oyst": "oyster", "sch": "schist", "Clst": "claystone", "ves": "vesicular", "Nod": "nodules", "tt": "tightly", "V.P.S.": "very poor sample V.P.S.", "asph": "asphaltic", "SIP": "shut in pressure", "tn": "tan", "G&OCM": "gas and oil cut mud", "DI": "dual induction log", "Mol": "mollusca", "Inoc": "inoceramus*", "spec": "speckled", "@": "at", "Amph": "amphipora*", "vert": "vertical", "lrg": "larger", "md": "muddy", "wthrd": "weathered", "Brec": "breccia", "D & A": "dry and abandoned", "fau": "fauna", "depau": "depauperate", "shad": "shadow", "DF": "derrick floor", "gy": "gray", "Elev": "elevation", "indst": "indistinct", "Syring": "syringopora*", "fac": "faceted", "GL": "guard log", "brhg": "branching", "Gt": "grit", "Gr": "grains", "FIt": "fault", "Tas": "tasmanites*", "Spr": "spore", "fenst": "fenestral", "plag": "plagioclase", "p": "poorly", "Spk": "speck", "Spl": "sampole", "SNP": "sidewall neutron porosity log", "n.s.": "no sample", "Clcar": "calcarenite", "pbl": "pebble (4-64 mm)", "cmt": "cemented", "Spg": "sponge", "Grv": "gravel", "Cyp": "cypridopsis*", "Grt": "granite", "SP": "spontaneous potential", "Res": "residue", "Bioh": "bioherm", "Biost": "biostrom", "tex": "texture", "Brach": "brachiopod", "hydc": "hydrocarbon", "Ren": "renalcis*", "Biot": "biotite", "Peld": "pelletoid", "Bld": "boulder", "ter": "terriginous", "splty": "splintery", "acic": "acicular", "sug": "sugary", "bdd": "bedded", "bdg": "bedding", "gl": "glassy", "abd": "abundant", "Intst": "intersticies", "Micr": "micrite", "O str": "Ostracod", "Clcsp": "calcisphere", "bl": "bluish", "abs": "absent", "abt": "about", "conspic": "conspicuous", "Spfool": "superficial olite", "sli": "slightly", "med": "medium", "O&SW": "oil and salt water", "biocl": "bioclastic", "Agg": "aggregate", "DST": "drill stem test", "Mn": "manganese", "psdo": "pseudo", "len": "lentilcular", "rug": "rugosa", "Wd": "wood", "hkl": "hackly", "DLL": "dual laterolog", "t.s.": "thin section", "Mtrx": "matrix", "crpxln": "crystocrystalline", "Zn": "zone", "Anthr": "anthracite", "altg": "alternating", "blksh": "blackish", "bor": "boreding", "dru": "drusy", "ctd": "coated", "Conc": "concretion", "wtr cush": "water cushion", "ctc": "contact", "micropor": "microporosity", "Zr": "zircon", "Cono": "conodont", "sft": "soft", "Piso": "pisoid", "LL": "laterolog", "lmn": "limonitic", "volc": "volcanics", "Ctgs": "cuttings", "apr": "apparent", "tr": "trace", "app": "appear", "brt": "bright", "ls": "limestone", "Slt": "silt", "Circ": "circulate", "aph": "aphanitic", "oomol": "oomoldic", "brk": "brackish", "vit": "vitreous", "org": "organic", "n.v.p.": "no visible porosity", "w/": "with", "brd": "bored", "intxln": "intercrystalline", "Para": "paraparchites*", "Fp": "flowing pressure", "Ft": "foot", "perf": "perforated", "&": "and", "fen": "fenestraal", "pred": "predominantly", "Phlog": "phloaopite", "perm": "permeability", "fibr": "fibrous", "msm": "metasomatic", "cht": "chert", "Fe": "iron-ferruginous", "dns": "denser", "vi": "violet", "fros": "frosted", "calc": "calcitareous", "Fm": "formation", "pres": "preservation", "cntrt": "contorted", "wvy": "wavy", "vps": "very poor samples", "ooc": "oocastic", "musc": "muscovite", "glas": "glassy", "Sh": "shale", "lchd": "leached", "rhb": "rhombic", "glau": "glauconitic", "Brac": "brachiopod", "choc": "chocolate", "chit": "chitinous", "Str": "structure", "Sl": "slate", "clus": "cluster", "Sa": "salt", "Cmt": "cement", "lmpy": "lumpy", "Sd": "sand", "intrapar": "intraparticle", "phos": "phosphatic", "prly": "pearly", "Lstr": "lustre", "tns": "tension", "f": "finely", "fls": "flesh", "des": "descript", "SW": "salt water", "flt": "faulted", "Cbl": "cobble", "plty": "platy", "lithgr": "lithographic", "flk": "flake", "W.R.": "washed residue", "SO": "show of oil", "v": "very", "deb": "debris", "slty": "silty", "fld": "feldsparthic", "flg": "flaggy", "ptch": "patches", "Lig": "lignite", "mica": "micaeous", "bent": "bentonitic", "Min": "mineral", "sy-Ca": "sparry calcite", "Lim": "limonite", "Invtb": "invertebrate", "sps": "sparsly", "Mid": "middle", "yelsh": "ish", "sph": "spherules", "spl": "sample", "Ls": "limestone", "tab": "tabular", "Plcy": "palecypod", "scat": "scattered", "psool": "pseudo oolitic", "GR": "gamma ray", "spsly": "sparsly", "Bdeye": "birdseye", "purp": "purple", "Pyr": "pyrite", "hom": "homogeneous", "Kao": "kaolin", "Spic": "spicule", "hor": "horizontal", "Belm": "belemnites*", "sid": "sideritic", "aft": "after", "Rhb": "rhomb", "Typ": "type", "sim": "similar", "sil": "siliceous", "frag": "fragmental", "lam": "laminated", "fr": "fair", "mar": "maroon", "frac": "fractured", "srt": "sorting", "Dol": "dolomite", "I.P.": "in part", "cpct": "compact", "max": "maximum", "insl": "insoluble", "lac": "lacustrine", "Mrl": "marl", "mag": "magnetic", "Ctc": "contact", "ireg": "irregular", "lav": "lavender", "IAB": "initial air blow", "fl": "filled", "Tril": "trilobite", "Foram": "foraminifera", "MMCFG": "million cubic feet of gas", "Clvg": "cleavage", "Alg": "algal", "sp": "spotty", "Deer": "decrease", "Microspr": "microspar", "su": "sulphurous", "or": "orangish", "strk": "streaked", "stri": "striated", "sh": "shale", "Moll": "mollusc", "spkld": "speckled", "sm": "smooth", "sl": "slightly", "sc": "scales", "sb": "sub", "sa": "salt", "strg": "stringer", "Trip": "tripoli", "Equiv": "equivalent", "lse": "loose", "mnut": "minute", "BHCS": "bore hole compensated sonic", "Cal": "caliper", "Chk": "chalk", "Biomi": "biomicrite", "brit": "brittle", "coln": "colonial", "Smwt": "somewhat", "Rf": "reef", "Cht": "chert", "(D)": "development", "decr": "decreasing", "Rk": "rock", "RT": "rotary table", "fis": "fissile", "cln": "clean", "xl": "crystalline", "cbl": "cobble (64-256 mm)", "Aglm": "agglomerate", "Evap": "evapourite", "sa-c": "salt castic", "fib": "fibrous", "imp": "impression", "lt": "lighter", "eux": "euxinic", "cren": "crenulated", "gty": "gravity", "dess": "dessiccation", "clr": "clear", "TSTM": "too small to measure", "Bas": "basalt", "Shw": "show", "nod": "nodule", "uncons": "unconsolidated", "rexl": "recrystallization", "Cav": "cavernous", "FAB": "fair air blow", "aprox": "approximately", "\u20b5": "core", "Schm": "schist", "Shl": "shell", "xln": "crystalline", "Rad": "radial", "Oomol": "oomold", "Dist": "distillate", "extr": "extremely", "l": "lower", "Anhy": "anhydrite", "intv": "interval", "Stach": "stachyodes*", "crpxl": "cryptocrystalline", "Poln": "pollen", "Chtz": "chitinozoa", "MCFG": "thousand cubic feet of gas", "frmwk": "framework", "Lith": "lithology", "Macrofos": "macrofossil", "prphy": "porphyry", "Lut": "lutite", "OFM": "oil flecked mud", "Asph": "assemblage", "intpar": "interparticle", "Perm": "permeability", "Bdst": "boundstone", "chty": "cherty", "meta": "metamorphic", "ex": "excellent", "hrtl": "horizontal", "p-p": "pin point", "zeo": "zeolite", "n/s": "no show", "nac": "nacerous", "Wtr": "water", "apprx": "approximate", "rr": "rare", "Musc": "muscovite", "intclas": "intraclastic", "rep": "replacedment", "porcel": "porcelaneous", "BOPH": "barrels of oil per hour", "rd": "rounded", "rf": "reefoid", "sml": "small", "blk": "black", "IP": "initial production", "bld": "bladed", "Tub": "tube", "Pisol": "pisolite", "mtx": "matrix", "lmy": "limy", "Phos": "phosphate", "crd": "cored", "G": "gas", "Spo": "spore", "GCM": "gas cut mud", "SGCM": "slight gas cut mud", "OWWO": "old well worked over", "Novac": "novaculite", "rhmb": "rhombic", "argl": "argillate", "W": "west", "carb": "carbonaceous", "Frac": "fracture", "freq": "frequent", "ES": "electric", "Pyrxn": "pyroxene", "g": "good", "Contam": "contamination", "srtg": "Sorteding", "Chal": "chalcedony", "fspr": "feldsparathic", "Char": "charophyte", "SSO": "slight show of oil", "Hyde": "hydrocarbon", "w": "well", "intgn": "inter grown", "vrtb": "vertebrate", "Sphal": "sphalerite", "intpt": "interpretation", "cche": "caliche", "Frg": "fringe", "sacc": "saccharoidal", "onc": "oncolites", "Slick slick": "slickenside", "Diagn": "diagenesis", "zn": "zone", "Imp": "impression", "sblit": "sublithic", "Prod": "production", "Incl": "inclusion", "Frag": "fragment", "sphal": "sphalerite", "Iran": "granule", "dtrl": "detritalus", "wthd": "weathered", "WCM": "water cut mud", "GCW": "gas cut water", "Pet": "petroleum", "Microstyl": "microstylolite", "Volc": "volcanic", "BWPH": "barrels of water per hour", "thru": "throughout", "intcl": "intraclasts", "Biosp": "biosparite", "Girv": "girvanella*", "OWDD": "oil well drilled deeper", "consol": "consolidated", "Fus": "fusulinid", "sz": "size", "grysh": "greyish", "mrlst": "marlstone", "Strk": "streak", "SGCW": "slight gas cut water", "crnk": "crinkled", "Rbl": "rubble", "Fuc": "fucoid", "bdeye": "birdseye", "gyp": "gypsumiferous", "orng": "orange", "Endo": "endothyra*", "BHFP": "bottom hole flow pressure", "Xl": "crystal", "stn": "staining", "Qtz": "quartz", "csg": "casing", "Chlor": "chlorite", "r": "rare", "mky": "milky", "str": "streak", "Onc": "oncolite", "Btm": "bottom", "Slst": "siltstone", "dissem": "disseminated", "spr": "sparry", "Pap": "paper", "grnt": "granite", "Par": "particle", "ang": "angular", "Descr": "description", "intgwn": "intergrown", "Stylio": "styliolina*", "Intclas": "intraclast", "Rem": "remains", "chlor": "chlorite", "euhd": "euhedral", "Pend": "pendularous", "Rec": "recovery", "grnl": "granule (2-4 mm)", "Calc": "calcite", "p.d": "pressure deformation", "recem": "recemented", "strgr": "stringer", "lig": "lignitic", "Glauc": "glauconite", "intbd": "interbedded", "lim": "itic", "mic": "micro", "Db": "diabase", "Port por": "porosity", "Ech": "echinoid", "lit": "lithic", "Fluor": "fluoresceince", "vrvd": "varved", "Arag": "aragonite", "vgt": "varigated", "Clus": "cluster", "mot": "mottled", "surf": "surface", "pos": "possibility", "plas": "plastic", "pyr": "pyritized", "In": "inch", "kao": "kaolin", "Orbit": "Orbitolina", "MLL": "microlaterolog", "sdy": "sandy", "Mic": "micaceous", "Plt": "plant", "assoc": "associated", "rthy": "earthy", "Ivan": "ivanovia*", "suc": "sucrosic", "intercal": "intercalated", "glos": "glossy", "typ": "typical", "abv": "above", "MCO": "mud cut oil", "Unconf": "unconformity", "Bent": "bentonite", "dol": "dolomitic", "dom": "dominant", "flor": "fluorescence", "sltst": "siltstone", "brec": "brecciated", "Stri": "striae", "dism": "disseminated", "BHT": "bottom hole temperature", "exv": "extrusive", "Pol": "polish", "GTS": "gas to surface", "Mbr": "member", "exp": "exposed", "Pybit": "pyrobitumen", "a.a.": "same as above sample", "intlam": "interlaminated", "sd": "sand (1/16-2 mm)", "Rpl": "ripple", "dend": "dendritic", "pkr": "packer", "drlg": "drilling", "Spher": "spherule", "Hal": "halitiferous", "lstr": "lustre", "Exclas": "extraclast", "ML": "microlog, minilog", "anhy": "anhydritic", "drlr": "driller", "Rud": "rudist", "grapst": "grapestone", "Bubl": "bubble", "pris": "prismatic", "Bnd": "band", "och": "ochre", "spher": "spherulitic", "Jt": "joint", "occ": "occasional", "Wl": "well", "varic": "varicolored", "intrlam": "interlaminated", "O&G": "oil and gas", "mnrl": "mineralized", "Shlt por": "shelter porosity", "AOF": "absolute open flow", "Gyp": "gypsumiferous", "Bit": "bitumen", "Gast": "gastropod", "Pst": "pumice-stone", "PB": "plugged back", "Stromlt": "stromatolite", "BO": "barrels of oil", "dk": "darker", "CN": "compensated neutron", "KB": "kelly bushing", "dd": "dead", "Intvl": "interval", "stromlt": "stromatolite", "Fspr": "feldspar", "Milid": "miliolid", "cotg": "coateding", "cotd": "coateding", "repl": "replacement", "slily": "slightly", "struc": "structure", "SO&G": "show of oil and gas", "gen": "generally", "hetr": "heterogeneous", "crs": "coarse", "bar": "baritic", "bas": "basaltic", "(W)": "wildcat", "shy": "shaly", "FDL": "formation density log", "w/o": "without w/o", "BW": "barrels of water", "rsns": "resinous", "PL": "proximity log", "gran": "granular", "BWPD": "barrels of water per day", "x": "cross", "grad": "grading", "Qtzt": "quartzite", "crm": "cream", "res": "residuual", "Pt": "part", "OTD": "old total depth", "contam": "contaminated", "S.W.C.": "sidewall core", "qtz": "quartz", "magnt": "magnetite", "Pel": "pellet", "num": "numerous", "sec": "secondary", "fnly": "finly", "arg": "argillaceous", "ark": "arkosic", "rmn": "remainant", "prim": "primary", "volat": "volatile", "SOCW": "slight oil cut water", "piso": "pisolitic", "pkish": "pinkish", "metaph": "metamorphosed", "trnsp": "transparent", "irr": "irregular", "hornbd": "hornblend", "'' or do": "ditto", "biost": "biostromal", "gept": "geopetal", "trnsl": "translucent", "PD": "per day", "PH": "per hour", "SO&W": "show of oil and water", "Vnlet": "veinlet", "Tham": "thamnopora*", "wg": "vuggy", "C": "coal", "men": "meniscus", "exclas": "extraclastic", "lg": "long", "jt": "jointing", "comp": "completion", "gnsh": "greenish", "wk": "weak", "wi": "with", "wh": "white", "Exv": "extrusive rock", "S": "sonic, acoustilog", "magn": "magnetic", "gywk": "graywacke", "G.W.": "granite wash", "Satm sat": "saturation", "tub": "tubular", "tuf": "tuffaceous", "coq": "coquina", "vug": "vugular", "c": "coarsely", "fnt": "faintly", "dkr": "darker", "cov": "covered", "conch": "conchoidal", "intgran": "intergranular", "SI": "shut in", "Chit": "chitinous", "s": "small", "Meta": "metamorphic rock", "Sst": "sandstone", "brak": "brackish", "uni": "uniform", "com": "common", "cotd gn": "coated grains", "Het": "Heterostegina", "foram": "foraminiferal", "chky": "chalky", "cl": "clastic", "cb": "carbonized", "Glas": "glass", "rad": "radiating", "poly": "polygonal", "hvy": "heavy", "pol": "polished", "Pent": "pentamerus*", "Hem": "hematite", "tgh": "tough", "cp": "compare", "Surf": "surface", "ps": "pseudo-", "frg": "fringing", "pt": "partly", "Bur": "burrow", "fri": "friable", "blsh": "bluish", "pch": "patchy", "stmg": "streaming", "frs": "fresh", "skel": "skeletal", "pyrbit": "pyrobitumen", "pk": "pink", "devit": "devitrified", "authg": "authigenic", "pl": "plant", "cly": "clayey", "t.b.": "thin-bedded", "Tr": "trace", "IES": "induction electric", "WAB": "weak air blow", "lge": "large", "spic": "spicular", "psi": "pounds per square inch", "crbnt": "carbonate", "Tp": "top", "Pkst": "packstone", "Sedm": "sediment", "Cont": "content", "xbdg": "cross-bedding", "gns": "gneiss", "micgr": "micrograined", "Cl": "clay", "slt": "silt", "vcol": "varicolored", "undly": "underlying", "grnt.w": "granite wash", "n": "no, none, non", "contm": "contaminated", "sln": "solution", "rbl": "rubblbly", "fuc": "fucoidal", "Intr": "intrusive", "cvg": "cavings", "k": "permeabilityable", "slb": "slabby", "FTAB": "faint air blow", "DIL": "dual induction laterolog", "pyrcl": "pyroclastic", "cons": "considerable", "rndd": "rounded", "bot": "botryoidal", "Sel": "selenite", "vn": "vein", "Tf": "tuffaceous", "styl": "stylotitic", "conc": "concretionary", "mott": "mottled", "xlam": "cross-laminated", "x-strat": "cross-stratified", "Strom": "stromatoporoid", "ig": "igneous", "pap": "papery", "incr": "increasing", "litt": "littoral", "intstl": "interstitial", "bioturb": "bioturbated", "PPM": "parts per million", "GAP": "good air blow", "Repl": "replaced", "lith": "lithographic", "elong": "elongate", "Chara": "charophytes", "sat": "saturated", "incl": "inclusion", "Coq": "coquina", "Vug": "vug", "Cor": "coral", "intst": "intersticitial", "cncn": "concentric", "rng": "range", "orth": "orthoclase", "rdsh": "redish", "syn": "syntaxial", "Microfos": "microfossilferous", "phr": "phreatic", "Wkst": "wackestone", "pisol": "pisolitic", "Col": "color", "Jasp": "jasper", "Mat": "material", "Mbl": "marble", "intxl": "intercrystalline", "detr": "detrital", "sed": "sedimentary", "x-bd": "cross-bedded", "gsy": "grasy", "OWPB": "oil well plugged back", "min": "mineralized", "Sol": "Soution", "Vn": "vein", "col": "colored", "x-lam": "cross-laminated", "thn": "thin", "thk": "thick", "fltg": "floating", "Ig": "igneous rock", "imbd": "imbedded", "ck": "choke", "BHP": "bottom hole pressure", "yel": "yellow", "Orth": "orthoclase", "sptd": "spottedy", "spty": "spottedy", "Sphaer": "sphaerocodium*", "Pbl": "pebble", "intfrag": "interfragmental", "Scaph": "scaphopod", "resd": "residual", "Bd": "bed", "Fe-mag": "ferro-magnesian", "sks": "slickensided", "rexlzd": "recrystallized", "Bm": "basement", "Glob": "globigerina*", "elg": "elongate", "unident": "unidentifiable", "Fau": "fauna", "Gal": "galeolaria*", "cub": "cubic", "Fac": "facet", "Glos": "gloss", "Gab": "gabbro", "bnd": "banded", "Oo": "ooid", "Gns": "gneiss", "amb": "amber", "strat": "strataified", "amm": "ammonite", "vis": "visible", "mos": "mosaic", "por": "poroussity", "uncons.": "unconsolidated", "embd": "embedded", "Dia": "diameter", "rnd": "rounded", "sbang": "subangular", "cntr": "centered", "mol": "moldic", "Cvg": "caving", "bit": "bitumeninous", "Micropor": "micropore", "S.W.": "salt water", "amt": "amount", "mod": "moderate", "Crin": "crinoidal", "Lyr": "layer", "brn": "brown", "boudg": "boudinage", "OC": "oil cut", "Microol": "micro-oolite", "Ltl": "little", "V.op": "valve open", "amor": "amorphous", "Ark": "arkose", "clas": "clastic", "Psool": "pseudo oolite", "Strat": "strata", "Bdg": "bedding", "bri": "bright", "drsy": "drusy", "tstg": "testing", "Scol": "scolecodonts", "crpld": "crumpled", "SOCM": "slight oil cut mud", "rec": "recovered", "Fvst": "favosites*", "sbrndd": "sub rounded", "p.p.": "pin-poin", "HO": "heavy oil", "olv": "olive", "Mdst": "mudstone", "s & p": "salt and pepper", "venn": "vermillon", "u": "upper", "gvl": "gravel", "fos": "fossiliferous", "pet": "petroleumiferous", "Clclt": "calcilutite", "OSR": "oil source rock", "Len": "lens", "pel": "pellet", "circ": "circulation", "prom": "prominently", "fol": "foliated", "peld": "pelletoidal", "Tent": "tentaculites*", "prob": "probably", "bd": "bed", "flky": "flaky", "bf": "buff", "LL8": "laterolog-8", "cgl": "conglomerate", "Gwke": "graywacke", "slky": "silky", "Grap": "graptolite", "Bor": "bored", "bo": "bophaceous", "Bot": "botryoid", "phen": "phenocrysts", "posa": "possible", "bu": "buff", "sel": "selenite", "Gran": "granule", "r.f.p": "rounded frosted pitted", "Clslt": "calcisiltite", "ss": "sandstone", "Uc": "underclay", "oo": "ooidal", "GOR": "gas-to-oil ratio", "Clcrd": "calcirudite", "euhed": "euhedral", "Solen": "solenopora*", "Euryamph": "euryamphipora*", "Ptg": "parting", "od": "odor", "eqnt": "equant", "Ost": "ostracod", "o": "oil", "Ceph": "cephalopod", "irid": "iridescent", "ox": "oxidized", "Casph": "calcisphaera*", "ti": "tight", "Foss": "fossiliferous", "sept": "septate", "marn": "marine", "Scs": "scarce", "op": "open", "chk": "chalky", "ahd": "anhedral", "Fen": "fenestra", "qtzc": "quartzitic", "sol": "solitary", "corln": "coralline", "mas": "massive", "ferr": "ferruginous", "Cub": "cube", "intr": "intrusionive", "Chaet": "chaetetes*", "OCM": "oil cut mud", "qtzs": "quartzose", "qtzt": "quartzite", "GIP": "good initial puff", "loc": "location", "blky": "blocky", "phyl": "phyllitic", "vrtl": "vertical", "Ooc": "oolicast", "anhed": "anhedral", "aren": "arenaceous", "Ool": "oolite", "bioh": "biohermal", "diagn": "diagenesisetic", "Pelec": "pelecypod", "biot": "biotite", "abnt": "abundant", "var": "variable", "hem": "hematitic", "gil": "gilsonite", "calctc": "calcitic", "clyst": "claystone", "fl/": "flowing", "bur": "burrowed", "ea": "earthy", "micr": "micritic", "grdg": "grading", "Flk": "flake", "hi": "high", "s&p": "salt & pepper", "Flo": "flora", "Deb": "debris", "Splin": "splintery", "hd": "hard", "coqid": "coquinaoid", "Grst": "grainstone", "Phyl": "phyllite", "med.": "medium", "microxln": "microcrystalline", "Plag": "plagioclase", "mat": "material, matter", "bldr": "boulder", "up": "upper", "Tex": "texture", "mdy": "muddy", "WIP": "weak initial puff", "olvn": "olivine", "ab": "above", "mrl": "marly", "orsh": "orangish", "Allo": "allochem", "m": "medium", "deer": "decreasing", "chal": "chalcedony", "ovgth": "overgrowth", "ap": "appears", "Sid": "siderite", "ind": "indurated", "pit": "pitted", "trip": "tripolic", "DL": "density log", "Sil": "silica", "Lam": "laminations", "F.Q.G.": "frosted quartz  grains", "Cgl": "conglomerate", "hex": "hexagonal", "wxy": "waxy", "gry": "greyish", "Fe-st": "ironstone", "oom": "oomoldic", "grd": "graded", "BHSIP": "bottom hole shut in pressure", "Mag": "magnetite", "ool": "oolitic", "Lat": "laterite", "mass": "massive", "T.D.": "total depth", "Stn": "stain", "sqz": "squeezed", "E": "east", "BOPD": "barrels of oil per day", "aglm": "agglomerate", "evap": "evapourititic", "fluor": "fluoresceincent", "est": "estimated", "Su": "sulphur", "lent": "lenticular", "stal": "stalactitic", "N": "Neutron", "wtr": "water", "dolst": "dolostone", "bcm": "becoming", "OTS": "oil to surface", "SAB": "strong air blow", "Bry": "bryozoa", "O-Qtz": "orthoquartzite", "Styl": "stylolite", "crinal": "crinoidal", "Brk": "break", "mrly": "marly", "Av": "average", "xbd": "cross-bedded", "Radax": "radiaxial", "swbd": "swabbed"}
           }
