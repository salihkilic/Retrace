from Engine.location import Location, Map
from Engine.object import Poi
from Assets import items

"""
################
EARTH LOCATIONS
################
"""

house = Location("House",
                 "Nestled in what was once a lively neighborhood, the house stands eerily quiet. Each room feels both alien and familiar, as if memories lie just out of reach, waiting to be rediscovered.",
                 [Poi("Window",
                      "Beyond the glass, streets that once thrived with daily life stand silent. An unsettling stillness blankets the scene, suggesting an abrupt pause in life's rhythm."),
                  Poi("Television",
                      "The screen, once a source of entertainment, remains black. No matter the button pressed, it gives no sign of life, amplifying the home's deafening silence."),
                  Poi("Table",
                      "Amongst decaying meals, a hastily written note speaks of an attack on Mars. The paper's creases hint at frequent handling, its message chilling."),
                  Poi("Desk",
                      "Amid scattered belongings, a handwritten letter urges its reader to cherish fleeting moments and embrace the present, rather than chase forgotten memories.")],
                 None,
                 """
                           ====
                           !!!!
      ==========================
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  ||      _____          _____    ||
  ||      | | |          | | |    ||
  ||      |-|-|          |-|-|    ||
  ||      #####          #####    ||
  ||                              ||
  ||      _____   ____   _____    ||
  ||      | | |   @@@@   | | |    ||
  ||      |-|-|   @@@@   |-|-|    ||
  ||      #####   @@*@   #####    ||
  ||              @@@@            ||
******************____****************
*************************************
         
                [HOUSE]
                 """)

laboratory = Location("Laboratory",
                      "From its imposing exterior with dark-tinted windows, the laboratory whispers of secrets and untold stories. An ever-present air of mystery cloaks the building, as if it's guarding the answers to the world's unsettling condition.",
                      [Poi("Memory Extractor",
                           "Dominated by blinking lights and humming machinery, this device stands out. Its purpose becomes clear: a tool to reclaim lost memories or choose the bliss of forgetfulness once again.")],
                      None,
                      '''
                 _ _.-'`-._ _
                ;."________".;
     _________n.[____________].n_________
    |""_""_""_""||==||==||==||""_""_""_""]
    |"""""""""""||..||..||..||"""""""""""|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
 ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
                  Laboratory
                      ''')

office = Location("Office",
                  "This once-bustling workplace now seems abandoned. The building's facade displays a familiar name, with the front doors ajar, hinting at a hasty exodus. Signs of a recent struggle are evident, weaving tales of desperation and hope.",
                  [Poi("Reception desk",
                       "Paperwork strewn about, an overturned coffee cup, and lifeless gadgets paint a picture of a receptionist's hurried departure, leaving behind unanswered questions."),
                   Poi("Office rooms",
                       "Navigating the corridor reveals numerous office doors. Yet, one nameplate stirs a feeling of deja vu. Within the room, a gleaming keycard promises passage to uncharted horizons.")],
                  None,
                  """
                        .|
                       | |
                       |'|            ._____
               ___    |  |            |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
--------------------------------------------------------
                   [Office District]
                  """)

earth_spaceport = Location("Spaceport",
                           "The spaceport stands scarred from conflict. Wrecked ships are strewn about, each telling tales of desperate battles. Yet amidst the ruins, there's a hint of salvation for those brave enough to seek it.",
                           [Poi("Personal Spaceship",
                                "Untouched by the surrounding chaos, one ship stands pristine. Intriguingly, a number etched on its hull matches the spaceship keycard, suggesting a bond yet to be remembered."),
                            Poi("Crashed spaceship",
                                "Metal twisted into grotesque shapes, shattered windows, and the eerie absence of life speak of a tragic descent. The aftermath of a journey ended too soon."),
                            Poi("Transport spaceship",
                                "Giant cargo bays lie exposed, revealing their hollow innards. Scattered remnants of supplies and clear signs of looting indicate the desperation of those left behind.")],
                           None,
                           """                                                                        
  .            #     ## ..#++.                                .   . ..  . 
                 .    #       .                                       . . 
                   -   ## #+#                                             
                     #   ### .#                                           
                       #                                                  
                    #############                                         
                      +# #.  . #    #####################                 
                     +        -++##-.  .    .-###..##                     
 .   .            ..   ######   Earth    ###    ###                   ... 
                     #       .#####.#+###-    ###                       . 
                      ####  #       #      ####                           
                      # ###.#       #     #+                              
                      # ### #       #  ###                                
                        #.# #       ####                                  
 ---.-.-.-.....-.-..- # #++ # --   ###  .--+++++++++++++++++++++######### 
                      #.##.##    ##                                       
                      ### - # ###                                         
                        #++##-#                                           
 .................    # ##  #                                             
 .... ............---. #  ##  -------.--......... ..
                  [Earth Spaceport]                      
""")

"""
################
MOON LOCATIONS
################
"""
moon_spaceport = Location("Spaceport on Moon",
                          "The lunar outpost's vastness is constrained only by the titanic dome arching overhead. Within its confines, the metallic glints of spacecraft and structures contrast the moon's grey regolith. An almost eerie stillness lingers.",
                          [Poi("Empty spaceship",
                               "Its desolation speaks volumes. Inside, a tattered note's plea to loved ones stands testament to a tragic tale: one of loss to the ruthless looters."),
                           Poi("Spaceport Utilities center",
                               "A hub of once-vibrant activity, now silent. Toolkits scattered, equipment stands cold and idle. A one-stop-shop for spacefarers, now trapped in lunar time.")
                           ],
                          None,
                          """                                                                        
  .            #     ## ..#++.                                .   . ..  . 
                 .    #       .                                       . . 
                   -   ## #+#                                             
                     #   ### .#                                           
                       #                                                  
                    #############                                         
                      +# #.  . #    #####################                 
                     +        -++##-.  .    .-###..##                     
 .   .            ..   ######   Moon    ###    ###                   ... 
                     #       .#####.#+###-    ###                       . 
                      ####  #       #      ####                           
                      # ###.#       #     #+                              
                      # ### #       #  ###                                
                        #.# #       ####                                  
 ---.-.-.-.....-.-..- # #++ # --   ###  .--+++++++++++++++++++++######### 
                      #.##.##    ##                                       
                      ### - # ###                                         
                        #++##-#                                           
 .................    # ##  #                                             
 .... ............---. #  ##  -------.--......... ..
                  [Moon Spaceport]                      
""")

platform = Location("Moon viewing platform",
                    "An expanse of silver-gray stretches out, bordered only by the vastness of space. Here, the moon's barrenness meets the stars' twinkle, a stark contrast to the empty outpost.",
                    [Poi("Loving couple",
                         "Time might have ravaged their bodies, leaving behind skeletal remnants, but death couldn't part their intertwined hands, a testament to enduring love."),
                     Poi("Moon view",
                         "The barren expanse mirrors the desolation seen elsewhere. An unsettling realization dawns: the vast universe seems just as empty and lifeless as the places recently traversed.")
                     ],
                    None,
                    """
                     ++                     
                  .........                 
              .------------+-.              
           +---------..--.......+           
        #----......... ..          -        
     -.  ........----------------.....+     
  +------............     .              .  
 --+---.--.-..--.-#--.-.+--..-.-++..-.-#--. 
          ###                .-#            
          #+#                .-#            
          #.#                .-#            
          -.#                . #            
   .+-  -+-.#  ++  +- .++. -+++#- -++. .    
   .+-  -+-.#  ++  +- .++-.-+#+#+ -++. .    
   -. -. .. .. --+..--..+-+---.+-.--..--    
          ###       - +. .++.+##-           
          # +    - #  +. .+#+# +            
          - # + ----  +-+-.  - +            
      #----++#-- .++.--.     - +            
        -+- #+#- #+-.        -.#            
      . -+-.#+++..-          - #            
      --+##-###+ -+# .       -.#            
          #+##-# .++. +-     +##            
          --#   #-##. +-  -  -.+            
          - #     .##++- .+# -.#            
          - #        +.#..++.- #            
          --#           ++##.-.#            
          - #              --# +            
 +#                   .     .+----.--...    

           
                    
                    """)

cafe = Location("Cafe Ditin",
                "Echoes of laughter and clinking glasses once filled this bar. Now, only silence prevails, disrupted occasionally by the hollow gazes of skeletal patrons.",
                [Poi("Tables",
                     "Three skeletons seated, a chilling remnant of a time past. An empty chair poses questions. Among the debris, a business card resonates familiarity: a name from the player's fragmented past."),
                 Poi("Bar",
                     "Broken bottles, empty glasses. The bar's large mirror reflects a revelation: the player's forehead bears a partially healed wound, unseen till now."),
                 Poi("Backdoor",
                     "Barely ajar, the backdoor reveals a soldier, lifeless but seated in quiet contemplation. Beyond him, Earth looms over the horizon, a silent sentinel to the solitude.")
                 ],
                None,
                """           
     _______________________________
    [=U=U=U=U=U=U=U=U=U=U=U=U=U=U=U=]
    |.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.|
    |        +-+-+-+-+-+-+-+        |
    |        | Cafe  Ditin |        |
    |        +-+-+-+-+-+-+-+        |
    |.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.|
    |  _________  __ __  _________  |
  _ | |___   _  ||[]|[]||  _      | | _
 (!)||OPEN|_(!)_|| ,| ,||_(!)_____| |(!)
.T~T|:.....:T~T.:|__|__|:.T~T.:....:|T~T.
                """)

"""
################
MARS LOCATIONS
################
"""

mars_spaceport = Location("Mars Spaceport",
                          "The vast expanse is littered with evidence of intense warfare: demolished buildings and war-ready ships, some scarred and burned, tell a silent tale of interstellar conflict.",
                          [Poi("Empty warship",
                               "Its towering form radiates power. Pocked with burn marks and gouges, its once-impenetrable hull now bears testimony to ferocious confrontations. Entry seems an insurmountable challenge."),
                           Poi("Destroyed buildings",
                               "Ruins of a once-thriving complex: shattered armories, collapsed barracks, and half-melted watchtowers. The scene paints a story of an epic battle, a last stand of sorts on this Martian base.")
                           ],
                          None,
                          """                                                                        
  .            #     ## ..#++.                                .   . ..  . 
                 .    #       .                                       . . 
                   -   ## #+#                                             
                     #   ### .#                                           
                       #                                                  
                    #############                                         
                      +# #.  . #    #####################                 
                     +        -++##-.  .    .-###..##                     
 .   .            ..   ######   Mars    ###    ###                   ... 
                     #       .#####.#+###-    ###                       . 
                      ####  #       #      ####                           
                      # ###.#       #     #+                              
                      # ### #       #  ###                                
                        #.# #       ####                                  
 ---.-.-.-.....-.-..- # #++ # --   ###  .--+++++++++++++++++++++######### 
                      #.##.##    ##                                       
                      ### - # ###                                         
                        #++##-#                                           
 .................    # ##  #                                             
 .... ............---. #  ##  -------.--......... ..
                  [Mars Spaceport]                      
""")

forget_inc = Location("Forget Inc",
                      "Standing mysteriously amidst chaos, Forget Inc's building beckons. The open door invites curiosity, but a menacing military robot stands guard, its intent clear.",
                      [Poi("Conference room",
                           "The sprawling table holds presentation remnants: diagrams and notes hinting at a revolutionary PTSD solution—memory removal. Could it be the key?"),
                       Poi("Forget Labs",
                           "Machines, once cutting-edge, lay in ruins. Among the debris, the lifeless CEO, his identity tag dangling, perhaps holding secrets within its chip.")
                       ],
                      None,
                      '''
                         |~
                     _|__|__|_                
     ___________    _|  | |  |_    ___________    
    (__IXIXIXIXI___|_|__|_|__|_|___IXIXIXIXI__)
    (__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)
    (__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)
    (__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)
    (__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)
    (__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)
  /)(__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)
_/ )(__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)_/)_
 ~^^(__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__) ~~^
^~~ (__|"|"|"|"| [=][=] [=] [=][=] |"|"|"|"|__)~~^
"""""IXI~IXI~IXI~IXI~=I=I=I=I=~IXI~IXI~IXI~IXI""""""
     """"""""""""""""""|   |""""""""""""""""""
                   
                   [FORGET Inc.]                    
                      ''')

military_base = Location("Military Base",
                         "Death's pallor hangs heavy. Bodies of fallen soldiers punctuate the area, grim reminders of a battle lost. Yet, the base's secrets remain, beckoning discovery.",
                         [Poi("Military Research Center",
                              "Papers scattered everywhere. One report stands out: it speaks of erasing soldier memories with startling success, yet hints at the possibility of their haunting return."),
                          Poi("Command center",
                              "A room of eerie silence, save for the soft hum of numerous screens. Documents allude to a catastrophic war, sparked by solar flare-induced tech failures."),
                          Poi("Robot center",
                              "Not a data haven, but a birthplace of robotic guards. Abandoned, but for a singular object: a remote, perhaps holding power over mechanical sentinels.")
                          ],
                         None,
                         """                                                                
                          
     ..                                                                  ..     
 ..++++++.                                                            .++++++.  
 ---#..#-..                                                          --+#..+-.- 
   ######.                                                            .######   
   .#++#              .......                       .... ..             ##++.   
   .++##.        ..####+-+####..                ..####+-+####..         #+++    
   .#++-..      .##----+++----+##.            .##+----++-----##.      ..#++#.   
   .++-...    .##--#++++#++++#--##.          .##--#+++++++++#--##.    ..#-+..   
.+###+#.###+..##---#++++#+++++-+-+###-+..--####---++++++++++----##..+###--++###.
---+-++++-----#-##-#++###+#+++-##-#+------+--#-##-++++++++++--##-#-----#-++#+---
+++#++++#+++++#++++###########++++##++++++++##++++##########+++++#+++++#++++#+++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                                 [Military Base]
                         
                         """)

"""
################
MAPS
################
"""

earth = Map("Earth",
            [house, office, laboratory, earth_spaceport],
            """
       +-------------------+
       |                   |
       |     Laboratory    |
       |                   |
       +-------------------+


+-------+
|       |           +---------------------+
| House |           |                     |
|       |           |                     |
+-------+           |      Spaceport      |
                    |                     |
                    |                     |
                    +---------------------+

 +-------------------+
 |                   |
 |      Office       |
 |                   |
 |                   |
 +-------------------+
           """)

moon = Map("Moon",
           [moon_spaceport, cafe, platform],
           """
                                   +-------+
                                   |       |
                                   | Cafe  |
                                   | Ditin |
                                   |       |
                                   +-------+

                 +-------------+
                 |             |
                 |             |
                 |  Spaceport  |
                 |             |
                 |             |
                 +-------------+


+----------+
|          |
| Moon     |
| Viewing  |
| Platform |
|          |
+----------+
           """)

mars = Map("Mars",
           [mars_spaceport, military_base, forget_inc],
           """
                    +---------------------+
                    |                     |
                    |    Military Base    |
                    |                     |
+---------------+   +---------------------+
|               |
|               |
|               |
|  Forget Inc   |        +-------------------+
|               |        |                   |
|               |        |                   |
|               |        |     Spaceport     |
+---------------+        |                   |
                         |                   |
                         +-------------------+
           """)
