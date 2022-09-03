/dungeon_start/start_assign_unit
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com

Request body
----------------

.. code-block:: json

	{
	    "quest_id": 230010101,
	    "request_party_setting_list": [
	        {
	            "unit_no": 1,
	            "chara_id": 10140101,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 0,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 10840501,
	            "edit_skill_2_chara_id": 10440301
	        },
	        {
	            "unit_no": 2,
	            "chara_id": 0,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 0,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 0,
	            "edit_skill_2_chara_id": 0
	        },
	        {
	            "unit_no": 3,
	            "chara_id": 0,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 0,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 0,
	            "edit_skill_2_chara_id": 0
	        },
	        {
	            "unit_no": 4,
	            "chara_id": 0,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 0,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 0,
	            "edit_skill_2_chara_id": 0
	        }
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
	            "dungeon_key": "5039ba2bc75465a74a43ec43bda53cbf59c1efed",
	            "dungeon_type": 16,
	            "play_type": 1,
	            "quest_id": 230010101,
	            "is_host": 1,
	            "continue_limit": 0,
	            "reborn_limit": 0,
	            "start_time": 1662162149,
	            "party_info": {
	                "party_unit_list": [
	                    {
	                        "position": 1,
	                        "chara_data": {
	                            "viewer_id": 66709573935,
	                            "chara_id": 10140101,
	                            "rarity": 4,
	                            "exp": 5890,
	                            "is_new": 0,
	                            "limit_break_count": 0,
	                            "status_plus_count": 0,
	                            "hp_plus_count": 0,
	                            "attack_plus_count": 0,
	                            "gettime": 1661976574,
	                            "level": 18,
	                            "additional_max_level": 0,
	                            "hp": 138,
	                            "attack": 93,
	                            "skill_1_level": 1,
	                            "skill_2_level": 0,
	                            "ability_1_level": 0,
	                            "ability_2_level": 0,
	                            "ability_3_level": 0,
	                            "ex_ability_level": 1,
	                            "ex_ability_2_level": 1,
	                            "burst_attack_level": 1,
	                            "combo_buildup_count": 0,
	                            "is_temporary": 0,
	                            "is_unlock_edit_skill": 1
	                        },
	                        "dragon_data": [],
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
	                        "dragon_reliability_level": 0,
	                        "game_weapon_passive_ability_list": []
	                    },
	                    {
	                        "position": 2,
	                        "chara_data": [],
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
	                        "position": 3,
	                        "chara_data": [],
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
	                        "chara_data": [],
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
	                    "scene_path": "Boss/BG001_7005_00/BG001_7005_00_00",
	                    "area_name": "SIMPLE_002_0101_01"
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
	            "multi_disconnect_type": 0,
	            "ingame_walker": {
	                "skill_2_level": 1
	            }
	        },
	        "ingame_quest_data": {
	            "quest_id": 230010101,
	            "play_count": 0,
	            "is_mission_clear_1": 0,
	            "is_mission_clear_2": 0,
	            "is_mission_clear_3": 0
	        },
	        "odds_info": {
	            "area_index": 0,
	            "reaction_obj_count": 0,
	            "drop_obj": [],
	            "enemy": [],
	            "grade": []
	        },
	        "update_data_list": {
	            "quest_list": [
	                {
	                    "quest_id": 230010101,
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