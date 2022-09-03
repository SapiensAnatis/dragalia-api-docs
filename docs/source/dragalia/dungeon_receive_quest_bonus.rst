/dungeon/receive_quest_bonus
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
	    "quest_event_id": 32000,
	    "is_receive": 1,
	    "receive_bonus_count": 1
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
	        "receive_quest_bonus": {
	            "target_quest_id": 320021102,
	            "receive_bonus_count": 1,
	            "bonus_factor": 1,
	            "quest_bonus_entity_list": [
	                {
	                    "entity_type": 8,
	                    "entity_id": 208020011,
	                    "entity_quantity": 2
	                },
	                {
	                    "entity_type": 8,
	                    "entity_id": 208020012,
	                    "entity_quantity": 1
	                },
	                {
	                    "entity_type": 8,
	                    "entity_id": 201021001,
	                    "entity_quantity": 1
	                },
	                {
	                    "entity_type": 8,
	                    "entity_id": 118001001,
	                    "entity_quantity": 2
	                },
	                {
	                    "entity_type": 8,
	                    "entity_id": 119001001,
	                    "entity_quantity": 2
	                }
	            ]
	        },
	        "update_data_list": {
	            "quest_event_list": [
	                {
	                    "quest_event_id": 32000,
	                    "daily_play_count": 1,
	                    "weekly_play_count": 1,
	                    "quest_bonus_receive_count": 1,
	                    "quest_bonus_stack_count": 2,
	                    "quest_bonus_stack_time": 1662205647,
	                    "quest_bonus_reserve_count": 0,
	                    "quest_bonus_reserve_time": 0,
	                    "last_daily_reset_time": 1662205647,
	                    "last_weekly_reset_time": 1662205647
	                }
	            ],
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 14
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