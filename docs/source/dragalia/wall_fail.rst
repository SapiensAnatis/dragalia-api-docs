/wall/fail
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 42156f332fe00e7cd0833d02cdbf756429482b4ceda53471246a4ded78922de7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888855260605899	Request-Time: 1662305303	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 67

Request body
----------------

.. code-block:: json

	{
	    "dungeon_key": "72c3715340e3b87134819ec54166893021f20efd",
	    "fail_state": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 195	Expires: Sun, 04 Sep 2022 15:28:32 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:28:32 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "result": 1,
	        "fail_helper_list": [],
	        "fail_helper_detail_list": [],
	        "fail_quest_detail": {
	            "quest_id": 0,
	            "wall_id": 216010005,
	            "wall_level": 75,
	            "is_host": 1
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
