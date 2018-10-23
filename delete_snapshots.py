# this is a script for deleting snapper snapshots that are deemed "Illegal" when using snapper delete 
import os
snapshot_locations = '/home/.snapshots/'
dirnames = os.listdir(snapshot_locations)
for d in dirnames:
	print('try remove snapshot subdir')
	os.system('sudo btrfs subvolume delete ' + snapshot_locations + d + '/' + 'snapshot')
	os.system('sudo rm -rf ' + d)
