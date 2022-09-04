/guild_chat/post_message_stamp
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888799040146156	Request-Time: 1662301959	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 61

Request body
----------------

.. code-block:: json

	{
	    "guild_id": 87745518,
	    "chat_message_id": 1221695,
	    "chat_message_stamp_id": 10008
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 472	Expires: Sun, 04 Sep 2022 14:32:41 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:32:41 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "guild_chat_message_list": [
	            {
	                "chat_message_id": 1221696,
	                "viewer_id": 28894575482,
	                "user_name": "Euden",
	                "profile_entity_type": 1,
	                "profile_entity_id": 10140101,
	                "profile_entity_rarity": 4,
	                "chat_message_type": 2,
	                "chat_message_text": "",
	                "chat_message_stamp_id": 10008,
	                "chat_message_system_message_id": 0,
	                "chat_message_param_value_1": 0,
	                "chat_message_param_value_2": 0,
	                "chat_message_param_value_3": 0,
	                "chat_message_param_value_4": 0,
	                "create_time": 1662301960
	            }
	        ],
	        "polling_interval": 3,
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
