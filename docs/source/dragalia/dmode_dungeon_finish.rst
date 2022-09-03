/dmode_dungeon/finish
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
	    "is_game_over": 0
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
	        "dmode_dungeon_state": 1,
	        "dmode_ingame_result": {
	            "floor_num": 1,
	            "is_record_floor_num": 1,
	            "chara_id_list": [
	                10230501
	            ],
	            "reward_talisman_list": [
	                {
	                    "talisman_id": 50230501,
	                    "talisman_ability_id_1": 0,
	                    "talisman_ability_id_2": 0,
	                    "talisman_ability_id_3": 0,
	                    "additional_hp": 100,
	                    "additional_attack": 100
	                }
	            ],
	            "take_dmode_point_1": 33,
	            "take_dmode_point_2": 0,
	            "take_player_exp": 0,
	            "player_level_up_fstone": 0,
	            "quest_time": 64,
	            "is_view_quest_time": 1,
	            "dmode_score": 1500,
	            "clear_state": 1
	        },
	        "dmode_dungeon_info": {
	            "chara_id": 10230501,
	            "floor_num": 0,
	            "quest_time": 0,
	            "dungeon_score": 0,
	            "is_play_end": 0,
	            "state": 1
	        },
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 5,
	                "exp": 790,
	                "crystal": 2119,
	                "coin": 2000418638,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 6,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 20841,
	                "mana_point": 44923,
	                "dew_point": 3170,
	                "build_time_point": 10,
	                "last_login_time": 1662158090,
	                "stamina_single": 250,
	                "last_stamina_single_update_time": 1662162305,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 65,
	                "last_stamina_multi_update_time": 1662162305,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 20501,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1009,
	                    1019,
	                    1020,
	                    1022,
	                    1023,
	                    1027
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 1662159858,
	                "create_time": 1661897736
	            },
	            "dmode_info": {
	                "total_max_floor_num": 1,
	                "recovery_count": 1,
	                "recovery_time": 1662162807,
	                "floor_skip_count": 0,
	                "floor_skip_time": 0,
	                "dmode_point_1": 33,
	                "dmode_point_2": 0,
	                "is_entry": 1
	            },
	            "talisman_list": [
	                {
	                    "talisman_key_id": 174172,
	                    "talisman_id": 50230501,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "talisman_ability_id_1": 0,
	                    "talisman_ability_id_2": 0,
	                    "talisman_ability_id_3": 0,
	                    "additional_hp": 100,
	                    "additional_attack": 100,
	                    "gettime": 1662162862
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