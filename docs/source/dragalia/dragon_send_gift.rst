/dragon/send_gift
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
	    "dragon_id": 20050419,
	    "dragon_gift_id": 30001
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
	        "is_favorite": 0,
	        "return_gift_list": [
	            {
	                "entity_type": 18,
	                "entity_id": 0,
	                "entity_quantity": 500,
	                "is_over": 0
	            }
	        ],
	        "reward_reliability_list": [],
	        "update_data_list": {
	            "dragon_reliability_list": [
	                {
	                    "dragon_id": 20050419,
	                    "gettime": 1648381213,
	                    "reliability_level": 23,
	                    "reliability_total_exp": 18700,
	                    "last_contact_time": 1662307061
	                }
	            ],
	            "dragon_gift_list": [
	                {
	                    "dragon_gift_id": 30001,
	                    "quantity": 1
	                }
	            ],
	            "party_power_data": {
	                "max_party_power": 52720
	            },
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jaysephine",
	                "level": 174,
	                "exp": 6181633,
	                "crystal": 14140,
	                "coin": 1660822379,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 400,
	                "main_party_no": 1,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 22220,
	                "mana_point": 8937271,
	                "dew_point": 849590,
	                "build_time_point": 1067,
	                "last_login_time": 1662304453,
	                "stamina_single": 129,
	                "last_stamina_single_update_time": 1662306575,
	                "stamina_single_surplus_second": 0,
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