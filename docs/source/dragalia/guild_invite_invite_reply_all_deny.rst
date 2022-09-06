/guild_invite/invite_reply_all_deny
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 583ee8bd14f9f45790e06f1690a2c52629b6cc79749504344ec489aea9839101	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27891826841094100	Request-Time: 1662482423	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 61

Request body
----------------

.. code-block:: json

	{
	    "guild_invite_params_list": [
	        {
	            "guild_id": 65426295,
	            "guild_invite_id": 14611
	        }
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 234	Expires: Tue, 06 Sep 2022 16:40:32 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Tue, 06 Sep 2022 16:40:32 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "guild_invite_receive_list": [],
	        "update_data_list": {
	            "guild_notice": {
	                "is_update_guild_apply_reply": 0,
	                "guild_apply_count": 0,
	                "is_update_guild_board": 0,
	                "is_update_guild": 0,
	                "is_update_guild_invite": 0
	            },
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
