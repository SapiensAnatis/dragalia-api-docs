/dragon/reset_plus_count
==================================================

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
	    "dragon_key_id": 4896202,
	    "plus_count_type": 1
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
	        "update_data_list": {
	            "dragon_list": [
	                {
	                    "dragon_key_id": 4896202,
	                    "dragon_id": 20050306,
	                    "level": 100,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 1,
	                    "exp": 1240020,
	                    "is_lock": 1,
	                    "is_new": 1,
	                    "get_time": 1557120441,
	                    "skill_1_level": 2,
	                    "ability_1_level": 5,
	                    "ability_2_level": 5,
	                    "limit_break_count": 4
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 118001001,
	                    "quantity": 206
	                }
	            ],
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jaysephine",
	                "level": 174,
	                "exp": 6181433,
	                "crystal": 14140,
	                "coin": 1663558245,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 400,
	                "main_party_no": 1,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 22219,
	                "mana_point": 9042316,
	                "dew_point": 922590,
	                "build_time_point": 1067,
	                "last_login_time": 1662304453,
	                "stamina_single": 13,
	                "last_stamina_single_update_time": 1662213130,
	                "stamina_single_surplus_second": 283,
	                "stamina_multi": 6,
	                "last_stamina_multi_update_time": 1662213130,
	                "stamina_multi_surplus_second": 3498,
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
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------