#Este programa recebe hora, minuto e segundos e cria um cronometro que percorre a contagem até estes números serem atingidos. Caso digite errado, a aplicação é interrompida.
# Criado por Rodrigo em 17-04

# EX1 Validar as entradas do usuário (hora, minuto segundo)
# EX2 Adicioanr o dia da semana (usuário digita o dia da semana)

hora = int(input('hora: '))
minuto = int(input('minuto: '))
segundo = int(input('segundo: '))

if hora < 24 and minuto < 60 and segundo < 60:    
    h = 0
    while h < 24:
        m = 0
        while m < 60:
            s = 0
            while s < 60:
                print(f'{h:02}:{m:02}:{s:02}')
                if h == hora and m == minuto and s == segundo:
                    print('ALARME!!!')
                    break
                s += 1
            if h == hora and m == minuto and s == segundo:
                break
            m += 1
        if h == hora:
            break
        h += 1
else:
    print('\n\n--Atenção!! Você digitou números fora do padrão permitido--\n')
