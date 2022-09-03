/mission/get_drill_mission_list
===================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com
	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
	Accept: */*
	Accept-Encoding: deflate, gzip
	App-Ver: 2.19.0
	Device: 2
	Platform: 2
	Carrier: OnePlus
	DeviceId: <device_id>
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 971a237033cb6cf29e29a8f4109388f283a224852c87e2ccda8d80b70f77c116
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883445900282132
	Request-Time: 1661982886
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 1


Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 1761
	Expires: Wed, 31 Aug 2022 21:54:48 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 21:54:48 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "drill_mission_list": [],
	        "mission_notice": {
	            "normal_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 3,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 222,
	                "completed_mission_count": 3,
	                "current_mission_id": 0
	            },
	            "daily_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 1,
	                "all_mission_count": 9,
	                "completed_mission_count": 0,
	                "current_mission_id": 0
	            },
	            "period_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 10,
	                "completed_mission_count": 0,
	                "current_mission_id": 0
	            },
	            "beginner_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 0,
	                "completed_mission_count": 0,
	                "current_mission_id": 0
	            },
	            "special_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 56,
	                "completed_mission_count": 0,
	                "current_mission_id": 0
	            },
	            "main_story_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 0,
	                "completed_mission_count": 0,
	                "current_mission_id": 0
	            },
	            "memory_event_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 0,
	                "completed_mission_count": 0,
	                "current_mission_id": 0
	            },
	            "drill_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 0,
	                "completed_mission_count": 0,
	                "current_mission_id": 100100
	            },
	            "album_mission_notice": {
	                "is_update": 1,
	                "receivable_reward_count": 0,
	                "new_complete_mission_id_list": [],
	                "pickup_mission_count": 0,
	                "all_mission_count": 22,
	                "completed_mission_count": 0,
	                "current_mission_id": 0
	            }
	        },
	        "current_main_story_mission": [],
	        "drill_mission_group_list": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
