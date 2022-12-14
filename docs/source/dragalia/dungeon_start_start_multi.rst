/dungeon_start/start_multi
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
	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886446119487746
	Request-Time: 1662161713
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 41


Request body
----------------

.. code-block:: json

	{
	    "quest_id": 204550301,
	    "party_no": 0,
	    "party_no_list": [
	        6
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 8072
	Expires: Fri, 02 Sep 2022 23:35:15 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:35:15 GMT
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
	            "dungeon_key": "fbc68f66feee78a89fe124ac69c2e73d4bb9e117",
	            "dungeon_type": 2,
	            "play_type": 2,
	            "quest_id": 204550301,
	            "is_host": 1,
	            "continue_limit": 0,
	            "reborn_limit": 0,
	            "start_time": 1662161714,
	            "party_info": {
	                "party_unit_list": [
	                    {
	                        "position": 1,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10950503,
	                            "rarity": 5,
	                            "exp": 1191950,
	                            "is_new": 1,
	                            "limit_break_count": 4,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976624,
	                            "level": 80,
	                            "additional_max_level": 0,
	                            "hp": 752,
	                            "attack": 506,
	                            "skill_1_level": 3,
	                            "skill_2_level": 2,
	                            "ability_1_level": 2,
	                            "ability_2_level": 2,
	                            "ability_3_level": 2,
	                            "ex_ability_level": 5,
	                            "ex_ability_2_level": 5,
	                            "burst_attack_level": 2,
	                            "combo_buildup_count": 0,
	                            "is_temporary": 0,
	                            "is_unlock_edit_skill": 0
	                        },
	                        "dragon_data": {
	                            "dragon_id": 20040502,
	                            "dragon_key_id": 19273098,
	                            "level": 28,
	                            "hp": 120,
	                            "attack": 42,
	                            "is_lock": 0,
	                            "is_new": 1,
	                            "skill_1_level": 1,
	                            "ability_1_level": 1,
	                            "ability_2_level": 0,
	                            "gettime": 1661976618,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "limit_break_count": 0,
	                            "exp": 41150
	                        },
	                        "weapon_skin_data": [],
	                        "weapon_body_data": [],
	                        "crest_slot_type_1_crest_list": [],
	                        "crest_slot_type_2_crest_list": [],
	                        "crest_slot_type_3_crest_list": [],
	                        "talisman_data": [],
	                        "edit_skill_1_chara_data": {
	                            "chara_id": 10840501,
	                            "edit_skill_level": 1
	                        },
	                        "edit_skill_2_chara_data": {
	                            "chara_id": 10440301,
	                            "edit_skill_level": 1
	                        },
	                        "dragon_reliability_level": 1,
	                        "game_weapon_passive_ability_list": []
	                    },
	                    {
	                        "position": 2,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10430501,
	                            "rarity": 3,
	                            "exp": 640,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976583,
	                            "level": 7,
	                            "additional_max_level": 0,
	                            "hp": 69,
	                            "attack": 49,
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
	                            "dragon_id": 20040502,
	                            "dragon_key_id": 19273091,
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
	                        "edit_skill_1_chara_data": {
	                            "chara_id": 10840501,
	                            "edit_skill_level": 1
	                        },
	                        "edit_skill_2_chara_data": {
	                            "chara_id": 10440301,
	                            "edit_skill_level": 1
	                        },
	                        "dragon_reliability_level": 1,
	                        "game_weapon_passive_ability_list": []
	                    },
	                    {
	                        "position": 3,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10530501,
	                            "rarity": 3,
	                            "exp": 640,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976585,
	                            "level": 7,
	                            "additional_max_level": 0,
	                            "hp": 69,
	                            "attack": 47,
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
	                            "dragon_id": 20030503,
	                            "dragon_key_id": 19273094,
	                            "level": 1,
	                            "hp": 18,
	                            "attack": 6,
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
	                        "edit_skill_1_chara_data": {
	                            "chara_id": 10840501,
	                            "edit_skill_level": 1
	                        },
	                        "edit_skill_2_chara_data": {
	                            "chara_id": 10440301,
	                            "edit_skill_level": 1
	                        },
	                        "dragon_reliability_level": 1,
	                        "game_weapon_passive_ability_list": []
	                    },
	                    {
	                        "position": 4,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10730501,
	                            "rarity": 3,
	                            "exp": 640,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976589,
	                            "level": 7,
	                            "additional_max_level": 0,
	                            "hp": 73,
	                            "attack": 46,
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
	                            "dragon_id": 20030503,
	                            "dragon_key_id": 19273107,
	                            "level": 1,
	                            "hp": 18,
	                            "attack": 6,
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
	                        "edit_skill_1_chara_data": {
	                            "chara_id": 10840501,
	                            "edit_skill_level": 1
	                        },
	                        "edit_skill_2_chara_data": {
	                            "chara_id": 10440301,
	                            "edit_skill_level": 1
	                        },
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
	                            "hp": 0.8,
	                            "attack": 0.8
	                        },
	                        {
	                            "elemental_type": 2,
	                            "hp": 0.7,
	                            "attack": 0.7
	                        },
	                        {
	                            "elemental_type": 3,
	                            "hp": 0.9,
	                            "attack": 0.9
	                        },
	                        {
	                            "elemental_type": 4,
	                            "hp": 0.8,
	                            "attack": 0.8
	                        },
	                        {
	                            "elemental_type": 5,
	                            "hp": 0.7,
	                            "attack": 0.7
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
	                            "hp": 0.5,
	                            "attack": 0.5
	                        },
	                        {
	                            "elemental_type": 2,
	                            "hp": 0.3,
	                            "attack": 0.3
	                        },
	                        {
	                            "elemental_type": 3,
	                            "hp": 0.5,
	                            "attack": 0.5
	                        },
	                        {
	                            "elemental_type": 4,
	                            "hp": 0.3,
	                            "attack": 0.3
	                        },
	                        {
	                            "elemental_type": 5,
	                            "hp": 0.3,
	                            "attack": 0.3
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
	                "event_passive_grow_list": [
	                    {
	                        "passive_id": 2045501,
	                        "progress": 1
	                    },
	                    {
	                        "passive_id": 2045502,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045503,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045504,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045505,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045506,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045507,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045508,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045509,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045510,
	                        "progress": 0
	                    },
	                    {
	                        "passive_id": 2045511,
	                        "progress": 0
	                    }
	                ]
	            },
	            "area_info_list": [
	                {
	                    "scene_path": "Boss/BGRAID004_8001_00/BGRAID004_8001_00_00",
	                    "area_name": "RAID_08_0104_01"
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
	            "quest_id": 204550301,
	            "play_count": 0,
	            "is_mission_clear_1": 0,
	            "is_mission_clear_2": 0,
	            "is_mission_clear_3": 0
	        },
	        "odds_info": {
	            "area_index": 0,
	            "reaction_obj_count": 0,
	            "drop_obj": [],
	            "enemy": [
	                {
	                    "param_id": 204080101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [
	                                {
	                                    "type": 4,
	                                    "id": 0,
	                                    "quantity": 40,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 8,
	                                    "id": 101001001,
	                                    "quantity": 1,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 4,
	                                    "id": 0,
	                                    "quantity": 40,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 8,
	                                    "id": 104001041,
	                                    "quantity": 2,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 4,
	                                    "id": 0,
	                                    "quantity": 20,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 8,
	                                    "id": 103001001,
	                                    "quantity": 1,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 20,
	                                    "id": 2045501,
	                                    "quantity": 27,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 20,
	                                    "id": 2045502,
	                                    "quantity": 20,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 20,
	                                    "id": 2045503,
	                                    "quantity": 23,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 20,
	                                    "id": 2045504,
	                                    "quantity": 3,
	                                    "place": 0
	                                }
	                            ],
	                            "coin": 3,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 0
	                },
	                {
	                    "param_id": 204080103,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [
	                                {
	                                    "type": 20,
	                                    "id": 2045501,
	                                    "quantity": 3,
	                                    "place": 0
	                                }
	                            ],
	                            "coin": 1,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 1
	                },
	                {
	                    "param_id": 204080104,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [
	                                {
	                                    "type": 20,
	                                    "id": 2045501,
	                                    "quantity": 3,
	                                    "place": 0
	                                }
	                            ],
	                            "coin": 1,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 2
	                },
	                {
	                    "param_id": 204080105,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [
	                                {
	                                    "type": 20,
	                                    "id": 2045501,
	                                    "quantity": 4,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 20,
	                                    "id": 2045501,
	                                    "quantity": 4,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 20,
	                                    "id": 2045503,
	                                    "quantity": 1,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 20,
	                                    "id": 2045503,
	                                    "quantity": 1,
	                                    "place": 0
	                                }
	                            ],
	                            "coin": 1,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 3
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 4
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 5
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 6
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 7
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 8
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 9
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 10
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 11
	                },
	                {
	                    "param_id": 204080106,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [],
	                    "enemy_idx": 12
	                }
	            ],
	            "grade": []
	        },
	        "update_data_list": {
	            "quest_list": [
	                {
	                    "quest_id": 204550301,
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
