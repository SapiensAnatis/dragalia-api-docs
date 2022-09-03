/dmode/buildup_servitor_passive
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887241678293188	Request-Time: 1662209125	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 59

Request body
----------------

.. code-block:: json

	{
	    "request_buildup_passive_list": [
	        {
	            "passive_no": 2,
	            "passive_level": 19
	        }
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 777	Expires: Sat, 03 Sep 2022 12:45:33 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 12:45:33 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_servitor_passive_list": [
	            {
	                "passive_no": 1,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 2,
	                "passive_level": 19
	            },
	            {
	                "passive_no": 3,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 4,
	                "passive_level": 12
	            },
	            {
	                "passive_no": 5,
	                "passive_level": 20
	            },
	            {
	                "passive_no": 6,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 7,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 8,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 9,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 10,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 11,
	                "passive_level": 1
	            },
	            {
	                "passive_no": 12,
	                "passive_level": 1
	            },
	            {
	                "passive_no": 13,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 14,
	                "passive_level": 10
	            },
	            {
	                "passive_no": 15,
	                "passive_level": 1
	            },
	            {
	                "passive_no": 16,
	                "passive_level": 1
	            },
	            {
	                "passive_no": 17,
	                "passive_level": 1
	            }
	        ],
	        "update_data_list": {
	            "dmode_info": {
	                "total_max_floor_num": 60,
	                "recovery_count": 3,
	                "recovery_time": 1653360289,
	                "floor_skip_count": 1,
	                "floor_skip_time": 1653243974,
	                "dmode_point_1": 287,
	                "dmode_point_2": 703,
	                "is_entry": 1
	            },
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
