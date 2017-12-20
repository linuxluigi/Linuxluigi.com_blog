SSH Befehle
###########

:date: 2017-10-31 11:05
:modified: 2017-10-31 11:05
:tags: ssh, keyring, shell, terminal
:category: shell
:slug: ssh
:summary: Wichtige & häufige SSH Befehle
:subtitle: SSH Befehle

Authenfizierung via Public Key
------------------------------

Public Key zum SSH Server hochladen.::

    ssh-copy-id -i ~/.ssh/id_rsa.pub user@hostname.example.com

SSH Keyring alten Fingerprint entfernen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn der SSH Server neu installiert wurde und versucht man versucht sich mit seinen alten Login Daten ein zu loggen, wird
folgender Text erscheinen.::

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
    Someone could be eavesdropping on you right now (man-in-the-middle attack)!
    It is also possible that a host key has just been changed.
    The fingerprint for the ECDSA key sent by the remote host is
    SHA256:Fd+wUMWEjj/eIcG4p8gs7uZMTjqfIpMr/46LNGW99J4.
    Please contact your system administrator.
    Add correct host key in ~/.ssh/known_hosts to get rid of this message.
    Offending ECDSA key in ~/.ssh/known_hosts:33
    ECDSA host key for 192.168.100.100 has changed and you have requested strict checking.
    Host key verification failed.

Um den alten Fingerprint nun zu entfernen, kann ``ssh-keygen`` verwendet werden mit der folgenden syntax.::

    ssh-keygen -R 192.168.100.100

Wobei darauf zu achten ist die IP ``192.168.100.100`` mit der Ziel IP / Domain aus zu tauschen. Danach kann man den
neuen Fingerprint herunterladen und verifizieren.