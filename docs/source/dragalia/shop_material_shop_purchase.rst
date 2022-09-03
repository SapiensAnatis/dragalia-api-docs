/shop/material_shop_purchase
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
	    "goods_id": 1000001,
	    "shop_type": 1,
	    "payment_type": 5,
	    "quantity": 1
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
	        "material_shop_purchase": [
	            {
	                "goods_id": 1000001,
	                "last_buy_time": 1661984810,
	                "effect_start_time": 1661925600,
	                "effect_end_time": 1662011999,
	                "buy_count": 1
	            }
	        ],
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 1,
	                "exp": 30,
	                "crystal": 450,
	                "coin": 1999991215,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 312,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 547,
	                "dew_point": 600,
	                "build_time_point": 0,
	                "last_login_time": 1661979293,
	                "stamina_single": 18,
	                "last_stamina_single_update_time": 1661984335,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 12,
	                "last_stamina_multi_update_time": 1661897736,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 10601,
	                "tutorial_flag_list": [
	                    1002,
	                    1020,
	                    1022
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1661897736
	            },
	            "present_notice": {
	                "present_count": 1,
	                "present_limit_count": 2
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