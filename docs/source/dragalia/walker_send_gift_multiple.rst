/walker/send_gift_multiple
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6a9ddb6f81c2155f896d95473329f71b86dad100734edc82268b0a321ea5d857	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27892282157965702	Request-Time: 1662509569	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 29

Request body
----------------

.. code-block:: json

	{
	    "dragon_gift_id": 40001,
	    "quantity": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1539	Expires: Wed, 07 Sep 2022 00:12:51 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Wed, 07 Sep 2022 00:12:51 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "is_favorite": 1,
	        "return_gift_list": [
	            {
	                "entity_type": 8,
	                "entity_id": 204006001,
	                "entity_quantity": 5,
	                "is_over": 0
	            }
	        ],
	        "reward_reliability_list": [],
	        "walker_data": {
	            "reliability_level": 3,
	            "reliability_total_exp": 200,
	            "last_contact_time": 1662509571,
	            "skill_2_level": 1
	        },
	        "update_data_list": {
	            "material_list": [
	                {
	                    "material_id": 204006001,
	                    "quantity": 5
	                }
	            ],
	            "dragon_gift_list": [
	                {
	                    "dragon_gift_id": 40001,
	                    "quantity": 14
	                }
	            ],
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 20,
	                    "new_complete_mission_id_list": [
	                        10017301
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 319,
	                    "completed_mission_count": 132,
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
