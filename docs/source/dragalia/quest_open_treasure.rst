/quest/open_treasure
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
	    "quest_treasure_id": 126201
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
	        "quest_treasure_reward_list": [
	            {
	                "entity_type": 8,
	                "entity_id": 123001001,
	                "entity_quantity": 10
	            }
	        ],
	        "duplicate_entity_list": [],
	        "add_max_dragon_quantity": 0,
	        "add_max_weapon_quantity": 0,
	        "add_max_amulet_quantity": 0,
	        "update_data_list": {
	            "quest_treasure_list": [
	                {
	                    "quest_treasure_id": 126201
	                }
	            ],
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jay",
	                "level": 174,
	                "exp": 6180333,
	                "crystal": 14035,
	                "coin": 1664268226,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 394,
	                "main_party_no": 1,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 21405,
	                "mana_point": 9041295,
	                "dew_point": 922290,
	                "build_time_point": 1067,
	                "last_login_time": 1662204727,
	                "stamina_single": 5,
	                "last_stamina_single_update_time": 1662211023,
	                "stamina_single_surplus_second": 336,
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
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 28
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