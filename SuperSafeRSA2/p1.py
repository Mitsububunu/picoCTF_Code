from pwn import *

c = 2406630770774067002969488973721471931018204466252985338778157023054313700122577969674801095968914138115159683835249515291036273321027004343571790131936084125655906043408782674885449464579968641081302429157166130115565352598598821570066283635305122709922390037730372591602868730589481713392049764648061801524
n = 147273688793934261024181248195230675783546488649508215206712909610823309020315167219784009002992362309068755668749150030649630484626726808282970862335298874686962338279846001531881628828732296269712243526593454314785171173549519521483321293695860652122785966138520696376542198407518431742168507833956480984961
e = 63898673129003779730878645535062396293775186608309292451636199166635042678069819794841971649603854650935655697405772023765540730127423849024616269748450841660052311890954340601218380974301418080097016300493123077080154006552987883044292330365369861886535969787230416626276257087720735443256331831473849394433

m = pow(c, 65537, n)
print hex(m)
print unhex(hex(m)[2:])