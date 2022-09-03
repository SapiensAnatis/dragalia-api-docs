/combat_event/receive_event_location_reward
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
	    "event_id": 22224,
	    "event_location_reward_id": 2222402
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
	        "user_event_location_reward_list": [
	            {
	                "event_id": 22224,
	                "location_reward_id": 2222402
	            }
	        ],
	        "event_location_reward_entity_list": [
	            {
	                "entity_type": 34,
	                "entity_id": 2222401,
	                "entity_quantity": 150
	            },
	            {
	                "entity_type": 34,
	                "entity_id": 2222403,
	                "entity_quantity": 1
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 202004004,
	                "entity_quantity": 1
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201009001,
	                "entity_quantity": 100
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201009002,
	                "entity_quantity": 50
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201009003,
	                "entity_quantity": 20
	            },
	            {
	                "entity_type": 4,
	                "entity_id": 0,
	                "entity_quantity": 10000
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 102001003,
	                "entity_quantity": 10
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201005001,
	                "entity_quantity": 20
	            }
	        ],
	        "update_data_list": {
	            "combat_event_user_list": [
	                {
	                    "event_id": 22224,
	                    "event_point": 4200,
	                    "exchange_item_01": 172,
	                    "quest_unlock_item_01": 3,
	                    "story_unlock_item_01": 1,
	                    "advent_item_01": 1
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 102001003,
	                    "quantity": 19120
	                },
	                {
	                    "material_id": 201005001,
	                    "quantity": 8919
	                },
	                {
	                    "material_id": 201009001,
	                    "quantity": 42493
	                },
	                {
	                    "material_id": 201009002,
	                    "quantity": 12112
	                },
	                {
	                    "material_id": 201009003,
	                    "quantity": 11642
	                },
	                {
	                    "material_id": 202004004,
	                    "quantity": 567
	                }
	            ],
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jay",
	                "level": 174,
	                "exp": 6179403,
	                "crystal": 13870,
	                "coin": 1664261778,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 394,
	                "main_party_no": 2,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 22224,
	                "mana_point": 9039322,
	                "dew_point": 922290,
	                "build_time_point": 1067,
	                "last_login_time": 1662204727,
	                "stamina_single": 36,
	                "last_stamina_single_update_time": 1662210188,
	                "stamina_single_surplus_second": 221,
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
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------