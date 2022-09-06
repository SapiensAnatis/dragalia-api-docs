Undocumented endpoints
=======================

A complete list of endpoints can be obtained by peering into the game files and looking for functions that handle the requests to and responses from these. This allows us to know which endpoints exist, but have not yet been documented. Some of these are very likely to be unused and impossible to trigger.

List
------

These are endpoints which may be possible to trigger, but which have yet to be documented. If you have any ideas about how to trigger them, please get in touch!

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Endpoint
     - Notes
   * - BattleRoyalEventReleaseCharaSkin
     - Not triggered when buying fighter skin, changing fighter skin, weapon skin in ABR
   * - BattleRoyalRecordRoyalRecordMulti
     - Not triggered when finishing a battle royale
   * - BattleRoyalStartMulti
     - Not triggered when starting a battle royale
   * - BuildEventReceiveDailyBonus
     - Possible related to Nightmare 
   * - CharaGetList
     -
   * - CollectEventEntry
     -
   * - CollectEventGetEventData
     -
   * - DmodeDungeonSystemHalt
     - See :doc:`/dragalia/dmode_dungeon_user_halt`. Closing app?
   * - DungeonRecordRecordMulti
     - Not triggered when finishing a co-op quest
   * - DungeonRetry
     - Not triggered when pressing retry on a quest
   * - DungeonSkipStartMultipleQuestAssignUnit
     -
   * - DungeonStartStartMultiAssignUnit
     - AssignUnit usually means quests where you are forced to use a specific unit
   * - EarnEventEntry
     - 
   * - EarnEventGetEventData
     -
   * - EarnEventReceiveEventPointReward
     -
   * - EventDamageGetTotalDamageHistory
     - Possibly related to the Satan event
   * - EventDamageReceiveDamageReward
     - Possibly related to the Satan event
   * - EventStoryRead
     - See :doc:`/dragalia/quest_read_story` or :doc:`/dragalia/story_read`
   * - ExchangeGetUnitList
     - Special vouchers? (dream, 5* unit)
   * - ExchangeSelectUnit
     - Special vouchers? (dream, 5* unit)
   * - GuildChatPostReport
     - 
   * - GuildJoinReply
     - Replying to a request to join your guild
   * - GuildJoinReplyAllDeny
     - Replying to a request to join your guild
   * - GuildJoinRequestCancel
     - Cancelling a request to join another guild
   * - GuildPostReport
     - Reporting a message in a guild?
   * - GuildSearchGetGuildDetail
     - 
   * - InquiryReply
     - Nintendo customer support reply
   * - LoginPenaltyConfirm
     -
   * - MatchingGetRoomListByGuild
     -
   * - MissionReceiveAlbumReward
     - See: :doc:`/dragalia/album_index` for Encyclopaedia. Not triggered when getting unit bonuses
   * - MissionReceiveBeginnerReward
     - Some kind of endeavour, e.g. :doc:`/dragalia/mission_receive_daily_reward`
   * - MissionReceiveMainStoryReward
     - Some kind of endeavour, e.g. :doc:`/dragalia/mission_receive_daily_reward`
   * - MissionUnlockMainStoryGroup
     -
   * - QuestGetQuestClearPartyMulti
     - For solo, this corresponds to the 'preferred team' button. See :doc:`/dragalia/quest_get_quest_clear_party`
   * - QuestSearchQuestClearPartyCharaMulti
     - Relates to seeing previous clears of endgame quests. See :doc:`/dragalia/quest_search_quest_clear_party_chara`
   * - QuestSearchQuestClearPartyMulti
     - Relates to seeing previous clears of endgame quests. See :doc:`/dragalia/quest_search_quest_clear_party`
   * - SummonExcludeGetOddsData
     -
   * - SummonExcludeRequest
     -
   * - SummonSummonPointTrade
     - Probably sparking a unit
   * - ToolReauth
     -
   * - TrackRecordUpdateProgress
     -
   * - TreasureTradeGetList
     - Related: :doc:`/dragalia/treasure_trade_get_list_all`
   * - UserGetWalletBalance
     -
   * - UserLinkedNAccount
     - Probably for completing the endeavour to link a Nintendo account
   * - UserOptInSetting
     -
   * - UserRecoverStaminaByStone
     -
   * - UserWithdrawal
     -
   * - WalkerSendGiftMultiple
     -
   * - WallReceiveMonthlyReward
     - Getting monthly Mercurial Gauntlet reward
   * - WallStartStartAssignUnit
     - See: :doc:`/dragalia/wall_start_start`. AssignUnit elsewhere forces you to use a particular unit


Deprecated
--------------------

These endpoints are *probably* deprecated, due to referring to pre-2.0 functionality or having their corresponding functions taken over by other endpoints.

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - Endpoint
     - Notes
   * - AmuletBuildup
     - Possibly previous wymprint endpoint pre-2.0 update
   * - AmuletLimitBreak
     - Possibly previous wymprint endpoint pre-2.0 update
   * - AmuletResetPlusCount
     - Possibly previous wymprint endpoint pre-2.0 update
   * - AmuletSell
     - Possibly previous wymprint endpoint pre-2.0 update
   * - AmuletSetLock
     - Possibly previous wymprint endpoint pre-2.0 update
   * - AmuletTradeGetList
     - Possibly previous wymprint endpoint pre-2.0 update
   * - AmuletTradeTrade
     - Possibly previous wymprint endpoint pre-2.0 update
   * - WeaponBuildup
     - Pre-2.0, now uses :doc:`/dragalia/weapon_body_buildup_piece`
   * - WeaponLimitBreak
     - Pre-2.0, now uses :doc:`/dragalia/weapon_body_buildup_piece`
   * - WeaponResetPlusCount
     - Pre-2.0, now uses :doc:`/dragalia/weapon_body_buildup_piece`
   * - WeaponSell
     - Pre-2.0, no longer possible to sell weapons
   * - WeaponSetLock
     - Pre-2.0, no longer possible to sell weapons
   * - CraftAssemble
     - Pre-2.0 weapon crafting, now uses :doc:`/dragalia/weapon_body_craft`
   * - CraftCreate
     - Pre-2.0 weapon crafting, now uses :doc:`/dragalia/weapon_body_craft`
   * - CraftDisassemble
     - Pre-2.0, no longer possible to disassemble weapons
   * - CraftResetNew
     - Probably pre-2.0, but unsure what it refers to
   * - MazeEventEntry
     - Possibly unused Kaleidoscape endpoint -- now uses :doc:`/dragalia/dmode_entry`
   * - MazeEventGetEventData
     - Possibly unused Kaleidoscape endpoint -- now uses :doc:`/dragalia/dmode_get_data`
   * - MazeEventReceiveMazePointReward
     - Possibly unused Kaleidoscape endpoint -- now uses :doc:`/dragalia/dmode_dungeon_finish`

Not possible to document
-------------------------

The following endpoints are unlikely to be documented before end-of-service.

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - Endpoint
     - Notes
   * - ExHunterEventEntry
     - Monster Hunter event
   * - ExHunterEventGetEventData
     - Monster Hunter event
   * - ExHunterEventReceiveExHunterPointReward
     - Monster Hunter event
   * - ExRushEventEntry
     - Mega Man event
   * - ExRushEventGetEventData
     - Mega Man event
   * - LotteryGetOddsData
     - New Year's lottery?
   * - LotteryLotteryExec
     - New Year's lottery?
   * - LotteryResult
     - New Year's lottery?
   * - MaintenanceGetText
     - Server maintenance
   * - ToolGetMaintenanceTime
     - Probably called when you try to log in during maintenance
   * - TimeAttackRankingGetData
     - Time attack
   * - TimeAttackRankingReceiveTierReward
     - Time attack
   * - ShopChargeCancel
     - 
   * - ShopGetBonus
     -
   * - ShopGetDreamSelectUnitList
     -
   * - ShopGetProductList
     -
   * - ShopPreChargeCheck
     -
   * - ShopSpecialShopPurchase
     -   
   * - MissionReceiveSpecialReward
     - Shop-bought special endeavours
   * - SimpleEventEntry
     - Likely corresponds to story-only events e.g. Cleo NY sweep
   * - SimpleEventGetEventData
     - Likely corresponds to story-only events e.g. Cleo NY sweep
   * - DreamAdventureClear
     - Notte's Slumber Shot?
   * - DreamAdventurePlay
     - Notte's Slumber Shot?