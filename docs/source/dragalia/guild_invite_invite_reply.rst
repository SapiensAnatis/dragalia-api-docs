/guild_invite/invite_reply
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 42156f332fe00e7cd0833d02cdbf756429482b4ceda53471246a4ded78922de7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888850160332212	Request-Time: 1662304999	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 48

Request body
----------------

.. code-block:: json

	{
	    "guild_id": 71407985,
	    "guild_invite_id": 16519,
	    "reply_status": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 234	Expires: Sun, 04 Sep 2022 15:23:28 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:23:28 GMT	Connection: keep-alive

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
