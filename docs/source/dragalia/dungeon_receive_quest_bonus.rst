/dungeon/receive_quest_bonus
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: d8dc0cf38fa13f08671603a6bd6040402fbffae315b5733a238f8fda55d81aa3	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887183310358783	Request-Time: 1662205647	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 52

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

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 765	Expires: Sat, 03 Sep 2022 11:47:35 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 11:47:35 GMT	Connection: keep-alive

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
