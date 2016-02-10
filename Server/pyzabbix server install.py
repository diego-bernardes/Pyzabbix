#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#Testado usando python 3 rodando sobre Debian 8.2

import subprocess, os
print('''
Antes de prosseguir, configure um IP fixo para o servidor
# vi /etc/networ/interfaces
auto <interface>
    iface <interface> inet static
    address <ip>
    netmask <mascara>
    gateway <gateway>
:wq''')

os.system('apt-get update')


print('Realizando a instalação do MySQL, informe uma senha de root para o mysql quando for solicitado')
os.system('apt-get install mysql-server')


print('Baixando e instalando o zabbix 2.4')
os.system('wget -c http://repo.zabbix.com/zabbix/2.4/debian/pool/main/z/zabbix-release/zabbix-release_2.4-1+jessie_all.deb')
os.system('dpkg -i zabbix-release_2.4-1+jessie_all.deb')
os.system('apt-get update')
os.system('apt-get install zabbix-server-mysql zabbix-frontend-php zabbix-agent zabbix-get zabbix-sender')
print('Alterando o arquivo apache.conf em /etc/zabbix/')
os.system('cp -f config/apache.conf /etc/zabbix/')
print('Alterando o arquivo php.ini em /etc/php5/apache2/')
os.system('cp -f config/php.ini /etc/php5/apache2/')
os.system('service apache2 restart')
