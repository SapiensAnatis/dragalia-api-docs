/summon/get_summon_point_trade
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
	DeviceId: <device_id>
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883475981830366
	Request-Time: 1661984679
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 16


Request body
----------------

.. code-block:: json

	{
	    "summon_id": 1020203
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 355
	Expires: Wed, 31 Aug 2022 22:24:40 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:24:40 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "summon_point_trade_list": [
	            {
	                "trade_id": 1020203001,
	                "entity_type": 1,
	                "entity_id": 10250203
	            },
	            {
	                "trade_id": 1020203002,
	                "entity_type": 1,
	                "entity_id": 10450202
	            },
	            {
	                "trade_id": 1020203003,
	                "entity_type": 7,
	                "entity_id": 20050217
	            }
	        ],
	        "summon_point_list": [
	            {
	                "summon_point_id": 1020203,
	                "summon_point": 10,
	                "cs_summon_point": 0,
	                "cs_point_term_min_date": 0,
	                "cs_point_term_max_date": 0
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
