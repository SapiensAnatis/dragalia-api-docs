/fort/build_cancel
==================================================

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
	SID: c7ed6901a28a867034d04fdf83a16dc7f9e261195033ec4d529637ef3f64d60b
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27891767768516967
	Request-Time: 1662478909
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 15


Request body
----------------

.. code-block:: json

	{
	    "build_id": 1360639
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 55
	Expires: Tue, 06 Sep 2022 15:41:50 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Tue, 06 Sep 2022 15:41:50 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
		"data_headers": {
			"result_code": 1
		},
		"data": {
			"result": 1,
			"build_id": 1360642,
			"fort_detail": {
				"max_carpenter_count": 5,
				"carpenter_num": 2,
				"working_carpenter_num": 0
			},
			"update_data_list": {
				"build_list": [
				],
				"functional_maintenance_list": [
				]
			}
		}
	}

Notes
------
