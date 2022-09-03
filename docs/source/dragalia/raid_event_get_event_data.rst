/raid_event/get_event_data
==================================

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
	Request-Token: 27883446084831514
	Request-Time: 1661982897
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 18


Request body
----------------

.. code-block:: json

	{
	    "raid_event_id": 20455
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 364
	Expires: Wed, 31 Aug 2022 21:54:59 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 21:54:59 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "raid_event_user_data": [],
	        "raid_event_reward_list": [],
	        "chara_friendship_list": [],
	        "event_trade_list": [],
	        "event_passive_list": [
	            []
	        ],
	        "is_receive_event_damage_reward": 0,
	        "event_damage_data": {
	            "user_damage_value": 0,
	            "user_target_time": 0,
	            "total_damage_value": 0,
	            "total_target_time": 0,
	            "total_aggregate_time": 0
	        },
	        "event_ability_chara_list": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
