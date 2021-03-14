import os
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('Creating lvm'))

print("Listing all the disk with their partitions...")
print()
os.system("sleep 2")
os.system("fdisk -l")
print()
drive_name=input("Please enter the name of your physical drive which you choose for creating physical volume: ")
os.system(f"pvcreate {drive_name}")
print()
vgname=input("Please enter the name of the Volume Group: ")
os.system(f"vgcreate {vgname} {drive_name}")
print()

os.system("vgdisplay")
size=input("Enter the size of logical volume:  ")
print()
name=input("Enter the name of the logical Volume: ")
print()
os.system(f"lvcreate --size {size}  --name {name} {vgname}")

os.system(f"mkfs.ext4 /dev/{vgname}/{name}")

mount_folder=input("Enter the directory location where you want to mount the storage: ")
os.system(f"mkdir -p {mount_folder}")
os.system(f"mount /dev/{vgname}/{name} {mount_folder}")
print("LVM Succefully Created")
os.system("df -h")
