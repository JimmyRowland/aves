from django.shortcuts import render
import random

def index(request):
    return render(request, 'home/home.html')
def contact(request):
    x = random.randrange(3)
    if x == 0:
        return render(request, 'home/contact.html')
    elif x == 1:
        return render(request, 'home/home.html')
    else:
        return render(request, 'home/about.html')


def about(request):
    return render(request, 'home/about.html')
def faq(request):
    return render(request, 'home/faq.html')
def audio(request):
    return render(request, 'home/audio.html')
def schedules(request):
    return render(request, 'home/schedules.html')
def geturl(request):
    img_url = ["https://collegexam.files.wordpress.com/2016/07/ladybowerreservoir_row12027188255_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/alaskapeninsula_row13823887282_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/hanoivietnam_row14516665864_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/maltacoast_zh-cn6974260336_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/notredamepuddle_row10243386109_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/mardigrasbeads_row12782899494_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/arcticice_row13730870383_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/mecoast_row11999975647_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/orphanbabies_zh-cn11125858807_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/mayottegecko_row8640385264_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/hohenzollerncastle_row11302025187_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/moerakibouldersnz_row10948737290_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/armydump_row11323503992_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/montedarochadam_row10497820606_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/ovisdalli_row12191483038_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/munnarindia_row7199944310_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/icebergsky_zh-cn9023749021_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/hoodedmerganser_row13096230592_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/lakebuttermere_row10783939870_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/autumntrees_zh-cn10373611719_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/piday_row11974953961_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/landscapeliriver_zh-cn12335671856_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/bananaslug_row14375923911_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/rickshawstajmahal_row9921748098_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/lanternfestival_zh-cn11167953822_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/rimedlarchforest_row10774697247_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/blacknosesheep_row14183147524_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/leopardmoremireserve_row10874261043_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/ruapehucraterlake_row12151259283_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/camareslandscape_row13330593851_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/mammothhs_row11507605833_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/secretarybird_row10401694467_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/millauviaduct_row8878996474_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/canoebanff_row12869587994_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/sheepkingpenguin_row13000015193_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/canolafield_row13669976851_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/mooncaketea_zh-cn12499152035_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/shortearedowl_zh-cn10401030673_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/canyonlands50_row12893258713_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/okavangodelta_row10902367114_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/springflowers_zh-cn12146467355_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/changanavenue_zh-cn10454331015_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/stlawrenceharpseal_zh-cn7809993664_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/oktoberfestferriswheel_zh-cn8389630141_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/chipmunkeating_row9362382344_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/orcaskenaifjords_row13060147576_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/torontocityhall_row13168683251_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/colorfulmacaws_row13327356049_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/palaisroyal_zh-cn12268827053_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/wildboars_row11399549736_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/fanjingshan_zh-cn11691452911_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/panacheboathouses_row12671553819_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/windmap_row9107932802_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/fishingxiaodongriver_zh-cn10867917762_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/pandaclimbingtree_row11074504569_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/yenbai_row11927875553_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/floriadecanberra_zh-cn11240866211_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/peacecamp_row11441035277_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/fortmchenry_row12090648921_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/amauferns_row13300950534_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/riotinto_row13864226561_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/glenanislands_row11618507821_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/rockymountainnp_row9933513452_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/antarcticsound_row14082948249_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/sheepflock_row6816979611_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/badalinggreatwall_zh-cn8953349136_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/shenzhenguangdong_zh-cn12256609322_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/banonprovence_row13577162668_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/sutjezkanp_zh-cn10008358917_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/belgiumbluebells_row11505375582_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/treefrogs_zh-cn13276767636_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/cancunpano_zh-cn5697138969_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/bonsairock_row10228778317_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/tikalguatemala_zh-cn11146845949_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/tsinghuaarche_zh-cn7826742772_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/causewaycoast_row11419261251_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/weizbergkirche_row11910689083_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/caveofthelakes_row10761216506_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/wildernessact50_row10309525566_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/dettifoss_row8878930310_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/youngguanaco_row14221452700_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/earthstrongholds_zh-cn10396925597_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/easternbluebirds_zh-cn12146223169_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/emergencyswap_zh-cn7058789247_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/flashmob_zh-cn10098310189_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/foggypicchu_row10705432857_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/frenchsunset_row12311384056_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/galapagossealion_row12227785290_1920x1080.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/q.jpg",
                   "https://collegexam.files.wordpress.com/2016/07/r.jpg"
                   ]


    return render_to_response('home/contact.html', {'img_url': img_url})
def hour(request):
    now = datetime.now()
    list = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    return render_to_response('home/contact.html', {"list": list})