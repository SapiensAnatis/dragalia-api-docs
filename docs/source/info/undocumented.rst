Undocumented endpoints
=======================

A complete list of endpoints can be obtained by peering into the game files and looking for functions that handle the requests to and responses from these. This allows us to know which endpoints exist, but have not yet been documented. Some of these are very likely to be unused and impossible to trigger.

List
------

These are endpoints which may be possible to trigger, but which have yet to be documented because it is not known or not easy to trigger them.

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - Endpoint
     - Notes

   * - AbilityCrestGetAbilityCrestSetList
     -
   * - AbilityCrestSetAbilityCrestSet
     -
   * - AbilityCrestUpdateAbilityCrestSetName
     -
   * - BattleRoyalEventReleaseCharaSkin
     - Not triggered when buying an ABR fighter skin or changing fighter skin/weapon skin in ABR
   * - BattleRoyalRecordRoyalRecordMulti
     - Not triggered when finishing a battle royale
   * - BattleRoyalStartMulti
     - Not triggered when starting a battle royale
   * - BuildEventReceiveDailyBonus
     - Possible related to Nightmare 
   * - CastleStoryRead
     -
   * - CharaGetList
     -
   * - Clb01EventEntry
     - Opening the FEH event on an account that hasn't played it before
   * - CollectEventEntry
     -
   * - CollectEventGetEventData
     -
   * - DmodeDungeonSystemHalt
     - Related to :doc:`/dragalia/dmode_dungeon_user_halt`, which is called when suspending a Kaleidoscape run manually. Probably called when the app closes/phone goes to sleep to save progress in these instances
   * - DmodeReadStory
     - Unlocking a new Kaleidoscape story
   * - DreamAdventureClear
     -
   * - DreamAdventurePlay
     -
   * - DungeonRecordRecordMulti
     - Not triggered when finishing a co-op quest
   * - DungeonRetry
     - Not triggered when pressing retry on a quest
   * - DungeonSkipStartMultipleQuestAssignUnit
     -
   * - DungeonStartStartMultiAssignUnit
     - AssignUnit in other places refers to quests where you are forced to use a specific unit.
   * - EarnEventEntry
     - 
   * - EarnEventGetEventData
     -
   * - EarnEventReceiveEventPointReward
     -
   * - EventDamageGetTotalDamageHistory
     - Possibly related to the Satan event where players were awarded based on damage dealt
   * - EventDamageReceiveDamageReward
     - Possibly related to the Satan event where players were awarded based on damage dealt
   * - EventStoryRead
     - Not triggered from compendium stories or current active raid event stories, which use :doc:`/dragalia/quest_read_story` or :doc:`/dragalia/story_read`
   * - ExchangeGetUnitList
     -
   * - ExchangeSelectUnit
     -
   * - FortBuildAtOnce
     - Possibly from rushing a new build (as opposed to a level-up which triggers :doc:`/dragalia/fort_levelup_at_once`). New player rupie mines?
   * - FortBuildCancel
     - Cancelling a level-up
   * - GuildChatPostReport
     - 
   * - GuildInviteInviteReplyAllDeny
     - Replying to an invitation to join a guild
   * - GuildJoinReply
     - Replying to a request to join your guild
   * - GuildJoinReplyAllDeny
     - Replying to a request to join your guild
   * - GuildJoinRequestCancel
     -
   * - GuildPostReport
     -
   * - GuildSearchGetGuildDetail
     -
   * - InquiryReply
     - Nintendo customer support reply
   * - LoginPenaltyConfirm
     -
   * - MatchingGetRoomListByGuild
     -
   * - MatchingGetRoomListByLocation
     -
   * - MazeEventEntry
     -
   * - MazeEventGetEventData
     -
   * - MazeEventReceiveMazePointReward
     -
   * - MissionReceiveAlbumReward
     - `album` usually refers to the Encyclopaedia, but not triggered when receiving 
   * - MissionReceiveBeginnerReward
     - MissionReceive refers to endeavours (:doc:`/dragalia/mission_receive_daily_reward`, :doc:`/dragalia/mission_receive_normal_reward`, etc.)
   * - MissionReceiveMainStoryReward
     - MissionReceive refers to endeavours (:doc:`/dragalia/mission_receive_daily_reward`, :doc:`/dragalia/mission_receive_normal_reward`, etc.)
   * - MissionReceiveSpecialReward
     - MissionReceive refers to endeavours (:doc:`/dragalia/mission_receive_daily_reward`, :doc:`/dragalia/mission_receive_normal_reward`, etc.)
   * - MissionUnlockMainStoryGroup
     -
   * - OptionSetOption
     -
   * - QuestGetQuestClearPartyMulti
     - For solo, this corresponds to the 'preferred team' button (:doc:`/dragalia/quest_get_quest_clear_party`), and when clearing in co-op :doc:`/dragalia/quest_set_quest_clear_party_multi` is called, but I'm not aware of any way to access historical co-op teams?
   * - QuestSearchQuestClearPartyCharaMulti
     -
   * - QuestSearchQuestClearPartyMulti
     -
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
   * - SimpleEventEntry
     -
   * - SimpleEventGetEventData
     -
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
     - Not called when starting Mercurial Gauntlet, that's :doc:`/dragalia/wall_start_start`. AssignUnit elsewhere forces you to use a particular unit, but unaware of any similar functionality for MG.


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

Not possible to document
-------------------------

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
