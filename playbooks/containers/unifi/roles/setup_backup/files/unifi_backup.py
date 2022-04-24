#!/usr/bin/env python3

import os

os.system('podman pod stop unifi')
os.system('podman run --volumes-from unifi-controller --privileged --rm -v $(pwd):/backup busybox tar cvf /backup/unifi_backup.tar /config')
os.system('podman pod start unifi')
os.system('mv /home/eingram/unifi_backup.tar /mnt/Shared/Backup/Containers/unifi-controller/unifi_backup_$(date +%m-%d).tar')