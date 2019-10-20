#!/usr/bin/python
from pwn import *
from capstone import *
context.arch = 'amd64'

md = Cs(CS_ARCH_X86, CS_MODE_64)

r = open(sys.argv[1]).read()[:]

new_r2 = ''
new_r1 = ''
super_r = ''


for i in md.disasm(r, 0):
    if i.mnemonic.startswith('nop'):
        continue
    new_r1 += str(i.bytes)

count = 0
for i in md.disasm(new_r1, 0):
    if i.mnemonic.startswith('mov') and i.op_str.split(',')[0] == "rcx":
        count = 0
        continue

    if count == 1 and i.mnemonic.startswith('mov') and i.op_str.split(',')[0] == "rax":
        new_r2 = new_r2[:-10]
    else:
        count = 0

    if i.mnemonic.startswith('mov') and i.op_str.split(',')[0] == "rax":
        count = 1

    if i.mnemonic.startswith('ro') and i.op_str.split(',')[1] == ' 0':
        continue
    new_r2 += str(i.bytes)

x = make_elf(new_r2)
open(sys.argv[1] + '_optimized', 'w').write(x)
