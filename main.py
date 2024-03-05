import customtkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import threading
import os
import configparser


playlist_count = 0


def add_random_track_to_queue():
    genres = ['A Cappella', 'Abstract', 'Abstract Beats', 'Abstract Hip Hop', 'Abstract Idm', 'Abstractro', 'Accordion',
              'Acid House', 'Acid Jazz', 'Acid Techno', 'Acousmatic', 'Acoustic Blues', 'Acoustic Pop',
              'Adult Standards', 'African Percussion', 'African Rock', 'Afrikaans', 'Afrobeat', 'Afrobeats',
              'Aggrotech', 'Albanian Pop', 'Album Rock', 'Albuquerque Indie', 'Alternative Americana',
              'Alternative Country', 'Alternative Dance', 'Alternative Emo', 'Alternative Hardcore',
              'Alternative Hip Hop', 'Alternative Metal', 'Alternative Metalcore', 'Alternative New Age',
              'Alternative Pop', 'Alternative Pop Rock', 'Alternative R&b', 'Alternative Rock',
              'Alternative Roots Rock', 'Ambeat', 'Ambient', 'Ambient Dub Techno', 'Ambient Fusion', 'Ambient Idm',
              'Ambient Psychill', 'Ambient Trance', 'Anarcho-punk', 'Andean', 'Anime', 'Anime Score', 'Anti-folk',
              'Antiviral Pop', 'Appalachian Folk', 'Arab Folk', 'Arab Pop', 'Arabesk', 'Argentine Indie',
              'Argentine Reggae', 'Argentine Rock', 'Armenian Folk', 'Art Rock', 'Athens Indie',
              'Atmospheric Black Metal', 'Atmospheric Post Rock', 'Atmospheric Post-metal', 'Aussietronica',
              'Austindie', 'Australian Alternative Rock', 'Australian Country', 'Australian Dance',
              'Australian Hip Hop', 'Australian Indie', 'Australian Pop', 'Austrian Hip Hop', 'Austropop',
              'Avant-garde', 'Avant-garde Jazz', 'Avantgarde Metal', 'Axe', 'Azonto', 'Bachata', 'Baile Funk',
              'Balearic', 'Balkan Brass', 'Banda', 'Bangla', 'Barbershop', 'Barnemusikk', 'Barnmusik', 'Baroque',
              'Baroque Ensemble', 'Basque Rock', 'Bass Music', 'Bass Trip', 'Bassline', 'Bay Area Hip Hop',
              'Beach Music', 'Beatdown', 'Beats & Rhymes', 'Bebop', 'Belgian Indie', 'Belgian Rock', 'Belly Dance',
              'Belorush', 'Bemani', 'Benga', 'Bhangra', 'Big Band', 'Big Beat', 'Big Room', 'Black Death',
              'Black Metal', 'Black Sludge', 'Black Thrash', 'Blackgaze', 'Blaskapelle', 'Bluegrass', 'Blues',
              'Blues-rock', 'Blues-rock Guitar', 'Bmore', 'Bolero', 'Boogaloo', 'Boogie-woogie', 'Bossa Nova',
              'Bossa Nova Jazz', 'Boston Rock', 'Bounce', 'Bouncy House', 'Bow Pop', 'Boy Band', 'Brass Band',
              'Brass Ensemble', 'Brazilian Composition', 'Brazilian Gospel', 'Brazilian Hip Hop', 'Brazilian Indie',
              'Brazilian Pop Music', 'Brazilian Punk', 'Breakbeat', 'Breakcore', 'Breaks', 'Brega', 'Breton Folk',
              'Brill Building Pop', 'British Alternative Rock', 'British Blues', 'British Brass Band',
              'British Dance Band', 'British Folk', 'British Indie Rock', 'British Invasion', 'Britpop', 'Broadway',
              'Broken Beat', 'Brooklyn Indie', 'Brostep', 'Brutal Death Metal', 'Brutal Deathcore', 'Bubble Trance',
              'Bubblegum Dance', 'Bubblegum Pop', 'Bulgarian Rock', 'Byzantine', 'C-pop', 'C64', 'C86', 'Cabaret',
              'Cajun', 'Calypso', 'Canadian Country', 'Canadian Hip Hop', 'Canadian Indie', 'Canadian Metal',
              'Canadian Pop', 'Candy Pop', 'Cantautor', 'Cante Flamenco', 'Canterbury Scene', 'Cantopop',
              'Canzone Napoletana', 'Capoeira', 'Carnatic', 'Catstep', 'Caucasian Folk', 'Ccm', 'Ceilidh', 'Cello',
              'Celtic', 'Celtic Christmas', 'Celtic Punk', 'Celtic Rock', 'Central Asian Folk', 'Chalga', 'Chamber Pop',
              'Chanson', 'Chanson Quebecois', 'Chaotic Black Metal', 'Chaotic Hardcore', 'Charred Death',
              'Chicago Blues', 'Chicago House', 'Chicago Indie', 'Chicago Soul', 'Chicano Rap',
              'Chilean Rock', 'Chill Groove', 'Chill Lounge', 'Chill-out', 'Chill-out Trance',
              'Chillstep', 'Chillwave', 'Chinese Indie Rock', 'Chinese Opera', 'Chinese Traditional', 'Chip Hop',
              'Chiptune', 'Choral', 'Choro', 'Christian Alternative Rock', 'Christian Christmas', 'Christian Dance',
              'Christian Hardcore', 'Christian Hip Hop', 'Christian Metal', 'Christian Music', 'Christian Punk',
              'Christian Rock', 'Christmas', 'Christmas Product', 'Cinematic Dubstep', 'Clarinet', 'Classic Afrobeat',
              'Classic Belgian Pop', 'Classic Chinese Pop', 'Classic Colombian Pop', 'Classic Czech Pop',
              'Classic Danish Pop', 'Classic Dutch Pop', 'Classic Eurovision', 'Classic Finnish Pop',
              'Classic Finnish Rock', 'Classic French Pop', 'Classic Funk Rock', 'Classic Garage Rock',
              'Classic Italian Pop', 'Classic Norwegian Pop', 'Classic Peruvian Pop', 'Classic Polish Pop',
              'Classic Psychedelic Rock', 'Classic Rock', 'Classic Russian Pop', 'Classic Russian Rock',
              'Classic Schlager', 'Classic Soundtrack', 'Classic Swedish Pop', 'Classic Turkish Pop',
              'Classic Venezuelan Pop', 'Classical', 'Classical Christmas', 'Classical Flute', 'Classical Guitar',
              'Classical Organ', 'Classical Performance', 'Classical Period', 'Classical Piano', 'College A Cappella',
              'College Marching Band', 'Colombian Rock', 'Columbus Ohio Indie', 'Comedy', 'Comedy Rock', 'Comic',
              'Commons', 'Complextro', 'Composition D', 'Concert Piano', 'Consort', 'Contemporary Classical',
              'Contemporary Country', 'Contemporary Folk', 'Contemporary Jazz', 'Contemporary Post-bop', 'Cool Jazz',
              'Corrosion', 'Corsican Folk', 'Country', 'Country Blues', 'Country Christmas', 'Country Dawn',
              'Country Gospel', 'Country Road', 'Country Rock', 'Coupe Decale', 'Coverchill', 'Covertrance',
              'Cowboy Western', 'Cowpunk', 'Crack Rock Steady', 'Croatian Pop', 'Crossover Prog', 'Crossover Thrash',
              'Crunk', 'Crust Punk', 'Cryptic Black Metal', 'Cuban Rumba', 'Cubaton', 'Cumbia', 'Cumbia Funk',
              'Cumbia Sonidera', 'Cumbia Villera', 'Cyber Metal', 'Czech Folk', 'Czech Rock', 'Dallas Indie',
              'Dance Pop', 'Dance Rock', 'Dance-punk', 'Dancehall', 'Dangdut', 'Danish Hip Hop', 'Danish Indie',
              'Danish Jazz', 'Danish Pop', 'Danish Pop Rock', 'Dansband', 'Danseband', 'Dansktop', 'Dark Ambient',
              'Dark Black Metal', 'Dark Cabaret', 'Dark Electro-industrial', 'Dark Hardcore', 'Dark Jazz',
              'Dark Minimal Techno', 'Dark Progressive House', 'Dark Psytrance', 'Dark Wave', 'Darkstep', 'Death Core',
              'Death Metal', 'Deathgrind', 'Deep Acoustic Pop', 'Deep Adult Standards', 'Deep Alternative R&b',
              'Deep Ambient', 'Deep Baroque', 'Deep Brazilian Pop', 'Deep Breakcore', 'Deep Canadian Indie', 'Deep Ccm',
              'Deep Cello', 'Deep Chill', 'Deep Chill-out', 'Deep Christian Rock', 'Deep Classic Garage Rock',
              'Deep Classical Piano', 'Deep Comedy', 'Deep Contemporary Country', 'Deep Dance Pop', 'Deep Darkpsy',
              'Deep Deep House', 'Deep Deep Tech House', 'Deep Delta Blues', 'Deep Disco', 'Deep Disco House',
              'Deep Discofox', 'Deep Downtempo Fusion', 'Deep Dub Techno', 'Deep East Coast Hip Hop', 'Deep Euro House',
              'Deep Eurodance', 'Deep Filthstep', 'Deep Flow', 'Deep Folk Metal', 'Deep Free Jazz', 'Deep Freestyle',
              'Deep Full On', 'Deep Funk', 'Deep Funk House', 'Deep G Funk', 'Deep German Indie', 'Deep German Punk',
              'Deep Gothic Post-punk', 'Deep Happy Hardcore', 'Deep Hardcore', 'Deep Hardcore Punk', 'Deep Hardstyle',
              'Deep House', 'Deep Indian Pop', 'Deep Indie Pop', 'Deep Indie Rock', 'Deep Indie Singer-songwriter',
              'Deep Italo Disco', 'Deep Jazz Fusion', 'Deep Jazz Guitar', 'Deep Jazz Piano', 'Deep Latin Alternative',
              'Deep Liquid', 'Deep Liquid Bass', 'Deep Melodic Death Metal', 'Deep Melodic Hard Rock',
              'Deep Melodic House', 'Deep Melodic Metalcore', 'Deep Minimal Techno', 'Deep Motown', 'Deep Neo-synthpop',
              'Deep Neofolk', 'Deep New Wave', 'Deep Nordic Folk', 'Deep Northern Soul', 'Deep Opera',
              'Deep Orchestral', 'Deep Orgcore', 'Deep Pop Emo', 'Deep Pop Punk', 'Deep Power-pop Punk',
              'Deep Progressive House', 'Deep Progressive Trance', 'Deep Psychobilly', 'Deep Psytrance',
              'Deep Punk Rock', 'Deep Ragga', 'Deep Rai', 'Deep Regional Mexican', 'Deep Smooth Jazz', 'Deep Soft Rock',
              'Deep Soul House', 'Deep Soundtrack', 'Deep Southern Soul', 'Deep Space Rock', 'Deep String Quartet',
              'Deep Sunset Lounge', 'Deep Surf Music', 'Deep Symphonic Black Metal', 'Deep Talent Show',
              'Deep Tech House', 'Deep Thrash Metal', 'Deep Trap', 'Deep Turkish Pop', 'Deep Uplifting Trance',
              'Deep Vocal House', 'Deep Vocal Jazz', 'Delta Blues', 'Demoscene', 'Denver Indie',
              'Depressive Black Metal', 'Desert Blues', 'Desi', 'Destroy Techno', 'Detroit Hip Hop', 'Detroit Techno',
              'Didgeridoo', 'Digital Hardcore', 'Dirty South Rap', 'Dirty Texas Rap', 'Disco', 'Disco House',
              'Discofox', 'Dixieland', 'Djent', 'Dominican Pop', 'Doo-wop', 'Doom Metal', 'Doomcore', 'Doujin',
              'Downtempo', 'Downtempo Fusion', 'Downtempo Trip Hop', 'Drama', 'Dream Pop', 'Dreamo', 'Drill And Bass',
              'Drone', 'Drone Folk', 'Drone Metal', 'Drone Psych', 'Drum And Bass', 'Drumfunk', 'Dub', 'Dub Techno',
              'Dubstep', 'Dubstep Product', 'Dubsteppe', 'Duranguense', 'Dutch Hip Hop', 'Dutch House', 'Dutch Pop',
              'Dutch Rock', 'E6fi', 'Early Music', 'Early Music Ensemble', 'East Coast Hip Hop', 'Easy Listening',
              'Ebm', 'Ectofolk', 'Ecuadoria', 'Edm', 'Electric Blues', 'Electro', 'Electro Dub', 'Electro House',
              'Electro Jazz', 'Electro Latino', 'Electro Swing', 'Electro Trash', 'Electro-industrial',
              'Electroacoustic Improvisation', 'Electroclash', 'Electrofox', 'Electronic', 'Electronica',
              'Electronicore', 'Electropowerpop', 'Electropunk', 'Emo', 'Emo Punk', 'Enka', 'Entehno', 'Environmental',
              'Epicore', 'Estonian Pop', 'Ethereal Gothic', 'Ethereal Wave', 'Etherpop', 'Ethiopian Pop', 'Eurobeat',
              'Eurodance', 'Europop', 'Euroska', 'Eurovision', 'Exotica', 'Experimental', 'Experimental Dubstep',
              'Experimental Psych', 'Experimental Rock', 'Fado', 'Fake', 'Fallen Angel', 'Faroese Pop',
              'Fast Melodic Punk', 'Fidget House', 'Filmi', 'Filter House', 'Filthstep', 'Fingerstyle',
              'Finnish Hardcore', 'Finnish Hip Hop', 'Finnish Indie', 'Finnish Jazz', 'Finnish Metal', 'Finnish Pop',
              'Flamenco', 'Flick Hop', 'Folk', 'Folk Christmas', 'Folk Metal', 'Folk Punk', 'Folk Rock', 'Folk-pop',
              'Folk-prog', 'Folklore Argentino', 'Folkmusik', 'Footwork', 'Forro', 'Fourth World', 'Freak Folk',
              'Freakbeat', 'Free Improvisation', 'Free Jazz', 'Freestyle', 'French Folk', 'French Folk Pop',
              'French Hip Hop', 'French Indie Pop', 'French Movie Tunes', 'French Pop', 'French Punk', 'French Reggae',
              'French Rock', 'Full On', 'Funeral Doom', 'Funk', 'Funk Carioca', 'Funk Metal', 'Funk Rock',
              'Funky Breaks', 'Future Ambient', 'Future Garage', 'Futurepop', 'G Funk', 'Gabba', 'Galego', 'Gamecore',
              'Gamelan', 'Gangster Rap', 'Garage Pop', 'Garage Punk', 'Garage Punk Blues', 'Garage Rock', 'Gauze Pop',
              'Gbvfi', 'Geek Folk', 'Geek Rock', 'German Ccm', 'German Hip Hop', 'German Indie', 'German Metal',
              'German Oi', 'German Pop', 'German Pop Rock', 'German Punk', 'German Show Tunes', 'German Techno',
              'Ghettotech', 'Ghoststep', 'Girl Group', 'Glam Metal', 'Glam Rock', 'Glitch', 'Glitch Beats',
              'Glitch Hop', 'Glitter Trance', 'Goa Trance', 'Goregrind', 'Gospel', 'Gospel Blues', 'Gospel Reggae',
              'Gothic Alternative', 'Gothic Americana', 'Gothic Doom', 'Gothic Metal', 'Gothic Post-punk',
              'Gothic Rock', 'Gothic Symphonic Metal', 'Grave Wave', 'Greek Hip Hop', 'Greek House', 'Greek Indie',
              'Grim Death Metal', 'Grime', 'Grindcore', 'Grisly Death Metal', 'Groove Metal', 'Grunge', 'Grunge Pop',
              'Grupera', 'Guidance', 'Gypsy Jazz', 'Hands Up', 'Happy Hardcore', 'Hard Alternative', 'Hard Bop',
              'Hard Glam', 'Hard House', 'Hard Rock', 'Hard Stoner Rock', 'Hard Trance', 'Hardcore', 'Hardcore Breaks',
              'Hardcore Hip Hop', 'Hardcore Punk', 'Hardcore Techno', 'Hardstyle', 'Harmonica Blues', 'Harp',
              'Hatecore', 'Hauntology', 'Hawaiian', 'Healing', 'Heavy Alternative', 'Heavy Christmas',
              'Heavy Gothic Rock', 'Hi Nrg', 'Highlife', 'Hindustani Classical', 'Hip Hop', 'Hip Hop Quebecois',
              'Hip Hop Tuga', 'Hip House', 'Hip Pop', 'Hiplife', 'Hoerspiel', 'Hollywood', 'Honky Tonk', 'Horror Punk',
              'Horrorcore', 'House', 'Hungarian Hip Hop', 'Hungarian Pop', 'Hungarian Rock', 'Hurban', 'Hyphy',
              'Icelandic Pop', 'Idol', 'Illbient', 'Indian Classical', 'Indian Pop', 'Indian Rock', 'Indie Christmas',
              'Indie Dream Pop', 'Indie Emo', 'Indie Emo Rock', 'Indie Folk', 'Indie Fuzzpop', 'Indie Pop',
              'Indie Pop Rock', 'Indie Post-punk', 'Indie Psych-pop', 'Indie R&b', 'Indie Rock', 'Indie Shoegaze',
              'Indie Singer-songwriter', 'Indietronica', 'Indonesian Indie', 'Indonesian Pop', 'Indorock', 'Industrial',
              'Industrial Metal', 'Industrial Rock', 'Instrumental Post Rock', 'Intelligent Dance Music', 'Irish Folk',
              'Irish Indie', 'Irish Rock', 'Iskelma', 'Islamic Recitation', 'Israeli Rock', 'Italian Disco',
              'Italian Folk', 'Italian Hip Hop', 'Italian Indie Pop', 'Italian Jazz', 'Italian Pop', 'Italian Pop Rock',
              'Italian Progressive Rock', 'Italian Punk', 'Italo Dance', 'J-alt', 'J-ambient', 'J-core', 'J-dance',
              'J-idol', 'J-indie', 'J-metal', 'J-pop', 'J-poppunk', 'J-poprock', 'J-punk', 'J-rap', 'J-rock', 'J-theme',
              'Jam Band', 'Jangle Pop', 'Jangle Rock', 'Japanese Jazztronica', 'Japanese Psychedelic', 'Japanese R&b',
              'Japanese Standards', 'Japanese Traditional', 'Japanoise', 'Jazz', 'Jazz Bass', 'Jazz Blues',
              'Jazz Brass', 'Jazz Christmas', 'Jazz Funk', 'Jazz Fusion', 'Jazz Metal', 'Jazz Orchestra', 'Jazz Trio',
              'Jerk', 'Jig And Reel', 'Judaica', 'Jug Band', 'Juggalo', 'Jump Blues', 'Jump Up', 'Jumpstyle', 'Jungle',
              'K-hop', 'K-indie', 'K-pop', 'K-rock', 'Kabarett', 'Karneval', 'Kc Indie', 'Kindermusik', 'Kirtan',
              'Kiwi Rock', 'Kizomba', 'Klapa', 'Klezmer', 'Kompa', 'Kraut Rock', 'Kuduro', 'Kurdish Folk', 'Kwaito',
              'La Indie', 'Laboratorio', 'Laiko', 'Latin', 'Latin Alternative', 'Latin Christian', 'Latin Christmas',
              'Latin Electronica', 'Latin Hip Hop', 'Latin Jazz', 'Latin Metal', 'Latin Pop', 'Latvian Pop', 'Lds',
              'Leeds Indie', 'Levenslied', 'Liedermacher', 'Light Music', 'Lilith', 'Liquid Funk', 'Lithumania',
              'Liturgical', 'Lo Star', 'Lo-fi', 'Louisiana Blues', 'Louisville Indie', 'Lounge', 'Lounge House',
              'Lovers Rock', 'Lowercase', 'Luk Thung', 'Madchester', 'Maghreb', 'Magyar', 'Makossa', 'Malagasy Folk',
              'Malaysian Pop', 'Mallet', 'Mambo', 'Mande Pop', 'Mandopop', 'Manele', 'Marching Band', 'Mariachi',
              'Martial Industrial', 'Mashup', 'Math Pop', 'Math Rock', 'Mathcore', 'Mbalax', 'Medieval',
              'Medieval Rock', 'Meditation', 'Melancholia', 'Melbourne Bounce', 'Mellow Gold', 'Melodic Death Metal',
              'Melodic Hard Rock', 'Melodic Hardcore', 'Melodic Metalcore', 'Melodic Power Metal',
              'Melodic Progressive Metal', 'Memphis Blues', 'Memphis Hip Hop', 'Memphis Soul', 'Merengue',
              'Merengue Urbano', 'Merseybeat', 'Metal', 'Metal Guitar', 'Metalcore', 'Metropopolis', 'Mexican Indie',
              'Mexican Rock-and-roll', 'Mexican Son', 'Mexican Traditional', 'Miami Bass', 'Michigan Indie',
              'Microhouse', 'Military Band', 'Minimal', 'Minimal Dub', 'Minimal Dubstep', 'Minimal Melodic Techno',
              'Minimal Tech House', 'Minimal Techno', 'Minimal Wave', 'Mizrahi', 'Mod Revival', 'Modern Blues',
              'Modern Classical', 'Modern Country Rock', 'Modern Downshift', 'Modern Free Jazz', 'Modern Performance',
              'Modern Southern Rock', 'Modern Uplift', 'Monastic', 'Moombahton', 'Morna', 'Motivation', 'Motown',
              'Movie Tunes', 'Mpb', 'Musica Para Ninos', 'Musiikkia Lapsille', 'Musique Concrete',
              'Musique Pour Enfants', 'Muziek Voor Kinderen', 'Nasheed', 'Nashville Sound', 'Native American',
              'Necrogrind', 'Neo Classical Metal', 'Neo Honky Tonk', 'Neo Mellow', 'Neo Metal', 'Neo Soul',
              'Neo Soul-jazz', 'Neo-industrial Rock', 'Neo-pagan', 'Neo-progressive', 'Neo-psychedelic',
              'Neo-rockabilly', 'Neo-singer-songwriter', 'Neo-synthpop', 'Neo-trad Metal', 'Neo-traditional Country',
              'Neoclassical', 'Neofolk', 'Nepali', 'Nerdcore', 'Neue Deutsche Harte', 'Neue Deutsche Welle',
              'Neurofunk', 'Neurostep', 'New Age', 'New Age Piano', 'New Americana', 'New Beat', 'New Jack Smooth',
              'New Jack Swing', 'New Orleans Blues', 'New Orleans Jazz', 'New Rave', 'New Romantic', 'New Tribe',
              'New Wave', 'New Wave Pop', 'New Weird America', 'Ninja', 'Nintendocore', 'Nl Folk', 'No Wave', 'Noise',
              'Noise Pop', 'Noise Punk', 'Noise Rock', 'Nordic Folk', 'Nordic House', 'Norteno', 'Northern Irish Indie',
              'Northern Soul', 'Norwegian Gospel', 'Norwegian Hip Hop', 'Norwegian Jazz', 'Norwegian Metal',
              'Norwegian Pop', 'Norwegian Punk', 'Norwegian Rock', 'Nu Age', 'Nu Disco', 'Nu Electro', 'Nu Gaze',
              'Nu Jazz', 'Nu Metal', 'Nu Skool Breaks', 'Nu-cumbia', 'Nueva Cancion', 'Nursery', 'Nwobhm', 'Nwothm',
              'Nz Indie', 'Oi', 'Old School Hip Hop', 'Old-time', 'Opera', 'Operatic Pop', 'Opm', 'Oratory',
              'Orchestral', 'Organic Ambient', 'Orgcore', 'Orquesta Tipica', 'Orquesta Tropical', 'Oshare Kei',
              'Ostrock', 'Outer Hip Hop', 'Outlaw Country', 'Outsider', 'Outsider House', 'P Funk', 'Pagan Black Metal',
              'Pagode', 'Pakistani Pop', 'Permanent Wave', 'Persian Pop', 'Persian Traditional', 'Perth Indie',
              'Peruvian Rock', 'Piano Blues', 'Piano Rock', 'Piedmont Blues', 'Pipe Band', 'Poetry', 'Polish Hip Hop',
              'Polish Indie', 'Polish Jazz', 'Polish Pop', 'Polish Punk', 'Polish Reggae', 'Polka', 'Polynesian Pop',
              'Polyphony', 'Pop', 'Pop Christmas', 'Pop Emo', 'Pop House', 'Pop Punk', 'Pop Rap', 'Pop Rock', 'Popgaze',
              'Porro', 'Portland Indie', 'Portuguese Pop', 'Portuguese Rock', 'Post Rock', 'Post-disco',
              'Post-disco Soul', 'Post-grunge', 'Post-hardcore', 'Post-metal', 'Post-post-hardcore', 'Post-punk',
              'Power Blues-rock', 'Power Electronics', 'Power Metal', 'Power Noise', 'Power Pop', 'Power Violence',
              'Power-pop Punk', 'Praise', 'Progressive Alternative', 'Progressive Bluegrass',
              'Progressive Electro House', 'Progressive House', 'Progressive Metal', 'Progressive Psytrance',
              'Progressive Rock', 'Progressive Trance', 'Progressive Trance House', 'Progressive Uplifting Trance',
              'Protopunk', 'Psych Gaze', 'Psychedelic Blues-rock', 'Psychedelic Rock', 'Psychedelic Trance', 'Psychill',
              'Psychobilly', 'Pub Rock', 'Puerto Rican Rock', 'Punjabi', 'Punk', 'Punk Blues', 'Punk Christmas',
              'Punk Ska', 'Qawwali', 'Quebecois', 'Quiet Storm', 'R&b', 'Ragga Jungle', 'Ragtime', 'Rai', 'Ranchera',
              'Rap', 'Rap Metal', 'Rap Metalcore', 'Rap Rock', 'Raw Black Metal', 'Re:techno', 'Reading', 'Rebetiko',
              'Reggae', 'Reggae Fusion', 'Reggae Rock', 'Reggaeton', 'Regional Mexican', 'Relaxative', 'Remix',
              'Renaissance', 'Retro Electro', 'Retro Metal', 'Rhythm And Boogie', 'Riddim', 'Rio De La Plata',
              'Riot Grrrl', 'Rock', 'Rock Catala', 'Rock En Espanol', 'Rock Gaucho', 'Rock Noise', 'Rock Steady',
              'Rock-and-roll', 'Rockabilly', 'Romanian Pop', 'Romanian Rock', 'Romantic', 'Roots Reggae', 'Roots Rock',
              'Rumba', 'Russian Alternative', 'Russian Hip Hop', 'Russian Pop', 'Russian Punk', 'Russian Rock',
              'Rva Indie', 'Salsa', 'Salsa International', 'Samba', 'Saxophone', 'Schlager', 'Schranz', 'Scorecore',
              'Scottish Rock', 'Scratch', 'Screamo', 'Screamo Punk', 'Screamocore', 'Seattle Indie', 'Sega',
              'Serialism', 'Sertanejo', 'Sertanejo Tradicional', 'Sertanejo Universitario', 'Sevdah', 'Shanty',
              'Sheffield Indie', 'Shibuya-kei', 'Shimmer Pop', 'Shimmer Psych', 'Shiver Pop', 'Shoegaze', 'Show Tunes',
              'Singaporean Pop', 'Singer-songwriter', 'Sinhala', 'Ska', 'Ska Punk', 'Ska Revival', 'Skate Punk',
              'Skiffle', 'Skinhead Oi', 'Skinhead Reggae', 'Skweee', 'Slam Death Metal', 'Slash Punk', 'Slc Indie',
              'Sleaze Rock', 'Sleep', 'Slovak Hip Hop', 'Slovak Pop', 'Slovenian Rock', 'Slow Core', 'Sludge Metal',
              'Smooth Jazz', 'Smooth Urban R&b', 'Soca', 'Soda Pop', 'Soft Rock', 'Solipsynthm', 'Soukous', 'Soul',
              'Soul Blues', 'Soul Christmas', 'Soul Flow', 'Soul Jazz', 'Soundtrack', 'South African Jazz',
              'Southern Gospel', 'Southern Hip Hop', 'Southern Rock', 'Southern Soul', 'Southern Soul Blues',
              'Space Rock', 'Spanish Classical', 'Spanish Folk', 'Spanish Hip Hop', 'Spanish Indie Pop',
              'Spanish Indie Rock', 'Spanish Invasion', 'Spanish New Wave', 'Spanish Pop', 'Spanish Pop Rock',
              'Spanish Punk', 'Spanish Reggae', 'Speed Garage', 'Speed Metal', 'Speedcore', 'Spoken Word', 'Spytrack',
              'Steampunk', 'Steelpan', 'Stl Indie', 'Stomp And Flutter', 'Stomp And Holler', 'Stomp And Whittle',
              'Stomp Pop', 'Stoner Metal', 'Stoner Rock', 'Straight Edge', 'Street Punk', 'Stride', 'String Band',
              'String Folk', 'String Quartet', 'Substep', 'Sunset Lounge', 'Suomi Rock', 'Surf Music', 'Swamp Blues',
              'Swamp Pop', 'Swedish Alternative Rock', 'Swedish Hard Rock', 'Swedish Hip Hop', 'Swedish Indie Pop',
              'Swedish Indie Rock', 'Swedish Jazz', 'Swedish Metal', 'Swedish Pop', 'Swedish Pop Punk', 'Swedish Prog',
              'Swedish Punk', 'Swedish Reggae', 'Swedish Soft Pop', 'Swedish Synthpop', 'Swing', 'Swirl Psych',
              'Swiss Folk', 'Swiss Hip Hop', 'Swiss Rock', 'Symphonic Black Metal', 'Symphonic Metal', 'Symphonic Rock',
              'Synthpop', 'Taiwanese Pop', 'Talent Show', 'Tango', 'Tech House', 'Technical Brutal Death Metal',
              'Technical Death Metal', 'Techno', 'Teen Pop', 'Tejano', 'Tekno', 'Terrorcore', 'Texas Blues',
              'Texas Country', 'Thai Indie', 'Thai Pop', 'Thrash Core', 'Thrash Metal', 'Thrash-groove Metal',
              'Throat Singing', 'Tibetan', 'Tico', 'Timba', 'Tin Pan Alley', 'Traditional Blues',
              'Traditional British Folk', 'Traditional Country', 'Traditional Folk', 'Traditional Funk',
              'Traditional Irish Folk', 'Traditional Reggae', 'Traditional Rock', 'N Roll', 'Traditional Rockabilly',
              'Traditional Scottish Folk', 'Traditional Ska', 'Traditional Soul', 'Traditional Swing', 'Trance', 'Trance Hop',
              'Trap Music', 'Trapstep', 'Trash Rock', 'Triangle Indie', 'Tribal House', 'Tribute', 'Trip Hop',
              'Tropical', 'Trova', 'Turbo Folk', 'Turkish Alternative', 'Turkish Classical', 'Turkish Folk',
              'Turkish Hip Hop', 'Turkish Jazz', 'Turkish Pop', 'Turkish Rock', 'Turntablism', 'Twee Indie Pop', 'Twee Pop',
              'Twin Cities Indie', 'Tzadik', 'Uk Dub', 'Uk Garage', 'Uk Hip Hop', 'Uk Post - punk', 'Ukrainian Rock', 'Ukulele',
              'Unblack Metal', 'Underground Hip Hop', 'Underground Latin Hip Hop', 'Underground Pop Rap', 'Underground Power Pop',
              'Underground Rap', 'Uplifting Trance', 'Urban Contemporary', 'Vallenato', 'Vancouver Indie', 'Vapor House', 'Vaporwave',
              'Vegan Straight Edge', 'Vegas Indie', 'Velha Guarda', 'Venezuelan Rock', 'Video Game Music', 'Vienna Indie',
              'Vietnamese Pop', 'Viking Metal', 'Vintage Chanson', 'Vintage Country Folk', 'Vintage Gospel', 'Vintage Jazz', 'Vintage Reggae',
              'Vintage Rockabilly', 'Vintage Schlager', 'Vintage Swedish Pop', 'Vintage Swing', 'Vintage Swoon', 'Vintage Tango',
              'Vintage Western', 'Violin', 'Viral Pop', 'Visual Kei', 'Vocal House', 'Vocal Jazz', 'Vocaloid', 'Volksmusik',
              'Warm Drone', 'Welsh Rock', 'West African Jazz', 'West Coast Rap', 'Western Swing', 'Wind Ensemble', 'Witch House', 'Wonky',
              'Workout', 'World', 'World Chill', 'World Christmas', 'World Fusion', 'Worship', 'Wrestling', 'Wrock', 'Ye Ye', 'Yoik',
              'Yugoslav Rock', 'Zeuhl', 'Zillertal', 'Zim', 'Zolo', 'Zouglou', 'Zouk', 'Zydeco' ]

    random_genre = random.choice(genres)
    results = sp.search(q=f'genre:"{random_genre}"', type='track', limit=50)
    tracks = results['tracks']['items']

    if not tracks:
        print("No tracks found.")
        return

    random_track = random.choice(tracks)
    track_uri = random_track['uri']
    sp.add_to_queue(uri=track_uri)


def update_slider(event, slider):
    value = event.widget.get()
    if value.isdigit():
        slider.set(int(value))


def slider_activity(value, user_input):
    user_input.delete(0, 'end')
    user_input.insert(0, int(value))


def end_program():
    end_label = tk.CTkLabel(app, text="Tracks added successfully!", font=("Roboto", 20, "bold"), text_color="green")
    end_label.place(relx=0.5, rely=0.5, anchor='center')
    app.after(5000, app.quit)


def check_thread(thread, wait_label):
    if thread.is_alive():
        app.after(100, check_thread, thread, wait_label)
    else:
        wait_label.destroy()
        end_program()


def add_queue():
    for i in range(playlist_count):
        add_random_track_to_queue()


def process_user_input(input, user_input, input_frame):
    global playlist_count
    if input.isdigit() and int(input) > 0:
        playlist_count = int(input)
        user_input.destroy()
        for widget in input_frame.winfo_children():
            widget.destroy()

        wait_label = tk.CTkLabel(app, text="Adding tracks to queue...", font=("Roboto", 20, "bold"), text_color="cyan")
        wait_label.place(relx=0.5, rely=0.5, anchor='center')

        thread = threading.Thread(target=add_queue)  # Remove the parentheses after add_queue
        thread.start()
        check_thread(thread, wait_label)

    else:
        error_label = tk.CTkLabel(app, text="Please enter a number.")
        error_label.pack()
        app.after(5000, error_label.destroy)


def get_user_input(input_frame):
    input_frame.pack(fill=tk.BOTH, expand=True)
    s_label = tk.CTkLabel(master=input_frame, text="How many tracks do you want to add", font=("Roboto", 18, "bold"))
    s_label.pack(pady=(30, 0), anchor='s')
    user_input = tk.CTkEntry(input_frame)
    user_input.pack(pady=15)
    user_input.bind('<KeyRelease>', lambda event: update_slider(event, slider))
    slider = tk.CTkSlider(input_frame, from_=1, to=100, number_of_steps=99, command=lambda value: slider_activity(value, user_input))
    slider.pack(pady=15)
    submit_button = tk.CTkButton(input_frame, text="Submit", command=lambda: process_user_input(user_input.get(), user_input, input_frame))
    submit_button.place(relx=0.5, rely=0.5, anchor='center')
    app.mainloop()


def get_user_input_config():
    input_frame = tk.CTkFrame(app)
    input_frame.pack(fill=tk.BOTH, expand=True)

    client_id_label = tk.CTkLabel(input_frame, text="Enter your client_id:", font=("Roboto", 16, "bold"), text_color="white")
    client_id_label.pack(pady=(40, 0))
    client_id_entry = tk.CTkEntry(input_frame)
    client_id_entry.pack(pady=5)

    client_secret_label = tk.CTkLabel(input_frame, text="Enter your client_secret:", font=("Roboto", 16, "bold"), text_color="white")
    client_secret_label.pack(pady=(30, 0))
    client_secret_entry = tk.CTkEntry(input_frame)
    client_secret_entry.pack(pady=5)

    redirect_uri_label = tk.CTkLabel(input_frame, text="Enter your redirect_uri:", font=("Roboto", 16, "bold"), text_color="white")
    redirect_uri_label.pack(pady=(30, 0))
    redirect_uri_entry = tk.CTkEntry(input_frame)
    redirect_uri_entry.pack(pady=5)

    submit_button = tk.CTkButton(input_frame, text="Submit", font=("Roboto", 10), text_color="white", command=lambda: process_user_input_config(client_id_entry.get(), client_secret_entry.get(), redirect_uri_entry.get(), input_frame))
    submit_button.place(relx=0.5, rely=0.9, anchor='s')
    app.mainloop()


def process_user_input_config(client_id, client_secret, redirect_uri, input_frame):
    config['SPOTIFY'] = {'client_id': client_id, 'client_secret': client_secret, 'redirect_uri': redirect_uri}

    with open(config_file, 'w') as configfile:
        config.write(configfile)

    input_frame.destroy()
    app.quit()


def end_all():
    app.quit()
    quit()


app = tk.CTk()
app.title("RandomQueue")
app.geometry("420x600")
app.protocol("WM_DELETE_WINDOW", end_all)

config_file = 'config.sg'
config = configparser.ConfigParser()

if not os.path.exists(config_file):
    get_user_input_config()
    config.read(config_file)
    client_id = config.get('SPOTIFY', 'client_id')
    client_secret = config.get('SPOTIFY', 'client_secret')
    redirect_uri = config.get('SPOTIFY', 'redirect_uri')
else:
    config.read(config_file)
    client_id = config.get('SPOTIFY', 'client_id')
    client_secret = config.get('SPOTIFY', 'client_secret')
    redirect_uri = config.get('SPOTIFY', 'redirect_uri')

scope = 'playlist-read-private user-modify-playback-state playlist-modify-public playlist-modify-private user-top-read'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

input_frame = tk.CTkFrame(app)
get_user_input(input_frame)

