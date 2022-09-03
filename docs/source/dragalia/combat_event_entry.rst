/combat_event/entry
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887255687268589	Request-Time: 1662209960	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 13

Request body
----------------

.. code-block:: json

	{
	    "event_id": 22224
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1569	Expires: Sat, 03 Sep 2022 12:59:28 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 12:59:28 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "combat_event_user_data": {
	            "event_id": 22224,
	            "event_point": 0,
	            "exchange_item_01": 0,
	            "quest_unlock_item_01": 0,
	            "story_unlock_item_01": 0,
	            "advent_item_01": 0
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
	                    "is_update": 1,
	                    "receivable_reward_count": 2,
	                    "new_complete_mission_id_list": [
	                        10250101
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 305,
	                    "completed_mission_count": 293,
	                    "current_mission_id": 0
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
