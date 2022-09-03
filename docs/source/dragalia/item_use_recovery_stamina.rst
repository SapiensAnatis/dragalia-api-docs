/item/use_recovery_stamina
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
	    "use_item_list": [
	        {
	            "item_id": 100702,
	            "item_quantity": 1
	        }
	    ]
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
	        "recover_data": {
	            "recover_stamina_type": 1007,
	            "recover_stamina_point": 6
	        },
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 3,
	                "exp": 330,
	                "crystal": 1594,
	                "coin": 1999965710,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 4,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 15057,
	                "dew_point": 3170,
	                "build_time_point": 0,
	                "last_login_time": 1662158090,
	                "stamina_single": 180,
	                "last_stamina_single_update_time": 1662160445,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 42,
	                "last_stamina_multi_update_time": 1662160490,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 20301,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
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
	            "item_list": [
	                {
	                    "item_id": 100702,
	                    "quantity": 19
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