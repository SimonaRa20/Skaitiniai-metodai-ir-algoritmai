import matplotlib.pyplot as plt
import numpy as np
from task2splainu import Hermite

def s(i,A):
    n=len(A)
    global t 
    if i==-1:
        return 2*s(0,A)-s(1,A)
    elif i==-2:
        return 2*s(-1,A)-s(0,A)
    elif i==n-1:
        return 2*s(n-2,A)-s(n-3,A)
    elif i==n:
        return 2*s(n-1,A)-s(n-2,A)
    else:
        return(A[i+1]-A[i])/(t[i+1]-t[i])

def w1(i,A):
    return np.abs(s(i+1,A)-s(i,A))

def w2(i,A):
    return np.abs(s(i-1,A)-s(i-2,A))

def d(i,A):
    W1=w1(i,A)
    W2=w2(i,A)
    
    return W1/(W1+W2)*s(i-1,A)+W2/(W1+W2)*s(i,A)

def akima(A):
    n=len(A)
    dA=[]
    for i in range(n):
        dA.append(d(i,A))
        
    return dA

X=[-54.08080455699991, -54.11428910399985, -54.140023966999934, -54.17655920499996, -54.190460164999934, -54.21118241399998, -54.18797969599987, -54.17707596799991, -54.17469885299997, -54.1770242929999, -54.17945308399996, -54.1840006109999, -54.188496459999925, -54.190666869999916, -54.18854813699994, -54.17919470299998, -54.1770242929999, -54.170874796999925, -54.16916947399997, -54.17361364799987, -54.18513749199991, -54.179763143999935, -54.16875606299996, -54.1634333909999, -54.16296830299987, -54.170203002999955, -54.17325191299997, -54.18704951999993, -54.190666869999916, -54.191338663999886, -54.18963334199992, -54.18338049399992, -54.170203002999955, -54.182191935999896, -54.188909871999925, -54.20472285999992, -54.21252600199995, -54.28533809499993, -54.320426391999945, -54.35944209799996, -54.375616821999955, -54.42346919799988, -54.435458130999905, -54.45054764799991, -54.472613484999926, -54.483310505999924, -54.49338741099987, -54.52031083199998, -54.53157629399993, -54.551161661999856, -54.58475134299988, -54.59922074399992, -54.615292114999875, -54.63412817399998, -54.65337764499992, -54.672859659999915, -54.69249670499994, -54.70412390199991, -54.70655269399987, -54.70544165099997, -54.706733561999926, -54.71569942299996, -54.70996333799991, -54.70727616399998, -54.70203100599994, -54.69725093599993, -54.69559728999991, -54.69683752399993, -54.701100830999906, -54.7025477709999, -54.70319372599997, -54.70766373799998, -54.72117712399995, -54.7430362559999, -54.759805256999954, -54.775494351999896, -54.79249060099991, -54.84191910799987, -54.88028885999998, -54.9785774339999, -54.98281490099993, -54.979559285999954, -54.960232299999916, -54.95366939299993, -54.95909541799989, -54.97687211099992, -55.01774816999992, -55.03774694899997, -55.076297566999926, -55.112471069999884, -55.12089432799985, -55.12885249899992, -55.13660396399993, -55.13308996599997, -55.137792521999955, -55.17195064299992, -55.25191992199987, -55.275251831999896, -55.28698238199988, -55.302795369999984, -55.320520385999885, -55.33775447699989, -55.35452347799992, -55.36007869499994, -55.36276586899987, -55.37105993699993, -55.39958532799997, -55.435552124999845, -55.47430944899989, -55.511309773999926, -55.5682055259999, -55.58732580599988, -55.60830643699998, -55.64538427699995, -55.72429418999991, -55.74411210199989, -55.754602416999944, -55.76612626199997, -55.773567667999885, -55.783127807999904, -55.853769490999895, -55.870667683999955, -55.925031290999954, -55.947200479999964, -55.971023315999844, -55.983012248999984, -55.989239257999884, -55.99691320899987, -56.007506876999855, -56.00817867099994, -56.01334631399993, -56.04256933699989, -56.05024328699997, -56.06215470399991, -56.073420166999966, -56.08228267399997, -56.09145524099995, -56.103780069999914, -56.11680253099985, -56.13199540299988, -56.14388098099991, -56.14677486199989, -56.13525101799988, -56.09145524099995, -56.07292923999992, -56.054015665999884, -56.044843099999895, -56.031329711999916, -56.004406290999924, -55.99577632699996, -55.95996455899993, -55.92580643799994, -55.91826167799991, -55.91513525399995, -55.91676306199989, -55.92038041299989, -55.92358435099996, -55.92234411599992, -55.91676306199989, -55.92203405799992, -55.95381506399988, -56.01965083799985, -56.082644408999954, -56.14527624499988, -56.20976843299991, -56.2579308679999, -56.273795531999895, -56.29270910699995, -56.32862422699989, -56.34795121299996, -56.367174845999955, -56.396527058999936, -56.41518225099992, -56.42980668199991, -56.481819010999914, -56.48510046399991, -56.491198282999875, -56.49998327699987, -56.52096390899996, -56.52938716699995, -56.53649267599988, -56.5420737309999, -56.57977168799994, -56.677801879999976, -56.70519038899991, -56.80146358199997, -56.80874995999994, -56.816346395999915, -56.8261907559999, -56.83887731899995, -56.84779150399996, -56.87086503099994, -56.88014095099996, -56.884430093999924, -56.88388749199987, -56.8950496009999, -56.93083553099993, -56.93845780399991, -56.93202408899995, -56.93024125199986, -56.93507299799998, -56.951635294999875, -56.95636368899994, -56.95959346499993, -56.95752640899988, -56.95261714699993, -56.951273559999976, -56.95959346499993, -56.980005655999975, -56.99411332199992, -57.000572875999865, -56.99530188099993, -56.99711055599994, -57.02238033099991, -57.027237914999915, -57.027909708999914, -57.023155476999904, -57.02046830299989, -57.027237914999915, -57.04801184099995, -57.05597001199993, -57.061964477999936, -57.071886352999854, -57.097724568999865, -57.102943887999885, -57.09901647999993, -57.09214351499995, -57.089869750999924, -57.09953324399996, -57.13374304299995, -57.13705033399995, -57.14366491699985, -57.126404988999866, -57.13338130699995, -57.145215209999975, -57.165265665999925, -57.17461909999986, -57.186608031999924, -57.19105220599994, -57.19425614499991, -57.202265991999866, -57.20634842999988, -57.21962927299998, -57.210327514999875, -57.19472123199992, -57.183817504999865, -57.188623412999874, -57.221851358999885, -57.23461543799996, -57.22645056199994, -57.221179564999915, -57.22179968299989, -57.224693562999875, -57.22645056199994, -57.22324662299988, -57.209242309999865, -57.20598669499989, -57.207020223999876, -57.211774455999944, -57.212859659999936, -57.2222130939999, -57.239473022999874, -57.24856807499995, -57.233323526999925, -57.23673417199984, -57.237405965999926, -57.23761267099988, -57.239473022999874, -57.24624263599992, -57.25497595199991, -57.2648978279999, -57.2749230549999, -57.28603348899992, -57.284173136999925, -57.277713582999866, -57.2749230549999, -57.285671752999946, -57.287945516999855, -57.28711869299994, -57.281744344999964, -57.280452433999926, -57.28401810699998, -57.29027095599989, -57.292493041999904, -57.28422481399994, -57.28277787299996, -57.280452433999926, -57.28355301999994, -57.3084093839999, -57.340035359999916, -57.366752075999955, -57.39346879099992, -57.42504309099991, -57.423957886999915, -57.430934204999915, -57.459201212999886, -57.46168168199995, -57.46876135299988, -57.47625443599992, -57.479716755999874, -57.48204219599998, -57.4879849859999, -57.49583980399984, -57.50390132699994, -57.509637410999886, -57.522401489999964, -57.535268920999954, -57.545035766999916, -57.554234171999894, -57.565137898999865, -57.596192593999945, -57.59640214099997, -57.61324865799995, -57.6414639889999, -57.64993892399991, -57.65484818599995, -57.65820715299995, -57.66254797399992, -57.66461503199989, -57.663994913999915, -57.658930623999936, -57.658362182999895, -57.660532592999886, -57.66068762199993, -57.645494751999905, -57.64404781199991, -57.66042924099986, -57.68125484199993, -57.685130574999874, -57.687249307999934, -57.697998005999864, -57.70285559099989, -57.7073514409999, -57.708643351999854, -57.70952185099989, -57.717480021999876, -57.72249263599991, -57.7261099859999, -57.764247192999875, -57.81313309799995, -57.82977290899987, -57.84098669399992, -57.84692948499992, -57.84961665899996, -57.85385412699992, -57.8751448159999, -57.925839396999976, -57.94211747299991, -58.00790157099996, -58.03213781699995, -58.042008015999926, -58.05508215299989, -58.067691202999924, -58.065934203999944, -58.05203324399986, -57.96495845599989, -57.95384802299989, -57.94738846899992, -57.945269734999954, -57.9480602619999, -57.95348628799988, -57.95663854999995, -57.95265946399988, -57.94278926699988, -57.93131709799988, -57.921860310999904, -57.914470580999875, -57.89607377099989, -57.879123901999975, -57.86331091399998, -57.84543086799994, -57.837421020999955, -57.836025756999874, -57.84434566299993, -57.871165730999905, -57.88454992699985, -57.90113806199986, -57.91782954999991, -57.92537430899995, -57.918501342999974, -57.902429972999926, -57.884188191999954, -57.87070064399998, -57.850340128999875, -57.84279536999992, -57.83023799599991, -57.820574503999865, -57.810962687999876, -57.79845699099988, -57.77396236199991, -57.762335164999854, -57.74729732299997, -57.720477253999974, -57.68693924999988, -57.649370482999956, -57.610096394999886, -57.566223103999874, -57.54327876799994, -57.51759558099985, -57.512221232999906, -57.49687333199992, -57.490258748999935, -57.47733963999991, -57.460493122999935, -57.381376505999924, -57.35621008399991, -57.345513060999906, -57.33807165499988, -57.32944169199993, -57.31523067199987, -57.30649735599991, -57.298694214999955, -57.290477660999926, -57.280452433999926, -57.31693599499994, -57.32143184399985, -57.32019160999991, -57.317091023999865, -57.302208211999925, -57.29554195199992, -57.288979044999934, -57.277713582999866, -57.25993688999995, -57.24727616399991, -57.23874955299988, -57.233323526999925, -57.217768921999976, -57.20200760899991, -57.18981197199989, -57.184902709999875, -57.19239579299989, -57.22572709199994, -57.23252170199993, -57.233323526999925, -57.23761267099988, -57.2476378989999, -57.25900671399998, -57.26742997299988, -57.26918697199994, -57.26401932799985, -57.253787394999875, -57.25642289299989, -57.26303747599988, -57.27166743999993, -57.280452433999926, -57.28546504799988, -57.28727372299997, -57.28882401599989, -57.29202795499987, -57.29833247899998, -57.3084093839999, -57.32282710799993, -57.33171545499994, -57.33569453899992, -57.332283894999904, -57.32411901899988, -57.27549149599989, -57.26520788599987, -57.2612288009999, -57.260091918999876, -57.25693965699992, -57.24767005099994, -57.23399817599994, -57.22508704299992, -57.193023240999935, -57.17951412699995, -57.17015540299991, -57.16368567599994, -57.13963782499991, -57.134877081999946, -57.12800045499995, -57.12576991299994, -57.11384695299995, -57.10228335599993, -57.07579505099994, -57.07164466099994, -57.06602942599994, -57.05768795499995, -57.034820115999935, -57.027902798999946, -57.022694464999915, -57.01744544199994, -57.01280676999994, -57.000111456999946, -56.99449622299994, -56.98468990799995, -56.974598761999914, -56.96387174799992, -56.95653728299993, -56.92884361699993, -56.866972319999945, -56.83035597899993, -56.7807244249999, -56.70263103499991, -56.65951168499993, -56.642432053999926, -56.61142173999991, -56.59310418799993, -56.57395023099991, -56.52685903299994, -56.41831440699991, -56.355023984999946, -56.303806599999916, -56.256765973999904, -56.22283396699993, -56.19163977799991, -56.124256964999915, -56.083036283999945, -56.05859455299992, -56.037993943999936, -55.99918207299993, -55.93600595099991, -55.91787675699993, -55.903553839999915, -55.897694464999915, -55.897694464999915, -55.897246873999904, -55.89024817599994, -55.88499915299991, -55.88329016799992, -55.884022589999915, -55.887277798999946, -55.90453040299991, -55.91536159299994, -55.89996263099994, -55.910002851999934, -55.922245296999904, -55.933958685999926, -55.94787193199994, -55.951168793999955, -55.9466686209999, -55.93043306399994, -55.92361255299994, -55.91039502299992, -55.90065382699993, -55.886051934999955, -55.86799044599991, -55.844381978999934, -55.8200945289999, -55.729088531999935, -55.678578253999945, -55.63731848899994, -55.394987880999906, -55.33596733599995, -55.307870814999944, -55.29204537399994, -55.270822719999956, -55.263783331999946, -55.25320390499991, -55.24290930899991, -55.23289954299992, -55.22976640499991, -55.22142493399991, -55.212880011999914, -55.20243289399991, -55.18836054199994, -55.17690766699991, -55.164051886999914, -55.14784048599995, -55.13072689299992, -55.11082923099991, -55.10310721299993, -55.1151012119999, -55.12987219999991, -55.12861080599993, -55.10103935899991, -55.09171227799993, -55.090748842999915, -55.08551998599995, -55.063423422999904, -55.03038489499994, -55.01012122299994, -54.99705969999991, -54.98892167899993, -54.98119055899991, -54.95881100199995, -54.95030676999994, -54.94180253799993, -54.93195553299995, -54.92414303299995, -54.91869055899991, -54.91197669199994, -54.90025794199994, -54.89077714799993, -54.88072669199994, -54.86302649599992, -54.86754309799994, -54.874338344999956, -54.88219153599994, -54.890288865999935, -54.90347245999993, -54.91258039499991, -54.92185060699995, -54.93331850699991, -54.956207495999934, -54.971565503999955, -54.98563364599994, -55.0015167599999, -55.01659094999991, -55.03172766799992, -55.04727128799993, -55.10529537699995, -55.12564042899993, -55.14297441299993, -55.150380011999914, -55.15412350199995, -55.15996561999992, -55.15332344099994, -55.14449955899994, -55.116851365999935, -55.085301141999935, -55.0447990049999, -55.01390540299991, -54.77358964799993, -54.75536048099991, -54.712555109999926, -54.67355600999991, -54.471780922999926, -54.34863012599993, -54.252699443999916, -54.16934160099993, -54.09739562699991, -54.0744563099999, -54.06203176999992, -54.03673144499993, -54.03094366199991, -54.02046226899995, -54.01468747699994, -54.01630686199991, -53.992085009999926, -53.986357453999915, -53.99592037699995, -54.0197529269999, -54.03114763399992, -54.03643877499991, -54.05036373599995, -54.061105923999946, -54.07359778599994, -54.091786261999914, -54.10912024599992, -54.118478969999956, -54.12254798099991, -54.12852942599994, -54.17096920499995, -54.190460164999934, -54.269163370999934, -54.311331339999896, -54.32065194299989, -54.332001912999914, -54.34357743299995, -54.350036986999896, -54.36543656399991, -54.36988073799989, -54.37230952999997, -54.375616821999955, -54.430238810999896, -54.44863561999989, -54.45478511599987, -54.45757564299993, -54.44884232599995, -54.4508060309999, -54.45550858599995, -54.48212194899989, -54.486721150999955, -54.48496415299988, -54.47865962699987, -54.47865962699987, -54.475404011999956, -54.46729081299986, -54.45700720299996, -54.44734370899994, -54.435458130999905, -54.43514807099993, -54.43855871599996, -54.43773189399994, -54.42527787299994, -54.42346919799988, -54.42346919799988, -54.42817175299993, -54.44796382699991, -54.4508060309999, -54.433442748999965, -54.4029536539999, -54.39411698399988, -54.39318680899993, -54.39959468599997, -54.410550089999845, -54.40657100399997, -54.3948921299999, -54.38248978699991, -54.34890010599989, -54.3385648199999, -54.33468908699993, -54.33758296699992, -54.351018839999966, -54.35515295399989, -54.35386104299994, -54.34435258099995, -54.31019445899997, -54.30388993399987, -54.29314123599994, -54.28647497599994, -54.27252233899995, -54.26580440299992, -54.24105139199989, -54.22224117099998, -54.21800370299994, -54.21454138199991, -54.20704829899995, -54.19748815999995, -54.1873595779999, -54.18162349499994, -54.170203002999955, -54.13609655799988, -54.12550288999989, -54.10478063999997, -54.094445352999855, -54.07403316299991, -54.05067541599996, -54.05010697499992, -54.039409952999904, -54.02840287299992, -54.01786088099996, -54.00881750499991, -53.994813191999896, -53.98881872599986, -53.99026566599986, -53.998275512999925, -54.00628535999991, -54.003029744999935, -54.01935949799986, -54.055688028999924, -54.06033890799989, -54.06271602399994, -54.06948563699987, -54.080234334999915, -54.08080455699991,]
Y=[3.3093140290000918, 3.2853819790001353, 3.2450226850000803, 3.200580953000099, 3.1781017050000884, 3.127407125000019, 3.130972799000091, 3.1165550740000754, 3.0939207970001092, 3.0727851360000784, 3.070304668000105, 3.0679792280000697, 3.064620260000055, 3.059142558000076, 3.0583157350000505, 3.0515977990001204, 3.04891062500009, 3.0248294070001407, 3.0107217410001113, 3.004520569000121, 2.9978026330001057, 2.9837466430000887, 2.9713959760000392, 2.9697423300000736, 2.9559963990000426, 2.9254039510001206, 2.919512837000127, 2.89930735300004, 2.887835185000114, 2.8773448700000728, 2.870626933000054, 2.8638573200001076, 2.8530569460000805, 2.846545716000108, 2.8382774860000666, 2.791768698000027, 2.776420797000057, 2.6779771930001033, 2.606663717000032, 2.5080134080001244, 2.483777161000134, 2.4359247840000364, 2.431118876000127, 2.428948466000051, 2.428690084000067, 2.4228506470000895, 2.41706288600011, 2.348901672000096, 2.340168356000021, 2.338101298000055, 2.348333231000126, 2.345801087000055, 2.3262673960000484, 2.3201179000000707, 2.316500550000086, 2.315983785000057, 2.318981018000059, 2.324820455000051, 2.3328819790001347, 2.3425454720000687, 2.3531908160000654, 2.375928446000046, 2.3947903440000573, 2.3958755500000564, 2.3957205200001113, 2.3973224900000503, 2.403523661000037, 2.4091047160000585, 2.4199050900000856, 2.4257445280000667, 2.4458466600001287, 2.450342509000052, 2.4579906210001212, 2.4665172330000473, 2.465793762000146, 2.4573352940000888, 2.448172099000061, 2.4334959920000756, 2.447345276000135, 2.543050029000142, 2.5523517860000737, 2.5660977180001083, 2.5856830860001168, 2.5990672810000603, 2.6089891560000638, 2.6069220990001014, 2.590592346000065, 2.5779316200001148, 2.5452204390000333, 2.527805481000101, 2.5248082480000846, 2.5256867470001225, 2.533799948000123, 2.5528685510001026, 2.562170309000038, 2.5593281050000627, 2.497884827000078, 2.499331767000072, 2.5139045210001143, 2.51969228100009, 2.518297018000027, 2.5112690230001107, 2.494887594000062, 2.476232402000093, 2.457938945000109, 2.442539368000041, 2.4301887000000733, 2.4308604940000578, 2.4358214310001074, 2.4363898720000634, 2.4312739060000723, 2.433857727000074, 2.4339610800001026, 2.4166494750000993, 2.396909078000135, 2.4010431930000635, 2.40941477500013, 2.4312739060000723, 2.4400588990000642, 2.445174866000059, 2.462641500000089, 2.470909729000141, 2.515661519000105, 2.5281672160000994, 2.5303376260000903, 2.5264618940001355, 2.5208291620000125, 2.503259176000128, 2.4606777950000662, 2.416287740000101, 2.3988211060000566, 2.355102844000072, 2.3470413210000913, 2.341563619000098, 2.3423904420001236, 2.347713115000076, 2.351898906000102, 2.3490567020000412, 2.3330886840000886, 2.30435658800009, 2.2747459920000495, 2.256194153000095, 2.2485460410000258, 2.2459105430001074, 2.2415180460001096, 2.2240514120000654, 2.1847256470000787, 2.163486634000108, 2.144986471000081, 2.1373900350001236, 2.090984599000109, 2.0616840620000545, 2.050392761000083, 2.037654521000121, 2.0285077930000455, 2.0193869020000648, 2.006596985000087, 1.9621552540000238, 1.9222352100000677, 1.8862167360000797, 1.8532730110000273, 1.8335067750000604, 1.8465550740000936, 1.8717731730000509, 1.8885421760000156, 1.8856482950001237, 1.8875086470000326, 1.8954668170000843, 1.9184628300000384, 1.926601868000148, 1.9288756310000679, 1.9216667690001117, 1.9197030640000747, 1.9227002980000947, 1.9416138710001292, 1.9532152310000868, 1.962904562000105, 1.9699842320000442, 1.9767280070000766, 1.9817922980000446, 1.9886394250001018, 1.9971660360001238, 2.0168030800000594, 2.018405050000098, 2.0296446740000533, 2.165967103000085, 2.1957844040000936, 2.21759185800002, 2.2616718550000883, 2.2811021930000663, 2.2858564250000626, 2.290145569000032, 2.294796448000085, 2.3037364710001214, 2.3397549440001058, 2.3620791630000753, 2.393291728000051, 2.411430155000076, 2.425796204000079, 2.4361831670001095, 2.445898336000141, 2.4612462360001075, 2.470031230000103, 2.483777161000134, 2.4934923300000804, 2.5045510860000775, 2.5154548140000514, 2.524704895000056, 2.5097187300000883, 2.504861146000067, 2.5141629030000985, 2.547855937000051, 2.555142314000122, 2.58454620400002, 2.593589580000071, 2.6105911250000986, 2.623665263000049, 2.6354474890000574, 2.6482115680001073, 2.6364810180000404, 2.6423721310000303, 2.681749573000033, 2.7000947070001047, 2.72737986200012, 2.740454000000085, 2.750375875000074, 2.7630366010001097, 2.7738886520000676, 2.778591207000133, 2.7734235640000406, 2.7711498010001208, 2.7900116980000433, 2.826030171000127, 2.832593078000116, 2.8304226690001144, 2.8210692340000776, 2.818950501000103, 2.8232396440000684, 2.832593078000116, 2.8419981890000656, 2.846235657000122, 2.8565709430000368, 2.908299052000089, 2.9182209270000783, 2.9306232710000586, 2.9446792610000756, 2.959510397000102, 2.9630243940000582, 2.9703624480000457, 2.9833849080000903, 2.9925833130000825, 3.0004381310001094, 3.009171448000089, 3.021263733000083, 3.0247777300000394, 3.024054261000046, 3.0281366990000436, 3.0356814580000986, 3.048342184000134, 3.056041972000031, 3.0782628380000716, 3.094127503000081, 3.1123692830001204, 3.1416698200000894, 3.143478495000082, 3.1439952600000254, 3.1448737590000633, 3.1478709920000796, 3.141618144000077, 3.1358303840001014, 3.1326264440000386, 3.134280091000079, 3.14239329100009, 3.148956197000075, 3.156914368000045, 3.169006653000025, 3.1921060180000893, 3.203113099000092, 3.215360412000024, 3.2359276320000987, 3.2478132120000396, 3.259750468000078, 3.2679670210001035, 3.2762869260000684, 3.288792623000063, 3.2950454710000656, 3.3297720340001007, 3.343802185000115, 3.3949101770000993, 3.3701571660000695, 3.3656096390000414, 3.3738261930000704, 3.387494609000086, 3.3693820190000707, 3.360622864000078, 3.3533364870001066, 3.349977518000088, 3.3431820680001323, 3.338944601000094, 3.343388774000104, 3.348556417000097, 3.351527812000114, 3.352974752000108, 3.3533364870001066, 3.3576773070000883, 3.365247904000043, 3.367780050000121, 3.348143006000086, 3.3467477420000193, 3.349822490000051, 3.3671207240001024, 3.367237447000079, 3.376642558000043, 3.3824303180000186, 3.38594431500006, 3.390130107000104, 3.3952202350000817, 3.407079976000105, 3.4175444540000512, 3.4258385210001023, 3.44389943500002, 3.450617371000135, 3.462993877000102, 3.4695051070000744, 3.4989865110000835, 3.5166598510000853, 3.5351858520000263, 3.5473039760001086, 3.5491643270001134, 3.5521615600000302, 3.553608500000024, 3.5556755580000754, 3.5606623340001278, 3.564124654000082, 3.567690329000044, 3.582443950000055, 3.5999622600000265, 3.607196961000085, 3.6315882360000984, 3.6518453980001055, 3.66243906600009, 3.680990906000119, 3.7021007290000654, 3.747472636000097, 3.7666704300001044, 3.812197368000085, 3.8864047240000446, 3.905447490000114, 3.9572789510000916, 3.987716370000072, 4.023037211000073, 4.108070780000077, 4.151143087000079, 4.171839498000097, 4.19310435000007, 4.282039490000045, 4.299015198000049, 4.318755595000113, 4.3439220180000575, 4.360484314000061, 4.375703024000089, 4.391438497000067, 4.409731954000037, 4.425105693000106, 4.437843933000067, 4.450943909000031, 4.484068502000127, 4.528510234000109, 4.556828918000093, 4.607730204000035, 4.633516744000133, 4.650880025000063, 4.669845276000018, 4.687518616000105, 4.721728414000012, 4.762862854000076, 4.773921611000091, 4.782370707000084, 4.796142476000028, 4.829757996000055, 4.852728170000091, 4.872261861000098, 4.888927511000134, 4.922801412000041, 4.929881083000069, 4.9330591840000295, 4.930294495000069, 4.925540263000087, 4.9230597950001, 4.926444601000128, 4.935539653000092, 4.964013367000035, 4.98979990600013, 5.006258851000027, 5.008429260000099, 4.991350199000067, 5.007085673000049, 5.01109059700012, 5.012434184000085, 5.0091527310001, 4.994657491000069, 4.991350199000067, 4.992487081000078, 4.997628886000072, 5.005742086000069, 5.012434184000085, 5.0166199750001255, 5.02075408900015, 5.024087220000055, 5.026102600000101, 5.024448955000054, 5.021115824000049, 5.020289001000037, 5.026102600000101, 5.058968811000042, 5.070156759000071, 5.0834117640000756, 5.0947547410000595, 5.128473612000022, 5.1572057090000385, 5.171029155000085, 5.176920268000089, 5.176300150000117, 5.17237274200005, 5.1620116170001324, 5.142116191000127, 5.148549907000074, 5.157619121000039, 5.169220480000092, 5.183147278000078, 5.203171896000114, 5.243608704000096, 5.260572120000077, 5.262573954000061, 5.268723450000039, 5.271772360000057, 5.271203919000101, 5.266294657000074, 5.25670867900007, 5.247045186000136, 5.234927063000043, 5.2282866410000395, 5.22399749700007, 5.222860616000062, 5.225341085000139, 5.230818787000118, 5.238699442000069, 5.3085401410000514, 5.311330668000011, 5.311020610000114, 5.313475240000088, 5.307609965000097, 5.307609965000097, 5.316885885000104, 5.32786712700009, 5.3385899870001055, 5.387398377000068, 5.403366395000106, 5.426749980000068, 5.448195699000095, 5.464086202000104, 5.484930731000077, 5.498968817000048, 5.507513739000046, 5.519720770000049, 5.5305850280000755, 5.542792059000078, 5.557074286000045, 5.665106512000079, 5.759914455000057, 5.793158270000049, 5.818145202000039, 5.858844279000039, 5.886415857000088, 5.92999909100007, 5.941229559000078, 5.950100002000056, 5.955877997000073, 5.959906317000048, 5.9644229190000715, 5.968939520000049, 5.970933335000041, 5.973863023000092, 5.987982489000046, 5.9926618510000935, 5.996283270000049, 5.998114325000074, 6.009151948000067, 6.011573766000083, 6.004262377000089, 5.989636515000086, 5.985556838000093, 5.985508468000091, 5.982190205000052, 5.979715570000053, 5.973222757000087, 5.953646911000078, 5.945752637000055, 5.940756315000044, 5.936548576000064, 5.911349189000077, 5.894670237000071, 5.8925079290000895, 5.880405812000049, 5.870753118000039, 5.8626162780000755, 5.848049221000053, 5.8343659570000455, 5.8277373120000675, 5.824164130000042, 5.810712549000073, 5.804660631000047, 5.7847354190000715, 5.776353257000039, 5.7630069030000755, 5.676703192000048, 5.676703192000048, 5.676703192000048, 5.692450262000079, 5.708075262000079, 5.741929429000038, 5.759466864000046, 5.79718659100007, 5.821770989000072, 5.841963548000081, 5.850917821000053, 5.850352823000037, 5.849827132000087, 5.861520820000067, 5.881510800000058, 5.896492641000066, 5.91758029500005, 5.927844941000046, 5.9416155530000765, 5.951945171000091, 5.962954274000083, 5.969812878000084, 5.975961707000067, 5.977274794000039, 5.981216439000093, 5.985256252000056, 5.9859072940000715, 5.9738760030000435, 5.962708199000076, 5.943349544000057, 5.936726952000072, 5.92999909100007, 5.92641836100006, 5.917792059000078, 5.909369208000044, 5.903265692000048, 5.902411200000074, 5.900213934000078, 5.900213934000078, 5.898761043000093, 5.897395008000046, 5.9012900010000635, 5.906683661000045, 5.908177475000059, 5.89585543600009, 5.88117096600007, 5.866412291000074, 5.837128193000069, 5.820746161000045, 5.821356512000079, 5.830499325000062, 5.852791383000067, 5.875116669000079, 5.882798570000091, 5.882882815000073, 5.859767971000053, 5.855536200000074, 5.858465887000079, 5.863674221000053, 5.865464585000041, 5.851792710000041, 5.850287177000041, 5.852118231000077, 5.855536200000074, 5.860419012000079, 5.867092190000051, 5.872870184000078, 5.875392971000053, 5.87335846600007, 5.868353583000044, 5.855536200000074, 5.863674221000053, 5.8715681010000935, 5.87836334800005, 5.882798570000091, 5.88540273600006, 5.8840249680000625, 5.876625344000047, 5.869671869000058, 5.867574735000062, 5.877266689000066, 5.880387456000051, 5.871258979000061, 5.871975002000056, 5.884466864000046, 5.892279364000046, 5.9089216170000896, 5.918646552000041, 5.930121161000045, 5.94086334800005, 5.951361395000049, 5.958113974000071, 5.968592041000079, 5.974247897000055, 5.985256252000056, 5.990649034000057, 5.99310494100007, 5.993394273000092, 5.985256252000056, 5.9809431010000935, 5.976183871000046, 5.96919162800009, 5.9409698500000445, 5.913755159000061, 5.894808339000065, 5.8679059920000896, 5.84733938100004, 5.84488748800004, 5.84055851800008, 5.842350790000069, 5.834184262000065, 5.830250206000073, 5.820148403000076, 5.809703943000045, 5.76349738600004, 5.745664571000077, 5.734523830000057, 5.688979194000069, 5.669309742000053, 5.62950234200008, 5.5520694030000755, 5.512884833000044, 5.4898135440000715, 5.467922268000052, 5.452826239000046, 5.442775783000059, 5.433417059000078, 5.414292710000041, 5.3483747420000896, 5.3257483930001115, 5.269085185000037, 5.225806173000066, 5.212454410000049, 5.196195577000111, 5.156378886000098, 5.149583436000057, 5.138757222000024, 5.132375183000079, 5.121058045000012, 5.114882711000035, 5.053387757000024, 5.024293925000023, 5.0085326130000425, 4.991350199000067, 4.951481832000127, 4.93672821100003, 4.931431377000081, 4.912802022000022, 4.902957662000048, 4.892751567000076, 4.878669739000145, 4.755188904000093, 4.741727194000134, 4.736197815000125, 4.7333297730001505, 4.727852071000072, 4.709403585000061, 4.692376200000126, 4.673281759000048, 4.6487354530000715, 4.616050110000089, 4.604345398000106, 4.563391825000082, 4.546157736000097, 4.509544983000055, 4.4842235320000725, 4.37637481700007, 4.312941997000038, 4.269818013000119, 4.244393209000108, 4.2272624720000636, 4.208581441000078, 4.191528219000048, 4.177911479000045, 4.169565735000077, 4.160522359000112, 4.152331645000089, 4.131712748000098, 4.1166490680001, 4.08207753500011, 4.066522929000087, 4.041718241000041, 4.02494923900008, 3.9942017620000314, 3.984460755000086, 3.949811707000066, 3.9407166550001023, 3.9295287070000597, 3.922526551000061, 3.876353658000113, 3.8661992390000535, 3.8576467890000288, 3.8582152300000843, 3.8464846800000885, 3.82689931200008, 3.814677837000147, 3.811008810000061, 3.805815328000051, 3.795738424000106, 3.788736267000104, 3.7580404670000718, 3.7470592250000863, 3.676107483000095, 3.6405540980000524, 3.6345337930001023, 3.636445821000038, 3.6398306270000518, 3.6414584350000894, 3.637918599000031, 3.623604228000133, 3.6109951780001097, 3.59569895500006, 3.573038839000091, 3.5310259000000883, 3.455397441000045, 3.4153740440000604, 3.3776760860001076, 3.3642143760000636, 3.346696066000092, 3.327084859000067, 3.309721578000051, 3.3093140290000918,3.3093140290000918,]

x=np.array(X)[::77];y=np.array(Y)[::77]#~10tasku
# x=np.array(X)[::22];y=np.array(Y)[::22]#~34tasku
# x=np.array(X)[::4];y=np.array(Y)[::4]#~185tasku
# x=np.array(X)[::2];y=np.array(Y)[::2]#~369tasku

nP=len(x)
t=np.linspace(0,nP,nP)
print(len(x))
plt.grid()
dx=akima(x)
dy=akima(y)
for i in range(len(x)):
    plt.scatter(x[i],y[i],c='firebrick',s=6)
    
for i in range(1,len(x)):
    tPlt=np.linspace(t[i-1],t[i],100)
    xPlt=np.zeros(100)
    yPlt=np.zeros(100)
    for j in range(2):
        U,V=Hermite(t[i-1:i+1],j,tPlt)
        yPlt=yPlt+U*y[i+j-1]+V*dy[i+j-1]
        xPlt=xPlt+U*x[i+j-1]+V*dx[i+j-1]
            
    plt.plot(xPlt,yPlt)

plt.show()