/dungeon_start/start
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com
	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
	Accept: */*
	Accept-Encoding: deflate, gzip
	App-Ver: 2.19.0
	Device: 2
	Platform: 2
	Carrier: OnePlus
	DeviceId: <device_id>
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883462224513224
	Request-Time: 1661983858
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 101


Request body
----------------

.. code-block:: json

	{
	    "quest_id": 100010101,
	    "party_no": 0,
	    "party_no_list": [
	        1
	    ],
	    "bet_count": 0,
	    "repeat_state": 0,
	    "support_viewer_id": 0,
	    "repeat_setting": null
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 7340
	Expires: Wed, 31 Aug 2022 22:11:00 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:11:00 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "ingame_data": {
	            "viewer_id": 66709573935,
	            "dungeon_key": "ce6bcba35fbd0ce406e326f1ce4e3dd13bdf9ef3",
	            "dungeon_type": 1,
	            "play_type": 1,
	            "quest_id": 100010101,
	            "is_host": 1,
	            "continue_limit": 3,
	            "reborn_limit": 3,
	            "start_time": 1661983860,
	            "party_info": {
	                "party_unit_list": [
	                    {
	                        "position": 1,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10140101,
	                            "rarity": 4,
	                            "exp": 0,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976574,
	                            "level": 1,
	                            "additional_max_level": 0,
	                            "hp": 60,
	                            "attack": 40,
	                            "skill_1_level": 1,
	                            "skill_2_level": 0,
	                            "ability_1_level": 0,
	                            "ability_2_level": 0,
	                            "ability_3_level": 0,
	                            "ex_ability_level": 1,
	                            "ex_ability_2_level": 1,
	                            "burst_attack_level": 0,
	                            "combo_buildup_count": 0,
	                            "is_temporary": 0,
	                            "is_unlock_edit_skill": 1
	                        },
	                        "dragon_data": {
	                            "dragon_id": 20040103,
	                            "dragon_key_id": 19273109,
	                            "level": 1,
	                            "hp": 29,
	                            "attack": 10,
	                            "is_lock": 0,
	                            "is_new": 1,
	                            "skill_1_level": 1,
	                            "ability_1_level": 1,
	                            "ability_2_level": 0,
	                            "gettime": 1661976618,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "limit_break_count": 0,
	                            "exp": 0
	                        },
	                        "weapon_skin_data": [],
	                        "weapon_body_data": {
	                            "weapon_body_id": 30129901,
	                            "buildup_count": 0,
	                            "limit_break_count": 0,
	                            "limit_over_count": 0,
	                            "equipable_count": 1,
	                            "additional_crest_slot_type_1_count": 0,
	                            "additional_crest_slot_type_2_count": 0,
	                            "additional_crest_slot_type_3_count": 0,
	                            "additional_effect_count": 0,
	                            "skill_no": 0,
	                            "skill_level": 0,
	                            "ability_1_level": 0,
	                            "ability_2_level": 0
	                        },
	                        "crest_slot_type_1_crest_list": [],
	                        "crest_slot_type_2_crest_list": [],
	                        "crest_slot_type_3_crest_list": [],
	                        "talisman_data": [],
	                        "edit_skill_1_chara_data": [],
	                        "edit_skill_2_chara_data": [],
	                        "dragon_reliability_level": 1,
	                        "game_weapon_passive_ability_list": []
	                    },
	                    {
	                        "position": 2,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10230101,
	                            "rarity": 3,
	                            "exp": 0,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976576,
	                            "level": 1,
	                            "additional_max_level": 0,
	                            "hp": 41,
	                            "attack": 29,
	                            "skill_1_level": 1,
	                            "skill_2_level": 0,
	                            "ability_1_level": 0,
	                            "ability_2_level": 0,
	                            "ability_3_level": 0,
	                            "ex_ability_level": 1,
	                            "ex_ability_2_level": 1,
	                            "burst_attack_level": 0,
	                            "combo_buildup_count": 0,
	                            "is_temporary": 0,
	                            "is_unlock_edit_skill": 0
	                        },
	                        "dragon_data": {
	                            "dragon_id": 20040103,
	                            "dragon_key_id": 19273108,
	                            "level": 1,
	                            "hp": 29,
	                            "attack": 10,
	                            "is_lock": 0,
	                            "is_new": 1,
	                            "skill_1_level": 1,
	                            "ability_1_level": 1,
	                            "ability_2_level": 0,
	                            "gettime": 1661976618,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "limit_break_count": 0,
	                            "exp": 0
	                        },
	                        "weapon_skin_data": [],
	                        "weapon_body_data": [],
	                        "crest_slot_type_1_crest_list": [],
	                        "crest_slot_type_2_crest_list": [],
	                        "crest_slot_type_3_crest_list": [],
	                        "talisman_data": [],
	                        "edit_skill_1_chara_data": [],
	                        "edit_skill_2_chara_data": [],
	                        "dragon_reliability_level": 1,
	                        "game_weapon_passive_ability_list": []
	                    },
	                    {
	                        "position": 3,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10630101,
	                            "rarity": 3,
	                            "exp": 0,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976586,
	                            "level": 1,
	                            "additional_max_level": 0,
	                            "hp": 42,
	                            "attack": 27,
	                            "skill_1_level": 1,
	                            "skill_2_level": 0,
	                            "ability_1_level": 0,
	                            "ability_2_level": 0,
	                            "ability_3_level": 0,
	                            "ex_ability_level": 1,
	                            "ex_ability_2_level": 1,
	                            "burst_attack_level": 0,
	                            "combo_buildup_count": 0,
	                            "is_temporary": 0,
	                            "is_unlock_edit_skill": 0
	                        },
	                        "dragon_data": [],
	                        "weapon_skin_data": [],
	                        "weapon_body_data": [],
	                        "crest_slot_type_1_crest_list": [],
	                        "crest_slot_type_2_crest_list": [],
	                        "crest_slot_type_3_crest_list": [],
	                        "talisman_data": [],
	                        "edit_skill_1_chara_data": [],
	                        "edit_skill_2_chara_data": [],
	                        "dragon_reliability_level": 0,
	                        "game_weapon_passive_ability_list": []
	                    },
	                    {
	                        "position": 4,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10830101,
	                            "rarity": 3,
	                            "exp": 0,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976590,
	                            "level": 1,
	                            "additional_max_level": 0,
	                            "hp": 45,
	                            "attack": 26,
	                            "skill_1_level": 1,
	                            "skill_2_level": 0,
	                            "ability_1_level": 0,
	                            "ability_2_level": 0,
	                            "ability_3_level": 0,
	                            "ex_ability_level": 1,
	                            "ex_ability_2_level": 1,
	                            "burst_attack_level": 0,
	                            "combo_buildup_count": 0,
	                            "is_temporary": 0,
	                            "is_unlock_edit_skill": 0
	                        },
	                        "dragon_data": {
	                            "dragon_id": 20040102,
	                            "dragon_key_id": 19273093,
	                            "level": 1,
	                            "hp": 29,
	                            "attack": 9,
	                            "is_lock": 0,
	                            "is_new": 1,
	                            "skill_1_level": 1,
	                            "ability_1_level": 1,
	                            "ability_2_level": 0,
	                            "gettime": 1661976618,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "limit_break_count": 0,
	                            "exp": 0
	                        },
	                        "weapon_skin_data": [],
	                        "weapon_body_data": [],
	                        "crest_slot_type_1_crest_list": [],
	                        "crest_slot_type_2_crest_list": [],
	                        "crest_slot_type_3_crest_list": [],
	                        "talisman_data": [],
	                        "edit_skill_1_chara_data": [],
	                        "edit_skill_2_chara_data": [],
	                        "dragon_reliability_level": 1,
	                        "game_weapon_passive_ability_list": []
	                    }
	                ],
	                "fort_bonus_list": {
	                    "param_bonus": [
	                        {
	                            "weapon_type": 1,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 2,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 3,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 4,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 5,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 6,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 7,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 8,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 9,
	                            "hp": 0,
	                            "attack": 0
	                        }
	                    ],
	                    "param_bonus_by_weapon": [
	                        {
	                            "weapon_type": 1,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 2,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 3,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 4,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 5,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 6,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 7,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 8,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "weapon_type": 9,
	                            "hp": 0,
	                            "attack": 0
	                        }
	                    ],
	                    "element_bonus": [
	                        {
	                            "elemental_type": 1,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 2,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 3,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 4,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 5,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 99,
	                            "hp": 0,
	                            "attack": 0
	                        }
	                    ],
	                    "chara_bonus_by_album": [
	                        {
	                            "elemental_type": 1,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 2,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 3,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 4,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 5,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 99,
	                            "hp": 0,
	                            "attack": 0
	                        }
	                    ],
	                    "all_bonus": {
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    "dragon_bonus": [
	                        {
	                            "elemental_type": 1,
	                            "dragon_bonus": 0,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 2,
	                            "dragon_bonus": 0,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 3,
	                            "dragon_bonus": 0,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 4,
	                            "dragon_bonus": 0,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 5,
	                            "dragon_bonus": 0,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 99,
	                            "dragon_bonus": 0,
	                            "hp": 0,
	                            "attack": 0
	                        }
	                    ],
	                    "dragon_bonus_by_album": [
	                        {
	                            "elemental_type": 1,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 2,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 3,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 4,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 5,
	                            "hp": 0,
	                            "attack": 0
	                        },
	                        {
	                            "elemental_type": 99,
	                            "hp": 0,
	                            "attack": 0
	                        }
	                    ],
	                    "dragon_time_bonus": {
	                        "dragon_time_bonus": 0
	                    }
	                },
	                "event_boost": [],
	                "event_passive_grow_list": []
	            },
	            "area_info_list": [
	                {
	                    "scene_path": "Main/01/MAIN_01_0101_01",
	                    "area_name": "MAIN_01_0101_01"
	                },
	                {
	                    "scene_path": "Boss/BG001_5001_00/BG001_5001_00_00",
	                    "area_name": "MAIN_01_0101_02"
	                }
	            ],
	            "use_stone": 50,
	            "is_fever_time": 0,
	            "repeat_state": 0,
	            "is_use_event_chara_ability": 0,
	            "event_ability_chara_list": [],
	            "is_bot_tutorial": 0,
	            "is_receivable_carry_bonus": 0,
	            "first_clear_viewer_id_list": [],
	            "multi_disconnect_type": 0
	        },
	        "ingame_quest_data": {
	            "quest_id": 100010101,
	            "play_count": 0,
	            "is_mission_clear_1": 0,
	            "is_mission_clear_2": 0,
	            "is_mission_clear_3": 0
	        },
	        "odds_info": {
	            "area_index": 0,
	            "reaction_obj_count": 1,
	            "drop_obj": [
	                {
	                    "drop_list": [
	                        {
	                            "type": 13,
	                            "id": 1001,
	                            "quantity": 1,
	                            "place": 0
	                        }
	                    ],
	                    "obj_id": 1,
	                    "obj_type": 2,
	                    "is_rare": 0
	                },
	                {
	                    "drop_list": [
	                        {
	                            "type": 13,
	                            "id": 1001,
	                            "quantity": 1,
	                            "place": 0
	                        }
	                    ],
	                    "obj_id": 2,
	                    "obj_type": 2,
	                    "is_rare": 0
	                },
	                {
	                    "drop_list": [
	                        {
	                            "type": 13,
	                            "id": 1001,
	                            "quantity": 1,
	                            "place": 0
	                        }
	                    ],
	                    "obj_id": 4,
	                    "obj_type": 2,
	                    "is_rare": 0
	                },
	                {
	                    "drop_list": [],
	                    "obj_id": 5,
	                    "obj_type": 2,
	                    "is_rare": 0
	                },
	                {
	                    "drop_list": [
	                        {
	                            "type": 8,
	                            "id": 104001031,
	                            "quantity": 1,
	                            "place": 0
	                        }
	                    ],
	                    "obj_id": 3,
	                    "obj_type": 1,
	                    "is_rare": 0
	                }
	            ],
	            "enemy": [
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 2,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 0
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 1,
	                            "mana": 0
	                        }
	                    ],
	                    "enemy_idx": 1
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 2,
	                            "mana": 0
	                        }
	                    ],
	                    "enemy_idx": 2
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 0,
	                            "mana": 0
	                        }
	                    ],
	                    "enemy_idx": 3
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 2,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 4
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 1,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 5
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 0,
	                            "mana": 0
	                        }
	                    ],
	                    "enemy_idx": 6
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 1,
	                            "mana": 0
	                        }
	                    ],
	                    "enemy_idx": 7
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 2,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 8
	                },
	                {
	                    "param_id": 100010102,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 2,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 9
	                },
	                {
	                    "param_id": 100010113,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 1,
	                            "mana": 0
	                        }
	                    ],
	                    "enemy_idx": 10
	                }
	            ],
	            "grade": []
	        },
	        "update_data_list": {
	            "quest_list": [
	                {
	                    "quest_id": 100010101,
	                    "state": 2,
	                    "is_mission_clear_1": 0,
	                    "is_mission_clear_2": 0,
	                    "is_mission_clear_3": 0,
	                    "play_count": 0,
	                    "daily_play_count": 0,
	                    "weekly_play_count": 0,
	                    "last_daily_reset_time": 0,
	                    "last_weekly_reset_time": 0,
	                    "is_appear": 1,
	                    "best_clear_time": -1.0
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
