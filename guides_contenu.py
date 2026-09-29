#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contenu des pages guide.

Chaque fait chiffré provient d'une source officielle vérifiée en septembre 2026
(aéroport de Nice, Métropole Nice Côte d'Azur, ville de Nice, Port de Nice,
office de tourisme métropolitain). Les informations incertaines ont été écartées
plutôt qu'approximées : ni tarif de carnet, ni distance non mesurée, ni
« gratuité en août », ni plage de sable.
"""

GUIDES = [
# ────────────────────────────────────────────────────────────────────────────
{
 'slug_fr': 'aeroport-nice', 'slug_en': 'nice-airport',
 'fr': {
  'titre': "De l'aéroport de Nice au centre-ville",
  'meta_titre': "De l'aéroport de Nice au centre : tram, taxi, tarifs — Nice Port Duplex",
  'meta_desc': "Rejoindre le centre de Nice et le Port Lympia depuis l'aéroport : tramway ligne 2 en direct, tarifs, durée et alternatives en taxi.",
  'carte_titre': "Venir de l'aéroport",
  'carte_desc': "Tramway, taxi, durée et tarifs pour rejoindre le centre.",
  'chapeau': "L'aéroport de Nice est à une demi-heure du centre-ville, et depuis 2019 un tramway relie directement les deux terminaux au Port Lympia. C'est, dans presque tous les cas, la meilleure option.",
  'corps': """
<h2>Le tramway, ligne 2</h2>

<p>La ligne 2 du tramway part des terminaux 1 et 2 et son terminus est <strong>Port Lympia</strong>. Aucune correspondance n'est nécessaire : vous montez à l'aéroport, vous descendez au port. Le trajet dure environ vingt-six minutes, avec un passage toutes les sept à huit minutes en semaine.</p>

<p>La ligne traverse le centre — arrêt Jean Médecin pour les grands magasins, Garibaldi–Le Château pour le Vieux Nice — avant de rejoindre le port par un tunnel. Les quatre stations centrales sont souterraines, ce qui surprend quand on attend un tramway de surface.</p>

<div class="encadre">
<p><strong>Le ticket coûte 1,70 €</strong> au distributeur, valable 74 minutes correspondances comprises. Comptez 2 € si vous l'achetez à bord. Les moins de 11 ans et, depuis septembre 2026, les 65 ans et plus voyagent gratuitement.</p>
<p>Les tarifs évoluent : vérifiez sur <a href="https://www.lignesdazur.com" rel="noopener">lignesdazur.com</a> avant votre départ.</p>
</div>

<p>Entre les terminaux, le tramway est gratuit. Utile si votre vol arrive au terminal 2 et que vous devez rejoindre le 1.</p>

<h2>Le taxi</h2>

<p>La station de taxis se trouve à la sortie A3 des deux terminaux. L'aéroport publie un forfait de 32 € vers le centre de Nice ; les centrales de réservation en affichent plutôt 36 €. Aucun tarif réglementé n'est publié pour le port précisément : prévoyez entre 35 et 40 €, suppléments éventuels compris.</p>

<p>Le taxi se justifie surtout tard le soir, avec des bagages encombrants, ou à plusieurs — à quatre, l'écart avec quatre tickets de tramway devient mince.</p>

<h2>Les autres options</h2>

<p>Le <strong>bus 12+</strong> dessert l'aéroport et rejoint le centre par la Promenade des Anglais, la place Masséna et le Vieux Nice, avec un arrêt à cent cinquante mètres du terminal 1. Plus lent que le tramway, mais la vue sur la baie vaut le détour au moins une fois.</p>

<p>Pour aller plus loin sur la côte, des cars interurbains partent du terminal 2 vers Monaco et Menton, Cannes, Antibes ou Saint-Raphaël.</p>

<div class="encadre">
<p>Deux idées reçues à écarter : les lignes de bus 98 et 99 ne sont plus des navettes aéroport depuis l'ouverture du tramway, et la ligne 23 n'existe pas dans le réseau actuel.</p>
</div>

<h2>Et pour arriver au duplex</h2>

<p>Le terminus Port Lympia est à quelques minutes à pied du quai Lunel. Si vous logez chez nous, c'est le trajet le plus simple : un seul tramway, pas de correspondance, et vous arrivez au pied de l'immeuble.</p>
""",
 },
 'en': {
  'titre': "From Nice Airport to the city centre",
  'meta_titre': "Nice Airport to the city centre: tram, taxi, fares — Nice Port Duplex",
  'meta_desc': "Getting from Nice Airport to the city centre and Port Lympia: direct tram line 2, fares, journey time and taxi alternatives.",
  'carte_titre': "Coming from the airport",
  'carte_desc': "Tram, taxi, journey times and fares into the centre.",
  'chapeau': "Nice Airport sits half an hour from the city centre, and since 2019 a tramway has linked both terminals directly to Port Lympia. In almost every case, it is the best option.",
  'corps': """
<h2>Tram line 2</h2>

<p>Tram line 2 leaves from Terminals 1 and 2 and terminates at <strong>Port Lympia</strong>. No change is needed: you board at the airport and step off at the port. The journey takes around twenty-six minutes, with a tram every seven to eight minutes on weekdays.</p>

<p>The line crosses the centre — Jean Médecin for the shops, Garibaldi–Le Château for the Old Town — before reaching the port through a tunnel. Four central stations are underground, which catches out anyone expecting a street-level tram.</p>

<div class="encadre">
<p><strong>A single ticket costs €1.70</strong> from the machine, valid for 74 minutes including connections. Expect €2 if you buy on board. Under-11s and, since September 2026, over-65s travel free.</p>
<p>Fares change: check <a href="https://www.lignesdazur.com" rel="noopener">lignesdazur.com</a> before you travel.</p>
</div>

<p>Between terminals the tram is free — useful if you land at Terminal 2 and need Terminal 1.</p>

<h2>Taxis</h2>

<p>The taxi rank is at exit A3 of both terminals. The airport publishes a €32 flat fare to central Nice; booking services tend to quote €36. No regulated fare is published for the port specifically, so allow €35 to €40 including possible supplements.</p>

<p>A taxi earns its cost late at night, with bulky luggage, or with four people — at which point the gap with four tram tickets narrows considerably.</p>

<h2>Other options</h2>

<p>The <strong>12+ bus</strong> serves the airport and reaches the centre along the Promenade des Anglais, Place Masséna and the Old Town, stopping a hundred and fifty metres from Terminal 1. Slower than the tram, but the view across the bay is worth doing once.</p>

<p>For destinations further along the coast, intercity coaches leave Terminal 2 for Monaco and Menton, Cannes, Antibes and Saint-Raphaël.</p>

<div class="encadre">
<p>Two things worth unlearning: bus routes 98 and 99 stopped being airport shuttles when the tram opened, and route 23 does not exist on the current network.</p>
</div>

<h2>Getting to the duplex</h2>

<p>The Port Lympia terminus is a few minutes' walk from quai Lunel. If you are staying with us, this is the simplest route: one tram, no changes, and you arrive at the foot of the building.</p>
""",
 },
},
# ────────────────────────────────────────────────────────────────────────────
{
 'slug_fr': 'se-garer-a-nice', 'slug_en': 'parking-in-nice',
 'fr': {
  'titre': "Se garer à Nice sans y laisser sa journée",
  'meta_titre': "Se garer à Nice : parkings, tarifs et stationnement — Nice Port Duplex",
  'meta_desc': "Stationnement à Nice : parking Lympia et parkings du centre, tarifs de voirie, deux heures gratuites par jour et parcs relais.",
  'carte_titre': "Où se garer",
  'carte_desc': "Parkings, tarifs de voirie et parcs relais.",
  'chapeau': "Nice se gare mal quand on improvise et très bien quand on a compris trois règles. Voici les tarifs officiels, les heures gratuites que peu de visiteurs connaissent, et les parkings qui valent le détour.",
  'corps': """
<h2>Le parking du port</h2>

<p>Le parking Lympia, sur le quai Lunel, compte 382 places souterraines, dont dix pour les personnes à mobilité réduite et quarante avec borne de recharge. Il est ouvert sept jours sur sept.</p>

<table>
<tr><th>Période</th><th>Tarif</th></tr>
<tr><td>15 premières minutes</td><td>gratuites</td></tr>
<tr><td>Tarif courant</td><td>0,65 € par quart d'heure, soit 2,60 € l'heure</td></tr>
<tr><td>De 12h à 14h et de 19h à 1h</td><td>0,35 € par quart d'heure, soit 1,40 € l'heure</td></tr>
<tr><td>Forfait semaine</td><td>120 €</td></tr>
</table>

<p>Le forfait journée de 15 € existe, mais il est réservé aux passagers des ferries et croisières, sur justificatif. Pour un séjour de plusieurs jours, le forfait semaine devient vite intéressant.</p>

<p>Juste à côté, le parking Entrecasteaux offre 53 places en extérieur aux mêmes tarifs, avec trente minutes gratuites. Attention : il peut fermer pendant l'embarquement des ferries vers la Corse ou lors d'événements au port.</p>

<h2>La règle que personne ne connaît</h2>

<p>Le stationnement en surface est payant du lundi au samedi de 9h à 19h, et <strong>gratuit les dimanches et jours fériés</strong>. Jusque-là, rien d'original.</p>

<div class="encadre">
<p>Ce qui l'est davantage : vous avez droit à <strong>deux heures gratuites par jour</strong>, du lundi au samedi, à condition de prendre un ticket à l'horodateur. Deux heures et quart pour un véhicule zéro émission.</p>
<p>Le ticket est indispensable. Sans lui, pas de gratuité — et l'amende tombe.</p>
</div>

<p>Au-delà, la grille monte doucement : 1,20 € l'heure, 2,40 € pour deux heures. La durée est plafonnée à deux heures et quart consécutives, après quoi vous risquez un forfait post-stationnement de 25 €. Le paiement se fait à l'horodateur ou via l'application PayByPhone.</p>

<h2>Une heure gratuite en parking couvert</h2>

<p>Plusieurs parkings du centre offrent la première heure. Les plus utiles depuis le port et le Vieux Nice :</p>

<ul>
<li><strong>Corvésy</strong>, 3 rue Alexandre Mari — au bord du Vieux Nice</li>
<li><strong>Palais de Justice</strong> — en plein cœur de la vieille ville</li>
<li><strong>Saleya</strong> — sous le marché aux fleurs</li>
<li><strong>Sulzer</strong> et <strong>Promenade des Arts</strong></li>
</ul>

<p>Pour une course rapide ou un déjeuner, cette heure suffit souvent.</p>

<h2>Les parcs relais</h2>

<p>La métropole gère dix parcs relais, soit près de trois mille cinq cents places. Le principe est simple : <strong>le stationnement est gratuit si vous faites un aller-retour en transport en commun dans la journée</strong>.</p>

<p>C'est la solution si vous arrivez en voiture et comptez visiter à pied : vous laissez le véhicule en périphérie — Henri Sappia, Charles Ehrmann, Vauban — et vous entrez en ville en tramway.</p>

<div class="encadre">
<p>Une idée reçue à écarter : il n'existe aucune gratuité générale du stationnement au mois d'août à Nice. Les seuls régimes de gratuité sont le dimanche, les jours fériés, et les deux heures quotidiennes évoquées plus haut.</p>
</div>
""",
 },
 'en': {
  'titre': "Parking in Nice without losing your day",
  'meta_titre': "Parking in Nice: car parks, rates and street parking — Nice Port Duplex",
  'meta_desc': "Parking in Nice: the Lympia car park and central options, street parking rates, two free hours a day, and park-and-ride sites.",
  'carte_titre': "Where to park",
  'carte_desc': "Car parks, street rates and park-and-ride.",
  'chapeau': "Nice is difficult to park in if you improvise, and straightforward once you know three rules. Here are the official rates, the free hours few visitors know about, and the car parks worth the walk.",
  'corps': """
<h2>The port car park</h2>

<p>The Lympia car park on quai Lunel has 382 underground spaces, ten of them for reduced-mobility drivers and forty with charging points. It is open seven days a week.</p>

<table>
<tr><th>Period</th><th>Rate</th></tr>
<tr><td>First 15 minutes</td><td>free</td></tr>
<tr><td>Standard rate</td><td>€0.65 per quarter hour — €2.60 an hour</td></tr>
<tr><td>12pm–2pm and 7pm–1am</td><td>€0.35 per quarter hour — €1.40 an hour</td></tr>
<tr><td>Weekly pass</td><td>€120</td></tr>
</table>

<p>A €15 day rate exists but is reserved for ferry and cruise passengers on proof of travel. For a stay of several days, the weekly pass quickly makes sense.</p>

<p>Next door, the Entrecasteaux car park offers 53 open-air spaces at the same rates, with thirty minutes free. One caveat: it may close during Corsica ferry boarding or when events are held at the port.</p>

<h2>The rule nobody knows</h2>

<p>Street parking is chargeable Monday to Saturday from 9am to 7pm, and <strong>free on Sundays and public holidays</strong>. So far, nothing unusual.</p>

<div class="encadre">
<p>What is unusual: you are entitled to <strong>two free hours a day</strong>, Monday to Saturday, provided you take a ticket from the machine. Two hours fifteen for a zero-emission vehicle.</p>
<p>The ticket is essential. Without it there is no free period — and the fine follows.</p>
</div>

<p>Beyond that the scale rises gently: €1.20 an hour, €2.40 for two hours. Stays are capped at two hours fifteen, after which you risk a €25 penalty. Pay at the machine or through the PayByPhone app.</p>

<h2>One free hour under cover</h2>

<p>Several central car parks give you the first hour. The most useful from the port and the Old Town:</p>

<ul>
<li><strong>Corvésy</strong>, 3 rue Alexandre Mari — on the edge of the Old Town</li>
<li><strong>Palais de Justice</strong> — in the heart of the old quarter</li>
<li><strong>Saleya</strong> — beneath the flower market</li>
<li><strong>Sulzer</strong> and <strong>Promenade des Arts</strong></li>
</ul>

<p>For a quick errand or a long lunch, that hour is often enough.</p>

<h2>Park and ride</h2>

<p>The metropolitan authority runs ten park-and-ride sites, close to three and a half thousand spaces. The principle is simple: <strong>parking is free if you make a return journey on public transport the same day</strong>.</p>

<p>This is the answer if you arrive by car and plan to explore on foot: leave the vehicle on the outskirts — Henri Sappia, Charles Ehrmann, Vauban — and come into town by tram.</p>

<div class="encadre">
<p>One myth worth dispelling: there is no general free parking in Nice during August. The only free periods are Sundays, public holidays, and the two daily hours described above.</p>
</div>
""",
 },
},
# ────────────────────────────────────────────────────────────────────────────
{
 'slug_fr': 'week-end-a-nice', 'slug_en': 'weekend-in-nice',
 'fr': {
  'titre': "Un week-end à Nice, sans courir",
  'meta_titre': "Un week-end à Nice : que voir et que faire en deux jours — Nice Port Duplex",
  'meta_desc': "Deux jours à Nice : Vieux Nice et Cours Saleya, colline du Château, Promenade des Anglais, musées et marchés, avec jours d'ouverture et tarifs.",
  'carte_titre': "Un week-end à Nice",
  'carte_desc': "Vieux Nice, colline du Château, marchés et musées.",
  'chapeau': "Nice se visite à pied. En deux jours on fait le tour de l'essentiel sans se presser, à condition de connaître les jours de fermeture — ils réservent quelques mauvaises surprises.",
  'corps': """
<h2>Samedi matin : le Vieux Nice</h2>

<p>Commencez par le <strong>Cours Saleya</strong>. Le marché aux fleurs s'y tient du mardi au dimanche — il est fermé le lundi, c'est la première chose à retenir. Le lundi, la place change de visage : environ cent quatre-vingts antiquaires et brocanteurs s'y installent de 7h à 18h.</p>

<p>Autour, les ruelles du Vieux Nice se parcourent sans plan. C'est le meilleur endroit pour goûter les spécialités locales : la <strong>socca</strong>, cette galette de pois chiches cuite au feu de bois, la <strong>pissaladière</strong> aux oignons et aux anchois, la tourte de blettes.</p>

<div class="encadre">
<p><strong>Chez Thérésa</strong>, 28 rue Droite, cuit sa socca dans un four à bois de 1867 et sert depuis 1925. Ouvert du mardi au dimanche, de 9h30 à 15h.</p>
<p>Côté port, <strong>Chez Pipo</strong>, 13 rue Bavastro, est une institution pour la socca et la pissaladière. Du mercredi au dimanche, de 11h30 à 14h30 et de 17h30 à 22h.</p>
</div>

<h2>Samedi après-midi : la colline du Château</h2>

<p>La colline domine la ville et sépare le Vieux Nice du port. Le panorama sur la baie des Anges d'un côté et sur le Port Lympia de l'autre est le plus beau de Nice, et l'accès au parc est libre et gratuit.</p>

<p>Le parc ouvre à 8h30 et ferme à 20h d'avril à octobre, à 18h le reste de l'année. On y monte à pied par les escaliers depuis le Vieux Nice ou depuis le port. Un ascenseur part de la rue des Ponchettes — en principe gratuit, mais son fonctionnement peut être interrompu pour maintenance, vérifiez sur place.</p>

<h2>Dimanche matin : la Promenade des Anglais</h2>

<p>Sept kilomètres le long de la baie, à faire à pied ou à vélo, tôt de préférence. Les plages qui la bordent sont de galets — c'est la nature du rivage niçois, pas un défaut d'entretien.</p>

<p>Le dimanche, le stationnement en surface est gratuit dans toute la ville : c'est le jour où venir en voiture ne coûte rien.</p>

<h2>Dimanche après-midi : les musées</h2>

<p>Deux musées valent le déplacement, et tous deux ferment le mardi.</p>

<p>Le <strong>musée Matisse</strong>, dans les hauteurs de Cimiez, demande 12 € en plein tarif. Un pass musées de la ville, valable quatre jours, coûte 15 € et devient rentable dès la deuxième visite. L'entrée est gratuite pour les moins de 18 ans, les étudiants et les demandeurs d'emploi.</p>

<p>Le <strong>musée national Marc Chagall</strong> fonctionne à part — c'est un musée national, non couvert par le pass municipal. Comptez 10 à 12 € selon la présence d'une exposition temporaire. Il ouvre de 10h à 18h avec une fermeture de 13h à 14h30, et l'entrée est gratuite pour tous le premier dimanche du mois.</p>

<h2>Si vous restez plus longtemps</h2>

<p>Le <strong>marché de la Libération</strong>, près de la Gare du Sud, se tient du mardi au dimanche le matin. Moins touristique que le Cours Saleya, c'est là que les Niçois font leurs courses.</p>

<p>La <strong>place Garibaldi</strong> accueille une brocante le troisième samedi de chaque mois, et un marché artisanal certains dimanches selon la saison.</p>
""",
 },
 'en': {
  'titre': "A weekend in Nice, without rushing",
  'meta_titre': "A weekend in Nice: what to see in two days — Nice Port Duplex",
  'meta_desc': "Two days in Nice: the Old Town and Cours Saleya, Castle Hill, the Promenade des Anglais, museums and markets, with opening days and prices.",
  'carte_titre': "A weekend in Nice",
  'carte_desc': "Old Town, Castle Hill, markets and museums.",
  'chapeau': "Nice is a walking city. Two days cover the essentials without hurrying — provided you know the closing days, which hold a few unpleasant surprises.",
  'corps': """
<h2>Saturday morning: the Old Town</h2>

<p>Start at the <strong>Cours Saleya</strong>. The flower market runs Tuesday to Sunday — it is closed on Mondays, which is the first thing to remember. On Mondays the square changes character entirely: around a hundred and eighty antique and second-hand dealers set up from 7am to 6pm.</p>

<p>Around it, the lanes of the Old Town are best walked without a map. This is where to try the local specialities: <strong>socca</strong>, a chickpea pancake baked over wood, <strong>pissaladière</strong> with onions and anchovies, and Swiss chard tart.</p>

<div class="encadre">
<p><strong>Chez Thérésa</strong>, 28 rue Droite, bakes its socca in an 1867 wood oven and has been trading since 1925. Tuesday to Sunday, 9.30am to 3pm.</p>
<p>By the port, <strong>Chez Pipo</strong>, 13 rue Bavastro, is an institution for socca and pissaladière. Wednesday to Sunday, 11.30am to 2.30pm and 5.30pm to 10pm.</p>
</div>

<h2>Saturday afternoon: Castle Hill</h2>

<p>The hill rises above the city and separates the Old Town from the port. The view over the Baie des Anges on one side and Port Lympia on the other is the finest in Nice, and the park is free to enter.</p>

<p>It opens at 8.30am and closes at 8pm from April to October, 6pm the rest of the year. You can climb the steps from the Old Town or from the port. A lift runs from rue des Ponchettes — free in principle, though it can be out of service for maintenance, so check on the day.</p>

<h2>Sunday morning: the Promenade des Anglais</h2>

<p>Seven kilometres along the bay, on foot or by bike, ideally early. The beaches along it are pebble — that is the nature of the Nice shoreline, not a lapse in maintenance.</p>

<p>On Sundays, street parking is free across the city: it is the one day driving in costs nothing.</p>

<h2>Sunday afternoon: the museums</h2>

<p>Two museums are worth the journey, and both close on Tuesdays.</p>

<p>The <strong>Matisse Museum</strong>, up in Cimiez, charges €12 full price. A city museum pass valid four days costs €15 and pays for itself on the second visit. Entry is free for under-18s, students and jobseekers.</p>

<p>The <strong>Marc Chagall National Museum</strong> works separately — it is a national museum, not covered by the city pass. Expect €10 to €12 depending on whether a temporary exhibition is running. It opens 10am to 6pm with a break from 1pm to 2.30pm, and entry is free for everyone on the first Sunday of the month.</p>

<h2>If you stay longer</h2>

<p>The <strong>Marché de la Libération</strong>, near the Gare du Sud, runs Tuesday to Sunday mornings. Less touristy than the Cours Saleya, it is where people in Nice actually shop.</p>

<p><strong>Place Garibaldi</strong> hosts a flea market on the third Saturday of each month, and a craft market on some Sundays depending on the season.</p>
""",
 },
},
# ────────────────────────────────────────────────────────────────────────────
{
 'slug_fr': 'plages-de-nice', 'slug_en': 'nice-beaches',
 'fr': {
  'titre': "Les plages de Nice, et laquelle choisir",
  'meta_titre': "Les plages de Nice : publiques, privées et galets — Nice Port Duplex",
  'meta_desc': "Vingt-trois plages publiques et quatorze privées à Nice. Lesquelles choisir depuis le port, pourquoi ce sont des galets, et ce qu'il faut emporter.",
  'carte_titre': "Les plages de Nice",
  'carte_desc': "Publiques ou privées, et la plus proche du port.",
  'chapeau': "Nice compte vingt-trois plages publiques et quatorze plages privées. Elles sont toutes de galets, et ce n'est pas un détail : cela change ce qu'on emporte.",
  'corps': """
<h2>Des galets, pas du sable</h2>

<p>Autant le dire tout de suite : le rivage niçois est fait de galets, sur toute sa longueur. Les visiteurs qui s'attendent à du sable sont parfois déçus, à tort — l'eau y est plus claire, précisément parce qu'il n'y a pas de sable en suspension.</p>

<div class="encadre">
<p>Deux objets changent tout : une <strong>paire de sandales de bain</strong>, car les galets brûlent en été et roulent sous les pieds, et un <strong>matelas fin</strong> ou une natte épaisse. Une simple serviette ne suffit pas.</p>
</div>

<h2>La plus proche du port</h2>

<p>La <strong>plage des Bains Militaires</strong>, au 50 boulevard Franck Pilatte, est immédiatement adjacente au port, entre celui-ci et le Cap de Nice. C'est la plage des habitants du quartier : on y accède par des escaliers et une dalle béton, elle est surveillée en saison et dispose d'un accès pour personnes à mobilité réduite.</p>

<p>Un avertissement, en revanche : le passage des gros navires peut provoquer des vagues importantes. Restez vigilant avec de jeunes enfants.</p>

<p>Juste à côté, la <strong>plage de la Réserve</strong>, à quelques centaines de mètres au sud-est du port, se compose de plusieurs petites criques successives. L'ambiance y est plus sauvage, et c'est notre préférée en fin de journée.</p>

<h2>Du côté du Vieux Nice</h2>

<p>De l'autre côté de la colline du Château, la <strong>plage des Ponchettes</strong> fait face à la vieille ville. C'est la plus centrale, surveillée en été, avec des terrains de beach-volley. Elle se remplit vite en juillet et août.</p>

<p>La <strong>Castel Plage</strong>, juste à l'ouest, au pied de la colline, offre un cadre un peu plus abrité.</p>

<h2>Publiques ou privées</h2>

<p>Les plages publiques sont gratuites et en libre accès. Les quatorze plages privées louent transats et parasols, avec restaurant et douches. Selon l'établissement et la saison, comptez plusieurs dizaines d'euros la journée pour deux transats.</p>

<p>Le choix dépend surtout de la durée : pour une heure de baignade, le public suffit largement. Pour une journée entière, le confort d'un transat se défend.</p>

<h2>Plus loin sur la côte</h2>

<p>Les villages voisins — Villefranche-sur-Mer, Beaulieu, Saint-Jean-Cap-Ferrat — offrent des criques plus abritées et souvent plus calmes, à quinze ou vingt minutes en train depuis la gare de Nice-Ville. La plage des Marinières, à Villefranche, est la plus vaste de la commune.</p>
""",
 },
 'en': {
  'titre': "The beaches of Nice, and which to choose",
  'meta_titre': "Nice beaches: public, private and pebbles — Nice Port Duplex",
  'meta_desc': "Twenty-three public beaches and fourteen private ones in Nice. Which to choose from the port, why they are pebble, and what to bring.",
  'carte_titre': "The beaches of Nice",
  'carte_desc': "Public or private, and the closest to the port.",
  'chapeau': "Nice has twenty-three public beaches and fourteen private ones. All of them are pebble, and that is not a detail — it changes what you pack.",
  'corps': """
<h2>Pebbles, not sand</h2>

<p>Best said straight away: the Nice shoreline is pebble, along its entire length. Visitors expecting sand are sometimes disappointed, though they shouldn't be — the water is clearer precisely because there is no sand suspended in it.</p>

<div class="encadre">
<p>Two items change everything: a <strong>pair of water shoes</strong>, because the pebbles burn in summer and roll underfoot, and a <strong>thin mattress</strong> or thick mat. A towel alone will not do.</p>
</div>

<h2>The closest to the port</h2>

<p><strong>Plage des Bains Militaires</strong>, at 50 boulevard Franck Pilatte, sits immediately beside the port, between it and Cap de Nice. This is the local beach: you reach it by steps and a concrete platform, it is supervised in season, and it has reduced-mobility access.</p>

<p>One warning, though: large ships passing can raise significant waves. Stay watchful with young children.</p>

<p>Just beyond, <strong>Plage de la Réserve</strong>, a few hundred metres south-east of the port, is made up of several small successive coves. The feel is wilder, and it is our favourite late in the day.</p>

<h2>On the Old Town side</h2>

<p>Across Castle Hill, <strong>Plage des Ponchettes</strong> faces the old quarter. It is the most central, supervised in summer, with beach volleyball courts. It fills quickly in July and August.</p>

<p><strong>Castel Plage</strong>, just to the west at the foot of the hill, is a slightly more sheltered setting.</p>

<h2>Public or private</h2>

<p>Public beaches are free and open to all. The fourteen private beaches rent sunloungers and parasols, with a restaurant and showers. Depending on the establishment and the season, expect several tens of euros a day for two loungers.</p>

<p>The choice comes down to how long you are staying: for an hour's swim, public is more than enough. For a full day, the comfort of a lounger has its arguments.</p>

<h2>Further along the coast</h2>

<p>The neighbouring villages — Villefranche-sur-Mer, Beaulieu, Saint-Jean-Cap-Ferrat — offer more sheltered and often quieter coves, fifteen to twenty minutes by train from Nice-Ville station. Plage des Marinières, at Villefranche, is the largest in that commune.</p>
""",
 },
},
]
