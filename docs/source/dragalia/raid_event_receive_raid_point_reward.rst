/raid_event/receive_raid_point_reward
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
	    "raid_event_id": 20455,
	    "raid_event_reward_id_list": [
	        1001
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
	        "raid_event_reward_list": [
	            {
	                "raid_event_id": 20455,
	                "raid_event_reward_id": 1001
	            }
	        ],
	        "update_data_list": {
	            "raid_event_user_list": [
	                {
	                    "raid_event_id": 20455,
	                    "box_summon_point": 35,
	                    "raid_point_1": 7,
	                    "raid_point_2": 0,
	                    "raid_point_3": 0,
	                    "advent_item_quantity_1": 15,
	                    "advent_item_quantity_2": 0,
	                    "ultimate_key_count": 0,
	                    "exchange_item_count": 0,
	                    "exchange_item_count_2": 0
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