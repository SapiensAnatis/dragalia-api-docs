/summon/get_summon_history
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 64a945894e18f4c6ee32c512ee4ceb54763d543e6d70db8c2714485ca6ea9198	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888888966035173	Request-Time: 1662307312	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 405	Expires: Sun, 04 Sep 2022 16:02:01 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 16:02:01 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "summon_history_list": [
	            {
	                "key_id": 21996095,
	                "summon_id": 1020204,
	                "summon_exec_type": 1,
	                "exec_date": 1662307301,
	                "payment_type": 8,
	                "entity_type": 7,
	                "entity_id": 20040102,
	                "entity_quantity": 1,
	                "entity_level": 1,
	                "entity_rarity": 4,
	                "entity_limit_break_count": 0,
	                "entity_hp_plus_count": 0,
	                "entity_attack_plus_count": 0,
	                "summon_prize_rank": 0,
	                "summon_point_id": 1020204,
	                "summon_point": 1,
	                "get_dew_point_quantity": 0
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
