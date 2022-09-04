/fort/levelup_cancel
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888803620326150	Request-Time: 1662302232	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 15

Request body
----------------

.. code-block:: json

	{
	    "build_id": 1363584
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 382	Expires: Sun, 04 Sep 2022 14:37:14 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:37:14 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "result": 1,
	        "build_id": 1363584,
	        "fort_detail": {
	            "max_carpenter_count": 5,
	            "carpenter_num": 3,
	            "working_carpenter_num": 0
	        },
	        "update_data_list": {
	            "build_list": [
	                {
	                    "build_id": 1363584,
	                    "fort_plant_detail_id": 10020115,
	                    "position_x": 25,
	                    "position_z": 20,
	                    "build_status": 0,
	                    "build_start_date": 0,
	                    "build_end_date": 0,
	                    "level": 15,
	                    "plant_id": 100201,
	                    "is_new": 0,
	                    "remain_time": 0,
	                    "last_income_date": 1662302219,
	                    "last_income_time": 15
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
