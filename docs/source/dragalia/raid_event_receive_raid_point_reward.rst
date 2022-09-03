/raid_event/receive_raid_point_reward
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com<device_id>
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
	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886438653626592
	Request-Time: 1662161267
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 48


Request body
----------------

.. code-block:: json

	{
	    "raid_event_id": 20455,
	    "raid_event_reward_id_list": [
	        1001
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 397
	Expires: Fri, 02 Sep 2022 23:27:49 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:27:49 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "raid_event_reward_list": [
	            {
	                "raid_event_id": 20455,
	                "raid_event_reward_id": 1001
	            }
	        ],
	        "update_data_list": {
	            "raid_event_user_list": [
	                {
	                    "raid_event_id": 20455,
	                    "box_summon_point": 35,
	                    "raid_point_1": 7,
	                    "raid_point_2": 0,
	                    "raid_point_3": 0,
	                    "advent_item_quantity_1": 15,
	                    "advent_item_quantity_2": 0,
	                    "ultimate_key_count": 0,
	                    "exchange_item_count": 0,
	                    "exchange_item_count_2": 0
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
