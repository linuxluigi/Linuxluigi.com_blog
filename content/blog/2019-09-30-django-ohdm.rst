Eigener OpenStreetMap Tile-Server mit Zeitsensitivität
######################################################

:date: 2019-09-30 18:00
:modified: 2019-10-07 18:12
:tags: Docker, Erfahrung, OHDM, OSM, Django, Flask
:category: blog
:slug: osm-zeit-sensitiv
:summary: 5 Monate Arbeit an ein eigenen OpenStreetMap Tile Server der Zeitangaben akzeptiert
:subtitle: OHDM -> OpenStreetMap mit Zeitangabe

Einleitung
----------

Es fing damit an, dass ich ein Projekt in den Fach Ortsbasierten Informationssysteme ausarbeiten sollte. Das Projekt sollte zu
80% in meiner Note einfließen. Ursprünglich wollte ich nur die vorhandenen Systeme Dokumentieren und Grafisch aufbereiten.
Doch schon bei der Dokumentation des erstens Projekt, mit Hilfe von Mapnik ein eigenen OpenStreetMap Tile Server zu
erstellen welcher Zeitangaben akzeptiert, hatte ich aufgehört zu Dokumentieren und fing an dem Team zu helfen, welches das System
zum laufen zu bringen soll. Immer mehr habe ich mich in dem Team eingearbeitet und fing an umfangreich Code beizusteuern.
So habe ich erst ein Docker System aufgebaut wo einen normalen Mapnik Tile-Server drauf lief und lernte erst einmal die
einzelnen Komponenten kennen. Am Anfang dachte ich erst man müsste den OpenStreetMap Tile Server aufbohren und ihn
beibringen Zeitangaben zu akzeptieren. Doch mein Prof hat mir schnell erklärt das er vom forken nicht viel hält, da es
schwer zu warten ist und so ein Uniprojekt müsse einfach bleiben.

Na gut dann halt etwas anderes. Der nächste Ansatz war für mich mit Flask & Python ein eigenen Tile Server zu schreiben.
Das ging ziemlich flott, nachdem ich herausbekommen habe welche Abhängigkeiten alles benötigt werden.
Der nächste Schritt war anschließend die Abhängigkeit https://github.com/gravitystorm/openstreetmap-carto die Zeitangaben
bei zu bringen. Auch hier versuchte ich mein Glück und fragte den Prof ob wir nicht wenigstens dieses Projekt forken
können, es muss hier auch nur eine Datei gewartet werden. Die Datei welche die SQL beinhaltet. Das sollte nicht so schwer
zu warten sein, meinte ich. Aber auch hier war seine Antwort, dass er sicher lieber ein Tool wünscht welches die `project.mml` Zeit
sensitiv macht. Nun gut, mein Team braucht ja auch Aufgaben und wollten sich diesen Punkt widmen. Mir war es recht, denn so
konnte ich mich ungestört der Webentwicklung konzentrieren. Yeah 😎

Der Simple Tile-Server
----------------------

Da mein Prof es möglich simple haben wollte, habe ich den Webserver zuerst als eine Flask App geschrieben. Innerhalb von
100 Zeilen Code & Kommentaren war der Tile Server mit ein einfachen Caching geschrieben. Etwas zäh und in meinen Augen
nicht Produktionsreif aber der Proof-of-Concept war damit geschaffen. Als nächstes wollte ich noch eine Tile-Producer-Queue
hinzufügen. So das eine Tile URL nur ein Tile vom System erstellt wird und nicht wenn mehrere User die URL
gleichzeitig aufrufen, dass das Tile mehrfach parallel erstellt wird. Aber mein Prof rudert mich auch hier wieder zurück
:'( ich sollte doch lieber die Dokumentation schreiben und es wartungsfreundlich zu machen.
Nun gut, den Punkt verstehe ja. Also Dokumentation schreiben und gut ist.

Der Komplexe Tile-Server
------------------------

Der simple Server war ja fertig und mein Team war mit den SQL Part beschäftigt. Ich hatte keine Vorlesungen und Zeit. So konnte
mich meinen Entwickler Herz frei hingeben, etwas nebenbei Arbeiten und mich weiter in der Materie einlesen.
Ich arbeite liebend gerne mit dem Web-Framework Django. Das ist das große Python Web Framework, wie geschaffen für eine
solch komplexe Aufgabe dachte ich mir. Die erste Frage die ich mir stellte, kann Django die OpenStreetMap Datenbank mappen?
In diversen Foren & Stackoverflow gab es diesbezüglich viele Anfragen aber keine direkte Lösung. Also recherchierte ich
weiter ob Django ORM Tool es zulässt eine bestehende Datenbank als ein Django Model zu konvertieren und siehe da, Django
kann es Wuhuu 😁
Das ich jetzt mehrere Tage brauchte um ein Docker Container zu erstellen wo Django mit PostGis Unterstützung läuft, sei
jetzt mal dahin gestellt. Für mich fühlte es sich nur wie wenige Stunden an 😝
Jetzt nur noch kurz probieren ob ich ein Tile auf die Datenbank projektieren kann ... ... Ja es geht und die Abfrage
von wann bis wann die das Tile valide ist, work like a Charme.
Ich fühlte mich zwar etwas schlecht dabei, das ich schon so viel probierte. Da ich mein Prof mir anbot meine
Bachelorarbeit in dem Thema zu schreiben (Tile Caching mit Zeitraum Angabe) aber es fühlte sich zu simple an.
Ich wollte mehr und steigerte mich weiter rein.

Nun gut das Tile Caching war innerhalb eines Vormittags so weit angepasst, das der Server nun ein Zeitraum festlegen
konnte von wann bis wann das Tile valide ist.

Der nächste Schritt, die Tile Producer Queue. Die war schon etwas kniffliger. Hierzu nutze ich Celery, ein Tool
um Aufgaben in extra Container und einer Producer Queue zu lösen. Da ich noch nie Celery bevor nutze musste ich mich
erst einmal einige Stunden einlesen was das überhaupt ist und zu was man es verwenden kann. Um so mehr ich mich einlas
um so mehr war ich der Meinung das es das Tool ist was ich brauche. Also Ärmel hochgekrempelt, Dinkelkaffe geschnappt
und ran ans Werk.
Damit gleich das Caching richtig integriert ist, habe ich erst einmal ein Django Model erstellt, welches Informationen
über bereits erstellte Tiles & Tiles die gerade bearbeitet werden erstellt. So konnte ich schon einmal sicherstellen
das ein Tile nur einmal bearbeitet wird und ein zweiter User das Tile von den Request zuvor erhält. Die Ausgabe der Tiles
erfolgt bei beiden Usern gleichzeitig, sobald es halt fertig ist :) Um die Performance hoch zu halten werden die fertigen
Tiles nicht in der Datenbank gesichert sondern in einem Redis Cache hochgeladen, welcher mir auch die Aufgabe abnimmt, alte
und nicht mehr benötigte Tiles automatisch aus dem System zu löschen.

Aber auch hier war die Arbeit in ein bis zwei Tagen gut erledigt und ich war zufrieden und konnte etwas durchatmen und
von Projekt in ruhe Abstand nehmen.

Der SQL Part
------------

Ja eigentlich war es der Plan das meine Kollegen sich mit dem Thema beschäftigen aber sie hatten Probleme und wir trafen
uns gemeinsam. Okay, an sich kein Problem, ich wollte mich für meine Bachelorarbeit eh mehr mit der OSM Datenbank
beschäftigen.
Nach einigen Stunden gemeinsam am Tool arbeiten welches die `project.mml` Zeit sensitiv machen soll, gaben wir auf ...
Wir sahen kein Ende der Arbeit. Sobald wir einige Statements fertigstellen haben, haben wir diese an einer anderen Stelle
zerstört. Also hat einer aus dem SQL Team die Aufgabe übernommen die SQL Statements per Hand zu ändern und das
Projekt zu forken https://github.com/linuxluigi/openstreetmap-carto/

Damit mein Kollege das Projekt gut bearbeiten kann, habe ich extra Debug URL's eingefügt, so das die `project.mml`
mithilfe von `carto` zu einer `style.xml` zu konvertieren, welche der Tile-Server akzeptiert. An sich sehr praktisch
um an dem System langfristig zu arbeiten. Bei der Gelegenheit habe ich auch gleich eine URL eingefügt, wo ein normales
Tile erstellt wird, welches nicht Zeit sensitiv sind.

Die Dokumention & Travis
------------------------

Die Dokumentation ging recht flott von der Hand. In Gedanken überlegte ich zwar was ich vergessen habe aufzuschreiben
aber in großen und ganzen sollte das meiste dabei sein, der Rest kommt halt nach.
Was mich aber viel mehr fertig machte ... testen mit `TRAVIS`, an sich läuft es gut aber sobald ich versuchte in Travis
`Postgis` zu integrieren kamen bei mir immer Fehler. Das Problem dabei war auch, jeder Test dauerte zwischen 15 bis 45
Minuten... Aber auch nach Tagen keine Lösung. Egal, lass es erst einmal sacken vielleicht fällt mir ja später was ein.
Heute nun habe ich auf Reddit mein Projekt vorgestellt -> https://www.reddit.com/r/django/comments/db8jvb/feedback_for_a_time_sensitive_openstreetmap/

Nach 8 Stunden kam das erste Feedback zu mein großes Problem `TRAVIS`. Der User meinte, ich könnte es doch mit Docker
lösen -.- warum ich mir die Arbeit mache 2 Systeme aufzubauen. Nun weiß ich was ich morgen Probieren werden.

Fazit
-----

Ich bin ziemlich happy über das Ergebnis, es ist zwar noch etwas Arbeit um es Produktion fähig zu machen aber es
ist Absehbar. Die nächste Aufgabe wird hoffentlich sein, die Zukunft abzubilden. Ein Kartenmaterial zu erzeugen welches
den steigenden Meeresspiegel simuliert, mein Prof hat grundsätzlich gemeint das es funktionieren sollte. Ich werde
diesbezüglich noch etwas recherchieren und mit etwas Glück wird das nun meine Bachelorarbeit 😉

Update zu Travis
----------------

Kurz um, es läuft super. Die Test laufen nun auch viel schneller durch und ich kann gleichzeitig die Docker Container testen.
