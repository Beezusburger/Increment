import os
import math
import sys

def main():
    """Interogate user for fixed values of the data"""
    id = input('Entri id di pubblicazione della misura: ')
    print('{"id":'+ id)
    period= input('Entri il period: ')
    os.system('cls')
    print('{"id":'+id+', "period":'+period)
    
    adressDiMisura = input('Entri address della misura: ')
    os.system('cls')
    print('{"id":'+id+', "period":'+period+ ', "tag":'+adressDiMisura)
    
    numeroDiRegistri = input('Entri numero di registri: ')
    os.system('cls')
    print('{"id":'+id+', "period":'+period+ ', "tag":'+adressDiMisura+','+numeroDiRegistri)
   
    tipoDiDato = input('Entri tipo di dato: ')
    os.system('cls')
    print('{"id":'+id+', "period":'+period+', "tag":'+adressDiMisura+','+numeroDiRegistri+','+tipoDiDato)
    
    moltiplicatore = input('Entri il modificatore: ')
    os.system('cls')
    print('{"id":'+id+', "period":'+period+ ', "tag":'+adressDiMisura+','+numeroDiRegistri+','+tipoDiDato+','+moltiplicatore+', 0, 3, X, X, X}')
    answer= input('Stringa e pronta per salvataggio e incremento di ultime 3 parametri. Procedere?')
    
    if (answer.lowercase()=='y'):
        writeFile()
    else:
        print('start again?')

def writeFile():
      
      with open('D:\Development\Playground\IncrementationTest.txt','w') as file:
             for i in range(1, 200):
                   file.write('{"id":'+id+', "period":'+period+ ', "tag":'+adressDiMisura+','+numeroDiRegistri+','+tipoDiDato+','+moltiplicatore+', 0, 3,'+i+','+i+',' +i+'}\n' )
      file.close()

if __name__ == '__main__':
    main()
