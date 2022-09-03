/guild_invite/invite_send
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: d8dc0cf38fa13f08671603a6bd6040402fbffae315b5733a238f8fda55d81aa3	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887181615859955	Request-Time: 1662205545	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 66

Request body
----------------

.. code-block:: json

	{
	    "target_viewer_id": 35789437060,
	    "guild_id": 72987015,
	    "guild_invite_message_id": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 429	Expires: Sat, 03 Sep 2022 11:45:53 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 11:45:53 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "guild_invite_send_list": [
	            {
	                "guild_invite_id": 14606,
	                "send_viewer_id": 97571459880,
	                "send_user_name": "Jay",
	                "receive_viewer_id": 35789437060,
	                "receive_user_name": "Archie",
	                "receive_user_level": 56,
	                "receive_max_party_power": 18412,
	                "receive_profile_entity_type": 7,
	                "receive_profile_entity_id": 20050110,
	                "receive_profile_entity_rarity": 5,
	                "receive_last_active_time": 1644963512,
	                "guild_invite_message_id": 1,
	                "limit_time": 1662464753
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
