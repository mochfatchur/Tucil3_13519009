## PETA Pasar Permiri Kota Lubuklinggau
numNode = 9
listKoordinatITB = [[-3.2968330050771906, 102.8615211463461],
		    [-3.296138792988724, 102.86124621994162],
		    [-3.2959419767357265, 102.86118855243879],
		    [-3.295654116172153, 102.86112417942701],
		    [-3.2956491265949515, 102.86208588598332],
		    [-3.2960266925283372, 102.86213416574216],
		    [-3.296590363398805, 102.8622843694457],
		    [-3.295659932808658, 102.86294479829793],
		    [-3.296467241446234, 102.86295851169892]
                 ]
listNodeITB = [["Jalan Garuda - Garuda Hitam"],
	       ["Jalan Garuda Hitam - Kenanga 1"],
	       ["Jalan Garuda Hitam - Garuda Merah"],
	       ["Jalan Garuda Hitam - Garuda Putih"],
	       ["Jalan Garuda Putih - Gelatik"],
	       ["Jalan Gelatik - Kenanga 1"],
	       ["Jalan Gelatik - Garuda"],
	       ["Jalan Garuda Putih - Jend. Sudirman"],
	       ["Jalan Jend. Sudirman - Garuda"],
            ]

adjacencyMatrix = [[0,1,0,0,0,0,1,0,0],
		   [1,0,1,0,0,1,0,0,0],
		   [0,1,0,1,0,0,0,0,0],
		   [0,0,1,0,1,0,0,0,0],
		   [0,0,0,1,0,1,0,1,0],
		   [0,1,0,0,1,0,1,0,0],
		   [1,0,0,0,0,1,0,0,1],
		   [0,0,0,0,1,0,0,0,1],
		   [0,0,0,0,0,0,1,1,0],
                   ]

