#Data in bytes
import shutil
disk_usage=shutil.disk_usage("/")
print(disk_usage)
print("Free Space In Bytes: {}".format(((disk_usage.used/disk_usage.total)*(100))))
