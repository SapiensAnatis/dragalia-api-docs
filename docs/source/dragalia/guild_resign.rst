/guild/resign
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: b6a54796b1e3e6cdd20880aa0f862f201bd3f91adc8f8b59b7d65c2d6cd8b352	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888906112338107	Request-Time: 1662308334	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 36

Request body
----------------

.. code-block:: json

	{
	    "guild_id": 83132741,
	    "is_temporary_member": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 377	Expires: Sun, 04 Sep 2022 16:19:02 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 16:19:02 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "user_guild_data": {
	                "guild_id": 0,
	                "guild_apply_id": 0,
	                "penalty_end_time": 1662394742,
	                "guild_push_notification_type_running": 2,
	                "guild_push_notification_type_suspending": 2,
	                "profile_entity_type": 1,
	                "profile_entity_id": 10150303,
	                "profile_entity_rarity": 5,
	                "last_attend_time": 1662307659,
	                "is_enable_invite_receive": 0,
	                "is_enable_invite_send": 0
	            },
	            "guild_data": [],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
