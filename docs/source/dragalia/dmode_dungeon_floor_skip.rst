/dmode_dungeon/floor_skip
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 64a945894e18f4c6ee32c512ee4ceb54763d543e6d70db8c2714485ca6ea9198	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888887019878107	Request-Time: 1662307196	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 253	Expires: Sun, 04 Sep 2022 16:00:05 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 16:00:05 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_dungeon_state": 4,
	        "update_data_list": {
	            "dmode_info": {
	                "total_max_floor_num": 60,
	                "recovery_count": 2,
	                "recovery_time": 1662306212,
	                "floor_skip_count": 2,
	                "floor_skip_time": 1662307205,
	                "dmode_point_1": 6114,
	                "dmode_point_2": 706,
	                "is_entry": 1
	            },
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
