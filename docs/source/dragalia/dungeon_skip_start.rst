/dungeon_skip/start
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 1a5a3cb1aa568946e14a539ae29b79f74c58858365dc2bb0dbe8d8e5150215ed	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886511953283240	Request-Time: 1662165637	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 67

Request body
----------------

.. code-block:: json

	{
	    "quest_id": 100100101,
	    "party_no": 6,
	    "support_viewer_id": 0,
	    "play_count": 1,
	    "bet_count": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 5941	Expires: Sat, 03 Sep 2022 00:40:39 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 00:40:39 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "ingame_result_data": {
	            "dungeon_key": "3b1c552c2f1fdf192d289d2699e896f94cb43be7",
	            "play_type": 1,
	            "quest_id": 100100101,
	            "reward_record": {
	                "drop_all": [
	                    {
	                        "type": 8,
	                        "id": 104001051,
	                        "quantity": 4,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 101001002,
	                        "quantity": 5,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 103001001,
	                        "quantity": 1,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202001001,
	                        "quantity": 2,
	                        "place": 0,
	                        "factor": 0.0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202001002,
	                        "quantity": 1,
	                        "place": 0,
	                        "factor": 0.0
	                    }
	                ],
	                "first_clear_set": [],
	                "quest_bonus_list": [],
	                "reborn_bonus": [],
	                "weekly_limit_reward_list": [],
	                "challenge_quest_bonus_list": [],
	                "campaign_extra_reward_list": [],
	                "shop_quest_bonus_factor": 0.0,
	                "mission_complete": [],
	                "missions_clear_set": [],
	                "enemy_piece": [],
	                "take_coin": 550,
	                "take_accumulate_point": 0,
	                "take_boost_accumulate_point": 0,
	                "player_level_up_fstone": 0,
	                "first_meeting": [],
	                "take_astral_item_quantity": 3,
	                "carry_bonus": []
	            },
	            "grow_record": {
	                "take_player_exp": 130,
	                "take_chara_exp": 1040,
	                "take_mana": 170,
	                "bonus_factor": 1.0,
	                "mana_bonus_factor": 1.0,
	                "chara_grow_record": [
	                    {
	                        "chara_id": 10950503,
	                        "take_exp": 0
	                    },
	                    {
	                        "chara_id": 10430501,
	                        "take_exp": 1040
	                    },
	                    {
	                        "chara_id": 10530501,
	                        "take_exp": 1040
	                    },
	                    {
	                        "chara_id": 10730501,
	                        "take_exp": 1040
	                    }
	                ],
	                "chara_friendship_list": []
	            },
	            "start_time": 1662165639,
	            "end_time": 1662165639,
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
	                    "chara_id": 10950503,
	                    "equip_dragon_key_id": 19273098,
	                    "equip_weapon_body_id": 0,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
	                    "edit_skill_1_chara_id": 10840501,
	                    "edit_skill_2_chara_id": 10440301
	                },
	                {
	                    "unit_no": 2,
	                    "chara_id": 10430501,
	                    "equip_dragon_key_id": 19273091,
	                    "equip_weapon_body_id": 0,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
	                    "edit_skill_1_chara_id": 10840501,
	                    "edit_skill_2_chara_id": 10440301
	                },
	                {
	                    "unit_no": 3,
	                    "chara_id": 10530501,
	                    "equip_dragon_key_id": 19273094,
	                    "equip_weapon_body_id": 0,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
	                    "edit_skill_1_chara_id": 10840501,
	                    "edit_skill_2_chara_id": 10440301
	                },
	                {
	                    "unit_no": 4,
	                    "chara_id": 10730501,
	                    "equip_dragon_key_id": 19273107,
	                    "equip_weapon_body_id": 0,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
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
	            "dungeon_skip_type": 1
	        },
	        "time_attack_ranking_data": [],
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 60,
	                "exp": 70120,
	                "crystal": 9679,
	                "coin": 2000502688,
	                "max_dragon_quantity": 185,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 323,
	                "main_party_no": 6,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 20841,
	                "mana_point": 54093,
	                "dew_point": 3170,
	                "build_time_point": 10,
	                "last_login_time": 1662158090,
	                "stamina_single": 994,
	                "last_stamina_single_update_time": 1662165639,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 99,
	                "last_stamina_multi_update_time": 1662165243,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 60999,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1007,
	                    1009,
	                    1010,
	                    1012,
	                    1014,
	                    1015,
	                    1019,
	                    1020,
	                    1021,
	                    1022,
	                    1023,
	                    1024,
	                    1027
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 1662159858,
	                "create_time": 1661897736
	            },
	            "party_power_data": {
	                "max_party_power": 4782
	            },
	            "quest_list": [
	                {
	                    "quest_id": 100100101,
	                    "state": 3,
	                    "is_mission_clear_1": 1,
	                    "is_mission_clear_2": 1,
	                    "is_mission_clear_3": 1,
	                    "play_count": 2,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "last_daily_reset_time": 1662165639,
	                    "last_weekly_reset_time": 1662165639,
	                    "is_appear": 1,
	                    "best_clear_time": -1.0
	                }
	            ],
	            "chara_list": [
	                {
	                    "chara_id": 10430501,
	                    "rarity": 3,
	                    "exp": 3680,
	                    "level": 15,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 0,
	                    "is_new": 0,
	                    "gettime": 1661976583,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "ability_1_level": 0,
	                    "ability_2_level": 0,
	                    "ability_3_level": 0,
	                    "burst_attack_level": 0,
	                    "combo_buildup_count": 0,
	                    "hp": 106,
	                    "attack": 74,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [],
	                    "list_view_flag": 1
	                },
	                {
	                    "chara_id": 10530501,
	                    "rarity": 3,
	                    "exp": 3680,
	                    "level": 15,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 0,
	                    "is_new": 0,
	                    "gettime": 1661976585,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "ability_1_level": 0,
	                    "ability_2_level": 0,
	                    "ability_3_level": 0,
	                    "burst_attack_level": 0,
	                    "combo_buildup_count": 0,
	                    "hp": 106,
	                    "attack": 73,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [],
	                    "list_view_flag": 1
	                },
	                {
	                    "chara_id": 10730501,
	                    "rarity": 3,
	                    "exp": 3680,
	                    "level": 15,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 0,
	                    "is_new": 0,
	                    "gettime": 1661976589,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "ability_1_level": 0,
	                    "ability_2_level": 0,
	                    "ability_3_level": 0,
	                    "burst_attack_level": 0,
	                    "combo_buildup_count": 0,
	                    "hp": 111,
	                    "attack": 70,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [],
	                    "list_view_flag": 1
	                },
	                {
	                    "chara_id": 10950503,
	                    "rarity": 5,
	                    "exp": 1191950,
	                    "level": 80,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 4,
	                    "is_new": 1,
	                    "gettime": 1661976624,
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
	                }
	            ],
	            "friend_notice": {
	                "friend_new_count": 0,
	                "apply_new_count": 0
	            },
	            "astral_item_list": [
	                {
	                    "astral_item_id": 10101,
	                    "quantity": 24
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 101001002,
	                    "quantity": 34
	                },
	                {
	                    "material_id": 103001001,
	                    "quantity": 17
	                },
	                {
	                    "material_id": 104001051,
	                    "quantity": 114
	                },
	                {
	                    "material_id": 202001001,
	                    "quantity": 323
	                },
	                {
	                    "material_id": 202001002,
	                    "quantity": 5011
	                }
	            ],
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
