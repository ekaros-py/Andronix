#import
import os
import time
from os import *
from time import *
#color
gr, r, g, y, b, p, c, w=[
'\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m' ]
#mkdir("Andronix")
system("clear")
system("figlet Andronix")
print("____")
#kali linux
print(f"{r}[{g}KALI{r}]{g}kali linux")
#ubuntu20.04
print(f"{r}[{g}UB20{r}]{g}ubuntu20{r}.04")
#ubuntu18.04
print(f"{r}[{g}UB18{r}]{g}ubuntu18{r}.04")
#debian
print(f"{r}[{g}DEBI{r}]{g}debian")
#arch
print(f"{r}[{g}ARCH{r}]{g}arch")
#manjaro
print(f"{r}[{g}MANJ{r}]{g}manjaro")
#fedora
print(f"{r}[{g}FEDO{r}]{g}fedora")
#void
print(f"{r}[{g}VOID{r}]{g}void")
#Alpine
print(f"{r}[{g}ALPH{r}]{g}alphine")
#____
ch=input(f"{r}Choose numper {g}=>{r} ")
if ch=="kali":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash")
	system("clear")
if ch=="ub20":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh | bash")
	system("clear")
if ch=="ub18":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu/ubuntu.sh | bash")
	system("clear")
if ch=="debi":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
	system("clear")
if ch=="arch":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash")
	system("clear")
if ch=="manj":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh | bash")
	system("clear")
if ch=="fedo":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash")
	system("clear")
if ch=="void":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh | bash")
	system("clear")
if ch=="alph":
	system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
	system("clear")
