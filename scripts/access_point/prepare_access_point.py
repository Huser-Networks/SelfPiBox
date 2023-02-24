###
# The purpose of this python script is to be runned by administrator to allow the SelfPiBox to create its own access point.
###

# imports
import os

# file path
parent_dir = "/etc/"
directory = "accesspoint"
path = os.path.join(parent_dir, directory)

# permission
permission = 0o755
user_id = 1000
group_id = 1000

# create directory
try:
    os.mkdir(path, permission)
    print("folder " + path + " created with permissions " + str(permission))

except OSError as error:
    print(error)

# set owner
try:
    os.chown(path, user_id, group_id)
    print("folder " + path + " now belongs to " + str(user_id) + " of group " + str(group_id))

except OSError as error:
    print(error)
