/guild/update_guild_setting
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 1a5a3cb1aa568946e14a539ae29b79f74c58858365dc2bb0dbe8d8e5150215ed	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886514369202367	Request-Time: 1662165780	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 215

Request body
----------------

.. code-block:: json

	{
	    "guild_id": 49295797,
	    "guild_name": "kings of dragon",
	    "guild_emblem_id": 10008,
	    "guild_introduction": "Hello, fellow adventurers!",
	    "guild_board": "Let's not seize the day! and watch Netflix inste",
	    "joining_condition_type": 1,
	    "activity_policy_type": 3
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 689	Expires: Sat, 03 Sep 2022 00:43:03 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 00:43:03 GMT	Connection: keep-alive

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
	                "guild_id": 49295797,
	                "guild_apply_id": 0,
	                "penalty_end_time": 0,
	                "guild_push_notification_type_running": 1,
	                "guild_push_notification_type_suspending": 1,
	                "profile_entity_type": 1,
	                "profile_entity_id": 10130103,
	                "profile_entity_rarity": 3,
	                "last_attend_time": 1662165692,
	                "is_enable_invite_receive": 0,
	                "is_enable_invite_send": 1
	            },
	            "guild_data": {
	                "guild_id": 49295797,
	                "guild_name": "kings of dragon",
	                "guild_emblem_id": 10008,
	                "guild_introduction": "Hello, fellow adventurers!",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 1,
	                "guild_board": "Let's not seize the day! and watch Netflix inste",
	                "is_penalty_guild_board": 0
	            },
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
