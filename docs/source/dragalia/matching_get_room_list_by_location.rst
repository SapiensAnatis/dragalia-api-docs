/matching/get_room_list_by_location
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com
	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
	Accept: */*
	Accept-Encoding: deflate, gzip
	App-Ver: 2.19.0
	Device: 2
	Platform: 2
	Carrier: OnePlus
	DeviceId: <device_id>
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886472442939747
	Request-Time: 1662163282
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 14


Request body
----------------

.. code-block:: json

	{
		"region": "usw",
		"quest_type": 0,
		"latitude": <latitude>,
		"longitude": <longitude>,
		"compatible_id": 36
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 51
	Expires: Sat, 03 Sep 2022 00:01:23 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Sat, 03 Sep 2022 00:01:23 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json
	
	{
		"data_headers": {
			"result_code": 1
		},
		"data": {
			"room_list": [
			],
			"update_data_list": {
				"functional_maintenance_list": [
				]
			}
		}
	}

Notes
------
I"m very glad I spotted the latitude and longitude to redact. It was to 15 decimal places and precise enough to know what room of my house I"m in