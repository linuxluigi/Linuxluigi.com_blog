Banana Pi Resilio Sync File Server
##################################

:date: 2017-10-31 11:05
:modified: 2017-10-31 11:05
:tags: banana pi, raspberry pi, Resilio Sync, Bittorent Sync, home Server, file server
:category: tutorial
:slug: Resilio-Sync-Banana-Pi-Tutorial
:summary: Resilio Sync Banana Pi Tutorial. Sichere dezentrale home cloud.
:subtitle: Resilio Sync Banana Pi Tutorial

Voraussetzung
-------------

Ziel
^^^^

Dieses Tutorial wird ein `Banana Pi M1`_ mit einer USB Festplatte zu einen `Resilio Sync`_ dezentralen File Server.

.. _Banana Pi M1: http://www.banana-pi.org/m1.html
.. _Resilio Sync: https://www.resilio.com/

Benötigte Hardware
^^^^^^^^^^^^^^^^^^

Die Folgende Hardware Liste ist nur ein Beispiel, es muss nicht genau diese kombination gewählt werden, es ist auch
möglich andere Komponenten zu wählen. Diese hier aufgezählten Produkte haben sich bei mit in der Praxis bewährt und kann
sie damit auch gut weiter empfelen.

+------------------+---------------------------------------------------------------------------------------------------+
| **Hardware Typ** | **Amazon Affiliate Links**                                                                        |
+==================+===================================================================================================+
| Micro Server     | `Banana Pi Mark 1`_                                                                               |
+------------------+---------------------------------------------------------------------------------------------------+
| SD-Card          | `Samsung EVO Plus Micro SDXC 64GB`_                                                               |
+------------------+---------------------------------------------------------------------------------------------------+
| Power Supply     | `Rydges EU 5V 3A Micro USB Stecker Netzteil`_                                                     |
+------------------+---------------------------------------------------------------------------------------------------+
| USB-Festplatte   | `Western Digital Elements Desktop`_                                                               |
+------------------+---------------------------------------------------------------------------------------------------+

.. _Banana Pi Mark 1: http://amzn.to/2zkxsvj
.. _Samsung EVO Plus Micro SDXC 64GB: http://amzn.to/2A2xwgg
.. _Rydges EU 5V 3A Micro USB Stecker Netzteil: http://amzn.to/2z5Ty3L
.. _Western Digital Elements Desktop: http://amzn.to/2iNMyCA

.. figure:: /images/devices/banana-pi-file-server.jpg
    :alt: Banana Pi File Server
    :scale: 60%
    :align: center

    Banana Pi File Server

Software
^^^^^^^^

Als Betriebsystem kommt ein Raspbian zum einsatz, welches direkt für den Banana Pi optimiert wurde.

http://www.banana-pi.org/m1-download.html

Und als File Server Software wird `Resilio Sync`_ verwendet, da es sehr schnell Daten von einem zum anderen Gerät
transportiert, gratis in der einsteiger Version und 128 Bit AES end-zu-end verschlüsselt und dezentral (keine Router
konfiguration nötig).

Zur installation werden Teile von https://github.com/linuxluigi/bananapi_resilio_sync verwendet.

Installation
------------

Betriebsystem downloaden
^^^^^^^^^^^^^^^^^^^^^^^^

Auf http://www.banana-pi.org/m1-download.html gehen und Raspbian downloaden & entpacken.

SD-Karte vorbereiten
^^^^^^^^^^^^^^^^^^^^

Dieser Part ist für Mac geschrieben aber die Befehle unter Linux sind sehr ähnlich. Windows User sollten auf der
Offiziellen Raspberry Pi Seite gehen und dort die Anleitung folgen.
https://www.raspberrypi.org/documentation/installation/installing-images/

Nachdem die Zip file entpackt wurde im Terminal ``diskutil list`` eingeben um alle Datenträger an zu zeigen.::

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

Wenn die SD-Karte richtig initialisiert wurde sollte warscheinlich der letzte eintrag die SD-Karte sein ``/dev/disk2``.

Um das Image auf der SC-Karte zu übertragen wird ``dd`` verwendet.::

    diskutil unmountDisk /dev/disk2
    sudo dd bs=1m if=/path/to/2016-07-12-raspbian-lite-bpi-m1-m1p-r1.img of=/dev/disk2

Jetzt noch SSH aktivieren indem auf der SD-Karte eine Datei namens ``ssh.txt`` ohne Inhalt erstellt wird.::

    sudo touch /Volumes/BPI-BOOT/ssh.txt

Die SD-Karte sollte nun fertig sein und bereit für den Banana Pi. Es kann ab hier auch schon alles an den Pi
angeschlossen und mit strom versorgt werden.

Um die SD-Karte aus zu werfen.::

    diskutil unmountDisk /dev/disk2

Raspbian einrichten
^^^^^^^^^^^^^^^^^^^

Mittels ``ssh`` auf dem Pi einloggen. Die standart login daten sind: ``pi/bananapi`` & ``root/bananapi``::

    ssh pi@raspberrypi

Nach dem einloggen am besten gleich das File System erweitern (Expand Filesystem). Dafür die ``raspi-config`` verwenden,
in der Offiziellen Dokumentation sind die einzelnen Steps sehr ausführlich beschrieben & was noch alles mit ``raspi-config``
gemacht werden kann: https://www.raspberrypi.org/documentation/configuration/raspi-config.md ::

    sudo raspi-config
    sudo reboot

Mittels ``raspi-config`` oder ``passwd`` das root & user passwort ändern.::

    sudo raspi-config
    passwd
    sudo passwd

Als nächstes das System updaten.::

    sudo apt-get update
    sudo apt-get dist-upgrade

USB-Festplatte mounten
^^^^^^^^^^^^^^^^^^^^^^

Um zu sehen ob die USB Festplatte richtig angeschlossen ist ``sudo blkid -s UUID`` ausführen und es
sollte so ähnlich aussehen.::

    /dev/mmcblk0p1: UUID="35CB-ED62"
    /dev/mmcblk0p2: UUID="2cfc428f-9afc-4036-8533-bb437fd1bc36"
    /dev/sda1: UUID="a6c240d4-0f07-46b4-adcd-b9e32117a74b"

Wenn unter ``dev/sda1`` auch ein Datenträger angezeigt wird, kann die Festplatte nun formatiert werden.::

    sudo mkfs.ext4 -t /dev/sda1

Damit die nun frisch formatierte festplatte gemountet werden kann, muss noch ein Ordner erstellt werden, wo die Festplatte
später auf zu finden sein wird. In diesen Beispiel wird der Ordner unter ``/srv/resilio-sync/`` sein.::

    sudo mkdir /srv/resilio-sync/

Und mit dem folgenden Befehl wird die Festplatte mit jeden start automatisch unter ``/srv/resilio-sync/`` gemountet.::

    sudo sh -c "echo '/dev/sda1 /srv/resilio-sync ext4 defaults,noatime,nodiratime,commit=600,errors=remount-ro 0 1' >> /etc/fstab"

Mit ``sudo mount -a`` kann die Festplatte auch sofort gemountet werden.

Resilio-Sync installieren
^^^^^^^^^^^^^^^^^^^^^^^^^

Resilio Sync lässt sich einfach aus der Repo heraus installieren::

    echo 'deb http://linux-packages.resilio.com/resilio-sync/deb resilio-sync non-free' | sudo tee --append /etc/apt/sources.list.d/resilio-sync.list > /dev/null
    wget -qO - https://linux-packages.resilio.com/resilio-sync/key.asc | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install -y resilio-sync
    # user rslsync
    sudo systemctl enable resilio-sync

Noch die Daten & Backup Ordner erstellen und ``resilio-sync`` User schreibrechte erteilen.::


    sudo mkdir /srv/resilio-sync/server
    sudo mkdir /srv/resilio-sync/backup
    sudo chown -R rslsync:rslsync /srv/resilio-sync

Backup
^^^^^^

In diesen Tutorial wird ``rsnapshot`` verwendet, es erstellt im Stundentakt Hardlinks von allen Datein und kann mit
dieser Technik Stündlich Backups über einer Woche erstellt werden und benötigt in einigen fällen 10% und weniger Speicher
als die Eigentlichen Daten. Jedes Backup wird innerhalb weniger Sekunden erstellt bis auf das erste. Diese Backup
Version sollte nur verwendet werden wenn mehr als ein Resilio File Server zum einsatz kommt, das wichtige Daten mehrfach
physisch existieren!

``rsnapshot`` installieren::

    sudo apt-get install -y rsnapshot

Das folgende Script ist sorgt dafür das der Ordner ``/srv/resilio-sync/server`` im Verzeichnis ``/srv/resilio-sync/backup``
gesichert wird.::

    sudo sh -c "echo 'backup\t/srv/resilio-sync/server/\tlocalhost' >> /etc/rsnapshot.conf"
    sudo sed -i 's!snapshot_root\t/var/cache/rsnapshot/!snapshot_root\t/srv/resilio-sync/backup!g' /etc/rsnapshot.conf

Die Backup intervalle sind in der Datei ``/etc/rsnapshot.conf` unter der Sektion `BACKUP INTERVALS`` zu bearbeiten.

Security
^^^^^^^^

Als wichtigtest ist es die Passwörter von pi & root zu ändern, wie schon bei der Installation beschrieben. Das geht mit.::

    # for pi user
    passwd
    # for root user
    sudo passwd

Der nächste Step ist zum login nur noch SSH Public Keys zu verwenden. Dazu am besten
im Ubuntu wiki nachlesen wie es zu machen ist https://wiki.ubuntuusers.de/SSH/#PubKeys

Wenn die Authenfizierung mit Public-Key funktioniert und auch nur wenn! Dann den Root user via SSH aussperren & der
Passwort login deaktivieren.::

    # secure ssh
    sudo sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin no/g' /etc/ssh/sshd_config
    sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
    # reload ssh server
    sudo /etc/init.d/ssh reload

Zum Schluss noch automatisch Sicherheits-Updates installieren lassen.::

    # activate auto install security updates
    sudo apt-get -y install unattended-upgrades
    sudo sh -c "echo 'APT::Periodic::Update-Package-Lists "1";' > /etc/apt/apt.conf.d/10periodic"
    sudo sh -c "echo 'APT::Periodic::Update-Package-Lists "1";' >> /etc/apt/apt.conf.d/10periodic"
    sudo sh -c "echo 'APT::Periodic::Download-Upgradeable-Packages "1";' >> /etc/apt/apt.conf.d/10periodic"
    sudo sh -c "echo 'APT::Periodic::AutocleanInterval "7";' >> /etc/apt/apt.conf.d/10periodic"
    sudo sh -c "echo 'APT::Periodic::Unattended-Upgrade "1";' >> /etc/apt/apt.conf.d/10periodic"

Cronjobs
^^^^^^^^

Cronjobs lassen sich leicht via ``anacron`` verwalten.::

    sudo apt-get -y install anacron

Backup
""""""

Folgendes Script sorgt dafür, dass rsnapshot Stündlich, Täglich & Wöchentlich ausgeführt wird.::

    # hourly
    sudo wget https://raw.githubusercontent.com/linuxluigi/bananapi_resilio_sync/master/cron/hourly/rsnapshot.sh -O /etc/cron.hourly/rsnapshot
    sudo sed -i 's/alpha/hourly/g' /etc/cron.hourly/rsnapshot
    sudo chmod +x /etc/cron.hourly/rsnapshot
    # daily
    sudo wget https://raw.githubusercontent.com/linuxluigi/bananapi_resilio_sync/master/cron/daily/rsnapshot.sh -O /etc/cron.daily/rsnapshot
    sudo chmod +x /etc/cron.daily/rsnapshot
    sudo sed -i 's/beta/daily/g' /etc/cron.daily/rsnapshot
    # weekly
    sudo wget https://raw.githubusercontent.com/linuxluigi/bananapi_resilio_sync/master/cron/weekly/rsnapshot.sh -O /etc/cron.weekly/rsnapshot
    sudo chmod +x /etc/cron.weekly/rsnapshot
    sudo sed -i 's/gamma/weekly/g' /etc/cron.weekly/rsnapshot

Stability
"""""""""

Nach meinen langzeit Erfahrung empfielt es sich bei Resilio Sync auf ein ARM Board es lieber am Tag ein mal neu zu starten
falls ein Prozess sich abwürgt. Dies passiert sehr selten aber durch tägliches neustarten funktioniert das System 24/7
ohne weitere Wartung auch bei großen Datenmengen. :)

Außerdem ist sollte der Zeitserver stündlich geupdatet werden, da Resilio Sync Daten nur Daten transferiert wenn alle
Geräte die gleiche Intere Zeit besitzten und wenn ein Pi aus dem Strom genommen wird, ist dieser nicht mehr Syncron.
Anders bei Desktop, Laptop oder größeren Servern wo eine interne Batterie die Zeit sichert.::

    # daily reboot the pi
    sudo wget https://raw.githubusercontent.com/linuxluigi/bananapi_resilio_sync/master/cron/daily/resilio-restart.sh -O /etc/cron.daily/resilio-restart
    sudo chmod +x /etc/cron.daily/resilio-restart

    # cron ntp time hourly
    sudo apt-get -y install ntp ntpdate
    ntpdate -s 0.de.pool.ntp.org
    sudo wget https://raw.githubusercontent.com/linuxluigi/bananapi_resilio_sync/master/cron/hourly/ntpdate.sh -O /etc/cron.hourly/ntpdate
    sudo chmod +x /etc/cron.hourly/ntpdate

Resilio Sync einrichten
^^^^^^^^^^^^^^^^^^^^^^^

Wenn alles geklappt habt könnt ihr euch auf eurern Pi mit dem Port ``8888`` in der Web GUI von Resilio Sync einloggen.

In den Einstellungen muss noch der Standart Ordner eingestellt werden ``/srv/resilio-sync/server``