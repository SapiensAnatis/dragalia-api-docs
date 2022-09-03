/weapon_body/craft
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
	    "weapon_body_id": 30239901
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
	            "weapon_body_list": [
	                {
	                    "weapon_body_id": 30239901,
	                    "buildup_count": 0,
	                    "limit_break_count": 0,
	                    "limit_over_count": 0,
	                    "equipable_count": 1,
	                    "additional_crest_slot_type_1_count": 0,
	                    "additional_crest_slot_type_2_count": 0,
	                    "additional_crest_slot_type_3_count": 0,
	                    "additional_effect_count": 0,
	                    "unlock_weapon_passive_ability_no_list": [
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0
	                    ],
	                    "fort_passive_chara_weapon_buildup_count": 0,
	                    "is_new": 1,
	                    "gettime": 1662165523
	                }
	            ],
	            "weapon_skin_list": [
	                {
	                    "weapon_skin_id": 30239901,
	                    "is_new": 1,
	                    "gettime": 1662165523
	                }
	            ],
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 60,
	                "exp": 69990,
	                "crystal": 2119,
	                "coin": 2000402138,
	                "max_dragon_quantity": 185,
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
	                "stamina_single": 999,
	                "last_stamina_single_update_time": 1662165243,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 99,
	                "last_stamina_multi_update_time": 1662165243,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 60999,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1009,
	                    1010,
	                    1014,
	                    1019,
	                    1020,
	                    1021,
	                    1022,
	                    1023,
	                    1024,
	                    1027
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 1662159858,
	                "create_time": 1661897736
	            },
	            "material_list": [
	                {
	                    "material_id": 202001001,
	                    "quantity": 321
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