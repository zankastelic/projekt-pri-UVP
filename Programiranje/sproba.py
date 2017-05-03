def razdeli(besedilo):
    if besedilo == '':
        return ('','')
    prvi = besedilo.split()[0]
    drugi = besedilo.split()[1:]
    return prvi, ' '.join(drugi)
