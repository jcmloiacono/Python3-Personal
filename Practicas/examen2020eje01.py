
kin = 1
uinal =  kin * 20
tun = uinal * 18
katun = tun * 20
baktun = katun * 20

cuenta_larga =  (int(input("Introduce una la cantidad de dias: \n >")))

if cuenta_larga < 0:
    print ("Por favor, no escriba números negativos.")

baktun = cuenta_larga

print ('{} dias son {} baktún, {} Katun, {} Tun, {} uinal, {} kin'.format(cuenta_larga, baktun, katun, tun, uinal, kin ))


