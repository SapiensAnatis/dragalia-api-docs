/guild/get_guild_member_data
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 1a5a3cb1aa568946e14a539ae29b79f74c58858365dc2bb0dbe8d8e5150215ed	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886513379346615	Request-Time: 1662165722	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 15

Request body
----------------

.. code-block:: json

	{
	    "guild_id": 49295797
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 348	Expires: Sat, 03 Sep 2022 00:42:04 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 00:42:04 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "guild_member_list": [
	            {
	                "viewer_id": 66709573935,
	                "user_name": "Eudenh",
	                "user_level": 60,
	                "max_party_power": 4782,
	                "profile_entity_type": 1,
	                "profile_entity_id": 10130103,
	                "profile_entity_rarity": 3,
	                "last_active_time": 1662165639,
	                "last_guild_active_time": 1662165719,
	                "last_attend_time": 1662165692,
	                "guild_position_type": 1,
	                "temporary_end_time": 0
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
