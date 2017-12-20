Images aufspielen und sichern mit dem Terminal
##############################################

:date: 2017-10-31 11:05
:modified: 2017-10-31 11:05
:tags: dd, shell, terminal
:category: shell
:slug: dd
:summary: Mac & Linux Images auf Speichermedium wie SD-Card & USB Stick aufspielen. Z.B. für Raspberry Pi.
:subtitle: DD Beispiele

Mac Geräte auflisten
^^^^^^^^^^^^^^^^^^^^

Unter mac kann mit ``diskutil list`` alle Speichergeräte aufgelistet werden ::

    diskutil list

Beispiel ausgabe ::

    /dev/disk0 (internal):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                         251.0 GB   disk0
       1:                        EFI EFI                     314.6 MB   disk0s1
       2:                 Apple_APFS Container disk1         250.7 GB   disk0s2

    /dev/disk1 (synthesized):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      APFS Container Scheme -                      +250.7 GB   disk1
                                     Physical Store disk0s2
       1:                APFS Volume Macintosh HD            225.3 GB   disk1s1
       2:                APFS Volume Preboot                 20.2 MB    disk1s2
       3:                APFS Volume Recovery                519.9 MB   disk1s3
       4:                APFS Volume VM                      3.2 GB     disk1s4

    /dev/disk2 (external, physical):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:     FDisk_partition_scheme                        *16.0 GB    disk2
       1:                      Linux                         21.0 MB    disk2s1
       2:                      Linux                         16.0 GB    disk2s2

SD-Card oder USB Stick ISO erstellen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mit ``dd`` lassen sich Datenträger als ISO abilden dabei gibt der Parameter ``if`` das Quellverzeichnis an & ``of``
das Ziel Verzeichnis. Beispiel beim Backup einer Raspbian SD-Card welches sich unter ``/dev/disk2`` befindet und auf
dem Desktop ``~/Desktop/raspberrypi.dmg`` gesichert werden soll.::

    sudo dd bs=1m if=/dev/disk2 of=~/Desktop/raspberrypi.dmg

sudo dd bs=100m if=/dev/rdisk2 of=~/Desktop/raspberrypi.dmg
Dies kann einige Minuten in anspruch nehmen, je nachdem wie groß die SD-Card ist & wie schnell die Datenübertragungsrate
zwischen der Card und dem PC ist.

ISO auf Datenträger aufspielen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wieder mit ``dd`` lassen sich Datenträger bearbeiten. Diesmal muss fast der gleiche Befehl eingegeben werden wie beim
erstellen einer ISO File nur ``if`` & ``of`` müssen ausgetauscht werden.::

    diskutil unmountDisk /dev/disk2
    sudo dd bs=1m if=~/Desktop/raspberrypi.dmg of=/dev/disk2

Mac SD-Card oder USB auswerfen im Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mittels ``diskutil list`` das Ziel Gerät auslesen, meist unter Mac ``/dev/disk2`` und dann via ``diskutil unmountDisk device``
auswerfen.::

    diskutil unmountDisk /dev/disk2
