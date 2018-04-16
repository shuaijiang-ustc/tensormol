#
# This is a tentative set of atomic identity data.
# Anyone got an opinion about a better spot for this?
#

from __future__ import absolute_import
import numpy as np

AtomFields = ['symbol','name','atomicnum','mass','ns','np','nd','elecneg','radius','ione','elecaff','polariz']
AtomData = [['X','Nullium', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
['H','Hydrogen', 1.0, 1.00794, 1.0, 0.0, 0.0, 2.3, 53.0, 1312.0, 0.754195, 4.4923955],
['He','Helium', 2.0, 4.002602, 2.0, 0.0, 0.0, 4.16, 31.0, 2372.0, -0.52, 1.383191],
['Li','Lithium', 3.0, 6.941, 1.0, 0.0, 0.0, 0.912, 167.0, 520.0, 0.618049, 164.0],
['Be','Beryllium', 4.0, 9.012182, 2.0, 0.0, 0.0, 1.576, 112.0, 900.0, -0.52, 37.71],
['B','Boron', 5.0, 10.811, 2.0, 1.0, 0.0, 2.051, 87.0, 801.0, 0.279723, 20.53],
['C','Carbon', 6.0, 12.0107, 2.0, 2.0, 0.0, 2.544, 67.0, 1087.0, 1.2621226, 11.26],
['N','Nitrogen', 7.0, 14.0067, 2.0, 3.0, 0.0, 3.066, 56.0, 1402.0, -0.000725, 7.26],
['O','Oxygen', 8.0, 15.9994, 2.0, 4.0, 0.0, 3.61, 48.0, 1314.0, 1.4611136, 5.24],
['F','Fluorine', 9.0, 18.9984032, 2.0, 5.0, 0.0, 4.193, 42.0, 1681.0, 3.4011898, 3.7],
['Ne','Neon', 10.0, 20.1797, 2.0, 6.0, 0.0, 4.787, 38.0, 2081.0, -1.2, 2.67],
['Na','Sodium', 11.0, 22.98976928, 1.0, 0.0, 0.0, 0.869, 190.0, 496.0, 0.547926, 162.7],
['Mg','Magnesium', 12.0, 24.305, 2.0, 0.0, 0.0, 1.293, 145.0, 738.0, -0.415, 70.89],
['Al','Aluminum', 13.0, 26.9815386, 2.0, 1.0, 0.0, 1.613, 118.0, 578.0, 0.43283, 55.4],
['Si','Silicon', 14.0, 28.0855, 2.0, 2.0, 0.0, 1.916, 111.0, 787.0, 1.3895212, 37.31],
['P','Phosphorus', 15.0, 30.973762, 2.0, 3.0, 0.0, 2.253, 98.0, 1012.0, 0.746607, 24.93],
['S','Sulfur', 16.0, 32.065, 2.0, 4.0, 0.0, 2.589, 88.0, 1000.0, 2.0771042, 19.37],
['Cl','Chlorine', 17.0, 35.453, 2.0, 5.0, 0.0, 2.869, 79.0, 1251.0, 3.612724, 14.57],
['Ar','Argon', 18.0, 39.948, 2.0, 6.0, 0.0, 3.242, 71.0, 1521.0, -1.0, 11.07],
['K','Potassium', 19.0, 39.0983, 1.0, 0.0, 0.0, 0.734, 243.0, 419.0, 0.501459, 290.6],
['Ca','Calcium', 20.0, 40.078, 2.0, 0.0, 0.0, 1.034, 194.0, 590.0, 0.02455, 155.9],
['Sc','Scandium', 21.0, 44.955912, 2.0, 0.0, 1.0, 1.19, 184.0, 633.0, 0.188, 142.28],
['Ti','Titanium', 22.0, 47.867, 2.0, 0.0, 2.0, 1.38, 176.0, 659.0, 0.084, 114.34],
['V','Vanadium', 23.0, 50.9415, 2.0, 0.0, 3.0, 1.53, 171.0, 651.0, 0.52766, 97.34],
['Cr','Chromium', 24.0, 51.9961, 1.0, 0.0, 5.0, 1.65, 166.0, 653.0, 0.67584, 78.4],
['Mn','Manganese', 25.0, 54.938045, 2.0, 0.0, 6.0, 1.75, 161.0, 717.0, -0.52, 66.8],
['Fe','Iron', 26.0, 55.845, 2.0, 0.0, 7.0, 1.8, 156.0, 763.0, 0.153236, 62.65],
['Co','Cobalt', 27.0, 58.933195, 2.0, 0.0, 8.0, 1.84, 152.0, 760.0, 0.66226, 57.71],
['Ni','Nickel', 28.0, 58.6934, 2.0, 0.0, 8.0, 1.88, 149.0, 737.0, 1.15716, 51.1],
['Cu','Copper', 29.0, 63.546, 1.0, 0.0, 10.0, 1.85, 145.0, 746.0, 1.2357, 40.7],
['Zn','Zinc', 30.0, 65.38, 2.0, 0.0, 10.0, 1.59, 142.0, 906.0, -0.62, 38.8],
['Ga','Gallium', 31.0, 69.723, 2.0, 1.0, 10.0, 1.756, 136.0, 579.0, 0.43, 51.4],
['Ge','Germanium', 32.0, 72.64, 2.0, 2.0, 10.0, 1.994, 125.0, 762.0, 1.23676, 39.43],
['As','Arsenic', 33.0, 74.9216, 2.0, 3.0, 10.0, 2.211, 114.0, 947.0, 0.8048, 29.8],
['Se','Selenium', 34.0, 78.96, 2.0, 4.0, 10.0, 2.424, 103.0, 941.0, 2.02, 26.24],
['Br','Bromine', 35.0, 79.904, 2.0, 5.0, 10.0, 2.685, 94.0, 1140.0, 3.363588, 21.03],
['Kr','Krypton', 36.0, 83.798, 2.0, 6.0, 10.0, 2.966, 88.0, 1351.0, -0.62, 17.075],
['Rb','Rubidium', 37.0, 85.4678, 1.0, 0.0, 0.0, 0.706, 265.0, 403.0, 0.485916, 318.8],
['Sr','Strontium', 38.0, 87.62, 2.0, 0.0, 0.0, 0.963, 219.0, 550.0, 0.05206, 186.0],
['Y','Yttrium', 39.0, 88.90585, 2.0, 0.0, 1.0, 1.12, 212.0, 600.0, 0.307, 153.0],
['Zr','Zirconium', 40.0, 91.224, 2.0, 0.0, 2.0, 1.32, 206.0, 640.0, 0.433, 121.0],
['Nb','Niobium', 41.0, 92.90638, 1.0, 0.0, 4.0, 1.41, 198.0, 652.0, 0.9174, 106.0],
['Mo','Molybdenum', 42.0, 95.96, 1.0, 0.0, 5.0, 1.47, 190.0, 684.0, 0.7473, 72.5],
['Tc','Technetium', 43.0, 98.0, 2.0, 0.0, 5.0, 1.51, 183.0, 702.0, 0.55, 80.4],
['Ru','Ruthenium', 44.0, 101.07, 1.0, 0.0, 7.0, 1.54, 178.0, 710.0, 1.04638, 65.0],
['Rh','Rhodium', 45.0, 102.9055, 1.0, 0.0, 8.0, 1.56, 173.0, 720.0, 1.14289, 58.0],
['Pd','Palladium', 46.0, 106.42, 0.0, 0.0, 10.0, 1.58, 169.0, 804.0, 0.56214, 32.0],
['Ag','Silver', 47.0, 107.8682, 1.0, 0.0, 10.0, 1.87, 165.0, 731.0, 1.30447, 52.5],
['Cd','Cadmium', 48.0, 112.411, 2.0, 0.0, 10.0, 1.52, 161.0, 868.0, -0.725, 46.9],
['In','Indium', 49.0, 114.818, 2.0, 1.0, 10.0, 1.656, 156.0, 558.0, 0.3, 68.7],
['Sn','Tin', 50.0, 118.71, 2.0, 2.0, 10.0, 1.824, 145.0, 709.0, 1.11207, 42.4],
['Sb','Antimony', 51.0, 121.76, 2.0, 3.0, 10.0, 1.984, 133.0, 834.0, 1.047401, 42.55],
['Te','Tellurium', 52.0, 127.6, 2.0, 4.0, 10.0, 2.158, 123.0, 869.0, 1.97087, 37.0],
['I','Iodine', 53.0, 126.90447, 2.0, 5.0, 10.0, 2.359, 115.0, 1008.0, 3.0590465, 34.6],
['Xe','Xenon', 54.0, 131.293, 2.0, 6.0, 10.0, 2.582, 108.0, 1170.0, -0.83, 27.815],
['Cs','Cesium', 55.0, 132.9054519, 1.0, 0.0, 0.0, 0.659, 298.0, 376.0, 0.47163, 401.0]]

atoi = {sym:an for (sym,an) in [(x[0],int(x[2])) for x in AtomData]}
itoa = {an:sym for (sym,an) in [(x[0],int(x[2])) for x in AtomData]}
def AtomicNumber(Symb):
	try:
		return atoi[Symb]
	except Exception as Ex:
		raise Exception("Unknown Atom")
	return 0
def AtomicSymbol(number):
	try:
		return itoa[number]
	except Exception as Ex:
		raise Exception("Unknown Atom")
	return 0


def ReadAtomCodeString():
	tmp = []
	for line in ATOMCODELINES.split('\n'):
		tmp.append(list(map(float,line.split(" "))))
	return np.array(tmp)
#ELEMENTCODES = ReadAtomCodeString()
ELEMENTCODES = np.array([[ 0.00000000,  0.00000000,  0.00000000,  0.00000000],
[-0.40375730,  1.05371916,  0.04568392, -1.13822238],
[-1.23694297,  2.11939793, -0.25570456,  0.10187750],
[-0.13026760, -1.43989585,  0.38310188, -0.95247308],
[-0.75104332, -0.10785660, -0.53962776,  0.63013525],
[-0.52373878,  0.31043193, -0.65513855,  0.49790437],
[-0.10284481,  0.83671599, -0.50380242,  0.34269946],
[-0.74897590,  1.32011216, -0.62507979,  0.56277587],
[-0.17642600,  1.35145798, -0.41895628,  0.45885406],
[ 0.44977670,  1.85452231,  0.34373733, -0.06618909],
[-1.30328069,  2.11668125, -0.55112016,  1.31079228],
[ 0.01511072, -1.45233975,  0.52147561, -0.99513821],
[-0.63567816, -0.82986551, -0.61350301,  0.62978268],
[-0.39445665, -0.35659674, -0.53610515,  0.40255610],
[ 0.21070064,  0.27234876, -0.15936595,  0.25065424],
[-0.21109020,  0.74450827, -0.34974642,  0.48508651],
[ 0.46685537,  0.97342801,  0.07172357,  0.26358350],
[ 0.91435704,  1.38054449,  0.57088761, -0.24997906],
[-1.01318710,  1.65309959, -0.65282528,  1.24902363],
[ 0.04148873, -1.66453545,  1.06891764, -0.84089898],
[-0.26224539, -1.41732804, -0.06935881,  0.46369326],
[-0.19694536, -1.33671474, -0.13151685,  0.43425145],
[-0.28994001, -1.22305523, -0.41150314,  0.57295163],
[ 0.04560683, -1.14945299, -0.26985518,  0.49537461],
[ 0.09415013, -0.98593191,  0.24079536, -1.02284055],
[-0.62094803, -0.95580846, -0.69595920,  1.10218259],
[-0.22699105, -0.88816619, -0.50788487,  0.87528223],
[ 0.20106724, -0.83701928, -0.37995366,  0.73410446],
[ 0.44170482, -0.72225285, -0.30191980,  0.52241870],
[ 0.36868053, -0.34719628,  0.17436051, -1.08821445],
[-0.46508227, -0.29603784, -0.78851223,  0.95284264],
[ 0.17881295, -0.54239783, -0.50657413,  0.93168193],
[ 0.59143771,  0.19355950, -0.34666179,  0.66260259],
[ 0.34355206,  0.63006302, -0.55529342,  0.78112856],
[ 0.71671046,  0.93931639, -0.33417173,  0.40923502],
[ 0.86002477,  1.06913135,  0.32316957,  0.02137660],
[-0.35909888,  1.20397006, -0.85038367,  1.57620248],
[ 0.15339622, -1.61507630,  1.29950731, -0.84740150],
[-0.23566970, -1.38083261,  0.13502276,  0.46141261],
[-0.09418296, -1.30760258,  0.05765451,  0.41158249],
[ 0.02749385, -1.20229050, -0.05946386,  0.44595832],
[ 0.33206215, -1.08694535,  0.42785824, -1.16029961],
[ 0.33969583, -0.81224518,  0.31309878, -1.15872680],
[ 0.21094019, -0.78711377, -0.32131427,  0.28133597],
[ 0.48983907, -0.61521347,  0.30619372, -1.20695156],
[ 0.53611579, -0.48666715,  0.31122971, -1.21428027],
[ 0.36503790, -0.09221583,  0.57123687, -1.51496318],
[ 0.55414296, -0.36537389,  0.22322466, -1.13311883],
[-0.03791524, -0.08187290, -0.73911051,  0.61015779],
[ 0.29341768, -0.19362820, -0.40275498,  0.45294985],
[ 0.62793230,  0.59489150, -0.28177015,  0.14615516],
[ 0.61970629,  0.87476446, -0.37568990,  0.22273577],
[ 0.92542217,  1.17163272, -0.02235719, -0.07609650],
[ 1.14868454,  1.35373467,  0.25709406, -0.45321420],
[-0.34942323,  1.17553673, -0.86947573,  1.19181219]],dtype=np.float64)
