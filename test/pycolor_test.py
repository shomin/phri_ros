#!/usr/bin/env python

def cprint(s, fg='white', bg='black',mod='none'):
    bgc = {'red':41,'green':42,'yellow':43,'blue':44,'magenta':45,'cyan':46,'grey':47,'black':40}
    fgc = {'red':91,'green':92,'yellow':93,'blue':94,'magenta':95,'cyan':96,'grey':90,'black':30,'white':97}
    modc = {'bold':1,'grey':2,'und':4,'flip':7,'strike':9,'none':3}
    print '\033['+str(fgc[fg])+'m'+'\033['+str(bgc[bg])+'m'+'\033['+str(modc[mod])+'m'+s+'\033[0m'

cprint('Regular')
cprint('Blue Foreground', fg='blue')
cprint('Red FG, Blue BG', fg='red', bg='blue')
cprint('Red FG, Blue BG, Strikthrough',fg='red',bg='blue',mod='strike')
