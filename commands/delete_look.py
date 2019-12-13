import sys
import os
import yaml ### install the pyyaml package
from modules.lookerapi import LookerApi
from datetime import datetime
from pprint import pprint
import pdb


### ------- HERE ARE PARAMETERS TO CONFIGURE -------

#pdb.set_trace()
looks_to_delete = sys.argv[1]
host = 'looker'

### ------- OPEN THE CONFIG FILE and INSTANTIATE API -------

f = open('config.yml')
params = yaml.load(f, Loader=yaml.FullLoader)
f.close()

my_host = params['hosts'][host]['host']
my_secret = params['hosts'][host]['secret']
my_token = params['hosts'][host]['token']


looker = LookerApi(token=my_token,
                   secret=my_secret,
                   host=my_host)


### ------- HANDLE ARGUMENT FILELIST OR SINGLE LOOK -------

if os.path.isfile(looks_to_delete):
	filelist = open(looks_to_delete)
	for i in filelist:
		print ("deleting lookid: " + i)
		data = looker.delete_look(i)
		pprint(data)
else:
	data = looker.delete_look(looks_to_delete)
	pprint(data)

### ------- Done -------

print ("Done")
