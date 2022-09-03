/wall_start/start
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Relates to
----------
Mercurial Gauntlet

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
	Request-Token: 27886457611880773
	Request-Time: 1662162397
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 55


Request body
----------------

.. code-block:: json

	{
	    "wall_id": 216010001,
	    "wall_level": 1,
	    "party_no": 6,
	    "support_viewer_id": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 6193
	Expires: Fri, 02 Sep 2022 23:46:39 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:46:39 GMT
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
	            "dungeon_key": "ef5dab49aded4720ac877d6c8420096d3df40c58",
	            "dungeon_type": 1,
	            "play_type": 1,
	            "quest_id": 0,
	            "is_host": 1,
	            "continue_limit": -1,
	            "reborn_limit": 0,
	            "start_time": 1662162399,
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
	                            "exp": 2640,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976583,
	                            "level": 13,
	                            "additional_max_level": 0,
	                            "hp": 96,
	                            "attack": 68,
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
	                            "exp": 2640,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976585,
	                            "level": 13,
	                            "additional_max_level": 0,
	                            "hp": 97,
	                            "attack": 66,
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
	                            "exp": 2640,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976589,
	                            "level": 13,
	                            "additional_max_level": 0,
	                            "hp": 102,
	                            "attack": 64,
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
	                            "hp": 0.5,
	                            "attack": 0.5
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
	                            "hp": 0.5,
	                            "attack": 0.5
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
	                "event_passive_grow_list": []
	            },
	            "area_info_list": [
	                {
	                    "scene_path": "Boss/BG034_5001_00/BG034_5001_00_00",
	                    "area_name": "WALL_01_0101_01"
	                }
	            ],
	            "use_stone": -1,
	            "is_fever_time": 0,
	            "is_bot_tutorial": 0,
	            "is_receivable_carry_bonus": 0,
	            "first_clear_viewer_id_list": [],
	            "repeat_state": 0,
	            "multi_disconnect_type": 0
	        },
	        "ingame_wall_data": {
	            "wall_id": 216010001,
	            "wall_level": 1
	        },
	        "odds_info": {
	            "area_index": 0,
	            "reaction_obj_count": 0,
	            "drop_obj": [],
	            "enemy": [
	                {
	                    "param_id": 216011001,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_idx": 0,
	                    "enemy_drop_list": [
	                        {
	                            "coin": 500,
	                            "mana": 120,
	                            "drop_list": [
	                                {
	                                    "type": 8,
	                                    "id": 101001003,
	                                    "quantity": 3,
	                                    "place": 0
	                                }
	                            ]
	                        }
	                    ]
	                }
	            ],
	            "grade": []
	        },
	        "update_data_list": {
	            "quest_wall_list": [
	                {
	                    "quest_group_id": 21601,
	                    "wall_id": 216010001,
	                    "wall_level": 0,
	                    "is_start_next_level": 1
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
