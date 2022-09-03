/dragon/limit_break
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
	    "base_dragon_key_id": 19273100,
	    "limit_break_grow_list": [
	        {
	            "limit_break_count": 1,
	            "limit_break_item_type": 1,
	            "target_id": 19273092
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
	        "delete_data_list": {
	            "delete_dragon_list": [
	                {
	                    "dragon_key_id": 19273092
	                }
	            ]
	        },
	        "update_data_list": {
	            "dragon_list": [
	                {
	                    "dragon_key_id": 19273100,
	                    "dragon_id": 20030103,
	                    "level": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "exp": 0,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "get_time": 1661976618,
	                    "skill_1_level": 1,
	                    "ability_1_level": 2,
	                    "ability_2_level": 0,
	                    "limit_break_count": 1
	                }
	            ],
	            "album_dragon_list": [
	                {
	                    "dragon_id": 20030103,
	                    "max_level": 1,
	                    "max_limit_break_count": 1
	                }
	            ],
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 11,
	                    "new_complete_mission_id_list": [
	                        10000801
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 235,
	                    "completed_mission_count": 29,
	                    "current_mission_id": 0
	                },
	                "daily_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "period_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
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
	            "current_main_story_mission": [],
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------