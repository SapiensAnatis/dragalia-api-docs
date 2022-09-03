/matching/get_room_list_by_quest_id
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: d8dc0cf38fa13f08671603a6bd6040402fbffae315b5733a238f8fda55d81aa3	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887187102009606	Request-Time: 1662205873	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 41

Request body
----------------

.. code-block:: json

	{
	    "region": "usw",
	    "quest_id": 219010101,
	    "compatible_id": 36
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 92	Expires: Sat, 03 Sep 2022 11:51:21 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 11:51:21 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "room_list": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
