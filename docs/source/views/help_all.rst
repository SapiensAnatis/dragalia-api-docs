/help/all
==================================================

- Base address: production-api.dragalialost.com
- Method: GET
- Status code: 200

Request headers
----------------

.. code-block:: text

	user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
	accept: application/json, text/javascript, */*; q=0.01
	accept-language: en-GB,en;q=0.5
	accept-encoding: gzip, deflate, br
	origin: https://dragalialost.akamaized.net
	dnt: 1
	referer: https://dragalialost.akamaized.net/
	sec-fetch-dest: empty
	sec-fetch-mode: cors
	sec-fetch-site: cross-site
	te: trailers


Request body
----------------

.. code-block:: json

	null

Response headers
----------------

.. code-block:: text

	content-type: application/json
	access-control-allow-origin: *
	vary: Accept-Encoding
	content-encoding: gzip
	expires: Sat, 03 Sep 2022 16:47:14 GMT
	cache-control: max-age=0, no-cache, no-store
	pragma: no-cache
	date: Sat, 03 Sep 2022 16:47:14 GMT
	content-length: 46813
	set-cookie: ak_bmsc=27E0534E332890D55F51995F5A685D74~000000000000000000000000000000~YAAQ0tPerWI0x/2CAQAA684/BBAATpprYE+jJYpJMg98FOCbwX8BpjrzOwcuu9WXiEoprrFkiu7g5vOfZLQUpQyKXM0/5HzUklkd+KpL9OdEGZ8mDEOsQHkbJAXD9ts2K/x+OaMbQ+qWRYGho2+buznEmZAwXZylQrRuPbgImU5jPwwWN4U/Oc8uFEF4nPmOS5PoIAFc4FY+sfB4q2LQAu3FVG3FtgHC3rNt+OpQnw7HezQ3I3EEvxNamyeZtVhd15TU0L5GhCvUBbPHYrLHZ1Nho2kIPahWn6pUryUMRQxy5+v9L28kBkuC2xpzgaQAfmDn/krkMveD/mRrQOsyZ4Oey7zFoPUD0bnHCKaq42f/9bH75SMfykeh2ZVU8b9txTzzq1H85sMmS8dFuGtm; Domain=.dragalialost.com; Path=/; Expires=Sat, 03 Sep 2022 18:47:13 GMT; Max-Age=7199; HttpOnly


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "parent_list": [
	            {
	                "id": 1,
	                "title": "Home",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "174",
	                        "title": "What is Home?",
	                        "text": "<div>The default screen of Dragalia Lost.</div><div>From here you can go to the quest and event screen, or check notices and endeavors.</div>"
	                    },
	                    {
	                        "id": "175",
	                        "title": "Player Levels",
	                        "text": "<div>Increases when the experience points received upon clearing a quest reach a certain number.</div><div>When your player level increases, the limits of your stamina and number of friends does as well. In the Halidom, level limits for facilities will be unlocked and new facilities will become available.</div>"
	                    },
	                    {
	                        "id": "176",
	                        "title": "Wyrmite",
	                        "text": "<div>Used for things like summoning, continuing on quests, increasing your inventory space, and acquiring in-game items. Received as in-game rewards.</div>"
	                    },
	                    {
	                        "id": "177",
	                        "title": "Diamantium",
	                        "text": "<div>Used for things like summoning, continuing on quests, increasing your inventory space, and acquiring items in the game. Acquired by purchasing through the Shop.</div>"
	                    },
	                    {
	                        "id": "178",
	                        "title": "Mana",
	                        "text": "<div>Used to unlock nodes on mana circles. Received as in-game rewards.</div>"
	                    },
	                    {
	                        "id": "179",
	                        "title": "Rupies",
	                        "text": "<div>Used for things like constructing and leveling up facilities, and the crafting and upgrading of weapons. Can also be used to buy certain items in the Shop. Received as in-game rewards.<br>You can hold a maximum of 9,999,999,999 rupies. Any rupies obtained beyond 9,999,999,999 will be discarded.</div>"
	                    },
	                    {
	                        "id": "180",
	                        "title": "Stamina",
	                        "text": "<div>Used to undertake quests during solo play.</div><br><div>\u25a0Maximum stamina</div><div>Your maximum stamina will increase as your player level increases.</div><br><div>\u25a0Stamina restoration</div><div>Stamina refills at a rate of one point every six minutes.</div><div>Your stamina will stop refilling once you reach maximum stamina.</div><div>For example, if your stamina is 30/20, you will not gain any more as time passes.</div><br><div>Stamina can also be restored with diamantium, wyrmite, and certain items, as well as by collecting honey tea produced at the Halidom. Such items can replenish your stamina beyond the maximum.</div><div>For example, if you use an item to restore 20 stamina when your stamina is at 20/20, it will become 40/20.</div><br><div>Your stamina cannot be higher than 999.</div><div>For example, if your stamina is 999/20, it cannot be increased any further.</div><br><div>\u25a0Required stamina exceeds your maximum</div><div>You will not be able to begin a quest if the stamina required is greater than your maximum stamina.</div><div>For example, if a quest requires 30 stamina to begin and your stamina is 20/20, you will not be able to start it.</div>"
	                    },
	                    {
	                        "id": "181",
	                        "title": "Getherwings",
	                        "text": "<div>Used when playing co-op.</div><br><br><div>\u25a0Maximum getherwings</div><div>The maximum number you can hold is 12.</div><div>Note: Unlike stamina, the maximum number of getherwings you can hold will not increase along with your player level.</div><br><br><div>\u25a0Getherwing restoration</div><div>Getherwings restore at a rate of one every sixty minutes.</div><div>Your getherwings will stop refilling once you reach maximum getherwings.</div><div>For example, if you have 12/12 getherwings, you will not gain any more as time passes.</div><br><br><div>Getherwings can also be restored with diamantium, wyrmite, and certain items. Such items can restore your getherwings beyond the maximum.</div><div>For example, if you use an item to restore one getherwing when your getherwings are at 12/12, you will then have 13/12.</div><br><br><div>You cannot have more than 99 getherwings at one time.</div><div>For example, if your getherwings are 99/12, you cannot obtain any more.</div>"
	                    },
	                    {
	                        "id": "182",
	                        "title": "Notices",
	                        "text": "<div>Check out updates regarding the game or information about currently active events.</div>"
	                    },
	                    {
	                        "id": "183",
	                        "title": "Endeavors",
	                        "text": "<div>You can receive various rewards by completing endeavors. The following kinds of endeavors may be available:</div><div>\u30fbDaily</div><div>\u30fbLimited time</div><div>\u30fbNormal</div><div>\u30fbSpecial</div><div><br /></div><div>The conditions for fulfilling endeavors may vary.</div>"
	                    },
	                    {
	                        "id": "512",
	                        "title": "The Royal Regimen",
	                        "text": "<div>The Royal Regimen is a special set of endeavors that convey rewards upon completion.</div><div>These endeavors are grouped into three stages, and completing all endeavors in one stage will unlock the next stage.</div>"
	                    },
	                    {
	                        "id": "184",
	                        "title": "Quests",
	                        "text": "<div>Tackle the main campaign and event quests.</div>"
	                    },
	                    {
	                        "id": "186",
	                        "title": "Goodies",
	                        "text": "<div>Check here to claim in-game items and rewards.</div><div><br /></div><div>\u25a0History:</div><div>Check presents you have received in the past.</div><div>Note: Presents that have expired are deleted automatically.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 2,
	                "title": "Quests",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "425",
	                        "title": "Quest Progression",
	                        "text": "<div>During quests, you'll freely control adventurers to defeat enemies.</div><div><br /></div><div>Each quest has a special condition you'll need to fulfill in order to clear it, such as defeating a boss.</div><div><br /></div><div>If you fulfill a failure condition, such as the HP of all adventurers in your party reaching 0, you'll fail the quest.</div><div><br /></div><div>You will acquire rewards and experience points after clearing quests.</div>"
	                    },
	                    {
	                        "id": "426",
	                        "title": "Continuing",
	                        "text": "<div>You can use wyrmite, diamantium, or other items to continue if all of your adventurers' HP reach 0 during a quest.</div><div><br /></div><div>When you continue, your HP will be fully restored, and your dragon and skill gauges will be filled. The support-skill counter will also be reset.</div><div><br /></div><div>You can choose to continue up to three times per quest.</div>"
	                    },
	                    {
	                        "id": "427",
	                        "title": "More",
	                        "text": "<div>You can check quest information, victory conditions, and acquired items in the menu window. You can also change options via the Sound and Game menus.</div>"
	                    },
	                    {
	                        "id": "428",
	                        "title": "Giving Up",
	                        "text": "<div>You can abandon a quest by tapping the Give Up button in the menu window.</div><div><br /></div><div>All experience points, mana, rupies, and items you acquired during the quest will be lost. Your stamina will not be consumed.</div>"
	                    },
	                    {
	                        "id": "429",
	                        "title": "Preferred Team",
	                        "text": "<div>Use this feature to reassemble the party that cleared a quest.</div><div><br /></div><div>By checking Set as Preferred Team after clearing a quest, the next time you attempt that quest you can tap the quest's History button to recall the exact party you used before.</div>"
	                    },
	                    {
	                        "id": "430",
	                        "title": "Helpers",
	                        "text": "<div style=\"\">You can use the skills of helpers set by other players while in battle.</div><br><div style=\"\">The skills of players who are not friends can be used only once. If you are friends, they can be used up to three times.</div><div style=\"\"><br></div><div style=\"\">In some cases, your helper's abilities can also benefit your team. However, this is only true for helper abilities that affect the entire team.</div>"
	                    },
	                    {
	                        "id": "431",
	                        "title": "Acquiring Mana when Using Helpers",
	                        "text": "<div>You can acquire mana by bringing helpers on solo quests. Mana is directly granted to you upon clearing the quest.</div><div><br /></div><div>You can also acquire mana when your own helper is brought on quests by other users. That mana is sent to your Limited present box when you log in the following day and onward.</div>"
	                    },
	                    {
	                        "id": "432",
	                        "title": "Co-op Play",
	                        "text": "<div>You can play quests cooperatively with up to four players total.</div><div>When playing with two players, each may bring along one additional team member.</div><div>If you&#39;re playing with three players, the person who created the room can bring an additional team member.</div><br><div>If you join a co-op room hosted by another player, and they give up, you will be able to continue the quest on your own.</div><div>Wyrmite or diamantium will be consumed if you use the continue feature.</div>"
	                    },
	                    {
	                        "id": "185",
	                        "title": "Playing Co-op",
	                        "text": "<div>Take part in quests other players are recruiting for.</div>"
	                    },
	                    {
	                        "id": "433",
	                        "title": "Creating a Room",
	                        "text": "<div>You can create a room and recruit up to three players to join you on a quest.</div>"
	                    },
	                    {
	                        "id": "434",
	                        "title": "Room IDs",
	                        "text": "<div>Enter a room ID to gain access to a specific room.</div>"
	                    },
	                    {
	                        "id": "435",
	                        "title": "Finding a Room",
	                        "text": "<div>You can automatically join a co-op room for the quest you've selected.</div>"
	                    },
	                    {
	                        "id": "436",
	                        "title": "Social Rewards",
	                        "text": "<div>When playing co-op with another player for the first time, you can receive a reward after clearing the quest. You can receive this reward for the first 50 people you meet.</div>"
	                    },
	                    {
	                        "id": "437",
	                        "title": "Main Campaign",
	                        "text": "<div>Play through the sweeping main campaign of Dragalia Lost.</div><div>As you progress, various game features will be unlocked and other adventurers will join your cause.</div><div>No stamina will be consumed when clearing main campaign quests on Normal difficulty for the first time.</div>"
	                    },
	                    {
	                        "id": "438",
	                        "title": "Required Might",
	                        "text": "<div>The might you'll need to take part in quests.</div>"
	                    },
	                    {
	                        "id": "439",
	                        "title": "Suggested Might",
	                        "text": "<div>The projected might you'll need to clear a quest.</div>"
	                    },
	                    {
	                        "id": "440",
	                        "title": "Difficulty",
	                        "text": "<div>A measure showing the difficulty of a quest.</div>"
	                    },
	                    {
	                        "id": "441",
	                        "title": "Victory Conditions",
	                        "text": "<div>Conditions required to clear a quest.</div>"
	                    },
	                    {
	                        "id": "442",
	                        "title": "Defeat Conditions",
	                        "text": "<div>Conditions that will lead to the quest failing.</div>"
	                    },
	                    {
	                        "id": "443",
	                        "title": "Quest Endeavors",
	                        "text": "<div>Additional conditions for a quest that grant you rewards upon fulfilling them.</div><div><br /></div><div>Every quest has these and they're separate from the regular endeavors.</div>"
	                    },
	                    {
	                        "id": "444",
	                        "title": "First Clear Rewards",
	                        "text": "<div>Rewards that you receive upon clearing a quest for the first time.</div>"
	                    },
	                    {
	                        "id": "445",
	                        "title": "Daily Bonuses",
	                        "text": "<div>For quests where a daily bonus is applied, the daily bonus can only be completed a certain number of times per day. The bonus will be rewarded upon clearing the quest.</div><div><br /></div><div>The number of times the daily bonus can be claimed in a day is reset daily at 07:00.</div>"
	                    },
	                    {
	                        "id": "649",
	                        "title": "Trials of the Mighty Daily Bonuses",
	                        "text": "<div>Any daily bonuses for Trials of the Mighty you don't earn on a given day will be available to earn on a later day.</div><div>Up to three daily bonuses can be stored in this way.</div><br><div>More daily bonuses will become available at 15:00 every day.</div><br><div>If the 7-Day Pack (Double Bonus) is active upon starting a quest, the daily bonus rewards earned by completing that quest will be doubled. However, the rewards for daily bonuses that are stocked while the 7-Day Pack (Double Bonus) is active but not earned until after the active period has elapsed will not be doubled.<br><br>The reward from each daily bonus depends on the boss who was defeated when it is earned. For example, if you stock a daily bonus while Thor's Trial is available, then earn it while Poseidon's Trial is available, you will earn the daily bonus rewards from Poseidon's Trial, not Thor's Trial.</div>"
	                    },
	                    {
	                        "id": "446",
	                        "title": "Weekly Bonuses",
	                        "text": "<div>Quests that have weekly bonuses only provide bonus rewards a fixed number of times per week when they are cleared.</div><br><div>Weekly bonus acquisition numbers are reset weekly on Sunday at 10:00 PM PST (11:00 PM PDT).</div><br><div>When you clear a quest with a weekly bonus, you can select whether you wish to accept the weekly bonus. Also, if the app is closed after clearing the quest but before the results screen displays, you will be able to select whether you wish to accept the weekly bonus on the Home page the next time you start the app.</div><br><div>The bonus rewards you can receive from weekly bonuses are determined when you accept them, so if the bonus rewards are changed via an update before you choose to accept them, then you will receive rewards based on the updated bonus content, not the rewards from when you started the quest.</div><br><div>Bonus rewards received when you accept a weekly bonus will be doubled if a 7-Day Pack (Double Bonus) was active when you started the quest.</div>"
	                    },
	                    {
	                        "id": "447",
	                        "title": "Skip Tickets",
	                        "text": "<div>When you play a quest that you have fulfilled the three endeavors for, you can spend a skip ticket and stamina to jump straight to the result screen.</div><br><div>The number of rewards you receive when clearing quests using skip tickets increases in proportion to the number of skip tickets used.</div><br><div>There are some quests that you cannot use a skip ticket on.</div>"
	                    },
	                    {
	                        "id": "448",
	                        "title": "Drop Rewards",
	                        "text": "<div>Drop rewards are obtained when you defeat enemies, open treasure chests, and smash barrels during quests.</div><br><div>5\u2605 wyrmprints are indicated by a rainbow icon when they drop.</div><div>4\u2605 wyrmprints are indicated by a gold icon when they drop.</div><div>3\u2605 and lower wyrmprints are indicated by a silver icon when they drop.</div>"
	                    },
	                    {
	                        "id": "449",
	                        "title": "The Auto-Repeat Feature",
	                        "text": "<div>The auto-repeat feature allows you to automatically do a quest a set number of times.</div><div>To enable it, you will need to have already completed all three quest endeavors for that quest.</div><br><div>When enabling the auto-repeat feature, you will be able to select how many times to automatically repeat that quest, and whether to allow the use of stamina recovery items in the event that you run out of stamina before the selected number of runs is complete.</div><div>You can also enable and disable this feature during quests.</div><div>There are certain quests in which the auto-repeat feature is not available.</div><br><div>The auto-repeat feature will be automatically disabled if any of the following conditions are met:</div><div>\u30fbYou repeat the quest the number of times that you initially set</div><div>\u30fbYou repeat the quest 99 times</div><div>\u30fbYou tap Stop on the auto-repeat confirmation screen</div><div>\u30fbYou disable the auto-repeat feature during a quest and go on to clear that quest without re-enabling it</div><div>\u30fbYou choose to give up during a quest</div><div>\u30fbYou run out of stamina (and items to restore it, if applicable)</div><div>\u30fbThe date changes, or new data is available</div><br><div>When using the auto-repeat feature, the calculation that determines whether you have enough stamina to start the next quest is made before the Auto-Repeat Confirmation pop-up is displayed. As such, there may be situations where enough stamina is recovered before said pop-up is displayed to start the next quest, but the auto-repeat feature is terminated regardless.</div>"
	                    },
	                    {
	                        "id": "450",
	                        "title": "Rewards When Using the Auto-Repeat Feature",
	                        "text": "<div>After completing all runs of the quest, or choosing to disable the auto-repeat feature, all of the spoils you have obtained will be displayed.</div><div>Even if you close the game during a quest, you will still obtain all the spoils you had obtained up until that point.</div>"
	                    },
	                    {
	                        "id": "451",
	                        "title": "Stamina Consumption When Using the Auto-Repeat Feature",
	                        "text": "<div>Stamina will be consumed every time you clear a quest while the auto-repeat feature is active.</div><div>The amount of stamina that will be consumed upon clearing the quest will be displayed on the initial quest selection screen, and determined at this point in time.</div><div>Even if something happens during a quest that would affect stamina consumption (such as a promotion beginning or ending), the amount of stamina displayed on the initial quest selection screen is the amount that will be consumed.</div><br><div>If you select the \"Repeat until all stamina is consumed\" option, it is possible that your player level increasing while the repeat feature is active or stamina recovering over time may lead to the quest being repeated more times than might be expected based on the amount of stamina you had before enabling the feature.</div><div>In addition, stamina consumption, player EXP increases, and player level increases are all calculated at the end of each individual quest, and so even if a player level increase is shown upon the auto-repeat feature terminating, it is possible that the stamina gained from that increase has already been consumed.</div>"
	                    },
	                    {
	                        "id": "452",
	                        "title": "Reviving",
	                        "text": "<div>In some quests, you will automatically consume one revive and resume battle when the adventurer or adventurers in your control lose all of their HP.</div><div>The number of revives available in each quest will be indicated above every adventurer's portrait during that quest.</div><div>During solo play, the number of hearts above each adventurer's portrait indicates the total number of revives available to you during that quest.</div><div>During co-op play, the number of hearts above each adventurer's portrait indicates the total number of revives available to that specific adventurer during that quest.</div><div>The number of revives available differs by quest, and when all revives have been consumed, you will no longer be able to revive during that quest.</div><div>Even if you choose the \"continue\" option during a quest, revives that have been consumed will not be recovered.</div><br><div>Upon revival, the revived adventurer's HP will only be restored to 30% of their max HP, all buffs will be lost, and their skill gauges will be reduced to zero. However, the dragon gauge's level will be retained.</div>"
	                    },
	                    {
	                        "id": "652",
	                        "title": "Skills and Abilities That Revive Adventurers",
	                        "text": "<div>Some skills and abilities can revive adventurers.</div><div>Abilities that can revive adventurers will activate before the revives provided for a given quest activate.</div><div>Skills that can revive adventurers will only activate before the revives provided for a given quest activate in the event that the relevant skill is used before the revives provided for a given quest activate.</div><div>The revives granted by these skills and abilities will not consume any of the revives provided for a given quest.</div><br><div>If the only revives used during a quest are those provided by these skills and abilities, conditions dependent upon the number of revives used in a quest, such as those for quest endeavors and survival bonuses, will be treated as though no revives have been consumed.</div><br><div>Notes:</div><div>\u30fbThe revives granted by these skills and abilities will not activate in quests where reviving is not permitted.</div><div>\u30fbAbilities that increase the amount of HP an adventurer revives with will also apply to these revives.</div><div>\u30fbThe number of times abilities that can revive adventurers can activate per quest will be reset upon using a continue.</div>"
	                    },
	                    {
	                        "id": "453",
	                        "title": "Reviving in Solo Mode",
	                        "text": "<div>When in solo mode, one revive will be consumed when the HP of all adventurers in the team reaches zero. When this happens, the entire team will be revived.</div>"
	                    },
	                    {
	                        "id": "454",
	                        "title": "Reviving in Co-op",
	                        "text": "<div>Revives in co-op are unique to each player, and not shared between them.</div><div>Each player will be able to individually use the number of revives alloted to a quest.</div><div>If a player is disconnected or chooses to give up on a quest, their adventurer(s) will not revive.</div><br><div>When you begin a quest with one adventurer under your control:</div><div>You will automatically consume one revive when that adventurer's HP reaches zero, and that adventurer will be resurrected.</div><br><div>When you begin a quest with two or more adventurers under your control:</div><div>You will automatically consume a revive for each adventurer under your control when the HP of all adventurers under your control reaches zero.</div><br><div>The number of times each adventurer can revive in a quest will be indicated by the number of hearts above their portrait.</div>"
	                    },
	                    {
	                        "id": "455",
	                        "title": "Survival Bonus",
	                        "text": "<div>In some quests where reviving is possible, you will obtain extra rewards for each revive left unused at the end of the quest.</div><div>The more revives left unused, the better the rewards you will obtain.</div><br><div>In co-op, the number of additional rewards will be based on the number of times that you yourself revived.</div><div>The number of times other players revive will have no impact on the rewards you can obtain.</div><br><div>The Survival Bonus rewards can be viewed on the quest&#39;s Quest Details screen.</div><div>Your reward will be chosen at random from the possible rewards shown on this screen under the Survival Bonus tier that you earned.</div><div>These rewards are not affected by increased drop reward promotions.</div>"
	                    },
	                    {
	                        "id": "478",
	                        "title": "Campaign Unlock Endeavors",
	                        "text": "<div>These are endeavors that must be completed in order to advance the main campaign.</div><div>You can check what these endeavors entail and how many you have yet to complete by tapping the endeavors icon on the home screen, tapping the Normal tab, then looking under the relevant chapter header.</div>"
	                    },
	                    {
	                        "id": "489",
	                        "title": "Retrying a Quest during Solo Play",
	                        "text": "<div>During solo play, you can retry a quest from the beginning by tapping the Retry button in the menu that opens by tapping the button in the top-right corner of the screen.</div><div>Your helper will remain unchanged when using the retry feature.</div><br>"
	                    },
	                    {
	                        "id": "490",
	                        "title": "Retrying a Quest during Co-op Play",
	                        "text": "<div>During co-op play, you can initiate a vote to retry a quest from the beginning by tapping the Retry button in the menu that opens by tapping the button in the top-right corner of the screen.</div><div>It's also possible to initiate a vote to retry a quest when all of the players' adventurers have been defeated and there are no continues available.</div><br><div>Each player can initiate a vote once per quest.</div><div>There is a time limit for casting votes.</div><br><div>In the event that all players vote to retry the quest, the quest will restart from the beginning.</div><br><div>In the event that one or more of the players vote to not retry the quest, the vote will end and the quest will continue as before.</div><div>(If all of the players' adventurers have been defeated, there are no continues available, and one or more of the players vote to not retry the quest, the quest will end and the Friend Info screen will display.)</div><br><div>In the event that one or more of the players give up or are disconnected and all of the remaining players vote to retry, they will return to the co-op room. If, however, one of the remaining players votes to not retry the quest, the quest will continue as before.</div><div>(If the host gives up or is disconnected, the quest will switch over to solo play.)</div>"
	                    },
	                    {
	                        "id": "491",
	                        "title": "Important Information Regarding the Retry Feature",
	                        "text": "<div>Regardless of how many times you retry a quest, when you clear it, only one clear&#39;s worth of stamina or getherwings will be used.</div><div>If you retry a quest, you will lose any EXP, mana, rupies, and items you have earned during the quest you have been playing.</div><div>If you use the continue feature before using the retry feature, any diamantium or wyrmite you used will not be returned to you.</div>"
	                    },
	                    {
	                        "id": "573",
	                        "title": "Solo/Co-op Quests",
	                        "text": "<div>Some quests are split into solo and co-op variations, with different difficulties and rewards for each.</div><br><div>\u25a0Rewards</div><div>A quest&#39;s obtainable rewards are the same for both solo and co-op variations, but the quantity of these rewards is greater in co-op than in solo play.</div><div>Weekly bonus rewards and the number of times they are collected are shared by both solo and co-op.</div><br><div>\u25a0Endeavors</div><div>Endeavors for quests that are split into solo and co-op variations can be completed by clearing these quests in solo play.</div><br><div>\u25a0Unlocking quests</div><div>Quests that are unlocked by clearing certain quests that are split into solo and co-op variations are unlocked by clearing them either in solo or co-op play.</div>"
	                    },
	                    {
	                        "id": "650",
	                        "title": "Suggested Teams",
	                        "text": "<div style=\"\">This feature allows you to check what teams other players have used to clear certain quests.</div><br><div>\u25a0Viewing suggested teams</div><div>Tap the Suggested Teams button at the bottom of the initial quest selection screen for certain quests to display a list of up to 100 different combinations of adventurers that players have used to clear the selected quest.</div><div>Then tap the View/Copy Team Loadouts button beneath any team to display up to 10 detailed team loadouts used to clear the selected quest with those adventurers.</div><br><div>\u25a0Quests with suggested teams</div><div>\u30fbAdvanced Dragon Trials: Standard, Expert, and Master difficulty quests (solo and co-op)</div><div>\u30fbThe Agito Uprising: Standard, Expert, Master, and Legend difficulty quests (solo and co-op)</div><div>\u30fbRise of the Sinister Dominion: Standard, Expert, and Master difficulty quests (solo and co-op)</div><div>\u30fbMorsayati Reckoning (solo only)</div><div>\u30fbPrimal Dragon Trials (solo and co-op)</div><br><div>\u25a0Team loadout details</div><div>The stats displayed for all adventurers, weapons, dragons, wyrmprints, and shared skills in each team loadout reflect the following upgrades:</div><br><div>\u30fbAdventurers: Mana circles fully unbound and max level.</div><div>\u30fbWeapons: Fully upgraded.</div><div>\u30fbDragons: Fully unbound, max level, and maximum bond.</div><div>\u30fbWyrmprints: Fully upgraded.</div><div>\u30fbShared skills: Max level.</div><br><div>Notes:</div><div>\u30fbStat increases from abilities, augments, facilities, and encyclopedia bonuses are not reflected.</div><div>\u30fbThe HP and strength values displayed for portrait wyrmprints may not reflect those of the portrait wyrmprints actually equipped by the indicated team.</div><div>\u30fbTeam loadout information may be reset when quests are adjusted.</div><br><div>\u25a0Copying team loadouts</div><div>For solo quests, you can copy a team loadout to one of your team slots by tapping the Copy button beneath the desired loadout.</div><div>For co-op quests, you can choose to copy an individual player's team loadout by tapping the Copy button beneath that player's adventurer, or you can copy the loadout of the entire co-op team by tapping the Copy Team Loadout button.</div><br><div>Notes:</div><div>\u30fbAny adventurers, weapons, or wyrmprints that are not in your collection, or that you do not have enough copies of, will not be copied.</div><div>\u30fbA Battleworn XX (e.g. Battleworn Sword) of the same weapon type will be equipped in place of any weapons that are not in your collection, or that you do not have enough copies of.</div><div>\u30fbDefault shared skills will be equipped in place of any shared skills that you have not unlocked.</div><div>\u30fbPortrait wyrmprints cannot be copied.</div><div>\u30fbIf you do not have any of the adventurers in the selected loadout, the copied team will instead include only the prince.</div><div>\u30fbWhen copying a team loadout, adventurers, dragons, weapons, and wyrmprints will be copied with your current upgrades, regardless of whether or not these upgrades differ from those displayed in the selected loadout.</div><div style=\"\">\u30fbThe adventurer, dragon, weapon, and wyrmprint stats viewable by tapping Team Information when copying a loadout will reflect your current upgrades.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 3,
	                "title": "Battles",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "339",
	                        "title": "Basic Controls",
	                        "text": "<div>During a quest, swipe the screen to move your adventurer.</div><div><br /></div><div>Tap the screen and the adventurer will attack.</div>"
	                    },
	                    {
	                        "id": "340",
	                        "title": "Changing Controlled Adventurer",
	                        "text": "<div>To change the adventurer you're controlling, tap either an adventurer portrait at the bottom of the quest screen or an adventurer icon at the top left of the screen.</div>"
	                    },
	                    {
	                        "id": "341",
	                        "title": "Minimap",
	                        "text": "<div>Check your adventurers' surroundings using the window at the top right of the quest screen.</div><div><br /></div><div>Tap the window to expand the map into the center of the screen.</div>"
	                    },
	                    {
	                        "id": "342",
	                        "title": "Field Objects",
	                        "text": "<div>Treasure chests and barrels are placed throughout quests. You may be able to acquire items by attacking them.</div>"
	                    },
	                    {
	                        "id": "343",
	                        "title": "Obstacles",
	                        "text": "<div>These snap into action once adventurers get close enough or attack them. You'll find various mechanisms throughout quests, from switches that open doors to traps that repeat an attack loop.</div>"
	                    },
	                    {
	                        "id": "344",
	                        "title": "Enemy Wall",
	                        "text": "<div>Sometimes during quests, a wall will appear to block your path along with enemies. The wall will disappear once you've defeated all the enemies associated with it.</div>"
	                    },
	                    {
	                        "id": "345",
	                        "title": "Force Strikes",
	                        "text": "<div>Tap and hold down on the screen to perform a force strike. This is a special attack that differs between weapon types.</div><br><div>Although force strikes take time to charge up, they have powerful effects that regular attacks do not\u2014such as breaking an enemy's guard or reducing their mode gauge.</div><br><div>Force strikes can be learned by unlocking certain nodes in an adventurer's mana circles.</div><br><div>For some adventurers, damage will sometimes be reduced if their force strike hits multiple times.</div>"
	                    },
	                    {
	                        "id": "346",
	                        "title": "Dodging",
	                        "text": "<div>Adventurers will roll along the ground if you swipe quickly across the screen. This is effective for avoiding enemy attacks.</div><br><div>\u25a0Evasion Abilities</div><div>There are abilities that require you to dodge enemy attacks to activate.</div><div>The following means of evasion count for these abilities:</div><br><div>\u30fbSwiping quickly across the screen</div><div>\u30fbEvasion using specific force strikes</div><div>\u30fbEvasion resulting from the Reflexive Evasion buff</div><br><div>\u203bThe invincibility window provided by using skills does not count as evasion for these abilities.</div>"
	                    },
	                    {
	                        "id": "347",
	                        "title": "Bracing",
	                        "text": "<div>When an attack sends you flying, after you reach a certain height you can brace yourself by tapping or swiping the screen.</div><div>Brace yourself with a tap to land where you are. Swipe to brace yourself and land in the direction you swiped.</div>"
	                    },
	                    {
	                        "id": "348",
	                        "title": "Skills",
	                        "text": "<div>You can activate an adventurer's specific skill by tapping the skill button on the bottom of the quest screen.</div><div>Skills can be used once the skill gauge is full.</div><br><div>While using most skills, adventurers will be immune to damage.</div><div>This does not apply to all skills, and certain types of enemy attacks will bypass this immunity and deal damage normally.</div>"
	                    },
	                    {
	                        "id": "349",
	                        "title": "Skill Gauge",
	                        "text": "<div>This gauge is necessary to perform skills while on quests. It fills as you attack enemies.</div><div>For some skills, the skill gauge will gradually fill automatically over time.</div><div>Abilities and other effects that increase skill gauge fill rate will not affect this automatic increase.</div>"
	                    },
	                    {
	                        "id": "350",
	                        "title": "Shapeshifting",
	                        "text": "<div>This is when an adventurer takes on the form of a dragon. It can be done during quests by expending the dragon gauge. An adventurer must have a dragon equipped in order to shapeshift.</div><div><br /></div><div>Adventurers do not take damage while they are in dragon form and will be able to use dragon-exclusive skills.</div>"
	                    },
	                    {
	                        "id": "351",
	                        "title": "Dragon Gauge",
	                        "text": "<div>This gauge is necessary in order to shapeshift while on quests. It fills up as enemies are defeated or as dragon obelisks found in quests are destroyed.</div><div><br /></div><div>During solo play, the dragon gauge is shared between adventurers. During co-op play, each player has their own.</div><div><br /></div><div>While in dragon form, the gauge will deplete as time passes and as you take damage. The shapeshift is undone once it's empty.</div>"
	                    },
	                    {
	                        "id": "352",
	                        "title": "Dragon Obelisks",
	                        "text": "<div>These dragon-shaped crystals fill the dragon gauge when destroyed.</div><div><br /></div><div>There are two types of dragon obelisks, each of which fills your dragon gauge a different amount.</div>"
	                    },
	                    {
	                        "id": "353",
	                        "title": "Action Marker",
	                        "text": "<div>A marker showing the impact of an attack that appears on the ground when an enemy uses a skill.</div><br><div>Action markers have various shapes, such as circles and crescents, and also function as a timer for when an enemy will attack.</div><br><div>When it comes to attacks that display an action marker, there are those you can avoid by using a skill's invincibility window, and those where you will still take damage. This depends on the action marker's color.</div><br><div>You can avoid taking damage from attacks with red action markers by using the invincibility window from skills, shapeshifting, and dodging.</div><div>Conversely, damage from attacks with purple action markers is generally unavoidable. However, there are exceptions where it is possible to avoid taking damage from these attacks by using the invincibility window from certain skills.</div>"
	                    },
	                    {
	                        "id": "354",
	                        "title": "Classes and Banes",
	                        "text": "<div>Enemies are separated into the following types:</div><div><br /></div><div>\u30fbPhysian</div><div>\u30fbThaumian</div><div>\u30fbDemihuman</div><div>\u30fbTherion</div><div>\u30fbDemon</div><div>\u30fbUndead</div><div>\u30fbDragon</div><div>\u30fbHuman</div><div><br /></div><div>There is a Bane effect that increases the damage dealt to each of these types with the exception of humans. The Bane effect's special hit effect is displayed when it's active.</div>"
	                    },
	                    {
	                        "id": "355",
	                        "title": "Overdrive",
	                        "text": "<div>Continually attacking a boss enemy will cause it to enter a very aggressive overdrive state.</div>"
	                    },
	                    {
	                        "id": "356",
	                        "title": "Break",
	                        "text": "<div>Continuing to attack a boss that's in overdrive will cause it to enter a break state, which will cause it to fall down.</div>"
	                    },
	                    {
	                        "id": "357",
	                        "title": "Barrier",
	                        "text": "<div>Among enemies, there are those who can block attacks using things like shields. You can remove this guard state by using force attacks or attacks with a guard-crush ability.</div>"
	                    },
	                    {
	                        "id": "358",
	                        "title": "Rare Enemies",
	                        "text": "<div>Certain rare enemies may appear during certain quests. These types of enemies flee after a set amount of time. Defeating them may yield rare items.</div><br><div>Their chances of appearing increase during co-op play.</div>"
	                    },
	                    {
	                        "id": "359",
	                        "title": "Menaces",
	                        "text": "<div>Certain enemies that are bigger and stronger than regular enemies may appear in certain quests.</div>"
	                    },
	                    {
	                        "id": "360",
	                        "title": "Buffing and Debuffing",
	                        "text": "<div>Among the various skill effects there exist what are known as &quot;buffs,&quot; which give positive effects to their targets, and &quot;debuffs,&quot; which give negative effects.</div><br><div>These kinds of effects can be stacked. If the same skill effect is applied to a target multiple times, some of its effect is added on top of the original. That said, each status has an upper limit to its effect. Strengthening or weakening beyond that limit is not possible.</div><br><div>When an adventurer&#39;s HP buff reaches the maximum possible amount, any further HP buffs will heal that adventurer instead.</div><div>Debuffs are not guaranteed to be applied.</div><div>*When a skill that applies multiple debuffs is used, each debuff has a separate chance to be applied.</div>"
	                    },
	                    {
	                        "id": "361",
	                        "title": "Auto-Play",
	                        "text": "<div>This function automatically makes your adventurer move, attack and open treasure chests.</div><div>Tap the Auto-Play button during a quest to activate it.</div><br><div>Notes:</div><div>Adventurers moving through auto-play will not break open barrels.</div><div>You can control your adventurer even when auto-play is turned on.</div><div>The function can be turned off by tapping the button again.</div>"
	                    },
	                    {
	                        "id": "362",
	                        "title": "Effective Range of Skills",
	                        "text": "<div>The effective range of skills varies depending on the skill.</div><div>Skills that say \"all teammates\" will only affect the four adventurers in your team.</div><div>Skills that say \"all allies\" will affect all 16 players in a raid battle.</div>"
	                    },
	                    {
	                        "id": "480",
	                        "title": "Stance Icons",
	                        "text": "<div>Some adventurers have multiple stances which can be toggled with icons on the right-hand (or left-hand if your UI layout setting is set to left) side of the screen.</div><div>Switching stances in this way can change the effects of adventurer skills and their standard attack patterns. Sometimes these changes will also require additional conditions to be met (such as reaching a certain combo count).</div>"
	                    },
	                    {
	                        "id": "482",
	                        "title": "Skills that Target Multiple Enemies",
	                        "text": "<div>Certain skills allow adventurers to target and attack multiple enemies.</div><div>These skills will target enemies within a set area starting with the enemy closest to the adventurer and progressing to the next closest enemy until all hits have landed. This selection process is unaffected by the position of the enemy targeted by the player. In the event that the number of enemies within this set area is fewer than the skill's number of hits, this selection process will be repeated for the remaining hits.</div><br>"
	                    },
	                    {
	                        "id": "487",
	                        "title": "Dragondrive",
	                        "text": "<div style=\"\">Certain adventurers have the ability to activate dragondrive instead of shapeshifting. Dragondrive is a special state that consumes an adventurer's dragondrive gauge rather than the dragon gauge, during which the adventurer will be powered up, but will take damage normally. It is possible to activate dragondrive even without a dragon being equipped.</div><div style=\"\"><br></div><div style=\"\">\u25a0Abilities that do not affect the dragondrive</div><div style=\"\">\u30fb Dragon Damage +XX%</div><div style=\"\">\u30fb Dragon's Claws XX</div><div style=\"\">\u30fb Dragon's Skill XX</div><div style=\"\">\u30fb Dragon Time +XX%</div><div style=\"\"><br></div><div style=\"\">\u25a0Facilities that do not affect the dragondrive</div><div style=\"\">\u30fb All Dracoliths</div><div style=\"\">\u30fb All Fafnir Statues</div>"
	                    },
	                    {
	                        "id": "488",
	                        "title": "Dragondrive Gauge",
	                        "text": "<div style=\"\">This gauge is necessary in order to activate dragondrive while on quests. It fills up as enemies are defeated or as dragon obelisks found in quests are destroyed.</div><div style=\"\">It exists independently of the dragon gauge for adventurers that possess one, and certain actions will consume it. While dragondrive is active, the gauge will deplete as time passes, and dragondrive will be deactivated once it is empty.</div><div style=\"\">You can also manually deactivate dragondrive by tapping the dragondrive button while dragondrive is active.</div><div style=\"\"><br></div><div style=\"\">\u25a0Abilities that affect the dragondrive gauge</div><div style=\"\">\u30fb Dragon Haste +XX%</div><div style=\"\">\u30fb Shapeshift Prep +XX%</div><div style=\"\">\u30fb Draconic Charge XX</div>"
	                    },
	                    {
	                        "id": "528",
	                        "title": "Tiki and her Divine Dragon Form",
	                        "text": "<div>The adventurer Tiki has a unique Divine Dragon button and Divine Dragon gauge. By activating her Divine Dragon gauge during quests she is able to transform into her Divine Dragon form, which is different than a standard shapeshift.</div><br><div>Tiki is able to transform into her Divine Dragon form even if she doesn&#39;t have a dragon equipped.</div><br><div>Her Divine Dragon form will be deactivated automatically after a certain amount of time.</div><div>Her Divine Dragon form can also be deactivated by tapping the Divine Dragon button while in Divine Dragon form.</div><div>After deactivation, it won&#39;t be possible for Tiki to transform into her Divine Dragon form again for a short period of time.</div><br><div>Using standard attacks and skills, defeating enemies, and destroying dragon obelisks found in quests will fill the Divine Dragon gauge.</div><br><div>\u25a0Regarding damage taken while in Divine Dragon form</div><div>Tiki will take damage from enemy attacks while in Divine Dragon form, but due to the effect of her Dragon Scion ability, the damage she takes is reduced.</div><div>Tiki is also immune to afflictions while in her Divine Dragon form.</div><div>Some attacks are unaffected by this damage reduction and will deal full damage. Examples include Void Nidhogg&#39;s Dark Detonation and damage traps on quests.</div><br><div>\u25a0Regarding skills and abilities that won&#39;t have any effect while in Divine Dragon form</div><div>When Tiki transforms into her Divine Dragon form, her skills will start fully charged.</div><div>Skill gauges in Divine Dragon form will charge as you damage enemies and can be used as many times as they can be charged.</div><div>However, the rate at which these skills charge is unaffected by skills and abilities that charge skills. For example, the skills and abilities of the dragon Gaibhne &amp; Creidhne and the abilities of the adventurer Marth will not charge Tiki&#39;s Divine Dragon skills.</div><br><div>\u25a0Abilities that affect the Divine Dragon gauge</div><div>\u30fb Dragon Haste +XX%</div><div>\u30fb Shapeshift Prep +XX%</div><div>\u30fb Draconic Charge XX</div><br><div>\u25a0Abilities that do not affect the Divine Dragon form</div><div>\u30fb Dragon Damage +XX%</div><div>\u30fb Dragon&#39;s Claws XX</div><div>\u30fb Dragon&#39;s Scales XX</div><div>\u30fb Dragon&#39;s Skill XX</div><div>\u30fb Dragon Time +XX%</div><br><div>\u25a0Facilities that do not affect the Divine Dragon form</div><div>\u30fb All Dracoliths</div><div>\u30fb All Fafnir Statues</div>"
	                    },
	                    {
	                        "id": "628",
	                        "title": "Persona Summoning",
	                        "text": "<div>The following adventurers have a unique Persona gauge. By activating their Persona gauge during quests, they can summon their Persona, which is different than a standard shapeshift.</div><br><div>\u30fb Joker</div><div>\u30fb Panther</div><div>\u30fb Mona</div><div>\u30fb Sophie</div><br><div>These adventurers can summon their Persona even if they don&#39;t have a dragon equipped.</div><br><div>\u25a0Taking damage</div><div>The above adventurers will receive damage even when their Persona is active, but damage taken will be reduced.</div><div>Some attacks are unaffected by this damage reduction and will deal full damage. Examples include Void Nidhogg&#39;s Dark Detonation and damage traps in quests.</div><br><div>\u25a0Abilities that do not affect Personas</div><div>\u30fb Dragon Damage +XX%</div><div>\u30fb Dragon&#39;s Claws XX</div><div>\u30fb Dragon&#39;s Scales XX</div><div>\u30fb Dragon&#39;s Skill XX</div><div>\u30fb Dragon Time +XX%</div><br><div>\u25a0Facilities that do not affect Personas</div><div>\u30fb All Dracoliths</div><div>\u30fb All Fafnir Statues</div>"
	                    },
	                    {
	                        "id": "663",
	                        "title": "Summoning with the Summon Gauge",
	                        "text": "<div>The following adventurers have a unique summon gauge. By activating their summon gauge during quests, they can summon support, which is different than a standard shapeshift.</div><br><div>\u30fb Gala Zethia</div><br><div>These adventurers can activate their summon gauge even if they don&#39;t have a dragon equipped.</div><br><div>\u25a0Taking damage</div><div>The above adventurers will receive damage even when their summon gauge is activated, but damage taken will be reduced.</div><div>Some attacks are unaffected by this damage reduction and will deal full damage. Examples include Void Nidhogg&#39;s Dark Detonation and damage traps in quests.</div><br><div>\u25a0Abilities that do not affect summoning with the summon gauge</div><div>\u30fb Dragon Damage +XX%</div><div>\u30fb Dragon&#39;s Claws XX</div><div>\u30fb Dragon&#39;s Scales XX</div><div>\u30fb Dragon&#39;s Skill XX</div><div>\u30fb Dragon Time +XX%</div><br><div>\u25a0Facilities that do not affect summoning with the summon gauge</div><div>\u30fb All Dracoliths</div><div>\u30fb All Fafnir Statues</div>"
	                    },
	                    {
	                        "id": "629",
	                        "title": "Persona Gauge",
	                        "text": "<div>This gauge is necessary in order for an adventurer to summon their Persona while on quests. Defeating enemies, destroying dragon obelisks found in quests, and performing certain adventurer-specific actions will fill it. It exists independently of the dragon gauge for adventurers that possess one. While the user's Persona is active, the gauge will deplete as time passes, and the user's Persona will disappear once it is empty. You can also manually deactivate this state by tapping the Persona button while the user's Persona is summoned. Abilities that fill the dragon gauge, such as Dragon Haste, Draconic Charge, and Dragon Prep +XX%, will also fill the Persona gauge.</div>"
	                    },
	                    {
	                        "id": "664",
	                        "title": "Summon Gauge",
	                        "text": "<div>This gauge is necessary in order for an adventurer to summon support while on quests. Defeating enemies, destroying dragon obelisks found in quests, and performing certain adventurer-specific actions will fill it. It exists independently of the dragon gauge for adventurers that possess one. While the user&#39;s summoned support is active, the gauge will deplete as time passes, and the user&#39;s summoned support will disappear once it is empty. You can also manually deactivate this state by tapping the summon button while the user&#39;s summoned support is active. Abilities that fill the dragon gauge, such as Dragon Haste, Draconic Charge, and Dragon Prep +XX%, will also fill the summon gauge.</div>"
	                    },
	                    {
	                        "id": "637",
	                        "title": "Unique Shapeshifts",
	                        "text": "<div>Certain adventurers have unique shapeshifting gauges, and can use these gauges to shapeshift in unique ways.</div><div>These adventurers can use their unique shapeshifts even without a dragon equipped.</div><br><div>These shapeshited forms will be deactivated automatically after the gauge depletes, and can also be manually deactivated by tapping the user's unique shapeshift button while in their shapeshifted form.</div><div>After deactivation, it won't be possible for the user to shapeshift again for a short period of time.</div><br><div>Destroying dragon obelisks found in quests and activating certain abilities will fill these unique shapeshift gauges.</div><br><div>\u25a0Taking damage while in a unique shapeshift form</div><div>Adventurers will still take damage while in their unique shapeshifted form, but that damage will be reduced. Traps within quests, and some attacks are exempt from this (such as Void Nidhogg's Dark Detonation).</div><div>Taking damage will not deplete the shapeshift gauge.</div><div>If an adventurer's HP reaches 0 while in their unique shapeshifted form, they will still be incapacitated.</div><div>They will also be immune to debuffs and afflictions while shapeshifted.</div><br><div>\u25a0Using skills while in a unique shapeshift form</div><div>It is not possible to use weapon skills or shared skills while in a unique shapeshifted form.</div><div>Unlike during normal shapeshifts, standard attacks will fill skill gauges, and skills can be used repeatedly.</div><div>However, skills and abilities that fill skill gauges, such as Gaibhne &amp; Creidhne's skill and one of the adventurer Marth's abilities, will not take effect.</div><br><div>\u25a0Abilities that affect unique shapeshifts</div><div>\u30fbAbilities that affect dragon gauge fill rate, such as Dragon Haste +XX%.</div><br><div>\u25a0Abilities that do not affect unique shapeshifts</div><div>\u30fbAbilities that only grant an effect while shapeshifted, such as Dragon Damage +XX%.</div><div>\u30fbAbilities that are affected by the number of times the user has shapeshifted, such as Dragon's Claws XX.</div><div>\u30fbAbilities that affect how long the user remains in shapeshifted form, such as Dragon Time +XX%.</div><br><div>\u25a0Facilities that do not affect unique shapeshifts</div><div>\u30fbAll Dracoliths</div>"
	                    },
	                    {
	                        "id": "661",
	                        "title": "Dragon Strikes",
	                        "text": "<div>Some dragons are able to perform a special attack called a dragon strike.</div><div>When in dragon form, tap and hold the screen to charge a dragon strike.</div><br><div>You can only use dragon strikes when shapeshifted into a dragon with an ability that enables dragon strikes.</div><div>Dragon strikes cannot be used when using unique replacements for standard shapeshifting, such as the dragondrive.</div><div>Dragon strikes also cannot be used with adventurers that shapeshift into a specific dragon regardless of the dragon they have equipped (unless the specific dragon they always shapeshift into has an ability that enables dragon strikes).</div><br><div>The effects of dragon strikes differ from dragon to dragon.</div><div>Mechanics that affect adventurers&#39; force strikes do not apply to dragon strikes.</div><div>For example, abilities and buffs that increase the damage of force strikes do not apply to dragon strikes.</div><br><div>In addition, the effect of the Dragon&#39;s Fierce Rule ability does not apply to dragon strikes.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 4,
	                "title": "Afflictions",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "234",
	                        "title": "Afflictions",
	                        "text": "<div>These are temporary debilitating states inflicted upon one of your adventurers by skills or traps within a quest.</div><div><br /></div><div>There are various types of afflictions, each one with different effects.</div><div><br /></div><div>An afflicted adventurer cannot shapeshift.</div>"
	                    },
	                    {
	                        "id": "602",
	                        "title": "Enemy Resistances",
	                        "text": "<div>Some enemies are resistant to certain afflictions.</div><div>In addition, if an enemy succumbs to an affliction, its resistance to said affliction will increase.</div><br><div>The color of the RESIST text that appears on-screen when an enemy's resistance has prevented an affliction is based on the following:</div><br><div>\u30fbEnemy resistance is less than 100%: White.</div><div>\u30fbEnemy resistance is 100% or above: Yellow.</div><div>\u30fbEnemy currently has affliction immunity: Red.</div>"
	                    },
	                    {
	                        "id": "235",
	                        "title": "Poison",
	                        "text": "<div>Receive periodic damage for a limited time.</div>"
	                    },
	                    {
	                        "id": "236",
	                        "title": "Stun",
	                        "text": "<div>Become unable to act or move for a limited time.</div><br><div>Stun is removed once the afflicted adventurer is attacked.</div>"
	                    },
	                    {
	                        "id": "237",
	                        "title": "Blindness",
	                        "text": "<div>Attacks will miss enemies at a fixed chance for a limited time.</div>"
	                    },
	                    {
	                        "id": "238",
	                        "title": "Burn",
	                        "text": "<div>Receive periodic damage for a limited time.</div>"
	                    },
	                    {
	                        "id": "239",
	                        "title": "Bog",
	                        "text": "<div>The adventurer&#39;s movement speed is lowered for a limited time, and damage received is increased.</div>"
	                    },
	                    {
	                        "id": "240",
	                        "title": "Paralysis",
	                        "text": "<div>Receive periodic damage for a limited time. This also halts your movement.</div>"
	                    },
	                    {
	                        "id": "241",
	                        "title": "Curse",
	                        "text": "<div>The adventurer cannot use their skill buttons for a limited time.</div>"
	                    },
	                    {
	                        "id": "242",
	                        "title": "Freeze",
	                        "text": "<div>The adventurer can neither act nor move for a limited time. Freeze can be undone via attacks from other party members.</div>"
	                    },
	                    {
	                        "id": "243",
	                        "title": "Sleep",
	                        "text": "<div>Become unable to act or move for a limited time.</div><br><div>After a brief period, sleep is removed once the afflicted adventurer is attacked.</div>"
	                    },
	                    {
	                        "id": "479",
	                        "title": "Frostbite",
	                        "text": "<div>Receive periodic damage for a limited time.</div>"
	                    },
	                    {
	                        "id": "571",
	                        "title": "Flashburn",
	                        "text": "<div>Receive periodic damage for a limited time.</div>"
	                    },
	                    {
	                        "id": "574",
	                        "title": "Shadowblight",
	                        "text": "<div>Receive periodic damage for a limited time.</div>"
	                    },
	                    {
	                        "id": "575",
	                        "title": "Stormlash",
	                        "text": "<div>Receive periodic damage for a limited time.</div>"
	                    },
	                    {
	                        "id": "576",
	                        "title": "Scorchrend",
	                        "text": "<div>Receive periodic damage for a limited time.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 5,
	                "title": "Special Effects",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "692",
	                        "title": "Energy/Energized",
	                        "text": "<div>\"Energy\" is a special kind of buff which upgrades certain skills once enough energy levels have been accumulated.</div><div>Once an adventurer reaches energy level five, they will become \"energized,\" and their next attack skill or recovery skill will be upgraded to deal more damage or recover more health respectively.</div><br><div>\u25a0Applicable Skills</div><div>Being energized only increases the damage of attack skills and recovery potency of recovery skills, and not any other effects (buffs, debuffs, etc.).</div><div>Even if an attack (or recovery) skill also has a buffing effect, the benefits applied by being energized will only apply to the skill's damage (or recovery potency).</div><br><div>\u25a0Energy Level</div><div>Once an adventurer's energy level has been increased to at least one, this will be indicated by a musical note icon at the top of the screen, and their exact energy level will be shown by the number next to this icon.</div><div>For skills such as Xander's, which are boosted by the number of buffs applied to the user, energy counts as one buff no matter how high the user's energy level is increased.</div><br><div>\u25a0Resetting Energy Level</div><div>Using a skill upgraded by being energized resets the user's energy level and ends the energized state.</div><div>Furthermore, becoming afflicted will also have the same effect.</div>"
	                    },
	                    {
	                        "id": "693",
	                        "title": "Skill Shift",
	                        "text": "<div>Skill Shift is a system in which certain skills are upgraded when they connect with a foe.</div><br><br><div>\u25a0About Phases</div><div>When Skill Shift has activated once, the skill is said to be in \"Phase II\". If Skill Shift activates once more, it will then be in \"Phase III\".</div><div>Not all skills have this many phases, however; the number of phases a skill has will depend on the individual skill.</div><br><br><div>\u25a0About Resetting</div><div>Skill Shift resets when you successfully connect during the final phase, returning the skill to its original capabilities.</div><div>Successfully connecting with the skill again after this will activate Skill Shift once more.</div><br><br><div>\u25a0About Mikoto's Stances</div><div>Mikoto's stances\u2014Flare Stance and Ruin Stance\u2014are a special kind of Skill Shift, which has a time limit.</div><div>Unlike regular Skill Shift, his skill is only upgraded for a set period of time.</div><div>Only by meeting the conditions for an additional Skill Shift in the alloted time will the skill be upgraded further.</div>"
	                    },
	                    {
	                        "id": "694",
	                        "title": "Bleeding",
	                        "text": "<div>A debuff that causes periodic damage.</div><div>This effect can stack up to three times,</div><div>increasing damage with each stack.</div>"
	                    },
	                    {
	                        "id": "695",
	                        "title": "Buff Zones",
	                        "text": "<div>Buff zones can be placed on the ground and provide a buff to allies that stand in them.</div><div>Four buff zones can exist simultaneously. If a fifth buff zone is created, the first one that was created will disappear.</div><div>If the visual effects are set to Basic in the graphics settings, buff zones will display as plain green shapes.</div><div>There is a limit to the buff provided by some buff zones.</div><div>The time that a buff zone lasts is not extended by Buff Skill Time +X% abilities.</div>"
	                    },
	                    {
	                        "id": "696",
	                        "title": "Debuff Zones",
	                        "text": "<div>Debuff zones apply a debuff to enemies that stand in them.</div><div>Four debuff zones can exist simultaneously. If a fifth debuff zone is created, the first one that was created will disappear.</div><div>If the visual effects are set to Basic in the graphics settings, debuff zones will display as plain yellow shapes.</div><div>There is a limit to the debuff applied by some debuff zones.</div><div>The duration of debuff zones is not extended by the Debuff Skill Time +XX% ability.</div>"
	                    },
	                    {
	                        "id": "697",
	                        "title": "Primed Abilities",
	                        "text": "<div>These abilities activate when the initial skill (not including dragon skills) for the adventurer you are currently controlling is fully charged.</div><div>Once activated, the buff specified in the ability description is applied to the adventurer you are currently controlling.</div><div>The buff provided by these abilities is not applied to adventurers controlled by other players during co-op play, nor is it extended by Buff Skill Time +X% abilities.</div><div>If an adventurer receives a buff from a Primed ability before the expiration of a buff provided by a previous activation of a Primed ability, the buffs will not overlap. Instead, the buff time will be extended.</div>"
	                    },
	                    {
	                        "id": "699",
	                        "title": "Dispel",
	                        "text": "<div>This effect removes the buff with the longest remaining duration from an enemy.</div><div>If there are multiple buffs with exactly the same remaining duration, the buff that was applied first will be removed.</div><div>If the burning ambition effect has been applied to an enemy, that will be dispelled instead of any buffs.</div>"
	                    },
	                    {
	                        "id": "700",
	                        "title": "Inspiration",
	                        "text": "<div>&quot;Inspiration&quot; is a special kind of buff which upgrades certain skills once enough inspiration levels have been accumulated.</div><div>Once an adventurer reaches inspiration level five, they will become &quot;inspired,&quot; and their next attack skill will deal critical damage.</div><br><div>\u25a0Applicable Skills</div><div>Being inspired only affects attack skills, and not any other kind of skills (buffs, debuffs, etc.).</div><div>Even if an attack skill also has a buffing effect, the benefits applied by being inspired will only apply to the skill&#39;s damage.</div><br><div>\u25a0Inspiration Level</div><div>Once an adventurer&#39;s inspiration level has been increased to at least one, this will be indicated by an icon on-screen, and their exact inspiration level will be shown by the number paired with this icon.</div><br><div>\u25a0Resetting Inspiration Level</div><div>Using a skill upgraded by being inspired resets the user&#39;s inspiration level and ends the inspired state.</div><div>Furthermore, becoming afflicted will also have the same effect.</div>"
	                    },
	                    {
	                        "id": "701",
	                        "title": "Life Shields",
	                        "text": "<div>Life shields are a special kind of shield that protect adventurers from taking damage up to a certain maximum value.</div><div>The amount of damage that the shield can absorb is shown in a special gauge underneath each adventurer&#39;s HP bar, and in numerical form underneath the life shield icon, and these will decrease as the shield absorbs damage.</div><div>If the shield absorbs more damage than it is able to, the shield will break, and the adventurer will take the excess damage.</div><div>Some damage cannot be absorbed by a life shield, such as that inflicted by adventurers on themselves, or damage taken when using skills that consume the user&#39;s HP.</div><div>If a life shield is applied to an adventurer who already has one, the new life shield may restore or increase the existing life shield&#39;s gauge.</div>"
	                    },
	                    {
	                        "id": "702",
	                        "title": "Healing Zones",
	                        "text": "<div>Healing zones are areas of ground that activate when an adventurer whose HP is not full steps inside, and heal all allies upon activation.</div><br><div>Each player can only activate a given healing zone once, but the healing zone will remain visible and usable to players who have not yet stepped inside it.</div><br><div>\u30fbIf the adventurer who steps inside the healing zone has full HP, the zone will remain intact and no one will be healed.</div><div>\u30fbHealing zones can also be activated by AI adventurers.</div><br><div>The potency of healing zones' HP recovery varies based on whether the quest is being played solo or co-op.</div><div>Only one healing zone can be active at any given time. If a second healing zone is placed, the first zone will be removed.</div><div>If visual effects are set to Basic in the graphic settings, healing zones will display as plain blue shapes.</div>"
	                    },
	                    {
	                        "id": "703",
	                        "title": "Overdamage",
	                        "text": "<div>\"Overdamage\" is a special kind of buff that, while active, grants attacks bonus non-elemental damage. This effect will not stack, and, if granted while already active, it will be replaced with the version of the effect that deals the most damage or has the most time remaining.</div><br><div>\u25a0Bonus Damage</div><div>Bonus damage dealt by overdamage is based on the user's strength at the time it is granted. This bonus damage is not affected by buffs, abilities, shapeshifting, or punisher effects, and will never deal critical damage or heal the user.</div>"
	                    },
	                    {
	                        "id": "704",
	                        "title": "Affliction Immunity",
	                        "text": "<div>\"Affliction immunity\" is an effect that prevents the user from being inflicted with any afflictions. This effect will prevent afflictions even if the user's resistance is reduced while it is active.</div>"
	                    },
	                    {
	                        "id": "705",
	                        "title": "Sigils",
	                        "text": "<div>Sigils are a special kind of debuff that certain adventurers inflict upon themselves.</div><br><div>Once this debuff has been removed, that adventurer will enter a &quot;sigil released&quot; state, and will be granted various bonuses.</div><div>Which bonuses the adventurer will receive will depend on their individual abilities.</div><br><div>\u25a0Releasing Sigils</div><div>Shapeshifting or becoming incapacitated during battle will not remove the sigil debuff, but certain actions (listed in the adventurer&#39;s abilities) can decrease the time it lasts.</div><br><div>In Rise of the Sinister Dominion quests, when an adventurer who inflicts the sigil debuff on themselves is summoned to fight through a team switch, that adventurer will begin the fight in their &quot;sigil released&quot; state.</div><div>If they are in the first team that fights when the quest begins, however, the sigil debuff will be present.</div>"
	                    },
	                    {
	                        "id": "706",
	                        "title": "Reflexive Evasion",
	                        "text": "<div>Reflexive Evasion is a unique buff that can nullify damage taken from enemy attacks.</div><br><div>This buff does not stack, and when multiple Reflexive Evasion buffs are applied, only the buff with the most activations remaining will take effect.</div><br><div>\u25a0Conditions for Nullifying Damage</div><div>As long as the user has at least one Reflexive Evasion activation remaining, any damage that meets the following conditions will be nullified:</div><br><div>\u30fbThe adventurer is in a state where they could swipe to dodge.</div><div>\u30fbThe attack is one that could be avoided using the invincibility window provided by skills.</div><br><div>If both conditions are not met, damage will be taken as normal, and the number of Reflexive Evasion activations remaining will not decrease.</div><br><div>If damage is avoided using other means (such as swiping across the screen or using specific force strikes) the Reflexive Evasion buff will not activate, and its number of remaining activations will not decrease.</div><br><div>When damage is nullified with Reflexive Evasion, the text DODGE will appear on the screen, and one activation of the buff will be consumed.</div>"
	                    },
	                    {
	                        "id": "707",
	                        "title": "Buffs and Debuffs with Levels",
	                        "text": "<div>Some buffs and debuffs have levels. The maximum level varies for each buff and debuff.</div><br><div>Using a buff or debuff that has multiple levels while that buff or debuff is already active and before its level has reached maximum will increase the level of the buff or debuff, changing its effects.</div><div>If the buff or debuff has already reached maximum level, the duration will be reset, but the level will remain unchanged.</div><br><div>If the duration of a buff or debuff that has multiple levels runs out, its level will decrease and its effects will change.</div><div>If the buff or debuff was only at level one, it will instead be removed entirely.</div>"
	                    },
	                    {
	                        "id": "708",
	                        "title": "Invulnerability",
	                        "text": "<div>Enemies protected by Invulnerability are immune to debuffs, afflictions, damage, and dispel effects.</div>"
	                    },
	                    {
	                        "id": "709",
	                        "title": "Immutable Nature",
	                        "text": "<div>This is a buff only used by enemies, which renders targets fully immune to all afflictions. It can be dispelled, or will disappear when its duration expires.</div>"
	                    },
	                    {
	                        "id": "710",
	                        "title": "Knockback Immunity",
	                        "text": "<div>When an adventurer has knockback immunity, enemy attacks will no longer cause them to flinch.</div><div>This effect does not prevent them from being sent flying.</div>"
	                    },
	                    {
	                        "id": "711",
	                        "title": "Amps",
	                        "text": "<div>Amps are special effects that temporarily power up the user. They can be granted by skills and abilities.</div><div>\u25a0Amp LevelsIf an adventurer is granted an amp when the same kind of amp is already active on that adventurer, that amp&#39;s level will increase.When an amp&#39;s level is increased, its effect will be extended and become more potent.When an amp&#39;s remaining time runs out, the amp will be removed.The maximum level of each amp is level two.If an adventurer is granted an amp when they already have that amp at maximum level, the amp will be replaced by a team amp.\u203bAmps are not affected by Curse of Nihility.</div><div>\u25a0Team AmpsIf an adventurer is granted a team amp when the same kind of team amp is already active on that adventurer, that team amp&#39;s level will increase.When a team amp&#39;s level is increased, its effect on the entire team will be extended and become more potent.When that team amp is already at maximum level, the effect will only be extended.When a team amp&#39;s remaining time runs out, the team amp will be removed.\u203bTeam amps are not affected by Curse of Nihility.</div><div>\u25a0Team Amp Maximum LevelsThe maximum level of team amps is specific to each adventurer.Team amps can only exceed their maximum level when a different adventurer has already activated a different team amp with a higher maximum level.</div><div>Examples:\u30fbIf an adventurer with a maximum team amp level of two activates team amp A when the same team amp is inactive or already active at level one, team amp A&#39;s level will be increased, and its duration extended.\u30fbIf an adventurer with a maximum team amp level of two activates team amp A when the same team amp is already active and at level two, and no other team amps are active, team amp A&#39;s level will remain the same, but its duration will be extended.\u30fbIf an adventurer with a maximum team amp level of two activates team amp A when the same team amp is already active and at level two, and another adventurer in the team with a maximum team amp level of three has already activated their team amp and it is still active, team amp A&#39;s level will be increased, and its duration will be extended.\u30fbIf an adventurer with a maximum team amp level of two activates team amp A when the same team amp is already active and at level three, team amp A&#39;s duration will be only slightly extended.</div>"
	                    },
	                    {
	                        "id": "712",
	                        "title": "Amp Types and Effects",
	                        "text": "<div>Listed below are the different types of amps and team amps, along with their effects.</div><br><div>\u25a0Strength</div><div>\u30fbLv. 1 Strength Amp</div><div>Increases the user's strength by 3% for 60 seconds.</div><br><div>\u30fbLv. 2 Strength Amp</div><div>Increases the user's strength by 5% for 60 seconds.</div><br><div>\u30fbLv. 1 Team Strength Amp</div><div>Increases the entire team's strength by 20% for 30 seconds.</div><br><div>\u30fbLv. 2 Team Strength Amp</div><div>Increases the entire team's strength by 40% for 30 seconds.</div><br><div>\u30fbLv. 3 Team Strength Amp</div><div>Increases the entire team's strength by 60% for 60 seconds.</div><br><div>\u25a0Defense</div><div>\u30fbLv. 1 Defense Amp</div><div>Increases the user's defense by 10% for 60 seconds.</div><br><div>\u30fbLv. 2 Defense Amp</div><div>Increases the user's defense by 15% for 60 seconds.</div><br><div>\u30fbLv. 1 Team Defense Amp</div><div>Increases the entire team's defense by 30% for 30 seconds.</div><br><div>\u30fbLv. 2 Team Defense Amp</div><div>Increases the entire team's defense by 60% for 30 seconds.</div><br><div>\u30fbLv. 3 Team Defense Amp</div><div>Increases the entire team's defense by 90% for 60 seconds.</div><br><div>\u25a0Critical Damage</div><div>\u30fbLv. 1 Critical Damage Amp</div><div>Adds 3% to the modifier applied to the user's critical damage for 60 seconds.</div><br><div>\u30fbLv. 2 Critical Damage Amp</div><div>Adds 5% to the modifier applied to the user's critical damage for 60 seconds.</div><br><div>\u30fbLv. 1 Team Critical Damage Amp</div><div>Adds 20% to the modifier applied to the entire team's critical damage for 30 seconds.</div><br><div>\u30fbLv. 2 Team Critical Damage Amp</div><div>Adds 40% to the modifier applied to the entire team's critical damage for 30 seconds.</div><br><div>\u30fbLv. 3 Team Critical Damage Amp</div><div>Adds 60% to the modifier applied to the entire team's critical damage for 60 seconds.</div>"
	                    },
	                    {
	                        "id": "713",
	                        "title": "Adaptive Suppression",
	                        "text": "<div>When an enemy inflicted with the Adaptive Suppression debuff attacks, they will deal reduced damage so long as the attack has no elemental attunement or has an elemental disadvantage against the target.</div>"
	                    },
	                    {
	                        "id": "714",
	                        "title": "Damage Diffusion",
	                        "text": "<div>Damage Diffusion is a unique buff effect that, when the user takes 2 or more damage from an attack, reduces damage taken by the user by 50%, then spreads out the remaining 50% equally among the rest of the user's team.</div><br><div>Damage Diffusion will not be activated if the user has no active teammates or if an enemy's attack deals 1 or less damage. Also, certain types of damage, such as damage dealt by afflictions, will not activate Damage Diffusion.</div><br><div>Note: If Damage Diffusion is not activated, the buff that grants it will not be consumed.</div><br><div>Damage dealt to the user's teammates by this effect cannot be reduced and is not blocked by life shields or one-use shields that nullify up to a certain amount of damage.</div><div>In addition, if the damage dealt by this effect is greater than the damaged adventurer's remaining HP, that adventurer will be incapacitated.</div>"
	                    },
	                    {
	                        "id": "715",
	                        "title": "Burst Gambits",
	                        "text": "<div>&quot;Burst gambits&quot; are a unique type of debuff with a counter that is reduced by one for every affliction or debuff applied to the affected target.</div><div>When a burst gambit&#39;s counter reaches zero, it will activate that burst gambit&#39;s specific effect (e.g. deal damage to enemies, restore HP to the entire team, etc.) and be consumed.</div><br><div>Notes:</div><div>\u30fb A burst gambit&#39;s counter is only reduced if an affliction or debuff is actually applied. For example, if an adventurer uses an attack that would apply an affliction or debuff, but that affliction or debuff is not applied for some reason (e.g. the target has a high resistance to that affliction, that debuff has a low chance of being applied, etc.), the counter will not be reduced.</div><div>\u30fb Burst gambits are not removed automatically over time.</div><div>\u30fb A burst gambit&#39;s effects will not activate if forcibly removed by an enemy action.</div><div>\u30fb Debuffs with multiple effects will still only reduce the counter by one.</div><div>\u30fb Being energized or inspired will not impact any burst gambit effects.</div><div>\u30fb The amount of damage dealt by a burst gambit that deals damage is based on the stats of the unit who applied it when the gambit was applied. However, the amount of HP restored by a burst gambit that restores HP is based on the stats of the unit who applied it when the gambit&#39;s counter reaches zero.</div><br><div>After the effects of a burst gambit applied to a target activate, burst gambits cannot be applied to that target for a set amount of time. Also, if a burst gambit is applied to a target that already has an active burst gambit, instead of stacking or being overwritten, the active burst gambit&#39;s counter will be reduced by one.</div><br><div>After reducing the burst gambit counter of a target with a debuff, the same adventurer cannot reduce that counter again with the same debuff via the same skill or effect for a set amount of time.</div><br><div>Note: Reducing burst gambit counters with afflictions or by applying additional burst gambits is not affected by this cooldown.</div><br><div>During raid battles:</div><div>\u30fb The counters for burst gambits applied by adventurers from one team cannot be reduced by adventurers from other teams.</div><div>\u30fb Burst gambits applied by adventurers from different teams can stack, but the icons for burst gambits applied by teams other than your own will not be visible.</div><br><div>Burst gambits cannot be applied to enemies who are defeated by dealing a certain number of hits instead of depleting their HP.</div><div>In addition, the text RESIST will appear on the screen in green when attempting and failing to apply a burst gambit to enemies to whom burst gambits cannot be applied, such as those immune to debuffs.</div><br><div>Also, the burst gambit counter may not appear for certain enemies with special ability icons or other unique icons displayed with higher priority.</div>"
	                    },
	                    {
	                        "id": "716",
	                        "title": "Soul Charge",
	                        "text": "<div>When an adventurer is granted the \"Soul Charge\" effect, their HP is completely restored, and their HP remains full for the duration of the effect.</div><div>Soul Charge grants the user immunity to damage dealt over time by skills, buffs, debuffs, and afflictions, and it nullifies damage dealt by enemy attacks. However, when Soul Charge nullifies damage from an enemy attack that would deal damage greater than or equal to 20% of the user's maximum HP, Soul Charge's level is decreased by one.</div><div>Damage from some attacks cannot be nullified by Soul Charge.</div><div>If Soul Charge's level is decreased when already at level one, the effect is removed entirely, and the user's HP is reduced to zero.</div><div>Soul Charge will automatically level up by one for every 15 seconds that pass from the last time its level has decreased, up to level three.</div>"
	                    },
	                    {
	                        "id": "717",
	                        "title": "Power of Bonds",
	                        "text": "<div>If an adventurer has the \"Power of Bonds\" effect, when the user would take damage greater than or equal to their remaining HP, that damage is nullified, the effect is consumed, and damage is instead dealt to the rest of the user's team. This damage equals 20% of each teammate's maximum HP.</div><br><div>This damage nullification will still activate even if the user has no active teammates.</div><div>Damage dealt to the user's teammates by this effect cannot be reduced and is not blocked by life shields or one-use shields that nullify up to a certain amount of damage.</div><div>In addition, damage dealt by this effect cannot reduce an adventurer's HP below 1.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 6,
	                "title": "Events",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "332",
	                        "title": "Special Events",
	                        "text": "<div>These events are open for just a limited period of time.</div>"
	                    },
	                    {
	                        "id": "333",
	                        "title": "Recurring Events",
	                        "text": "<div>These are events that are held every week.</div><div><br /></div><div>You can acquire wyrmprints and resources by taking part in Path to Power or the ruins quests that change daily.</div>"
	                    },
	                    {
	                        "id": "334",
	                        "title": "Challenge Events",
	                        "text": "<div>These are high-difficulty events that are unlocked by progressing through the main campaign.</div>"
	                    },
	                    {
	                        "id": "335",
	                        "title": "Dragon Trials",
	                        "text": "<div>These are challenge events where you have direct showdowns against dragons from the story. The number of dragons you can challenge increases as you progress in the main story.</div><div><br /></div><div>Rewards received in Dragon Trials can be exchanged for dragons in the Treasure Trade.</div>"
	                    },
	                    {
	                        "id": "336",
	                        "title": "The Imperial Onslaught",
	                        "text": "<div>This is a challenge event where you face off against the Dyrenell Empire.</div><br><div>Rewards earned in The Imperial Onslaught can be exchanged for wyrmprints at the Treasure Trade.</div>"
	                    },
	                    {
	                        "id": "337",
	                        "title": "Advanced Dragon Trials",
	                        "text": "<div>A challenge event where dragons you fought in Dragon Trials show their true power, facing off with you as even stronger enemies.</div><div><br /></div><div>Rewards earned in Advanced Dragon Trials can be exchanged for facilities and dragons at the Treasure Trade.</div>"
	                    },
	                    {
	                        "id": "338",
	                        "title": "Astral Raids",
	                        "text": "<div>Astral Raids are co-op quests only available during set periods, which can be challenged alongside up to three other parties.</div><br><div>Challenging Astral Raids requires astral pieces.</div><br><div>Astral pieces can be obtained from quests during the periods Astral Raids aren&#39;t available.</div>"
	                    },
	                    {
	                        "id": "424",
	                        "title": "The Agito Uprising",
	                        "text": "<div>A series of challenging battles that pit you against a group of powerful opponents.</div><div>Materials gathered from Agito Uprising quests can be traded for facilities in the Treasure Trade, or used to craft and upgrade weapons.</div>"
	                    },
	                    {
	                        "id": "634",
	                        "title": "Rise of the Sinister Dominion",
	                        "text": "<div>Rise of the Sinister Dominion is a challenge event where you can obtain wyrmprints that can only be equipped in specific slots, and the materials to upgrade them.</div><br><div>Adventurers will not gain adventurer EXP in quests with a team change.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 21,
	                "title": "Void Battles",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "250",
	                        "title": "What are Void Battles?",
	                        "text": "<div>Void battles are event quests that pit you against enemies with unique abilities that yield special rewards.</div><br><div>\u25a0Unlock conditions for void battles</div><div>Void battles are unlocked by clearing Chapter 7 of the main campaign on Normal difficulty.</div>"
	                    },
	                    {
	                        "id": "251",
	                        "title": "Void Battle Schedule",
	                        "text": "<div>Some void battles are only available on certain days. To view the schedule, tap the Schedule button on the banner at the top of the main void battles screen.</div>"
	                    },
	                    {
	                        "id": "252",
	                        "title": "Void Battle Rewards",
	                        "text": "<div>The unique materials obtained from void battles can be exchanged at the Treasure Trade for items, weapons, dragons, facilities, and more.</div><br><div>To see what&#39;s available, check out the Treasure Trade section of the shop, accessible via the Home screen.</div>"
	                    },
	                    {
	                        "id": "253",
	                        "title": "Unique Abilities",
	                        "text": "<div>Some enemies in void battles come equipped with unique abilities.</div><div>These abilities can be viewed by tapping the Details button on the banner above a selected battle's quest list.</div>"
	                    },
	                    {
	                        "id": "254",
	                        "title": "Stamina and Getherwing Consumption",
	                        "text": "<div>Taking on void battles during solo play will consume stamina. The amount consumed will change depending on the quest. (Stamina is not consumed when you give up or fail to clear a quest.)</div><br><div>Taking on void battles during co-op play will consume getherwings. The amount consumed will change depending on the quest. (Getherwings are not consumed when you give up or fail to clear a quest.)</div>"
	                    }
	                ]
	            },
	            {
	                "id": 32,
	                "title": "Trials of the Mighty",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "647",
	                        "title": "What is Trials of the Mighty?",
	                        "text": "<div>These are event quests that pit you against powerful foes, from which you can acquire special items used to upgrade certain adventurers.</div><br><div>\u25a0Unlock condition for Trials of the Mighty</div><div>Trials of the Mighty is unlocked by clearing Chapter 10 of the main campaign on Normal difficulty.</div>"
	                    },
	                    {
	                        "id": "648",
	                        "title": "Element and Weapon Requirements",
	                        "text": "<div>These quests will require you use only adventurers of specific elements and weapon types, so you will need to form teams that take this into account.</div><div>The required elements and weapon types will change after each event period ends.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 7,
	                "title": "Raid Events",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "504",
	                        "title": "Raid Events",
	                        "text": "<div>A limited time event comprised of story quests and raid battles.</div><div><br /></div><div>The event sees you challenging a raid boss with up to four players, commanding a maximum of sixteen adventurers.</div>"
	                    },
	                    {
	                        "id": "505",
	                        "title": "Emblems",
	                        "text": "<div>Event items used exclusively for raid events. You have a certain chance to receive these when clearing an event quest. You can acquire rewards based on the number of emblems you've acquired.</div><div><br /></div><div>Emblems are reset for each event.</div>"
	                    },
	                    {
	                        "id": "506",
	                        "title": "Otherworld Fragments",
	                        "text": "<div>Event items used exclusively in raid events. You have a chance to receive them when clearing certain event quests. These are used to take part in raid battles and are reset for each event.</div>"
	                    },
	                    {
	                        "id": "507",
	                        "title": "Blazons",
	                        "text": "<div>These are event items used exclusively in raid events. You have a chance to receive these when clearing event quests. They&#39;re used to perform blazon summons.</div><br><div>Blazons are reset for each event.</div>"
	                    },
	                    {
	                        "id": "508",
	                        "title": "Blazon Summoning",
	                        "text": "<div>A summoning specific to raid events that you can perform using Blazons.</div><div><br /></div><div>You can summon adventurers and upgrade materials available for a limited time.</div><div><br /></div><div>The lineup changes between events.</div>"
	                    },
	                    {
	                        "id": "509",
	                        "title": "XX's Conviction",
	                        "text": "<div>These items are obtainable primarily from blazon rewards.</div><div>During raid events with event-exclusive adventurers, mana nodes for these adventurers can only be unlocked using the appropriate XX's Conviction item. However, once the event has ended and after you have used all of the XX's Conviction that you obtained, you will be able to unlock their mana nodes using the standard materials and mana.</div>"
	                    },
	                    {
	                        "id": "510",
	                        "title": "Raid Battles",
	                        "text": "<div>Event quests specific to raid events.</div><div><br /></div><div>These are quests where you fight a colossal enemy that you can only challenge in events while playing co-op, with up to four players and a total of sixteen adventurers.</div>"
	                    },
	                    {
	                        "id": "511",
	                        "title": "HP Gauges for Boss Parts",
	                        "text": "<div>If you tap the HP gauge for a part of a raid boss, a \u25b2 will display under that gauge.</div><div>This is to communicate to other players which part you want to focus damage on,</div><div>and has no bearing on the AI adventurers' actions.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 8,
	                "title": "Facility Events",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "392",
	                        "title": "Facility Events",
	                        "text": "<div>A limited-time event where you can acquire and upgrade facilities that appear only in certain events.</div><div><br /></div><div>You can play story quests and special boss battles that are limited to these events.</div>"
	                    },
	                    {
	                        "id": "394",
	                        "title": "Challenge Battles",
	                        "text": "<div>Event quests specific to facility events.</div><br><div>The goal is to defeat the enemies of each wave, and then defeat all of the enemies in the final wave.</div><br><div>When playing expert and master difficulty challenge battles, there is a reward for clearing each wave. You can obtain the rewards for waves you've cleared even if you get a game over.</div><br><div>*However, unless you clear the final wave, the conditions will not be met for some quest endeavors and conditional bonuses, including the quest endeavors \"Don't allow any of your team to fall in battle,\" \"Allow no more than 2 of your team to fall in battle,\" and \"Don't use any continues,\" along with the conditional bonus \"Don't allow any of your team to fall in battle.\"</div><br><div>When playing a nightmare difficulty challenge battle, you must clear the final wave for the quest to count as cleared. You will not obtain any rewards if you get a game over, even if you cleared one or more waves.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 25,
	                "title": "Event Compendium",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "484",
	                        "title": "What is the Event Compendium?",
	                        "text": "<div>The Event Compendium is a feature that allows you to play certain events that were previously only available for a limited time.</div><div>You can only activate one event at any given time, but you are free to switch between events whenever you like.</div><br><div>\u25a0 Downloading Data</div><div>When selecting a new event to activate in your Event Compendium, it will be necessary to download additional data.</div><div>If you had previously selected another event, that event's data will also be deleted. Your progress in that event, and the status of all related endeavors, will be retained so you may resume at a later date if you wish.</div><br><div>\u25a0 Quest Changes</div><div>The contents of an event added to the Event Compendium may be slightly different to when the event was previously accessible. For example, certain quests may not be available, and changes may be made to drop rewards.</div><br><div>\u25a0 Treasure Trade</div><div>Event items that are obtainable from facility events in the Event Compendium can be exchanged for various rewards. The rewards on offer will not necessarily be the same as those available when the event was previously run.</div><br><div>\u25a0 Endeavors</div><div>Endeavors for your active Event Compendium event will be added to the Normal tab of the endeavor list. Events in the Event Compendium do not have limited or daily endeavors, and the endeavors will not necessarily be the same as those available when the event was previously run.</div><br><div>\u25a0 Event Items</div><div>If you have any facility-upgrade event items remaining from when the events in the Event Compendium were previously run as limited-time events, these will be carried over for the same event in the Event Compendium.</div><br><div>In raid events in the Event Compendium, boss drops have been adjusted, and blazon and emblem rewards will not be available.</div><br><div>\u25a0Befriending Adventurers</div><div>By clearing quests in raid events in the Event Compendium, it will be possible to befriend that event's exclusive adventurer.</div><div>If you participated in the event when it was previously available but did not forge a friendship with that adventurer, it will be treated as if they never joined your team. If you befriended the exclusive adventurer when the event was previously available, they will not join your team again.</div><br><div>In addition, when event-exclusive adventurers join your team through the Event Compendium, they will not have any event-exclusive abilities, and you will not be able to obtain conviction items used to unlock their mana nodes.</div>"
	                    },
	                    {
	                        "id": "485",
	                        "title": "Unlocking the Event Compendium",
	                        "text": "<div>Clear \"The Sylvan Archer\" (2-1) in Chapter 2 of the main campaign to unlock the Event Compendium.</div><div>Some events in the Event Compendium may have additional unlock conditions.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 26,
	                "title": "Onslaught Events",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "513",
	                        "title": "Onslaught Events",
	                        "text": "<div>Onslaught events are limited-time events where you must defend territory from waves of encroaching enemies.</div><div>They also include unique boss battles that are specific to this event type.</div><br><div>\u25a0Unlock conditions for onslaught events</div><div>Onslaught events are unlocked by clearing Chapter 2 (2-1) of the main campaign on Normal difficulty.</div>"
	                    },
	                    {
	                        "id": "514",
	                        "title": "Unlocking Quests and Quest Difficulties",
	                        "text": "<div>Onslaught events have multiple quests for each difficulty (beginner, standard, expert, and master).</div><div>At the start of an onslaught event, only one beginner quest will be unlocked.</div><br><div>More quests can be unlocked using items that are unique to the event.</div><br><div>After clearing all of the quests for a difficulty, you will receive a Victory Reward and the next difficulty will be unlocked.</div>"
	                    },
	                    {
	                        "id": "515",
	                        "title": "Glory",
	                        "text": "<div>You can obtain glory by clearing quests in onslaught events and doing so will earn you various rewards.</div><div>Among these rewards are event-specific items that can be used to unlock new stories and quests during onslaught events.</div>"
	                    },
	                    {
	                        "id": "516",
	                        "title": "Event-Specific Items",
	                        "text": "<div>You can use the following event-specific items, earned by obtaining glory, to unlock quests and stories during onslaught events.</div><div>These event-specific items will reset each time there is a new onslaught event.</div><br><div>\u25a0Battle chart</div><div>This item is used to unlock quests.</div><br><div>\u25a0Stratagem</div><div>This item is used to unlock EX quests.</div><br><div>\u25a0War chronicle</div><div>This item is used to unlock stories.</div>"
	                    },
	                    {
	                        "id": "517",
	                        "title": "Treasure Trade",
	                        "text": "<div>Primal crystals are event-specific items earned during onslaught events that can be exchanged at the treasure trade for various rewards.</div><div>Please keep in mind that event-specific items will reset each time there is a new onslaught event.</div>"
	                    },
	                    {
	                        "id": "518",
	                        "title": "Dragon Battles",
	                        "text": "<div style=\"\">Dragon battles are solo quests unique to onslaught events where you remain shapeshifted for the entire duration of the quest.</div><div>Some dragon battles involve defeating a single boss, while others require you to defeat multiple waves of enemies.</div><br><div>\u25a0Shapeshifting</div><div>The adventurer that you are controlling will automatically shapeshift at the start of the quest and their shapeshift will have an unlimited duration.</div><br><div>\u25a0Conditions for victory</div><div>For dragon battles that involve defeating a single boss, you must defeat the boss for the quest to count as cleared.</div><div>For dragon battles that involve defeating waves of enemies, you must clear the final wave for the quest to count as cleared.</div><br><div>\u25a0Conditions for defeat</div><div>Unlike standard shapeshifting, you will take damage from enemy attacks.</div><div>You will fail the quest if the HP for all of the adventurers in your team reaches zero.</div><div style=\"\"><br></div><div style=\"\">Note: When shapeshifted as Gala Chronos Nyx, using standard attacks, dragon strikes, skills, and the automatic dodge effect granted by his ability will consume the shapeshifted adventurer's HP.</div><div style=\"\"><br></div><div>\u25a0Skills</div><div>Unlike in standard shapeshifting, attacking enemies will charge your skill gauge and you will be able to use skills as many times as your skill gauge fills.</div><br><div>\u25a0Adventurers that cannot participate</div><div>Adventurers that have a dragondrive are unable to participate in dragon battles, even if they have a dragon equipped.</div><div>Meanwhile, while Tiki functions differently than other adventurers, she is a dragon, so she can naturally take part.</div>"
	                    },
	                    {
	                        "id": "519",
	                        "title": "Types of Dragon Battles",
	                        "text": "<div>Some dragon battles are limited to a single adventurer while others require four adventurers to participate. The rules vary slightly in both cases.</div><br><div>\u25a0Participating adventurers</div><div>Adventurers participating in dragon battles must be eligible and have a dragon equipped.</div><div>The team creation for dragon battles limited to a single adventurer is separate from your normal teams and is unique to these quests.</div><br><div>The team creation for dragon battles that require four adventurers uses your normal teams and all eligible adventurers can participate.</div><br><div>\u25a0Switching adventurers</div><div>During dragon battles that require four adventurers, the adventurer you are controlling will automatically switch at the beginning of each wave.</div><div>Only on the final wave of these quests will you be able to freely switch the adventurer that you are controlling.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 27,
	                "title": "Defensive Events",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "520",
	                        "title": "Defensive Events",
	                        "text": "<div>Defensive events are limited-time events containing quests where you must defend a gate from waves of encroaching enemies.</div><br><div>\u25a0Unlock conditions for defensive events<br>Defensive events are unlocked by clearing Chapter 2 (2-1) of the main campaign on Normal difficulty.</div>"
	                    },
	                    {
	                        "id": "521",
	                        "title": "Unlocking Quests and Quest Difficulties",
	                        "text": "<div>Defensive events have multiple quests for each difficulty (beginner, standard, expert, and master).</div><div>At the start of a defensive event, only one beginner quest will be unlocked.</div><br><div>More quests can be unlocked using items that are unique to the event.</div><br><div>After clearing all of the quests for a difficulty, you will receive a Victory Reward and the next difficulty will be unlocked.</div>"
	                    },
	                    {
	                        "id": "522",
	                        "title": "Quest Types and Clear Conditions",
	                        "text": "<div>Defensive Events feature three kinds of quests: skirmishes, local conflicts, and defensive battles. Each can be challenged on various difficulties.</div><br><div>\u25a0 Skirmishes and Local Conflicts</div><div>In these quests, you simply have to defeat several waves of enemies.</div><div>There is no gate to defend.</div><br><div>Clearing the last wave in the alloted time will result in victory, but failing to do so will result in defeat.</div><br><div>\u25a0 Defensive Battles</div><div>Defensive Battles are special quests where you are tasked with defending a gate from oncoming enemies.</div><br><div>You can clear defensive battles by simply preventing the gate from being destroyed or by losing to the boss, but by defeating the quest's boss, you will earn additional rewards.</div><div>If the gate's HP reaches zero or you are defeated before reaching the boss area, however, the quest will end in defeat.</div>"
	                    },
	                    {
	                        "id": "523",
	                        "title": "Glory",
	                        "text": "<div>You can obtain glory by clearing quests in defensive events and doing so will earn you various rewards.</div><div>Among these rewards are event-specific items that can be used to unlock new stories and quests during defensive events.</div>"
	                    },
	                    {
	                        "id": "524",
	                        "title": "Event-Specific Items",
	                        "text": "<div>You can use the following event-specific items, earned by obtaining glory, to unlock quests and stories during defensive events.</div><div>These event-specific items will reset each time there is a new defensive event.</div><br><div>\u25a0Battle chart</div><div>This item is used to unlock quests.</div><br><div>\u25a0Stratagem</div><div>This item is used to challenge EX quests.</div><br><div>\u25a0War chronicle</div><div>This item is used to unlock stories.</div>"
	                    },
	                    {
	                        "id": "525",
	                        "title": "Treasure Trade",
	                        "text": "<div>Primal crystals are event-specific items earned during defensive events that can be exchanged at the treasure trade for various rewards.</div><div>Please keep in mind that event-specific items will reset each time there is a new defensive event.</div>"
	                    },
	                    {
	                        "id": "526",
	                        "title": "Defensive Battles",
	                        "text": "<div>Defensive Battles are special quests where you are tasked with defending a gate from oncoming enemies.</div><br><div>\u25a0 The Gate</div><div>You will begin these quests in front of the gate, and its HP will be visible in the upper part of the screen.</div><div>Your enemies' progress towards reaching it will also be visible in the same portion of the screen.</div><div>The gate is entirely inanimate, and will not attack enemies.</div><br><div>\u25a0 Enemy Routes</div><div>When a new group of enemies appears on the map, the route they will take will be shown with arrows on the minimap.</div><div>There are some difficulties where enemy routes will not be displayed.</div><br><div>\u25a0 Boss Enemies</div><div>If you defeat all of the enemy waves on a map, you will be able to advance to a new area where a boss enemy is waiting.</div><div>The boss will not leave the boss area.</div><div>By defeating the boss within the allocated time, you will receive additional rewards.</div><br><div>\u25a0 Drawbridges</div><div>Some maps will have drawbridges placed on them.</div><div>Such quests will begin with the drawbridges raised, stopping both enemies and allies from crossing them.</div><div>By attacking a switch near a drawbridge, you will be able to lower and cross it.</div><div>Once a drawbridge has been lowered, it cannot be raised again. Enemies will never attack drawbridge switches.</div><br><div>\u25a0 Houses and Bandits</div><div>Some maps have houses on them. If a map has houses on it, bandits will prioritize attacking the houses over attacking your gate.</div><div>If you can defeat the bandits before a house is destroyed, a ring of light will appear in front of it. Standing in these rings will give you useful benefits, such as making your adventurers stronger and revealing enemy locations on the minimap.</div><div>Whether houses are destroyed will have no bearing on the rewards you receive at the end of a quest.</div><br><div>\u25a0 Quest Skills</div><div>Some quests feature special skills which can only be used in that quest.</div><div>The skill's area of effect will be based around the position of the adventurer you are controlling.</div><div>Each skill can only be used three times in a given quest, and after using the skill once, you will need to wait a set time before using it again.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 29,
	                "title": "Coliseum Events",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "596",
	                        "title": "What are Coliseum Events?",
	                        "text": "<div>Coliseum events are limited-time events in which you will seek to win a tournament.</div><div>You can also take part in event-exclusive boss battles.</div><br><div>\u25a0Unlock condition for coliseum events</div><div>Coliseum events are unlocked by clearing Chapter 2 (2-1) of the main campaign on Normal difficulty.</div>"
	                    },
	                    {
	                        "id": "597",
	                        "title": "Unlocking Quests and Quest Difficulties",
	                        "text": "<div>Coliseum events have multiple quests for each difficulty (beginner, standard, expert, and master).</div><div>At the start of a coliseum event, only one beginner quest will be unlocked.</div><br><div>More quests can be unlocked using items that are unique to the event.</div><br><div>After clearing all of the quests for a difficulty, you will receive a Victory Reward and the next difficulty will be unlocked.</div>"
	                    },
	                    {
	                        "id": "598",
	                        "title": "Prestige",
	                        "text": "<div>You can obtain prestige by clearing quests in coliseum events and doing so will earn you various rewards.</div><div>Among these rewards are event-specific items that can be used to unlock new stories and quests during coliseum events.</div>"
	                    },
	                    {
	                        "id": "599",
	                        "title": "Event-Specific Items",
	                        "text": "<div>You can use the following event-specific items, earned by obtaining prestige, to unlock quests and stories during coliseum events.</div><div>These event-specific items will reset each time there is a new coliseum event.</div><br><div>\u25a0Coliseum Map</div><div>This item is used to unlock quests.</div><br><div>\u25a0Special Invitation</div><div>This item is used to unlock EX quests.</div><br><div>\u25a0Tournament Chronicle</div><div>This item is used to unlock stories.</div>"
	                    },
	                    {
	                        "id": "600",
	                        "title": "Treasure Trade",
	                        "text": "<div>Coliseum crystals are event-specific items earned during coliseum events that can be exchanged at the treasure trade for various rewards.</div><div>Please keep in mind that event-specific items will reset each time there is a new coliseum event.</div>"
	                    },
	                    {
	                        "id": "601",
	                        "title": "Duels",
	                        "text": "<div>Duels are special quests unique to coliseum events. These can only be played solo, and the player will control only one adventurer.</div><br><div>\u25a0Winning Duels</div><div>Defeat the boss enemy to win the duel.</div><br><div>\u25a0Losing Duels</div><div>If your adventurer's HP falls to zero, you will lose the duel.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 9,
	                "title": "Statuses",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "255",
	                        "title": "Rarity",
	                        "text": "<div>The greater the \u2605number, the higher the rarity.</div>"
	                    },
	                    {
	                        "id": "256",
	                        "title": "Unbinding",
	                        "text": "<div>Refers to increasing the maximum potential of an adventurer, weapon, dragon, or wyrmprint.</div><br><div>For adventurers, this process is referred to as promotion rather than unbinding.</div><div>Weapons and wyrmprints are unbound by using either standard or unique materials.</div><div>Dragons are unbound by using either duplicate copies of the dragon in question or unique materials.</div>"
	                    },
	                    {
	                        "id": "257",
	                        "title": "Unit Types",
	                        "text": "<div>Indicates the following roles during quests:</div><div><br /></div><div>\u30fbAttack</div><div>\u30fbDefense</div><div>\u30fbSupport</div><div>\u30fbHealing</div>"
	                    },
	                    {
	                        "id": "258",
	                        "title": "Elements",
	                        "text": "<div>The following types of elements exist:</div><div><br /></div><div>\u30fbFlame</div><div>\u30fbWater</div><div>\u30fbWind</div><div>\u30fbLight</div><div>\u30fbShadow</div><div><br /></div><div>And they are related in the following ways:</div><div><br /></div><div>\u30fbFlame is weak to water, and strong to wind.</div><div>\u30fbWater is weak to wind, and strong to flame.</div><div>\u30fbWind is weak to flame, and strong to water.</div><div>\u30fbLight is weak to shadow.</div><div>\u30fbShadow is weak to light.</div>"
	                    },
	                    {
	                        "id": "259",
	                        "title": "HP",
	                        "text": "<div>A numerical value displaying health. If it reaches 0, the adventurer can no longer take part in battle.</div><div>During quests, your main adventurer&#39;s primary HP gauge (in the bottom corner of the screen) is light-green when full and dark-green when not.</div>"
	                    },
	                    {
	                        "id": "260",
	                        "title": "Strength",
	                        "text": "<div>A numerical value displaying attack power. The larger the number, the more damage the adventurer deals.</div>"
	                    },
	                    {
	                        "id": "261",
	                        "title": "Lv",
	                        "text": "<div>A numerical value showing an adventurer's growth. As an adventurer's level increases, so does their HP and strength.</div>"
	                    },
	                    {
	                        "id": "262",
	                        "title": "Co-abilities",
	                        "text": "<div>Abilities that all adventurers have that are applied to the entire team.</div><div>These abilities can be upgraded in each adventurer's mana circles.</div><div>In the event that two adventurers with the same co-ability are on the same team, only the more powerful of the two will be activated.</div><br><div>For example, if an adventurer with a co-ability that provides +10% defense and an adventurer with a co-ability that provides +5% defense are on the same team, the team will receive +10% defense.</div><br><div>When playing co-op, only the co-abilities of the adventurers in your team will affect your team; the co-abilities of adventurers in other players' teams will not.</div><div>The co-abilities of adventurers in your team will affect your entire team, regardless of if they actually participate in a quest (such as when playing co-op).</div>"
	                    },
	                    {
	                        "id": "486",
	                        "title": "Chain Co-abilities",
	                        "text": "<div>Abilities that all adventurers have that apply to the entire team.</div><div>These abilities can be upgraded in each adventurer's mana circles.</div><div>In the event that two adventurers with the same chain co-ability are on the same team, the effect will stack.</div><br><div>For example, if an adventurer with a chain co-ability that provides +10% defense to flame-attuned adventurers and an adventurer with a chain co-ability that provides +5% defense to flame-attuned adventurers are on the same team, flame-attuned adventurers on the team will receive +15% defense.</div><br><div>When playing co-op, only the chain co-abilities of the adventurers in your team will affect your team; the chain co-abilities of adventurers in other players' teams will not.</div><div>The chain co-abilities of adventurers in your team will affect your entire team, regardless of if they actually participate in a quest (such as when playing co-op).</div>"
	                    },
	                    {
	                        "id": "263",
	                        "title": "Abilities",
	                        "text": "<div>Effects that apply to the adventurers possessing them.</div>"
	                    },
	                    {
	                        "id": "264",
	                        "title": "Might",
	                        "text": "<div>A cumulative indication of power based on all types of stats, abilities, and skills.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 10,
	                "title": "Adventurers",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "492",
	                        "title": "Adventurers",
	                        "text": "<div>Adventurers who fight alongside the main character. They can be controlled during quests.</div><div><br /></div><div>They're recruited via summoning or by progressing through the story and events.</div>"
	                    },
	                    {
	                        "id": "493",
	                        "title": "Upgrading Adventurers",
	                        "text": "<div>\u25a0Grant Experience</div><div>Use materials to increase an adventurer's experience points.</div><div>Once their experience points reach a certain value, they will gain a level.</div><br><div>\u25a0Augments</div><div>Augmentation materials can be used to further increase an adventurer's HP and strength.</div><br><div>\u25a0Auto Upgrade</div><div>Automatically selects the materials necessary to upgrade the adventurer to the maximum level.</div><div>The materials will not be used until you press the Upgrade button.</div><div>The auto upgrade function will not select augmentation materials.</div><br><div>\u25a0Resetting Augments</div><div>Augments can be reset at the cost of rupies.</div><div>After resetting augments, the bonus HP and strength from augments will be reset and the augmentation materials that had been used will be returned to you.</div>"
	                    },
	                    {
	                        "id": "494",
	                        "title": "Mana Circles",
	                        "text": "<div>Use mana or materials to make adventurers stronger.</div><div>Each adventurer has their own set of mana circles.</div><br><div>\u25a0Unbinding</div><div>Once you have unlocked all of the nodes on a mana circle, you can unbind that level.</div><div>Materials are necessary to perform an unbinding.</div><br><div>\u25a0Attributes</div><div>Lets you check the mana circle status of the adventurer you have selected.</div><br><div>\u25a0Full unbinding reward</div><div>A reward received when you unlock the first 50 nodes in an adventurer's mana circles.</div><br><div>\u25a0XX's conviction/devotion</div><div>The mana nodes of certain adventurers are unlockable using items, such as XX's Conviction or XX's Devotion, that are obtained from certain events or quests.</div><div>Note that some mana nodes require additional items to unlock.</div>"
	                    },
	                    {
	                        "id": "495",
	                        "title": "Promotion",
	                        "text": "<div>Refers to raising an adventurer's rarity using eldwater.</div><div><br /></div><div>Once promoted, all of an adventurer's attributes and their maximum level increase.</div>"
	                    },
	                    {
	                        "id": "496",
	                        "title": "Eldwater",
	                        "text": "<div>A material required for promoting adventurers and upgrading co-abilities.</div><div>The necessary amount changes according to the \u2605 value of the adventurer.</div><br><div>You can acquire eldwater by summoning adventurers you've already befriended, by parting with dragons of 3\u2605 or greater rarity, by obtaining wyrmprints you already possess, and from events and endeavors.</div>"
	                    },
	                    {
	                        "id": "497",
	                        "title": "What are Shared Skills?",
	                        "text": "<div>Shared skills are an additional two skills that can be used by a team's leader.</div><div>Shared skills can be equipped by all members of the team, but only the team's leader may use them.</div><div>Only skills from other adventurers that meet certain conditions may be equipped.</div><br><div>\u25a0Unlock conditions for shared skills</div><div>Shared skills are unlocked by clearing Chapter 2 1-1 of the main campaign on Normal difficulty.</div>"
	                    },
	                    {
	                        "id": "498",
	                        "title": "Equipping and Unlocking Shared Skills",
	                        "text": "<div style=\"\">Shared skills can be equipped and unlocked from the Teams menu.</div><div style=\"\"><br></div><div>Once a skill has been unlocked for sharing, it can be equipped by any adventurer. Shared skills will always be the same level as the original skill.</div><br><div>\u25a0Unlock conditions for shared skills</div><div>1. The adventurer whose skill you want to use must be at Lv. 80 or above, and have 50 or more mana nodes unlocked.</div><div>2. The skill must be unlocked for sharing using elemental tomes of the same element as the skill.</div><div>(You can use the skills of adventurers who join during the main campaign as shared skills without unlocking them.)</div><br><div>\u25a0Additional information</div><div>There are some skills that cannot be shared.</div><div>Skills that can be shared but have yet to be unlocked will be shown as &quot;Shareable (Locked)&quot;.</div><div>Skills that do not have this text cannot be shared.</div><div>There are some adventurers that do not have any shareable skills.</div>"
	                    },
	                    {
	                        "id": "499",
	                        "title": "Shared Skill Priority",
	                        "text": "<div>Each adventurer has two shared skill slots, and these slots work slightly differently.</div><div>Shared Skill 1: When an adventurer is equipped with a weapon with a weapon skill, they will be able to equip either the weapon skill or a shared skill.</div><div>Shared Skill 2: When playing solo content, you can choose to use either a helper skill or this shared skill.</div><div>(When you are using a weapon skill in slot one, and a helper skill in slot two, you will not be able to use any shared skills. When a helper skill is equipped to the Shared Skill 2 slot, you will be able to use helper skills as normal. Helper skills can be used by adventurers other than the team leader.)</div><br><div>By default, skills from adventurers that join during the main campaign will be assigned as shared skills.</div><div>The priority list for these automatic assignments is as follows, from highest to lowest:</div><div>1. Cleo</div><div>2. Ranzal</div><div>3. The Prince</div><br><div>You cannot assign skills from adventurers with the same name and epithet as support skills.</div><div>For example, Ranzal from the main campaign cannot use shared skills from the same version of Ranzal, but can use skills from Gala Ranzal.</div>"
	                    },
	                    {
	                        "id": "500",
	                        "title": "Skill Point Costs for Shared Skills",
	                        "text": "<div>Each adventurer has a maximum number of skill points that can be used to equip shared skills, which varies for each adventurer.</div><div>Both shared skills&#39; combined point totals must be less than the maximum points allowed.</div><br><div>Even if you are playing solo using a helper skill instead of a second shared skill, the amount of points available for the first shared skill will still take into account the point cost of the user&#39;s second shared skill.</div>"
	                    },
	                    {
	                        "id": "501",
	                        "title": "Unlocking Shared Skills",
	                        "text": "<div>To unlock shared skills for use, you will need elemental tomes for the corresponding element.</div><br><div>These can be obtained from events, or from the shop by using diamantium.</div>"
	                    },
	                    {
	                        "id": "502",
	                        "title": "Shared Skills' Efficacy",
	                        "text": "<div>When a skill is used as a shared skill, the following reductions will be applied:</div><div>\u30fbIts skill gauge will fill either more slowly or more quickly depending on the adventurer.</div><div>\u30fbWhen a skill deals damage, its damage will be reduced.</div><div>\u30fbWhen a skill restores HP, its recovery potency will be reduced.</div><div>\u30fbIn some cases, it may function differently.</div>"
	                    },
	                    {
	                        "id": "503",
	                        "title": "Elemental Attunement of Shared Skills",
	                        "text": "<div>\u30fbDamage-dealing skills</div><div>In the event that the elemental attunement of a shared skill and the adventurer equipping said shared skill differ, the damage dealt by the shared skill will change to match the elemental attunement of the adventurer using the skill.</div><div>For example, if a flame-attuned adventurer uses a shared skill that would normally deal wind damage, the skill will instead deal flame damage.</div><br><div>\u30fbBuff and debuff skills</div><div>For shared skills that provide buffs and debuffs restricted to specific elements, these buffs and debuffs will only be applied to adventurers and enemies attuned to the element specified in the relevant skill's description.</div><div>For example, if a flame-attuned adventurer uses a shared skill that provides a strength buff to wind-attuned adventurers, the buff will not be applied to them and will instead only be applied to any wind-attuned team members.</div>"
	                    },
	                    {
	                        "id": "572",
	                        "title": "Manacaster Modes",
	                        "text": "<div>The following three manacaster modes exist, each with their own unique characteristics. Which modes are available varies by adventurer.</div><br><div>\u30fbLong-range mode</div><div>As the name implies, this manacaster mode specializes in attacking foes from afar. Its attacks damage foes in a line, and when attacking with force strikes, its range is increased even further.</div><br><div>\u30fbClose-range mode</div><div>The standard attacks of this manacaster arc outwards, making it ideal for close-range crowd control. By attacking foes at point-blank range, you can do even more damage.</div><br><div>\u30fbRapid-fire mode</div><div>This mode is ideal for attacking foes at mid-range, and both its standard attacks and force strikes shoot multiple shots rapidly.<br>Its force strikes are especially powerful. During force strikes, the manacaster will continue to fire as long as your finger touches the screen.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 11,
	                "title": "Weapons",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "542",
	                        "title": "Weapons",
	                        "text": "<div>The following types of weapons exist:</div><br><div>\u30fbSword</div><div>\u30fbDagger</div><div>\u30fbBlade</div><div>\u30fbLance</div><div>\u30fbAxe</div><div>\u30fbBow</div><div>\u30fbWand</div><div>\u30fbStaff</div><div>\u30fbManacaster</div><br><div>Equipping weapons to adventurers raises their HP and Strength. Adventurers are only able to equip a fixed weapon type.</div><br><div>Certain weapons have skills that can be used on quests when equipped to adventurers with matching elements.</div><br><div>Weapons can be obtained through the main campaign, events, and crafting.</div>"
	                    },
	                    {
	                        "id": "543",
	                        "title": "Forging",
	                        "text": "<div>Combine materials to create new weapons. You can craft more weapons by leveling up the smithy facility, and by obtaining certain other weapons.</div>"
	                    },
	                    {
	                        "id": "544",
	                        "title": "Upgrading Weapons",
	                        "text": "<div>Use materials to increase the HP and strength provided by a weapon.</div><br><div>The materials required will vary depending on the weapon you are upgrading and the amount its HP and strength will be upgraded.</div>"
	                    },
	                    {
	                        "id": "545",
	                        "title": "Unbinding Weapons",
	                        "text": "<div>You can increase the maximum amount of HP and strength a weapon can provide by using materials or specific items.</div><div>This process can only be performed a certain number of times.</div>"
	                    },
	                    {
	                        "id": "549",
	                        "title": "Weapon Refinement",
	                        "text": "<div>By using materials to refine a weapon, you can increase the maximum number of times that it can be unbound.</div><div>This process can only be performed a certain number of times for each weapon.</div>"
	                    },
	                    {
	                        "id": "550",
	                        "title": "Weapon Abilities",
	                        "text": "<div>By using materials, you can acquire weapon abilities that are effective against certain foes, such as some bosses in Void Battles.</div><div>An adventurer can only use these abilities if their weapon type and elemental attunement match that of the ability.</div><div>Different weapon types have different selections of weapon abilities available.</div>"
	                    },
	                    {
	                        "id": "551",
	                        "title": "Slots",
	                        "text": "<div>The number of wyrmprints a specific weapon can equip is determined by the weapon&#39;s number of slots, while the rarity of wyrmprints that can be equipped is determined by the types of slots.</div><div>You can add additional slots to weapons by using materials.</div><div>The most 5\u2605 wyrmprints that can be equipped on a given weapon is three, while the most 2\u2605 to 4\u2605 wyrmprints that can be equipped is two.</div>"
	                    },
	                    {
	                        "id": "552",
	                        "title": "Weapon Bonuses",
	                        "text": "<div>Weapon bonuses can be acquired by using materials, and combine with the boosts shown under Castle Information (viewable in the Castle Grounds) to power up adventurers.</div><div>Different weapons have different weapon bonuses, and some weapons have no weapon bonuses at all.</div>"
	                    },
	                    {
	                        "id": "553",
	                        "title": "Copies",
	                        "text": "<div>This number indicates the maximum number of adventurers in a team that you can equip with a given weapon.</div><div>This number can be increased by using materials, but the maximum number of copies you can possess of a weapon varies depending on the specific weapon.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 12,
	                "title": "Dragons",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "375",
	                        "title": "Dragons",
	                        "text": "<div>Use a pact to borrow a dragon's strength and shapeshift into it during a quest.</div><div><br /></div><div>Equipping a dragon to an adventurer increases the adventurer's HP and Strength, grants them new skills upon shapeshifting, and grants them effective abilities.</div><div><br /></div><div>You can form pacts with dragons through summoning or by progressing in the main story and events.</div>"
	                    },
	                    {
	                        "id": "376",
	                        "title": "Upgrading Dragons",
	                        "text": "<div>You can use materials or other dragons to upgrade a dragon.</div><br><div>\u25a0Grant Experience</div><div>Use materials or dragons to increase the experience points of the selected dragon. Once its experience points reach a certain value, it will gain a level.</div><br><div>Experience points obtained from dragons used as materials depend on the dragon&#39;s level.</div><br><div>\u25a0Augments</div><div>Augmentation materials and augmented dragons can be used to further increase a dragon&#39;s HP and strength.</div><div>When an augmented dragon is used as an upgrade material, the dragon being upgraded will gain the augments from the dragon used as an upgrade material.</div><div>If, during this process, the dragon has reached the maximum possible augmentation, the excess augmentation materials will be returned to you.</div><div>*If your storage for the augmentation material has reached capacity, the excess will be sent to your limited goodie box.</div><br><div>\u25a0Auto Upgrade</div><div>Automatically selects the materials necessary to upgrade the dragon to the maximum level.</div><div>The materials will not be used until you press the Upgrade button.</div><div>The auto upgrade function will not select augmentation materials or augmented dragons.</div><br><div>\u25a0Resetting Augments</div><div>Augments can be reset at the cost of rupies.</div><div>After resetting augments, the bonus HP and strength from augments will be reset and the augmentation materials that had been used will be returned to you.</div>"
	                    },
	                    {
	                        "id": "377",
	                        "title": "Unbinding Dragons",
	                        "text": "<div>You can raise a Dragon's maximum level by using a dragon identical to it or a special item. Dragons can be unbound even if they haven't reached their level cap.</div><br><div>Dragons used as unbinding materials will not transfer their unbinding progress.</div><div>Unbinding stages have a limit.</div><br><div>When an augmented dragon is used as an unbind material, the dragon being unbound will gain the augments from the dragon used as an unbind material.</div><div>If, during this process, the dragon has reached the maximum possible augmentation, the excess augmentation materials will be returned to you.</div><div>*If your storage for the augmentation material has reached capacity, the excess will be sent to your limited goodie box.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 13,
	                "title": "Wyrmprints",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "605",
	                        "title": "Wyrmprints",
	                        "text": "<div>These are talismans of sorts; memories of the world taken shape.</div><br><div>Equipping them to a weapon increases the wielder&#39;s HP and strength, but some grant abilities as well.</div><br><div>You can earn them by progressing through the main campaign and events, or trade for them at the shop.</div><br><div>The number of wyrmprints an adventurer can equip, as well as their rarity, is determined by the number of slots in their weapon.</div><br><div>Some wyrmprints also have an affinity, and if you have enough wyrmprints with the same affinity equipped at the same time, you will activate an affinity bonus.</div>"
	                    },
	                    {
	                        "id": "606",
	                        "title": "Upgrading Wyrmprints",
	                        "text": "<div>Use materials to strengthen wyrmprints.</div><br><div>\u25a0HP and Strength</div><div>You can use materials to increase a wyrmprint&#39;s HP and strength.</div><div>Materials vary based on the wyrmprint you are upgrading and how much it has already been upgraded.</div><br><div>\u25a0Augments</div><div>Augmentation materials can be used to further increase a wyrmprint&#39;s HP and strength.</div><div>There is a limit to how much a wyrmprint&#39;s HP and strength can be increased by augments.</div><br><div>\u25a0Resetting Augments</div><div>Augments can be reset at the cost of rupies.</div><div>After resetting augments, the bonus HP and strength from augments will be reset and the augmentation materials that had been used will be returned to you.</div>"
	                    },
	                    {
	                        "id": "607",
	                        "title": "Unbinding Wyrmprints",
	                        "text": "<div>You can increase the maximum amount of HP and strength a wyrmprint can provide by using materials or specific items.</div><div>This process can only be performed a certain number of times.</div><br><div>With some exceptions, additional text will be revealed as you unbind a wyrmprint and its image will change once you unbind two stages.</div>"
	                    },
	                    {
	                        "id": "609",
	                        "title": "Ability Effects and Maximum Values",
	                        "text": "<div>When multiple equipped wyrmprints have abilities with the same buff, that buff stacks.</div><div>However, there is a limit to how high a buff&#39;s value can go (e.g. Max 20%; Max 3 Times).</div><br><div>Notes:</div><div>\u30fbThis limit applies separately to each adventurer who has these wyrmprints equipped.</div><div>\u30fbAdventurer, weapon, and dragon abilities are not affected by this limit.</div><br><div>Example: Suppose an adventurer has a wyrmprint with Recovery Potency +13% (Max 20%) and a wyrmprint with Recovery Potency +10% (Max 20%) equipped. This adventurer will be granted Recovery Potency +20%, as this is the combined total of these effects up to the maximum limit of 20%.</div>"
	                    },
	                    {
	                        "id": "610",
	                        "title": "Regarding Certain Abilities",
	                        "text": "<div>If multiple wyrmprints an adventurer has equipped have an ability that provides the same buff under the same conditions, those abilities will be displayed as a single merged ability.</div><div>The buff value or roman numeral for a merged ability will display in a different color.</div><div>Furthermore, when a merged ability reaches its maximum potential, the buff value or roman numeral will display in yet another color.</div><br><div>Abilities that increase the amount of event-specific points and items obtained only benefit your own team when equipped.</div><br><div>Abilities that increase the amount of player EXP gained upon clearing a quest will confer their benefits to you in co-op rooms even when equipped on adventurers other than the team leader.</div><br><div>The ability Shield Prep grants its user a one-use shield that nullifies damage less than or equal to the specified percentage of their maximum HP. If the user takes damage greater than this amount, the shield will be broken, and no damage will be nullified. If the damage taken is less than or equal to this amount, the damage will be nullified, and the shield will be consumed.</div>"
	                    },
	                    {
	                        "id": "611",
	                        "title": "List of Abilities That Share the Same Maximum Value",
	                        "text": "<div>The following abilities share a maximum potential buff with other abilities that offer the same type of buff (e.g. two abilities that offer Strength +X%). When two of such abilities are equipped at once, the buff values are combined up to a maximum shared value (displayed alongside the buff).</div><div>*This list comprises buffs that have a variety of possible triggers, along with examples of relevant abilities for each buff type.</div><div>*Abilities that are dependent on the weapon type or elemental attunement of an adventurer also share a maximum potential buff with other abilities that offer the same type of buff and will function as described above.</div><br><div>Recovery Potency</div><div>Recovery Potency +X%</div><div>HP 70% = Healing +X%</div><div>Full HP = Healing +X%</div><br><div>Critical Damage</div><div>Critical Damage +X%</div><div>HP 70% = Critical Damage +X%</div><div>Full HP = Critical Damage +X%</div><br><div>Critical Rate</div><div>Critical Rate +X%</div><div>HP 70% = Critical Rate +X%</div><div>Flurry Devastation +X%</div><br><div>Skill Damage</div><div>Skill Damage +X%</div><div>HP 70% = Skill Damage +X%</div><div>Full HP = Skill Damage +X%</div><br><div>Strength</div><div>HP 70% = Strength +X%</div><div>Full HP = Strength +X%</div><div>Flurry Strength +X%</div><br><div>Defense</div><div>HP 70% = Defense +X%</div><div>Full HP = Defense +X%</div><br><div>Player EXP</div><div>Loving Heart</div><div>Happy Dragonyule!</div><br><div>Dragon Damage</div><div>Dragon Damage +X%</div><div>Enhanced Shapeshifting</div><br><div>Dragon Time</div><div>Dragon Time +X%</div><div>Enhanced Shapeshifting</div><br><div>Dragon Haste</div><div>Dragon Haste +X%</div><div>Enhanced Shapeshifting</div>"
	                    },
	                    {
	                        "id": "612",
	                        "title": "Copies",
	                        "text": "<div>This number indicates the maximum number of adventurers in a team that you can equip with a given wyrmprint.</div><div>This number can be increased by using materials, but the maximum number of copies you can possess of a wyrmprint varies depending on the specific wyrmprint.</div>"
	                    },
	                    {
	                        "id": "613",
	                        "title": "Equipping Wyrmprints",
	                        "text": "<div>You can equip a wyrmprint of the specified rarity in each slot of a given weapon.</div><div>An adventurer cannot be equipped with two copies of the same wyrmprint.</div>"
	                    },
	                    {
	                        "id": "614",
	                        "title": "Affinity Bonuses",
	                        "text": "<div>Equipping multiple wyrmprints with the same affinity on an adventurer will grant them an affinity bonus. Affinity bonuses do not count towards the maximum value a given type of ability (such as Strength +XX%) can reach.</div>"
	                    },
	                    {
	                        "id": "615",
	                        "title": "Favorites",
	                        "text": "<div>You can add or remove a wyrmprint to or from your favorites by tapping the star icon on that wyrmprint's details screen.</div><div>Wyrmprints added to your favorites will be displayed first when sorting with the Prioritize Favorites box checked on the Sort screen.</div>"
	                    },
	                    {
	                        "id": "644",
	                        "title": "Dragon Haste",
	                        "text": "<div>If multiple adventurers in the same team have wyrmprints with the Dragon Haste ability on them, only the most potent version of the ability will activate\u2014the abilities will not stack.</div><div>However, the Dragon Haste wyrmprint ability can stack with co-abilities and chain co-abilities with the Dragon Haste effect.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 14,
	                "title": "Teams",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "563",
	                        "title": "Editing Teams",
	                        "text": "<div>Customize or copy the team being sent out on a quest.</div>"
	                    },
	                    {
	                        "id": "564",
	                        "title": "Optimizing Teams",
	                        "text": "<div>Automatically selects the adventurers, weapons, wyrmprints, and dragons that best fit the situation.</div>"
	                    },
	                    {
	                        "id": "565",
	                        "title": "Swapping Adventurers",
	                        "text": "<div>You can include up to four adventurers in a single team. Tap the adventurer you want to include and then the slot you want to put them in.</div>"
	                    },
	                    {
	                        "id": "566",
	                        "title": "Changing Equipment",
	                        "text": "<div>To equip adventurers with a different weapon, dragon, or wyrmprints, tap the weapon, dragon, or wyrmprint that you want to change. This will take you to the equipment page. You can also save and equip equipment sets specific to each adventurer here, as well as save and equip wyrmprint decks from the wyrmprints section.</div><br><div>Notes:</div><div>The same dragon can't be equipped by two or more adventurers in a team at the same time.</div><div>Adventurers cannot be unarmed. They must always have a weapon equipped.</div>"
	                    },
	                    {
	                        "id": "567",
	                        "title": "Collection",
	                        "text": "<div>Check your adventurers, as well as the weapons, wyrmprints, and dragons in your possession. You can also part with your dragons from here.</div>"
	                    },
	                    {
	                        "id": "568",
	                        "title": "Details Screen",
	                        "text": "<div>On each list screen, you can tap and hold on an adventurer, weapon, wyrmprint, or dragon's icon to go to its details screen.</div><div><br /></div><div>You can view its details screen using this same method from other screens as well.</div>"
	                    },
	                    {
	                        "id": "569",
	                        "title": "Parting",
	                        "text": "<div>\u25a0Parting</div><div>Part ways with a dragon you&#39;ve made a pact with.</div><div>You will receive rupies and eldwater if you part with a dragon.</div><br><div>Note: You cannot part with dragons that are currently equipped to an adventurer.</div><br><div>If you part ways with an augmented dragon, the augmentation materials that had been used on them will not be returned to you.</div><br><div>\u25a04\u2605 rarity and higher</div><div>Before parting with any 4\u2605 or higher dragons, you&#39;ll need to mark the check box before you can proceed.</div><br><div>\u25a0Selecting multiples</div><div>You can specify certain conditions and select up to 50 dragons to part with at a time.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 15,
	                "title": "The Halidom",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "123",
	                        "title": "What is the Halidom?",
	                        "text": "<div>This is the castle the main character uses as his base. You can build various facilities and change the layout freely.</div><div><br /></div><div>You'll need a certain combined facility level in order to raise the Halidom's overall level. The area you can build on will increase as you raise the Halidom's level.</div>"
	                    },
	                    {
	                        "id": "124",
	                        "title": "Facilities",
	                        "text": "<div>These can be built within the Halidom.</div><div>By building facilities you can increase adventurers' abilities and receive items after a fixed amount of time passes.</div>"
	                    },
	                    {
	                        "id": "125",
	                        "title": "Special Benefits",
	                        "text": "<div>The ability of facilities to apply an effect to all targets.</div><div><br /></div><div>Event-limited facilities are only effective for the duration of the event. After the conclusion of the event, their special ability disappears.</div>"
	                    },
	                    {
	                        "id": "126",
	                        "title": "Castle Grounds",
	                        "text": "<div>You can spend rupies to build facilities within the Halidom. The number of facilities you can build at one time depends on your amount of smithwyrms.</div>"
	                    },
	                    {
	                        "id": "127",
	                        "title": "Storing in Storehouse",
	                        "text": "<div>Facilities in the Halidom can be stored in the storehouse.<br>You can retrieve facilities from the storehouse and place them on the castle grounds from the Manage Facilities screen.</div>"
	                    },
	                    {
	                        "id": "128",
	                        "title": "Repositioning Facilities",
	                        "text": "<div>You can reposition facilities within the Halidom.</div>"
	                    },
	                    {
	                        "id": "129",
	                        "title": "Leveling Up Facilities",
	                        "text": "<div>You can use rupies or materials to improve facilities built in the Halidom.</div><div><br /></div><div>Facilities that are under construction will still increase adventurers' attributes, but you cannot collect items from them until they're complete.</div>"
	                    },
	                    {
	                        "id": "130",
	                        "title": "Finishing Construction Now",
	                        "text": "<div>You can complete a construction tent immediately using either diamantium, wyrmite or a hustle hammer.</div><br><div>The amount of diamantium or wyrmite required depends on the time left until construction is complete.</div><div>A single hustle hammer, however, will instantly complete a facility's construction, regardless of how much time is left.</div>"
	                    },
	                    {
	                        "id": "132",
	                        "title": "Showing/Hiding Objects",
	                        "text": "<div>Display facilities in the Halidom by their ability icons.</div>"
	                    },
	                    {
	                        "id": "133",
	                        "title": "Castle Info",
	                        "text": "<div>Check the details of facilities placed in the Halidom.</div>"
	                    },
	                    {
	                        "id": "134",
	                        "title": "Hiding UI",
	                        "text": "<div>Hide on-screen buttons in the Halidom.</div><div>Tap the screen to bring them back.</div>"
	                    },
	                    {
	                        "id": "135",
	                        "title": "Smithwyrms",
	                        "text": "<div>Used in the construction and leveling-up of facilities.</div><div>You'll begin with two smithwyrms, but you can increase that number to a maximum of five by using diamantium or wyrmite.</div>"
	                    },
	                    {
	                        "id": "412",
	                        "title": "Honey Tea",
	                        "text": "<div>One honey tea is produced by the Halidom every 30 minutes.</div><div>You can restore stamina by collecting honey tea. If collecting the honey tea produced at the Halidom would increase your stamina past 999, you will be unable to collect it.</div>"
	                    },
	                    {
	                        "id": "655",
	                        "title": "Manage Facilities",
	                        "text": "<div>All of the facilities you currently possess can be viewed on the Manage Facilities screen, where they will be divided into categories. From this screen, you can place, store, and level up individual facilities.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 16,
	                "title": "The Dragon's Roost",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "136",
	                        "title": "What is the Dragon's Roost?",
	                        "text": "<div>This is a place where the player can interact with dragons.</div><div>Give gifts to dragons to increase their bond with you.</div>"
	                    },
	                    {
	                        "id": "137",
	                        "title": "Bond",
	                        "text": "<div>Increasing your bond with a dragon increases its might and lengthens the duration your shapeshift into it will last.</div><div>You can acquire items or unlock dragon stories each time you reach a certain bond level.</div>"
	                    },
	                    {
	                        "id": "138",
	                        "title": "Gifts",
	                        "text": "<div>You can give these to dragons to increase their bond gauge and receive items in return.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 17,
	                "title": "Story",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "139",
	                        "title": "Adventurer Stories",
	                        "text": "<div>These are the stories of adventurers who have joined your cause. You will unlock new adventurer stories by unlocking story-unlock nodes in an adventurer&#39;s mana circles.</div>"
	                    },
	                    {
	                        "id": "140",
	                        "title": "Dragon Stories",
	                        "text": "<div>Stories of dragons you have entered into pacts with.</div><div>You will unlock new stories by raising your bonds with dragons in the Dragon's Roost.</div>"
	                    },
	                    {
	                        "id": "141",
	                        "title": "Castle Stories",
	                        "text": "<div>Special stories that can be unlocked using Looking Glasses.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 18,
	                "title": "Summoning",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "668",
	                        "title": "Summoning",
	                        "text": "<div>You can use diamantium, wyrmite, or vouchers to summon adventurers or dragons.</div><br><div>\u25a0Daily Deal</div><div>A single summon using 30 diamantium. This is limited to once per day, and can summon either an adventurer or a dragon.</div><br><div>Note: Wyrmite and summoning vouchers cannot be used for the Daily Deal.</div><br><div>\u25a0Single Summon</div><div>A single summon using 120 wyrmite or diamantium. This summons either an adventurer or a dragon.</div><div>Unlike Tenfold Summons, even if you use ten Summon Vouchers at once you are not guaranteed one 4\u2605 or higher summon.</div><br><div>\u25a0Tenfold Summon</div><div>Ten consecutive summons using 1200 wyrmite or diamantium. This is guaranteed to summon a 4\u2605 or higher of either an adventurer or a dragon.</div>"
	                    },
	                    {
	                        "id": "669",
	                        "title": "First Encounters",
	                        "text": "<div>See a preview of the first chapter of a summonable adventurer&#39;s story.</div>"
	                    },
	                    {
	                        "id": "670",
	                        "title": "Summon History",
	                        "text": "<div>You can view your summon history by opening the Menu, tapping Help/Support, and then tapping Summon History.</div><div>This will display up to 30 summons that you performed in the last two weeks (14 days).</div><div>If more than two weeks have passed since a summon was performed, it will be removed from the summon history.</div><div>Also, if the number of summons in the summon history exceeds 30, only the 30 most recent summons will be displayed.</div><div>The Prize Tier Obtained section displayed in Summon Details under Summon History will only show results for summon showcases where you can obtain prizes.</div><div>For summon showcases where you cannot obtain prizes, it will display as N/A.</div>"
	                    },
	                    {
	                        "id": "671",
	                        "title": "Wyrmsigils",
	                        "text": "<div>\u25a0Earning Wyrmsigils</div><div>Wyrmsigils are earned by summoning in summon showcases.</div><div>However, the following exceptions exist: Platinum Showcases (including the Platinum Showcase Deluxe), 5\u2605 adventurer summons (including 5\u2605 adventurer summon+), 5\u2605 dragon summons (including 5\u2605 dragon summon+), and Scratch-A-Thon summons do not grant the player wyrmsigils.</div><br><div>Each summon performed using wyrmite or summon vouchers will earn the player one wyrmsigil.</div><div>Each summon performed using diamantium will earn the player two wyrmsigils.</div><div>This amount is fixed, and does not vary based on adventurer or dragon rarity, or whether you have already befriended the adventurers and dragons you summon.</div><br><div>\u30fbUsing Wyrmsigils</div><div>After earning the required number of wyrmsigils required for redemption in the same summon showcase, you can redeem the required number of wyrmsigils for an adventurer or dragon of your choosing. You cannot select adventurers you have already befriended.</div><br><div>Wyrmsigils can only be used while the summon showcase where they were earned is still available, and cannot be used during later summon showcases or in other showcases being held at the same time.</div><br><div>Even after earning the number of wyrmsigils required for redemption on a given summon showcase, you can continue to summon and earn more wyrmsigils without exchanging those wyrmsigils for an adventurer or dragon. Even in this case, you will continue to receive the same number of wyrmsigils for each summon as before.</div><br><div>The number of wyrmsigils required for redemption varies between summon showcases. You can check the details for each showcase by tapping the Showcase Info button on a summon showcase&#39;s page in the Summon menu, then tapping the Details tab.</div><br><div>\u30fbWyrmsigil Redemption List</div><div>The lineup of adventurers and dragons available for redemption with wyrmsigils varies between summon showcases. You can confirm which adventurers and dragons are available by tapping the Wyrmsigils button on each summon showcase&#39;s page in the Summon menu.</div><br><div>\u30fbAfter a Summon Showcase Ends</div><div>When a summon showcase ends, all wyrmsigils earned during that showcase will automatically be converted into an equal number of wyrmsigil remnants.</div><div>The time at which this will happen is displayed next to &quot;Available until&quot; at the bottom of the Wyrmsigil Redemption screen.</div><div>Providing you have the required number of wyrmsigils, they can be exchanged for an adventurer or dragon of your choice from the available selection before this time.</div><div>Once this time passes, however, all wyrmsigils you have acquired from that summon showcase will be automatically converted into wyrmsigil remnants, even if you have the number of wyrmsigils required for redemption or more.</div><br><div>\u30fbWyrmsigil Remnants</div><div>Wyrmsigil remnants can be redeemed for a selection of items listed in the Treasure Trade.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 19,
	                "title": "More",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "144",
	                        "title": "Items",
	                        "text": "<div>Check held items, items details, and their quantities.</div>"
	                    },
	                    {
	                        "id": "145",
	                        "title": "Profiles",
	                        "text": "<div>Change your epithet and player name, or check your Player ID.</div>"
	                    },
	                    {
	                        "id": "146",
	                        "title": "Stickers",
	                        "text": "<div>Check your stickers for use during co-op play or edit your sticker sets.</div>"
	                    },
	                    {
	                        "id": "148",
	                        "title": "Achievements",
	                        "text": "<div>You can use a separate service to view the achievements you&#39;ve earned in game.</div><div><br></div><div>The iOS version requires a Game Center account.</div>"
	                    },
	                    {
	                        "id": "149",
	                        "title": "Friends",
	                        "text": "<div>You will receive more mana when you set one of your friends as a helper.</div><div><br /></div><div>Helpers will be able to use their skills more frequently in battle than normal adventurers.</div><div><br /></div><div>\u25a0Registering friends</div><div>After a quest has ended, you can send a friend request to the player whose adventurer you used for support.</div><div><br /></div><div>You can also enter a Player ID to directly send a request. Once the request has been accepted, you will be friends.</div>"
	                    },
	                    {
	                        "id": "150",
	                        "title": "Helper Settings",
	                        "text": "<div>The adventurer set as your helper can be used by other players on quests as their helper.</div><div><br /></div><div>\u25a0Setting a helper</div><div>From the Friends menu, tap Helper Settings and then select an adventurer. After that, outfit them with the desired weapon, wyrmprint, and dragon.</div><div><br /></div><div>\u25a0Optimizing adventurers</div><div>You can automatically set up adventurers, weapons, wyrmprints, and dragons.</div>"
	                    },
	                    {
	                        "id": "151",
	                        "title": "Help/Support",
	                        "text": "<div>Takes you to Help, Feedback, and Inquiries.</div>"
	                    },
	                    {
	                        "id": "152",
	                        "title": "Leaving Feedback",
	                        "text": "<div>We are reviewing customers&#39; opinions and requests for the game.</div>"
	                    },
	                    {
	                        "id": "153",
	                        "title": "Contact",
	                        "text": "<div>If you require assistance concerning a technical issue or misconduct within the game, please contact Support.</div><br><div>Note: A response from the support office may sometimes take some time.</div>"
	                    },
	                    {
	                        "id": "154",
	                        "title": "Options",
	                        "text": "<div>Change various settings, such as those for sound, graphics, text, and notifications.</div>"
	                    },
	                    {
	                        "id": "155",
	                        "title": "Notices",
	                        "text": "<div>Check the User Agreement, Copyright Notice and Privacy Policy.</div>"
	                    },
	                    {
	                        "id": "156",
	                        "title": "Account Management",
	                        "text": "<div>Sign up for a Nintendo Account or link an existing account.</div><div>By linking to a Nintendo Account, you will have a backup of your save data in the event you want to change devices or if you lose or damage your current device.</div>"
	                    },
	                    {
	                        "id": "157",
	                        "title": "Purchase Information",
	                        "text": "<div>Check on the amount of diamantium you currently have.</div>"
	                    },
	                    {
	                        "id": "158",
	                        "title": "Return to Title Screen",
	                        "text": "<div>Return to the title screen.</div>"
	                    },
	                    {
	                        "id": "159",
	                        "title": "Dragalia Life",
	                        "text": "<div>A four-panel comic series that provides a laid-back introduction to the world of Dragalia Lost.</div>"
	                    },
	                    {
	                        "id": "160",
	                        "title": "The Adventurer's Guide!",
	                        "text": "<div>A four-panel comic series in which the game's adventurers attempt to ease the worries of players just starting out.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 20,
	                "title": "The Shop",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "161",
	                        "title": "What is the Shop?",
	                        "text": "<div>Here you can purchase diamantium, increase your inventory space, trade items, or purchase special goods.</div>"
	                    },
	                    {
	                        "id": "163",
	                        "title": "Upgrade Essentials",
	                        "text": "<div>These are items necessary for growing stronger.</div>"
	                    },
	                    {
	                        "id": "164",
	                        "title": "Treasure Trade",
	                        "text": "<div>Exchange items acquired during quests for precious goods.</div><div>The maximum amounts of rupies, mana, and materials that you can exchange for at one time are as follows:</div><br><div>\u25a0Rupies</div><div>30,000,000</div><div>\u25a0Mana</div><div>5,000,000</div><div>\u25a0Materials (excluding event items)</div><div>10,000</div>"
	                    },
	                    {
	                        "id": "423",
	                        "title": "Packs",
	                        "text": "<div>Packs can be purchased in the shop, and come in several different varieties, including packs that pair diamantium with useful items, and packs that confer helpful benefits for a set period of time.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 22,
	                "title": "The Mercurial Gauntlet",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "283",
	                        "title": "What is The Mercurial Gauntlet?",
	                        "text": "<div>The Mercurial Gauntlet is a rewarding event that pits you against Fafnir Roy III, a treasure-loving dragon who lives in the Halidom's vaults.</div><br><div>\u25a0Unlock conditions for The Mercurial Gauntlet</div><div>The Mercurial Gauntlet is unlocked by clearing Chapter 2 (2-1) of the main campaign on Normal difficulty.</div>"
	                    },
	                    {
	                        "id": "284",
	                        "title": "Quests and Quest Levels",
	                        "text": "<div>The Mercurial Gauntlet is comprised of the following five elementally-attuned quests:</div><div>\u30fbThe Mercurial Gauntlet (Flame)</div><div>\u30fbThe Mercurial Gauntlet (Water)</div><div>\u30fbThe Mercurial Gauntlet (Wind)</div><div>\u30fbThe Mercurial Gauntlet (Light)</div><div>\u30fbThe Mercurial Gauntlet (Shadow)</div><br><div>You will face off with an elemental variant of Fafnir Roy III based on the quest you select.</div><div>Once defeated, that elemental variant of Fafnir Roy III will gain a level and grow in strength.</div><br><div>Clearing quests in The Mercurial Gauntlet will not provide player EXP or adventurer EXP.</div><div>Once a quest has been cleared, it cannot be repeated.</div><div>*Once all levels for a given quest have been cleared, it is possible to replay the final level of that quest.</div>"
	                    },
	                    {
	                        "id": "285",
	                        "title": "Combined Level",
	                        "text": "<div>The combined level adds up the highest level of each elemental variant of Fafnir Roy III that you have defeated and creates one total.</div><div>Each time you conquer a new level of The Mercurial Gauntlet, your combined level will increase by one.&nbsp;</div>"
	                    },
	                    {
	                        "id": "286",
	                        "title": "The Victor's Trove",
	                        "text": "<div>When you clear a quest in The Mercurial Gauntlet, treasure will be added to the Victor's Trove.</div><div>The Victor's Trove can be collected by tapping the banner for The Mercurial Gauntlet on or after a specified date each month.</div><div>If you wait until the specified date on the next month without collecting the Victor's Trove, you will lose the ability to collect the Victor's Trove from the previous month.</div><div>The combined level will not reset after the Victor's Trove is collected.</div><br><div>You can check what day the Victor's Trove can be collected on the quest screen for The Mercurial Gauntlet.</div>"
	                    },
	                    {
	                        "id": "287",
	                        "title": "Stamina Consumption",
	                        "text": "<div>The Mercurial Gauntlet is exclusively for solo play, but stamina is not consumed when playing quests related to The Mercurial Gauntlet.</div>"
	                    },
	                    {
	                        "id": "288",
	                        "title": "Drop Rewards",
	                        "text": "<div>Drop rewards can only be obtained once from each level of a given quest in The Mercurial Gauntlet.</div>"
	                    },
	                    {
	                        "id": "289",
	                        "title": "Clearing Endeavors",
	                        "text": "<div>While playing quests in The Mercurial Gauntlet, you will only be able to clear endeavors that are directly related to The Mercurial Gauntlet.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 23,
	                "title": "Alliances",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "460",
	                        "title": "What are Alliances?",
	                        "text": "<div>The alliance feature allows players to chat and play co-op with other alliance members.</div><div>Enjoy and explore the world of Dragalia Lost with your comrades!</div>"
	                    },
	                    {
	                        "id": "461",
	                        "title": "Important Information Regarding Alliances",
	                        "text": "<div>Using the Alliance feature, players can freely input text to communicate with one another.</div><div>Please check the Code of Conduct in the Dragalia Lost User Agreement and be considerate when interacting with other players.</div><br><div>\u25a0How to handle inappropriate messages</div><div>In the event that you find an inappropriate message, you can report it by tapping on it and holding your finger down.</div><br><div>\u25a0How User Agreement violations will be handled</div><div>In the event that any violation is determined to have occurred, actions may be taken such as deleting the relevant message, limiting message functionality for the player that sent said message, and suspension of that player&#39;s ability to play Dragalia Lost.</div>"
	                    },
	                    {
	                        "id": "462",
	                        "title": "Forming an Alliance",
	                        "text": "<div>You can form an alliance, thus automatically becoming its leader.</div>"
	                    },
	                    {
	                        "id": "463",
	                        "title": "Joining an Alliance",
	                        "text": "<div>You can search for alliances that are recruiting members and join them.</div><div>You can also join the alliances of other players from your Friend List and several other places.</div><br><div>\u25a0Recruitment status</div><div>If an alliance's recruitment status is set to \"Open to All,\" anyone can join.</div><div>If an alliance's recruitment status is set to \"Approval Req.,\" you can join if your application is approved.</div><div>*You can only apply to one alliance at a time.</div><div>*If an alliance's recruitment status is set to \"Not Recruiting,\" you cannot apply to join that alliance.</div><br><div>\u25a0Suggested alliances</div><div>Selecting this tab will display a list of suggested alliances that are recruiting members.</div><br><div>\u25a0Search for an alliance by name</div><div>You can search for an alliance by entering its name.</div><div>The search results will display alliances with names that at least partially match the text entered.</div><br><div>\u25a0Search for an alliance by ID</div><div>You can search for an alliance by entering its ID.</div><div>The search results will display the alliance with an ID that exactly matches the eight-digit ID entered.</div><br><div>You will need a member of a given alliance to tell you their alliance's ID.</div><div>You can view your alliance's ID in the Alliance Settings menu.</div><br><div>\u25a0Current application</div><div>If you apply to join an alliance with \"Approval Req.\" set as its recruitment status, the information for the alliance that you are applying to will be displayed under the \"Current Application\" tab until your application is approved, rejected, or expires.</div><div>Applications will automatically expire after ten days.</div><br><div>\u25a0If searching for an alliance produces no results</div><div>A search may produce zero results in the following cases:</div><div>\u30fbThe alliance you searched for has set its recruitment status as \"Not Recruiting.\"</div><div>\u30fbThere is a mistake in the name or ID that you entered.</div><br><div>\u25a0Transferring to another alliance</div><div>You can be invited to join an alliance even when you are already in one.</div><div>If you choose to accept such an invitation, you will leave your current alliance, and be placed on standby.</div><br><div>While on standby, you will not be able to join another alliance, and once 24 hours have passed, you will automatically join the alliance whose invite you accepted.</div><div>During this standby period, the invitee can choose to cancel joining the alliance, but the alliance which invited them cannot revoke that invitation.</div><div>Even if the invitee chooses to cancel, they will need to wait 24 hours after being placed on standby before they can join any other alliance.</div>"
	                    },
	                    {
	                        "id": "464",
	                        "title": "Alliance Name",
	                        "text": "<div>An alliance's name can be changed at any time, but only by the alliance's leader.</div><div>Inappropriate names may be adjusted by the Dragalia Lost Team.</div>"
	                    },
	                    {
	                        "id": "465",
	                        "title": "Alliance Introduction",
	                        "text": "<div>An alliance's introduction is displayed when other players search for alliances.</div><div>It can be changed at any time, but only by the leader of that alliance.</div><div>Inappropriate introduction text may be adjusted by the Dragalia Lost Team.</div>"
	                    },
	                    {
	                        "id": "466",
	                        "title": "Alliance Notice Board Message",
	                        "text": "<div>An alliance's notice board message is displayed at the top of the alliance screen.</div><div>It can be changed at any time, but only by the leader of that alliance.</div><div>Inappropriate notice board messages may be adjusted by the Dragalia Lost Team.</div>"
	                    },
	                    {
	                        "id": "467",
	                        "title": "Chatting",
	                        "text": "<div>You can chat with your fellow alliance members.</div><div>Please review \"Important Information Regarding Alliances\" in the Alliances section of the Help menu before using the chat function.</div><br><div>\u25a0Alliance room recruiting</div><div>If an alliance member creates an alliance room, they will automatically send a message to the alliance chat requesting assistance.</div><div>This message will include the word \"Join\" in blue, which other members can tap to join the alliance room.</div>"
	                    },
	                    {
	                        "id": "468",
	                        "title": "Personal Icon",
	                        "text": "<div>Your personal icon is displayed when chatting and in your alliance's member list.</div><div>You can choose to use the icon for any of the adventurers or dragons in your collection.</div>"
	                    },
	                    {
	                        "id": "469",
	                        "title": "Crest",
	                        "text": "<div>An alliance's crest is displayed on the alliance screen and when other players search for alliances.</div><div>It can be changed at any time, but only by the leader of that alliance.</div>"
	                    },
	                    {
	                        "id": "470",
	                        "title": "Alliance Settings",
	                        "text": "<div>The Alliance Settings menu includes different options depending on if you are the alliance's leader or not. If you are the leader, you can also change the alliance's name, introduction, notice board message, crest, goal, and recruitment status.</div><br><div>\u25a0Notifications while the game is running</div><div>When this option is turned on, you will receive a notification while playing Dragalia Lost if an alliance member creates an alliance room.</div><div>*You will not receive notifications regarding chat messages.</div><div>*You will not receive notifications while playing quests.</div><div>*You will receive notifications when Dragalia Lost contacts the server, such as when you open the Home screen. You will not necessarily receive a notification immediately after an alliance member creates an alliance room.</div><br><div>\u25a0Notifications while the game is not running</div><div>When this option is turned on, you will receive a notification when not playing Dragalia Lost if an alliance member creates an alliance room.</div><div>*You will not receive notifications regarding chat messages.</div><div>*You must enable notifications in your device's settings to receive these notifications.</div>"
	                    },
	                    {
	                        "id": "471",
	                        "title": "Member List",
	                        "text": "<div>The Member List displays a list of current members, how many members there are, and the online status of each member.</div><div>Here the alliance's leader can manage members, which includes transferring leadership, appointing or relieving the alliance's officer, and dismissing members.</div><br><div>\u25a0Members' online status</div><div>\u30fbIf a member is marked as \"Available,\" they are currently accessing the alliance menu.</div><div>\u30fbIf a member is marked as \"Online,\" they are currently playing Dragalia Lost, but not accessing the alliance menu.</div><div>\u30fbIf a member is marked as \"Last play: X m ago,\" \"Last play: X h ago,\" or \"Last play: X d ago,\" the time shown is how long it's been since they last played Dragalia Lost.</div><br><div>\u25a0How to transfer leadership, appoint or relieve the alliance's officer, and dismiss members</div><div>1. Tap the Alliance button on the Home screen.</div><div>2. Tap the Member List button.</div><div>3. Tap the Manage button for the relevant member.</div><div>4. To transfer leadership to the selected member, tap the Transfer button.</div><div>&nbsp; &nbsp; To appoint the selected member as the alliance's officer, tap the Appoint button.</div><div>&nbsp; &nbsp; To relieve the selected member from their duty as the alliance's officer, tap the Relieve button.</div><div>&nbsp; &nbsp; To dismiss the selected member from the alliance, tap the Dismiss button.</div>"
	                    },
	                    {
	                        "id": "472",
	                        "title": "An Alliance's Leader and Officer",
	                        "text": "<div>When an alliance is formed, the player that formed that alliance automatically becomes its leader.</div><div>The leader can appoint one officer.</div><br><div>\u25a0The leader's responsibilities</div><div>\u30fbInviting others to join the alliance</div><div>\u30fbEditing the alliance's name, introduction, and notice board message</div><div>\u30fbChanging the alliance's crest</div><div>\u30fbSetting the alliance's goal</div><div>\u30fbChanging the alliance\u2019s recruitment status</div><div>\u30fbApproving applications to join the alliance</div><div>\u30fbDismissing members from the alliance</div><div>\u30fbTransferring leadership</div><div>\u30fbAppointing and relieving the officer</div><div>\u30fbDisbanding the alliance</div><br><div>\u25a0The officer's responsibilities</div><div>\u30fbInviting others to join the alliance</div><div>\u30fbApproving applications to join the alliance</div><br><div>\u25a0Automatic transfer of leadership</div><div>If the leader of an alliance does not log in for more than 14 days, the first member to check in with the alliance after 14 days have passed since the leader's last login will automatically have leadership of the alliance transferred to them.</div><br><div>\u25a0How to transfer leadership, appoint or relieve the alliance's officer, and dismiss members</div><div>1. Tap the Alliance button on the Home screen.</div><div>2. Tap the Member List button.</div><div>3. Tap the Manage button for the relevant member.</div><div>4. To transfer leadership to the selected member, tap the Transfer button.</div><div>&nbsp; &nbsp; To appoint the selected member as the alliance's officer, tap the Appoint button.</div><div>&nbsp; &nbsp; To relieve the selected member from their duty as the alliance's officer, tap the Relieve button.</div><div>&nbsp; &nbsp; To dismiss the selected member from the alliance, tap the Dismiss button.</div>"
	                    },
	                    {
	                        "id": "473",
	                        "title": "Leaving an Alliance",
	                        "text": "<div>You can leave an alliance by tapping the Leave button in the Alliance Settings menu.</div><div>After leaving an alliance, you will be unable to form or join an alliance for 24 hours.</div><br><div>If you are an alliance's leader, you cannot leave your alliance unless you either disband the alliance or transfer its leadership to another player.</div>"
	                    },
	                    {
	                        "id": "474",
	                        "title": "Disbanding an Alliance",
	                        "text": "<div>The leader of an alliance can disband the alliance.</div><div>After disbanding an alliance, the former leader of the alliance will be unable to form or join another alliance for 24 hours.</div><div>The former members of the alliance will be able to form or join other alliances as normal.</div>"
	                    },
	                    {
	                        "id": "475",
	                        "title": "Reporting",
	                        "text": "<div>If you find inappropriate content in any of the following, you can report it by tapping on it and holding your finger down.</div><br><div>\u30fbAlliance name</div><div>\u30fbAlliance introduction</div><div>\u30fbAlliance notice board message</div><div>\u30fbChat messages</div><br><div>In the event that any prohibited activity is determined to have occurred, actions may be taken such as deleting the relevant message or messages, limiting message functionality for the player that sent said message or messages, and suspension of that player's ability to play Dragalia Lost.</div>"
	                    },
	                    {
	                        "id": "476",
	                        "title": "Alliance Invitations",
	                        "text": "<div>You can invite others to join the alliance you are part of from the following screens:</div><div>\u30fbFriend List</div><div>\u30fbCo-op rooms</div><div>\u30fbThe repeat quest confirmation screen in co-op</div>"
	                    },
	                    {
	                        "id": "477",
	                        "title": "Receiving Alliance Invitations",
	                        "text": "<div>In the Alliance Settings, you can choose whether to receive alliance invitations when already part of an alliance.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 24,
	                "title": "Time Attack",
	                "anchor_id": "time_attack",
	                "child_list": [
	                    {
	                        "id": "590",
	                        "title": "Time Attack Challenges",
	                        "text": "<div style=\"\">This is a special event in which you can compete against other players to see who can clear set quests in the fastest time. These quests are divided into five variations: Beginner (solo), Standard (solo), Expert (solo), Master (solo), and Ranking (solo and co-op).</div>"
	                    },
	                    {
	                        "id": "591",
	                        "title": "Ranking Participation Conditions",
	                        "text": "<div style=\"\">Rankings are split into solo and co-op categories.</div><br><div>Solo</div><div>Anyone who clears the solo Ranking quest during the event period will automatically be placed in the time attack rankings as long as their network connection is working when they clear the quest. If you are disconnected before clearing the quest, or your connection is otherwise compromised when starting the quest, your clear time will not be eligible.</div><br><div>Co-op</div><div style=\"\">Anyone who clears the co-op Ranking quest during the event period with three other players will automatically be placed in the time attack rankings. If you clear the quest with fewer than three other players, your clear time will not be eligible. This applies even if you start a quest with three other players and one or more players is disconnected during the quest.</div>"
	                    },
	                    {
	                        "id": "592",
	                        "title": "Number of Attempts",
	                        "text": "<div>You can take on the quests in the Time Attack Challenges event as many times as you like for as long as they are available. However, stamina will be used when playing solo, and getherwings when playing co-op.</div>"
	                    },
	                    {
	                        "id": "593",
	                        "title": "Ranking Tiers",
	                        "text": "<div>There are two kinds of rankings available in the Time Attack Challenges event&mdash;the Top 100 Rankings (Solo)/Top 25 Rankings (Co-op) and the Overall Placement rankings.</div><div>Separate sets of rankings will be available for each quest.</div><br><div>You can check these rankings by tapping the Rankings buttons at the top right of the Time Attack Challenges event screen.</div><br><div>Top 100 Rankings (Solo)/Top 25 Rankings (Co-op)</div><div>The team compositions for the top 100 fastest teams in solo mode and top 25 fastest teams in co-op mode to clear the relevant quests during the event period will be displayed.</div><br><div>Overall Placement Rankings</div><div>Your overall percentile ranking relative to other participants will be displayed.</div>"
	                    },
	                    {
	                        "id": "594",
	                        "title": "Ranking Rewards",
	                        "text": "<div>After the event ends, players will receive rewards according to their best clear time.</div><div>To view the details of specific rewards, tap the Rewards button in the top right corner of the Time Attack Rankings screen.</div><div>Your final placement in the rankings can be viewed in the Overall Placement section of the menu.</div>"
	                    },
	                    {
	                        "id": "595",
	                        "title": "Class Rewards",
	                        "text": "<div>Class rewards are earned by clearing solo quests in the Time Attack Challenges event within a set amount of time.</div><div>They can be earned once for each class (C, B, A, A+, S, and S+) per difficulty, and earning the reward for a higher class will net you the rewards for all lower classes.</div><div>Example: Suppose you have already earned all the rewards up to the A (Beginner) class. If you earn the reward for C (Standard), you will also obtain the rewards for A+ (Beginner), S (Beginner), and S+ (Beginner).</div><br><div>Tap the Class Rewards button to see what rewards are available.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 28,
	                "title": "The Alberian Battle Royale",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "616",
	                        "title": "What is the Alberian Battle Royale?",
	                        "text": "<div>In this event, up to 16 players are scattered across a single map and must fight to be the last one standing.</div><br><div>In each match of the Alberian Battle Royale, you will choose an adventurer from groups of up to nine weapon types and upgrade them as the match progresses.</div><div>Adventurers who participate in the Alberian Battle Royale are not affected by the stats or effects of adventurers used during normal quests, dragons, weapons, wyrmprints, or Halidom facilities.</div>"
	                    },
	                    {
	                        "id": "617",
	                        "title": "Weapons That Can Be Used",
	                        "text": "<div>Before the battle begins, you must choose what type of weapon to wield: a sword, blade, dagger, axe, lance, wand, bow, staff, or manacaster.</div><div>Note: The manacaster operates in close-range mode.</div><br><div>Each type of weapon has its own inherent skill.</div>"
	                    },
	                    {
	                        "id": "618",
	                        "title": "Adventurer Skins",
	                        "text": "<div>You can change an adventurer's appearance with an adventurer skin. Skins for certain adventurers can be obtained at the Alberian Battle Royale's treasure trade, while others can be unlocked using items. Skins for adventurers featured in the current summon showcase will go on sale, costing fewer items to unlock. Note that some adventurers do not have adventurer skins, and that obtained adventurer skins may only be used in the Alberian Battle Royale.</div>"
	                    },
	                    {
	                        "id": "619",
	                        "title": "Weapon Skins",
	                        "text": "<div>You can change a weapon&#39;s appearance with a weapon skin from your collection.</div><br><div>Note: Weapon skins have no effect on an adventurer&#39;s stats in the Alberian Battle Royale.</div>"
	                    },
	                    {
	                        "id": "620",
	                        "title": "Upgrading Adventurers",
	                        "text": "<div>Adventurers can be upgraded with items obtained during the battle. There are two types of items: whetstones and tablets.</div><br><div>\u30fbWeapon upgrade items (whetstones)</div><div>Once a certain number of weapon upgrade items are collected, your weapon's level will increase and its HP and Strength stats will be upgraded. Weapons can be upgraded up to level 7.</div><br><div>\u30fbSkill items (tablets)</div><div>Depending on the type of skill item collected, a skill that differs from your weapon's inherent skill can be activated. Up to three types of skill items may be equipped and you may equip up to two of the same type. A skill item will be consumed each time the related skill is activated.</div><br><div>Skill items come in the following types:</div><br><div>\u30fbClose-range skills</div><div>Deals damage to enemies at close range.</div><br><div>\u30fbLong-range skills</div><div>Deals damage to enemies at long range.</div><br><div>\u30fbParalysis skills</div><div>Deals damage that inflicts paralysis.</div><br><div>\u30fbPoison skills</div><div>Deals damage that inflicts poison.</div><br><div>\u30fbBog skills</div><div>Deals damage that inflicts bog.</div><br><div>\u30fbRestorative skills</div><div>Gradually restores HP.</div>"
	                    },
	                    {
	                        "id": "621",
	                        "title": "Shapeshifting",
	                        "text": "<div>You can shapeshift into a predetermined dragon by charging the dragon gauge during battle. The appearance and capabilities of this dragon are equal between all players. The dragon gauge will only charge when you defeat other players.</div>"
	                    },
	                    {
	                        "id": "622",
	                        "title": "Miasma",
	                        "text": "<div>As the battle progresses, a harmful miasma will draw ever closer from the outskirts of the map. Your adventurer will take damage if they get caught in it, so keep an eye on its progress by using the minimap.</div>"
	                    },
	                    {
	                        "id": "623",
	                        "title": "Grass, Houses, and Tents",
	                        "text": "<div>You can hide yourself from other players by entering the grass and houses you find around the map. While in the grass, you can only see a short distance around you. You can find troves of items stored away in houses and tents.</div>"
	                    },
	                    {
	                        "id": "624",
	                        "title": "Enemies",
	                        "text": "<div>Other players aren't the only obstacles that you'll have to overcome. Defeat computer-controlled enemies and they may drop useful items. Special enemies may even appear after a certain amount of time has passed.</div>"
	                    },
	                    {
	                        "id": "625",
	                        "title": "Rewards",
	                        "text": "<div>\u25a0Rewards</div><div>Player EXP and battle points.</div><br><div>\u25a0Treasure Trade Rewards</div><div>You can redeem battle points to unlock new weapon types and adventurer skins to use in the Alberian Battle Royale, among other great rewards.</div><br><div>\u25a0Monthly Rewards</div><div>Obtain monthly rewards based on the number of battle points accumulated by participating in the Alberian Battle Royale. These rewards are reset every month.</div><br><div>Note: Battle points acquired in the Alberian Battle Royale tutorial will be added to your current battle points, but they will not be added to your monthly total.</div>"
	                    },
	                    {
	                        "id": "626",
	                        "title": "Volcano",
	                        "text": "<div>A volcano area has been added to the map. Flaming boulders will rain across the map after a set amount of time, and being hit by one of these will deal damage and inflict burn. There is a fixed chance for various items to appear from the fallen debris.</div>"
	                    },
	                    {
	                        "id": "627",
	                        "title": "Adventurer Skins with Battle Royale Skills",
	                        "text": "<div>Certain adventurer skins come with special skills for use in the Alberian Battle Royale when selected.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 30,
	                "title": "Notte's Notes",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "666",
	                        "title": "Battle Records",
	                        "text": "<div>Each time you clear a quest, your battle records will be updated with the total number of times adventurers of each element, weapon type, and unit type have been used.</div><br><div>Note: Elements, weapon types, and unit types used will only be counted once each per quest, even if your team includes multiple adventurers in the same category.</div>"
	                    },
	                    {
	                        "id": "667",
	                        "title": "Encyclopedia",
	                        "text": "<div>\u25a0Encyclopedia</div><div>Adventurers and dragons added to your roster will be logged in the encyclopedia.</div><div>Note: This does not include adventurers who have only joined you temporarily.</div><br><div>\u25a0Unit Icon Symbols</div><div>A special symbol will appear on a unit&#39;s icon in the encyclopedia upon fulfilling certain requirements for that unit.</div><br><div>\u30fbAdventurer requirements</div><div>Reach Lv. 80 and unlock 50 mana nodes.</div><div>The symbol&#39;s color will change upon reaching Lv. 100 and unlocking 70 mana nodes.</div><br><div>\u30fbDragon requirements</div><div>Unbind four times and reach a bond level of 30.</div><div>The symbol&#39;s color will change upon unbinding five times.</div><br><div>\u25a0Encyclopedia Bonuses</div><div>You can earn encyclopedia bonuses that will power up your adventurers and dragons by logging new units in the encyclopedia and achieving certain upgrade requirements. These bonuses can be activated by opening Notte&#39;s Notes.</div><br><div>\u30fbAdventurer bonuses</div><div>For every new adventurer logged in the encyclopedia, all adventurers attuned to that unit&#39;s element will gain +0.1% bonuses to both HP and strength. Reaching Lv. 80 with that adventurer will increase the HP bonus gained by 0.1%, followed by an additional 0.1% at Lv. 100, while unlocking 50 of their mana nodes will increase the strength bonus gained by 0.1%, followed by an additional 0.1% at 70 mana nodes.</div><br><div>\u30fbDragon bonuses</div><div>For every new dragon logged in the encyclopedia, all dragons attuned to that unit&#39;s element will gain +0.1% bonuses to both HP and strength. Unbinding a dragon four times will increase the HP bonus gained by 0.1%, followed by an additional 0.1% at five times, while reaching a bond level of 30 with a dragon will increase the strength bonus gained by 0.1%.</div><div>Note: The bonuses for unbinding a dragon a certain number of times can each only be earned once per dragon. Unbinding multiple copies of the same dragon will not grant additional bonuses.</div><br><div>\u25a0Encyclopedia Bonus Limit</div><div>The maximum possible value for each encyclopedia bonus is based on the total number of adventurers and dragons that exist in the game.</div><div>These limits will increase as new adventurers and dragons are introduced.</div><br><div>\u25a0Medals</div><div>By clearing certain quests without using skip tickets, your adventurers can earn medals. Medals are given on a per-adventurer basis.</div><br><div>If an adventurer&#39;s HP falls to zero, they will not gain any medals. If you use any revives or continues, none of your adventurers will gain any medals.</div><br><div>When playing co-op, only adventurers you yourself control will be eligible for medals.</div><div>Also, if a player disconnects immediately after a quest begins and your own adventurer(s) are forced to take their place, those adventurers will not be able to obtain any medals.</div><br><div>Adventurers that are only temporarily part of your roster can only earn medals once they have permanently joined you.</div>"
	                    }
	                ]
	            },
	            {
	                "id": 35,
	                "title": "Enter the Kaleidoscape",
	                "anchor_id": "",
	                "child_list": [
	                    {
	                        "id": "673",
	                        "title": "What is Enter the Kaleidoscape?",
	                        "text": "<div>In this solo play event, you take on the ever-changing labyrinth called the Kaleidoscape, collecting equipment and skills to aid you on your journey to its final floor.</div><br><div>When starting a new run, you first choose an adventurer to enter the Kaleidoscape, then level them up as you make your way through the labyrinth.</div><div>Note that your adventurer will not receive stat bonuses from facilities or encyclopedia bonuses, and their stats, skills, dragons, weapon, and wyrmprints are only specifically for in the Kaleidoscape.</div><div>While in the Kaleidoscape, your active adventurer will receive the bonuses and unlocks from all of their mana nodes, including those in the mana spiral if applicable, regardless of upgrade status.</div><br><div>With the exception of certain adventurers, your adventurer&#39;s skill gauges will fill automatically over time, and upon proceeding to a new floor, your adventurer&#39;s HP will be completely restored and all skill gauges will be filled.</div><div>In addition, except when taking on boss floors, your adventurer&#39;s skill damage and recovery potency will be reduced.</div><br><div>Note that the Kaleidoscape&#39;s floors change with each run.</div>"
	                    },
	                    {
	                        "id": "674",
	                        "title": "Fafnir",
	                        "text": "<div>Fafnir will fight together with your adventurer in the Kaleidoscape automatically and is immune to and unaffected by damage from enemies and traps.</div><br><div>\u25a0Skills</div><div>You can equip one of three possible skills for Fafnir to use in the Kaleidoscape.</div><div>Fafnir will not take any actions beyond following your adventurer and using the equipped skill.</div><br><div>\u25a0Abilities</div><div>You can use materials to unlock and upgrade Fafnir&#39;s abilities from the Fafnir Upgrades menu, increasing your adventurer&#39;s capabilities.</div><br><div>Note: Ability unlocks and upgrades completed while a Kaleidoscape run is suspended will not be reflected until that run has been completed.</div>"
	                    },
	                    {
	                        "id": "675",
	                        "title": "Enemies",
	                        "text": "<div>No enemies in the Kaleidoscape have any elemental attunement.</div><div>In addition, the race of some enemies may differ from elsewhere in the game.</div>"
	                    },
	                    {
	                        "id": "676",
	                        "title": "Rewards",
	                        "text": "<div>\u25a0Amber</div><div>Two types of amber can be collected in Enter the Kaleidoscape: dawn amber and dusk amber.</div><div>These can be acquired by defeating enemies, converting items in the Kaleidoscape, or completing expeditions, and they can be redeemed for treasure in the Treasure Trade or used to upgrade Fafnir's abilities.</div><div>You can hold a maximum of 99,999,999 of each type of amber, and any dawn amber or dusk amber that exceeds this amount will be discarded.</div><br><div>\u25a0Portrait wyrmprints</div><div>These wyrmprints are earned by completing runs of the Kaleidoscape or expeditions and feature artwork of the adventurer who earned them.</div><div>A maximum of one portrait wyrmprint can be equipped to a weapon.</div><div>Each portrait wyrmprint can have up to two abilities. The effects and potency of these abilities are random, and some abilities can only be used by adventurers with the same elemental attunement and/or weapon type as the pictured adventurer.</div><div>A portrait wyrmprint's stats are determined by the number of abilities it has.</div><div>Portrait wyrmprints cannot be upgraded or augmented.</div>"
	                    },
	                    {
	                        "id": "677",
	                        "title": "Continuing",
	                        "text": "<div>Continues are consumed in the Kaleidoscape when retrying a floor or suspending your progress. Your adventurer's skill gauges and dragon gauge will be completely filled when starting a floor after using a continue.</div><br><div>If you have no remaining continues, you will be unable to retry your current floor. You can still suspend your progress, but you will not be able to resume your run until your continues have been restored. Furthermore, if your adventurer's HP falls to zero with no remaining continues, you will be forced to end your run. When ending your run this way, you will obtain no portrait wyrmprints, and any amber collected as your reward for that run will be halved.</div><br><div>Continues are restored each day.</div>"
	                    },
	                    {
	                        "id": "678",
	                        "title": "Levels",
	                        "text": "<div>Your adventurer and Fafnir will start each run of the Kaleidoscape at level 1. Earn EXP by defeating enemies to level up and raise their stats.</div>"
	                    },
	                    {
	                        "id": "679",
	                        "title": "Inventory",
	                        "text": "<div>You can organize and equip items obtained in the Kaleidoscape from your inventory.</div><br><div>\u25a0Equipment</div><div>The equipment section displays the weapon and wyrmprints you currently have equipped.</div><div>You can change this equipment out with weapons and wyrmprints located in your adventurer or Fafnir pouches.</div><br><div>\u25a0Adventurer pouch</div><div>Weapons and wyrmprints that are not equipped are stored in your adventurer pouch. When obtained, they are automatically placed here if there is available space.</div><br><div>\u25a0Fafnir pouch</div><div>When obtained, weapons and wyrmprints that cannot fit in your adventurer pouch and shared skills that are not equipped are automatically placed in your Fafnir pouch.</div><div>The contents of your Fafnir pouch will be automatically emptied and converted to dawn amber when proceeding to a new floor.</div>"
	                    },
	                    {
	                        "id": "680",
	                        "title": "Weapons",
	                        "text": "<div>Equipping a weapon will raise your adventurer's HP and strength.</div><div>Weapons can be dropped by defeated enemies or otherwise found in treasure chests throughout the Kaleidoscape.</div><div>Weapons obtained in the Kaleidoscape cannot be brought back to the Halidom, but they can be converted to dawn amber.</div><br><div>\u25a0Skills</div><div>Some weapons have a randomly assigned skill.</div><div>If a weapon has a skill, equipping that weapon will automatically make its skill available for use.</div><br><div>\u25a0Abilities</div><div>Some weapons have a randomly assigned ability.</div><div>If a weapon has an ability, equipping that weapon will automatically activate its ability.</div>"
	                    },
	                    {
	                        "id": "681",
	                        "title": "Wyrmprints",
	                        "text": "<div>Up to three wyrmprints can be equipped in the Kaleidoscape, and equipping wyrmprints will raise your adventurer's HP and strength.</div><div>Wyrmprints can be dropped by defeated enemies or otherwise found in treasure chests throughout the Kaleidoscape.</div><div>Wyrmprints obtained in the Kaleidoscape cannot be brought back to the Halidom, but they can be converted to dawn amber.</div><br><div>\u25a0Abilities</div><div>Some wyrmprints have a randomly assigned ability.</div><div>If a wyrmprint has an ability, equipping that wyrmprint will automatically activate its ability.</div>"
	                    },
	                    {
	                        "id": "682",
	                        "title": "Shared Skills",
	                        "text": "<div>In the Kaleidoscape, shared skills are consumed upon use.</div><div>Shared skills can be dropped by defeated enemies or otherwise found in treasure chests throughout the Kaleidoscape.</div><div>Shared skills obtained in the Kaleidoscape cannot be brought back to the Halidom for use outside the Kaleidoscape, but they can be converted to dawn amber.</div><br><div>Note: Shared skills will not be used during auto-play.</div><br><div>When preparing to enter the Kaleidoscape, you can choose two shared skills that you have unlocked through normal play to bring with you.</div><br><div>Note: The combined shared skill point cost of both shared skill&#39;s can exceed 11 points.</div><br><div>\u25a0Unavailable shared skills</div><div>The following shared skills cannot be selected for use in the Kaleidoscape:</div><br><div>\u30fbGespenst (Veronica)</div><div>\u30fbShining Slash (Gala Luca)</div>"
	                    },
	                    {
	                        "id": "683",
	                        "title": "Dragons",
	                        "text": "<div>You can shapeshift into a dragon by tapping its icon, consuming one shapeshift for that dragon and some of the dragon gauge.</div><div>Up to a total of eight dragons can be added to your dragon roster for the current run by clearing certain floors.</div><div>Dragons obtained in the Kaleidoscape cannot be brought back to the Halidom.</div><br><div>Note: Your adventurer will not shapeshift during auto-play.</div><br><div>\u25a0Abilities</div><div>Adding a dragon to your dragon roster will automatically activate its ability.</div><div>Dragon abilities will remain active even after a dragon&#39;s shapeshift count has been reduced to zero.</div><br><div>\u25a0Rare dragons</div><div>Rare dragons will occasionally be available for selection.</div><div>They can only be acquired by redeeming dawn amber.</div><br><div>\u25a0Adventurers who cannot shapeshift into acquired dragons</div><div>Adventurers who shapeshift into a specific dragon designated by their abilities (e.g. Humanoid Midgardsormr) and adventurers who have dragondrive, unique shapeshift, Divine Dragon, Persona, or summon gauges cannot shapeshift into the dragons in their dragon roster, but their dragons&#39; abilities will still be activated.</div>"
	                    },
	                    {
	                        "id": "684",
	                        "title": "Suspending Progress",
	                        "text": "<div>Using the Suspend Progress feature consumes one continue, saves your progress, and returns you to the event menu. The next time you enter the Kaleidoscape, you can resume your run from the beginning of the floor where you previously suspended your progress. You will begin that floor with max HP. Certain buffs granted before suspending your progress will be reset.</div><div>Using the Retry Current Floor feature consumes one continue and returns you to the beginning of the current floor with max HP. Certain buffs granted before retrying the current floor will be reset.</div><br><div>Note: You cannot retry a floor with no remaining continues.</div><br><div>If you have no remaining continues, you can still suspend your progress, but you will not be able to resume your run until your continues have been restored.</div><br><div>Closing the game while in the Kaleidoscape will automatically suspend your progress.</div>"
	                    },
	                    {
	                        "id": "685",
	                        "title": "Retrying a Floor",
	                        "text": "<div>Using the Retry Current Floor feature consumes one continue and returns you to the beginning of the current floor with max HP.</div><div>Certain buffs granted before retrying the floor will be reset, and your inventory and shared skills will return to the state they were in when you first entered the floor.</div><br><div>Note: You cannot retry a floor with no remaining continues.</div>"
	                    },
	                    {
	                        "id": "686",
	                        "title": "Ending a Run",
	                        "text": "<div>Upon ending a run, you will collect the rewards earned for all cleared floors, which does not include the current floor, and return to the Halidom.</div><div>If your adventurer's HP falls to zero with no remaining continues, you will be forced to end your run. When ending your run this way, you will obtain no portrait wyrmprints, and any amber collected as a reward for that run will be halved.</div>"
	                    },
	                    {
	                        "id": "687",
	                        "title": "Skipping Floors",
	                        "text": "<div>You can use the Skip feature to skip to a floor midway through the Kaleidoscape.</div><div>You can only skip to certain floors that you have already reached with at least one adventurer, and you can only skip up to a maximum of 30 floors at once.</div><div>You will begin your run with random equipment, dragons, and shared skills.</div><br><div>Remaining skips are reset each day.</div>"
	                    },
	                    {
	                        "id": "688",
	                        "title": "Clear Time",
	                        "text": "<div>The amount of time spent on your run is displayed on the results screen after ending a run.</div><div>This time is only recorded when starting a run from floor one. It will not be recorded when using the Skip feature.</div>"
	                    },
	                    {
	                        "id": "689",
	                        "title": "Score",
	                        "text": "<div>Your score represents points gathered by defeating enemies.</div><div>Your score does not affect what rewards can be obtained in the Kaleidoscape.</div>"
	                    },
	                    {
	                        "id": "690",
	                        "title": "Expeditions",
	                        "text": "<div>You can select up to four adventurers to embark on an expedition into the Kaleidoscape.</div><div>Expeditions are completed automatically after a set amount of time and net rewards upon completion. Expeditions can explore up to certain floors that you have already cleared with at least one adventurer, and they can explore up to a maximum of 30 floors at once.</div><div>You can end expeditions early, but you will only receive rewards for the floors cleared up until that point.</div><br><div>Adventurers on expeditions cannot embark upon a standard run of the Kaleidoscape.</div><div>Conversely, an adventurer with suspended progress in the Kaleidoscape cannot embark upon an expedition.</div>"
	                    },
	                    {
	                        "id": "691",
	                        "title": "Memories of the Sacred Tree",
	                        "text": "<div>Memories of the Sacred Tree are unlocked by clearing certain requirements in Enter the Kaleidoscape.</div>"
	                    }
	                ]
	            }
	        ],
	        "text_list": []
	    }
	}

Notes
------
