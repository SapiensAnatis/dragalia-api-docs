/fort/build_start
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
	    "fort_plant_id": 100201,
	    "position_x": 24,
	    "position_z": 11
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
	        "result": 1,
	        "build_id": 1376768,
	        "build_start_date": 1662159828,
	        "build_end_date": 1662159831,
	        "remain_time": 3,
	        "fort_detail": {
	            "max_carpenter_count": 5,
	            "carpenter_num": 2,
	            "working_carpenter_num": 1
	        },
	        "update_data_list": {
	            "build_list": [
	                {
	                    "build_id": 1376768,
	                    "fort_plant_detail_id": 10020101,
	                    "position_x": 24,
	                    "position_z": 11,
	                    "build_status": 1,
	                    "build_start_date": 1662159828,
	                    "build_end_date": 1662159831,
	                    "level": 0,
	                    "plant_id": 100201,
	                    "is_new": 0,
	                    "remain_time": 3,
	                    "last_income_date": 1662159831,
	                    "last_income_time": -3
	                }
	            ],
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 3,
	                "exp": 280,
	                "crystal": 895,
	                "coin": 1999992629,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 12495,
	                "dew_point": 1270,
	                "build_time_point": 0,
	                "last_login_time": 1662158090,
	                "stamina_single": 180,
	                "last_stamina_single_update_time": 1662159096,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 36,
	                "last_stamina_multi_update_time": 1662159096,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 11002,
	                "tutorial_flag_list": [
	                    1002,
	                    1020,
	                    1022,
	                    1023,
	                    1027
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1661897736
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