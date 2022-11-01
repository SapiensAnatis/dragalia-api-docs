/earn_event/entry
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 8674027400a802915be40b6cf1a10c6549dd9b767119e969491596ee95ae6617	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27973281499848748	Request-Time: 1667337498	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 13

Request body
----------------

.. code-block:: json

	{
	    "event_id": 22907
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1546	Expires: Tue, 01 Nov 2022 21:18:27 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Tue, 01 Nov 2022 21:18:27 GMT	Connection: keep-alive

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
