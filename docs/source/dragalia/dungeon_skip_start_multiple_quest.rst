/dungeon_skip/start_multiple_quest
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887233407125661	Request-Time: 1662208632	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 249

Request body
----------------

.. code-block:: json

	{
	    "party_no": 2,
	    "request_quest_multiple_list": [
	        {
	            "quest_id": 201010104,
	            "play_count": 1,
	            "bet_count": 0
	        },
	        {
	            "quest_id": 202060104,
	            "play_count": 1,
	            "bet_count": 0
	        },
	        {
	            "quest_id": 202010103,
	            "play_count": 1,
	            "bet_count": 0
	        },
	        {
	            "quest_id": 203030104,
	            "play_count": 1,
	            "bet_count": 0
	        },
	        {
	            "quest_id": 211010102,
	            "play_count": 1,
	            "bet_count": 0
	        }
	    ],
	    "support_viewer_id": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 10109	Expires: Sat, 03 Sep 2022 12:37:21 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 12:37:21 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "ingame_result_data": {
	            "play_type": 1,
	            "reward_record": {
	                "drop_all": [
	                    {
	                        "type": 8,
	                        "id": 101001003,
	                        "quantity": 20,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 103001003,
	                        "quantity": 23,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 102001003,
	                        "quantity": 21,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 104001011,
	                        "quantity": 15,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 104001012,
	                        "quantity": 4,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 104001001,
	                        "quantity": 1,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202002002,
	                        "quantity": 4,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202002003,
	                        "quantity": 5,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 102001001,
	                        "quantity": 7,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 102001002,
	                        "quantity": 2,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 104002011,
	                        "quantity": 4,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 104002012,
	                        "quantity": 1,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 201002011,
	                        "quantity": 5,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202004002,
	                        "quantity": 1,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202004003,
	                        "quantity": 1,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202001002,
	                        "quantity": 240,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 103001001,
	                        "quantity": 6,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 201009001,
	                        "quantity": 240,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 201009002,
	                        "quantity": 40,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 201010011,
	                        "quantity": 80,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202005021,
	                        "quantity": 80,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202001001,
	                        "quantity": 280,
	                        "place": 0,
	                        "factor": 0.0
	                    }
	                ],
	                "first_clear_set": [],
	                "quest_bonus_list": [
	                    {
	                        "type": 8,
	                        "id": 101001003,
	                        "quantity": 50
	                    },
	                    {
	                        "type": 18,
	                        "id": 0,
	                        "quantity": 6000
	                    },
	                    {
	                        "type": 4,
	                        "id": 0,
	                        "quantity": 140800
	                    },
	                    {
	                        "type": 8,
	                        "id": 104001013,
	                        "quantity": 6
	                    },
	                    {
	                        "type": 8,
	                        "id": 102001002,
	                        "quantity": 8
	                    },
	                    {
	                        "type": 8,
	                        "id": 104002012,
	                        "quantity": 10
	                    },
	                    {
	                        "type": 8,
	                        "id": 201009002,
	                        "quantity": 240
	                    },
	                    {
	                        "type": 8,
	                        "id": 201010011,
	                        "quantity": 720
	                    }
	                ],
	                "reborn_bonus": [],
	                "weekly_limit_reward_list": [],
	                "challenge_quest_bonus_list": [],
	                "campaign_extra_reward_list": [],
	                "shop_quest_bonus_factor": 0.0,
	                "mission_complete": [],
	                "missions_clear_set": [],
	                "enemy_piece": [],
	                "take_coin": 34334,
	                "take_accumulate_point": 0,
	                "take_boost_accumulate_point": 0,
	                "player_level_up_fstone": 0,
	                "first_meeting": [],
	                "take_astral_item_quantity": 26,
	                "carry_bonus": []
	            },
	            "grow_record": {
	                "take_player_exp": 900,
	                "take_chara_exp": 10600,
	                "take_mana": 1693,
	                "bonus_factor": 1.0,
	                "mana_bonus_factor": 1.0,
	                "chara_grow_record": [
	                    {
	                        "chara_id": 10150504,
	                        "take_exp": 0
	                    },
	                    {
	                        "chara_id": 10540502,
	                        "take_exp": 0
	                    },
	                    {
	                        "chara_id": 10650505,
	                        "take_exp": 0
	                    },
	                    {
	                        "chara_id": 10750502,
	                        "take_exp": 10600
	                    }
	                ],
	                "chara_friendship_list": []
	            },
	            "start_time": 1662208640,
	            "end_time": 1662208640,
	            "current_play_count": 1,
	            "is_clear": 1,
	            "state": 5,
	            "is_host": 1,
	            "is_fever_time": 0,
	            "wave_count": 0,
	            "reborn_count": 0,
	            "helper_list": [],
	            "helper_detail_list": [],
	            "quest_party_setting_list": [
	                {
	                    "unit_no": 1,
	                    "chara_id": 10150504,
	                    "equip_dragon_key_id": 13594236,
	                    "equip_weapon_body_id": 30160501,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 32538,
	                    "equip_crest_slot_type_1_crest_id_1": 40050090,
	                    "equip_crest_slot_type_1_crest_id_2": 40050120,
	                    "equip_crest_slot_type_1_crest_id_3": 40050088,
	                    "equip_crest_slot_type_2_crest_id_1": 40040068,
	                    "equip_crest_slot_type_2_crest_id_2": 40040017,
	                    "equip_crest_slot_type_3_crest_id_1": 40090001,
	                    "equip_crest_slot_type_3_crest_id_2": 40090002,
	                    "edit_skill_1_chara_id": 0,
	                    "edit_skill_2_chara_id": 10550101
	                },
	                {
	                    "unit_no": 2,
	                    "chara_id": 10540502,
	                    "equip_dragon_key_id": 12554073,
	                    "equip_weapon_body_id": 30560501,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 49800,
	                    "equip_crest_slot_type_1_crest_id_1": 40050144,
	                    "equip_crest_slot_type_1_crest_id_2": 40050070,
	                    "equip_crest_slot_type_1_crest_id_3": 40050039,
	                    "equip_crest_slot_type_2_crest_id_1": 40040089,
	                    "equip_crest_slot_type_2_crest_id_2": 40040038,
	                    "equip_crest_slot_type_3_crest_id_1": 40090029,
	                    "equip_crest_slot_type_3_crest_id_2": 40090018,
	                    "edit_skill_1_chara_id": 10850402,
	                    "edit_skill_2_chara_id": 10140302
	                },
	                {
	                    "unit_no": 3,
	                    "chara_id": 10650505,
	                    "equip_dragon_key_id": 17598381,
	                    "equip_weapon_body_id": 30660501,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 49801,
	                    "equip_crest_slot_type_1_crest_id_1": 40050076,
	                    "equip_crest_slot_type_1_crest_id_2": 40050088,
	                    "equip_crest_slot_type_1_crest_id_3": 40050120,
	                    "equip_crest_slot_type_2_crest_id_1": 40040017,
	                    "equip_crest_slot_type_2_crest_id_2": 40040068,
	                    "equip_crest_slot_type_3_crest_id_1": 40090002,
	                    "equip_crest_slot_type_3_crest_id_2": 40090007,
	                    "edit_skill_1_chara_id": 10840501,
	                    "edit_skill_2_chara_id": 10440301
	                },
	                {
	                    "unit_no": 4,
	                    "chara_id": 10750502,
	                    "equip_dragon_key_id": 8296337,
	                    "equip_weapon_body_id": 30760501,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 47705,
	                    "equip_crest_slot_type_1_crest_id_1": 40050070,
	                    "equip_crest_slot_type_1_crest_id_2": 40050144,
	                    "equip_crest_slot_type_1_crest_id_3": 40050020,
	                    "equip_crest_slot_type_2_crest_id_1": 40040072,
	                    "equip_crest_slot_type_2_crest_id_2": 40040068,
	                    "equip_crest_slot_type_3_crest_id_1": 40090007,
	                    "equip_crest_slot_type_3_crest_id_2": 40090018,
	                    "edit_skill_1_chara_id": 10840501,
	                    "edit_skill_2_chara_id": 10440301
	                }
	            ],
	            "bonus_factor_list": [],
	            "scoring_enemy_point_list": [],
	            "score_mission_success_list": [],
	            "event_passive_up_list": [],
	            "clear_time": -1,
	            "is_best_clear_time": 0,
	            "converted_entity_list": [],
	            "dungeon_skip_type": 2
	        },
	        "time_attack_ranking_data": [],
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jay",
	                "level": 174,
	                "exp": 6179047,
	                "crystal": 13170,
	                "coin": 1661465596,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 394,
	                "main_party_no": 2,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 20846,
	                "mana_point": 8369464,
	                "dew_point": 741390,
	                "build_time_point": 1067,
	                "last_login_time": 1662204727,
	                "stamina_single": 53,
	                "last_stamina_single_update_time": 1662208640,
	                "stamina_single_surplus_second": 113,
	                "stamina_multi": 5,
	                "last_stamina_multi_update_time": 1662207177,
	                "stamina_multi_surplus_second": 1145,
	                "tutorial_status": 60999,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1003,
	                    1004,
	                    1005,
	                    1006,
	                    1007,
	                    1008,
	                    1009,
	                    1010,
	                    1011,
	                    1012,
	                    1013,
	                    1014,
	                    1015,
	                    1016,
	                    1017,
	                    1018,
	                    1019,
	                    1020,
	                    1021,
	                    1022,
	                    1023,
	                    1024,
	                    1025,
	                    1026,
	                    1027,
	                    1028,
	                    1029,
	                    1030
	                ],
	                "prologue_end_time": 1557120311,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1557120036
	            },
	            "quest_list": [
	                {
	                    "quest_id": 201010104,
	                    "state": 3,
	                    "is_mission_clear_1": 1,
	                    "is_mission_clear_2": 1,
	                    "is_mission_clear_3": 1,
	                    "play_count": 790,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640,
	                    "is_appear": 1,
	                    "best_clear_time": 53.4
	                },
	                {
	                    "quest_id": 202010103,
	                    "state": 3,
	                    "is_mission_clear_1": 1,
	                    "is_mission_clear_2": 1,
	                    "is_mission_clear_3": 1,
	                    "play_count": 435,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640,
	                    "is_appear": 1,
	                    "best_clear_time": 37.1
	                },
	                {
	                    "quest_id": 202060104,
	                    "state": 3,
	                    "is_mission_clear_1": 1,
	                    "is_mission_clear_2": 1,
	                    "is_mission_clear_3": 1,
	                    "play_count": 946,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640,
	                    "is_appear": 1,
	                    "best_clear_time": 31.7
	                },
	                {
	                    "quest_id": 203030104,
	                    "state": 3,
	                    "is_mission_clear_1": 1,
	                    "is_mission_clear_2": 1,
	                    "is_mission_clear_3": 1,
	                    "play_count": 347,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640,
	                    "is_appear": 1,
	                    "best_clear_time": 2.1
	                },
	                {
	                    "quest_id": 211010102,
	                    "state": 3,
	                    "is_mission_clear_1": 1,
	                    "is_mission_clear_2": 1,
	                    "is_mission_clear_3": 1,
	                    "play_count": 2,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640,
	                    "is_appear": 1,
	                    "best_clear_time": 24.5
	                }
	            ],
	            "quest_event_list": [
	                {
	                    "quest_event_id": 20101,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "quest_bonus_receive_count": 1,
	                    "quest_bonus_stack_count": 0,
	                    "quest_bonus_stack_time": 0,
	                    "quest_bonus_reserve_count": 0,
	                    "quest_bonus_reserve_time": 0,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640
	                },
	                {
	                    "quest_event_id": 20200,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "quest_bonus_receive_count": 1,
	                    "quest_bonus_stack_count": 0,
	                    "quest_bonus_stack_time": 0,
	                    "quest_bonus_reserve_count": 0,
	                    "quest_bonus_reserve_time": 0,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640
	                },
	                {
	                    "quest_event_id": 20206,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "quest_bonus_receive_count": 1,
	                    "quest_bonus_stack_count": 0,
	                    "quest_bonus_stack_time": 0,
	                    "quest_bonus_reserve_count": 0,
	                    "quest_bonus_reserve_time": 0,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640
	                },
	                {
	                    "quest_event_id": 20300,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "quest_bonus_receive_count": 1,
	                    "quest_bonus_stack_count": 0,
	                    "quest_bonus_stack_time": 0,
	                    "quest_bonus_reserve_count": 0,
	                    "quest_bonus_reserve_time": 0,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640
	                },
	                {
	                    "quest_event_id": 21100,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "quest_bonus_receive_count": 1,
	                    "quest_bonus_stack_count": 0,
	                    "quest_bonus_stack_time": 0,
	                    "quest_bonus_reserve_count": 0,
	                    "quest_bonus_reserve_time": 0,
	                    "last_daily_reset_time": 1662208640,
	                    "last_weekly_reset_time": 1662208640
	                }
	            ],
	            "chara_list": [
	                {
	                    "chara_id": 10150504,
	                    "rarity": 5,
	                    "exp": 1191950,
	                    "level": 80,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 100,
	                    "attack_plus_count": 100,
	                    "limit_break_count": 4,
	                    "is_new": 1,
	                    "gettime": 1648381239,
	                    "skill_1_level": 3,
	                    "skill_2_level": 2,
	                    "ability_1_level": 2,
	                    "ability_2_level": 2,
	                    "ability_3_level": 2,
	                    "burst_attack_level": 2,
	                    "combo_buildup_count": 0,
	                    "hp": 752,
	                    "attack": 506,
	                    "ex_ability_level": 5,
	                    "ex_ability_2_level": 5,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [
	                        1,
	                        2,
	                        3,
	                        4,
	                        5,
	                        6,
	                        7,
	                        8,
	                        9,
	                        10,
	                        11,
	                        12,
	                        13,
	                        14,
	                        15,
	                        16,
	                        17,
	                        18,
	                        19,
	                        20,
	                        21,
	                        22,
	                        23,
	                        24,
	                        25,
	                        26,
	                        27,
	                        28,
	                        29,
	                        30,
	                        31,
	                        32,
	                        33,
	                        34,
	                        35,
	                        36,
	                        37,
	                        38,
	                        39,
	                        40,
	                        41,
	                        42,
	                        43,
	                        44,
	                        45,
	                        46,
	                        47,
	                        48,
	                        49,
	                        50
	                    ],
	                    "list_view_flag": 1
	                },
	                {
	                    "chara_id": 10540502,
	                    "rarity": 5,
	                    "exp": 8866950,
	                    "level": 100,
	                    "additional_max_level": 20,
	                    "hp_plus_count": 100,
	                    "attack_plus_count": 100,
	                    "limit_break_count": 5,
	                    "is_new": 1,
	                    "gettime": 1570177099,
	                    "skill_1_level": 4,
	                    "skill_2_level": 3,
	                    "ability_1_level": 3,
	                    "ability_2_level": 3,
	                    "ability_3_level": 2,
	                    "burst_attack_level": 2,
	                    "combo_buildup_count": 1,
	                    "hp": 961,
	                    "attack": 537,
	                    "ex_ability_level": 5,
	                    "ex_ability_2_level": 5,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 1,
	                    "mana_circle_piece_id_list": [
	                        1,
	                        2,
	                        3,
	                        4,
	                        5,
	                        6,
	                        7,
	                        8,
	                        9,
	                        10,
	                        11,
	                        12,
	                        13,
	                        14,
	                        15,
	                        16,
	                        17,
	                        18,
	                        19,
	                        20,
	                        21,
	                        22,
	                        23,
	                        24,
	                        25,
	                        26,
	                        27,
	                        28,
	                        29,
	                        30,
	                        31,
	                        32,
	                        33,
	                        34,
	                        35,
	                        36,
	                        37,
	                        38,
	                        39,
	                        40,
	                        41,
	                        42,
	                        43,
	                        44,
	                        45,
	                        46,
	                        47,
	                        48,
	                        49,
	                        50,
	                        51,
	                        52,
	                        53,
	                        54,
	                        55,
	                        56,
	                        57,
	                        58,
	                        59,
	                        60,
	                        61,
	                        62,
	                        63,
	                        64,
	                        65,
	                        66,
	                        67,
	                        68,
	                        69,
	                        70
	                    ],
	                    "list_view_flag": 1
	                },
	                {
	                    "chara_id": 10650505,
	                    "rarity": 5,
	                    "exp": 1191950,
	                    "level": 80,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 100,
	                    "attack_plus_count": 100,
	                    "limit_break_count": 4,
	                    "is_new": 1,
	                    "gettime": 1635931682,
	                    "skill_1_level": 3,
	                    "skill_2_level": 2,
	                    "ability_1_level": 2,
	                    "ability_2_level": 2,
	                    "ability_3_level": 2,
	                    "burst_attack_level": 2,
	                    "combo_buildup_count": 0,
	                    "hp": 801,
	                    "attack": 472,
	                    "ex_ability_level": 5,
	                    "ex_ability_2_level": 5,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 1,
	                    "mana_circle_piece_id_list": [
	                        1,
	                        2,
	                        3,
	                        4,
	                        5,
	                        6,
	                        7,
	                        8,
	                        9,
	                        10,
	                        11,
	                        12,
	                        13,
	                        14,
	                        15,
	                        16,
	                        17,
	                        18,
	                        19,
	                        20,
	                        21,
	                        22,
	                        23,
	                        24,
	                        25,
	                        26,
	                        27,
	                        28,
	                        29,
	                        30,
	                        31,
	                        32,
	                        33,
	                        34,
	                        35,
	                        36,
	                        37,
	                        38,
	                        39,
	                        40,
	                        41,
	                        42,
	                        43,
	                        44,
	                        45,
	                        46,
	                        47,
	                        48,
	                        49,
	                        50
	                    ],
	                    "list_view_flag": 1
	                },
	                {
	                    "chara_id": 10750502,
	                    "rarity": 5,
	                    "exp": 1238230,
	                    "level": 80,
	                    "additional_max_level": 5,
	                    "hp_plus_count": 100,
	                    "attack_plus_count": 100,
	                    "limit_break_count": 5,
	                    "is_new": 1,
	                    "gettime": 1569827126,
	                    "skill_1_level": 3,
	                    "skill_2_level": 2,
	                    "ability_1_level": 3,
	                    "ability_2_level": 2,
	                    "ability_3_level": 2,
	                    "burst_attack_level": 2,
	                    "combo_buildup_count": 0,
	                    "hp": 790,
	                    "attack": 492,
	                    "ex_ability_level": 5,
	                    "ex_ability_2_level": 5,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [
	                        1,
	                        2,
	                        3,
	                        4,
	                        5,
	                        6,
	                        7,
	                        8,
	                        9,
	                        10,
	                        11,
	                        12,
	                        13,
	                        14,
	                        15,
	                        16,
	                        17,
	                        18,
	                        19,
	                        20,
	                        21,
	                        22,
	                        23,
	                        24,
	                        25,
	                        26,
	                        27,
	                        28,
	                        29,
	                        30,
	                        31,
	                        32,
	                        33,
	                        34,
	                        35,
	                        36,
	                        37,
	                        38,
	                        39,
	                        40,
	                        41,
	                        42,
	                        43,
	                        44,
	                        45,
	                        46,
	                        47,
	                        48,
	                        49,
	                        50,
	                        51,
	                        52
	                    ],
	                    "list_view_flag": 1
	                }
	            ],
	            "friend_notice": {
	                "friend_new_count": 0,
	                "apply_new_count": 0
	            },
	            "material_list": [
	                {
	                    "material_id": 101001003,
	                    "quantity": 834
	                },
	                {
	                    "material_id": 102001001,
	                    "quantity": 32366
	                },
	                {
	                    "material_id": 102001002,
	                    "quantity": 13804
	                },
	                {
	                    "material_id": 102001003,
	                    "quantity": 19090
	                },
	                {
	                    "material_id": 103001001,
	                    "quantity": 835
	                },
	                {
	                    "material_id": 103001003,
	                    "quantity": 60242
	                },
	                {
	                    "material_id": 104001001,
	                    "quantity": 31
	                },
	                {
	                    "material_id": 104001011,
	                    "quantity": 479
	                },
	                {
	                    "material_id": 104001012,
	                    "quantity": 278
	                },
	                {
	                    "material_id": 104002011,
	                    "quantity": 275
	                },
	                {
	                    "material_id": 104002012,
	                    "quantity": 230
	                },
	                {
	                    "material_id": 201002011,
	                    "quantity": 167
	                },
	                {
	                    "material_id": 201009001,
	                    "quantity": 42393
	                },
	                {
	                    "material_id": 201009002,
	                    "quantity": 11822
	                },
	                {
	                    "material_id": 201010011,
	                    "quantity": 167
	                },
	                {
	                    "material_id": 202001001,
	                    "quantity": 8414
	                },
	                {
	                    "material_id": 202001002,
	                    "quantity": 57935
	                },
	                {
	                    "material_id": 202002002,
	                    "quantity": 42712
	                },
	                {
	                    "material_id": 202002003,
	                    "quantity": 50042
	                },
	                {
	                    "material_id": 202004002,
	                    "quantity": 5284
	                },
	                {
	                    "material_id": 202004003,
	                    "quantity": 28
	                },
	                {
	                    "material_id": 202005021,
	                    "quantity": 3915
	                }
	            ],
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 71
	            },
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "over_discard_entity_list": [
	                {
	                    "entity_type": 26,
	                    "entity_id": 10101,
	                    "entity_quantity": 5
	                },
	                {
	                    "entity_type": 26,
	                    "entity_id": 10101,
	                    "entity_quantity": 5
	                },
	                {
	                    "entity_type": 26,
	                    "entity_id": 10101,
	                    "entity_quantity": 5
	                },
	                {
	                    "entity_type": 26,
	                    "entity_id": 10101,
	                    "entity_quantity": 6
	                },
	                {
	                    "entity_type": 26,
	                    "entity_id": 10101,
	                    "entity_quantity": 5
	                }
	            ],
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
