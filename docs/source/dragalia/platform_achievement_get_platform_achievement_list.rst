/platform_achievement/get_platform_achievement_list
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888793704991448	Request-Time: 1662301641	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 823	Expires: Sun, 04 Sep 2022 14:27:22 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:27:22 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "achievement_list": [
	            {
	                "achievement_id": 10000101,
	                "state": 1,
	                "progress": 1
	            },
	            {
	                "achievement_id": 10000102,
	                "state": 1,
	                "progress": 1
	            },
	            {
	                "achievement_id": 10000103,
	                "state": 1,
	                "progress": 1
	            },
	            {
	                "achievement_id": 10000104,
	                "state": 1,
	                "progress": 1
	            },
	            {
	                "achievement_id": 10000105,
	                "state": 1,
	                "progress": 1
	            },
	            {
	                "achievement_id": 10000106,
	                "state": 1,
	                "progress": 1
	            },
	            {
	                "achievement_id": 10000201,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000202,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000203,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000204,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000205,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000206,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000301,
	                "state": 1,
	                "progress": 2
	            },
	            {
	                "achievement_id": 10000401,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000402,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000403,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000501,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000502,
	                "state": 0,
	                "progress": 0
	            },
	            {
	                "achievement_id": 10000503,
	                "state": 0,
	                "progress": 25
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
