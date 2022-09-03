/dmode/expedition_start
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887240386447549	Request-Time: 1662209048	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 42

Request body
----------------

.. code-block:: json

	{
	    "target_floor_num": 30,
	    "chara_id_list": [
	        10150104,
	        0,
	        0,
	        0
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 192	Expires: Sat, 03 Sep 2022 12:44:16 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 12:44:16 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_expedition": {
	            "chara_id_1": 10150104,
	            "chara_id_2": 0,
	            "chara_id_3": 0,
	            "chara_id_4": 0,
	            "start_time": 1662209056,
	            "target_floor_num": 30,
	            "state": 2
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
