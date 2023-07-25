import lief
import sys

import pwn
if (len(sys.argv) < 2):
    print("Syntax: python3 patch_executable.py <path-to-executable>")
    exit(1)

print("Parsing executable")
binary = lief.PE.parse(sys.argv[1])

def patch_start_with_giga_mode(binary):
    modes = {0:"NETHER",1:"HYPER",2:"MEGA",3:"SUPER",4: "ULTRA",5: "EXTRA",6:"GIGA"}
    current_mode_address = 0x47D6EF+1
    current_mode = pwn.u32(bytes(binary.get_content_from_virtual_address(current_mode_address,4,lief.Binary.VA_TYPES.VA)))

    binary.patch_address(current_mode_address,6,4,lief.Binary.VA_TYPES.VA)


    current_mode = pwn.u32(bytes(binary.get_content_from_virtual_address(current_mode_address,4,lief.Binary.VA_TYPES.VA)))
    print("-- New value of initial mode:",modes[current_mode])



def patch_giga_control(binary):
    current_mode_address = 0x0491979

    asm = b'\x83\xa0\xd0\x00\x00\x00\xfe' # and DWORD PTR [eax+0xd0], ~1
    binary.patch_address(current_mode_address,list(asm),lief.Binary.VA_TYPES.VA)

    print("-- Giga Mode Control patched")

def patch_disable_mode_down(binary):
    current_mode_address = 0x47db40

    asm = b'\xb8\x06\x00\x00\x00\xc3' # mov eax, 6; ret
    binary.patch_address(current_mode_address,list(asm),lief.Binary.VA_TYPES.VA)

    print("-- Mode Down patched out!")

def patch_boot_original_aksys_logo(binary):
    commonbootfile_address = 0x04FD0BC

    filename = b"Common/Boot/BootUS.aemenu\x00"
    binary.patch_address(commonbootfile_address,list(filename),lief.Binary.VA_TYPES.VA)
    print("-- Use original Wii aemenu")

patch_start_with_giga_mode(binary)
patch_disable_mode_down(binary)
patch_giga_control(binary)
patch_boot_original_aksys_logo(binary)
print("Writing patched exe")
binary.write("BIT.TRIP FATE.patched.exe")



