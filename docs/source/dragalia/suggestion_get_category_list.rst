/suggestion/get_category_list
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com<device_id>
	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
	Accept: */*
	Accept-Encoding: deflate, gzip
	App-Ver: 2.19.0
	Device: 2
	Platform: 2
	Carrier: OnePlus
	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886472677820772
	Request-Time: 1662163296
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 21


Request body
----------------

.. code-block:: json

	{
	    "language_code": "en_eu"
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 463
	Expires: Sat, 03 Sep 2022 00:01:38 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Sat, 03 Sep 2022 00:01:38 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "category_list": [
	            {
	                "category_id": 1,
	                "name": "About the gameplay/controls"
	            },
	            {
	                "category_id": 2,
	                "name": "About the characters"
	            },
	            {
	                "category_id": 3,
	                "name": "About the story and setting"
	            },
	            {
	                "category_id": 4,
	                "name": "About the sound and graphics"
	            },
	            {
	                "category_id": 5,
	                "name": "About game modes/events"
	            },
	            {
	                "category_id": 6,
	                "name": "About summoning"
	            },
	            {
	                "category_id": 7,
	                "name": "Requests for additional features"
	            },
	            {
	                "category_id": 8,
	                "name": "Other (about the game in general)"
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
