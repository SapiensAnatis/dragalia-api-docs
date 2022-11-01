/earn_event/entry
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
	    "event_id": 22907
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
	        "earn_event_user_data": {
	            "event_id": 22907,
	            "event_point": 0,
	            "exchange_item_01": 0,
	            "exchange_item_02": 0,
	            "advent_item_quantity_01": 0
	        },
	        "update_data_list": {
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "daily_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "period_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 1,
	                    "new_complete_mission_id_list": [
	                        11850101
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 11,
	                    "completed_mission_count": 1,
	                    "current_mission_id": 0
	                },
	                "beginner_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "special_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "main_story_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "memory_event_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "drill_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "album_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                }
	            },
	            "current_main_story_mission": {
	                "main_story_mission_group_id": 11,
	                "main_story_mission_state_list": [
	                    {
	                        "main_story_mission_id": 10110101,
	                        "state": 2
	                    },
	                    {
	                        "main_story_mission_id": 10110201,
	                        "state": 2
	                    },
	                    {
	                        "main_story_mission_id": 10110301,
	                        "state": 2
	                    },
	                    {
	                        "main_story_mission_id": 10110401,
	                        "state": 2
	                    },
	                    {
	                        "main_story_mission_id": 10110501,
	                        "state": 2
	                    }
	                ]
	            },
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------