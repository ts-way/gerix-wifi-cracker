# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gerix.ui'
#
# Created: mer lug 14 20:02:13 2010
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
from qttable import QTable

image0_data = [
"251 49 2349 2",
"bg c #000000",
"bO c #010000",
"GY c #010100",
"vb c #020100",
"al c #020200",
"aI c #030200",
"aG c #040301",
"hi c #040402",
"cm c #050402",
"vc c #060503",
"aK c #060604",
"aH c #070604",
"i9 c #070705",
"E1 c #080403",
"tH c #080705",
"aJ c #080806",
"Cf c #090504",
"va c #090806",
"aM c #090907",
"A5 c #0a0605",
"x4 c #0a0907",
"a8 c #0b0a08",
"aN c #0b0b09",
"z# c #0c0b09",
"aL c #0c0c0a",
"iZ c #0d0908",
"c0 c #0d0c0a",
"aT c #0d0d0b",
"vm c #0e0a09",
"bo c #0e0d0b",
"am c #0e0e0c",
"iS c #0f0e0c",
"hd c #0f0f0d",
"kW c #100c0b",
"aF c #100f0d",
"Ac c #10100e",
"kZ c #110d0c",
"bn c #11100e",
"dz c #12110f",
"A1 c #121210",
"BB c #130f0e",
"bm c #131210",
"gS c #131311",
"Af c #14100f",
"bl c #141311",
"aO c #141412",
"se c #151110",
"bL c #151412",
"E4 c #151513",
"qt c #161211",
"cl c #161513",
"a# c #161614",
"y. c #171312",
"gU c #171614",
"C2 c #171715",
"h. c #181413",
"lc c #181713",
"a7 c #181715",
"aP c #181816",
"sc c #191514",
"b2 c #191816",
"an c #191917",
"j# c #191a15",
"kX c #1a1615",
"ep c #1a1917",
"a. c #1a1a18",
"k0 c #1b1716",
"fa c #1b1a18",
"zb c #1b1b19",
"DR c #1c1817",
"#9 c #1c1b19",
"j. c #1c1c1a",
"wN c #1d1918",
"cn c #1d1c1a",
"x8 c #1d1d1b",
"Ae c #1e1a19",
"i1 c #1e1d1b",
"C8 c #1f1b1a",
"iO c #1f1e1c",
"i5 c #1f1f1d",
"iW c #201c1b",
"fb c #201f1d",
"aa c #20201e",
"aD c #21201e",
"hk c #21211f",
"y# c #221e1d",
"bN c #22211f",
"lb c #222220",
"g8 c #231f1e",
"aE c #232220",
"ak c #232321",
"k2 c #24201f",
"a6 c #242321",
"ab c #242422",
"g9 c #252120",
"dy c #252422",
"Bz c #252523",
"bM c #262523",
"i4 c #262624",
"wO c #272322",
"#7 c #272624",
"#P c #272725",
"b3 c #282725",
"ac c #282826",
"gX c #292826",
"m6 c #292927",
"vj c #2a2625",
"g3 c #2a2927",
"DU c #2a2a28",
"#8 c #2b2a28",
"la c #2b2b29",
"k1 c #2c2827",
"m0 c #2c2b29",
"hj c #2c2c2a",
"qp c #2d2928",
"oJ c #2d2c2a",
"aV c #2d2d2b",
"zf c #2e2a29",
"#6 c #2e2d2b",
"aU c #2e2e2c",
"gT c #2f2e2c",
"he c #2f2f2d",
"A4 c #302c2b",
"kS c #302f2d",
"ad c #30302e",
"tO c #312d2c",
"m1 c #31302e",
"GP c #31312f",
"DS c #322e2d",
"kL c #32312f",
"qj c #333230",
"#Q c #333331",
"oQ c #34302f",
"iR c #343331",
"GZ c #343432",
"m2 c #353130",
"A# c #353432",
"FY c #353533",
"a9 c #363533",
"HY c #363634",
"Fu c #373332",
"bK c #373634",
"aC c #383735",
"BC c #393534",
"oK c #393836",
"qq c #3a3635",
"k6 c #3a3937",
"ae c #3a3a38",
"EH c #3b3734",
"Ad c #3b3736",
"g2 c #3b3a38",
"x7 c #3b3b39",
"Cg c #3c3837",
"Cb c #3c3b39",
"Cd c #3c3c3a",
"A6 c #3d3938",
"fc c #3d3c3a",
"G0 c #3d3d3b",
"DW c #3e3a39",
"oL c #3e3d3b",
"zc c #3e3e3c",
"DD c #3e433c",
"DZ c #3f3b3a",
"ja c #3f3e3a",
"#5 c #3f3e3c",
"bf c #3f3f3d",
"EY c #403c3b",
"HB c #403f3d",
"FT c #40403e",
"vn c #413d3c",
"fi c #41403e",
"vl c #423e3d",
"c1 c #42413f",
"kO c #434240",
"Hj c #434341",
"bP c #444341",
"k5 c #454442",
"DT c #464241",
"oF c #464543",
"mX c #474644",
"be c #474745",
"E7 c #484443",
"GR c #484745",
"aS c #484846",
"tP c #494846",
"C3 c #494947",
"fh c #4a4947",
"aW c #4a4a48",
"A3 c #4b4a48",
"wL c #4b4b49",
"s9 c #4bc228",
"kV c #4c4847",
"b1 c #4c4b49",
"iN c #4d4c4a",
"GO c #4d4d4b",
"GQ c #4e4d4b",
"af c #4e4e4c",
"rw c #4ec627",
"fj c #4f4e4c",
"HU c #4f4f4d",
"t. c #4fc12b",
"wH c #504f4d",
"DQ c #514d4c",
"z. c #51504e",
"By c #51514f",
"uG c #51bc32",
"Ab c #52514f",
"iV c #534f4e",
"mU c #535250",
"uH c #53ba33",
"pN c #53c12c",
"rv c #53c532",
"rx c #53c62b",
"wK c #545351",
"g4 c #555150",
"sb c #555452",
"t# c #55bb34",
"s8 c #55c636",
"Gj c #565553",
"pO c #56c22e",
"Gs c #575654",
"Hy c #575755",
"qs c #585453",
"zd c #585755",
"uI c #58b33c",
"n6 c #58b830",
"EI c #595552",
"a5 c #595856",
"EV c #595957",
"uF c #59be3c",
"ry c #59bf35",
"b. c #5a5957",
"n7 c #5abb30",
"pM c #5ac038",
"Fx c #5b5756",
"bk c #5b5a58",
"s6 c #5bac46",
"s7 c #5bbf41",
"ru c #5bc040",
"FP c #5c5857",
"qk c #5c5b59",
"HD c #5c5c5a",
"rt c #5cad47",
"ta c #5cae40",
"n8 c #5cb535",
"pP c #5cbc36",
"eq c #5d5c5a",
"#R c #5d5d5b",
"uD c #5da34a",
"rz c #5db23d",
"C7 c #5e5a59",
"dA c #5e5d5b",
"bh c #5e5e5c",
"pK c #5ea549",
"wc c #5eb445",
"uE c #5eb846",
"gW c #5f5e5c",
"uJ c #5fa948",
"wb c #5fb047",
"wd c #5fb246",
"pL c #5fba43",
"C5 c #605c5b",
"x5 c #605f5d",
"hl c #60605e",
"n3 c #609e4b",
"we c #60ac4a",
"pQ c #60b03d",
"FH c #615d5c",
"oM c #61605e",
"GX c #61615f",
"tL c #625e5d",
"r9 c #62615f",
"w# c #629c52",
"n9 c #62ab3f",
"n5 c #62bc40",
"FJ c #635f5e",
"vd c #636260",
"hh c #636361",
"wa c #63aa4c",
"FD c #64605f",
"wG c #646361",
"oN c #646462",
"mk c #64b23b",
"mi c #64b53d",
"mj c #64b63a",
"FK c #656160",
"mV c #656462",
"hf c #656563",
"HO c #662939",
"FA c #666261",
"kR c #666563",
"DV c #666664",
"wf c #66a353",
"ml c #66a942",
"n4 c #66b54c",
"x9 c #676362",
"g0 c #676664",
"FV c #676765",
"fg c #686765",
"mf c #689b56",
"mh c #68b448",
"tF c #696866",
"f# c #696967",
"vs c #6a192c",
"aB c #6a6967",
"Gn c #6b6a68",
"qu c #6b6b69",
"CQ c #6b726a",
"g7 c #6c6867",
"#4 c #6c6b69",
"Gv c #6c6c6a",
"mR c #6d6c6a",
"#I c #6d6d6b",
"Fq c #6e6a69",
"C4 c #6e6d6b",
"bd c #6e6e6c",
"ze c #6f6b6a",
"b4 c #6f6e6c",
"Hl c #6f6f6d",
"kb c #6fa655",
"mg c #6fb056",
"Ft c #706c6b",
"Hi c #706f6d",
"Gf c #70706e",
"HH c #713243",
"nu c #713b49",
"qn c #71706e",
"kf c #71a455",
"ke c #71ac52",
"Hu c #722d3f",
"FC c #726e6d",
"mS c #72716f",
"aj c #727270",
"mY c #737270",
"Gp c #737371",
"su c #742038",
"jD c #744651",
"FO c #74706f",
"kP c #747371",
"k# c #749b66",
"kd c #74b154",
"HP c #753546",
"FN c #757170",
"iT c #757472",
"HE c #757573",
"#G c #767573",
"#H c #767674",
"kc c #76b258",
"oO c #777372",
"b# c #777674",
"bX c #777775",
"k8 c #787473",
"Hh c #787775",
"bb c #787876",
"yl c #792a40",
"Hv c #792e42",
"lG c #794551",
"HN c #794753",
"DJ c #797574",
"#F c #797876",
"bc c #797977",
"ka c #79a864",
"wT c #7a2238",
"ff c #7a7977",
"GU c #7a7a78",
"qC c #7b1f34",
"vE c #7b213b",
"vS c #7b293f",
"jR c #7b2c3f",
"lF c #7b3b4b",
"wJ c #7b7a78",
"wM c #7b7b79",
"BR c #7c2538",
"vC c #7c2b3c",
"nt c #7c3c4c",
"DN c #7c7877",
"#E c #7c7b79",
"HT c #7c7c7a",
"Cv c #7d2438",
"w4 c #7d2740",
"Dk c #7d283b",
"np c #7d2940",
"ls c #7d2a3c",
"na c #7d313e",
"hc c #7d7c7a",
"GL c #7e2a41",
"HI c #7e3347",
"E0 c #7e7a79",
"ba c #7e7d7b",
"G6 c #7f233c",
"qQ c #7f273f",
"F4 c #7f2e41",
"ng c #7f3647",
"jj c #7f424a",
"vk c #7f7b7a",
"tI c #7f7e7c",
"#J c #7f7f7d",
"Gc c #802840",
"GJ c #803146",
"t6 c #803147",
"ns c #803549",
"Fs c #807c7b",
"k3 c #807f7d",
"Hz c #80807e",
"sl c #812d44",
"Ga c #812f45",
"qE c #813043",
"ln c #813746",
"HG c #81515d",
"Ag c #817d7c",
"AY c #81807e",
"yj c #823444",
"tT c #82374b",
"Ho c #82394c",
"nh c #823a48",
"E3 c #828280",
"GA c #833245",
"G4 c #833449",
"nc c #833646",
"zu c #83384d",
"HJ c #834051",
"iY c #837f7e",
"EA c #83827e",
"E2 c #838280",
"FR c #838381",
"lU c #842038",
"Bi c #842c42",
"B. c #843143",
"D5 c #843749",
"jK c #844651",
"nv c #845963",
"zg c #84807f",
"i8 c #848381",
"lu c #852a3b",
"t3 c #853043",
"zs c #853244",
"vL c #85364b",
"Db c #853747",
"D3 c #854150",
"EL c #858180",
"r4 c #858482",
"lD c #862e44",
"BH c #862f42",
"Hq c #86344a",
"Aj c #863848",
"Ei c #868281",
"GT c #868583",
"pR c #86c06c",
"tb c #86c073",
"rA c #86c16d",
"sj c #87233b",
"uj c #87233f",
"yd c #872b42",
"Fj c #872e44",
"EB c #878682",
"oH c #878684",
"E5 c #878785",
"qa c #87b9de",
"nH c #881c36",
"E# c #882941",
"jL c #882f41",
"Cn c #883545",
"lr c #883549",
"Ha c #883d51",
"jC c #88505d",
"fk c #888785",
"FW c #888886",
"qb c #88badd",
"o. c #88bf6c",
"Fb c #892a42",
"Cl c #892d42",
"lt c #893646",
"nr c #89374d",
"w2 c #893b4b",
"FG c #898584",
"co c #898886",
"u5 c #89b6d5",
"rY c #89bbe0",
"vR c #8a213f",
"qD c #8a293d",
"lC c #8a2c44",
"nj c #8a3846",
"Bg c #8a394a",
"lm c #8a3c49",
"lE c #8a3d4f",
"ni c #8a424e",
"cZ c #8a8987",
"FS c #8a8a88",
"mJ c #8ab8dc",
"rZ c #8abcdf",
"lB c #8b2d45",
"oW c #8b3244",
"zt c #8b334b",
"BJ c #8b3445",
"nb c #8b3746",
"oX c #8b3c4f",
"I# c #8b5965",
"bQ c #8b8a88",
"#K c #8b8b89",
"uK c #8bbe79",
"mm c #8bc070",
"D# c #8c2f44",
"Ar c #8c344a",
"BD c #8c8887",
"HZ c #8c8b89",
"H1 c #8c8c8a",
"p8 c #8cacc1",
"rU c #8cafc5",
"u4 c #8cb7d7",
"n2 c #8cb97e",
"u6 c #8cb9d6",
"oy c #8cbce2",
"GC c #8d2e46",
"yk c #8d354d",
"Aq c #8d3649",
"nq c #8d3950",
"Fi c #8d3c4f",
"kQ c #8d8c8a",
"Ig c #8d8d8b",
"u1 c #8db0c4",
"q# c #8dbbdf",
"rX c #8dbde1",
"pJ c #8dc27e",
"s5 c #8dc77d",
"pp c #8e1b3a",
"sL c #8e1d3b",
"vM c #8e2641",
"B# c #8e3144",
"Gb c #8e324b",
"lA c #8e364c",
"GK c #8e364e",
"lN c #8e3d4c",
"Fc c #8e4556",
"nf c #8e4558",
"jk c #8e525c",
"Gx c #8e8d8b",
"ES c #8e8e8c",
"rV c #8eb6d0",
"mI c #8eb9db",
"r0 c #8ebad3",
"mK c #8ebcde",
"rs c #8ec87e",
"BQ c #8f3044",
"Ea c #8f3149",
"Bh c #8f3348",
"Hb c #8f3b52",
"D. c #8f565f",
"oG c #8f8e8c",
"p9 c #8fb3cd",
"u2 c #8fb4ce",
"oB c #8fb7d0",
"tA c #8fb9d1",
"oz c #8fbfe3",
"ty c #8fc0e0",
"uC c #8fc381",
"ss c #902843",
"Ct c #903145",
"D4 c #903147",
"Fa c #903149",
"Hc c #904357",
"Ap c #904856",
"l# c #908f8d",
"tu c #90b4ca",
"qd c #90bad3",
"wg c #90bb83",
"mL c #90bcd9",
"tz c #90bdda",
"oA c #90bddc",
"qc c #90bfdd",
"xA c #90ca7d",
"q9 c #911a3a",
"jQ c #912b43",
"Al c #912d45",
"FZ c #91908e",
"kD c #91b6d1",
"mM c #91b7ce",
"wV c #922743",
"Di c #923047",
"jo c #924b5d",
"Fp c #928e8d",
"tJ c #92918f",
"A2 c #929290",
"wA c #92b7d2",
"u8 c #92b8cb",
"tv c #92bad4",
"u3 c #92bbd9",
"q. c #92bddd",
"ox c #92bee1",
"tx c #92c0e2",
"tU c #932842",
"BI c #932d45",
"zl c #93344a",
"no c #93354d",
"jA c #93485c",
"pd c #936973",
"r5 c #939290",
"ao c #939391",
"me c #93b885",
"wz c #93b8d3",
"rW c #93c0e1",
"xy c #93c181",
"lO c #94223b",
"zm c #942c45",
"nA c #943549",
"tW c #944057",
"E. c #944558",
"Eb c #944a5b",
"H5 c #946470",
"En c #948e8e",
"DG c #94918a",
"r7 c #949391",
"Eg c #949693",
"kC c #94b6d1",
"kg c #94be7f",
"u7 c #94bed7",
"xB c #94ce82",
"yf c #952e49",
"uc c #95314b",
"Ak c #95334a",
"lz c #95364e",
"Hp c #953b54",
"EG c #959492",
"ww c #95b4c6",
"mG c #95b5ca",
"kE c #95bad5",
"wU c #962845",
"ye c #962946",
"Cu c #963046",
"F5 c #96324c",
"t4 c #96344d",
"t5 c #963651",
"o9 c #963a53",
"zk c #964d5e",
"o3 c #965a64",
"jl c #965a66",
"wr c #967296",
"Fy c #969291",
"gY c #969593",
"H0 c #969694",
"mF c #96b0bf",
"ou c #96b3c5",
"kG c #96b7ca",
"ov c #96b8d1",
"w. c #96c18b",
"tw c #96c3e2",
"Cm c #973147",
"Dj c #97334b",
"G5 c #973450",
"w3 c #973d56",
"jx c #974e5f",
"jp c #975060",
"As c #975062",
"o1 c #975a69",
"Hn c #975f6c",
"sd c #979392",
"Dt c #979598",
"r3 c #979694",
"fo c #979795",
"wx c #97b7cc",
"kF c #97bbd3",
"wB c #97bcd6",
"xC c #97cc88",
"nn c #982743",
"nk c #983247",
"Da c #98354a",
"zn c #983a52",
"jr c #984c59",
"ll c #98505c",
"Em c #989292",
"DY c #989493",
"#D c #989795",
"EQ c #989896",
"IH c #989898",
"fI c #989a97",
"wD c #98b9c8",
"mH c #98bdda",
"vN c #99193c",
"ly c #992643",
"vu c #992c49",
"F6 c #995063",
"jq c #99515f",
"jB c #995667",
"H6 c #995f6d",
"fy c #999594",
"r6 c #999896",
"EP c #999997",
"wC c #99bed1",
"xx c #99bf8c",
"xD c #99c68d",
"xz c #99ce86",
"nB c #9a1937",
"nl c #9a2841",
"qO c #9a2c47",
"o8 c #9a2c49",
"jw c #9a4d5f",
"zr c #9a5864",
"EW c #9a9695",
"r8 c #9a9997",
"If c #9a9a98",
"wy c #9abed8",
"ow c #9ac1e0",
"GB c #9b3751",
"jz c #9b495f",
"Hw c #9b5668",
"pc c #9b6774",
"H4 c #9b787f",
"CW c #9b9798",
"gV c #9b9a98",
"kA c #9bb5c4",
"vQ c #9c1f41",
"lv c #9c2f46",
"pi c #9c314b",
"Am c #9c475a",
"pb c #9c6271",
"bJ c #9c9b99",
"kB c #9cbad2",
"o7 c #9d2a47",
"Dh c #9d5060",
"wl c #9d709b",
"uV c #9d729f",
"km c #9d7da4",
"Ev c #9d9996",
"vg c #9d9c9a",
"DM c #9d9d9b",
"Ef c #9d9f9e",
"kz c #9db1bc",
"k. c #9db991",
"lT c #9e1c3e",
"qP c #9e334f",
"jy c #9e4c62",
"pa c #9e5e6e",
"G3 c #9e6170",
"Ia c #9e6a77",
"ms c #9e74a4",
"EM c #9e9a99",
"qm c #9e9d9b",
"fB c #9e9e9c",
"m7 c #9e9f9a",
"lx c #9f2441",
"nm c #9f2844",
"lw c #9f2943",
"o6 c #9f334b",
"sk c #9f3951",
"vD c #9f415b",
"vv c #9f4d63",
"I. c #9f757f",
"Bx c #9f9e9c",
"#L c #9f9f9d",
"ui c #a01f45",
"js c #a04858",
"oe c #a06ea3",
"tm c #a070a2",
"kK c #a09f9d",
"IM c #a0a09e",
"sE c #a1304e",
"vt c #a13451",
"Ba c #a15464",
"E8 c #a19d9c",
"aA c #a1a09e",
"bY c #a1a19f",
"pj c #a21538",
"ud c #a22042",
"jM c #a22d48",
"q2 c #a22f4c",
"p# c #a25b6d",
"ok c #a270a3",
"rL c #a270a5",
"ks c #a27ea4",
"tK c #a2a19f",
"Hm c #a2a2a0",
"DC c #a2a89e",
"jv c #a3475c",
"p. c #a35469",
"my c #a373a3",
"kr c #a373a5",
"s# c #a3a2a0",
"bW c #a3a3a1",
"lq c #a45268",
"lo c #a45b6c",
"p2 c #a472a7",
"HV c #a4a3a1",
"CF c #a4a4a6",
"xX c #a4c3d8",
"jP c #a52846",
"tV c #a53a54",
"st c #a5415d",
"H# c #a56877",
"Gz c #a56975",
"pW c #a56ba5",
"wn c #a56ea5",
"wq c #a577a5",
"x3 c #a5a4a2",
"fD c #a5a5a3",
"HQ c #a66c7b",
"wm c #a674a5",
"fx c #a6a2a1",
"#3 c #a6a5a3",
"gR c #a6a6a4",
"nG c #a71b40",
"vP c #a71c43",
"xf c #a76e7d",
"ji c #a76f78",
"Ej c #a7a3a2",
"HC c #a7a6a4",
"fn c #a7a7a5",
"BK c #a86471",
"yi c #a86c76",
"uP c #a872a6",
"GW c #a8a7a5",
"za c #a8a8a6",
"vO c #a91e45",
"vF c #a96177",
"o0 c #a96b7a",
"GI c #a96c7b",
"rF c #a96ca7",
"o2 c #a96f7b",
"ko c #a976b1",
"kT c #a9a8a6",
"Gt c #a9a9a7",
"jO c #aa2445",
"si c #aa6577",
"jE c #aa8990",
"wI c #aaa9a7",
"fG c #aaaaa8",
"o5 c #ab4e61",
"GD c #ab6678",
"Bj c #ab6879",
"pe c #ab8a91",
"Ey c #aba7a6",
"bp c #abaaa8",
"Gw c #ababa9",
"xU c #abc5d6",
"xY c #abcade",
"sK c #ac1b44",
"mx c #ac6eaf",
"tg c #ac6fa8",
"kn c #ac82b4",
"mZ c #acaba9",
"aQ c #acacaa",
"fH c #acaeab",
"q3 c #ad173d",
"sF c #ad1b42",
"jN c #ad2a4a",
"jt c #ad4e62",
"tN c #ada9a8",
"HW c #adacaa",
"ju c #ae4d61",
"FI c #aeaaa9",
"fr c #aeadab",
"qo c #aeaeac",
"r1 c #aed3e5",
"po c #af1d44",
"wo c #af78af",
"uU c #af78b1",
"H7 c #af7b87",
"FL c #afabaa",
"bR c #afaeac",
"xT c #afc7d3",
"qe c #afd2e5",
"tB c #afd3e3",
"q8 c #b01944",
"lP c #b01a3f",
"o4 c #b06874",
"Co c #b0727d",
"kp c #b078b7",
"mt c #b07ab8",
"b0 c #b0afad",
"fC c #b0b0ae",
"xV c #b0cce1",
"xW c #b0cfe4",
"oC c #b0d1e2",
"Cs c #b16977",
"oj c #b170b4",
"fw c #b1adac",
"kM c #b1b0ae",
"Hg c #b1b1af",
"mN c #b1d1e0",
"nd c #b2697a",
"Fk c #b26e7d",
"mu c #b26eb9",
"uR c #b270b0",
"kq c #b27bb5",
"mz c #b293b3",
"fs c #b2aead",
"EE c #b2aeaf",
"vh c #b2b1af",
"Gu c #b2b2b0",
"xE c #b2d2a9",
"u9 c #b2d2df",
"wp c #b37eb2",
"m5 c #b3afae",
"c2 c #b3b2b0",
"HA c #b3b3b1",
"xZ c #b3d0de",
"xe c #b46b7f",
"x# c #b46f81",
"rK c #b473b7",
"tl c #b476b5",
"x. c #b4828d",
"xJ c #b497b5",
"kt c #b49ab3",
"FE c #b4b0af",
"fe c #b4b3b1",
"C1 c #b4b4b2",
"CP c #b4bcb1",
"p1 c #b572b7",
"of c #b577ba",
"uQ c #b578b3",
"Dc c #b57d86",
"ol c #b593b6",
"ws c #b59bb6",
"Es c #b5b1b2",
"Gm c #b5b4b2",
"#i c #b5b5b3",
"x0 c #b5d0d9",
"lS c #b61740",
"i6 c #b6b5b3",
"#h c #b6b6b4",
"kH c #b6d0dd",
"wE c #b6d3db",
"w1 c #b77e87",
"Ex c #b7b3b2",
"cr c #b7b6b4",
"Fn c #b7b7b5",
"uh c #b81d49",
"og c #b86fbe",
"oY c #b87183",
"uS c #b875b8",
"Ck c #b8858c",
"xP c #b89bb7",
"Fv c #b8b4b3",
"EF c #b8b6b7",
"ld c #b8b7b3",
"H2 c #b8b7b5",
"xw c #b8d4ae",
"wW c #b96c80",
"mv c #b970bf",
"p3 c #b995bb",
"h# c #b9b5b4",
"Er c #b9b5b6",
"i2 c #b9b8b6",
"#M c #b9b9b7",
"lR c #ba0f3b",
"xd c #ba6079",
"ti c #ba6eb8",
"mw c #ba73bf",
"pX c #ba77bc",
"uT c #ba7cbb",
"rM c #ba96bc",
"tn c #ba98bb",
"uW c #ba9bbb",
"qh c #bab9b7",
"rI c #bb69bb",
"rH c #bb6cbb",
"tj c #bb6fba",
"rJ c #bb71be",
"jn c #bb7688",
"yc c #bb7987",
"F3 c #bb818d",
"lH c #bb939c",
"EJ c #bbb7b4",
"fl c #bbbab8",
"ue c #bc1f4a",
"qN c #bc596e",
"xa c #bc647c",
"pZ c #bc6dc0",
"pY c #bc6fbf",
"Eo c #bcb8b7",
"ql c #bcbbb9",
"fq c #bcbcba",
"lQ c #bd143d",
"oh c #bd70c2",
"oi c #bd73c2",
"tk c #bd75be",
"m3 c #bdb9b8",
"Ca c #bdbcba",
"fp c #bdbdbb",
"nC c #be1943",
"rG c #be77bd",
"th c #be79ba",
"vB c #be828c",
"i3 c #bebdbb",
"eo c #bebebc",
"Ee c #bec0bd",
"xb c #bf5f7a",
"p0 c #bf72c0",
"G# c #bf8291",
"k4 c #bfbebc",
"Cc c #bfbfbd",
"qi c #c0bfbd",
"HX c #c0c0be",
"nF c #c11643",
"CX c #c1bfc0",
"Gy c #c1c0be",
"fE c #c1c1bf",
"FQ c #c2bebd",
"Aa c #c2c1bf",
"fm c #c2c2c0",
"kl c #c3afca",
"EX c #c3bfbe",
"s. c #c3c2c0",
"Hk c #c3c3c1",
"xc c #c4647f",
"xL c #c49ec5",
"qr c #c4c0bf",
"a4 c #c4c3c1",
"ii c #c4e3b7",
"if c #c4e5ba",
"sJ c #c51748",
"ug c #c51b4c",
"BS c #c58593",
"BP c #c58691",
"xO c #c5a3c4",
"mr c #c5aacb",
"Gg c #c5c4c2",
"ER c #c5c5c3",
"ie c #c5e3bd",
"nE c #c60c3e",
"G7 c #c68897",
"xK c #c6a4c7",
"jb c #c6c2c1",
"EC c #c6c2c3",
"E6 c #c6c5c3",
"u0 c #c6e6f5",
"ih c #c6e7b8",
"q4 c #c70f41",
"yg c #c78092",
"Ib c #c799a4",
"xN c #c7a1c8",
"DH c #c7c2bc",
"Eq c #c7c3c2",
"DK c #c7c3c4",
"oI c #c7c6c4",
"ag c #c7c7c5",
"rT c #c7e7f6",
"nD c #c81141",
"sG c #c81648",
"pk c #c81847",
"DX c #c8c4c3",
"#C c #c8c7c5",
"Id c #c8c8c6",
"p7 c #c8e4f2",
"q7 c #c91346",
"pn c #c91747",
"Et c #c9c5c4",
"GS c #c9c8c6",
"EU c #c9c9c7",
"ig c #c9edbd",
"uf c #ca204f",
"fd c #cac9c7",
"x6 c #cacac8",
"tt c #caebfa",
"od c #cba7cd",
"FM c #cbc7c6",
"bS c #cbcac8",
"Ce c #cbcbc9",
"ij c #cbe7c1",
"q6 c #cc053e",
"pm c #cc0a3f",
"qF c #cc8799",
"l9 c #cc9a5d",
"v0 c #cc9e63",
"wk c #cca6cb",
"C0 c #cccbc9",
"FU c #ccccca",
"CG c #cccccc",
"xM c #cda7ce",
"nw c #cdaeb4",
"fv c #cdc9c8",
"EO c #cdcdcb",
"x1 c #cde2e7",
"id c #cde6c6",
"sI c #ce0f45",
"Fr c #cecac9",
"iM c #cecdcb",
"fF c #cececc",
"wv c #ceeaf6",
"xQ c #cfbacd",
"EN c #cfcbcc",
"gZ c #cfcecc",
"Go c #cfcfcd",
"q5 c #d00940",
"pV c #d0a2d0",
"HF c #d0b1b7",
"cp c #d0cfcd",
"#O c #d0d0ce",
"pl c #d10f43",
"oP c #d1cdcc",
"F0 c #d1d0ce",
"Ie c #d1d1cf",
"B4 c #d1d8d0",
"mE c #d1e5ee",
"ot c #d1e9f5",
"qB c #d292a2",
"Gi c #d2d1cf",
"iF c #d2e9f7",
"iH c #d2eaf6",
"sH c #d31448",
"Hr c #d39fab",
"rE c #d39fcf",
"j3 c #d3ad7c",
"vZ c #d3ae81",
"dB c #d3d2d0",
"hm c #d3d3d1",
"iG c #d3eaf8",
"v5 c #d4a86b",
"g6 c #d4d0cf",
"iQ c #d4d3d1",
"ky c #d4e5ec",
"pS c #d4fbc4",
"rB c #d4fbc6",
"uO c #d5a6d2",
"Ep c #d5d1d0",
"kN c #d5d4d2",
"#S c #d5d5d3",
"iE c #d5ebf8",
"xS c #d5ecf4",
"l8 c #d6984f",
"ur c #d69b57",
"tf c #d6a0d1",
"Bf c #d6a1a9",
"er c #d6d5d3",
"f. c #d6d6d4",
"iC c #d6e7ee",
"o# c #d6fdc4",
"v4 c #d7a463",
"m. c #d7b381",
"EZ c #d7d3d2",
"Gh c #d7d6d4",
"#j c #d7d7d5",
"iB c #d7e4ea",
"iI c #d7edf8",
"tc c #d7fcc9",
"Gd c #d893a5",
"l4 c #d89747",
"mT c #d8d7d5",
"FX c #d8d8d6",
"iD c #d8ecf7",
"yQ c #d8f9ce",
"mn c #d8ffc6",
"j2 c #d9ab70",
"HM c #d9bac0",
"Gk c #d9d8d6",
"sa c #d9d9d7",
"ik c #d9f0d3",
"zo c #da9cab",
"uw c #daa15a",
"v2 c #daa15c",
"v1 c #daa563",
"Fw c #dad6d5",
"vf c #dad9d7",
"Io c #dadada",
"yP c #dafbce",
"wS c #db9ead",
"uq c #dbae77",
"H3 c #dbc5c8",
"Ew c #dbd7d6",
"cq c #dbdad8",
"#g c #dbdbd9",
"xv c #dbefd6",
"s4 c #dbffd2",
"sU c #dc9a4e",
"ve c #dcdbd9",
"CH c #dcdcda",
"Ip c #dcdcdc",
"y3 c #dceffe",
"uL c #dcfdd2",
"sm c #dd9dae",
"rg c #dda665",
"D6 c #dda8b2",
"sT c #ddaa6b",
"jX c #ddb582",
"xp c #ddbb8b",
"j4 c #ddc19a",
"#2 c #dddcda",
"ic c #ddf1d8",
"kh c #ddfdce",
"rr c #ddffd2",
"sY c #de9c4e",
"Fh c #dea2ae",
"jY c #deab6c",
"xq c #dec394",
"H9 c #dec3c8",
"Gl c #dedddb",
"ai c #dededc",
"Ij c #dedede",
"CR c #dee3dd",
"y8 c #def1f7",
"xF c #def5d9",
"nW c #dfa661",
"pw c #dfa865",
"v6 c #dfba83",
"xk c #dfc5a2",
"iu c #dfc7df",
"g1 c #dfdedc",
"ET c #dfdfdd",
"n1 c #dffbd3",
"pI c #dfffd3",
"uv c #e0a154",
"nQ c #e0ab69",
"l3 c #e0af6d",
"DP c #e0dcdb",
"mW c #e0dfdd",
"iJ c #e0f3fa",
"md c #e0f8d6",
"wh c #e0fbd8",
"uB c #e0ffd7",
"v3 c #e1ab65",
"hN c #e1abb8",
"HK c #e1b7c1",
"xr c #e1cba2",
"fz c #e1dddc",
"tG c #e1e0de",
"BA c #e1e1df",
"Ds c #e1e1e1",
"pC c #e2a258",
"xI c #e2c8e3",
"iv c #e2cfe2",
"A7 c #e2dedd",
"iP c #e2e1df",
"GV c #e2e2e0",
"In c #e2e2e2",
"y7 c #e2f6ff",
"oD c #e2fdff",
"tC c #e2feff",
"sX c #e39b46",
"t2 c #e3a4af",
"ID c #e3bec6",
"w9 c #e3c4c9",
"tM c #e3dfde",
"k7 c #e3e2e0",
"aR c #e3e3e1",
"Ik c #e3e3e3",
"B3 c #e3eae2",
"y4 c #e3f8ff",
"y5 c #e3faff",
"uZ c #e3fbff",
"v. c #e3feff",
"qf c #e3ffff",
"Cw c #e4a6b3",
"xl c #e4c396",
"it c #e4cae7",
"pf c #e4ced1",
"CU c #e4e1da",
"bT c #e4e3e1",
"bV c #e4e4e2",
"iA c #e4eff1",
"yM c #e4fdd6",
"yN c #e4ffd5",
"px c #e59e4c",
"nR c #e5a150",
"xo c #e5c08b",
"IC c #e5c6cc",
"Do c #e5dcdf",
"FF c #e5e1e0",
"Du c #e5e3e4",
"#B c #e5e4e2",
"bi c #e5e5e3",
"fJ c #e5e7e4",
"yR c #e5fce0",
"mO c #e5fcff",
"yO c #e5ffd7",
"pB c #e69b48",
"qR c #e69eb2",
"nV c #e6a153",
"GM c #e6a6b6",
"j0 c #e6aa62",
"hS c #e6acb8",
"Ao c #e6bcc0",
"hM c #e6bcc6",
"xn c #e6be8a",
"xm c #e6c18d",
"IE c #e6c1c9",
"jJ c #e6c2c6",
"iq c #e6cdea",
"hH c #e6d1d6",
"Fz c #e6e2e1",
"vi c #e6e5e3",
"Fo c #e6e6e4",
"j9 c #e6fade",
"rS c #e6feff",
"vK c #e7b3bf",
"k9 c #e7e3e2",
"b5 c #e7e6e4",
"Gq c #e7e7e5",
"Iq c #e7e7e7",
"Eh c #e7e9e8",
"gt c #e7f8e5",
"yL c #e7fadc",
"p6 c #e7fbff",
"rl c #e8a556",
"BG c #e8b7bd",
"Ix c #e8c9cf",
"is c #e8cdec",
"#c c #e8e7e5",
"hg c #e8e8e6",
"Il c #e8e8e8",
"y9 c #e8f8f8",
"gp c #e8fbe5",
"rh c #e9a252",
"hO c #e9a9b9",
"pD c #e9b675",
"ux c #e9b977",
"ir c #e9ceed",
"ip c #e9d2ec",
"EK c #e9e5e4",
"i0 c #e9e8e6",
"es c #e9e9e7",
"Ii c #e9e9e9",
"z8 c #e9f6ff",
"gu c #e9f7e6",
"z9 c #e9f7ff",
"il c #e9fbe5",
"kI c #e9fcff",
"gq c #e9fde4",
"tD c #e9fdff",
"wF c #e9feff",
"v9 c #e9ffe3",
"pz c #ea9636",
"us c #eaa759",
"oZ c #eaa7b8",
"j1 c #eab16e",
"Fd c #eab7c0",
"Iw c #ead4d7",
"h7 c #ead7b9",
"hb c #eae6e5",
"mQ c #eae9e7",
"bZ c #eaeae8",
"B5 c #eaeaea",
"Bv c #eaebed",
"iK c #eaf9fe",
"go c #eafbe8",
"v# c #eafdff",
"s3 c #eafee5",
"r2 c #eafeff",
"ts c #eaffff",
"l6 c #eb9e44",
"l5 c #eb9f49",
"w5 c #ebacbf",
"jZ c #ebb06a",
"nX c #ebbe83",
"ho c #ebcbd0",
"hG c #ebd0d5",
"El c #ebe5e5",
"kU c #ebe7e6",
"ck c #ebeae8",
"A0 c #ebebe9",
"x2 c #ebfafd",
"gs c #ebfee8",
"mo c #ebffe0",
"oa c #ebffe1",
"pT c #ebffe3",
"rq c #ebffe4",
"y6 c #ebffff",
"ne c #eca3b6",
"D9 c #ecb2be",
"oV c #ecb2c0",
"sZ c #ecb36c",
"Ht c #ecc9cf",
"iw c #ecdeeb",
"iU c #ecebe9",
"#N c #ececea",
"Dp c #ececec",
"mD c #ecfbff",
"qg c #ecfdff",
"rC c #ecfee4",
"ki c #ecffe4",
"l7 c #eda34e",
"ut c #eda654",
"An c #edb5c2",
"hT c #edbbc6",
"lM c #edbec4",
"Iy c #edc8d0",
"h2 c #edd5b3",
"hI c #eddee1",
"Eu c #ede9e6",
"kY c #ede9e8",
"cY c #edecea",
"#e c #ededeb",
"BX c #ededed",
"qx c #edefee",
"Bp c #edf3f1",
"uA c #edffe9",
"os c #edffff",
"hR c #eeaab9",
"jm c #eeaebe",
"ym c #eeb8c8",
"Iz c #eecdd4",
"C9 c #eee4e2",
"C6 c #eeeae9",
"cj c #eeedeb",
"gQ c #eeeeec",
"CE c #eeeef0",
"tQ c #eef0ed",
"z7 c #eefbff",
"gJ c #eefdff",
"pH c #eeffe6",
"rj c #ef9b3b",
"sV c #efa34d",
"xg c #efc7d0",
"hq c #efcfd4",
"h6 c #efd8b8",
"g5 c #efebea",
"Ez c #efeeea",
"AZ c #efeeec",
"aX c #efefed",
"C# c #efefef",
"Bw c #eff2f7",
"zP c #eff6e4",
"IP c #effaf4",
"kx c #effafe",
"gv c #effbef",
"rR c #effcff",
"gn c #effdec",
"gI c #effdff",
"ib c #effeeb",
"gL c #effeff",
"td c #efffe9",
"gr c #efffec",
"pA c #f09d41",
"py c #f09f44",
"uu c #f0ac59",
"rm c #f0b770",
"F# c #f0bbc5",
"hu c #f0cdd3",
"l. c #f0eceb",
"c3 c #f0efed",
"#d c #f0f0ee",
"Im c #f0f0f0",
"B8 c #f0f1eb",
"et c #f0f2ef",
"AI c #f0f5ee",
"BE c #f0f5ef",
"zw c #f0f6f2",
"tR c #f0f6f4",
"Dm c #f0f6f6",
"mC c #f0f8fb",
"AG c #f0f9f4",
"Bo c #f0f9f6",
"z6 c #f0fbff",
"y1 c #f0fcfc",
"yK c #f0fee7",
"yS c #f0ffec",
"y2 c #f0ffff",
"vT c #f1b7c5",
"zq c #f1ced2",
"h3 c #f1d5b0",
"vY c #f1d7b4",
"h1 c #f1dcc1",
"xR c #f1e4ee",
"i7 c #f1edec",
"B1 c #f1eff2",
"#A c #f1f0ee",
"Gr c #f1f1ef",
"CL c #f1f1f1",
"Bu c #f1f2ec",
"or c #f1faff",
"gG c #f1fbfc",
"kJ c #f1fbfd",
"xu c #f1fdef",
"j8 c #f1feea",
"n0 c #f1ffe7",
"mc c #f1ffe8",
"gK c #f1ffff",
"wt c #f2e1f3",
"h8 c #f2e2c9",
"Iv c #f2e6e8",
"kk c #f2eaf5",
"AM c #f2edf1",
"FB c #f2eeed",
"bU c #f2f1ef",
"ah c #f2f2f0",
"qw c #f2f3ee",
"Dz c #f2f4f1",
"BY c #f2f6f5",
"AF c #f2f8ee",
"iL c #f2fcfe",
"ea c #f2fded",
"cD c #f2fdf7",
"cE c #f2fdf9",
"p5 c #f2fdff",
"cF c #f2fefa",
"de c #f2fefc",
"zR c #f2ffeb",
"uM c #f2ffec",
"zS c #f2ffee",
"hP c #f3acbc",
"ub c #f3b0c1",
"jS c #f3bbc6",
"hp c #f3d3d8",
"IF c #f3d4da",
"io c #f3e1f7",
"iX c #f3efee",
"Is c #f3f1f2",
"B6 c #f3f1f4",
"c4 c #f3f2f0",
"sf c #f3f3f1",
"Ih c #f3f3f3",
"CM c #f3f4ef",
"BV c #f3f5f2",
"CI c #f3f5f4",
"CN c #f3f6ef",
"vp c #f3f8f2",
"IO c #f3f8f4",
"Cy c #f3f9f9",
"AT c #f3faff",
"AU c #f3fbfd",
"db c #f3fcf7",
"lY c #f3fcfb",
"AR c #f3fcff",
"cG c #f3fdfc",
"e6 c #f3fdfe",
"eb c #f3feee",
"cC c #f3fef8",
"e7 c #f3feff",
"im c #f3ffef",
"dd c #f3fff9",
".4 c #f3fffd",
"tE c #f3ffff",
"ri c #f4a348",
"sW c #f4a549",
"tX c #f4b7c7",
"nz c #f4bbc4",
"hA c #f4cfd6",
"yo c #f4dbde",
"yX c #f4dcf4",
"om c #f4e3f6",
"fu c #f4f0ef",
"zI c #f4f3e1",
"#1 c #f4f3f1",
".R c #f4f4f2",
"It c #f4f4f4",
"CD c #f4f4f6",
"Bl c #f4f5f0",
"wP c #f4f6f3",
"cs c #f4f6f5",
"qz c #f4f8f7",
"Cx c #f4f8f9",
"zU c #f4f9f3",
"zh c #f4f9f5",
"w8 c #f4faf6",
"dV c #f4faf8",
"zx c #f4fbf4",
"CO c #f4fcf1",
"iz c #f4fcfe",
"cB c #f4fdf8",
"nL c #f4fdfc",
"gw c #f4fef3",
"Av c #f4fef6",
"z5 c #f4feff",
"wi c #f4ffef",
"v8 c #f4fff0",
"kj c #f4fff1",
"gm c #f4fff2",
"dc c #f4fff9",
"#n c #f4fffa",
"gH c #f4ffff",
"lp c #f5a8bc",
"hQ c #f5acbd",
"Hd c #f5bbc9",
"hB c #f5d0d7",
"hF c #f5d2d9",
"h4 c #f5d9b2",
"h5 c #f5dbb6",
"rN c #f5e1fa",
"uX c #f5e2f6",
"to c #f5e2f8",
"mA c #f5e4f6",
"Ek c #f5efef",
"m4 c #f5f1f0",
"BU c #f5f4f0",
"bj c #f5f4f2",
".1 c #f5f5f3",
"CC c #f5f5f5",
"B2 c #f5f5f7",
"Ah c #f5f6f0",
"CK c #f5f6f1",
"AQ c #f5f7f2",
"c5 c #f5f7f4",
"DA c #f5f7f6",
"zO c #f5f9ea",
"lh c #f5f9f8",
"zM c #f5faf3",
"zi c #f5faf6",
"tr c #f5faff",
"eG c #f5fbf7",
"AV c #f5fbf9",
"rb c #f5fbfb",
"ec c #f5fdee",
"ej c #f5fefb",
"el c #f5fefd",
"gM c #f5feff",
"zQ c #f5ffed",
"Fg c #f5fff4",
"dO c #f5fffa",
"#p c #f5fffb",
".3 c #f5fffc",
"#o c #f5fffd",
"ek c #f5fffe",
".5 c #f5ffff",
"rk c #f6a144",
"hC c #f6ccd6",
"hE c #f6ced7",
"jh c #f6d1d9",
"hw c #f6d2d6",
"hL c #f6d8e0",
"qX c #f6e1e6",
"BF c #f6e2e1",
"xj c #f6e5cb",
"ga c #f6edde",
"DO c #f6f2f1",
"zW c #f6f3fa",
"DE c #f6f4f7",
"CZ c #f6f5f1",
"#b c #f6f5f3",
"#f c #f6f6f4",
".f c #f6f6f6",
"zV c #f6f6f8",
"B7 c #f6f7f2",
"BW c #f6f7f9",
"Bs c #f6f8f3",
"eu c #f6f8f5",
"oT c #f6f8f7",
"je c #f6faf9",
"kw c #f6fafd",
"AJ c #f6fbf4",
"wQ c #f6fbf5",
"dN c #f6fbf7",
"rQ c #f6fbff",
"zK c #f6fcf0",
"da c #f6fcf8",
"z4 c #f6fcfa",
"em c #f6fcfc",
"zL c #f6fdf5",
"vI c #f6fdf6",
"AS c #f6fdff",
"ed c #f6fef1",
"D7 c #f6fef3",
"gN c #f6feff",
"e# c #f6fff0",
"e3 c #f6fff1",
"yJ c #f6fff2",
"mp c #f6fff3",
"Aw c #f6fff8",
"E9 c #f6fff9",
"#U c #f6fffa",
"A. c #f6fffd",
".6 c #f6fffe",
"e8 c #f6ffff",
"lV c #f7b3c2",
"Dl c #f7bdc9",
"F7 c #f7c5d0",
"Bb c #f7c8d2",
"hD c #f7ccd6",
"hv c #f7d3d7",
"yu c #f7d6dd",
"qW c #f7d9e1",
"yh c #f7dadc",
"p4 c #f7e4fa",
"xH c #f7e6f6",
"dE c #f7eeef",
"G1 c #f7f2ef",
"AD c #f7f3e8",
"AC c #f7f3ea",
"dR c #f7f3f2",
"ED c #f7f3f4",
"AB c #f7f4ed",
"Dq c #f7f5f6",
"CT c #f7f5fa",
"dT c #f7f6f2",
"#a c #f7f6f4",
"Dx c #f7f7ef",
".u c #f7f7f5",
".# c #f7f7f7",
"mB c #f7f7f9",
"oR c #f7f8f3",
"AK c #f7f8fa",
"qv c #f7f9f4",
"b8 c #f7f9f6",
"GF c #f7faf3",
"uY c #f7faff",
"en c #f7fbfa",
"dx c #f7fcf5",
"vo c #f7fcf6",
"d. c #f7fcf8",
"rp c #f7fdf1",
"cA c #f7fdf9",
"lZ c #f7fdfb",
"Cz c #f7fdfd",
"gk c #f7fef6",
"qY c #f7fef7",
"e2 c #f7fff1",
"e. c #f7fff2",
"e1 c #f7fff3",
"eZ c #f7fff4",
"gl c #f7fff8",
"D0 c #f7fff9",
"#V c #f7fffb",
"eF c #f7fffc",
"IQ c #f7fffd",
"#q c #f7fffe",
".V c #f7ffff",
"qK c #f8cbd0",
"hy c #f8cdd4",
"HR c #f8ced8",
"hx c #f8cfd5",
"H8 c #f8dbe0",
"jW c #f8dcb5",
"hn c #f8dee1",
"ku c #f8eaf7",
"zZ c #f8ecf8",
"mq c #f8eef9",
"hJ c #f8eff0",
"Az c #f8f3f0",
"xh c #f8f4e9",
"CV c #f8f4f1",
"ft c #f8f4f3",
"jf c #f8f4f5",
"Dw c #f8f5ec",
"Ir c #f8f6f7",
"CS c #f8f6fb",
"CA c #f8f7f3",
".0 c #f8f7f5",
"oo c #f8f7fc",
".M c #f8f8f6",
".g c #f8f8f8",
"lf c #f8f8fa",
"AW c #f8f9f3",
"dU c #f8f9f4",
"bu c #f8f9fb",
"nM c #f8faef",
"d7 c #f8faf5",
"br c #f8faf7",
"ct c #f8faf9",
"#w c #f8fcfb",
"bt c #f8fcfd",
"gO c #f8fcff",
"F9 c #f8fdf6",
"cd c #f8fdf7",
"cV c #f8fdf9",
"e9 c #f8fdff",
"pG c #f8fef0",
"s2 c #f8fef4",
"#T c #f8fefa",
"fU c #f8fefc",
"oE c #f8fefe",
"j7 c #f8fff0",
"dq c #f8fff3",
"xG c #f8fff4",
"e0 c #f8fff5",
"ia c #f8fff6",
"gx c #f8fff7",
"ce c #f8fff8",
"F. c #f8fffa",
"IG c #f8fffb",
"sC c #f8fffc",
"#W c #f8fffe",
".W c #f8ffff",
"nT c #f9a64a",
"nS c #f9a950",
"uk c #f9b0c3",
"vw c #f9c0cf",
"n# c #f9c3d0",
"hz c #f9ccd3",
"rf c #f9d4a0",
"l2 c #f9d7a7",
"up c #f9d8af",
"yT c #f9e8fb",
"yz c #f9e9d0",
"HL c #f9e9ea",
"z2 c #f9eef6",
"fT c #f9f0f1",
"gg c #f9f1de",
"yG c #f9f2d6",
"vy c #f9f3f3",
"B0 c #f9f3f5",
"AE c #f9f5e9",
"vz c #f9f5f2",
"le c #f9f5f4",
"vH c #f9f5f6",
"yw c #f9f6f1",
"jd c #f9f7f8",
"AL c #f9f7fa",
"AA c #f9f8f3",
".K c #f9f8f6",
".L c #f9f9f7",
".b c #f9f9f9",
"Bn c #f9f9fb",
"gj c #f9faf2",
"cP c #f9faf5",
"gP c #f9fafc",
"zN c #f9fbee",
"bG c #f9fbf6",
"cy c #f9fbf8",
"b9 c #f9fbfa",
"ee c #f9fcf5",
"dW c #f9fcff",
"#m c #f9fdfc",
"b6 c #f9fdfe",
"op c #f9fdff",
"ob c #f9fef7",
"cc c #f9fef8",
"ax c #f9fefa",
"df c #f9feff",
"d9 c #f9fff2",
"d8 c #f9fff3",
"dw c #f9fff5",
"cS c #f9fff6",
"cR c #f9fff8",
"d# c #f9fff9",
"yI c #f9fffa",
"Bm c #f9fffb",
"qZ c #f9fffd",
".7 c #f9ffff",
"nU c #faaa51",
"nI c #faadbf",
"nP c #fad6a2",
"sS c #fad6a6",
"hs c #fad7de",
"yV c #fae4fb",
"F1 c #faeceb",
"ex c #faeef0",
"GG c #faefed",
"II c #faf0ef",
"ix c #faf0f8",
"h9 c #faf2dd",
"lX c #faf4f8",
"IL c #faf5f2",
"Dn c #faf6f3",
"dQ c #faf6f5",
"CY c #faf6f7",
"C. c #faf7f0",
"hX c #faf7f2",
"zX c #faf7ff",
"eM c #faf8f9",
"j6 c #faf9e5",
"Bt c #faf9f4",
"AX c #faf9f5",
".Q c #faf9f7",
"eK c #faf9fe",
"ps c #fafaf0",
".n c #fafaf8",
".i c #fafafa",
"eL c #fafafc",
"rP c #fafaff",
"DB c #fafbf5",
"bH c #fafbf6",
"bs c #fafbfd",
"dX c #fafbff",
"i. c #fafcee",
"ei c #fafcf7",
"bq c #fafcf9",
".h c #fafcfb",
"ca c #fafdf4",
"c# c #fafdf6",
".2 c #fafefd",
"bv c #fafeff",
"mb c #fafff2",
"dp c #fafff3",
"dr c #fafff4",
"i# c #fafff7",
"e4 c #fafff8",
"a2 c #fafff9",
"sB c #fafffa",
"ay c #fafffb",
"cz c #fafffc",
"#z c #fafffe",
".X c #faffff",
"sD c #fbb0c4",
"ph c #fbb7c6",
"pv c #fbd6a2",
"w0 c #fbe1e2",
"yF c #fbeece",
"Ay c #fbf1f0",
"gF c #fbf1f9",
"wu c #fbf1fa",
"li c #fbf2f5",
"Bq c #fbf3f1",
"tp c #fbf3ff",
"Iu c #fbf5f5",
"zY c #fbf5ff",
"Ax c #fbf7f4",
"ha c #fbf7f6",
"rc c #fbf8ef",
"z3 c #fbf8f3",
"c6 c #fbf9fa",
"DL c #fbf9fc",
"cU c #fbfaf5",
"dY c #fbfaf6",
".P c #fbfaf8",
"xt c #fbfbef",
".N c #fbfbf9",
".a c #fbfbfb",
"nx c #fbfbfd",
"tq c #fbfbff",
"c. c #fbfcf6",
"ci c #fbfcf7",
"az c #fbfcfe",
"bI c #fbfdf8",
"aw c #fbfdfa",
"#l c #fbfdfc",
"ds c #fbfef5",
"bF c #fbfef7",
"oq c #fbfeff",
"do c #fbfff5",
"dv c #fbfff7",
"zT c #fbfff8",
"du c #fbfff9",
"cQ c #fbfffa",
"cf c #fbfffb",
".Y c #fbfffc",
"dP c #fbfffd",
".U c #fbfffe",
".C c #fbffff",
"zv c #fccedb",
"ht c #fcd9e0",
"Cj c #fce7e6",
"m# c #fce8c3",
"jI c #fce9eb",
"yZ c #fce9fc",
"IJ c #fceced",
"y0 c #fcecf9",
"u# c #fcf1f5",
"gE c #fcf2fb",
"jH c #fcf3f4",
"rO c #fcf4ff",
"zH c #fcf5e2",
"eE c #fcf6f6",
"CB c #fcf6f8",
"f7 c #fcf6fa",
"DI c #fcf7f3",
"ef c #fcf7fb",
"eg c #fcf7fd",
"dS c #fcf8f5",
"cI c #fcf8f7",
"fV c #fcf8f9",
"bA c #fcfafb",
"kv c #fcfafd",
"DF c #fcfaff",
"dt c #fcfbf6",
"dk c #fcfbf7",
".O c #fcfbf9",
"di c #fcfcf4",
".p c #fcfcfa",
".c c #fcfcfc",
"bB c #fcfcfe",
"dm c #fcfdf5",
"dl c #fcfdf7",
"aq c #fcfdf8",
"av c #fcfdff",
"bC c #fcfef9",
".9 c #fcfefb",
".k c #fcfefd",
"dn c #fcfff4",
"cM c #fcfff6",
"bD c #fcfff8",
"cg c #fcfffa",
".x c #fcfffb",
".w c #fcfffd",
".v c #fcffff",
"lk c #fdcbd6",
"A9 c #fdd0d7",
"jF c #fde4e8",
"yB c #fde5c1",
"Hs c #fdebeb",
"t0 c #fdefef",
"fS c #fdf1f3",
"gD c #fdf1fd",
"vV c #fdf2f8",
"G. c #fdf3f1",
"Br c #fdf3f2",
"in c #fdf3fe",
"dD c #fdf4f5",
"hW c #fdf4f9",
"pg c #fdf5f3",
"eW c #fdf7e9",
"AO c #fdf7f7",
"AN c #fdf7f9",
"b7 c #fdf8f5",
"eh c #fdf8fc",
"d2 c #fdf9ed",
"by c #fdf9f6",
"dj c #fdf9f8",
"d6 c #fdfaf1",
"Ci c #fdfaf5",
"d5 c #fdfbef",
"bz c #fdfbfc",
"Dr c #fdfbfe",
"f8 c #fdfbff",
"Dy c #fdfcf7",
"ap c #fdfcf8",
".J c #fdfcfa",
"vW c #fdfdf5",
".t c #fdfdfb",
".e c #fdfdfd",
"a3 c #fdfdff",
"cL c #fdfef6",
"cH c #fdfef8",
"bE c #fdfef9",
"## c #fdfeff",
"zJ c #fdfff1",
"cb c #fdfff9",
"ch c #fdfffa",
".S c #fdfffc",
".T c #fdfffe",
"Hx c #feccd7",
"yW c #fee6ff",
"IB c #feeaec",
"yE c #feebca",
"u. c #feeff4",
"gA c #fef0ff",
"gb c #fef2e2",
"gC c #fef2ff",
"gc c #fef3e1",
"wZ c #fef3f7",
"IA c #fef4f3",
"m9 c #fef5f6",
"nK c #fef5fa",
"gf c #fef6e3",
"BN c #fef6f4",
"on c #fef6ff",
"gh c #fef7e5",
"hY c #fef7ef",
"eX c #fef8ec",
"dC c #fef8f8",
"qy c #fef8fa",
"l0 c #fef9e6",
"mP c #fef9f5",
"AH c #fef9f6",
"d1 c #fefaef",
"eN c #fefaf7",
"fA c #fefaf9",
"iy c #fefafb",
"sP c #fefbf2",
"Dv c #fefbf4",
"AP c #fefbf6",
"#k c #fefcfd",
"#y c #fefcff",
"cK c #fefdf8",
"#u c #fefdf9",
".s c #fefdfb",
"#. c #fefdff",
"dh c #fefef6",
".q c #fefefc",
".d c #fefefe",
".Z c #fefeff",
"cN c #fefff8",
"dg c #fefff9",
"#t c #fefffa",
".E c #fefffb",
".l c #fefffd",
".j c #feffff",
"pq c #ffabc2",
"r. c #ffabc3",
"sM c #ffacc3",
"q1 c #ffb3c5",
"qM c #ffb6c6",
"sr c #ffc7d5",
"Ec c #ffcfd8",
"Dg c #ffcfd9",
"yq c #ffd0dc",
"vr c #ffd1de",
"yr c #ffd3e2",
"t7 c #ffd5e6",
"BL c #ffd6dc",
"tS c #ffd6e2",
"sv c #ffd6e7",
"hU c #ffd7df",
"GE c #ffd7e1",
"wX c #ffd7e3",
"qS c #ffd8e7",
"yp c #ffd9e1",
"qI c #ffd9e3",
"qH c #ffd9e5",
"Ai c #ffdae0",
"Fl c #ffdae1",
"GN c #ffdae2",
"yt c #ffdae5",
"ys c #ffdbe8",
"Cr c #ffdce5",
"sh c #ffdce6",
"qG c #ffddec",
"H. c #ffdee4",
"qL c #ffdee5",
"ul c #ffdee8",
"Ge c #ffdfe9",
"Ic c #ffe0e6",
"f0 c #ffe0e7",
"qA c #ffe0e8",
"sN c #ffe0ec",
"Cp c #ffe1e5",
"GH c #ffe1e6",
"vU c #ffe1e8",
"At c #ffe1e9",
"qJ c #ffe1ea",
"qT c #ffe1ec",
"sw c #ffe1ee",
"f4 c #ffe2e6",
"f1 c #ffe2e9",
"oU c #ffe2eb",
"pE c #ffe3b5",
"t1 c #ffe3e4",
"f3 c #ffe3e8",
"qV c #ffe3ed",
"qU c #ffe3ef",
"r# c #ffe3f0",
"rn c #ffe4b1",
"Be c #ffe4e7",
"zj c #ffe4e8",
"BO c #ffe4ea",
"He c #ffe4eb",
"fZ c #ffe4ec",
"nJ c #ffe4ee",
"vG c #ffe4f2",
"sn c #ffe4f3",
"f2 c #ffe5ea",
"q0 c #ffe5ee",
"so c #ffe5f0",
"pr c #ffe5f1",
"te c #ffe5ff",
"G2 c #ffe6ed",
"n. c #ffe6ee",
"tY c #ffe6f2",
"w6 c #ffe6f4",
"rD c #ffe6ff",
"s0 c #ffe7b3",
"f5 c #ffe7ea",
"vJ c #ffe7ec",
"Bk c #ffe7ed",
"hr c #ffe7ee",
"lW c #ffe7ef",
"uN c #ffe7ff",
"yC c #ffe8c3",
"Dd c #ffe8ea",
"sq c #ffe8eb",
"fY c #ffe8ee",
"v7 c #ffe9c0",
"zy c #ffe9ec",
"lI c #ffe9ee",
"wj c #ffe9ff",
"lL c #ffeaec",
"BT c #ffeaee",
"F2 c #ffeaef",
"vx c #ffeaf5",
"D2 c #ffebec",
"vA c #ffebed",
"zA c #ffebf0",
"jT c #ffebf1",
"tZ c #ffebf2",
"yn c #ffebf6",
"yY c #ffebff",
"yA c #ffeccd",
"Ed c #ffeceb",
"Fe c #ffecee",
"yb c #ffecef",
"lj c #ffecf4",
"yU c #ffecff",
"uy c #ffedbe",
"Df c #ffedef",
"HS c #ffedf0",
"Bc c #ffedf1",
"sy c #ffedf4",
"sx c #ffedf5",
"pU c #ffedff",
"h0 c #ffeeda",
"vq c #ffeef0",
"wR c #ffeef2",
"fR c #ffeef3",
"fX c #ffeef4",
"A8 c #ffefed",
"G9 c #ffefef",
"BM c #ffeff0",
"IK c #ffeff1",
"fQ c #ffeff5",
"yD c #fff0cc",
"j5 c #fff0d3",
"fL c #fff0f1",
"hV c #fff0f4",
"t8 c #fff0fb",
"oc c #fff0ff",
"Hf c #fff1f0",
"Cq c #fff1f1",
"f6 c #fff1f3",
"F8 c #fff1f4",
"zz c #fff1f6",
"gz c #fff1ff",
"Fm c #fff2f1",
"fO c #fff2f2",
"fK c #fff2f3",
"dL c #fff2f5",
"sz c #fff2f8",
"nY c #fff3c8",
"zp c #fff3f2",
"fN c #fff3f3",
"lJ c #fff3f5",
"hK c #fff3f6",
"jg c #fff3f8",
"fP c #fff3f9",
"ra c #fff3fa",
"gB c #fff3ff",
"re c #fff4d2",
"xs c #fff4d7",
"De c #fff4f1",
"fM c #fff4f4",
"eI c #fff4f5",
"G8 c #fff4f6",
"dK c #fff4f7",
"eC c #fff4f9",
"sO c #fff4fb",
"z1 c #fff4fe",
"nO c #fff5d4",
"sR c #fff5d6",
"vX c #fff5de",
"pF c #fff5e1",
"lK c #fff5f4",
"ny c #fff5f5",
"eJ c #fff5f6",
"ev c #fff5f7",
"sA c #fff5f8",
"fW c #fff5f9",
"w7 c #fff5fc",
"sp c #fff5fd",
"wY c #fff5fe",
"z0 c #fff5ff",
"pu c #fff6d3",
"l1 c #fff6d5",
"zF c #fff6e0",
"ro c #fff6e3",
"ua c #fff6f6",
"dF c #fff6f7",
"Au c #fff6f9",
"oS c #fff6fb",
"m8 c #fff6fc",
"lg c #fff6fd",
"e5 c #fff6ff",
"uo c #fff7db",
"zE c #fff7e1",
"gd c #fff7e3",
"yy c #fff7e5",
"g# c #fff7ed",
"ya c #fff7f5",
"dI c #fff7f6",
"ez c #fff7f7",
"eD c #fff7f8",
"zB c #fff7f9",
"IN c #fff7fa",
"jc c #fff7fc",
"gy c #fff7ff",
"jV c #fff8de",
"nZ c #fff8e3",
"f9 c #fff8f5",
"eA c #fff8f6",
"jG c #fff8f7",
"ey c #fff8f8",
"dM c #fff8f9",
"c8 c #fff8fa",
"yv c #fff8fb",
"t9 c #fff8fe",
"as c #fff8ff",
"rd c #fff9e4",
"ge c #fff9e5",
"nN c #fff9e6",
"eR c #fff9ec",
"dH c #fff9f6",
"bx c #fff9f7",
"BZ c #fff9f8",
"cu c #fff9f9",
"cv c #fff9fa",
"sg c #fff9fb",
"dJ c #fff9fc",
"eB c #fff9fd",
"ar c #fff9ff",
"pt c #fffae5",
"xi c #fffae9",
"eS c #fffaea",
"hZ c #fffaec",
"dG c #fffaf7",
"aZ c #fffaf8",
"Bd c #fffaf9",
"cJ c #fffafa",
"c9 c #fffafb",
"ew c #fffafc",
"eH c #fffafd",
"at c #fffafe",
"#0 c #fffaff",
"zG c #fffbe5",
"ma c #fffbe7",
"sQ c #fffbe8",
"un c #fffbea",
"jU c #fffbed",
"d3 c #fffbef",
"a0 c #fffbf8",
"aY c #fffbf9",
"a1 c #fffbfa",
"cw c #fffbfb",
"c7 c #fffbfc",
"#Y c #fffbfd",
"#Z c #fffbfe",
"#x c #fffbff",
"s1 c #fffceb",
"uz c #fffcec",
"eV c #fffcee",
"eQ c #fffcf0",
"zC c #fffcf1",
"CJ c #fffcf3",
"dZ c #fffcf5",
"Ff c #fffcf6",
"cT c #fffcf7",
"cX c #fffcf8",
"#v c #fffcf9",
"bw c #fffcfa",
"cx c #fffcfb",
"au c #fffcfc",
"#X c #fffcfd",
"Ch c #fffcfe",
".z c #fffcff",
"eT c #fffded",
"eP c #fffdf3",
"um c #fffdf4",
"g. c #fffdf6",
"eO c #fffdf7",
"D1 c #fffdf8",
"cW c #fffdf9",
".8 c #fffdfa",
".B c #fffdfc",
".A c #fffdfd",
".D c #fffdfe",
".y c #fffdff",
"yH c #fffee9",
"zD c #fffeec",
"d4 c #fffef2",
"eY c #fffef3",
"B9 c #fffef7",
"D8 c #fffef8",
"#r c #fffef9",
"#s c #fffefa",
".H c #fffefb",
".r c #fffefc",
".I c #fffefd",
".m c #fffeff",
"eU c #ffffef",
"gi c #fffff1",
"yx c #fffff3",
"d0 c #fffff6",
"cO c #fffff8",
".G c #fffffa",
".F c #fffffb",
".o c #fffffd",
"Qt c #ffffff",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.a.b.c.dQtQtQtQt.e.b.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtQt.b.f.cQtQtQtQtQtQt.g.d.dQtQtQtQtQtQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.d.dQtQtQtQtQtQtQt.h.i.jQt.j.e.j.c.jQt.kQt.l.e.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.m.m.m.m.m.m.m.m.m.m.mQtQtQtQtQtQtQtQtQt.j.j.j.j.j.j.j.jQtQtQtQtQtQtQtQtQt.mQt.mQt.mQtQtQtQtQtQt.jQtQtQtQtQtQt.cQt.d.nQt.oQt.a.cQtQt.b.o.o.p.o.o.o.o.o.mQt.mQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
".q.q.q.q.q.q.q.o.o.o.o.o.r.r.o.o.s.o.o.s.r.o.o.s.o.o.n.o.o.o.o.n.o.o.q.q.q.o.t.n.o.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.p.o.t.o.o.p.o.o.q.o.o.o.u.o.o.o.o.o.o.o.t.t.o.o.o.o.o.o.o.o.o.o.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.j.v.j.v.j.v.l.w.l.w.l.w.l.x.l.l.j.jQtQtQtQtQtQtQtQt.j.j.j.j.j.j.m.y.y.y.y.z.z.z.z.y.A.B.r.o.l.lQtQt.j.j.j.v.C.C.C.C.v.v.v.j.jQt.o.o.o.o.m.m.m.m.D.m.m.m.o.r.r.o.j.v.j.j.j.j.l.l.l.l.l.E.l.E.l.lQtQt.o.o.F.F.G.G.G.G.H.F.I.o.m.m.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.d.d",
".q.o.o.o.q.o.o.o.o.J.r.o.o.o.o.o.r.K.J.r.r.r.s.o.o.o.p.t.u.L.o.o.o.o.o.o.o.o.o.o.o.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.q.o.o.p.t.p.n.M.o.t.o.N.q.o.o.N.o.o.o.o.q.q.o.o.o.o.o.o.o.o.o.o.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.j.v.j.v.j.v.l.w.l.w.l.w.E.x.E.l.j.jQtQtQtQtQtQtQtQt.j.j.j.j.v.j.j.m.m.m.y.y.z.z.y.y.I.r.q.l.w.lQtQtQt.j.j.v.C.C.C.C.C.v.v.j.jQt.o.o.o.o.m.m.m.m.m.m.m.m.o.q.r.o.j.j.j.j.j.jQt.lQt.l.o.l.o.l.o.lQt.jQt.o.F.G.G.G.G.G.H.F.I.m.m.m.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.d.d",
".q.o.o.o.o.o.o.o.o.o.o.o.o.r.O.P.O.o.o.o.o.o.o.J.Q.t.o.o.o.o.o.p.R.p.t.o.o.t.o.o.p.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.p.o.o.t.o.o.o.o.t.o.o.o.o.t.o.t.t.q.o.o.o.o.o.o.o.o.o.o.o.o.o.o.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.j.jQt.jQt.jQt.j.o.l.q.S.q.S.o.l.j.j.j.j.j.j.j.j.j.j.j.j.j.j.T.U.V.V.W.X.v.v.j.jQtQt.T.T.T.Y.w.l.m.m.mQtQt.j.j.v.v.v.v.T.T.q.q.q.o.lQtQtQtQt.d.d.DQtQtQtQt.T.q.lQtQtQtQtQtQt.mQt.y.d.D.d.D.d.D.Z.j.v.j.j.j.o.o.F.F.F.oQt.mQt.mQtQt.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.d.d",
".q.o.o.q.q.q.q.q.q.o.r.r.o.r.J.r.o.s.r.s.P.0.s.o.o.o.N.p.R.1.q.q.o.o.t.p.o.p.t.o.L.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.o.p.o.n.n.p.u.o.M.t.L.o.t.L.1.t.n.p.o.o.o.o.o.o.q.q.q.q.q.q.q.q.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.d.d.d.d.d.d.d.d.d.q.q.t.t.q.q.q.T.T.T.T.T.T.T.T.j.j.j.T.T.k.k.2.3.4.5.6.V.7.7.C.C.v.U.T.T.T.j.o.B.8.B.r.r.q.q.S.q.S.d.q.q.s.s.s.S.S.T.T.T.k.k.k.e.T.j.j.T.k.9.k.Z.y.y.y.y.y.y.y.y.y.y.y.y.y.y#.##.C.C.C.C.U.T.S.S.S.d.d.Z.Z#..Z.d.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.q.q.t.t.p.p.t.t.P.Q.P.O.Q#a.0.P.J#b.0.J.J.r.0#c#d#e.M.p.n.M#f.o.o.o.L.o.o.p.o.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.L.t.q.N.t.t.t#g#h#i#j.o.q.1.o.M.N.q.o.o.q.q.q.q.q.q.q.q.q.q.q.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.d.y.y.y.y.y.y.D.D.D#k#k#k#k.r.q.T.U.U.U.U.U.U.U.T.T.T.k.k#l#l#m.3#n#o#p.6#q.W.7.C.U.T.d.D.D.D.y.8#r.8#s#s#s#s#t#s#t.r#s#u#v#v.s.9.2.2#m#m#m#m#m#l.2.U.2#m#w#w#l.y.z.z.z.z.z.z.z#x#x#x#x#x#x#x#y.C.X.X.X.X#z.U.U.U.U############.d.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".t.q.t.t.p.N.N.N.p.o.r.Q#a.Q.r.o.s.J#A#B#C#D#E#F#G#H#I#H#J#K#L#M#g#N.q.u.q.o.n.o.o.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.N.p.o.p.o.N#O#I#P#Q#R#S.R#d.M.M.N.t.o.o.q.q.q.q.q.q.q.q.q.q.q.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.T.Z.y.y.y.y.y.y.y.D.D#k#k#k#k.r.q.T.U.U.U.U.U.U.U.T.T.k.k.k#l#l#l#T#U#U#V#V#V#W#z.U.T.d#X#Y#Z#0#Z.8#r#r#r#r#r#r#r#s#s#s#s#v#v#v.s.c#m#m#m#m#m#w#w#w#m.2.2#m#w#w#l.D.D.z.z.z.z.z.z.z.z.z.y.z.y.z#.##.X.X.X.X.X#z#z.U.U.C.C######.Z.d.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".t.q.q.t.p.p.N.N.N.o.r.O.J.o.o#1#2#3#4#5#6#7#8#8#9a.a#aaabacadaeafag.L.n.n.o.L.o.t.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.o.o.n.pah.uaiajakalamanao.o.o.o.n.p.q.o.o.q.q.o.q.q.q.q.q.q.q.q.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.T.Z#..Z.Z.Z.Z.Z.Z.Z.Z.d.e.e.d.d.d.T.T.U.U.U.U.U.U.U.U.T.T.T.T.d.d.Japapaq.p.9.9.9.d.D#x#0arasaratau#s#s#t#t#t#t#t#t#t#s#s.r.r.s#k.eav.k.kawawaxaxaxay.S.S#l#laz.c.D.r.D.D.D.D.y.D.y.y.y.Z.y.Z.y.Z##.U.C.U.U.U.U.U.U.U.T.T.d.d.Z.d.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".t.o.q.t.t.p.p.p.p.0.J.r.s.K#2aAaBaCaDaDaEaFaGaHaIaJaKaLaMaNaOaPakaQ.u.o.n.o.p.o.t.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q#f.o.u.t.n.oaRaSaTaUaVaMaW.o.1aX.p.q.o.o.o.o.o.o.q.q.q.q.q.q.q.q.S.S.S.S.S.S.S.S.S.S.S.S.S.S.S.T####.Z##.Z##.Z##Qt##.d.T.d.T.d.j.d.T.T.U.U.U.U.U.U.U.j.j.j.jQt.o#vaYaZa0a1.J.p.p.d.D#x#0arasar#0.D.S.S.S.S#t#t#t.F.F.F#t.r.q.D.d.y.d.d.q.9.9.9a2ay.Y.l.l.e.ea3.e.r#t.r.q.r.q.r.q.q.d.d.T.T.T.T.T.d.S.S.S.T.Y.U.Y.U.S.T.q.d.r.r.r.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.t.q.N.q#f.o.M.N.P.o.P.Oa4a5a6#9a7a8a8#9a9b.b#babbbcbdbebfa#bgbhbi.L.o.p.o.o.N.o.t.o.p.q.q.t.o.n.o.N.L.o.o.q.n.p.o.o.n.o.o.L.o.o.o.t.n.o.p.oah.o.Q.o.s.o.o#bbjbkblbmbnbobp.P.s.o.o.1.o.o.p.o.o.N.o.t.o.p.p.o.n.o.lbq.lbr.Sbq.law.l.S.9.9.S.S.S.kbs.v.jbtbubv.jbv.T.2.k#m.k.U.l.l.t.t.taw.S.l.w.Y.w.w.w.w.S.S.t.JaZbwa1bxby#u.q.tQt.dbzbAatatatat##.v.v#m.2.l.lbqbq.9.S.9.e.Ta3bB.D#kbA.O.pbCbCbDbCbCbE.F.o.o.DbzbEbFaq.E.FbCaqbCbCawaw.Y.w.waybGbH#u.F#t.tbC.9bI.l.F.q#u.s#v#v.8.r.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.o.o.N.o.1.p.u.N.r.QbjbJbKbLbMbNbObPbQbRbSbTbU.Q.n.p.obV#ObWbXbYbZ.N.o.p.o.o.N.q.p.o.o.q.N.n.q.o.p.o.o.n.M.o.o.o.L.L.o.q.o.p.n.p.u.o.q.t.t.o.o.o.o.Q#b.J.J#b.ob0b1b2b3b4b5.obj.K.o.L.o.N.N.o.n.o.n.M.t.o.o.o.t.o.9aw.l.l.law.l.9.9awaw.9.S.S.l.l.Tbt##bt.jb6.j.U.T.2.k.2.T.Y.l.l.r.I.o.r.t.9.S.Y.Y.Y.w.w.S.S.t.Jb7#v.H.H.H.F.pb8b9#w#m.k.T.j.j.v.X.C.C.C.v.v.l.9.l.E.l.l.S.T.T.d#k.B.B#sapc.c#cac#c#c.aq#v.B.D.r.FcbbFcb#t#t#t#tcccdcdcdcea2cfcg.G.G.F#s.F.E.Echciaq#u#s.H.H#s.G.r.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.t.p.p.o.M.n.t.ocjckbQclcmbNcnb2cocp#b#b.r.o.J.o.t.N.o.N.M.Mah.Nah.t.q.N.t.q.p.t.o.O.O.J.o.o.s.r.P.Q.s.r.o.J.J.J.o.L.o.M.o.o.o.o.o.o.t.t.t.R.L.N.o.Q.Q.s.O.O.o.Qcqcr#C.0.o.O.P.o.o.o.q.L.o.o.u.o.o.o.t.o.o.N.t.taw.S.lbq.lbq.S.l.l.l.l.9awbqawaw.kcs.bb9Qtct.c.k.abq.Naw.paw.papcucvcwcx.P.Lcyawaxayay.Y.S.S.t.tbE#t#tbEbC.E.wczcAcBcBcCcDcEcFcG.7.W.C.C.v.2awch#tcHcibHbH.ncy.NcIcJ.B.FcKcLcMcMbDcNcOcHa0a0au.I.FbEcPcibCbCbDbDcgcgcQa2cRcSa2cg.GcTcUcUaqbCawcV.S.l.F.F.G.GcWcX.r.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.N.p.o.o.n.L.o.qcYcZc0b2b3cnc1c2c3.r.J.Q.o.o.0.s.o.o.p.n.L.q.o.u.n.q.q.N.N.t.t.p#b.K.o.o.r.P.0.o.o.O.K.K.o.K.s.o.o.n.t.R.o.N.o.t.p.n.o.t.p.o.o.p.O.o.o.r.J.J.Q.J.r.o#a.oc4.o.o#a.t.N.L.n.o.o.L.p.p.t.M.o.o.N.o.Nc5.S.9b8.9.9.S.l.9.S.S.9bqbqaw.t.mbzc6.m.D.m#k.o.s.r.o.o.o.F#s.8c7c8c9c7au.s.q.ld.cVaxay.9.S.q.S.xcfd#cdcdbIawbq.w.YdadbcCdcddde.7dfdf.C.kbrbHdgdhdididhcKcKaq#udjbydkdldmdndodpdqdrdndsdtdka1.B.o.r.J.r.o.tbEchchduducgcgdvdwdx.G#s#u#t.l.Y#z.C.v.w.S#t#u#va0a0.r.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.o.o.q.o.M.M.obZcZb3b2dydzdAdB.o.o.r.r.o.o.P.P.J.M.o.L.p.o.q.o.N.o.q.q.p.n.p.t.N.o.o.O.K.P.s.O.sc3.K.o.P.o.r.o#1.L.L.1.L.oah.o.o.o.R.1.o.M.u.u.p.P.o.J.P.J.s.K#a.K.o#A.K.s.o.o.s.o.t.q.o.q.n.t.N.1.p.t.t.L.u.p.t.S.l.l.S.S.lbqb8brbrcybqaw.9.l.odC#XdDc7dE#XdFaYbxbxaZaYaYdGdHdIdJdKdLdFdMdj.PbqdNd.cVax.9.S.q.S#UdO#VdP.l.pdQdRdGdSdTdUbIbCcddV.XdWdXbB.OdYdZd0d1d2d3d4d4d5d6dZ#saqd7dxd8d9e.e#eaebecedeec#aq.sefegehatatehbA.D.OcPdUeich#tbDc#eibq.9.w#zejek.Welelemen.h.p.s.r.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.o.o.N.u.N.q.Leoa9bOaEepeq#C.o.Q.J.0.J.s#b.P.o.o.o.o.q.q.o.t.o.o.o.p.q.q.L.n.q.nc4#ac4.s.o.PcYerbTcY.o.J.o.0.J#b.p.q.M.q.t.n.q.q.p.M#d.o.nes.o.N.r#b.Q.0.o.o.o.o.0.O.o.r.Q#1#A#b.p.o.p.o.o.n.q.o.t.o.o.M#f.o.q.o.lc5etbqeu.9cyeu.Sawbqbqawawbq.OdM#Yevewex#YeyezeyeyeyeybxbxeAdIeBeCdLdKeDeE.P.qbrd.cVax.9.S.q.YeFdceGbq.rc7eweHeIeIeJeycuaYdGcIeKdXeLeMeNeOePeQeReSeTeUeVeWeXeYdlc#dxeZe0dqe1e2e1e1e3e3cSe4bC.pase5e5ararar#0.y.m.s.O.O.s.F#tbC.S#m.7.7.We6e7.5.Ve8.Ve9b6#l.e.e.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.q.o.L.R.o.pf.f#faa6fbfcfd.obU.o.Q.r.o.r.o.o.s.P.n.L.q.o.o.t.L.N.o.n.q.o.L.L.q.nc4.o.r#cfefffgfhfifjfkfl#1bj.r.P.o.p.q.t.u.qfmfnfofp.o.R.o.RaXfqfrfsfta1.BfufvfwfxfyfzdQfA.Ia1#CfBfCfDfE.L.o.n.o.t.R.oah.N.ofFfGfHfIfHfJetbq.9.9.l.Scycybqawbr#aeyeIfKfKcvc9eDfLfMfNfNfOfOfOfOfOfPfQfRdLfSfTcI.ocybqaxay.S.S.S.Y.7fUctfVfWfXfYfZf0f1f2f3f4f5f6eHf7f8c7eEf9g.g#gagbgcgdgegfggghgigjgkglgmgngogpgqgrgsgtgugvgwgx.p#xgygzgAgBgCgDgEgFf7at.D.Dcxcx.t.v.VgGe7gHgIgJgKgJgLe7gMgNe9gOgP.d.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.q.o.n.R.ogQgRgSbngTgU#D.J.o#a.J#b.o.K.0.o.s#b.o.o#f.o.o.u.o.o.t.t.M.o.o.M.M.q.n.obUgVgWgTbmgXclgXfagXfigYgZ.r.o.raX.o.n#Aahg0aabMaUg1#N.saQa5g2g3g4g5.Idjg6g7g8g9h.h#cxcxhahbhchdheabhfaR.o#b.t.oah.o.1.qhghhhihjhkhlhmeu.l.S.tbz.K.1b8.9.oauezhnhohphqhrhshthuhvhwhxhyhzhyhAhBhChDhEhFhGhHhIhJdj.O.p.9.S.S.S.l.2.k.m.zhKhLhMhNhOhPhQhRhShThUhVhW.Z.DhXhYhZh0h1h2h3h4h5h6h7h8h9i.i#iaibicidieifigihiiijikilima2inioipiqirisitiuiviwix#x.Diybz.eiziAiBiCiDiEiFiGiHiIiJiKiLe9az.a.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.q.d.d",
".q.J.s.r.Q.oiMiNiOfbbniNiP.oc4.o#b#b.o.0.o.P.K.o#a.o.o.O.s.r.s.o.s.r.o.o.P.J.o.Q.oiQbaiRfbiOfagUbmfaaFa6iSepiT.O.o#a.s.I.OcxiUiVb2iWg3iX.OiYdyiZepepaBi0.Q.odBfhc0i1fai2.s.P.o.Oi3i4i5dzb3i6.oft#adj.oi7.K#bi8i9j.j#jajb.o.h.j.biyjcdJjd.jjejfjgjhjijjjkjljmjnjojpjqjrjsjtjujvjwjxjyjzjAjBjCjDjEjFeDjGa1.t.q.l.T.e#y.m#kjHjIjJjKjLjMjNjOjPjQjRjSjTf7b6.vcLjUjVjWjXjYjZj0j1j2j3j4j5j6j7j8j9k.k#kakbkckdkekfkgkhkikjkkklkmknkokpkqkrksktku.zkvQtQtkwkxkykzkAkBkCkDkEkFkGkHkIkJ.2cxeN#s#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.o.r.J.P.0kKkLa7aDdykM.o.Q.K.o.o.J.J.K.r.J.r.o.o.o.K.K.o.o.o.o.r.P.o#a.O.QbU.okN#Ec0cldzepkOkPkQkRg2a7kSi1a6kT#cfAfAcxha.IkUkVkWkXg4kYfykZk0k1k2a7k3.O.O#ak4k5epa7k6iQ.o.O.o.Ok7hlaMbMdzk8k9.I.Ihal..I.Il#aGlalblcldlele.j#llfatlglgc6.jlhliljlklllmlnlolplqlrlsltlulvlwlxlylzlAlBlClDlElFlGlHlIlJdIcu.J.9.S.TQtat.y#XlKlLlMlNlOlPlQlRlSlTlUlVlWlXlYlZgjl0l1l2l3l4l5l6l7l8l9m.m#mambmcmdmemfmgmhmimjmkmlmmmnmompmqmrmsmtmumvmwmxmymzmAasmBbs##mCmDmEmFmGmHmImJmKmLmMmNmOkx#ma0mP#s#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.o.J.P.omQmRaDi1clb1cj.r.K.O.Q.K.J.Q.o.Q.O.o.Q.P.o.r.o.o.O.O.o.o.o.o#1.o.o.o#cmSa8#8clc1fe.o.K.o.0mTmUbLfadzmV.r.s.P.Q.0.omWmXbLepmYmZaGm0bLm0aCaCbJ.o.o.JkTm1fadzdAmQ.P.Q.J#a.ofBadb2clm2m3hba1.Im4ham5dygUaPm6m7.FcIkU.k.TQt#xasm8bz.heum9n.n#nanbncndnenfngnhninjnknlnmnnnonpnqnrnsntnunvnwhKfNb7apbIawax.Y.jnx.mc7nylInznAnBnCnDnEnFnGnHnInJnKnLcAnMnNnOnPnQnRnSnTnUnVnWnXnYnZmbn0n1n2n3n4n5n6n7n8n9o.o#oaobocodoeofogohoiojokolomonooopoqorosotouovowoxoyozoAoBoCoDmDoE.pdY#s#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.s.J.O.omToFcnaEbnoG.0c4.o.o.r.O.K.r.o.P.s.o.o.Q.o.o.o.Q#a.o.o.0.J.O.K.r.K.QoHb2bli1bkb5.r.J.0bU.o.PoIkSiSoJoKi3.s.s.s.K.P#CoLaDiSoMgTbNgXmYcq.K.o.o.Obj.J#Da6#9bm#GbU#b.K.o#b.ogQoNcli1g9oO.IcxcI.IoPoQfbb3a##JcPoR.I.o.hengP.m#xoS.moTbrcvoUoVlsoWoXoYoZo0o1o2o3o4o5o6o7o8o9p.p#papbpcpdpepfnypgdYbCa2axcVay.w#l.dfAeJlWphpipjpkplpmpnpopppqprm8emcVpsptpupvpwpxpypzpApBpCpDpEpFpGpHpIpJpKpLpMpNpOpPpQpRpSpTcipUpVpWpXpYpZp0p1p2p3p4gydX.X.Xp5p6p7p8p9q.q#qaqbqcqdqeqfqg.Vav.N#t#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.s.o.o.Oqhg3b2a7#9qi.J.K.o.Q.o.o.Q.o.J.oc3#c.ObU#AcYc3cY#b.sbj.Q.Q.P.o.K#aqhqjc0bmqkk7.J.obU.r.ock.J.ra9c0b3faql.s.s.s.Q#abRoJcnbNdya7bMqm.rc4.r.K.O.P.o#aqnbldyclcZ#a.P.P.o.O.P.1qogUaFqpqqqrcxdRk9qsqtgXbmqubVqvqw.I.o.j.vqx.m.zqyQtqz.N#YqAqBqCqDqEqFqGqHqIqJqKqLqMqNqOqPqQqRqSqTqUqVqWqXeyb7dYbI.xcfceqYa2.wqZ.UfAlJq0q1q2q3q4q5q6q7q8q9r.r#rarbcyrcrdrerfrgrhrirjrkl5rlrmrnrorprqrrrsrtrurvrwrxryrzrArBrCiyrDrErFrGrHrIrJrKrLrMrNrOrPe9rQrRrSrTrUrVrWrXrYrZqcr0r1qfr2gH.X#l.q#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.s.o.oc4r3cniOaFc1cp.o.obj.J.O.P.r.o#b.Pc2r4r5oGr6oGr5r7r7cZr8k7.r.J.o.Q#Ar9c0clmUs..oc4.o#a.P.o.O.ockfii1iOk6bS.Q.K.Q.O.Os#a6#9gXfaaDr7c3.r.o#1.o.o#1.siPdAcla7fas#.P.o.P.J.o.Q.osasbm0scqpsdcxhaoOsekXbofghmsf.Ech#a#1.2.C.U.e.ysg.jdN.pcvshsisjskslsmsnsospsqlLlIsrjvssstsusvswsxsyszsAc9.IcPeia2cfsBa2ccbIcQsC.C.OlJqVsDsEsFsGsHsIsJsKsLsMsNsObt.9sPsQsRsSsTsUsVpysWsXsYsZs0s1s2s3s4s5s6s7s8s9t.t#tatbtctd#xtetftgthtitjtktltmtntotptqdftrrRtstttutvtwtxrXtytztAtBtCtDtE.Vbt.q#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.s.J.rmQ#GgUdybotFmQ.o.o.r.o.r.O.o.o.QtGa5fbfbbNbNi1dyaEiOiSfca4.O.Pbjc4kMfbtHiOkQ.sbj.K.o.Pbj#b#ac4tIclbNgUqkmQ.Q.Q.O.s.0tJcna6b2dzaBc4.oc3#a.o.Q.o.o.ri3k6bLa7oJoI.P.J.r#a.o.P.taXtKiSh.k0tLtMtNk2tOh.tPiM.qtQa2ei.r.o#mtR.v.b.Diy.YcV.OlJtStTtUtVtWtXtYtZdJt0ezt1t2t3t4t5t6t7t8t9u.u#qy.O.laxcdcea2a2bDbDcHbC#V.7.puafZubucudueufuguhuiujukulsOav.oumunuoupuqurusutuuuvuwuxuyuze4uAuBuCuDuEuFuGuHuIuJuKuLuM.zuNuOuPuQuRuSuTuUuVuWuXtp.m.vuYgHuZu0u1u2u3u4u5u6u7u8u9v.v#.5df#w.q#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.o.Q.Ok7gWboaDvaaB.o.P#a.o.K.O.o.J.o.os.epbOvba8aGvcboblaE#9b1cq.J.o.o#1vdc0iOmXvec4.r.P.O.s.0#1vfoGkLkSblgUvg.Q.r.o.o.Oi0#FiSbMvaoLk4.o#1.o.o.o.K.J.O.ovh#8bmbnbPvi.P.0.o.0.o.P.N.o#BmXkXk2vjvkvltOvmvni3.oah.lvovp.P.JenfU.v.k#k.OaxccdSvqvrvsvtvuvvvwvxarvyvzaYvAvBvCvDvEvFvGra.yvHeMQt.hdNdavIvovobIcH#rcKaq#U.7.ScvvJvKvLvMvNvOvPvQvRvSvTvUvVbs.ovWeRvXvYvZv0v1v2v3v4v5v6v7eRd#v8v9w.w#wawbwcwdwewfwgwhwi#Xwjwkwlwmwnwowpwqwrwswtwu.y.jbue8r2wvwwwxwywzwAwBwCwDwEwFgJ.W.X#l.q#t#t#t#t#t.q.q.q.q.q.q.q.q.d.d.d.d",
".q.0.obj#BfhdzfbcmmS.o.J.P.r.o.J.o.Q.oc4cpwGdAgWwGwHb4kObmb2bNqniU.siU#1#2va#9m0#Gi0.P#bvfiMbSwIwJwKg3b2aFgUb4#2.o.u.u.N.oaRwLa#j.aPwM#d.L#f.N.o#d.J.o.s#bl#bLdyvcvdbj.o.J#b#a.o#b.o.n.P#3kZg9g8wNwOkZk1h#.o.o.LwP.Y.Y.r.r.T.2fU#m.osfdPwQbwwRwSwTwUwVwWwXwYwZ.odU.8w0w1w2w3w4w5w6w7eL.a#l.k.U.w.w.Y.9bC#t.G#rcW.Fw8qZd.a1cww9x.x#xaxbxcxdxexfxgjT.ybu.#.FxhxixjxkxlxmxnxoxpxqxrxsxtqYxuxvxwxxxyxzxAxBxCxDxExFxG.uxHxIxJxKxLxMxNxOxPxQxRnK.D.m.PrbgKxSxTxUxVxWxXxYxZx0x1x2.W.C.T.q#t#t#t#t#t#t.t.t.p.t.t.q.q.t.e.e.d.d",
".q.o.K.JmQc1fa#8bOmY.P.P.r.J.o.r.o.O.o.o.okNb5mQmQmQi0wGbNclb2#D.o.K.o.ox3x4aEbnoFmVtFg0eqwHfioJcnb2i1epiOx5gZ.o.0.p.L.N.tx6x7anx8aa#L.N.q.o.o.o.o.o.r.Qviqnc0b3clr4.0.J.J.s.P.o#1.M.o.Kfdx9y.scqpk0y#m3.I.obU.q.ldNdN.P.J.k.2#z.U.t.tcfeiyaybycydyeyfygullgvHaxeidGyhyiyjykylymyn#0av.2#m#m#maxaw.S.taqap#vcX.8.HawdPeGc5.HfNyoypyqyryrysytyuyvsgbAaz.e.oywyxyyyzyAyByCyDyEyFyGyHcNcfyIyJyKyLyMyNyOyPyQwhyRySe0bC.zaryTyUyVyWyXyYyZy0asdJdCa0by.ly1y2kItDy3y4y5y6y7y8y9.V.C.Y.o.t#t.F.F.F.F#t.q.t.q.q.q.q.q.t.e.c.d.d",
".q.o#b.ob5oFi1a6bOmY.K.s.o.O.o.s.s.r.J.P.o.J.o.o.r.ocYz.aDepbMc2.J.O.scjtFepdyblgXiOcni1fbfabmgUaDaGz#g2qmc4.r#1.o.o.L.t.nzaaczbaPzc#O.t.u.o.t.R.o.o.O.rtGzdiSb3aEfr.J.P.s.o.Q.s.0.o.R.r.ozek0g8k0zfzgiX.I.o.Jah.lzhzi.PfA.c.2#z.Ubr.lsBqveAzjzkzlzmznzon.oSjdeu.FzpzqzrzsztzuzvfP#Y.2.2.2#l#law.N.q.s.JfAfAa0cw.B.q.w#Tzwzxeib7ezzyzzzAoSzBcw#X#1.aQt##Qt.McOzCeSzDzEzFzGzHzIzJzKzLqYwQzMnMzNzOzPzQzRimzSzScSzTzUzVzWzXzYgy#xzZz0z1z2fWc7.H#rz3.Gz4z5z6z7z8gHtEz9.5gHA.czcdbE.Fdk#t#t#t#t#tbE.t.p.o.o.o.o.q.q.e.c.d.d",
".q.o.o.oiPoMfaa7boeq.0.s.o.O.s.J.J.o.r.P.Q.P.0bj#abjk4A#bLclfiAa.P.o.o.OAbcnz#aEdy#9cnb2bniSepb3m1#EqhmQ.J.o.rbj.s.t.M.o.u#Kj.j.Acaj.n.q.M.o.o.M.o.r.Q.oerc1bLa6gTfd.o.o.o.o#a.O.J.n.n.oerAdAeg8h.AfAgfu.Ibj.o.pbqaxawcxcx.d.T.2.2cy.lcfAhdHAiAjAkAlAmAnjTdM.N.1.HlLAoApAqArAsAtAuc6#w#w#l.k.d.q.o.J.s.Jdjdja1a1.O.Mbqcz#VAvAwccdUAxbwAyyaAzvz.NwP.cQtgPbu.e.oAAABACADAEyxd0AFcf#VAGcf.EbEb7f9bxAHbycibIzUAIAJdwAI.vbv.vAKgPQtALAM.yANsgAOdG#rAP.GAQcV.v.C.7ARASATAUAV#TcdAW#s.HAXdkaqaqaqaqci.N.n.t.t.q.q.q.q.e.e.d.d",
".q.P.o.QcjAYb2cni1aCvi.P.s.s#a.r.o.J.o.o.s.o.J.o.o.ovhgTiOfabkcq.J.o#bbUfafba6#6iRfifjgWmYgYs.k7AZ#abjc3bU.J.o.o.J.t.M.oA0bdanj.A1A2.o.n.q.N.o.o.o.o.Q.oqhg3gUcnbP#2.s.o.O.o.P.s.QA0.ogZA3g8qtk0A4A5A6A7ft.o.o.R.S.w.l.I.A.D.d.2.2aw.lcdcKA8A9B.AlB#BaBbBcc9.oftBdBeBfBgBhBiBjBkjH.Qcybq.p.t.r.o.oc6bz#kbAc6bz.a.M.NBleuaycABmdP.w.o.o.r.r.o.Mayay#l.cBnmB.j.j.p.L.F.FcUc..xeGBo.7Bpd..odYBqBrdFAu.yALBn.j.lBsee#tbrenayBmzxvp.S.tbAc7.m.Dcx.FcUBtvWBusfBv.jBw##.jctbq.EdldU#s.I.Kdkcicicicici.n.n.n.n.N.t.t.q.d.d.d.d",
".q.o.J.Q.rr8fbaEa7#7qi.s.r.o#a.J.o.K.P.O.O.o.O.Q.J.OBxi1bMfbaBc4.Q.P.O.odzbNg3#5qi.s.Q.0.Q.r.o.o.r.J.o.o.r#b.O.o.O.o.N.o#SByanj.Bzfn.p.N.o#f.N.o.N.o.K.os#a6cna7gWAZ.0.J#b.o.o.obj.oBAkRboBBBCkVg8g8y#BDi7.o.O.R.laxawcxau.D.d.T.U.t.EBE.GBFBGBHBIBJBKBLBM.8.FBNeIBOBPoWBQBRBSBTle.paw.p.p.J.s.s.sc6.e.eb9ct#l#woT.tBUsfeuc5BVc5wP.1ahahsf.obrzicV.k.a.ZBnbsBW.k.hBX.i.abrBY.vBpz4#z.v.o.8cX#vBZdFB0B1B2bB.i.napap.NcyzUcQcQB3B4ccB5B6.y.y.D.oB7B8B9C..H.o.yB2ALC#.nbHc.AWBU.Q.DeM.paqaqbEaqaq.N.N.M.L.n.p.t.qQtQt.d.d",
".q.o.O.J.oCaoLfbblaDba.P.s.J.r.P.s.J.s.J.o.o.o.r.P.ooHgUi1gU#E.Q.r.o.0.0vab2a7CbbT.O.Q.P.o.o.P.0.Q.K.P.J.s.r.s.s.o.o.q.oCcaea.a.CdCe.o.o.o.q.t.q.q.O.K.obQfbaDcltI.P#1.s.0.o.s.J.K#dajiOi1y#fytNg9scCfCgg5#1bj.oawcVbqcJc9Ch.D.l.w.q.EzUCiCjCkClCmCnCoCpCq.H#veywRCrCsCtCuCvCwvqaq#t#t#u#u.J.O.O.O.cQtavCxCyCz.VAV.RCAAXAXfAa1qyCBsg.yc7c7.J.o.M.lQtCC.e.inxCDBnCECFCG.eQtCH.o.p.9qzCI.RAAdZCJdZcKCKcy#lCICLbAfAg5.I.sCMCNCOCPCQCRQtQt.mCSCTnxqzd7CUAC#sCVCWCXCY.m.0CZAWdU.R.fnxBn.paqbEbEaqaq.N.N.L.n.N.p.t.qQtQt.d.d",
".q.Q.o.s.KiPwGi1bNbLoLcY#a#b.o.P.r.o.o.s.o.K.o.o.O#avdfbbNcnbJ#1.o.s.oAZfbiO#9a5C0AZ#a.O.P.Q.O.o.o.J.o.s#b.o.o.K.r.p.o.oC1aUzbC2C3ai.o.R.n.o.q.n.o.r.Q.0C4bnepa7qm.oc4.o.s.Jc4.K.otJfbcna7C5kYC6C7C8BBy.sd.Q.oc3.Law.tcwc7.D.r.Y.Y.wbC#tC9lJD.D#DaDbDcDdDe.GcUaYDfDgDhDiDjDkDlBM#t#tbE#u#u.J.J.O.OQtQt#lBYDmlZ.WfU#f.F.HDneEc9dJAuDoyvANChiX.Ic4.o.mDpDq.a.m.eDrDsDtCX#kDu#Dk7dT.oQt.e.r.GDvDwDxDyciDzDzDA.fjda1dCvy.B.FDBcMDCDD.E.dDEDF.m.mQtoT.pDGDHDI.HDJDK.mle.OAX#s.F.O.bDL.g.Nciaqaqcici.n.n.n.N.p.t.q.q.d.d.d.d",
".q.t.o.p.p.NDMBzepaDwODNi7.Ig5dQdjcIha.I.IDOfA.IDODPDQDRy#DSfs.I.I.I.IiXDTg8wNwOAa.s.t.p.o.n#f.o.N.oaX.o.o.n.o.o#f.L.o.tfoDUBzhdDV#e.p.t.N.o.o.N.o.o.Jk7b.iScn#9fl.P#a.o.P.o.oiUfrm0y.DRDWDXl.ftDYvjAeC8DZiXcx.Ibj.D.DChCh.B.qBmD0AwdxD1D2f1D3znD4D5D6lLD1bDD7D8vqD9E.E#EaEbEcEd.GAX.N.t.t.p.N.p.q.o.N.tEeEfEgEhcy#btNEiEj.BEkcuElEmEnEoiXm5EpdR.0tNgZ.Ii0EqqlErAaEsm4EtDNAdDNEtfxcp.OfAEuEvDn.HCVmQa4#EkM.shaEwExEiEyDO.FEzEAEB.rfrECEDjfEEEF.JEGEHEIEJDOfxEKdRDOoPELEMdB.IbjENqlEOEPEQ.L.R.NEREQESET#f.o.p.n.q.o.q.q",
".q.q.t.L.t.oEUEVhdaDAezfEWlecIdj.I.IdQa1.Ia1.B.I.IEXEYqtscvnEZ.Ihale.I.IE0E1zfk0E2gQ.L#f.o.o.n.q.t.o.t.L.LgQ.M.N.N.o.ngQE3E4gSa#E5ah.p.o.t.o.q.p.t.o.sE6m0gUclbKgZ#b.o#1.smQ.KcpbKE1C8kXEjfA.I.IqrE7AeC8iWE8cIft.I#X.D.D.D.r.Sd#E9F.cgaZhVF#D5FaFbFcFdFeFfeZFgeOf6FhFilBFjFkFlFmcXAX.N.t.t.t.t.q.o.pbZfnbdhfFnFo.NdAFpsdFqFpDOFrkVAgFsoPoPFtfx.IC6FuFvleFwFxqssdFyFym4FzqsDQEWqrFAm5ftFBFCC7m4fAhafyFDFpFEkYFFFGFHfyDQfycIfvDTFIFzFJm5cxkUFKFLEKELDWvkjbFMFNEK.IFyFOFsDJFPFQ.IBDsbFRFSFTFR.tFUFVFWA2FX.o.o.1.o.o.n.q.q",
".q.o.p.n.p.o.ufGFYbmdyaEa6FZ.J.P#a.o.s.J.s.r.o.s.PmZbNiOb3oFtG.o#b.O.s.Qk4dzfbbLbPfE.o.nhg.o.o.N.o.p.oes.1.q.t.t.o.o.p#NbXC2aPhkEP.L.N.o.o.N.p.o.N.P.obpa8g3bobkbT.oc4.O.o.oF0aCepcn#7ba#c.Q.r.rviqnbnfabLmX#c#a.J#k#k.D.D.r.Sd#d#d#bHF1F2F3F4F5FaF6F7F8bwF9cgG.vJG#GaGbGcGdGecv.GdY.N.t.q.t.q.q.o#f.RbcquaXgQ.oGfr5iPbjmRoGGgfic2.KcY.KqhzdGhbUkNa6k7.oGibKr4cktKba.KbU#4oH.obUaBoH.oF0iO#c.o#1C0bPr7.sc4.or9aBi0.rr6GjiUGkaCGimTGjmT.rGlA3kM.otJkPmQ.OmZ#4.sa4#5GmbUtGb.bJ.oGnoLGosfGpC3GqaQbeaR#dGr.N.o.u.o.t.o.q.q",
".q.o.o.p.p.L.o#eaogUaEaDb2fbGsc2i0#1.o.o.J.r.sckkNhccldzdzgWbU.obj#a.o.QiPfhc0bMb2#QGt.N.o.p.L.R#d#gGuGvEQGr.L.N.u#f.osaafAczbhjGw.q.n.o.o.L.N.o.N.r.sGxaI#8aItI.K#a.o.JbjGleqvacnclz.c3.Obj.o.0#bGy#6epepbox3.sc4.c.e.e.D.q.Sa2a2.x.HezfQGzGAGBGCGDGEhKbwGF#tGGGHGIGJGKGLGMGNfOAP.J.p.t.t.t.t.t.t.q.oaoGObY#f#NGPbahcbPwKa4gYffcY.o.r.rCaGQcj.Qs#k5.ObjCaGRGh.obaBx.o#aGjqm.0.obJtF.OtPi8bU.s.o#ahcb1Gm.PF0mXwI.OckGhbKGSi2c1bTc2b.i0.PqhGnE6.oGTE2.0.sbQb#.rkPqk.Q.o.rb4E2erGnr8.o.1DVDV.nEOFTGU.o.o.u.o.q.t.L.o.q.q",
".q.q.o.p.o.N.t.oGVoHepbmaE#9bLc0bKtFbQGWbRGWoHfjaDbloJ#6fagV#A#a.r.O.r#1.obRaD#9boabanaWE5gRCcgRGXzcj.GYDV.L.t.o.osf.oERGZa#zbG0Go.o.L.q.o.L.N.o.p.si0mRbLm0dzkK.P.rbj.o.KtIaHdyfbiRoI.O.r.s.o#1.oiUGnfbdyb2Gs#b.o#l#l.e.e.q.t.9.9dUG1cvG2G3G4G5G6G7lWG8bxAh.GG9H.H#HaHbHcHdHeHfAA.t.t.t.t.p.p.N.n.o.o.nGwFYfnHgFYvdHhGgbj#bi8FZ.Q#a.OcYoGoH#a.ogWb#.o.Px3oM.PckhcbR.oC0tPoI#a#b#3iTwIb1#a.KmQ#bbUcYoGoLflGWGQkN.r.svgGQiUcZwK.sEGHhbU.otI#FiUGhaBqm#A#aHir7bUwGk3.J#atGx5kKGiaBcr.p.qHjza.o.qHkHjwMhg.q.o.o.t.o.N.q.q",
".q.o.q.N.o.o#f.u.Ni0#3A3a6b2blfadzblvavbbOaIx4bLiO#9bMdzgXGg.Q.J.o.o#Ac3.o.JcZqjcli5a#A1aKbgalbghiA1aMaTHlA0#N.t.o.L.tHmi5A1aJC3Gq.q.n.p.q.p.p.q.q.ObS#5aFcldycr.K.Q.P.Qhcz#iOclm1i6.o#A.Q.J.o.K.oiUkTg3bLbNdzvh.n.h.h.c.e.t.t.9.9.FeAcvhAHnHoHpHqHrF2ua.8Dy.GHsHtjCHuHvHwHxeCaZci.t.t.p.p.p.p.n.L.pA0.NA0HyHzGoj.ve.JiUbTbUGTkRvf#A#A#aGnfkmTk4m0r6.sbjC4mR.JGgqnkM.sbJ#5GS.o#aGiC4oLr3.s.P.o.Ock.sGhbKs#iMbPflviiQfhgV.oGsmR.JHhaBkNs.A3iT.JC0sbr3.ockoLi3.0AYGQAZi0r6b1gZGSwGvf#ff.C3GoaRGr.qHAaWGV.o.o.q.N.o.n.q.q",
".q.o.p.q.q.o.psf.u.o#aGyHhfjg2#7bMa7aFfagXaEiObMg3a9HBr9HCAZ.K.P#a.P.o.obU.o.0qmGsj.aVi5aTi4m6a#GPhebeHDqo.u.o.o#N.o#N#Km6DUaaHEaX.t.p.n.p.o.p.L.q.oiMoF#8dywHGi.o.s.0kKA#gXqjb3r3.s.0.o.o.r.o.o.r.rtGgW#8a9aDk3Fo.h.h.c.e.9.9.9.9.F#vDfHFHGHHHIHJHKybey.H.F.HHLHMHNHOHPHQHRHSdGcd.t.p.N.p.t.q.p.N.qx6#KHTHUeo.NGfwKkQkQkM.PGSHikPAYgY.sbRA3bacZfjk4.KbUGnkT.rvhwGve.JGyoKkQdB.obUwHCbbU.Oi0.K.0bRk3tItIql#ahcdAl#qkb4bjc4qkc2.o#3k5cok3mVr8#bmWg0x5GkoIk6iQ.JqhGsffwJr9HV.oHW#4#A.LHXHY.RhgGvFWoNfD.L.L.q.o.M.o.o.q.q",
".q.o.N.o.u.1.o.N.1c3.o.r.scqx3HZqnqnkRg0mVeqHioGr3GWgZcY.o.K.s.J.o.o.P.s.K.J.oc3GibWbcquoNhlhfqu#JH0hmGq.o#N.L.p.n.o.ufpH1#LESx6.n.p.o.n.n.o.N#f.q#ac3vgkKr5kTc4.J.PAZkMfkwIgYs#AZ.ObU.o.obj.K.s.O.s.KH2r3r6vg#3#f.i.a.c.e.9.9.9.9dU.HcuH3H4H5H6H7H8eydGAXaq#vfNH9I.I#IaIbIcHL#tcfaw.N.N.p.o.o.q.t.LGo#KDMId.M.nbZvgFZaAoI.o.0i2cooGcrc3.ovgl#cpi2AZ.K#1FZcY.odBGm.0.Q.0#3vgbU.OHW#5k4.P.K.o.objqlEGEGC0.o.J#A#Dl#x3vi.o#1s#b5.0.raAr7Caa4vf.o.ok4FZC0i0bpAZ.P.OCafkmZk4.o.JCaGg.K.o#jfmGrIeIfIgfChg.o.n.o.o.o.q.o.q.q",
".o.o.q.p.n.L.L.L.L.e.c.c.a.b.#CCIhIiDsIjIkIlIiDpCL.c.a.i.i.i.i.a.c.c.c.c.c.c.c.c.c.aImInIoIpIqIh.a.b.i.c.e.d.d.e.cIh.g.c.a.#.f.iQt.i.a.eQtQt.e.a.i#kIrIsIsIrc6eMDq.m.DbzeMIrDqDqDqQt.a.cQtQt.c.aQt.a.e.d.a.#ItCC.#.bc6.O.t.9.9axax.9.pIuIvIwIxIyIzBMbybEeibGdkIAIBICIDIEIFIBb7ceIG.l.o.q.p.n.M.u#f.t.o.p.R.R.n.t.n.L.L.L.n.n.N.N.p.N.N.p.p.p.N.L.Msf.N.n.1.n.q.p.N#e.o.N.M.o.MfGGvIHCLQt.f.aQtQt.iCCQtQt.f.#Qt.bIl.o.N.1.1.L.p.p.N.q.R.p.N.N.p.R.q.g.c.a.f.f.a.c.g.#.b.a.e.e.a.i.g.a.a.a.i.b.g.#.#.b.i.c.e.d.d.e.e.o.o",
".o.o.q.p.N.n.n.n.N.a.a.a.a.a.a.i.i.d.a.g.#.aQtQtQt.e.c.a.i.i.a.c.e.c.c.c.c.c.c.c.c.f.g.eQtQtQt.a.f.g.b.i.a.c.c.a.i.#.i.e.c.i.b.cQt.c.e.dQtQt.d.e.c.mbzeMeMbz.D#kbAbzbAc6eMeMc6bAbA.c.b.iQtQt.i.b.c.f.g.a.a.b.b.c.dc6bA.J.t.q.9ayax.w.l.odjIIIJIKeJILbI.xa2bC.FaZfOF8BTBTlJa1bED0IGax.p.p.p.p.N.N.N.p.o.p#f.1.n.p.n.n.n.n.N.N.p.p.p.n.n.N.N.N.L.M.u.u.o.t.M.p.o.p.N.o.oGr.p.RIeIMIfIq.d.#.aQtItItQt.b.i.i.g.a.d.aCC.N.N.n.L.L.n.N.N.q.1.p.N.N.p.1.q.b.e.c.g.g.c.e.b.g.b.a.c.c.a.i.b.a.a.a.i.i.b.g.#.i.a.c.d.d.d.d.e.o.o",
".o.o.q.t.p.N.p.p.t.c.c.c.c.e.dQtQt.cQt.c.#.bQtQt.i.d.e.c.c.c.c.e.d.c.c.c.c.c.c.c.c.d.a.b.g.i.c.d.d.i.a.c.e.e.e.e.c.c.e.d.d.e.e.dQt.a.c.c.c.c.c.c.a.D#kbzbz#k.D#k#kbAbAc6c6bAbz.D.D.a.b.i.e.e.i.b.a.a.e.d.e.a.i.a.e.Oa1.s.q.q.S.Yayd.axaw.n.Khacu.Bc5cVBmaxaw.oaueD#YINc8c7.OIOIPcCcV.N.p.p.t.q.q.q.p.q.t.M.M.N.p.n.N.N.p.p.t.t.t.t.n.N.N.p.N.n.L.M.M.o.t.M.N.p.L.L.q.o.N.o.oGraRahQtQt.g.iQt.i.g.#Qt.g.f.c.d.a.aQt.u.N.q.q.N.L.n.p.q.u.p.p.p.p.u.q.a.d.e.i.i.e.d.a.i.i.a.a.c.c.a.a.a.a.a.a.a.i.i.b.a.c.e.dQtQtQt.d.o.o",
".o.o.q.q.t.t.t.q.qQtQtQt.d.d.dQtQt.e.d.e.i.i.d.e.gQt.d.d.e.e.d.dQt.e.e.e.e.e.e.e.e.e.c.c.e.e.d.d.d.e.d.dQtQtQtQtQtQtQt.dQtQtQtQt.d.c.c.c.c.c.c.c.cbzbz#k#k#kbzbzbz.D.D#k#kbz#k#k#k.d.c.cQtQt.c.c.dQtQtQtQt.c.i.i.a.s.s.r.o.l.l.Y.Y.l.l.S.9.9awawbqdN#Tayax.t.o.Ia1dCdja1.q.9cA#VdP.S.q.q.q.q.q.q.q.t.o.q.N.N.t.t.N.t.t.t.q.q.q.q.q.t.q.q.q.q.t.p.p.n.o.t.n.t.t.L.nsf.t.L.R.n.o.t.tItQtQt.a.iQtQtItQt.a.bQtQt.a.aQt.L.t.o.o.t.N.N.t.q.N.p.q.q.p.N.q.c.d.d.c.c.d.d.c.e.c.c.c.c.e.e.d.c.c.e.e.e.e.e.c.e.e.dQtQtQtQtQt.o.o",
".o.o.o.o.q.q.o.o.oQtQtQt.d.d.d.dQtQtQtQtQtQtQtQtQtQtQtQt.d.dQtQtQt.d.d.d.d.d.d.d.d.cQtQtQtQtQtQt.e.e.d.d.d.d.d.d.dQtQt.dQtQtQtQt.dQtQtQtQtQtQtQtQt#k.m.m.m.m.D.D.m.m.m.m.D.D#k#k#kQtQtQtQtQtQtQtQt.d.dQtQtQtQtQtQt.q.q.o.l.l.w.l.lQtQtQtQt.j.j.v.v.v.v.jQt.m.m.m.mQt.T.v.v.v.v.v.j.o.o.o.o.q.q.q.t.q.o.o.o.q.o.o.t.q.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.q.o.o.q.o.o.q.o.o.o.o.o.o.o.p.tQt.cQtQt.a.eQtQtQtQt.dQtQt.d.e.d.q.o.o.o.o.q.q.o.o.o.t.o.o.t.o.o.eQtQt.d.dQtQt.eQt.d.d.d.dQtQtQt.d.dQtQtQtQtQtQt.d.dQtQtQtQtQtQt.o.o",
".o.o.o.o.o.o.o.o.oQtQtQtQtQtQtQtQtQt.a.cQtQt.c.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.i.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.dQtQtQtQtQtQtQtQt.D.m.m.m.m.m.m.m.D.D.m.m.m.m.m.mQtQtQtQtQtQtQtQt.e.d.dQtQtQtQtQt.o.l.l.w.w.w.l.obziyiy#X.m.j.v.U.v.jQt.m.y.y.m.d.v.CIQ#W.v.j.Dbz.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.q.o.o.q.o.o.q.o.t.M.q.o.o.L.t.oQt.aQtQtQtQt.eQt.eQtQtQtQtQtQt.d.o.o.q.q.o.o.o.o.o.o.t.o.o.t.o.o.dQtQtQtQtQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.o.o",
".o.o.o.o.o.o.o.q.q.d.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.d.d.d.d.d.d.d.d.m.D.D.D.D.D.D.D.D.D.m.m.m.m.m.m.dQtQt.d.dQtQt.dQtQtQtQtQtQt.d.e.l.w.w.Y.Y.S.d.m.y.z#x.z.y.m.j.T.T.d.DChateH#Y.e.v.7.W.7.vQt.y.y.r.q.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.o.q.q.q.q.o.o.o.t.o.q.t.o.q.N.o.o.o.o.q.o.N.o.o.d.aQt.eQtQt.c.a.dQtQtQtQtQtQtQt.o.o.q.o.o.o.o.q.t.o.p.o.o.p.o.tQt.dQtQtQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.o.o"
]
image1_data = [
"300 322 694 2",
".x c #000000",
"dz c #000002",
"dy c #000100",
"dx c #010000",
"iT c #010002",
"ho c #010100",
"#p c #010101",
"eo c #010103",
"hp c #010302",
"e7 c #020001",
".P c #020202",
"ek c #020204",
"en c #030104",
".W c #030303",
"iW c #030305",
"e9 c #030406",
"iG c #040203",
".C c #040404",
"gI c #040406",
"#o c #050505",
"gV c #050507",
"hl c #05060a",
"hg c #060604",
".O c #060606",
"hE c #07060b",
".D c #070707",
"#b c #080808",
"in c #08090e",
".X c #090909",
"f# c #090a0e",
".J c #0a0a0a",
"#n c #0b0b0b",
"hW c #0b0b0d",
"#c c #0c0c0c",
"fJ c #0c0d0f",
"#C c #0d0d0d",
".6 c #0e0e0e",
"#h c #0f0f0f",
"#4 c #101010",
"hV c #101420",
"ae c #111111",
"gl c #111320",
"#P c #121212",
"eb c #121622",
".5 c #131313",
"bh c #141414",
".w c #151515",
"#g c #161616",
"iH c #16192a",
"io c #171425",
".I c #171717",
"dB c #17192e",
"#X c #181818",
"gk c #181b2c",
"a. c #191919",
"em c #191e32",
"hS c #191e34",
"#1 c #1a1a1a",
"au c #1b1b1b",
"dY c #1b1e2f",
"he c #1b2036",
"#D c #1c1c1c",
"eD c #1c1e35",
"ar c #1d1d1d",
"dW c #1d213a",
"aE c #1e1e1e",
"aO c #1f1f1f",
"ib c #1f253d",
"bn c #202020",
".V c #212121",
"b. c #222222",
"ep c #222744",
"#a c #232323",
"dj c #232740",
"ic c #232943",
".K c #242424",
"bj c #252525",
"aX c #262626",
"aB c #272727",
".r c #282828",
"hm c #282d4d",
"#H c #292929",
"fI c #292e4e",
"ej c #292f51",
"#s c #2a2a2a",
"aZ c #2b2b2b",
"bG c #2c2c2c",
"dk c #2c3256",
"b# c #2d2d2d",
"aR c #2e2e2e",
"eE c #2e3359",
"hf c #2e3458",
"aC c #2f2f2f",
"fK c #2f3130",
"hU c #2f3559",
"at c #303030",
"f1 c #30385d",
".B c #313131",
"bC c #323232",
"bb c #333333",
"dl c #333a64",
"bm c #343434",
"#d c #353535",
"dm c #353a64",
"g6 c #353c66",
"#5 c #363636",
"dZ c #363f6a",
"bu c #373737",
"iI c #37406b",
".s c #383838",
"hR c #38406f",
"#9 c #393939",
"iX c #3a3839",
"aI c #3a3a3a",
"am c #3b3b3b",
"di c #3b3b47",
"#i c #3c3c3c",
".4 c #3d3d3d",
"by c #3e3e3e",
"a2 c #3f3f3f",
"g5 c #3f467a",
"aj c #404040",
".Q c #414141",
"e# c #414b7e",
"ad c #424242",
"ab c #434343",
"iV c #434345",
"dn c #43496d",
"a5 c #444444",
"#x c #454545",
"gU c #454e6d",
"dC c #454e85",
"a8 c #464646",
"bl c #474747",
"fH c #475089",
"aK c #484848",
"f2 c #48518c",
"#W c #494949",
".7 c #4a4a4a",
"aT c #4b4b4b",
"fG c #4b5175",
"hD c #4b5592",
"av c #4c4c4c",
"ei c #4c5691",
"f. c #4c5693",
"#B c #4d4d4d",
"f0 c #4d568d",
"dc c #4d578a",
"#m c #4e4e4e",
"ec c #4e5896",
"ip c #4e5997",
"iJ c #4e5a96",
"b4 c #4f4f4f",
"bX c #505050",
"ea c #505b9b",
"bR c #515151",
"hC c #515c9e",
"aF c #535353",
".8 c #545454",
"dd c #545fa1",
"aJ c #555555",
"hd c #5564a9",
"#O c #565656",
"#t c #575757",
"e. c #575c84",
"iF c #5761a8",
"#0 c #585858",
"#q c #595959",
"hB c #5967a8",
"a4 c #5a5a5a",
"cW c #5a65a7",
"c4 c #5a66ae",
"hn c #5a66b0",
"dt c #5b5b5b",
"dV c #5b67b1",
"dD c #5b69b2",
"aP c #5c5c5c",
"c7 c #5c68b2",
"gj c #5c6ab3",
"a0 c #5d5d5d",
"iK c #5d6bb6",
"bO c #5e5e5e",
"d# c #5e68b0",
"e6 c #5e6bb9",
"#Q c #5f5f5f",
".v c #606060",
"cT c #606dbb",
"eC c #606dbc",
"bi c #616161",
"de c #616ebc",
"fa c #626061",
"bJ c #626262",
"hk c #626683",
"id c #6272c0",
"br c #636363",
"el c #6370bf",
"gH c #6372c3",
"dE c #6373c1",
"dA c #6374c4",
"hT c #6374c6",
"dw c #646464",
"cF c #6473c4",
"fv c #6473c6",
"fR c #6474c2",
"ck c #6475c5",
"e8 c #6475c7",
"ag c #656565",
"cL c #6572c0",
"cl c #6574c5",
"cB c #6574c7",
"cv c #6575c3",
"gz c #6576c6",
"bQ c #666666",
"h# c #6672c4",
"cu c #6675c6",
"ee c #6675c8",
"cK c #6676c4",
"gy c #6677c7",
"h3 c #6677c9",
"bM c #676767",
"c1 c #6773c5",
"im c #6773c7",
"dX c #6774c3",
"dK c #6776c7",
"g9 c #6776c9",
"fg c #6777c5",
"d1 c #6778c6",
"ai c #686868",
"e5 c #686b7a",
"g8 c #6874c6",
"ig c #6877c8",
"iR c #6878c5",
"eK c #6878c6",
".Y c #696969",
"d2 c #6975c9",
"fN c #6979c7",
"az c #6a6a6a",
"eA c #6a76c8",
"fo c #6a77c6",
"#I c #6b6b6b",
"c0 c #6b75a8",
"iP c #6b78c7",
"bU c #6c6c6c",
"d0 c #6c77b7",
"ed c #6c79c7",
"dL c #6c79c8",
"aq c #6d6d6d",
"iq c #6d7ac8",
".H c #6e6e6e",
"d6 c #6e7bc9",
"d3 c #6e7ecb",
"bY c #6f6f6f",
"cj c #6f7cca",
"dJ c #6f7dc8",
"bT c #707070",
"gG c #70727f",
"eN c #707dcb",
"cU c #707dcc",
"bq c #717171",
"cM c #717ecc",
"ff c #717fca",
"ik c #7181cc",
"bs c #727272",
"iy c #727fcd",
"fh c #7280cb",
"an c #737373",
"e0 c #737fcb",
"eS c #7381cc",
"a9 c #747474",
"fn c #7482cb",
"bf c #757575",
"iz c #757ecb",
"dM c #7583cc",
"## c #767676",
"hZ c #7682cc",
"aA c #777777",
"il c #7783cd",
"cw c #7788cd",
"bW c #787878",
"cE c #7884cc",
"dQ c #7884ce",
"d5 c #7884d0",
".U c #797979",
"ct c #7985cd",
"ij c #7987d0",
".n c #7a7a7a",
"gM c #7a86ce",
"gZ c #7a86d0",
"as c #7b7b7b",
"cJ c #7b86c8",
"eY c #7b87cf",
"hy c #7b88cc",
"gJ c #7b88ce",
"#U c #7c7c7c",
"fB c #7c89cf",
"bL c #7d7d7d",
"hx c #7d8ad0",
"eT c #7d8cd1",
"dv c #7e7e7e",
"df c #7e89cb",
"fu c #7e8bcf",
"bS c #7f7f7f",
"dU c #7f8295",
"hj c #7f89d0",
"iL c #7f8acc",
"eh c #7f8cd0",
"aM c #808080",
"d. c #8087b1",
"iv c #808acf",
"#6 c #818181",
"dI c #818bd0",
"#3 c #828282",
"c6 c #8289b3",
"er c #828cd1",
"cm c #828dcf",
".E c #838383",
"ci c #838ed0",
"iD c #8391d2",
"#V c #848484",
"cX c #848fcf",
"fe c #848fd1",
"#j c #858585",
"ie c #858fd4",
"iS c #8590d0",
"ir c #8590d2",
"a6 c #868686",
"fX c #8691d1",
"aU c #878787",
"#8 c #888888",
"bp c #898989",
"fi c #8992d3",
"dN c #8994d2",
"ft c #8997d4",
"#w c #8a8a8a",
"gD c #8a95d3",
".q c #8b8b8b",
"fU c #8b95d3",
"eR c #8b96d4",
"hz c #8b97d3",
"ac c #8c8c8c",
"fS c #8c96d4",
"#f c #8d8d8d",
"fm c #8d97d4",
"g4 c #8d97d5",
"aN c #8e8e8e",
"e2 c #8e96d4",
"gL c #8e9ad6",
"b0 c #8f8f8f",
"gE c #8f99d4",
"bD c #909090",
"h. c #909ad5",
"hG c #909ad7",
"fP c #909ad8",
"eg c #909cd6",
"af c #919191",
"g7 c #919bd6",
"gQ c #919dd7",
"be c #929292",
"ew c #929cd7",
"ax c #939393",
"gr c #939dd8",
"bF c #949494",
"ht c #949dd8",
"ga c #949fd5",
"eP c #949fd7",
"bA c #959595",
"iE c #959ed5",
"dq c #969696",
"ih c #969fd8",
"al c #979797",
"fb c #97a0d7",
"fC c #97a0d9",
"fW c #97a2da",
"#M c #989898",
"f7 c #98a1da",
"aG c #999999",
"gC c #99a0d7",
"hq c #99a2d9",
".N c #9a9a9a",
"hc c #9a9b9d",
"iB c #9aa3da",
"aH c #9b9b9b",
"cQ c #9ba2cc",
"gd c #9ba5d8",
"gm c #9ba5da",
"hv c #9ba7db",
"#y c #9c9c9c",
"eJ c #9ca5dc",
"cH c #9ca6d9",
"d9 c #9ca6db",
"f6 c #9ca8dc",
"ds c #9d9d9d",
"c3 c #9da3c3",
"dH c #9da7dc",
".9 c #9e9e9e",
"cn c #9ea5d9",
"iu c #9ea5db",
"gK c #9ea8d9",
"ch c #9ea8db",
".3 c #9f9f9f",
"eF c #9fa1ae",
"iA c #9fa6dc",
"#l c #a0a0a0",
"dg c #a0a7db",
"hA c #a0a8d9",
".A c #a1a1a1",
"i. c #a1a8dc",
"gs c #a1a9da",
"bI c #a2a2a2",
"bx c #a3a3a3",
"a# c #a4a4a4",
"iw c #a4abdf",
"d8 c #a4acdd",
"aQ c #a5a5a5",
"hN c #a5addc",
"eU c #a5adde",
"#A c #a6a6a6",
"cS c #a6acd0",
"dO c #a6aedd",
"aD c #a7a7a7",
"gS c #a7addd",
"fp c #a7afdd",
"hO c #a7afde",
".m c #a8a8a8",
"h9 c #a8b0df",
"h0 c #a8b3e0",
"bV c #a9a9a9",
"hP c #a9b1df",
"#u c #aaaaaa",
"gT c #aab2e0",
"dr c #ababab",
"fE c #abb3e1",
"bP c #acacac",
"cO c #acb3dd",
"ay c #adadad",
"fF c #adb6e1",
".o c #aeaeae",
"cs c #aeb5df",
"eX c #aeb5e1",
"ba c #afafaf",
"hQ c #afb6e0",
"fj c #afb6e2",
"hw c #afb8e1",
"aY c #b0b0b0",
"fr c #b0b7e1",
"cP c #b0b7e3",
"f5 c #b0b8df",
"bo c #b1b1b1",
"ix c #b1b8e2",
"#E c #b2b2b2",
"hX c #b2b5be",
"db c #b2b7d4",
"c# c #b2b9e3",
"cx c #b2bae1",
"aS c #b3b3b3",
"cR c #b3bae4",
"ii c #b3bae6",
"h6 c #b3bbe0",
"fl c #b3bbe2",
"a1 c #b4b4b4",
"cC c #b4b9e3",
"fs c #b4bce3",
"hr c #b4bde4",
".u c #b5b5b5",
"g3 c #b5bde4",
"ao c #b6b6b6",
"gn c #b6bbe3",
"hi c #b6bee3",
"is c #b6bee5",
".L c #b7b7b7",
"ge c #b7bfe3",
"h1 c #b7bfe4",
".t c #b8b8b8",
"d7 c #b8bde3",
"it c #b8c0e5",
"bZ c #b9b9b9",
"h8 c #b9bee4",
"bk c #bababa",
"fO c #babfe5",
"cN c #bac0e4",
"#Z c #bbbbbb",
"fx c #bbc0e6",
"hH c #bbc0e8",
"ca c #bbc1e5",
"#2 c #bcbcbc",
"fD c #bcc1e7",
"c. c #bcc2e6",
".0 c #bdbdbd",
"fw c #bdc1e6",
"f4 c #bdc3e7",
"aL c #bebebe",
"dT c #bec2e5",
"fd c #bec4e8",
"#G c #bfbfbf",
"f9 c #bfc3e8",
"gu c #bfc5e7",
"ah c #c0c0c0",
"ha c #c0c4e7",
".G c #c1c1c1",
"gv c #c1c7e9",
"bv c #c2c2c2",
"co c #c2c7e4",
"ef c #c2c7e7",
"bK c #c3c3c3",
"dh c #c3c8e6",
"fQ c #c3c8e8",
"gR c #c3c9e9",
"#e c #c4c4c4",
"cg c #c4c9e7",
"bg c #c5c5c5",
"es c #c5cae8",
"cD c #c5cbeb",
"a3 c #c6c6c6",
"eq c #c6cbe9",
"#7 c #c7c7c7",
"#z c #c8c8c8",
"fM c #c8cbea",
"iM c #c8cdea",
"dS c #c8cdeb",
"du c #c9c9c9",
"e3 c #c9cdea",
"gY c #c9ceeb",
"bB c #cacaca",
"#k c #cbcbcb",
"gF c #cbcfe8",
"hY c #cbcfec",
"eI c #cbd0ed",
"cb c #cbd1e9",
"aW c #cccccc",
"do c #ccd0e9",
"bd c #cdcdcd",
"dG c #cdd1ec",
"eZ c #cdd3ed",
"bt c #cecece",
"cY c #ced2ed",
"#. c #cfcfcf",
"b9 c #cfd3ee",
"g0 c #cfd5eb",
"ak c #d0d0d0",
"e1 c #d0d4ed",
"cV c #d0d4ef",
"gN c #d0d5eb",
"#v c #d1d1d1",
"if c #d1d5ee",
"gw c #d1d7ed",
"a7 c #d2d2d2",
"gW c #d2d6ef",
"g2 c #d2d7ed",
".T c #d3d3d3",
"gB c #d3d7f0",
"g# c #d3d8ee",
"#Y c #d4d4d4",
"fY c #d4d6ef",
"i# c #d4d9ef",
"#r c #d5d5d5",
"fZ c #d5daf0",
"#T c #d6d6d6",
"bw c #d7d7d7",
"gt c #d7dcf0",
"#K c #d8d8d8",
"go c #d8ddf1",
"#L c #d9d9d9",
"ap c #dadada",
"hJ c #dadbf0",
"bE c #dbdbdb",
"gX c #dbddf2",
"aa c #dcdcdc",
"dR c #dcdff2",
".1 c #dddddd",
"iC c #dde0f3",
"bN c #dedede",
"iO c #dedff3",
"iQ c #dee1f2",
".Z c #dfdfdf",
"fq c #dfe2f3",
"bc c #e0e0e0",
"h2 c #e0e1f3",
"f8 c #e0e3f4",
".y c #e1e1e1",
"hM c #e1e2f4",
"fV c #e1e4f5",
".R c #e2e2e2",
"eV c #e2e4f3",
".p c #e3e3e3",
"gb c #e3e6f5",
"f3 c #e3e7f3",
".M c #e4e4e4",
"hI c #e4e6f5",
"cG c #e4e7f0",
".2 c #e5e5e5",
"hF c #e5e7e6",
"gx c #e5e7f6",
"cy c #e5e8f1",
"hK c #e5e9f5",
"#S c #e6e6e6",
"aw c #e7e7e7",
"ex c #e7e9f6",
"c2 c #e7eaf3",
".j c #e8e8e8",
"dp c #e8e8f4",
"cc c #e8eaf6",
"ev c #e8eaf7",
"ia c #e8ebf4",
"bH c #e9e9e9",
"fc c #e9ebf7",
"c8 c #e9ecf5",
"cp c #eae8f5",
"#N c #eaeaea",
"cZ c #eaecf8",
"#F c #ebebeb",
"et c #ebedf9",
"b8 c #ebeef7",
"h5 c #ebeff8",
"eH c #eceaf5",
"aV c #ececec",
"cf c #ececf6",
"cA c #eceff8",
"bz c #ededed",
"eB c #ededf7",
"cr c #edf0f9",
".z c #eeeeee",
"g. c #eeeef8",
"eQ c #eef1f8",
".i c #efefef",
"fA c #f0eef9",
".F c #f0f0f0",
"gp c #f0f0f8",
"fz c #f0f0fa",
"#R c #f1f1f1",
"fk c #f1f1f9",
"#J c #f2f2f2",
"gO c #f2f2fa",
"g1 c #f3f2fa",
".k c #f3f3f3",
"hL c #f3f3fb",
"gP c #f3f4f9",
"eM c #f3f6fb",
".S c #f4f4f4",
"h7 c #f4f4fc",
"ez c #f4f5fa",
"fL c #f5f4f9",
".l c #f5f5f5",
"gi c #f5f6fa",
"gg c #f5f6fb",
"c5 c #f6f4f5",
"gh c #f6f5fa",
".f c #f6f6f6",
"gq c #f6f7fc",
"da c #f6f8f7",
".d c #f7f7f7",
"eW c #f7f8fc",
"d4 c #f8f7fc",
".h c #f8f8f8",
"hs c #f8f8fa",
"h4 c #f8f9fb",
"gf c #f8f9fd",
"cq c #f8faf9",
"hu c #f9f8fd",
".c c #f9f9f9",
"hh c #f9f9fb",
"eG c #f9fafc",
"dP c #f9fafe",
"cd c #fafaf8",
".g c #fafafa",
"cI c #fafafc",
"gA c #fafbfd",
"hb c #fafcfb",
"iZ c #fbf9fa",
"e4 c #fbfbf9",
".b c #fbfbfb",
"eu c #fbfbfd",
"fT c #fbfcfe",
"dF c #fbfcff",
"iN c #fcfafd",
"ce c #fcfcfa",
".e c #fcfcfc",
"eO c #fcfcfe",
"gc c #fcfdff",
"iY c #fcfefd",
"iU c #fdfbfc",
"fy c #fdfbfe",
"c9 c #fdfdfb",
".a c #fdfdfd",
"b7 c #fdfdff",
"b6 c #fdfffe",
"ey c #fefefc",
".# c #fefefe",
"b5 c #fefeff",
"eL c #fefffd",
"b1 c #feffff",
"cz c #fffdfe",
"b3 c #fffeff",
"b2 c #fffffd",
"Qt c #ffffff",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#QtQtQtQtQtQtQtQtQtQt.aQtQtQtQt.bQtQt.#.#",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.b.c.aQtQt.#.#",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQt.d.eQtQt.#.#.#.a.#",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQtQtQtQtQt.aQtQtQtQt.c.fQt.#.#.#Qt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.g.aQt.#.#.a.#.#Qt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#QtQtQtQtQtQtQtQtQt.d.hQtQt.i.j.k.e.a.#Qt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.e.e.#.#.#.#.#.#.#.#.e.eQt.l.m.n.oQt.e.a.#Qt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.b.g.a.a.a.a.a.a.a.aQt.p.q.r.s.tQt.i.e.a.#Qt",
".aQtQtQt.#.eQt.#.#QtQtQtQtQtQt.#QtQtQtQt.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.#.eQt.#QtQtQt.a.e.aQt.e.h.eQt.cQt.e.u.v.w.x.v.yQt.b.#.e.a.#Qt",
".eQtQt.#.#Qt.#.cQtQtQtQt.a.c.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.aQt.#.eQtQt.b.gQtQt.#.#Qt.gQt.g.l.z.A.B.C.x.D.E.aQt.FQtQt.e.aQtQt",
"QtQtQtQtQtQt.#.#Qt.g.h.#QtQt.a.a.#.#QtQtQtQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQtQtQtQtQt.#Qt.gQtQtQt.#.g.e.aQt.c.G.H.I.x.J.x.K.LQt.f.#Qt.l.e.a.#QtQt",
"Qt.g.eQtQt.b.#QtQtQtQtQt.#QtQt.aQt.#.aQtQtQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.e.a.#QtQt.#QtQt.h.eQt.e.M.N.r.O.O.P.x.C.Q.R.lQt.#.S.eQt.bQtQtQtQt",
"Qt.a.b.b.gQtQt.c.cQtQt.h.hQtQt.hQt.a.b.e.#QtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.eQtQtQt.#.gQt.aQtQt.e.T.U.V.W.X.x.P.C.P.Y.lQtQt.a.bQtQtQt.bQtQtQtQt",
".f.bQt.#.c.h.Z.u.0.1.aQt.#.c.#Qt.a.e.e.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.aQt.a.f.d.#Qt.#.#.2.3.4.x.x.O.W.x.5.x.6.A.#.h.#.aQtQt.#.g.gQtQtQtQtQt",
"QtQtQt.g.dQt.g.y.7.4.8.9.pQt.#.#.c.b.aQtQtQt.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.#QtQtQt.d#.###a.P.x#b.X.x.x#c.x#d#eQtQtQtQtQtQt.g.a.#.#QtQtQtQtQt",
"Qt.cQtQt.b.bQt.aQt#f#g.x#h#i#j#k.f.gQtQtQt.#.b.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.j#l#m#n.x.x.O.x.x#o#p.J.x#q.2Qt.S.b.cQt.d.aQt.e.#Qt.#QtQtQt.#",
"QtQtQtQtQtQtQtQt.aQt#r#m.x#o.x#p#s#t#u.2QtQt.fQtQtQt.g.aQt.#.bQt.e.a.#QtQtQtQtQtQt.eQtQtQt.e.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQtQt.e.b.a.#.aQtQt.aQtQtQtQt.a#v###a.x.x#b.x.P.O.x.X.P.x.x#w.lQtQt.#.g.aQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.d.aQt.f.E#n.x.x#o.x.x#b#x#y#z.z.dQtQt.bQtQtQt.g.#QtQt.a.#QtQt.aQt.g.bQt.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQtQt.a.e.aQt.aQt.g.aQt.e.e.c.k#A#B.5.x.x.P.D#n#C#p.C.W.x.x#D#E#FQt.e.h.eQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQt.h.#.S.a#G#H#o.D.x.C.X.D.x.X#d#I#E#JQt.#.h.b.#.a.g.bQtQt.#.#QtQt.#QtQt.#.e.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.dQtQt.bQt.S.c.#.hQt#K.n.V#c.x#p.x.C#p.x.D.X.W#p.D.P#d#L.bQt.a.gQtQtQt.aQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQt.b#J.a.lQt.j.v.x.P.x.x.x.x.P.x.x.x.w#B#M#r.kQtQt.a.b.bQtQt.e.SQtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.b.bQt.#.h.h.e.SQtQt#N.o#O#P.x.x.x#p.x.x.x.x#p.x#C.P.C.x#Q#RQt.c.k.lQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.a.lQtQt.d.a.e.e#y.I.P.O.x.O.x.J.D.O#p.x.x.6.4.H.0#SQtQt.g.b.a.d.g.#QtQtQtQt.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.g.aQtQt.eQt#T#U#H.X.x.x.W.P.W.W.P.C#o#p.x.J.x.x#n#VQt.lQtQt.c.b.#Qt.b.#QtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQt.h#J.#Qt.c.cQt.#.Z#W.x.O.x.C.x.x.P.P#o.J#o.x.x.x#X#O#y#Y#J.aQtQtQt.b.h.#QtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQt.a.aQtQt#N#Z#0#C.x#n.x.x.D#p#o#b.C.x.x.x.x.P.x.D#1#2Qt.FQt#R.a.h.c.aQtQt.#.eQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.hQtQt.a.e.#Qt.lQt.#.g#3#4.x#p.X.x.O#o#p.x.x.x.D#c.x.x#o#P#5#6#7.lQtQtQtQtQt.e.#.#.#.#.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#QtQt.#Qt.R#8#9.P.x.x.x.x.P.C.x.x.x.x.x#p.D.O.P#o.x#i#vQt.iQt.a.aQtQt.b.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQt.a.eQt.a.hQtQtQt.#.bQt#G#9.x#p#b.O.P.C#b#p.x.x.x#p.C.P.x.x.x.xa.#0a#aa.bQt.e.e.a.a.a.a.a.a.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.e.e.e.e.e.e.eQt.h.u#Q.w.x.C.P#o.x.W.x.x.P.x.P.x.x.x#p#b.C.x.O.H.z.a.lQt.b.gQt.aQtQtQtQt.e.bQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.aQt.j.n.x.O.x.D.O.x.C.P.x.O.x.x#p#p.C.D.x.W.x.P.Iab#3#z.hQtQt.#Qt.a.b.g.eQt.aQt.#.#QtQtQtQt.g.bQtQtQtQt.e.#.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.#Qt.#.aQt.e.#QtQtQt.#.#.#Qt.h.eQt.bQt.a.zacad.X.x.P#o.O.C.x.C.P.x.x.x.x.x.x.x#p.P#n.xaeaf.e.b.g.c.b.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.l.gQt#F.u#X.O.x.x.x.P.x.P.x.x.x.C.C.C.D#b.O#p#p.x.x.x#C#1ag.m.j.aQtQtQt.e.e.aQtQtQtQt.#.lQtQtQtQt.a.#QtQtQtQtQt.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.h.bQt.#.gQtQtQt.eQtQtQt.#Qt.a.gQtQt#Jahai.5.D.x.x.D.O.C#o#p.W.x.x.x#p.x.x.x#o.x.x#o.x.s.G.#.e.e.b.b.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.dQtQt.a.R#m.x.W.O.W.P.x.x#p.x.C.C.x.x#p.x#p.P#o.C.x.x.x.P.xaeaj.qak.l.a.eQtQt.a.c.#QtQt.e.aQtQtQtQtQt.aQtQtQtQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.a.e.#Qt.a.bQtQtQt.#.#.#QtQtQtQt.a.yalam.D.x#p.P#p#b#n.P.x.P.x.x.x.x#o#o.P.x.x.W.x#c.x#O.M.e.a.a.a.e.e.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.eQtQt.b.b.a.gQtQt#w.J.P#C.x.C.P.x.x.x#p.W.x.W#o.C.W.P.P.P.P.W.x#p.O#o.x.x#5anaoap.hQtQt.#.h.aQt.#.b.b.a.#.#.b.#.#.#.#Qt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.#Qt.a.cQtQt.f.gQtQt.f#Zaqar.x.x.W.C.x.W.x.x#p.x.x.C.x#p.x.C.C.x.x.x#p.x.O.xas.bQtQt.g.a.#.a.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.e.#Qt.#Qt.#.d.cQt#eat.x#C.P.X.D.X.x.x.W#p#o.x.x.x.x.x#p.P.P.W.x.x.P.O#o.x.x.xauavaf#r.fQtQt.a.a.e.b.#.#.e.a.b.b.b.e.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.b.#QtQtQt.e.fQt.#.eQtQtawaxab.6.x.x#p.P.x.x.C.x.x.C.O#p.x.W.P.W#p.x.x.x.W.O.D#p#4ayQt.SQt.eQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.eQt.h#RQt.iaz.C.x.P.x#n#o.x.P.x#p.x.x#p.x.x#p.x.x.x.W#o#p.x.x.P.W#p.x.x.x#bataAao.i.cQt.a.g.f.h.#.c.g.b.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.aQt.e.d.aQt.cQt.g#7anaB.P.x.P.P.P.P#p#p#p.x#p.x.x.x.x.x.x#p.P#p.x.O.J.x.x.PaC.T.#.aQt.bQt.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQt.#.#QtQtQt.dQt.c.fQtQtaDaE#h.x.P.C.x#o.x.x.x.x#p.x.x.P.W#p#p.x.x.W.C.x.x.x.O#p.P.C#p.x.x.WaraFaG#r.hQt.e.#.b.e.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.b.c.gQtQt.h.iaHaI#b.x#p.O#n.W.W.x.x.x.C#o#p.P#p.x#p.W.C.P.x.x.W.W.D.W.x#XaJ.d.eQt.d.#Qt.kQtQtQtQtQtQtQt.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.b.#.a.b.gQt.#.e.a.cQtQt#SaK#h#p.x.x#p.x.x.x#p#p.x.x.x.x.x#p.P.P.P#p#p.x.x.W#p.D.X.C#o#b.W.x#p.x.6aI.UaL#J.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.#Qt.eQt.##7aM#X#b.x.x#o.W.x#p#p.x.x.W.P.x.x.x.x.P.C.x.x.x.x#p.x#o.W#p.xae#UQt.bQt.fQtQt.cQt.bQtQtQtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.#.aQt.#.h.a.a.caN.I.x.O.P.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x#o#p.x.W.x.OaOaPaQaw.g.eQtQt.#QtQt.#.#.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.b.a.#.aQt.hQt.e.e.a.#Qt#J.m#x.J.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.J.X.xaRaSQt.a.b.aQt.#Qt.g.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.hQtQt.f.cQtQtQt#7aT.x.P.X.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.C#o#p.x.W.x.x#o#p.x#b#iaU#eaVQt.gQtQt.g.eQt.a.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.bQt.fQt.fQt.h.bQtQtaW##aX.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.C#p#DaYQt.#QtQtQt.h.dQtQt.#.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.bQtQt.h#R#N#v#G.m.8#C.W.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x.x.x.C.P.x.x#b.D#o.P.x.WaZa0a1aa.cQtQt.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.b.SQt.pQt.bQt.i#Za2#g.x#p.J.W.x.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W#n.X.5.sasa3aa.aQtQt.g.fQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g#N.u#8ana4#dae#c.x.x.x.x#o#p.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x#p#p.x.x.W.W.x.W.P.x.P.P.x#p.xa.a5a6a7.d.c.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.b.##JQt.e#r#3#s.x#p.x.x.O#b.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x#o.P.x#o#p.x.Va8a9.G.f.e.#.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.Faxb..x.x.X.x.P.C.C.D#o.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x#p#p.x.x.P.P.x.C#o.P#p.x.x#p#cb##QaD.iQt.a.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.b.c.lba#x.5.x.x.O.P#c.X.x.x.O#b.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#n#o.x.W.C.x.x.xbbaoQt.c.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtbc#6.I.x#p.x#p#p.O.W.x.C.D.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x.x.x.W.P.x.x.P#p.x.x.x#1aP.Abd.iQtQt.#.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.bQt.jbb.x.W.P#o.P#p#p.x#o#o.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#b.x.x.W.D#p.x#b#Xbe#RQt.a.eQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.e.e.#Qt#Ybf#c#p.x#o.W#p.C.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.C#o#p#p#o.x.x#b.P#Cbb.Ubg.z.g.#.gQtQt.c.eQtQt.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.bQt.bayae.x.P.P#o.x.W.C#p.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x#n#p.x.O.xbhbiaw.#QtQt.aQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.aQt.c#..8.X.x#o.O.D.x.D.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.P.x.x#o.P#nbjaDap.a.#.bQtQt.aQt.e.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.a.b.dQtQt.H.x#4.x.W.x.x.x.x.x#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.P.P.P.P.P.P.P.X.x.J.D.xa2aoQt.d.aQtQtQt.#.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.eQtbkbl.P#p#o.x.J.x.x.x.x.x.W.O.x.x.x.x.x.x.x#p#p.x.x.x.x.x.x.x.x.P#p.x.x#p.W.O#bbf.ZQt.c.g.#QtQtQtQtQt.bQtQt.c.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.e.aQtQt.b.#.a.gQtaVbm.x#n.x.x.x.x.x.P.P#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P#p#o.C.x.x.x.J.P.D.xbnaH.lQt.g.b.e.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.e.fQtQtbo#5.P.O.x.x.C.x.x.C.x.x#o.x.x.x.x.x.x#p#p.x.x.x.x.x.x.x.x.P#p.x.x#p.W.C#o.x#1bp.bQt#RQtQtQt.fQtQt#J.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.eQt.hQt.bQt#z.D.x#p#p.x.x.x#p.P#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.6.x.x.J.D#n#p.x#nbq.jQt#J.fQt.e.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.cQt.bQt.dbe.K.D.x.O.W.x#p.C.x.x.x.x.x.x.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x#p#p.P.P.P.x#4#p#5aLQtQtQt.bQt.#.gQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.aQtQt.#Qt.#.eQt.dQtax.x#o#p.x.x.x#p.P#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.x.W.P.x.x.OaF#zQt.kQtQtQt.h.a.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.aQt.g.a.b.dQt.2aU#P.x.x#n.W.x.O#n.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p.x.x.x.W.x#o.C.Pbr.ZQtQt.g.hQtQt.k.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.#QtQtQt.#.e.c.#.h#RQt.a#ea..x.P#p.x.x#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.W.W.x.x.X#p.K#l.iQtQt.a.a.c.hQt.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.gQtQt.e.b.b.bQt#Faq.X.x.C.X.O.x#o#o.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x.X.x.x.C.x.V#w.S.c.aQtQt.hQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.e.f.fQtQt.k.3aX.x.C.W#p.x.x.x#p.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x#p.P.P.x.C#b.C#bbs.d.#Qt.l.eQt.#.aQt.b.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.e.dQtQtbtbi#n.x#o#c.O.O.C.P#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x#o.x#p.W.W.x.x.WbuaoQt.e.dQt.#.lQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQtQt.e.gQtap.7#b.x.P.W.C.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x#p.W.C.W.D.xa8btQt.SQt.cQt.#.dQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQt.c.bQtQt.f.l.b.#Qt.hQtQtbv#O#c.x.W.W.P#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.P.C.x.C.X.x.x.P#o#QbwQtQt.h.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.#QtQt.f.e#f#X.x.O.J.C.X#o.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x#p.C.C.xbn#A.b.eQt.a.e.b.aQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQt.e.dQtQt.#Qt.#.g.e.h.a.##E#i.x.x.x.x.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.P#p.x#p.x.C.W.x.xb..q.S.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.#.#.l.Rad.J.x.D#p.x.X.P#o.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x.P.C#o#6.2Qt.a.e.c.eQtQt.a.aQt.#.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.#.#.a.abxby.x#p.O.x#p.C.x.O#p.x.x.x.x#p.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.C.P.W.W.O.saQQtQtQt.gQtQt.#Qt.h.a.#QtQtQt.#.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.#.bQtQt.eQtQt.h.#Qt.#.fbe#P#p#p#p#p#p#p#p#p.x.x.x.x.x.x.x.x.P.x.W#p.C.x.x.x#b.x.P.J.x.xaPa7.#.#.#.a.a.a.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.aQtbzbA.K.x.C#C.x.X.W.W.D#o.C.W.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x#p.W.x.x.Vavap.#Qt.b.e.c.b.e.e.e.a.a.#.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.l.gQtQt.b.#QtQtbB#W#p.W#p#p#p#p#p#p#p#p.x.x.x.x.x.x.x.x#b.C.D.x.P.C.O.x.x.C.x.xbC.m.bQt.a.a.a.a.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.h.#Qt#JbD#X.x#c.x.C#o.P.x.P.P.x.x#p.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x.x#b.O.x.x.W.Ibe.zQt.g.f.g.#.c.gQtQt.#.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.g.eQtQt.c.c.e.b.#.c.qae.x.x.x#p#p#p#p#p#p#p#p.x.x.x.x.x.x.x.x.x.x#p.W.C.x.P#c.O.x#X#j.FQt.k.e.e.a.a.a.#.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#QtQt.l.lQt.e#Tbs#o.x.P.W#o.O.x.x.x#p#p#p.x.x.x.x.x#p#p#p#p#p#p#p#p.C.x.x.x.x.x.P#o.x.xbuba.#Qt.d.S.e.a.#Qt.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtQt.g.#Qt.bQt.TaK.x#o.x.x#o#p#p#p#p#p#p#p#p.x.x.x.x.x.x.x.x#p.O.x.x.O.C.P.x.W#Q#YQt.d.eQtQt.e.e.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.eQtQt.g.cQtQtbEa4#4.x.D.x.x.J.x.P#p#p#p.x.x.x.x#p#p#p#p#p#p#p#p.W.C#o#o.C.W.W.W.O.O.x#b#0btQtQtQtQtQtQtQtQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.fQtQt.b.kbF#h.x#h.O.X#o#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#b.D.x#obG.u#JQt.g.h.e.c.e.e.a.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.a.b.#.a.eQtQt#eaT.x.C#p.x.D.P.P.P#p#p.x.x.x#p#p#p#p#p#p#p#p.x.x.x#p.W.W.P.x.x.P.O.W.xbha9#R.c.a.a.g.gQtQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.SQtQt.cQtbd#B.x#h#p.P#b.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.O.x.x#D#6.lQt.c.b.#.hQtQt.d.a.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQtQtQtQt.#.aQt.hQt.baYbu#p.O.W.W.W.P#p#p.x.x.x#p#p#p#p#p#p#p#p.X#o#p.x#p.x.x#p.W.C.P.x.P#p.DaR#ebHQtQt.g.h.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.S.e.S#wbh.x#4#p.x#p.x#o.X.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.D#0.ZQt.c.gQtQt.eQt.h.cQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.#.#.gQtQt.a.#.#.bQt.dbI.B.x.W.W.P.P#p.x.x.x#p#p#p#p#p#p#p#p.x.x.x#p#p.x.x.W.W.x.x.P.P.D#p#p.xbJ#vQt.a.f.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtbK.Q.x.P.W.x#o.x.x#b.x.x.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x#p.xada7Qt.eQt.g.b.a.e.a.#.aQtQtQtQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.a.e.eQtQt.eQtQt.h.lQt.eQt.k.AaE.C#p.W.x#p#p.x.x.x.x.x.x.x.x.x.x.x.W.x.x.x.x.P.x.x.P#p.D.O.x#c.C.xae#6.iQt.c.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.l.eQt.g.gQt.aQt.f#3.D.W.C.x.D.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.W.W.W.W.W.P.O.x.x.J.xa.bIQt.#.gQt.e.#Qt.SQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.aQt.#.bQtQtQt.d.1ayaPbh.P.P.P.x#p.x.x.x.x.x.x.x.x.x.x.x#p#o.x.x#o.x.x.W.C.D.x.x.D#o.x.x.D.x.x.saSQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.g.bQtQt.h#e#9.x.O.x.x#n.x.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.D.x.x.x.x.x.x.x.x.x.x.x#n.x#bbL.dQt.d.d.e.hQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.f.gQtQt.aQtQt.dQt.i.tbLby#C#o.x#o.x.P.x.x.W#p.W.x.x.x.x.x.x.x.x.C.x.x.x.W.x.x.P.x.x.x#p#p#XaIa8bM##afa#ba#r.e.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.aQtQtQtbN.q.J#p.x#p#b#o.C.P.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x.x.P.C#p#p.C.x#b.P.W.x.x#c.xbO#TQt.bQtQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.a.e.z#TaFbj.x.x#o.x.x#p.x#p.D.P.P.P.x.x.x.x.x.x.x.x.x.x.x.x.C.C#p.xb.ai#6afbP#Y.R.2.d.#QtQtQtQtQt.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQt.e.cQt#KbQ.W#o.x#p.X.x.x.W.D.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.W#p.x.x#p#c.x.W.W#o#p.x#C.x#qbcQt.i.SQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.#.a.#QtQtbz.Gbsb..D#p.x.O.O#o.C.O.x.x.C#p#o.x.x.x.x.x.x.x.x.x.x.C.O.P.x#aai.2QtQtQtQtQtQt.h.kQt.a.SQtQt.b.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.l.c.a.lQt.a.1.ual##bRbj#4.X#p.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.C#p.x.C#o.C.x.x.O.x.x#p.J#x.N#LQt.g.bQt.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.#.eQtQt.a.cQt.cbKai.r#c.x.X#p.W.x.P#o.x.x.x.x.x.x.x.x.x.x.P.x.x.x.O.W.x.W#DaH.d.#.cQtQt#JQt.g.#QtQt.a.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQt.e.bQt.g.lQtQt.e.g.a.c#S.E#b.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.C#o.W.x.P#o.x.X#HbSbc.iQt.#.SQtQt.fQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtQt.#.b.g.eQt.c.bQtQt.SbkbfaE.D.x.x.x.P.P#p.x.x.x.x.x.x.x.x.x.P.D.W#o.X#p.x#p.xajbkQt.b.FQt.b.dQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.l.fQt.e.b.e.f.eQt.lQt.gax#X.x.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.P.x.x.x#n.P#1#IaL.cQt.kQtaVQt.g.dQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.a.eQtQt.eQt.g.aQt.e.g.#Qt.c.aaobT.B#o.x.x.x.x.x.x.x.x.x.x.x.x.x#o.C#p#o.W#o#b.P.x#oa0.ZQt.fQt.a.#.g.eQt.g.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#.g.c.#.a.g.a.a.SQtaw#0.C.x.C.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.P.O.x#p.V#WbP.iQtQt.#.lQt.#Qt.fQtQt.fQt.#.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.##F.L.Ybn.x.C.x.x.W#o.x.x.W#p.W#p.x.x#o#o#p#o.C.C#p.xaEa6.cQt.c.eQt.a.a.#Qt.aQtQt.#Qt.a.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.cQt.b.cQtQt.b.cQtaLbu.x.x.x#p.O.x.x.P#b.x.x.W.O#p.x#p.x#p.W.x.x.O.x.Oa2be.p.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.bQtQt.y.0#tat#b.x.x.C.W.x.C.x.x.W.O.P.x.x.x.x.x#p.x#p#nb#.t.SQt.l.gQt.gQt.e.#QtQt.bQtQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.g.h.h.d.hQtQtacbj.x.x.W.x.x.x.O#o.x.x#p#o#p.P.D.x#p.X.W.x.P.xat.U#YQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.#.a.b.e.aQtbH.obrbn.x.x.O.x.x.W.P.x.x.P.C.x.x.x.x#o#o.P.C.Paz#LQtQt.a.#.gQt.#.cQtQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.bQt.f.#Qt.#.a#RbM#P.x.P#o.x.x.x#p.x.x#o.W.x#p.J.C.D.D#o#p.xbjbUaL.j.eQt.b.#.#.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.aQtQt.h.cQt.a.#Qt.#aV#Ea4#g.O.x.x.W.C.x.x.W#p.C#p.x.x.P.P.x.x.xaO#w.iQt.lQt.eQtQtQt.eQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#QtQt.g.b.fQtbtbb.x.x.O#o.x.x.x#p#p.P.x.x.x.C#o.P#b#o#p.6aT#u.zQt.bQtQt.g.l.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.h.bQtQt.d.g.e.e.g.e.#.c.FaSbJbh.x.D.C.x.x#p.x.x.x#p#o.D.O.D.C.P#p.saSQt.gQt#J.gQt.h.#Qt.a.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#QtQt.SQtQt.cbVa..x.C#n.C.x.x#p.x.P.x.x.x.x.x.x.x.x.WbyalbcQtQtQt.b.e.S.kQtQt.b.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.b.b.e.a.d.#QtQt.e.b.b.gQtQt#F#u#ta..W.P.x.x.x#o.W.x.x.x#p#b.x.x.x.x#q.j.aQtQt.bQt.#.dQt.a.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.l.#.aaVaA.x.x.X.P.x.x.J.D.x.P#p.W.x.x.W#p.C#5bq#v.gQt.g.h.g.bQt.aQtQt.c.gQtQt.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.hQt.#Qt.eQtQtQt.a.b.#QtQtQt.cQtQt.#.#aw.9aFae.W.x#p.P.C.D.C.x#p.P.P.C.W.C.XaN#SQt.b.e.a.f.e.e.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.a.bQtapaK.x#n.x.x#o.O#p.P.x.x#o.x.C.x.xaEbQ.L#F.aQtQt.cQtQt.#.dQt.a.#QtQtQt.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.e.g.#Qt.a.e.#QtQtQt.a.aQtQt.#.e.e.#QtQtQt#SbIbR#X.x.x#o#p.P.x.C.O#p.x.x.D.xbmbVQtQt.h.#.h.b.e.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.#.#.a.aQt.Abh.x#C#p.W.C.x#C.C.x.C.C#o.x#C.7.A#SQtQt.aQt.a.aQt.#.eQtQt.#.#.#QtQt.#.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.b.b.b.bQt.#.eawaQ#mae.x.P#o#o.P.P.C.C#p.W.x.x#q#YQt.a.f.g.#.eQtQt.hQt.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQt.#Qt.b.aQt.gQt.e.e.cQt.a.#a9.6.x.X.x.P#o#p.P.x.C.D.x.xbybD#L.lQt.b.c.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.b.b.b.b.#Qt.b.bQtQtbw#A#B#a.W#p#p.x.x.6.O#p.x.x.5#6.iQt.g.hQt.aQtQt.kQtQtQtQtQtQt.#.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.#QtQtQtQtQtQtQt.gbcaK.C.x.J#C.x.x.W.W.D#p.x#abWbd.fQt.dQt.#.d.f.d.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.e.a.a.b.#.e.d.bQtQt.c.e.p#yby#b#o.D.x#p#p.W.X.C.x#5ba.hQt.g.b.b.gQt.#.a.a.#QtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.eQtQt.aQtQtQt.#.b.eQt.b.Lau.x#h.x.x.x.O#o.x.C#obO#2.zQtQt.a.bQt.#.g.eQt.e.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#Qt.#QtQtQt.l.gQtQt.cQtQt.Zafad.I.x#p.W#p#p#o.x.x#t#L.b.aQt.h.e.a.g.b.e.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.bQtQt.b.cQt.#.F#8.P#o.x.x.P.J.W.x#c#x#M.F.cQt.#Qt.g.cQtQt.g.gQtQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#QtQtQtQt.aQtQtQt.#.gQtQt.b.dQtQt.l#Kax.4.6.x.x#o.X.W.x#na6.i.d.gQt.b.#.a.b.a.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.b.b.aQtQt.d.cQt.S.j.8.x.P.x.W.X.x.xb#bp#K.dQtQtQt.e.bQtQtQtQtQtQt.aQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQtQtQt.a.e.#QtQt.h.e.#.a.b.b.#QtQt.a#YafbX.I.x.P.x.D.xaBa1Qt.h.#QtQt.a.e.e.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQt.S.a.#.ebv.K#p#b.D.x.C.VbYbB.d.a.e.b.c.d.e.e.e.#.a.eQtQtQtQtQt.b.aQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.aQtQtQtQt.#QtQtQtQt.e.#QtQt.e.e.c.f.cQt.fQtQt.e.SbEbDbm.5.x.x#o.x#WbdQt.a.a.a.a.#Qt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.gQtQtbzbD.P.x.P.x.JbObZ.i.hQtQtQt.e.a.a.b.h.l.gQtQt.eQt.a.bQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.aQtQtQtQtQtQt.b.eQtQtQtQt.a.aQtQt.#.b.gQt.a.eQtQt.cQt.bak#8a5.J.x.xbhbL.f.h.b.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.hQtQtQt.1bJ.x.x.6bl#M.jQt.a.eQt.b.h.c.g.a.g.gQtQt.g.bQtQt.#Qt.b.eQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.S#rb0#i#b.xb..A.aQt.f.e.#.bQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtb1QtQtb2QtQtQtQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.e.bQtQt.oaB.xb#aMbw.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQtQtQtQt.d.G#8#9#o.4bgQtQtQt.c.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQt.fQtbz#fbmb4#e.hQtQtQt.b.a.a.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.l.gQt.#Qt.zbw###9bL#L.dQt.a.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.baV#EaD.2Qt.aQt.#.d.c.aQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.k.kQtQt.dQt.b.0bV#KQt.e.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQtQtb2.a.#QtQtQtQtb5QtQtQtQtQtQtQtQtQtQt.a.#.cQtQt.e.b.f.cQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.g.eQtQt.g.l.lQtQt.gQtQt.d.f.e.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qtb6.#.#.#.#.#QtQtb7.a.#QtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.a.aQt.c#JQtQtQt.#.b.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.gQtQt.#.bQt.a.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtb5.#.#.#.#.#.#.#.#QtQt.#.a.#.a.a.e.a.#QtQtQtQt.#QtQtQtQtQtQtQtQtQtQt.a.h.d.#QtQt.#Qt.#.eQtQt.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.eQtQt.e.aQt.a.#QtQt.cQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#b5.#.#b5.#.#b8b9c.c#c#cacbcccd.bce.#QtQtQtQt.#QtQtQtQtQtQtQtQt.e.g.#QtQt.#.a.h.#QtQtQtQtQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtQt.#QtQt.a.#.#.eQtQtQt.bQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQt.#.#.#.#.acfcgchcicjckclcjcmcncocp.e.aQtQtQtQt.#QtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQt.a.e.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtcqQt.ccrcsctclclclclcucvclclcwcxcy.cQtb3.aQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtcz.#.ccAc#ctclclclclclclclclcBclctcCcA.#.gQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.lcDcEclclclclclclcFclclclclcvcEcDb1.eQt.gb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#cGchclclclclclclclclcFclclcvcFclcHcr.e.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtcIb9cJcvckclclcFcKclclclclclclcBclcmb9Qt.bb2b6QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.kQtc.cLclclclclclclclclclclclclclclcMcNQtQtQt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.fcOcFclclclclclclclcuclclclclclclcBcP.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtcQclcuclclcuclclclcFclclclclcFcvclcRQt.e.gb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.b.aQt.#QtQtQtQtQtQtQtQtQtQt.gQtcScTclcvcvclclclclclclcBclclclclcUc..hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.e.#Qt.eQt.aQtQtQtQtQtQtQtQtQt.fcVcWcvclclclclclclclclclclclclclcXcYQtQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.aQtQt.a.a.aQtQtQtQtQtQtQtQt.bQtcZc0cFclclclclcFckclclcFc1clclclchc2Qt.b.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQt.fQtc3c4clclc1cvclclclclclcuclclctcgQtQt.bb1.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.#QtQtQtQtQtQtQtQt.#Qtc5cAc6c7clclclclclcvcFcBckcBctc#c8QtQtQtQtc9QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#Qt.aQtQt.eQt.#.#QtQtQtQtQtQtQtQt.b.e.fQtcAd.d#clclclclclclclclctcxcyb7.c.eQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.e.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#.g.lQtQt.e.#.#.aQtQtQtQtQtQtQtQtb1Qtda.#.kcAdbdcddcTclcldedfdgdhb8QtQt.eQtb1QtczQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.e.e.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#.FaV.g.#.aQtQtQtQtQtQtQtQtQtQtQt.#.gQt.hQt.cb3didjdkdldmdndodp.#.c.hQt.#Qt.bQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQt.b.eQtQt.eQt.f.a.e.c.aQtQtQtQtQtQtQtQtQt.e.#QtQtQtQt.a.aQtQt.e.bQt.cbkbIbcQt.aQtQt.gQtQtQtQtQtQtQtQtQt.e.#Qt.a.c.eQt#1.W.x.x.x#h.e.e.h.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.#Qt.bQt.#Qt.c.#.#.kQt.e.RQtQtQtQtQtQtQtQtQtQt.g.#QtQt.#.aQtQt.aQt.bQtQtbBa0azawQtQt.e.#.#.eQtQtQtQtQtQtQtQtQt.#.#.#.a.b.#.g.6.P.x#p.P#n.F.b.b.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtQtQt.d.hQtQtQt.a.ibUbp.F.#QtQtQtQtQtQtQtQtQtQt.a.h.eQt.#.e.dQtQtbdbMa.#jQtQtQt.#.aQtQtQtQtQtQtQtQtQtQtQtQtQt.#.g.a.aQt.i#p#p#p.W.P.ObN.g.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.h.c.g.c.bQtQt.aQt#S.E.K.XbgQtQtQtQtQtQtQtQtQtQtQt.d.gQt.#.l.gQtQtbEai.W#Xbk.dQt.c.c.aQtQt.a.e.eQtQtQtQtQtQtQtQt.#Qt.g.a.aQt.y.x#p.x#p#p.CaW.a.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.eQt.#.d.#.#aV#8bn.x.xbqQt.#.lQtQtQtQtQtQtQtQtQtQtQt.c.dQtQtbca9#g.Wab.TQtQt.h.e.eQtQt.a.#Qt.#QtQtQtQtQtQtQtQtQtQt.aQt.aQt#..x.P.x.x.x.P#ZQt.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.b.e.eQt.zbDau.x.x#oaO.MQt.kQtQtQtQtQtQtQtQtQtQt.f.dQtQt.2#VaE.x.DaFbzQt.d.a.b.#.a.a.a.#QtQt.#QtQtQtQtQtQtQtQt.#QtQt.#.aQt.t.P.P.x.x.x.x.mQt.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.#QtbzbD.K.x#n.X.x#b#3.#.lQt.gQtQtQtQtQtQtQtQtQtQtQtbH#MbG.x.W#b#V.#Qt.b.c.#.eQtQt.#QtQtQt.e.bQtQtQtQtQtQtQtQtQt.#Qt.eQtQt.A#p#p.x.x.P.xdq.#.e.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQt.a.#QtQtQt.#.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtaVbDbn.x.W.C.x#p.Ob..fQt.h.g.aQtQtQtQtQtQtQtQtQt.l.9b#.x.x.x.6dr.b.e.eQt.d.e.e.e.#.#QtQt.#.b.#QtQtQtQtQtQtQtQtQt.aQt.gQtQtaf.x#p.x.C#o.x#w.b.b.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.#.g.d.lQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.a.aQt.hQt.g.hQtQt.eQt.e.aQtQt.#.#.#Qt#J.e.g.c.c.aQtbz#f.V.x.D#o#p.6.x#c.x#u.h.aQt.a.#.a.a.eQt.aQtQt.adsbm#p.x.C#pataW.a.a.#.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.g.gQtbr#p.W.x.C#p#p#I.bQt.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.#.bQtbd.U#u.fQt.c.#QtQtQt.aQt.b.eQtQt.gQt.eQtQt.#Qt.l.#.g.dQt.e.b.l.e.b.aQt.b.eQt.e.aQt.aQtQtQtQtQt.#Qt.#QtQtQtQtQtQtQtQt.#.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQt.#Qt.#.f.e.fQtQt.dQtQtQtQtQtQt.#.a.c.b.#Qt.c.l.#Qt.zdsbj.D.x.X.x.x.D.x.O.xam#N.#.S.c.SQt.b.c.aQtQt.hbo#9#o.W.x#o.xaTbNQt.a.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.bQt#t.P.x.x.P.x.x#0.bQt.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.eQt.e.eQt.##L#9b#aD#JQt.a.a.gQt.eQtQt.c.#Qt.#Qt.e.bQt.b.#.e.3bE.b.aQtQt.b.lQt.a.c.a.#QtQtQt.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.d.a.e.eQt.SQt.gQt.e.hQt.#.gQtQtQtQtQt.b.S.eQtQtaVaGaX#p.C.x#b.J.x.x.O#p.P#pa1Qt.bQtQtQt.fQt.a.#.c.ua5.O.W.W.x#p.DbUbH.e.g.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.#.e.#ad#p.x.x#p.x.x.4.h.a.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQt.e.d.bQt.#.ldt.x.K#6bH.hQt.f.f.e.e.d.cQt.#.a.#.g.#.cQt.hbO#o.Ha7Qt.bQtQt.z.e.b.e.a.eQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQtQt.cQtQt.c.hQt#K.pQtQt.aQt.#QtQtQtQt.c.h.aQt.h.z.NbG.x.x.W.W.D#o.P.O.x.x#h.x#mQtQt.#Qt.kQt.#.cQtbk#W#o.x.x.X.x#n#naUQtQt.lQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQt.#.kaZ#p.P#p.P.x.xbnbz.b.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.b.g.e.gQt#V.P#p.WbMa3.gQt.c.cQt.#.c.#.dQt.aQt.dQtQtdq.x#b#h#q#7.bQtQt.S.bQtQt.a.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.g.dQtQtaL#B.yQt.eQt.bQtQtQtQtQtQtQtQt.Fbx.B.x.C.X#o#o.x.x.x.C.C.x.W.x.O#v.h.SQt.c.#Qt.ebgaJ#o.x.P.D#b.x#p#PaLQt.lQt.fQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.gQtQtbc#X.x.P#p.W.x#p#c.Z.#.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.b.aQtQt.#Qt.hQtQtaQ#o.W#c.xbl#u.k.#QtQt.g.dQt.#QtQt.b.d.a#7#o.x.P.x.Jdta3.gQtQt.#.gQt.#Qt.a.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.h.a.#.cQt.daSaOaC.dQt.d.#.a.a.fQtQt.f.g.fbxaC.O.x.C#p.x.x.D.x#p.x.O.x.O#o.xai.lQtQtQt.eQtbvag.x.x#o#b.C.C#p.xajbE.fQtQt#JQt.d.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.bQtQt#z.J.x.x.x.x.x.W.WbdQt.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.a.a.e.gQtQtQtQtaLaO.x.D.W.xaZa6aaQt.#QtQt.k.cQtQt.c.e.RaX.W#p.x.x.x#Ca8.G.RQtQt.#.c.bQt.e.e.a.a.#.#QtQtQtQtQtQtQtQtQtQt.#.a.e.e.e.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQtQt.S.#.fbD.X.x.N.#.gQt.dQt#RQt.bQt.faQat.x.O.P#o.W.x#o.D.x.x.x.x.J.W.W.xbn#YQt.c.zQtapbQ.I.x#n#o.x.P#b.x.J.8#NQtQt.eQtQt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.#.##E.W.x.P#p.x.x.P.x.tQt.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQt.gQt.bQt#r#5.x.x.D.P.xaEbYduQt.cQtQt.h.b.c.#.ca5.x#p.W.x.C.W#p.x#mbo.iQtQt.c.h.b.b.e.e.a.a.#.#QtQtQtQtQtQtQtQt.e.b.b.g.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.dQtbHbM.x.P.Obt.aQt.g.z.#Qt.a.l.9aB.x.P#o.x.C.x.C.W.x.x.x.P#p.C.x.O.x.DbUQt.b.e.2aq#4#p.x#o.W.P#n.O.x#cbfQtQtQt.c.#QtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.#bx.x.x.O.x.P.x.x.xaQ.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.#Qt.aQtQtQt.eQt.aQt.f.#.F#0.W.C.x.x.W.x#caK.L.lQt.f.e.lQtQtbY#b.x.x#p#o.x.X#o.x.Pam#l.iQt.e.g.g.b.e.e.a.#.#QtQtQtQtQtQtQtQt.b.c.g.g.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.#Qt.g.eQt.aQt.a.dQt#Ya5.x#p.xbm.d.cQtQt.eQt.c#y.4.x.x.C#o.D#p#o.C.W.P#p.x.x.x.x.x.P.W#p#X.z.b.pdvbh.x.X#b.C.x.W.C.C.xau.AQt.S.c.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.dQt.#Qt.E.P.x#p.x.x.x.x#panQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#bU.X.P#c.x.P.J.x.WaR#MbzQt.#.b.#bV.x.O.x.C.x.W.C.W.x.x#p#oaCbe#R.eQtQt.e.a.#.aQt.#.aQtQtQt.g.bQtQt.fQt.h.#.b.eQtQtQtQtQt.#QtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQtQt.#QtQtQt.k.bQtayb.#p.O.D.xbOQt.g.hQt#J.3bC.O.x.x.X#p.P.X.D.P.W.P.P#p.x.x.x.P.x#b.x.xbIbza6aX.x.x.J.x.x#c.x.O.x.xb#bvQt.hQt.g.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.cQtaz.x.x.x#p.x.x.P.xdtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#Qtaxae.x.P#o.P#p.O.x.x#Dasbw.eQtbN.O.x.P.D.x#o.x.J#o#o.W.x.x#bbnal#K.#.a.l.#QtQtQt.#Qt.e.eQtQt.d.udq.l.aQt.e.#QtQtQt.a.#Qt.a.c.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.hQtQt.l.eQt.b#V.w#p.x.D.x#o#A.hQt.b#AaI#p.P.x.x.C.P.x.C.W#p.P.P#p#p#p.x.x.x.x.O.x#paEdvat.C.x.x#C.x#p.O.x#o.x.OaT.yQtQt.#.f.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQt.fQtbl.x.x.x.P#p#p.P.x#9QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.#.#QtQtbk#g.x.X.x.P.x#C.6.x.x#naP#2#JbC.x.O.x.x#p.C.x#p.C.O#o.W#p.x.x#H#U#KQtQt.gQtQt.c.eQt.#.d.eQt#E.JbWQt.hQtQt.e.eQt.b.aQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.gQt.##Fag.C.x.x.W.x#4.6.S.faD.Q.x.x.O.W.P.P.x.x#p#o#o#o.x.x#p#p#p#p#p#p.W.x.x.x#b.5.x.x.x.D.x#o.P.x.6.x#nbi#J.#Qt.cQtQt.#.#QtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQt.cQt.r.x.x.x.P#p#p#p.War.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.cQt#raZ.x.Dae.J#o.x.X.J.x.P.X#mae.x#o#o.O.x.x.x.x#p.x.x.x#p.x.P.x.x.VbSbEQt.#.c.a.#.a.#.#QtQtbK.x#oag.kQt.S.g.hQtQtQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.S.#.eQtaabl.P#o.x.6#o.O.xadba.7.x.x#o#o.x.C.x.x.x#p#p.x.x#p.x.x.x.x#p#p#p#p.P.x#c.D.C.x#C.x.x#p#n.x.x#b.x.PbDQtQt.h.hQt.gQtQtQtQtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.eQt.hbh.x.x.x#p.x.x.x.O#c.FQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.g.e.M#B.x.x#b.O#o.O.P#p.C.C.x#n.D#p#p.X.x#o.P#p.x#p.P#p.x.x.x.J#c.x#p.5bqa7.bQt.e#J.g.a.h.bdu#X.x.xav#N.dQt.h.d.dQt.#.#Qt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.bQt.bQtao#D#p.x.D.6.x#o.x.W#P.W.x.x#p.x.O.O.x.P.W.x.x.x.W#p.x.x.x.x.x.x.x.x#p.x.W.x.x.O.x.x#n#c.x.P.P.D.x#a.tQt.zQt.kQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.gQt.1.D.x#p#p.x.x.x.x.O.Oa7QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.hQt.eQtQt.l.H#o.P.P.O.x.x.W.P#n.x.x.x#o.P.P.x.x.x.x.x.x.x.x#p#o.x.x#p#o.O.x.x.D.v#GQtQt.e.#QtQt.T#g.x.X.x#s#KQtQt.b#RQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.dQtQt#f.6.x.x#c.x.C#g.x.O.X.x.P.x#o#C.J.x.W.P.x#p#o.P.x.x#p.x.x.x.x.x.x.x.x.x.x.x.J.C.x.X.x.O.xbh#b.x.xa2bdQt.f.e.lQt.l.a.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQta1.x.x#p#p.x.x.x.x.C.PbVQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.d.gQt.b.c.abA.O.x#c#o.x#C#o.x.D.x.x.P.P.W.C.P.x#p#o.W.x.x.x.P.x.P.x.x.P.P.W.J#p.6aJbvQtQt.hQt.Z#D.W#b.W.x.wbgbzQt.a.bQt.g.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.dbs.P.x.x.C.x.P.x.x#o#p.W.P#p.W.x.x.P.x.X.x.D.x.x.P.P.P.P.x.x.x.x.x.x.x.x.x.W#p#o.x.C.x.x.x#b.x.C.x#Q#FQt.hQtQtQt.k.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.bbF.x#p.x#p.x#p#p.x.P.xacQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.#.#.a.g.#Qt.hba.V.x#p.x.P.x#p.x.C.X.x.x.x#p.x.x#p.x.x.x.C.C#p.x.x.x.P#o.x.x#p#p#p.x#baK.t.#.gaV#s#p.x.X.W#p#baQ.SQt.eQtQtQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.#QtQtQtQtQtQt.bQt.b.l.hQt.kQt.pbR.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.P.x.x.X#n.P.6#p.PbS.aQt.l.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtbU.x#o.x#p.x.x#p.x#p.xbMQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.e.abtb##p#c.x.x.J.C.x#o.x.x.x.x.O.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x.W#WdraVa2.x.X.x.x#b.x.xac.d.gQt.g.a.S.a.#.#.a.#QtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.c.eQt.#Qt.FQt.LaB.x.J.W.P.W.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.x.x.D.P.x#n.x#P#u.d.SQt.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.##0.x.C.x#p.x.x.P.x.P.x.8.#QtQtQt.aQt.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.e.aQtap#B.x.xae.x.O.P.x.x#o.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.C#p.W.C.x.x#h#i#4#o.O.W.O.C#p.J.xbM.iQt.e.hQtQt.#.eQtQt.e.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.c.cQtQt#lbh.x.x.x.P.X.x#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.C.O.x.W.W.PaZbgQtQt.g.eQt.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.daI.x.P.x.P.x.x.P.x.C.x#5.kQt.#Qt.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.F.g.##J.v.x.x#h.x.O.C#o.x.x.D.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P#p.x.W.X#h.D.x.x#o.X.W.P.P.x#c.x.O.x#x.j.#.h.S.bQtQt.e.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.l.S.a.b.k#I#o.x.X#b#p.x.x.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.O.x.x.x.JabaaQt.c.cQt#J#RQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.ebHaE#p#p.x.P.x.x.P.x#o.x#1.pQt.#QtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.aQt.hQt.aQt#6.6.x#n#o.x.x.D#p.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.W.W.x.x.W.P.D.x.P.O.P.x.x#o#o#C#p.xbCa7Qt.a.cQtQtQtQtQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.eQt.e.b#S#m.C.x#h#p.x.J#o.x#C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x#o.O.DbO.SQt.cQt.S.l.#.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.T#c.W.W.x.P.x.x.P.x.C.x#o.TQt.aQt.#QtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#Qt.a.k.#.iQt.A#P.x.O.D.x.P.O.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.W.X.W.x.C.P.x.x.C#o.x.W.D.x.W#p.J.O.xaO#ZQtQt.a.h.aQt.a.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.a.e.e.a#RQt#vaB.x.x.x.x.W.x.x#o.P.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.D.x#n.x.C#fQt.e.S.#.hQtQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtaS.W.C#o.x#p.x.x#p.x.P.x.x#ZQt.#.c.bQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.dQtQt.gQt.cQtbkaC.x.x.J.x.x#o#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W#p.P.D.x.x.x.x.W#p#p#b.x.X.C.x#4al.cQtQt.l.h.e.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.a.e.e.b.b.gQtaH#X.W.x#o.x.O.x.P.x.x#p.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#4.x#aao.b.d.gQt.c.#Qt.gQtQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtaf.x.W.O.x#p.x.x.x.x#p.W.xax.#Qt.g.aQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQt.kQtQtbz.g.SQta7a2.x.D.J.W.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.P.C.W.x.x#p#p.x.x.x.x.P.x.x.x.W#p.x.W#b.W.6#palbcQt.e.fQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.e.e.b.g.g.cbs.D.x#o.D.x.P.x.W.x.x.O#o#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.X#pby#rQt.fQt.g.#.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQt#U.x.P.D.x.x.P.x.x#p.x#o#pbY.c.#QtQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQt.gQtQt.dQt.c.kQtQtaVdw.x.C#o.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.x.P.C.x.x#p.x.P#o.O.x.x#b.x.x.W.W.J.x.O.x.O.x##awQt.#.b.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQt.#.aQt.#.gQt.eQt.g.g.f.#.f.kb4.X.x#b.x.W.x#p.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x.x#p.x.x#p.x.x#p.W.x.W.x.x#p#p.C.P#p#p.x.x.O.xa4.MQt.d.c.lQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQt#m.P.x.C.x#p.x.x.x#p.P#p.xbyQtQt.bQtQt.e.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.b.g.e.e.gdv.O.x.x.x.W.W.C.C.x.x.W.x.P#p#p.x.x.x.x.x#p.x#o.x.x#o.x.x.x.x.x.x.x.x.x.x.x#p.x#p.P.C.C#o#b#p#B.2Qt.dQtQt.#.#Qt.e.#.#.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.g.aQtQt.aQtQtQt.a.dQt.##TaB.J#p#o#o.x.C#p.C.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x.W.P.x#p.C.x.D.W.x.W.X.x#o.W.x.x.x.x.O.x#c.x#6#RQt.F.eQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#Qt#d.x.x.P.x#p.x.x.x#p.P#p.x.r.fQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.e.eQt.cQtQtaG.I.x.x.x.x.x.x#o#p.x.O.x.x.O.P.x.W.W.x.D.x.x.P.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x#p.P.W.W.C.W.x.CaRbwQtQt.aQt.e.dQt.#.eQt.lQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQtQt.#.g.l.g.h.h.gQt.da1#X.x.x.x.D.x.x.D.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.x#p.C.x.x#p.W.x.C.6.x.x#mav.x.C.J#p#b#o.x#P.m#JQt.h.bQt.SQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.f.w.x#p#p#p#p.x.x.x#p.P#p.xbh.pQt.eQt.e.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.aQt.FQt.tau.C#h#p.x.W.P.C.P.x.D.P.O.x.O#p.x#o.xae.W.x.C.x#p#p.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p.P.P.O.x#pau#2.fQt.g.fQtQt.h.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.#.bQt.gQt.k.#.h.lac.x.W#b.D#p.x.x#o.D.x#p.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.W.W.P.x.x#o.C.x.6.x#pa2bo.la5.x.x.W.X.x.xaZah.#Qt.l.aQt.g.#Qt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtbN.x.x#p#p.x#p.x.x.x#p.P#p.x.DduQt.bQt.eQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.dQt.eQt.h.b#Y.B#p#o#b.x.x.W.x#p.x.x#h.x#c.P.x.P.D.x.x.C.P.x#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.O#C.W.P.D.A.d.bQt.b.aQt.#.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.eQt.aQtQt.f.bQt.b.zdt.x.C#p.J#p.x.x.P.x.x.x.W.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.C#b.W#p.W.x.x.xatbx.dQtbE#o.W#b.D.x.xaK.yQt.eQtQtQt.c.#Qt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e#Z.x.x#p.W.x#p.x.x.x#p.P#p.x.x#A.#.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.b.bQt.g.SQtQt#F.8.O.x.C.W.x.x.O.D#n.x.XbFaMae.W.x.J#C.x#p#p.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.O#p.W.x.D#o.xaU.b.#Qt.b.cQtQt.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQt.b.eQt.b#K#i#p.x#c#b.x.P.x.C.P.x.x#p.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.D.x.x#b.X.x.WaE#f#J.#.fQt.o.x#p.O.x#b.Y.S.#.a.a.eQt.g.eQt.e.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bbD.x#p#p.W.x#p.x.x.x#p.P#p.x.P#j.a.gQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.a.fQtQt.c.dQt.hbU.6.x.x#o.x.x.W.C.x.xalQtaSbu#p.x.D#p.x.C.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.D.x.P.W.x.P.x#Q.eQt.bQt.kQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.cQtQt#Rao.I.x.W#c.W#p.W.P#p.x.x.x.C.D#p.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.W.P.x.xau#U.2.dQtQtQt.e#m.x.C.x.XbpQt.eQtQt.#QtQtQtQt.e.#Qt.lQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtai.W.x.P#p#p#p.x.x.x#p.P#p.x.Waz.#.#.a.#.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.g.l.#QtQt.fQt.hbAbh.x.X.x.x.x.x.P#bbL.aQt.cbS.w.x#c.x.x.J.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x.W.O#b#o.x#n.x.xad.1Qt#J.#Qt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.cQt.gQt.Sdq.C.P.x#o.P.P.x.C.x.P#p.P#p.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.P.xbhbY#TQt.eQt.f.b.l.bb..x.x.IdrQt.#QtQt.e.aQt.e.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtb4.P#p.W.x.x#p.x.x.x#p.P#p.x.xbR.eQt.a.#.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#Qt.b.#Qt.b.aQtQt.#QtQtbIau.x.W.x.x#o.x.xbf.a.g.#.#bKa2.x.W.P.x.O.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#c.P.x.W.O.x.C.W.x#H#kQt.iQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.bQt.e.lQt.l.Y.x.x.J#o.x.x.x.P.x.x.x.x.x.x.x.x#p#p.x#p.W.x#p#o.x.O.x#p.O.O.C.W.x#p#c#QbtQtQt.d.b.dQt.g.a.0#b.xbC#L.cQt.bQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.a.e.eQt.kbu#p.W.W.x.W.x.x.x.x.x.x.x.x#b#s#J.eQt.gQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.cQtbB#d.x#n.C.P.x.O.vQtQt.g.fQt.h#8.I.x.P#o.X#b.P.W.O.P.P.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#C.xbna1Qt.d.c.g.bQt.f.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.e.hQt.#.aQt.a.a.bQtbdbX.x#h.J#o#b.W.x.P.C.x.x.x.x.x.x.x.x#p.P#p.x.P.W.x.x#o.W.J.W.x.X#o.x.Cbr#2Qt.#.l.c.#.eQt.a.#.aan.Wa0#N.SQtQt.#Qt.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQt.#.a.e.ebc.V#p#p.P.x.x.x.x.x.x.x.x.x.x.x.wbN.aQt.g.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.zQt.2aK.x#p.X.X.xa4Qt.gQtQtaVQtQtbKb4.D.x.C.P#c.x#p.P.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.O.x#o.x.XacQtQt.gQt.lQt.f.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQtQt.aQtQt.fQtQt.ubj.x#c.x.x.x.W.x.P.x.x.O.x.x.x.x.x.x#p#p.x.C#p.x.x.D.C.x.x.C#b#o.x.x#maL.cQtQt.cQtQt.a.fQt#FQt.i#9bT.dQtQt.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQt.#.a.a.abg.X.x.P.P.x.x.x.x.x.x.x.x.x.x.x.DbKQtQt.aQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQt.lQt.iaz.W.x#b#pbX.aQt.b.e.#.b.kQt.gaf#P.x#p.x.J.X.x.J.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.O.P#p.Jbq.a.#.a.e#JQt.SQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.cQtQt.cQt.h.q.I.x.X#o#o.6.x#o.x#p.D.W.x.x.x.x.x.x#p#p#p.x.x.P#o.x.x.x.C#o#o.x.xaj.o.hQt.bQt.a.g.g.d.eQt#RQt.d.1aS.kQt.F.e.S.cQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#.a.aQt#A.x.x#o#p.P#p.x.x.x.x.x.x.x.x.W.P.9Qt.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.e.b.b.gQt.hax.x.x.xa8.a.f.e.e.b.#.#.#Qt.f.RbR#n.x.C#o.P.x.X#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.O.x#o#g.x.Dag.i.gQtQt.lQtQt.c.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQtQtQtQt.c.f.#awdw.6#p#o.O.x.D.x.C.D.x.x#p.O.P.x.x.x.x#p#p#p#p.x#o.W.x.W.O.W.x.x.xbm.A.FQt.a.e.#.g.#QtQtQtQt.cQt.eQtQt.gQt.#.a.e.hQtQt.#.aQt.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#.#QtaM.x.W.C.x#p.P.x.x.x.x.x.x.x.x.C.xbsQt.g.a.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.zQtQt.dQt.eQt.h.u#b.Cat.#.eQtQtQt.e.c.d.aQt.#QtbAau.x.x.x#C.x.P#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x#o.x#p.x.x.J#b#p.4.pQt.bQt.eQtQt.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.h.g.c.cQtQtbN#m#b.x.x#p#p.x.D#o.x.x.X.C.xb.aE.x.x#p#p#p#p#p.P.x#c.P.x.D.P.x#p#1ac.j.#Qt.#Qt.#Qt.g.eQt.a.c.a.#.a.#Qt.a.a.b.aQtQt.#QtQt.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.a.#.#.##m.x.W.P.x.x#p.x.x.x.x.x.x.x.x.x.x#W.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQt.a.eQt.cQt.eQt.eahaubG.#Qt.#.gQtQtQtQtQtQt.d.aQtbNa0.x#p#b#b.P.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.C.x.P.W.x.x.x.D.xaZ#..aQtQt.e.g.a.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.c.cQtaSaZ.P.x#b#p.P#o.P.x.C.P.D#p#gbe.RaR.x#p#p#p#p#p.P.P.x.x.W.X.C.xb#bs#RQtQt.aQt.g.fQt.gQtQt.e.eQtQt.aQtQtQt.aQtQt.a.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.a.#.#.d.V.P.x#p.x.x.x.x.x.x.x.x.x.x.x.x.CaX#JQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.e.bQtQt.hQtQt.dQtbwa0.d.#.a.#Qt.#QtQt.bQtQt.h.eQtQt#A#H.x#p.W.W.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W#p.x.x.P.J.x#PbZ.e.a.eQt.e.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQt.dQt.bdqaO.x#p#o.C.x.J.x.W.C.x.Ca.bp.F.g#z#o.x#p#p#p#p.P.P.P.x.P.D.x.Xai#LQt.e.c.c.c.cQtQt.aQtQt.e.eQtQt.bQt.bQt.eQt.cQt.#QtQt.#.eQt.#Qt.b.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.aQt.#.k#o.C.x.P#p.P.x.x.x.x.x.x.x.x.x.x.D#c.p.g.#.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.aQtQtQtQt.#Qt.k.hQt.d#R.gQtQtQt.eQtQt.aQtQtQt.a.c.gQtbc#I.x.W.W.P.P#p.x.x.x.x.x.x.x.x.x.x.x#p#p.W.x.x.x.x.C.x.C#o#4aG.e.k.e.b.e.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQt.aQt.aQt.hQtQt.SQt.Saq.x.x.P.D.x.O.x#p#b.x.Oatax.F.#.cQtaT.P.x.x.C.x.x#p.x.W.P.x.Xa4#zQtQt.g.g.b.e.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#Qt.eQt.dQt.0.J.x#p.x.W.W.x.x.x.x.x.x.x.x.x.x.W.W.mQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.g.g.e.#QtQtQtQtQtQtQtQtQt.a.b.h.b.cQt.laLaB.x.x#p.P.P.x.W.x.x.x#p.x.x#p.x.x.x.x.x.x.x.x.x.P#c.W.x.PbW.c.#.h.l.eQt.b.aQt.#QtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.b.aQt.fQt.dQt.g.S.##SaF.x.O.x#c.W.x.C.W.x.xbuaD.kQt.g.#.bbc#D.x.W.W.D.x.x.J#b.x.xa0bK.f.#.b.f.#.e.e.a.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQt.eQt.dQt#M#p#p.P.x#p.x.x.x.x.x.x.x.x.x.x.x#p.xaN.#.b.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.b.b.e.#QtQtQtQtQtQtQtQtQtQt.a.b.e.hQt.#.i#Faq.O.x#p.P.W.x.P.D.x.x#o.W.x.x.x.D.x.P.C#p.W.C.W#4#p#p.x#nbQ#NQt.d.aQtQtQt.e.#QtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.eQt.l.a.dQt#J.bQtbvaB.x#b.x#o.x.C.C#p.XaKa1.gQt.bQt.h.gQtaG#p.O#p#o.x.x#c.x#p.4#ZaVQtQt.g.g.b.b.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQt.a.#.cQt.H.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.W.P#I.#.c.g.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.#QtQtQtQtQtQtQtQtQtQt.a.#.#Qt.b.bQtQtQt.##2bC.x.P.x.J.x#p.x.x.x.D.D.x.C#c.x#p.x#p.J.x.x.C.P.C.C#p#p#W.M.e.a.eQt.g.hQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.#.zQt.a.g.b.a.#aQ.6.x.6.x.C.x#n.x#oaK.L.fQt.#.h.b.aQt.SQtad.x#o.x.x.W.W.xaC.9.a.#QtQt.c.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQt.a.a.#.ebX.C.P.x.x.x.x.P.x.x.x.x.x.x.x.x#p.W#p#xQt.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.c.f.f.c.a.#bHas#C#p.x.X.x.W.J.W.x.x#pag#y.Q#p.O.x.xae#4.x#p.P.Dae.J.W#5akQt.k.#Qt.#.dQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.g.#.S.l.h.#.kaM.x#n.x.x#b#p.x#bb4#zQtQt.e.f.aQtQt.hQtQt#r#b.C#b#b#b.xaX.N.lQt.g.h.aQtQtQt.e.aQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.a.#Qt.Fbb.O#p.x#p.P.x.x.x.x.x.x.x.x.x.x.x.x.xbn.iQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.e.aQt.gQt.a.h.Ga5.x.x.J.x.x.P#n#o#p##Qt.aaSbX#c.W.x.x#c.J.x.x.x.X.O.x#1boQt.k.k.h#JQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQt.h.e.a.eawav.O.D.W#b#p.xaebi#z.gQt.f.d.#QtQtQt.eQt.a.##6.x#o.x.xbna6#RQt.c.a.a.a.e.c.bQtQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#.a.#Qt#Kbh#p.x.x#p.P.x.x.x.x.x.x.x.x.x.x.x.x.x#c.TQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQt.a.aQt.#Qt.g.c#R.#QtQtaV#V#b.x.W#c.x.x.P.x#VQt.e.eQtaWbM.D.P.x.x.W.D.x.W.x.W.O.C#MQt.i.dQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.gQt.S.g#r#5#p.x#o.x.W#PaqbE.dQt.h.aQtQt.f.eQt.hQtQtQtawat.x#p.6#6bNQt.e.lQtQt.f.l.eQtQt.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.b.#Qtbk.P.x.x.x#p.x#p#p.x.x.x.x.x.x.x.x.x.C.x.W#EQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.gQtQt.e.#.g.aQtQtQt.b.c.e.aQt#z.7.x.x.x.x.P.xaQ.a.c.#.d.#.a#LbT.V.x.x.P.x.x#o.x#b.x#o#6.aQt.c.#.#.#.#.#.#.#.#QtQtQtQt",
"QtQtQtQtQtQtQtQt.gQtQt#u.5.x.D#p.xbhdv.yQtQt.c.#Qt.a.g.#QtQt.eQtQt.bQt.0.x.Jai.Z.eQt.gQtQt.#.#QtQt.e.gQtQt.#.a.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.aQt.b.#.#aQ.x.O#p.P.x.x.W#p.x.x.x.x.x.x.x.x.x.W.x.xdq.h.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQtQt.#Qt.#Qt.aQt.bQtQt.bQt.dQt.f.qbh.x.X.C.W#lQt.cQtQt.a.eQtQt#r#faO.x#o.x.C.P.x.x.C.xaP#RQt.a.a.a.a.a.a.a.aQtQtQtQt",
"QtQt.a.#.h.cQt.b.fQtas.x.x.x.x.KaU.yQt.#Qt.a.eQtQtQtQtQtQtQtQtQtQtQt.aaPaJ#..cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.b.cQt.hQtaA#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.W.x.x.W#qQtQt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQtbdaF.W.x.DbP.aQt.#.cQt.bQt.a.gQt#Ndqbm.C.x#b.D.x#p#n.xaj.j.aQt.b.b.b.b.#Qt.#QtQt.#",
"Qt.bQt.b.gQt.eQt.f#O.x.x.O.BbA.j.kQt.#.b.#Qt.#.aQtQtQtQtQtQtQtQtQt.SQtbwbHQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtaK#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#pab.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.gQt.SbAbj.x.u.g.#Qt.aQt.aQt.aQtQtQtQt.S.3a2.x.x#o.x#p.P.P#aduQtQt.cQtQtQt.b.#QtQt.#",
".e.#.e.d.aQt.S#rat#p.xaIbI.F.eQtQt.e.fQtQt.#Qt.gQtQtQtQtQtQtQtQtQt.gQt.bQt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQtQt.g#D#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#a#FQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.bQt.e.fQta7brbd.e.eQt.#QtQt.#.b.b.#Qt.g.gQtQt.tb4#b.x.C.6.C.x.5.tQt#J.lQt.#Qt.#QtQt.#",
".gQtQtQt.bQt.L#1.xbmdr#R.k.aQt.a.b.gQtQt.e.bQtQtQtQtQtQtQtQtQtQt.bQt.a.k.h.kQt.SQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.gQt.g.aQtbH#b#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.P#p.x#b.T.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.k.lQt.g.h.a.gbz.#.bQt.bQtQt.#Qt.#.a.a.e.b.b.b.e.bbd#Q#n.x.P.x.x.XbDQtQt.bQt.#.#QtQt.#",
"Qt.#.b.b.cbS#p#i#E.cQtQtQt.a.hQt.#QtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQt.a.#.#QtQtQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.#.a#G.x#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.W.P#p.x.x#E.e.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.fQtQt.gQt.#.f.#.#.#.bQt.bQtQt.#.dQtQt.a.aQtQt.bQt.bQt.#bdbqar.x#p.W.Cas.l.e.cQt.#.a.a.#",
"QtQtQt.jaia2aL.f.#Qt.c.e.g.fQtQt.a.b.b.#QtQt.cQtQtQtQtQtQtQtQtQtQt.eQt.a.e.b.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.aaN.x#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.P.xbp.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.aQt.c.aQt.e.#.#.eQtQtQtQt.#Qt.#.c.#Qt.a.aQt.aQtQt#J.bQtbw#8.V.P#o.xbr.eQt.l.#.e.e.#",
".#.cbE#MaoQt.c.#.c.hQtQt.eQtQt.a.#QtQtQtQtQt.bQtQtQtQtQtQtQtQtQtQt.#Qt.aQtQt.b.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.eQtQt.#QtbM.x#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.xaP.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#Qt.#Qt.a.#Qt.#.#.#QtQtQt.aQt.aQtQtQtQtQt.a.aQt.e.#QtQt.eQt.#.SaxaZ#b.x#WapQt.#.e.e.#",
".h.baV.dQt.c.g.cQtQtQt.cQtQt#JQt.e.eQt.#.aQt.a.bQtQtQtQtQtQtQtQt.#QtQt.a.b.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQt.hQtbX#p#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.W.P.W#p.4.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.#QtQt.#.b.#Qt.#Qt.e.#.a.bQt.a.#.eQtQtQt.bQt.hQt.a.gQt.#.b.e.hQt.c#uad.xaX#v.#.b.b.#",
".b.b.b.b.b.b.b.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#.bQt#FaZ.x.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.P#C#N.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.b.g.g.gQtQt#J.u#O.Jba.bQt.b",
".a.a.a.a.a.a.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.g.#Qt.aaaae.x.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.C.x#p.X.TQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.e.eQt.#.bQtQtQtaVbwbiaD.kQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.bQt.gbv.x.x.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.O.x#p.C#AQt.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#.#QtQt.e.g.bQtQt.#.b#.#S.e",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.ebe.x#o.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x#o#pbs.e.a.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.e.g.eQtQtQt",
".#.#.#.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.b.aQt#q.x#p.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x#o.xaKQt.a.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#Qt.#.aQtQt.#.#.#QtQt.dQt",
".#.#.#.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQtQtQt.eaR.C.x.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.P#p.x#H.e.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#QtQtQt.a.aQt.#QtQt.g",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtQt.j#g.C#p.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P#o#p.x.P.6#K.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.c.h.e.c.gQt.#",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.c.g#k#b.x.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.P.x.x#b.xayQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#Qt.#.aQtQt.#.#.aQtQt.hQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.a.a.#.N.x#p.C.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.PaUQt.c.#QtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.eQt.a.#bW.x.W.W.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.Y.#.bQt.#Qt.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.gQt.#.e#W.x.C.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x#p.x.x.xby.c.#Qt.e.eQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.gQtQt.lb..x.P.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.P.x#p.x#X.zQtQt.e.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.b.aQt.Z#c.x.x.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.W.x.P.x.P#rQt.b.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.a.eQtao.W.x.x.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x#p.x.C.P.xaDQt.h.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQt.#Qta6.x.x.x#p.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x.x.P#p.x.HQt.bQt.#QtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQt.#Qtdw.x.x#p#p.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.x.x.x#pa8.aQtQt.e.#Qt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.b.bQt#s.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#paB.zQt.gQt.a.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#Qt.a#Nbn.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#P#YQt.aQtQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#Qt.abv.6.x.W.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#pboQt.#.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.bQtal.x.x.C.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.xaNQt.#.eQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.gQtbs#p.x#o.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#pag.aQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.#Qt#m.x.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.s.kQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#Qt.ibj.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#p#P.MQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.aap.D.x.W.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#o.xap.bQt.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.t.P.P.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.x.P.9QtQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtbF.x.W.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P#p.xaA.g.g.a.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtbO.x#o.x#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.P.x.7.bQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.fbG.x.O.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.W.x#a#RQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtap.6.x.D.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P#o.x#bbB.a.c.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt#u.P.x#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.C.P.WaGQt.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtan#p.x.P#p.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.W.P#oagQt.#Qt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt#B.P.x.x.C.x#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.C.x.xbu.c.bQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.eQt.bQt.aaVbh.D.x.x#p.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#o.x.Oaw.#Qt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.#.#.e.abB#b.C.W.C.C#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#o.x.P.0Qt.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.hQt.dQtbe.x#p.C.O.W.x.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#o.x.xdvQt.a.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.dQt.hQt#O.x#p.W.P.x.x#p.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x#xQt.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.bQtQt.d.r.W.P.x.x.x.x#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.Pbn.iQt.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.#.eQta7.6.x.P#p.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.x#o#n#zQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.gQt.aQtds.W.x.P.W#p.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.C.x#M.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.SQtQt.ebf.x.x.P.C.x#p.x.P.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.x.P.xbf.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.gQt.S.#Qt.Q.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.Cbj.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.cQt.R.5.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.P.x.x.6.RQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.##2.x.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.C.x.x#EQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQt.a#f#p.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.P.D#pbWQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.#.b.bbX#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.X#pad.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.e.a.S#a.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.W.War#NQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.aQtbt.J.C.O.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.P.x.P#b.GQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt#y.x.D.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.x.X.x.C.xaGQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.dQtQtaq.C.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.x.x.x#p.X#QQt.#Qt.eQtQt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#Qt.haI.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p.xbm.eQtQt.a.#Qt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt#S.6.W.W.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p.W.x#b.ZQt.e.#QtQtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.##e.x.O.P#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x#p#o.P.xbV.#.a.eQt.#Qt.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.a.##8.x#p.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x.x.x#p.P#b.xbqQtQt.gQt.#Qt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQtaT.x.x.C#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x#p.x.C.x#x.bQt.gQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtaV.V.x.C.O.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.P.x.P.x.x.xaE.pQt.a.#.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c#.#n#p#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.C.x.W.P.P#p.W#z.cQt.#.eQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.bQtds.x.x.O.W.x.xdx.x.x.x.xdy.x.x.x.x.x.x.x.x.x.x.x.x.x.xdydz.x.x.x.x.x.x.x.x.x.x.x.x#p.P.P.W.W.WalQt.hQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.g.#.v.W#o.W.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdx.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.W.W#p#tQt.a.c.eQt.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb5Qtb2Qtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#QtQt.haE.W#p.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdy.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.P.P.P.Pa..lQt.g.#Qt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.#QtQt#Y.P#p.x.x.W#p.x.x.x.x.x.x.x.x.xdxdx.x#p.x.x.x.x.x.x.x.x.x.xdy.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p.P.P.x#zQtQt.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.#.aQtQtQtaf.x.W#o.C.W.xdz.x.x.x.x.xdy.x.x.x.x.x.x.x.x.xdy.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.x.x.EQtQt.c.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.#.a.#Qt.#b4#p.x#o#p.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdz.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xa8.aQt.bQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.a.e.a.#.j.V.x.x.x.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x.x.x.C.xaE.Z.aQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtdAclcldAQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.a.a.aQta1#o.x.J.x.P.P.Pclclclcl.x.x.x.x.x.xdBdCdDdEcuclclcl.xclclcucl.x.x.x.x.x.x.x.x.x#p.x.x.x.x.x.x.x.P.x.CbZ.b.e.lQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3dAclcFckQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb5QtQtb3QtQtQtQtdFdGdHdIdJdKdLdMdNdOdGdPQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtclclclclQtQtb1QtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtdQclcBcldRQtQtQtQtQtdSclckclcldTQt.c.aQtb1dUclclcldV.W.W.xclclclcB.x.xdy.x.xdWclclclclcldXclcl.xc1ckclcl.x.x.x.x.x.x.x.x.xdz.x.x.xdy.x.x.x#pdYdZd0dMd1d2d3cichdSd4b1QtQtQtQtQtQtQtQtQtQtQtQtQtb1QtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb1b1Qtb1Qtb1QtQtQtclclclclQtQtQt.#QtQtb2QtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtb9d5clclclclclclclclclcld6QtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtb2QtQtQtb2Qtb2QtQtQtQtQtQtQtQtclclclclQtQtQtb2QtQtQtb3b1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtcHcvclcld7b3QtczQtQtd8clclclcld9Qtb3.g.d.ae.clclcFe#.x.x#pclclclcl.x.x.x.x.xeaclcBclclclclclcl.xckckclcldz.x.x.x.x.x.x.x.x.xdx.x.x.x.x.xebecclclcFc1clclclclcucledQtQtb1QtQtQtb2QtQtQtQtQtb1.#QtQtQtQtQtQtQtQtb5Qtb3QtQtQtQtQtQtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtclclclclQtb3QtQtb6QtQtQtQtQt.#QtQtb1b3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3b6QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtcRcBclckclcuclckclcleeclclclQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtefclclclegQtQtQtb2Qtehclclclclct.bQt.b.e#Reiclclclej.x.xek.x.x.x.x.x.x.x.x.xelclclclemen.x.x.x.x.xdz.x.x.x.x.x.x.x.x.x.x.x.x.xdxeo.x.xepelclclclclclclcFclclcBclclQtQtQtQtQtQtQtQtQtQtQtb2b2Qt.#b1QtQtQtQtQtb3QtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtb3Qtb1QtQtQtQtQtQtclclclclQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtb1QtQtQtb2Qt.#QtQtQtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.#Qtb2QtQteqcBclclclereseteueuevcDewcuclQtQtb1QtQtQtQtQtQtQtb3b3QtQtQtQtQtQtQtQt.#QtQtb2b6QtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2Qtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtexcvcvcld6eyQtb2QtezcucleAdLclcleBQt.b.#bZeCclckckeb.P.x.x.x.x.xdx.x.x.x.x.xclclcBcl#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdy.xeDcFclclcBc7eEeFdPeGeHeIeJeKclQtQtQtQtQtb1Qtb1QtQtQtQtQtQtQtb1QtQtQtQtQtQtQtQtb1QtQtQtQtb2QtQtQtQteLQtQtQtQt.#b3eLQtb2QtQtQtclclclclQtQtb1b3QtQtczQtQtQtQtb3QtQtb3QtQtb3QtQtQtQtQtb3Qtb1QtQtQtb1QtQtQtQtb3QtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQteMeNclcvcFdHeOQtQtQtb2QtQtQtexePb3QtQtQtQtQtQtQteQcReReSeKcjeTeUeVQtQtQtQtQtQtclclclclQteWeXeYdKclQtQtclclclclQtQtQtd9clclclclcVQtQtQteZclclclcldHQtQtQtQtQtQtQtQtQtQtQt.#e0clcBcleVQtQtQte1clcldNe2cFcle3e4cIQte5clclcve6e7.P.W.xc1clclcl.x.x.xclclclclckclclclcke8clclclclclcl#p.x.x.x.x.x.x.x.xdz.x.xdze9c4cuclckf.f#.CfaQt.#.g.#QtcAfbQtQtQtclclcFe8b3eWeXeYdKclb2Qtfcfdd9fefffgdKfhfifjetQtQtQtQt.#Qt.#QtfkflfmfnfodLehfpfqQtQtQtQtclclclclQtQtQtQtfrclcBclclfsQtQtQtQteQcRfteSd1cjfueUeVQtQtQtQtQtQtcBfvclclQteWeXeYdKcBQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtfwclcvcldIeOQtQtQtQtQtQtQtQtQtb1QtQtQtQtQtQtQtfxeAclclclclclclc1cldOfyb1QtQtb2clclclclezehclclcFclQtQtclclclclQtQtb1eWeYclclclfffzb6fAeNcvclclfBd4QtQtQtQtQtQtQtQtQtQt.#QtfCclclclfDb2b2b2fEclclfFcCclcldO.hQt.bfGclclclfH.x.x.P.xclcFclcl.xdz.xclclclclcvclclclclclc1clclclclcl.x.x.x.x.x.x.x.x.x.x.x#p.xfIcuckckdVfJ.x.JfK.gQtQtQtQt.#QtQtQtQtclclclcFfLehcFcFclc1b2QtclclclclclclcldAclclfofMQtQtQtQtQtb2c.fNclcBclclclclclcFQtQtQtQtclclclclQtQtb1fsclclckckfOQtQtQtQtfxeKclcBeeclcBclcFcldO.eb3QtQtQtcFclclclezehclclclclb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtfPclcBclfQQtb1QtQtQtb2b3.#b1QtQtQtQtQtQtb1QtfrclfRclclclclclclclcucldHQtQtQtQtcBclcFc1fCclclclclcBQtQtclclclclQtQtQtQtfqeKclc1clfSfTfUclclclfofVQtQtQtQtQtQtQtQtQt.#QtQtQtc.clclclfWQtQtb2fXclclfYfZclcleh.aQt#Lf0ckclclf1.x.xdz#pclcuclcl.x.xdxclclclclclclcuclclclclclcvclclcl.x.x.x.x.x.x.x.x.x.x.x.x.xf2clclcldk.C.x.P#C#..bb1QtQtQtQtQtQtQtclclclclfCclclclclckQtb3clclclcBclcvclclclclcudKf3Qt.#QtQtcsclckclclclcBclckclclQtQtQtQtclclclclQtb3fxclcFclcBf4QtQtQtQtf5ckclclclclclclclclclcBf6b1QtQtQtclcvclclf7clclclclclQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtdMclc1clcZb2QtQtQtQtQtb3QtQtQtQtQtQtQtQtQtf8ckcucld3f9g..#d4g#cmclclclg#.#Qtb2clclcucFclgagbgcexgdQtQtclclclclQtQtQtQtQtgeclclcFcucickcBckclfxQtQtQtQtQtQtQtQtQtQtQtQtQtQtf8clclckeSb2QtgfdKclcuggghdKclcugi.abVgjclcvcBgk.x.P.x.PcBclclcl.x.x.x.x#pclclclcldx.xdx.x.xdyckcFcBcl.x.x.x.x.x.x.x.x.x.x.x.x.xdVcuclclgl.P.J.x.x#uQtb3QtQtQtQtb2Qtb2c1clclcFclePgbfTexgmQtQtcmgngogpcI.#gqdRgrc1clclgsb2b1Qtfqclclclclfmgtd4fTcZesdNQtQtQtQtclclclclQtguclckclcugvQtQtb3Qtf8cuclcleNfdcA.aeWg#cmcFclclgwb1b3QtckclclcBclgagxfTexgdQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtgyclcvgzgAQtQtQtQtQtcFc1clclclc1clQtQtQtb2dgcFclclgBQtQtb2QtQtcAclclclgCQtQtQtclclclclgD.aQtQtQtQtQtQtclclclclQtQtb3Qt.#.#gEclclcuclckclclew.#QtQtQtQtQtQtQtQtQtQtQtQt.#b1.acjcBclclexQtfZclclcmQtQtfXcvdXgFQtgGclclcBel.P.x.xdz.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.xdy.x.xgHclclcugI.x.x.X#oa4Qt.aQtQtb3Qtb3QtQtcBclclclgDb7Qtb2QtQtQtQtQtQtQtQtQtQtQtQteWclclclgJb1QtQtgKcvclcFgL.#QtQtQtQtQtQtQtQtQtQtclcFclclcgcuclclcueqQtQtQtQtQtdgclcuclgBQtb3Qtb2QtcAe8clclfbQtQtQtclclclclgD.a.#QtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtdKclc1cBcIQtQtQtQtQtclclclc1clcFclQtQtQtQtgMckclcldAcucFckclclclclcFcldMQtb3.#clclclclgNQtQtQtQtQtQtQtclclclclQtQtQtb2QtQtgOeSclclclclcldMgPQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtgQcvclclgRQtc#cucFgSQtQtgTclclfF.SgUclclclf..x.x.x.x.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.xdx.x.xgHclclclgV.x.W.W.xaR.dQt.#.#QtQtQtQtQtclckclclgNQtQtQtQtQtQtQtb2gWchcmeNdKckclclcFclcvdLQtQtQtgMclclcugXQtQtb2QtQtQtQtQtQtQtQtc1clclclcuclcldKgYQtQtQtQtQtQtgZclclclclclclclclclclclgzcldMQtQtQtclclclclg0Qtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtb1QtdMclcuclevQtQtQtQtb3clcBclclcBclclQtQtQtb2eKclclclclclclclclclclclclclgyb3Qtb3clclclclg1QtQtQtQtQtQtQtclclclclQtQtQtQtb3.#Qtg2clclclclclg#QtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtg3clclckgmQtg4cBcleIQt.ab9clclgD#.g5clclclg6.x.x.x.x.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.x.x.x.xdVclckclgl.x.X.x.x.WaWb3b5.#.#.#b2.#Qtclckclclg1QtQtQtQtQtb2cIg7dAclclclclclclclclclclg8b2QtQteKclc1clcIQtQtb3QtQtb1b3b3b1QtQtclcuclclckclclgmQtQtQtQtQtQtQteKclclclcFclclclclckclclclclg9QtQtQtclclclclg1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQth.clh#clha.#b3QtQtQtQtb3QtcBclclclQtQtQtQteKclclclclclcvclcuclclckcle8clQtQtQtclclclcl.#QtQtQtb2.#QtQtclclclclQtQtQt.#QtQtQtflclclclclc1cxQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtgXclclcFdQfydLclclfzQthbgOclclfohchdcvcBclhe.x.x.x.x.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.xdx.x.x.xf2clclclhf.x.O.xhg.xbeQt.aQt.#.#.#.#QtclcvcBcl.aQtQtQtQtb1QtfjcBclclclclclclcvckclclclcFQtQtb3eKc1clclhhQtQtQtQtQtb2QtQtQtQtQtclclclclclclcFclhib2Qt.#QtQtQteKclclclcFclclclclcFcFclclclclQtQtQtc1cFclcl.aQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtf9clclcvgMdPQtQtQtQtQtQtQtclclclclQtQtQtb1dQclclclfzQtQtQtb2QtQtQtQtQtQtQtQtQtckcvclclQtQt.#QtQtQtQtQtclclclclQtQtQtQtb1.#f8eKclclclclcldKfqQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQthbeKclclcleIclclgMb2Qt.g.ehjcuclhkclclclgHhl.x.x.x.x#pclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.xdz.xdyhmclc1clhnhlho.x.ChpaJ.g.a.#.#.aQt.#QtcvclclclQtQtQtb1Qtb3QtctckclclchgbcIQtQteOclclclclQtQtQtgMclclcldRQtQtQtQt.#QtQtQtQtQtQtclclclclhqclclclcFhrQtQtb3b1QtctclclclfzQtb2QtQtQtQtQtQtb2b2.#QtQtclcKclclQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQthsffclclclhthuQtQtQtQtQtQtcBclclcuQtQtQtQthvclckckhwQtQtQtQtb1QtQtQtb3QtQtQtQtclclclclb2QtQtQtQtQtQtQtclclclclQtQtQtQtQthhhxcBckclclclclcvhydPQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QthzcBckclcmclcBdHQtQt.gb6hAclcuhBclclcBhC#p.x.x.xdz.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.x.x.x.xe9c4clcvclhDhE#p.x.ObjhF.#eyb8fbQtb1QtclclclcFQtQtQtQtQtQtQteKclclcldPQtQtQtb3eIclclclclQtQtQtchclclclhG.#QtQtQtQtQtQtQtQtQtQtclclclcleOewclclclcFg3Qtb1QtQtd9cBclcvfrb2Qtb1Qtb2QtQtQtQtb1Qtb3QtcFcuclcvQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3gYcvcFclclcthHhIhu.#ezhJclclcucBQt.#QtQtdRcBc1clcugThKfTeOhLhMeqhNeYQtQtQtQtclclclc1QtQtQtQtb3QtQtQtclclclclQtQtQtQtb1hOcvclclclhPclclclcldOQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQthQclclclcBclcBfQQtQt.a.ecgclcvclclcBcKhR#p.x.x.x.x.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.x.x.x.x.xhShTclclcldVhUhVhlhWhXhYgmfocBQtQtb2cBclclclQtQtQtQtczb3QthZcuc1clh0eQ.#fzh1fNclcvclclQtb1Qth2h3clc1cBh.goh4eOh5gYfSQtQtQtQtc1clclclQtcIfSclclclclh6Qtb2QtdRclclclcugThKgceOh7f8eqhNeYb2QtQtQtclclclclQtQtQtb3b3.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQteyQtQtQtQth8cFdAcBclclclclclclclclclcvclQtQtQtQtQth9cleeckclc1clclclclclclclQtQtQtQtclcuckclQtQtQtQtQtQtQtQtclclclclQtQtQtb1fZcuclclcli.b1hNclh#clcli#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQti#clclclclclcliaQtQtQt.dcAcFcuclclclclib#p.x#p.x.x.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.x#pdydy.x.xicidclclclclclcuclclfvclclclb2.#QtclclclcBQtb2b3QtQtQtQtgTclclclclc1clclclclckclclclQtQtQtQthQclclcvclcFclcBclclclb3.#QtQtclclclclQtQteWieclclclclgnQtQtQtfpclclclclclclclclclcBclclQtQtQtQtcvclclclQtQtQtQtQtb3b1b2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtifcEclclclclclclclcFcldAigihQtQtQteLb3.#iicuclclclclclclclclclcuQtQtQtQtdAclclclQtQtQtQtQtQtQtQtclclclclQtQtQtgihZclfvckijeWQtdPgJclc1clhZggQtQtQtQtQtQtQtQtQtQtQtQtb3b2d4dKclcBclckikb2Qt.#.#Qt.gilcFclimclclin#p.xdy#p.x.xclclclcl.x.x.x.x.xclclclcl.x.x.x.x.x.xclclclcl.x.x.x.x.x.x.x.x.x.x.xdz.x.x.x.xioipc1clclc1clclclcuclcliq.#.eQtcFclckclQtQtQtQtQtQtQteWirclcFckclclcleeiscle8clclQtQtQtQtQtitfoclclclclclcFclclQtQtQtQtclclclclQtQtQtfLdIclclckclfsQtQt.#cRg9clclclclclclclclclclQtQtQtQtclclclclQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb1QtfTdGiuivd6cudLdMdNiwgYhLQtb2QtQtQtQtQtb1cAixgDiyeKfoizcXiAguc8b2QtQtQtcBclcBe8QtQtQtQtQtQtQtQtclclclclQtQtQtiBclclclcudRQtQtQtiCfgckclcliBQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtiDclclclfvfCQtb1Qt.a.dQtiEcBclclcliFdxdx.x.x.x.xdxclclclcl.x.x.x.x.xcBclcFcl.x.x.x.x.x.xclcFclcB.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xiGiHiIiJiKdEfvdeiLdgiMd4.#QtQtcBckcldAQtQtQtQtQtQtQtQtiNh1cidLdKilhqiOQtckclclclQtQtQtQtQtQtgpcReRe0eKiPfudOiQQtQtQtQtclclclcBQtQtQtb3fkeYcuclcBcFcRQtQtQtcAfrgDe0iRige0iSf6gufcQtQtQtQtclclclclQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb1QtQtb1QtQtb1QtQtQtQtQtb2Qtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2Qtb2QtQtQtQtb3QtQtQt.#QtQtQtQtb3QtQtQtQtQtQtQtQtQtb1QtQtQtb3QtQtQtQtb3QtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.dQtbv.x.x.W.x.x.x.xdx.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdz.x.x.x.x.x.x.x.x.P.W.x.x.LQtQtQt.ab2QtQtQtb1QtQtQtQtQtQtb2b3QtQtQtQtb5Qtb3QtQtb2QtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtb2QtQtQtczQtQtQtb3b2QtQtQteyQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQteyQtQtQtQtb1b3Qtb2.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtb2.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtb2b3QtQtQtQtQtQtQtQtQtQtQtQt.#b3QtaM.x.W.xiT#p.xdy.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdz.x.x.x#p.x#p.x.x.P.P.xanQt.#.a.aQtQtb2QtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3b3QtQtQt.#QtQtb2QtQtQtQtb1QtQtQtQtQtQtQtQt.#QtQtQtQtQtb3b1QtQtQtQtQtQtQtQt.#QtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtb3QtQtb2QtQtQtQtQt.#Qtb1QtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQteLQtQtQtQtQtQtQtiUQt.diV.P#p#p.x.x.x.x.xeo.xdx.x.x.x.x.x.x.xdx.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdz.x.x#p.P.WiW.x.x.W.CiX.gQt.a.#.gQtQtQtQtQtQtQtQtQtQtQtQtQtb1QtQt.#QtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtb2QtQteyQtQtQtQtQtb2QtQtQtb2QtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb1b1QtQtQtQtb2QtQtQtQtQtQtb1b3QtQtQt.#b3QtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQt.#Qt.#QtQtb2QtQtQtQtQt.g.bap#Dhpho#odz.x.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x.x.x.x.xdx.x.xdydy.x.xdx.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.xdz.x.x#p.P#p.x.P.x#gaab3Qtb3.bb3iYQtQtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtb1Qtb2Qtb1QtQtb3QtQtQtQtQtQtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtb1QtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtb1b1QtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQt.#QtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb2QtQtQtb1b3b3QtQtb3QtQtQtQtQthbiZbP#o#pdx.Cdy.x.x.x.x.xdy.x.x.x.x.x.x.x.x.x.x.x.xiTdx.x.x.x.x.x.x.x.xdxiT.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.W.x.W#AQtQt.#QtQt.aQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtb1b1QtQt.#QtQtQtQtQt.#QtQtQtQtb3QtQtQtQtQtQtb3QtQtQtQtQtczb3QtQtQtQtQtQtQtQtQtb2b2QtQtQtQtQtQtQtb3QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtb1Qtb3QtQt.#QtQtQtQtQtQtQtb3QtQtQtQtb3QtQtb1QtQtQtQtb1QtQtQtQtQtQtQtQtb2QtQtQtQtQtQtQtQtQtQtb1QtQtb2QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQteyQtQtb2QtaU.x.W.W.xdy.x.x.xdx.x.x.x.x.x.x.x.x.x.x.x.x.x.xdx.x.xdy.x.x.x.xdy.x.xdx.x.x.x.x.x.x.x.x.x.x#p.x.x.x.x.x.x.x.x#b.x.x.x.x.W.P.xaA.hb2.bQt.#.#QtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtb1QtQtQtQtb3Qt.#.#b3QtQtQtQtQtQtQtQtQtQtb1Qt.#b3QtQtQtQtb1QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQt.eQtaZ#b.x.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P#paX.#.#Qt.bQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qtak#P.x.x.W.W#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.x#haWQtQt.#.aQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.#Qt.#.a.aQtaU#p.x.x.x#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.P.xa6Qt.#Qt.aQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.#QtQt.h.Q#p.P#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P#b.xa5.#Qt.aQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt#Y#h.W.W.P.W.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P#p.xbhbNQt.d.#.b.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQt#y.x.W#p.x.D.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.x.P.PbIQt.eQt.g.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQt.a.h#m.P.x.W.x.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.x.C#paJ.#QtQt.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQtQtQt.h#R#c.W.x.J.x.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p.P.D.P.x.IbzQt.l.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.eQt.gQtbF.P.P.P#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.C.xaSQt.kQt.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#Qt.a.gQt.#QtaJ.P.P#p#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.W.x#pbf.h.a.c.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt.g.eQt.a.2#X.P#p#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#pb#.iQt.e.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.eQt.bQtbI.C#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x#oak.dQt.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.#.eQt.8.P#p#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.W#p.xbp.cQt.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.a.h.##J#D.x#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x#b.x.4.gQt.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.hQt.m#o.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#o.x.6#rQt.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQt.a.#.ea0.x#o.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.X.x.W.x.N.a.a.#QtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.cQt#NbG.x.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x.O.x#baJ.aQtQtQt.#.#.a.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#.g.t#o#p.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P#p.x.x.x.x.rbEQt.aQtQt.aQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#an.x.O#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.O.x#pbPQt.aQtQt.bQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.b.d#H.x#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.x#b.P.x.HQtQt.#Qt.bQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.G.x.W.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W#p.W#p.x#o.x#s.kQt.eQt.aQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQt##.x.x.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.x.x#p.x.C#b#p.GQt.eQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.e.k.B.D.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#o#b.x.n.b.#QtQt.eQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#bB.x#p.P.x#o.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.P.x.W.C.x#pa5#JQtQtQt.aQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.#.a.#Qt.eQtas.X.x.O.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.P#T.cQt.g.aQtQtQtQtQtQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.#.a.#QtQt.kaj.x.x#n.C.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x#yQt.#Qt.aQt.aQtQtQtQtQt.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.#.a.#QtQtdu#n.x.P#o#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x#m.#.eQt.#.e.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.a.a.a.#Qt#V.x#o.D.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#p.wbcQt.eQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQtQt.a.e.a.#.faI#p.O.X.x#p.O.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.W.x#AQt.gQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#Qt.#.a.e.a.##L.6.P.x#o.P.O.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p#p.x.vQt.#Qt.e.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#Qt.#.a.e.a.#bD.W.W.x.x#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x.xb..RQt.#.e.e.a.a.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#Qt.#.a.e.a.#ad.P.C#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p#p#p#p.x#p.xa3Qt.h.#Qt.e.e.e.a.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.b.eQt.#QtQt.#QtQt.c.eQtQt.e.#.aQt.#.#.ebc.X#o#p.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.D.xaz.#.e.a.cQt.g.e.aQtQt.aQt.aQt.#.e.aQtQt.eQtQtQt.#.#.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.e.eQt.#.#QtQtQtQtQt.d.bQt.e.eQt.#btbL.D.C.x.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#o.x.x#d.0aVQtQt.f.#Qt.b.cQtQt.bQt.aQt.#Qt.h.cQtQtQtQt.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.b.eQtQt.aQtQtQt.a.bQt.#.aQt#Rduax#Ob##g.x.W.P.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#bae.x#caEa8bqbk.1QtQt.e.a.#QtQtQt.a.#QtQtQtQt.#.#.#.a.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.#QtQtQtQtQt.bQt.c.cQtQt.g#vaQ#t#a.x.x.P#p.x.x.x.x.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.W.x#p.x.x.x.x#na2a6#k.S.g.e.a.#Qt.#.e.g.c.f.a.a.#.#QtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.c.gQt.e.c.b.e.eQtQtbw#Vbu#h#p.D#p.W.O.P.x#p.C.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.x.P.P.x#b.O.x.x.X.O.Cbj.H#2.f.c.#Qt.a.g.aQt.e.a.#QtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.cQtQt.b#R.eQt.hbNaf.4.6#p.W#o#p.W#o.J.P.x.x.x.W.x.x#p.x.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W#p.x.W.x#b.x.x.x.D#b.x.x.V#IaL#F.#QtQt.l.b.e.#QtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.b.aQtQt.SbPaF.w.D.x.x#p#p#o#o.O.x.x.x.C.O.x#p.x#p.P#p.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.P.P.x.x#p.x.O.W.P.W#b.x.x.P.x.W.x.x#o.rbfbB.cQt.g.b.#QtQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.Ta9#a.C.x.P.x#o.O#p.W#o.P.C#o.X.x.x#p.x.x.x.W.P#p.x.x.x.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W.x.x.W#o.x.x.O.P#p.O.C.C#o.x.W#p.x.W.C.x#ob4.A.g.g.aQt.#Qt.#.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#Qt.a.#.#.#.a.#.a.#Qt.#.#QtQt.e.e.#Qt.#.#Qt.caQab.6#p.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#DbWapQtQt.b.e.a.cQtQtQt.b.e.#QtQt.e.#Qt.#Qt.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQtQtQtQtQtQt.#Qt.g.eQt.g.b.a.d.aQtQt.aQt.SbZbW#a#c.x.x.C#o.W.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x#c.7dsbN.eQtQt.h.f.#.a.f.f.#.#.c.eQt.a.e.#.eQtQtQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#QtQt.a.e.#.#.e.cQtQt.g.#.#.d.b.l.#.ibobOaO.W.x.x#p#o#b.D.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p.P.P.O#o#o.P.xaeaTaUaa.lQt.b.l.aQt.g.g.aQt.#.gQt.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.e.e.b.gQtQtQt.#.#Qt.e.S.gQtQt.faL.Har.x.C#o#p#p.C.O.O.C.x.x.x#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.P.P.W.W.x#p.C#o#p.x.x.x#pa8a#bHQtQt.aQtQt.g.bQtQtQt.#.#QtQtQtQtQtQt.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.aQtQtQt.#.eQtQt.i.eQt.c.ZdqbC.W#p.x.P#p.x.x.P.P.C.W.W.W.C.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.P.P.W.W.W.W#p.x#p.O#o#p.W.x.x.wbQa3.h.bQtQtQtQtQt.g.aQtQtQtQt.#.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.cQtQtQtQt.baoa4#1.P.x.x.C.O.x.x.x.W.O.W.W#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p.P.P.x.x.P.W.x.x.x.W#p.x.C.O.x#padac.R.aQt.c.bQtQt.l.a.a.a.a.#.#.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.c.a.b.l.#Qt.f.bbPa2.W.P.x.x.D.x.x.x#o.D#p.x.x.x.x#p.W.C.P.P.W.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.C.x.x.x.x#p#p.P.x.x.x.P.W.P.x.xaE#6.yQtQt.a.b.g.g.b.b.e.a.#.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.bQt.#.hQt.S#zaT#b.x.D.x.x#o.x#p.x.x.x.x#p#p.P.P.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p.P.x.x.x#p.x.P#p.x.x.x.x#p#o#b.xb.#8awQt.c.b.c.c.g.b.a.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.a.e.#QtQt.e.eQt.g.b.a.aa7br.C.C.C.W.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p#p.P.P#p.x#b.x.xbm#l.iQt.f.aQt.h.fQtQt.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.b.h.c.#QtQt.bQt#rag#c.x#b.W.W.P.P#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p.P#o.x.D#n.x.x.Q.NQt.#.#QtQt.h.gQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.a.#QtQtQtQtQt.cQta3bJ.6.x.O.x.x.W.W.P.P#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x#p#p#p#p.P.P#o.x.x#o.J.W.x.P.rbebzQt.b.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.eQtQt.h.d#NbdaJ#c.x#p.x.x.x.P#p#p#p.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.x.W#o.P.x.x.P.W.P.xbn#jawQt.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQt.a.#QtawaabHbzaw.l.h#F.F.z.z.z.z.zbzbzbz.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.z.zbzbzbz.z.z.z.z.i.iaV#Nbz.F#RaV.jbHbzawaw.d.g.dQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.#.e.#.a.cQtQt.hQt.lQtQt.l.#Qt.cQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.h.gQtQt.aQtQt.e.hQtQt.aQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.g.aQtQt.e.b.b.h.a.b.a.#QtQt.gQt.a.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#QtQtQtQtQt.g.eQtQt.g.h.#.b.#.a.b.g.c.g.#QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt.aQtQtQt.e.aQt.hQtQt.b.#QtQt.#.#.#.#QtQtQtQt.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#QtQtQtQtQtQtQt.#.#Qt.a.aQtQtQt.e.c.bQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt"
]

class Main_window(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap(image0_data)
        self.image1 = QPixmap(image1_data)

        if not name:
            self.setName("Main_window")

        self.setPaletteBackgroundColor(QColor(255,255,255))

        self.setCentralWidget(QWidget(self,"qt_central_widget"))
        Main_windowLayout = QGridLayout(self.centralWidget(),1,1,11,6,"Main_windowLayout")

        self.pixmapLabel1 = QLabel(self.centralWidget(),"pixmapLabel1")
        self.pixmapLabel1.setPixmap(self.image0)
        self.pixmapLabel1.setScaledContents(1)

        Main_windowLayout.addWidget(self.pixmapLabel1,2,1)
        spacer1 = QSpacerItem(31,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Main_windowLayout.addItem(spacer1,2,0)
        spacer2 = QSpacerItem(61,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Main_windowLayout.addItem(spacer2,2,2)

        self.text_output = QTextEdit(self.centralWidget(),"text_output")
        self.text_output.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum,0,0,self.text_output.sizePolicy().hasHeightForWidth()))
        self.text_output.setMaximumSize(QSize(32767,100))
        self.text_output.setTextFormat(QTextEdit.RichText)
        self.text_output.setWordWrap(QTextEdit.WidgetWidth)
        self.text_output.setReadOnly(1)

        Main_windowLayout.addMultiCellWidget(self.text_output,1,1,0,2)

        self.tabWidget2 = QTabWidget(self.centralWidget(),"tabWidget2")

        self.tab = QWidget(self.tabWidget2,"tab")
        tabLayout = QGridLayout(self.tab,1,1,11,6,"tabLayout")

        self.pixmapLabel2 = QLabel(self.tab,"pixmapLabel2")
        self.pixmapLabel2.setPixmap(self.image1)
        self.pixmapLabel2.setScaledContents(1)

        tabLayout.addWidget(self.pixmapLabel2,0,1)
        spacer3 = QSpacerItem(101,41,QSizePolicy.Expanding,QSizePolicy.Minimum)
        tabLayout.addItem(spacer3,0,0)
        spacer4 = QSpacerItem(21,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        tabLayout.addItem(spacer4,0,2)

        self.textLabel1 = QLabel(self.tab,"textLabel1")
        self.textLabel1.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Preferred,0,0,self.textLabel1.sizePolicy().hasHeightForWidth()))
        self.textLabel1.setMinimumSize(QSize(600,0))
        self.textLabel1.setMouseTracking(0)
        self.textLabel1.setTextFormat(QLabel.AutoText)

        tabLayout.addMultiCellWidget(self.textLabel1,1,1,0,2)
        self.tabWidget2.insertTab(self.tab,QString.fromLatin1(""))

        self.TabPage = QWidget(self.tabWidget2,"TabPage")
        TabPageLayout = QGridLayout(self.TabPage,1,1,11,6,"TabPageLayout")

        self.toolBox3_2 = QToolBox(self.TabPage,"toolBox3_2")
        self.toolBox3_2.setCurrentIndex(0)

        self.page1 = QWidget(self.toolBox3_2,"page1")
        self.page1.setBackgroundMode(QWidget.PaletteBackground)
        page1Layout = QGridLayout(self.page1,1,1,11,6,"page1Layout")

        self.textLabel3_5_6_2_2 = QLabel(self.page1,"textLabel3_5_6_2_2")

        page1Layout.addWidget(self.textLabel3_5_6_2_2,1,0)

        self.table_interfaces = QTable(self.page1,"table_interfaces")
        self.table_interfaces.setNumCols(self.table_interfaces.numCols() + 1)
        self.table_interfaces.horizontalHeader().setLabel(self.table_interfaces.numCols() - 1,self.__tr("Interface"))
        self.table_interfaces.setNumCols(self.table_interfaces.numCols() + 1)
        self.table_interfaces.horizontalHeader().setLabel(self.table_interfaces.numCols() - 1,self.__tr("MAC"))
        self.table_interfaces.setNumCols(self.table_interfaces.numCols() + 1)
        self.table_interfaces.horizontalHeader().setLabel(self.table_interfaces.numCols() - 1,self.__tr("Chipset"))
        self.table_interfaces.setNumCols(self.table_interfaces.numCols() + 1)
        self.table_interfaces.horizontalHeader().setLabel(self.table_interfaces.numCols() - 1,self.__tr("Driver"))
        self.table_interfaces.setNumCols(self.table_interfaces.numCols() + 1)
        self.table_interfaces.horizontalHeader().setLabel(self.table_interfaces.numCols() - 1,self.__tr("Mode"))
        self.table_interfaces.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.MinimumExpanding,0,0,self.table_interfaces.sizePolicy().hasHeightForWidth()))
        self.table_interfaces.setMinimumSize(QSize(0,85))
        self.table_interfaces.setMaximumSize(QSize(32767,100))
        self.table_interfaces.setNumRows(0)
        self.table_interfaces.setNumCols(5)
        self.table_interfaces.setReadOnly(1)
        self.table_interfaces.setSelectionMode(QTable.SingleRow)

        page1Layout.addWidget(self.table_interfaces,2,0)

        self.textLabel3_5_6_2 = QLabel(self.page1,"textLabel3_5_6_2")

        page1Layout.addWidget(self.textLabel3_5_6_2,4,0)

        self.table_networks = QTable(self.page1,"table_networks")
        self.table_networks.setNumCols(self.table_networks.numCols() + 1)
        self.table_networks.horizontalHeader().setLabel(self.table_networks.numCols() - 1,self.__tr("Essid"))
        self.table_networks.setNumCols(self.table_networks.numCols() + 1)
        self.table_networks.horizontalHeader().setLabel(self.table_networks.numCols() - 1,self.__tr("Bssid"))
        self.table_networks.setNumCols(self.table_networks.numCols() + 1)
        self.table_networks.horizontalHeader().setLabel(self.table_networks.numCols() - 1,self.__tr("Channel"))
        self.table_networks.setNumCols(self.table_networks.numCols() + 1)
        self.table_networks.horizontalHeader().setLabel(self.table_networks.numCols() - 1,self.__tr("Signal"))
        self.table_networks.setNumCols(self.table_networks.numCols() + 1)
        self.table_networks.horizontalHeader().setLabel(self.table_networks.numCols() - 1,self.__tr("Enc"))
        self.table_networks.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding,0,0,self.table_networks.sizePolicy().hasHeightForWidth()))
        self.table_networks.setMinimumSize(QSize(0,0))
        self.table_networks.setMaximumSize(QSize(32767,32767))
        self.table_networks.setNumRows(0)
        self.table_networks.setNumCols(5)
        self.table_networks.setShowGrid(1)
        self.table_networks.setReadOnly(1)
        self.table_networks.setSelectionMode(QTable.SingleRow)

        page1Layout.addWidget(self.table_networks,5,0)

        layout7 = QGridLayout(None,1,1,0,6,"layout7")

        self.textLabel3_4_4 = QLabel(self.page1,"textLabel3_4_4")

        layout7.addMultiCellWidget(self.textLabel3_4_4,0,0,0,1)

        self.line_gath_logs = QLineEdit(self.page1,"line_gath_logs")

        layout7.addWidget(self.line_gath_logs,1,0)

        self.button_gath_clean = QPushButton(self.page1,"button_gath_clean")

        layout7.addWidget(self.button_gath_clean,1,1)

        page1Layout.addLayout(layout7,0,0)

        layout8 = QHBoxLayout(None,0,6,"layout8")

        self.textLabel1_2 = QLabel(self.page1,"textLabel1_2")
        layout8.addWidget(self.textLabel1_2)

        self.combo_channel = QComboBox(0,self.page1,"combo_channel")
        self.combo_channel.setMinimumSize(QSize(100,0))
        layout8.addWidget(self.combo_channel)

        self.textLabel2_4 = QLabel(self.page1,"textLabel2_4")
        layout8.addWidget(self.textLabel2_4)

        self.spin_sec = QSpinBox(self.page1,"spin_sec")
        self.spin_sec.setMaxValue(200)
        self.spin_sec.setMinValue(5)
        self.spin_sec.setValue(10)
        layout8.addWidget(self.spin_sec)

        self.button_rescan_networks = QPushButton(self.page1,"button_rescan_networks")
        self.button_rescan_networks.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed,0,0,self.button_rescan_networks.sizePolicy().hasHeightForWidth()))
        layout8.addWidget(self.button_rescan_networks)

        page1Layout.addLayout(layout8,6,0)

        layout9 = QHBoxLayout(None,0,6,"layout9")

        self.button_reload_interfaces = QPushButton(self.page1,"button_reload_interfaces")
        layout9.addWidget(self.button_reload_interfaces)

        self.button_random_mac = QPushButton(self.page1,"button_random_mac")
        layout9.addWidget(self.button_random_mac)

        self.button_monitor = QPushButton(self.page1,"button_monitor")
        layout9.addWidget(self.button_monitor)

        page1Layout.addLayout(layout9,3,0)
        self.toolBox3_2.addItem(self.page1,QString.fromLatin1(""))

        TabPageLayout.addWidget(self.toolBox3_2,0,0)
        self.tabWidget2.insertTab(self.TabPage,QString.fromLatin1(""))

        self.TabPage_2 = QWidget(self.tabWidget2,"TabPage_2")
        TabPageLayout_2 = QGridLayout(self.TabPage_2,1,1,11,6,"TabPageLayout_2")

        self.toolBox2_2 = QToolBox(self.TabPage_2,"toolBox2_2")
        self.toolBox2_2.setCurrentIndex(2)

        self.page1_2 = QWidget(self.toolBox2_2,"page1_2")
        self.page1_2.setBackgroundMode(QWidget.PaletteBackground)
        page1Layout_2 = QVBoxLayout(self.page1_2,11,6,"page1Layout_2")

        self.buttonGroup2_3_2 = QButtonGroup(self.page1_2,"buttonGroup2_3_2")
        self.buttonGroup2_3_2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup2_3_2.layout().setSpacing(6)
        self.buttonGroup2_3_2.layout().setMargin(11)
        buttonGroup2_3_2Layout = QVBoxLayout(self.buttonGroup2_3_2.layout())
        buttonGroup2_3_2Layout.setAlignment(Qt.AlignTop)

        self.button_wep_start_sniff = QPushButton(self.buttonGroup2_3_2,"button_wep_start_sniff")
        buttonGroup2_3_2Layout.addWidget(self.button_wep_start_sniff)
        page1Layout_2.addWidget(self.buttonGroup2_3_2)

        self.buttonGroup2_3 = QButtonGroup(self.page1_2,"buttonGroup2_3")
        self.buttonGroup2_3.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup2_3.layout().setSpacing(6)
        self.buttonGroup2_3.layout().setMargin(11)
        buttonGroup2_3Layout = QVBoxLayout(self.buttonGroup2_3.layout())
        buttonGroup2_3Layout.setAlignment(Qt.AlignTop)

        self.button_wep_test_inj = QPushButton(self.buttonGroup2_3,"button_wep_test_inj")
        buttonGroup2_3Layout.addWidget(self.button_wep_test_inj)
        page1Layout_2.addWidget(self.buttonGroup2_3)
        spacer22_4 = QSpacerItem(41,110,QSizePolicy.Minimum,QSizePolicy.Expanding)
        page1Layout_2.addItem(spacer22_4)
        self.toolBox2_2.addItem(self.page1_2,QString.fromLatin1(""))

        self.page2 = QWidget(self.toolBox2_2,"page2")
        self.page2.setBackgroundMode(QWidget.PaletteBackground)
        page2Layout = QGridLayout(self.page2,1,1,11,6,"page2Layout")
        spacer22_2_2 = QSpacerItem(41,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        page2Layout.addItem(spacer22_2_2,3,0)

        self.buttonGroup1_2_3 = QButtonGroup(self.page2,"buttonGroup1_2_3")
        self.buttonGroup1_2_3.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_2_3.layout().setSpacing(6)
        self.buttonGroup1_2_3.layout().setMargin(11)
        buttonGroup1_2_3Layout = QVBoxLayout(self.buttonGroup1_2_3.layout())
        buttonGroup1_2_3Layout.setAlignment(Qt.AlignTop)

        self.button_wep_assoc_fake_auth_frag = QPushButton(self.buttonGroup1_2_3,"button_wep_assoc_fake_auth_frag")
        buttonGroup1_2_3Layout.addWidget(self.button_wep_assoc_fake_auth_frag)

        self.button_wep_start_frag = QPushButton(self.buttonGroup1_2_3,"button_wep_start_frag")
        buttonGroup1_2_3Layout.addWidget(self.button_wep_start_frag)

        self.button_wep_create_arp_frag = QPushButton(self.buttonGroup1_2_3,"button_wep_create_arp_frag")
        buttonGroup1_2_3Layout.addWidget(self.button_wep_create_arp_frag)

        self.button_wep_arp_inj_frag = QPushButton(self.buttonGroup1_2_3,"button_wep_arp_inj_frag")
        buttonGroup1_2_3Layout.addWidget(self.button_wep_arp_inj_frag)

        page2Layout.addWidget(self.buttonGroup1_2_3,2,0)

        self.buttonGroup1_3 = QButtonGroup(self.page2,"buttonGroup1_3")
        self.buttonGroup1_3.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_3.layout().setSpacing(6)
        self.buttonGroup1_3.layout().setMargin(11)
        buttonGroup1_3Layout = QVBoxLayout(self.buttonGroup1_3.layout())
        buttonGroup1_3Layout.setAlignment(Qt.AlignTop)

        self.button_wep_fake_auth_chop = QPushButton(self.buttonGroup1_3,"button_wep_fake_auth_chop")
        buttonGroup1_3Layout.addWidget(self.button_wep_fake_auth_chop)

        self.button_wep_start_chop = QPushButton(self.buttonGroup1_3,"button_wep_start_chop")
        buttonGroup1_3Layout.addWidget(self.button_wep_start_chop)

        self.button_wep_create_arp_chop = QPushButton(self.buttonGroup1_3,"button_wep_create_arp_chop")
        buttonGroup1_3Layout.addWidget(self.button_wep_create_arp_chop)

        self.button_wep_arp_inj_chop = QPushButton(self.buttonGroup1_3,"button_wep_arp_inj_chop")
        buttonGroup1_3Layout.addWidget(self.button_wep_arp_inj_chop)

        page2Layout.addWidget(self.buttonGroup1_3,1,0)
        self.toolBox2_2.addItem(self.page2,QString.fromLatin1(""))

        self.page = QWidget(self.toolBox2_2,"page")
        self.page.setBackgroundMode(QWidget.PaletteBackground)
        pageLayout = QVBoxLayout(self.page,11,6,"pageLayout")

        self.buttonGroup1_2_2_3 = QButtonGroup(self.page,"buttonGroup1_2_2_3")
        self.buttonGroup1_2_2_3.setFlat(0)
        self.buttonGroup1_2_2_3.setCheckable(0)
        self.buttonGroup1_2_2_3.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_2_2_3.layout().setSpacing(6)
        self.buttonGroup1_2_2_3.layout().setMargin(11)
        buttonGroup1_2_2_3Layout = QVBoxLayout(self.buttonGroup1_2_2_3.layout())
        buttonGroup1_2_2_3Layout.setAlignment(Qt.AlignTop)

        self.button_wep_assoc_fake_auth_rep = QPushButton(self.buttonGroup1_2_2_3,"button_wep_assoc_fake_auth_rep")
        buttonGroup1_2_2_3Layout.addWidget(self.button_wep_assoc_fake_auth_rep)

        self.button_wep_start_rep = QPushButton(self.buttonGroup1_2_2_3,"button_wep_start_rep")
        buttonGroup1_2_2_3Layout.addWidget(self.button_wep_start_rep)
        pageLayout.addWidget(self.buttonGroup1_2_2_3)

        self.buttonGroup1_2_2_2_3 = QButtonGroup(self.page,"buttonGroup1_2_2_2_3")
        self.buttonGroup1_2_2_2_3.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_2_2_2_3.layout().setSpacing(6)
        self.buttonGroup1_2_2_2_3.layout().setMargin(11)
        buttonGroup1_2_2_2_3Layout = QVBoxLayout(self.buttonGroup1_2_2_2_3.layout())
        buttonGroup1_2_2_2_3Layout.setAlignment(Qt.AlignTop)

        self.button_wep_assoc_fake_auth_req = QPushButton(self.buttonGroup1_2_2_2_3,"button_wep_assoc_fake_auth_req")
        buttonGroup1_2_2_2_3Layout.addWidget(self.button_wep_assoc_fake_auth_req)

        self.textLabel6_3 = QLabel(self.buttonGroup1_2_2_2_3,"textLabel6_3")
        buttonGroup1_2_2_2_3Layout.addWidget(self.textLabel6_3)

        self.spin_wep_wireless_req = QSpinBox(self.buttonGroup1_2_2_2_3,"spin_wep_wireless_req")
        self.spin_wep_wireless_req.setMaxValue(90000)
        self.spin_wep_wireless_req.setValue(68)
        buttonGroup1_2_2_2_3Layout.addWidget(self.spin_wep_wireless_req)

        self.textLabel7_2 = QLabel(self.buttonGroup1_2_2_2_3,"textLabel7_2")
        buttonGroup1_2_2_2_3Layout.addWidget(self.textLabel7_2)

        self.spin_wep_wired_req = QSpinBox(self.buttonGroup1_2_2_2_3,"spin_wep_wired_req")
        self.spin_wep_wired_req.setMaxValue(90000)
        self.spin_wep_wired_req.setValue(86)
        buttonGroup1_2_2_2_3Layout.addWidget(self.spin_wep_wired_req)

        self.button_wep_capture_req = QPushButton(self.buttonGroup1_2_2_2_3,"button_wep_capture_req")
        buttonGroup1_2_2_2_3Layout.addWidget(self.button_wep_capture_req)
        pageLayout.addWidget(self.buttonGroup1_2_2_2_3)

        self.buttonGroup1_2_2_2_2_2 = QButtonGroup(self.page,"buttonGroup1_2_2_2_2_2")
        self.buttonGroup1_2_2_2_2_2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_2_2_2_2_2.layout().setSpacing(6)
        self.buttonGroup1_2_2_2_2_2.layout().setMargin(11)
        buttonGroup1_2_2_2_2_2Layout = QVBoxLayout(self.buttonGroup1_2_2_2_2_2.layout())
        buttonGroup1_2_2_2_2_2Layout.setAlignment(Qt.AlignTop)

        self.textLabel6_2_2 = QLabel(self.buttonGroup1_2_2_2_2_2,"textLabel6_2_2")
        buttonGroup1_2_2_2_2_2Layout.addWidget(self.textLabel6_2_2)

        self.combo_wep_mac_cfrag = QComboBox(0,self.buttonGroup1_2_2_2_2_2,"combo_wep_mac_cfrag")
        self.combo_wep_mac_cfrag.setEditable(1)
        buttonGroup1_2_2_2_2_2Layout.addWidget(self.combo_wep_mac_cfrag)

        self.button_wep_autoload_clients_cfrag = QPushButton(self.buttonGroup1_2_2_2_2_2,"button_wep_autoload_clients_cfrag")
        buttonGroup1_2_2_2_2_2Layout.addWidget(self.button_wep_autoload_clients_cfrag)

        self.button_wep_arp_inj_cfrag = QPushButton(self.buttonGroup1_2_2_2_2_2,"button_wep_arp_inj_cfrag")
        buttonGroup1_2_2_2_2_2Layout.addWidget(self.button_wep_arp_inj_cfrag)
        pageLayout.addWidget(self.buttonGroup1_2_2_2_2_2)
        spacer25_2 = QSpacerItem(41,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        pageLayout.addItem(spacer25_2)
        self.toolBox2_2.addItem(self.page,QString.fromLatin1(""))

        self.page_2 = QWidget(self.toolBox2_2,"page_2")
        self.page_2.setBackgroundMode(QWidget.PaletteBackground)
        pageLayout_2 = QVBoxLayout(self.page_2,11,6,"pageLayout_2")

        self.buttonGroup1_2_2_3_2 = QButtonGroup(self.page_2,"buttonGroup1_2_2_3_2")
        self.buttonGroup1_2_2_3_2.setMidLineWidth(0)
        self.buttonGroup1_2_2_3_2.setFlat(0)
        self.buttonGroup1_2_2_3_2.setCheckable(0)
        self.buttonGroup1_2_2_3_2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_2_2_3_2.layout().setSpacing(6)
        self.buttonGroup1_2_2_3_2.layout().setMargin(11)
        buttonGroup1_2_2_3_2Layout = QVBoxLayout(self.buttonGroup1_2_2_3_2.layout())
        buttonGroup1_2_2_3_2Layout.setAlignment(Qt.AlignTop)

        self.button_wep_start_latte = QPushButton(self.buttonGroup1_2_2_3_2,"button_wep_start_latte")
        buttonGroup1_2_2_3_2Layout.addWidget(self.button_wep_start_latte)
        pageLayout_2.addWidget(self.buttonGroup1_2_2_3_2)

        self.buttonGroup1_2_2_3_2_2 = QButtonGroup(self.page_2,"buttonGroup1_2_2_3_2_2")
        self.buttonGroup1_2_2_3_2_2.setMidLineWidth(0)
        self.buttonGroup1_2_2_3_2_2.setFlat(0)
        self.buttonGroup1_2_2_3_2_2.setCheckable(0)
        self.buttonGroup1_2_2_3_2_2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_2_2_3_2_2.layout().setSpacing(6)
        self.buttonGroup1_2_2_3_2_2.layout().setMargin(11)
        buttonGroup1_2_2_3_2_2Layout = QVBoxLayout(self.buttonGroup1_2_2_3_2_2.layout())
        buttonGroup1_2_2_3_2_2Layout.setAlignment(Qt.AlignTop)

        self.button_wep_start_hirte_ap = QPushButton(self.buttonGroup1_2_2_3_2_2,"button_wep_start_hirte_ap")
        buttonGroup1_2_2_3_2_2Layout.addWidget(self.button_wep_start_hirte_ap)
        pageLayout_2.addWidget(self.buttonGroup1_2_2_3_2_2)

        self.buttonGroup1_2_2_3_2_3 = QButtonGroup(self.page_2,"buttonGroup1_2_2_3_2_3")
        self.buttonGroup1_2_2_3_2_3.setMidLineWidth(0)
        self.buttonGroup1_2_2_3_2_3.setFlat(0)
        self.buttonGroup1_2_2_3_2_3.setCheckable(0)
        self.buttonGroup1_2_2_3_2_3.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1_2_2_3_2_3.layout().setSpacing(6)
        self.buttonGroup1_2_2_3_2_3.layout().setMargin(11)
        buttonGroup1_2_2_3_2_3Layout = QVBoxLayout(self.buttonGroup1_2_2_3_2_3.layout())
        buttonGroup1_2_2_3_2_3Layout.setAlignment(Qt.AlignTop)

        self.button_wep_start_hirte_adhoc = QPushButton(self.buttonGroup1_2_2_3_2_3,"button_wep_start_hirte_adhoc")
        buttonGroup1_2_2_3_2_3Layout.addWidget(self.button_wep_start_hirte_adhoc)
        pageLayout_2.addWidget(self.buttonGroup1_2_2_3_2_3)
        spacer23 = QSpacerItem(41,111,QSizePolicy.Minimum,QSizePolicy.Expanding)
        pageLayout_2.addItem(spacer23)
        self.toolBox2_2.addItem(self.page_2,QString.fromLatin1(""))

        TabPageLayout_2.addWidget(self.toolBox2_2,1,0)

        self.textLabel4_4_3 = QLabel(self.TabPage_2,"textLabel4_4_3")

        TabPageLayout_2.addWidget(self.textLabel4_4_3,0,0)
        self.tabWidget2.insertTab(self.TabPage_2,QString.fromLatin1(""))

        self.TabPage_3 = QWidget(self.tabWidget2,"TabPage_3")
        TabPageLayout_3 = QGridLayout(self.TabPage_3,1,1,11,6,"TabPageLayout_3")

        self.textLabel4_4_2_3 = QLabel(self.TabPage_3,"textLabel4_4_2_3")

        TabPageLayout_3.addWidget(self.textLabel4_4_2_3,0,0)

        self.toolBox4_2 = QToolBox(self.TabPage_3,"toolBox4_2")
        self.toolBox4_2.setCurrentIndex(0)

        self.page2_2 = QWidget(self.toolBox4_2,"page2_2")
        self.page2_2.setBackgroundMode(QWidget.PaletteBackground)
        page2Layout_2 = QVBoxLayout(self.page2_2,11,6,"page2Layout_2")

        self.buttonGroup2_2_2_2 = QButtonGroup(self.page2_2,"buttonGroup2_2_2_2")
        self.buttonGroup2_2_2_2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup2_2_2_2.layout().setSpacing(6)
        self.buttonGroup2_2_2_2.layout().setMargin(11)
        buttonGroup2_2_2_2Layout = QVBoxLayout(self.buttonGroup2_2_2_2.layout())
        buttonGroup2_2_2_2Layout.setAlignment(Qt.AlignTop)

        self.button_wpa_start_sniff = QPushButton(self.buttonGroup2_2_2_2,"button_wpa_start_sniff")
        buttonGroup2_2_2_2Layout.addWidget(self.button_wpa_start_sniff)
        page2Layout_2.addWidget(self.buttonGroup2_2_2_2)

        self.buttonGroup2_2_2 = QButtonGroup(self.page2_2,"buttonGroup2_2_2")
        self.buttonGroup2_2_2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup2_2_2.layout().setSpacing(6)
        self.buttonGroup2_2_2.layout().setMargin(11)
        buttonGroup2_2_2Layout = QVBoxLayout(self.buttonGroup2_2_2.layout())
        buttonGroup2_2_2Layout.setAlignment(Qt.AlignTop)

        self.button_wpa_test_inj = QPushButton(self.buttonGroup2_2_2,"button_wpa_test_inj")
        buttonGroup2_2_2Layout.addWidget(self.button_wpa_test_inj)
        page2Layout_2.addWidget(self.buttonGroup2_2_2)
        spacer22_3_2 = QSpacerItem(41,140,QSizePolicy.Minimum,QSizePolicy.Expanding)
        page2Layout_2.addItem(spacer22_3_2)
        self.toolBox4_2.addItem(self.page2_2,QString.fromLatin1(""))

        self.page_3 = QWidget(self.toolBox4_2,"page_3")
        self.page_3.setBackgroundMode(QWidget.PaletteBackground)
        pageLayout_3 = QVBoxLayout(self.page_3,11,6,"pageLayout_3")

        self.groupBox4_2 = QGroupBox(self.page_3,"groupBox4_2")
        self.groupBox4_2.setColumnLayout(0,Qt.Vertical)
        self.groupBox4_2.layout().setSpacing(6)
        self.groupBox4_2.layout().setMargin(11)
        groupBox4_2Layout = QVBoxLayout(self.groupBox4_2.layout())
        groupBox4_2Layout.setAlignment(Qt.AlignTop)

        self.textLabel8_2 = QLabel(self.groupBox4_2,"textLabel8_2")
        groupBox4_2Layout.addWidget(self.textLabel8_2)

        self.combo_wpa_mac_hand = QComboBox(0,self.groupBox4_2,"combo_wpa_mac_hand")
        self.combo_wpa_mac_hand.setEditable(1)
        groupBox4_2Layout.addWidget(self.combo_wpa_mac_hand)

        self.button_wpa_autoload_clients = QPushButton(self.groupBox4_2,"button_wpa_autoload_clients")
        groupBox4_2Layout.addWidget(self.button_wpa_autoload_clients)

        self.textLabel8_2_2 = QLabel(self.groupBox4_2,"textLabel8_2_2")
        groupBox4_2Layout.addWidget(self.textLabel8_2_2)

        self.spin_wpa_deauth_hand = QSpinBox(self.groupBox4_2,"spin_wpa_deauth_hand")
        self.spin_wpa_deauth_hand.setValue(4)
        groupBox4_2Layout.addWidget(self.spin_wpa_deauth_hand)

        self.textLabel9_2 = QLabel(self.groupBox4_2,"textLabel9_2")
        groupBox4_2Layout.addWidget(self.textLabel9_2)

        self.button_wpa_deauth_hand = QPushButton(self.groupBox4_2,"button_wpa_deauth_hand")
        groupBox4_2Layout.addWidget(self.button_wpa_deauth_hand)
        pageLayout_3.addWidget(self.groupBox4_2)
        spacer32_2 = QSpacerItem(20,80,QSizePolicy.Minimum,QSizePolicy.Expanding)
        pageLayout_3.addItem(spacer32_2)
        self.toolBox4_2.addItem(self.page_3,QString.fromLatin1(""))

        TabPageLayout_3.addWidget(self.toolBox4_2,1,0)
        self.tabWidget2.insertTab(self.TabPage_3,QString.fromLatin1(""))

        self.TabPage_4 = QWidget(self.tabWidget2,"TabPage_4")
        TabPageLayout_4 = QGridLayout(self.TabPage_4,1,1,11,6,"TabPageLayout_4")

        self.textLabel4_4_2_3_2 = QLabel(self.TabPage_4,"textLabel4_4_2_3_2")

        TabPageLayout_4.addWidget(self.textLabel4_4_2_3_2,0,0)

        self.toolBox5 = QToolBox(self.TabPage_4,"toolBox5")
        self.toolBox5.setCurrentIndex(0)

        self.page1_3 = QWidget(self.toolBox5,"page1_3")
        self.page1_3.setBackgroundMode(QWidget.PaletteBackground)
        page1Layout_3 = QVBoxLayout(self.page1_3,11,6,"page1Layout_3")

        self.textLabel2_3 = QLabel(self.page1_3,"textLabel2_3")
        page1Layout_3.addWidget(self.textLabel2_3)

        self.line_fake_ap_essid = QLineEdit(self.page1_3,"line_fake_ap_essid")
        page1Layout_3.addWidget(self.line_fake_ap_essid)

        self.textLabel2_3_3 = QLabel(self.page1_3,"textLabel2_3_3")
        page1Layout_3.addWidget(self.textLabel2_3_3)

        self.line_fake_ap_chan = QLineEdit(self.page1_3,"line_fake_ap_chan")
        page1Layout_3.addWidget(self.line_fake_ap_chan)

        layout7_2 = QHBoxLayout(None,0,6,"layout7_2")

        self.buttonGroup14 = QButtonGroup(self.page1_3,"buttonGroup14")
        self.buttonGroup14.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup14.layout().setSpacing(6)
        self.buttonGroup14.layout().setMargin(11)
        buttonGroup14Layout = QHBoxLayout(self.buttonGroup14.layout())
        buttonGroup14Layout.setAlignment(Qt.AlignTop)

        self.check_fake_ap_wep = QCheckBox(self.buttonGroup14,"check_fake_ap_wep")
        buttonGroup14Layout.addWidget(self.check_fake_ap_wep)

        self.radioButton13 = QRadioButton(self.buttonGroup14,"radioButton13")
        self.radioButton13.setChecked(1)
        buttonGroup14Layout.addWidget(self.radioButton13)

        self.radio_fake_ap_wpa = QRadioButton(self.buttonGroup14,"radio_fake_ap_wpa")
        buttonGroup14Layout.addWidget(self.radio_fake_ap_wpa)

        self.radio_fake_ap_wpa2 = QRadioButton(self.buttonGroup14,"radio_fake_ap_wpa2")
        buttonGroup14Layout.addWidget(self.radio_fake_ap_wpa2)
        layout7_2.addWidget(self.buttonGroup14)

        layout6 = QVBoxLayout(None,0,6,"layout6")

        self.textLabel3 = QLabel(self.page1_3,"textLabel3")
        layout6.addWidget(self.textLabel3)

        self.line_fake_ap_wep_key = QLineEdit(self.page1_3,"line_fake_ap_wep_key")
        layout6.addWidget(self.line_fake_ap_wep_key)
        layout7_2.addLayout(layout6)
        page1Layout_3.addLayout(layout7_2)

        self.buttonGroup13 = QButtonGroup(self.page1_3,"buttonGroup13")
        self.buttonGroup13.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup13.layout().setSpacing(6)
        self.buttonGroup13.layout().setMargin(11)
        buttonGroup13Layout = QHBoxLayout(self.buttonGroup13.layout())
        buttonGroup13Layout.setAlignment(Qt.AlignTop)

        self.radio_fake_ap_wep40 = QRadioButton(self.buttonGroup13,"radio_fake_ap_wep40")
        self.radio_fake_ap_wep40.setChecked(1)
        buttonGroup13Layout.addWidget(self.radio_fake_ap_wep40)

        self.radio_fake_ap_tkip = QRadioButton(self.buttonGroup13,"radio_fake_ap_tkip")
        buttonGroup13Layout.addWidget(self.radio_fake_ap_tkip)

        self.radio_fake_ap_wrap = QRadioButton(self.buttonGroup13,"radio_fake_ap_wrap")
        buttonGroup13Layout.addWidget(self.radio_fake_ap_wrap)

        self.radio_fake_ap_ccmp = QRadioButton(self.buttonGroup13,"radio_fake_ap_ccmp")
        buttonGroup13Layout.addWidget(self.radio_fake_ap_ccmp)

        self.radio_fake_ap_wep104 = QRadioButton(self.buttonGroup13,"radio_fake_ap_wep104")
        buttonGroup13Layout.addWidget(self.radio_fake_ap_wep104)
        page1Layout_3.addWidget(self.buttonGroup13)

        self.groupBox7 = QGroupBox(self.page1_3,"groupBox7")
        self.groupBox7.setColumnLayout(0,Qt.Vertical)
        self.groupBox7.layout().setSpacing(6)
        self.groupBox7.layout().setMargin(11)
        groupBox7Layout = QGridLayout(self.groupBox7.layout())
        groupBox7Layout.setAlignment(Qt.AlignTop)

        self.check_fake_ap_adhoc_mode = QCheckBox(self.groupBox7,"check_fake_ap_adhoc_mode")

        groupBox7Layout.addWidget(self.check_fake_ap_adhoc_mode,0,0)

        self.check_fake_ap_hidden_ssid = QCheckBox(self.groupBox7,"check_fake_ap_hidden_ssid")

        groupBox7Layout.addWidget(self.check_fake_ap_hidden_ssid,0,1)

        self.check_fake_ap_no_broadcast = QCheckBox(self.groupBox7,"check_fake_ap_no_broadcast")

        groupBox7Layout.addWidget(self.check_fake_ap_no_broadcast,0,2)

        self.check_fake_ap_all_probes = QCheckBox(self.groupBox7,"check_fake_ap_all_probes")

        groupBox7Layout.addWidget(self.check_fake_ap_all_probes,0,3)
        page1Layout_3.addWidget(self.groupBox7)

        self.button_fake_ap_start = QPushButton(self.page1_3,"button_fake_ap_start")
        page1Layout_3.addWidget(self.button_fake_ap_start)
        spacer28 = QSpacerItem(21,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        page1Layout_3.addItem(spacer28)
        self.toolBox5.addItem(self.page1_3,QString.fromLatin1(""))

        TabPageLayout_4.addWidget(self.toolBox5,1,0)
        self.tabWidget2.insertTab(self.TabPage_4,QString.fromLatin1(""))

        self.TabPage_5 = QWidget(self.tabWidget2,"TabPage_5")
        TabPageLayout_5 = QGridLayout(self.TabPage_5,1,1,11,6,"TabPageLayout_5")

        self.toolBox5_3 = QToolBox(self.TabPage_5,"toolBox5_3")
        self.toolBox5_3.setCurrentIndex(0)

        self.page1_4 = QWidget(self.toolBox5_3,"page1_4")
        self.page1_4.setBackgroundMode(QWidget.PaletteBackground)
        page1Layout_4 = QVBoxLayout(self.page1_4,11,6,"page1Layout_4")

        self.groupBox1_5 = QGroupBox(self.page1_4,"groupBox1_5")
        self.groupBox1_5.setColumnLayout(0,Qt.Vertical)
        self.groupBox1_5.layout().setSpacing(6)
        self.groupBox1_5.layout().setMargin(11)
        groupBox1_5Layout = QVBoxLayout(self.groupBox1_5.layout())
        groupBox1_5Layout.setAlignment(Qt.AlignTop)

        self.textLabel10_4 = QLabel(self.groupBox1_5,"textLabel10_4")
        groupBox1_5Layout.addWidget(self.textLabel10_4)

        self.button_crack_wep_aircrack = QPushButton(self.groupBox1_5,"button_crack_wep_aircrack")
        groupBox1_5Layout.addWidget(self.button_crack_wep_aircrack)
        page1Layout_4.addWidget(self.groupBox1_5)
        spacer33_4 = QSpacerItem(31,91,QSizePolicy.Minimum,QSizePolicy.Expanding)
        page1Layout_4.addItem(spacer33_4)
        self.toolBox5_3.addItem(self.page1_4,QString.fromLatin1(""))

        self.page2_3 = QWidget(self.toolBox5_3,"page2_3")
        self.page2_3.setBackgroundMode(QWidget.PaletteBackground)
        page2Layout_3 = QGridLayout(self.page2_3,1,1,11,6,"page2Layout_3")

        self.groupBox1_2_3 = QGroupBox(self.page2_3,"groupBox1_2_3")
        self.groupBox1_2_3.setColumnLayout(0,Qt.Vertical)
        self.groupBox1_2_3.layout().setSpacing(6)
        self.groupBox1_2_3.layout().setMargin(11)
        groupBox1_2_3Layout = QVBoxLayout(self.groupBox1_2_3.layout())
        groupBox1_2_3Layout.setAlignment(Qt.AlignTop)

        self.textLabel11_2_4 = QLabel(self.groupBox1_2_3,"textLabel11_2_4")
        groupBox1_2_3Layout.addWidget(self.textLabel11_2_4)

        self.line_crack_wpa_dictionary = QLineEdit(self.groupBox1_2_3,"line_crack_wpa_dictionary")
        groupBox1_2_3Layout.addWidget(self.line_crack_wpa_dictionary)

        self.button_crack_wpa_aircrack = QPushButton(self.groupBox1_2_3,"button_crack_wpa_aircrack")
        groupBox1_2_3Layout.addWidget(self.button_crack_wpa_aircrack)

        page2Layout_3.addWidget(self.groupBox1_2_3,0,0)
        spacer33_2_3 = QSpacerItem(31,200,QSizePolicy.Minimum,QSizePolicy.Expanding)
        page2Layout_3.addItem(spacer33_2_3,2,0)

        self.groupBox1_3_3 = QGroupBox(self.page2_3,"groupBox1_3_3")
        self.groupBox1_3_3.setColumnLayout(0,Qt.Vertical)
        self.groupBox1_3_3.layout().setSpacing(6)
        self.groupBox1_3_3.layout().setMargin(11)
        groupBox1_3_3Layout = QVBoxLayout(self.groupBox1_3_3.layout())
        groupBox1_3_3Layout.setAlignment(Qt.AlignTop)

        self.textLabel10_2_3 = QLabel(self.groupBox1_3_3,"textLabel10_2_3")
        groupBox1_3_3Layout.addWidget(self.textLabel10_2_3)

        self.textLabel11_2_2_3 = QLabel(self.groupBox1_3_3,"textLabel11_2_2_3")
        groupBox1_3_3Layout.addWidget(self.textLabel11_2_2_3)

        self.line_crack_wpa_dictionary_pyrit = QLineEdit(self.groupBox1_3_3,"line_crack_wpa_dictionary_pyrit")
        groupBox1_3_3Layout.addWidget(self.line_crack_wpa_dictionary_pyrit)

        self.button_crack_wpa_pyrit = QPushButton(self.groupBox1_3_3,"button_crack_wpa_pyrit")
        groupBox1_3_3Layout.addWidget(self.button_crack_wpa_pyrit)

        page2Layout_3.addWidget(self.groupBox1_3_3,1,0)
        self.toolBox5_3.addItem(self.page2_3,QString.fromLatin1(""))

        self.page_4 = QWidget(self.toolBox5_3,"page_4")
        self.page_4.setBackgroundMode(QWidget.PaletteBackground)
        pageLayout_4 = QGridLayout(self.page_4,1,1,11,6,"pageLayout_4")

        self.groupBox1_3_3_2 = QGroupBox(self.page_4,"groupBox1_3_3_2")
        self.groupBox1_3_3_2.setColumnLayout(0,Qt.Vertical)
        self.groupBox1_3_3_2.layout().setSpacing(6)
        self.groupBox1_3_3_2.layout().setMargin(11)
        groupBox1_3_3_2Layout = QVBoxLayout(self.groupBox1_3_3_2.layout())
        groupBox1_3_3_2Layout.setAlignment(Qt.AlignTop)

        self.textLabel10_2_3_2 = QLabel(self.groupBox1_3_3_2,"textLabel10_2_3_2")
        groupBox1_3_3_2Layout.addWidget(self.textLabel10_2_3_2)

        self.textLabel11_2_2_3_2 = QLabel(self.groupBox1_3_3_2,"textLabel11_2_2_3_2")
        groupBox1_3_3_2Layout.addWidget(self.textLabel11_2_2_3_2)

        self.line_crack_wpa_rainbow_tables_file = QLineEdit(self.groupBox1_3_3_2,"line_crack_wpa_rainbow_tables_file")
        groupBox1_3_3_2Layout.addWidget(self.line_crack_wpa_rainbow_tables_file)

        self.button_crack_wpa_rainbow_tables = QPushButton(self.groupBox1_3_3_2,"button_crack_wpa_rainbow_tables")
        groupBox1_3_3_2Layout.addWidget(self.button_crack_wpa_rainbow_tables)

        pageLayout_4.addWidget(self.groupBox1_3_3_2,0,0)
        spacer24 = QSpacerItem(31,101,QSizePolicy.Minimum,QSizePolicy.Expanding)
        pageLayout_4.addItem(spacer24,1,0)
        self.toolBox5_3.addItem(self.page_4,QString.fromLatin1(""))

        TabPageLayout_5.addWidget(self.toolBox5_3,1,0)

        self.textLabel4_4_2_2_3 = QLabel(self.TabPage_5,"textLabel4_4_2_2_3")

        TabPageLayout_5.addWidget(self.textLabel4_4_2_2_3,0,0)
        self.tabWidget2.insertTab(self.TabPage_5,QString.fromLatin1(""))

        self.TabPage_6 = QWidget(self.tabWidget2,"TabPage_6")
        TabPageLayout_6 = QGridLayout(self.TabPage_6,1,1,11,6,"TabPageLayout_6")

        self.textLabel4 = QLabel(self.TabPage_6,"textLabel4")

        TabPageLayout_6.addWidget(self.textLabel4,0,0)

        self.table_database = QTable(self.TabPage_6,"table_database")
        self.table_database.setNumCols(self.table_database.numCols() + 1)
        self.table_database.horizontalHeader().setLabel(self.table_database.numCols() - 1,self.__tr("Essid"))
        self.table_database.setNumCols(self.table_database.numCols() + 1)
        self.table_database.horizontalHeader().setLabel(self.table_database.numCols() - 1,self.__tr("Bssid"))
        self.table_database.setNumCols(self.table_database.numCols() + 1)
        self.table_database.horizontalHeader().setLabel(self.table_database.numCols() - 1,self.__tr("Channel"))
        self.table_database.setNumCols(self.table_database.numCols() + 1)
        self.table_database.horizontalHeader().setLabel(self.table_database.numCols() - 1,self.__tr("Key"))
        self.table_database.setNumCols(self.table_database.numCols() + 1)
        self.table_database.horizontalHeader().setLabel(self.table_database.numCols() - 1,self.__tr("Ascii (not saved)"))
        self.table_database.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding,0,0,self.table_database.sizePolicy().hasHeightForWidth()))
        self.table_database.setMinimumSize(QSize(0,0))
        self.table_database.setMaximumSize(QSize(32767,32767))
        self.table_database.setNumRows(0)
        self.table_database.setNumCols(5)
        self.table_database.setShowGrid(1)
        self.table_database.setReadOnly(0)
        self.table_database.setSelectionMode(QTable.SingleRow)

        TabPageLayout_6.addWidget(self.table_database,1,0)

        layout10 = QHBoxLayout(None,0,6,"layout10")

        self.button_database_add = QPushButton(self.TabPage_6,"button_database_add")
        layout10.addWidget(self.button_database_add)

        self.button_database_delete = QPushButton(self.TabPage_6,"button_database_delete")
        layout10.addWidget(self.button_database_delete)

        self.line_database = QLineEdit(self.TabPage_6,"line_database")
        layout10.addWidget(self.line_database)

        self.button_database_reload = QPushButton(self.TabPage_6,"button_database_reload")
        layout10.addWidget(self.button_database_reload)

        self.button_database_save = QPushButton(self.TabPage_6,"button_database_save")
        layout10.addWidget(self.button_database_save)

        TabPageLayout_6.addLayout(layout10,2,0)
        self.tabWidget2.insertTab(self.TabPage_6,QString.fromLatin1(""))

        self.TabPage_7 = QWidget(self.tabWidget2,"TabPage_7")
        TabPageLayout_7 = QVBoxLayout(self.TabPage_7,11,6,"TabPageLayout_7")

        layout75 = QHBoxLayout(None,8,6,"layout75")
        spacer37 = QSpacerItem(51,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout75.addItem(spacer37)

        self.textLabel14 = QLabel(self.TabPage_7,"textLabel14")
        textLabel14_font = QFont(self.textLabel14.font())
        textLabel14_font.setPointSize(14)
        textLabel14_font.setBold(1)
        self.textLabel14.setFont(textLabel14_font)
        layout75.addWidget(self.textLabel14)
        spacer38 = QSpacerItem(31,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout75.addItem(spacer38)
        TabPageLayout_7.addLayout(layout75)

        self.textLabel16 = QLabel(self.TabPage_7,"textLabel16")
        TabPageLayout_7.addWidget(self.textLabel16)

        layout74_2 = QHBoxLayout(None,8,6,"layout74_2")
        spacer39_2 = QSpacerItem(61,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout74_2.addItem(spacer39_2)
        TabPageLayout_7.addLayout(layout74_2)

        self.textLabel17_2 = QLabel(self.TabPage_7,"textLabel17_2")
        TabPageLayout_7.addWidget(self.textLabel17_2)
        spacer41 = QSpacerItem(41,140,QSizePolicy.Minimum,QSizePolicy.Expanding)
        TabPageLayout_7.addItem(spacer41)
        self.tabWidget2.insertTab(self.TabPage_7,QString.fromLatin1(""))

        Main_windowLayout.addMultiCellWidget(self.tabWidget2,0,0,0,2)



        self.languageChange()

        self.resize(QSize(648,642).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.button_crack_wep_aircrack,SIGNAL("clicked()"),self.slot_crack_wep_aircrack)
        self.connect(self.button_crack_wpa_aircrack,SIGNAL("clicked()"),self.slot_crack_wpa_aircrack)
        self.connect(self.button_crack_wpa_pyrit,SIGNAL("clicked()"),self.slot_crack_wpa_pyrit)
        self.connect(self.button_crack_wpa_rainbow_tables,SIGNAL("clicked()"),self.slot_crack_wpa_rainbow_tables)
        self.connect(self.button_fake_ap_start,SIGNAL("clicked()"),self.slot_fake_ap_start)
        self.connect(self.button_gath_clean,SIGNAL("clicked()"),self.slot_gath_clean)
        self.connect(self.button_reload_interfaces,SIGNAL("clicked()"),self.slot_reload_interfaces)
        self.connect(self.button_rescan_networks,SIGNAL("clicked()"),self.slot_rescan_networks)
        self.connect(self.button_wep_arp_inj_cfrag,SIGNAL("clicked()"),self.slot_wep_arp_inj_cfrag)
        self.connect(self.button_wep_arp_inj_frag,SIGNAL("clicked()"),self.slot_wep_arp_inj_frag)
        self.connect(self.button_wep_assoc_fake_auth_frag,SIGNAL("clicked()"),self.slot_fake_auth)
        self.connect(self.button_wep_assoc_fake_auth_rep,SIGNAL("clicked()"),self.slot_fake_auth)
        self.connect(self.button_wep_assoc_fake_auth_req,SIGNAL("clicked()"),self.slot_fake_auth)
        self.connect(self.button_wep_autoload_clients_cfrag,SIGNAL("clicked()"),self.slot_autoload_victim_clients)
        self.connect(self.button_wep_capture_req,SIGNAL("clicked()"),self.slot_wep_capture_req)
        self.connect(self.button_wep_create_arp_frag,SIGNAL("clicked()"),self.slot_wep_create_arp_frag)
        self.connect(self.button_wep_start_frag,SIGNAL("clicked()"),self.slot_wep_start_frag)
        self.connect(self.button_wep_start_hirte_adhoc,SIGNAL("clicked()"),self.slot_wep_start_hirte_adhoc)
        self.connect(self.button_wep_start_hirte_ap,SIGNAL("clicked()"),self.slot_wep_start_hirte_ap)
        self.connect(self.button_wep_start_latte,SIGNAL("clicked()"),self.slot_wep_start_latte)
        self.connect(self.button_wep_start_rep,SIGNAL("clicked()"),self.slot_wep_start_rep)
        self.connect(self.button_wep_start_sniff,SIGNAL("clicked()"),self.slot_start_sniffing)
        self.connect(self.button_wep_test_inj,SIGNAL("clicked()"),self.slot_test_inj)
        self.connect(self.button_wpa_autoload_clients,SIGNAL("clicked()"),self.slot_autoload_victim_clients)
        self.connect(self.button_wpa_deauth_hand,SIGNAL("clicked()"),self.slot_wpa_deauth_hand)
        self.connect(self.button_wpa_start_sniff,SIGNAL("clicked()"),self.slot_start_sniffing)
        self.connect(self.button_wpa_test_inj,SIGNAL("clicked()"),self.slot_test_inj)
        self.connect(self.combo_wep_mac_cfrag,SIGNAL("textChanged(const QString&)"),self.slot_line_wep_mac_cfrag)
        self.connect(self.combo_wpa_mac_hand,SIGNAL("textChanged(const QString&)"),self.slot_line_wpa_mac_hand)
        self.connect(self.line_crack_wpa_dictionary,SIGNAL("textChanged(const QString&)"),self.slot_line_crack_wpa_dictionary)
        self.connect(self.line_crack_wpa_dictionary_pyrit,SIGNAL("textChanged(const QString&)"),self.slot_line_crack_wpa_dictionary_pyrit)
        self.connect(self.line_crack_wpa_rainbow_tables_file,SIGNAL("textChanged(const QString&)"),self.slot_line_crack_wpa_rainbow_tables_file)
        self.connect(self.line_gath_logs,SIGNAL("textChanged(const QString&)"),self.slot_line_gath_logs)
        self.connect(self.spin_wep_wired_req,SIGNAL("valueChanged(const QString&)"),self.slot_spin_wep_wired_req)
        self.connect(self.spin_wep_wireless_req,SIGNAL("valueChanged(const QString&)"),self.slot_spin_wep_wireless_req)
        self.connect(self.spin_wpa_deauth_hand,SIGNAL("valueChanged(int)"),self.slot_line_wpa_deauth_hand)
        self.connect(self.table_interfaces,SIGNAL("selectionChanged()"),self.slot_interface_selected)
        self.connect(self.table_networks,SIGNAL("selectionChanged()"),self.slot_network_selected)
        self.connect(self.button_random_mac,SIGNAL("clicked()"),self.slot_random_mac)
        self.connect(self.button_wep_arp_inj_chop,SIGNAL("clicked()"),self.slot_wep_arp_inj_chop)
        self.connect(self.button_wep_create_arp_chop,SIGNAL("clicked()"),self.slot_wep_create_arp_chop)
        self.connect(self.button_wep_start_chop,SIGNAL("clicked()"),self.slot_wep_start_chop)
        self.connect(self.button_wep_fake_auth_chop,SIGNAL("clicked()"),self.slot_fake_auth)
        self.connect(self.line_database,SIGNAL("textChanged(const QString&)"),self.slot_line_database)
        self.connect(self.button_database_delete,SIGNAL("clicked()"),self.slot_database_delete)
        self.connect(self.button_database_reload,SIGNAL("clicked()"),self.slot_database_reload)
        self.connect(self.button_database_save,SIGNAL("clicked()"),self.slot_database_save)
        self.connect(self.button_database_add,SIGNAL("clicked()"),self.slot_database_add)
        self.connect(self.table_database,SIGNAL("valueChanged(int,int)"),self.slot_database_changed)
        self.connect(self.button_monitor,SIGNAL("clicked()"),self.slot_monitor)


    def languageChange(self):
        self.setCaption(self.__tr("Gerix wifi cracker"))
        self.text_output.setText(QString.null)
        self.textLabel1.setText(self.__tr("Hello and Welcome!<br>\n"
"Gerix Wifi Cracker is a GUI that can help you to work in Wireless 802.11 Penetration Test.<br>\n"
"Created by Emanuele `emgent` Gentili and Emanuele `crossbower` Acri. The tool is under GPL 2 License.\n"
"<br> enJoy! <br>"))
        self.tabWidget2.changeTab(self.tab,self.__tr("Welcome"))
        self.textLabel3_5_6_2_2.setText(self.__tr("Select the <b>interface</b>:"))
        self.table_interfaces.horizontalHeader().setLabel(0,self.__tr("Interface"))
        self.table_interfaces.horizontalHeader().setLabel(1,self.__tr("MAC"))
        self.table_interfaces.horizontalHeader().setLabel(2,self.__tr("Chipset"))
        self.table_interfaces.horizontalHeader().setLabel(3,self.__tr("Driver"))
        self.table_interfaces.horizontalHeader().setLabel(4,self.__tr("Mode"))
        self.textLabel3_5_6_2.setText(self.__tr("Select the <b>target network</b>:"))
        self.table_networks.horizontalHeader().setLabel(0,self.__tr("Essid"))
        self.table_networks.horizontalHeader().setLabel(1,self.__tr("Bssid"))
        self.table_networks.horizontalHeader().setLabel(2,self.__tr("Channel"))
        self.table_networks.horizontalHeader().setLabel(3,self.__tr("Signal"))
        self.table_networks.horizontalHeader().setLabel(4,self.__tr("Enc"))
        self.textLabel3_4_4.setText(self.__tr("Directory for session files (logs, .cap, ...):"))
        self.button_gath_clean.setText(self.__tr("Clean old session files"))
        self.textLabel1_2.setText(self.__tr("Channel:"))
        self.combo_channel.clear()
        self.combo_channel.insertItem(self.__tr("all channels"))
        self.combo_channel.insertItem(self.__tr("1"))
        self.combo_channel.insertItem(self.__tr("2"))
        self.combo_channel.insertItem(self.__tr("3"))
        self.combo_channel.insertItem(self.__tr("4"))
        self.combo_channel.insertItem(self.__tr("5"))
        self.combo_channel.insertItem(self.__tr("6"))
        self.combo_channel.insertItem(self.__tr("7"))
        self.combo_channel.insertItem(self.__tr("8"))
        self.combo_channel.insertItem(self.__tr("9"))
        self.combo_channel.insertItem(self.__tr("10"))
        self.combo_channel.insertItem(self.__tr("11"))
        self.combo_channel.insertItem(self.__tr("12"))
        self.combo_channel.insertItem(self.__tr("13"))
        self.textLabel2_4.setText(self.__tr("Seconds:"))
        self.button_rescan_networks.setText(self.__tr("Rescan networks"))
        self.button_reload_interfaces.setText(self.__tr("Reload wireless interfaces"))
        self.button_random_mac.setText(self.__tr("Set random MAC address"))
        self.button_monitor.setText(self.__tr("Enable/Disable Monitor Mode"))
        self.toolBox3_2.setItemLabel(self.toolBox3_2.indexOf(self.page1),self.__tr("General configurations and network selection."))
        self.tabWidget2.changeTab(self.TabPage,self.__tr("Configuration"))
        self.buttonGroup2_3_2.setTitle(self.__tr("Functionalities"))
        self.button_wep_start_sniff.setText(self.__tr("Start Sniffing and Logging"))
        self.buttonGroup2_3.setTitle(self.__tr("Tests"))
        self.button_wep_test_inj.setText(self.__tr("Performs a test of injection AP"))
        self.toolBox2_2.setItemLabel(self.toolBox2_2.indexOf(self.page1_2),self.__tr("General functionalities"))
        self.buttonGroup1_2_3.setTitle(self.__tr("Fragmentation attack"))
        self.button_wep_assoc_fake_auth_frag.setText(self.__tr("Associate with AP using fake auth"))
        self.button_wep_start_frag.setText(self.__tr("Fragmentation attack"))
        self.button_wep_create_arp_frag.setText(self.__tr("Create the ARP packet to be injected on the victim access point"))
        self.button_wep_arp_inj_frag.setText(self.__tr("Inject the created packet on victim access point"))
        self.buttonGroup1_3.setTitle(self.__tr("ChopChop attack"))
        self.button_wep_fake_auth_chop.setText(self.__tr("Start false access point Authentication on victim"))
        self.button_wep_start_chop.setText(self.__tr("Start the ChopChop attack"))
        self.button_wep_create_arp_chop.setText(self.__tr("Create the ARP packet to be injected on the victim access point"))
        self.button_wep_arp_inj_chop.setText(self.__tr("Inject the created packet on victim access point"))
        self.toolBox2_2.setItemLabel(self.toolBox2_2.indexOf(self.page2),self.__tr("WEP Attacks (no-client)"))
        self.buttonGroup1_2_2_3.setTitle(self.__tr("ARP request replay attack"))
        self.button_wep_assoc_fake_auth_rep.setText(self.__tr("Associate with AP using fake auth"))
        self.button_wep_start_rep.setText(self.__tr("ARP request replay"))
        self.buttonGroup1_2_2_2_3.setTitle(self.__tr("ARP request attack"))
        self.button_wep_assoc_fake_auth_req.setText(self.__tr("Associate with AP using fake auth"))
        self.textLabel6_3.setText(self.__tr("Minimum packet length:"))
        self.textLabel7_2.setText(self.__tr("Maximum packet length:"))
        self.button_wep_capture_req.setText(self.__tr("Capture replay packets"))
        self.buttonGroup1_2_2_2_2_2.setTitle(self.__tr("Fragmentation client attack"))
        self.textLabel6_2_2.setText(self.__tr("Add victim client MAC:"))
        self.button_wep_autoload_clients_cfrag.setText(self.__tr("Autoload victim clients"))
        self.button_wep_arp_inj_cfrag.setText(self.__tr("Start Client Fragmentation Attack"))
        self.toolBox2_2.setItemLabel(self.toolBox2_2.indexOf(self.page),self.__tr("WEP Attacks (with clients)"))
        self.buttonGroup1_2_2_3_2.setTitle(self.__tr("Caffe-Latte attack in access point mode"))
        self.button_wep_start_latte.setText(self.__tr("Start Caffe-Latte attack"))
        self.buttonGroup1_2_2_3_2_2.setTitle(self.__tr("Hirte attack in access point mode"))
        self.button_wep_start_hirte_ap.setText(self.__tr("Start Hirte attack"))
        self.buttonGroup1_2_2_3_2_3.setTitle(self.__tr("Hirte attack in ad-hoc mode"))
        self.button_wep_start_hirte_adhoc.setText(self.__tr("Start Hirte attack"))
        self.toolBox2_2.setItemLabel(self.toolBox2_2.indexOf(self.page_2),self.__tr("WEP Attack (with clients, in Access Point and Ad-Hoc mode)"))
        self.textLabel4_4_3.setText(self.__tr("<h2>Welcome in WEP Attacks Control Panel</h2>"))
        self.tabWidget2.changeTab(self.TabPage_2,self.__tr("WEP"))
        self.textLabel4_4_2_3.setText(self.__tr("<h2>Welcome in WPA Attacks Control Panel</h2>"))
        self.buttonGroup2_2_2_2.setTitle(self.__tr("Functionalities"))
        self.button_wpa_start_sniff.setText(self.__tr("Start Sniffing and Logging"))
        self.buttonGroup2_2_2.setTitle(self.__tr("Tests"))
        self.button_wpa_test_inj.setText(self.__tr("Performs a test of injection AP"))
        self.toolBox4_2.setItemLabel(self.toolBox4_2.indexOf(self.page2_2),self.__tr("General functionalities"))
        self.groupBox4_2.setTitle(self.__tr("WPA handshake attack"))
        self.textLabel8_2.setText(self.__tr("Add victim client MAC:"))
        self.button_wpa_autoload_clients.setText(self.__tr("Autoload victim clients"))
        self.textLabel8_2_2.setText(self.__tr("Add the deauth number:"))
        self.textLabel9_2.setText(self.__tr("Now you need to capture the HandShake, start the deauthentication."))
        self.button_wpa_deauth_hand.setText(self.__tr("Client deauthentication"))
        self.toolBox4_2.setItemLabel(self.toolBox4_2.indexOf(self.page_3),self.__tr("WPA attacks"))
        self.tabWidget2.changeTab(self.TabPage_3,self.__tr("WPA"))
        self.textLabel4_4_2_3_2.setText(self.__tr("<h2>Welcome in Fake Access Point Control Panel</h2>"))
        self.textLabel2_3.setText(self.__tr("Access point ESSID:"))
        self.line_fake_ap_essid.setText(self.__tr("honeypot"))
        self.textLabel2_3_3.setText(self.__tr("Access point channel:"))
        self.line_fake_ap_chan.setText(self.__tr("12"))
        self.buttonGroup14.setTitle(self.__tr("Cryptography tags"))
        self.check_fake_ap_wep.setText(self.__tr("WEP"))
        self.radioButton13.setText(self.__tr("None"))
        self.radio_fake_ap_wpa.setText(self.__tr("WPA"))
        self.radio_fake_ap_wpa2.setText(self.__tr("WPA2"))
        self.textLabel3.setText(self.__tr("<b>Key in Hex</b> (Ex. aabbccddee) or <b>Empty</b>:"))
        self.line_fake_ap_wep_key.setText(self.__tr("aabbccddee"))
        self.buttonGroup13.setTitle(self.__tr("WPA/WPA2 types"))
        self.radio_fake_ap_wep40.setText(self.__tr("WEP40"))
        self.radio_fake_ap_tkip.setText(self.__tr("TKIP"))
        self.radio_fake_ap_wrap.setText(self.__tr("WRAP"))
        self.radio_fake_ap_ccmp.setText(self.__tr("CCMP"))
        self.radio_fake_ap_wep104.setText(self.__tr("WEP104"))
        self.groupBox7.setTitle(self.__tr("Options"))
        self.check_fake_ap_adhoc_mode.setText(self.__tr("AdHoc mode"))
        self.check_fake_ap_hidden_ssid.setText(self.__tr("Hidden SSID"))
        self.check_fake_ap_no_broadcast.setText(self.__tr("Disable broadcast probes"))
        self.check_fake_ap_all_probes.setText(self.__tr("Respond to all probes"))
        self.button_fake_ap_start.setText(self.__tr("Start Fake Access Point"))
        self.toolBox5.setItemLabel(self.toolBox5.indexOf(self.page1_3),self.__tr("Create Fake AP"))
        self.tabWidget2.changeTab(self.TabPage_4,self.__tr("Fake AP"))
        self.groupBox1_5.setTitle(self.__tr("Normal cracking"))
        self.textLabel10_4.setText(self.__tr("When you have enougth packets (>5000) you can try to decrypt the password."))
        self.button_crack_wep_aircrack.setText(self.__tr("Aircrack-ng - Decrypt WEP password"))
        self.toolBox5_3.setItemLabel(self.toolBox5_3.indexOf(self.page1_4),self.__tr("WEP cracking"))
        self.groupBox1_2_3.setTitle(self.__tr("Normal cracking"))
        self.textLabel11_2_4.setText(self.__tr("Add you dictionary:"))
        self.button_crack_wpa_aircrack.setText(self.__tr("Aircrack-ng - Crack WPA password"))
        self.groupBox1_3_3.setTitle(self.__tr("Pyrit cracking"))
        self.textLabel10_2_3.setText(self.__tr("<p align=\"center\">(For use it you need to install pyrit support)</p>"))
        self.textLabel11_2_2_3.setText(self.__tr("Add you dictionary:"))
        self.button_crack_wpa_pyrit.setText(self.__tr("Crack the password with pyrit"))
        self.toolBox5_3.setItemLabel(self.toolBox5_3.indexOf(self.page2_3),self.__tr("WPA bruteforce cracking"))
        self.groupBox1_3_3_2.setTitle(self.__tr("Rainbow Tables cracking"))
        self.textLabel10_2_3_2.setText(self.__tr("<p align=\"center\">(Get rainbow tables from http://www.renderlab.net/projects/WPA-tables/ )</p>"))
        self.textLabel11_2_2_3_2.setText(self.__tr("Add your rainbow tables file:"))
        self.button_crack_wpa_rainbow_tables.setText(self.__tr("Crack the password with coWPAtty and Rainbow Tables"))
        self.toolBox5_3.setItemLabel(self.toolBox5_3.indexOf(self.page_4),self.__tr("WPA rainbow tables cracking"))
        self.textLabel4_4_2_2_3.setText(self.__tr("<h2>Welcome in Cracking Control Panel</h2>"))
        self.tabWidget2.changeTab(self.TabPage_5,self.__tr("Cracking"))
        self.textLabel4.setText(self.__tr("<h2>KEY Database</h2>"))
        self.table_database.horizontalHeader().setLabel(0,self.__tr("Essid"))
        self.table_database.horizontalHeader().setLabel(1,self.__tr("Bssid"))
        self.table_database.horizontalHeader().setLabel(2,self.__tr("Channel"))
        self.table_database.horizontalHeader().setLabel(3,self.__tr("Key"))
        self.table_database.horizontalHeader().setLabel(4,self.__tr("Ascii (not saved)"))
        self.button_database_add.setText(self.__tr("Add entry"))
        self.button_database_delete.setText(self.__tr("Delete entry"))
        self.button_database_reload.setText(self.__tr("Reload"))
        self.button_database_save.setText(self.__tr("Save"))
        self.tabWidget2.changeTab(self.TabPage_6,self.__tr("Database"))
        self.textLabel14.setText(self.__tr("Authors:"))
        self.textLabel16.setText(self.__tr("Emanuele Gentili - emgent@backtrack-linux.org<br>\n"))
        self.textLabel17_2.setText(self.__tr("Emanuele Acri - crossbower@backtrack-linux.org\n"))
        self.tabWidget2.changeTab(self.TabPage_7,self.__tr("Credits"))


    def slot_wep_capture_req(self):
        print "Main_window.slot_wep_capture_req(): Not implemented yet"

    def slot_crack_wpa_aircrack(self):
        print "Main_window.slot_crack_wpa_aircrack(): Not implemented yet"

    def slot_crack_wpa_pyrit(self):
        print "Main_window.slot_crack_wpa_pyrit(): Not implemented yet"

    def slot_mac_restore(self):
        print "Main_window.slot_mac_restore(): Not implemented yet"

    def slot_monitor_on(self):
        print "Main_window.slot_monitor_on(): Not implemented yet"

    def slot_net_map_on(self):
        print "Main_window.slot_net_map_on(): Not implemented yet"

    def slot_wep_arp_inj_cfrag(self):
        print "Main_window.slot_wep_arp_inj_cfrag(): Not implemented yet"

    def slot_wep_arp_inj_chop(self):
        print "Main_window.slot_wep_arp_inj_chop(): Not implemented yet"

    def slot_wep_arp_inj_frag(self):
        print "Main_window.slot_wep_arp_inj_frag(): Not implemented yet"

    def slot_wep_create_arp_cfrag(self):
        print "Main_window.slot_wep_create_arp_cfrag(): Not implemented yet"

    def slot_wep_create_arp_chop(self):
        print "Main_window.slot_wep_create_arp_chop(): Not implemented yet"

    def slot_wep_create_arp_frag(self):
        print "Main_window.slot_wep_create_arp_frag(): Not implemented yet"

    def slot_wep_start_chop(self):
        print "Main_window.slot_wep_start_chop(): Not implemented yet"

    def slot_wep_start_frag(self):
        print "Main_window.slot_wep_start_frag(): Not implemented yet"

    def slot_wep_start_rep(self):
        print "Main_window.slot_wep_start_rep(): Not implemented yet"

    def slot_wep_test_inj(self):
        print "Main_window.slot_wep_test_inj(): Not implemented yet"

    def slot_wpa_deauth_hand(self):
        print "Main_window.slot_wpa_deauth_hand(): Not implemented yet"

    def slot_wpa_start_sniff_hand(self):
        print "Main_window.slot_wpa_start_sniff_hand(): Not implemented yet"

    def slot_crack_wep_aircrack(self):
        print "Main_window.slot_crack_wep_aircrack(): Not implemented yet"

    def slot_crack_wpa_rainbow_tables(self):
        print "Main_window.slot_crack_wpa_rainbow_tables(): Not implemented yet"

    def slot_wep_start_hirte_adhoc(self):
        print "Main_window.slot_wep_start_hirte_adhoc(): Not implemented yet"

    def slot_wep_start_hirte_ap(self):
        print "Main_window.slot_wep_start_hirte_ap(): Not implemented yet"

    def slot_wep_start_latte(self):
        print "Main_window.slot_wep_start_latte(): Not implemented yet"

    def slot_mac_change(self):
        print "Main_window.slot_mac_change(): Not implemented yet"

    def slot_gath_int(self):
        print "Main_window.slot_gath_int(): Not implemented yet"

    def slot_save_ap_name(self):
        print "Main_window.slot_save_ap_name(): Not implemented yet"

    def slot_save_mon(self):
        print "Main_window.slot_save_mon(): Not implemented yet"

    def slot_save_mon_mac(self):
        print "Main_window.slot_save_mon_mac(): Not implemented yet"

    def slot_line_crack_wep_log(self):
        print "Main_window.slot_line_crack_wep_log(): Not implemented yet"

    def slot_line_crack_wpa_dictionary(self):
        print "Main_window.slot_line_crack_wpa_dictionary(): Not implemented yet"

    def slot_line_crack_wpa_dictionary_pyrit(self):
        print "Main_window.slot_line_crack_wpa_dictionary_pyrit(): Not implemented yet"

    def slot_line_crack_wpa_log_pyrit(self):
        print "Main_window.slot_line_crack_wpa_log_pyrit(): Not implemented yet"

    def slot_line_crack_wpa_rainbow_tables_file(self):
        print "Main_window.slot_line_crack_wpa_rainbow_tables_file(): Not implemented yet"

    def slot_line_gath_logs(self):
        print "Main_window.slot_line_gath_logs(): Not implemented yet"

    def slot_line_mac_change_int(self):
        print "Main_window.slot_line_mac_change_int(): Not implemented yet"

    def slot_line_mac_change_mac(self):
        print "Main_window.slot_line_mac_change_mac(): Not implemented yet"

    def slot_line_wep_mac_cfrag(self):
        print "Main_window.slot_line_wep_mac_cfrag(): Not implemented yet"

    def slot_line_wpa_mac_hand(self):
        print "Main_window.slot_line_wpa_mac_hand(): Not implemented yet"

    def slot_spin_wep_wired_req(self):
        print "Main_window.slot_spin_wep_wired_req(): Not implemented yet"

    def slot_spin_wep_wireless_req(self):
        print "Main_window.slot_spin_wep_wireless_req(): Not implemented yet"

    def slot_line_wpa_deauth_hand(self):
        print "Main_window.slot_line_wpa_deauth_hand(): Not implemented yet"

    def slot_start_sniffing(self):
        print "Main_window.slot_start_sniffing(): Not implemented yet"

    def slot_autoload_ap_info(self):
        print "Main_window.slot_autoload_ap_info(): Not implemented yet"

    def slot_gath_clean(self):
        print "Main_window.slot_gath_clean(): Not implemented yet"

    def slot_enable_ip_forward(self):
        print "Main_window.slot_enable_ip_forward(): Not implemented yet"

    def slot_fake_ap_start(self):
        print "Main_window.slot_fake_ap_start(): Not implemented yet"

    def slot_save_ap_mac(self):
        print "Main_window.slot_save_ap_mac(): Not implemented yet"

    def slot_save_ap_chan(self):
        print "Main_window.slot_save_ap_chan(): Not implemented yet"

    def slot_reload_interfaces(self):
        print "Main_window.slot_reload_interfaces(): Not implemented yet"

    def slot_autoload_victim_clients(self):
        print "Main_window.slot_autoload_victim_clients(): Not implemented yet"

    def slot_rescan_networks(self):
        print "Main_window.slot_rescan_networks(): Not implemented yet"

    def slot_interface_selected(self):
        print "Main_window.slot_interface_selected(): Not implemented yet"

    def slot_network_selected(self):
        print "Main_window.slot_network_selected(): Not implemented yet"

    def slot_disable_ip_forward(self):
        print "Main_window.slot_disable_ip_forward(): Not implemented yet"

    def slot_random_mac(self):
        print "Main_window.slot_random_mac(): Not implemented yet"

    def slot_line_database(self):
        print "Main_window.slot_line_database(): Not implemented yet"

    def slot_database_delete(self):
        print "Main_window.slot_database_delete(): Not implemented yet"

    def slot_database_reload(self):
        print "Main_window.slot_database_reload(): Not implemented yet"

    def slot_database_save(self):
        print "Main_window.slot_database_save(): Not implemented yet"

    def slot_database_add(self):
        print "Main_window.slot_database_add(): Not implemented yet"

    def slot_database_changed(self):
        print "Main_window.slot_database_changed(): Not implemented yet"

    def slot_fake_auth(self):
        print "Main_window.slot_fake_auth(): Not implemented yet"

    def slot_wep_client_frag(self):
        print "Main_window.slot_wep_client_frag(): Not implemented yet"

    def slot_test_inj(self):
        print "Main_window.slot_test_inj(): Not implemented yet"

    def slot_monitor(self):
        print "Main_window.slot_monitor(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("Main_window",s,c)
