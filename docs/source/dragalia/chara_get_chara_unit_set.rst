/chara/get_chara_unit_set
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 0d529f74bec02cbdd6ed8e24f91f5d1a3c8aae212bdd684643033eef032f2d95	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888760989420072	Request-Time: 1662299691	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 36

Request body
----------------

.. code-block:: json

	{
	    "chara_id_list": [
	        10140101,
	        10830101,
	        10130102,
	        10850403
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 274	Expires: Sun, 04 Sep 2022 13:54:53 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 13:54:53 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "chara_unit_set_list": [
	            {
	                "chara_id": 10140101,
	                "chara_unit_set_detail_list": []
	            },
	            {
	                "chara_id": 10830101,
	                "chara_unit_set_detail_list": []
	            },
	            {
	                "chara_id": 10130102,
	                "chara_unit_set_detail_list": []
	            },
	            {
	                "chara_id": 10850403,
	                "chara_unit_set_detail_list": []
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
