/combat_event/receive_event_point_reward
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
	    "event_id": 22224
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
	        "event_reward_list": [
	            {
	                "event_id": 22224,
	                "event_reward_id": 1
	            },
	            {
	                "event_id": 22224,
	                "event_reward_id": 2
	            },
	            {
	                "event_id": 22224,
	                "event_reward_id": 3
	            },
	            {
	                "event_id": 22224,
	                "event_reward_id": 4
	            },
	            {
	                "event_id": 22224,
	                "event_reward_id": 5
	            },
	            {
	                "event_id": 22224,
	                "event_reward_id": 6
	            }
	        ],
	        "event_reward_entity_list": [
	            {
	                "entity_type": 34,
	                "entity_id": 2222405,
	                "entity_quantity": 1
	            },
	            {
	                "entity_type": 2,
	                "entity_id": 100602,
	                "entity_quantity": 20
	            },
	            {
	                "entity_type": 34,
	                "entity_id": 2222404,
	                "entity_quantity": 1
	            }
	        ],
	        "update_data_list": {
	            "combat_event_user_list": [
	                {
	                    "event_id": 22224,
	                    "event_point": 4200,
	                    "exchange_item_01": 22,
	                    "quest_unlock_item_01": 3,
	                    "story_unlock_item_01": 1,
	                    "advent_item_01": 0
	                }
	            ],
	            "item_list": [
	                {
	                    "item_id": 100602,
	                    "quantity": 733
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