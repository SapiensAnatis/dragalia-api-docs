/combat_event/receive_event_point_reward
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887259814463750	Request-Time: 1662210206	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 13

Request body
----------------

.. code-block:: json

	{
	    "event_id": 22224
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 649	Expires: Sat, 03 Sep 2022 13:03:34 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 13:03:34 GMT	Connection: keep-alive

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
