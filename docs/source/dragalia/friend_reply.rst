/friend/reply
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 142f3eef616e3c196682f8a8b744773db057593eb3e238707c538acd7cd9c8e2	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886401341098119	Request-Time: 1662159044	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 27

Request body
----------------

.. code-block:: json

	{
	    "friend_id": 55169104656,
	    "reply": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 139	Expires: Fri, 02 Sep 2022 22:50:46 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Fri, 02 Sep 2022 22:50:46 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "result": 1,
	        "update_data_list": {
	            "friend_notice": {
	                "friend_new_count": 2,
	                "apply_new_count": 0
	            },
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
