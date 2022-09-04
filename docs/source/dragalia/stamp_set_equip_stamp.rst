/stamp/set_equip_stamp
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888792094378704	Request-Time: 1662301545	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 632

Request body
----------------

.. code-block:: json

	{
	    "deck_no": 1,
	    "stamp_list": [
	        {
	            "slot": 1,
	            "stamp_id": 10001
	        },
	        {
	            "slot": 2,
	            "stamp_id": 10004
	        },
	        {
	            "slot": 3,
	            "stamp_id": 10003
	        },
	        {
	            "slot": 4,
	            "stamp_id": 10002
	        },
	        {
	            "slot": 5,
	            "stamp_id": 10005
	        },
	        {
	            "slot": 6,
	            "stamp_id": 10303
	        },
	        {
	            "slot": 7,
	            "stamp_id": 10007
	        },
	        {
	            "slot": 8,
	            "stamp_id": 10008
	        },
	        {
	            "slot": 9,
	            "stamp_id": 10009
	        },
	        {
	            "slot": 10,
	            "stamp_id": 10010
	        },
	        {
	            "slot": 11,
	            "stamp_id": 10011
	        },
	        {
	            "slot": 12,
	            "stamp_id": 10012
	        },
	        {
	            "slot": 13,
	            "stamp_id": 10013
	        },
	        {
	            "slot": 14,
	            "stamp_id": 10014
	        },
	        {
	            "slot": 15,
	            "stamp_id": 10015
	        },
	        {
	            "slot": 16,
	            "stamp_id": 10016
	        },
	        {
	            "slot": 17,
	            "stamp_id": 10017
	        },
	        {
	            "slot": 18,
	            "stamp_id": 10018
	        },
	        {
	            "slot": 19,
	            "stamp_id": 10019
	        },
	        {
	            "slot": 20,
	            "stamp_id": 10020
	        },
	        {
	            "slot": 21,
	            "stamp_id": 10021
	        },
	        {
	            "slot": 22,
	            "stamp_id": 10022
	        },
	        {
	            "slot": 23,
	            "stamp_id": 10023
	        },
	        {
	            "slot": 24,
	            "stamp_id": 10024
	        },
	        {
	            "slot": 25,
	            "stamp_id": 10025
	        },
	        {
	            "slot": 26,
	            "stamp_id": 10026
	        },
	        {
	            "slot": 27,
	            "stamp_id": 10027
	        },
	        {
	            "slot": 28,
	            "stamp_id": 10028
	        },
	        {
	            "slot": 29,
	            "stamp_id": 10029
	        },
	        {
	            "slot": 30,
	            "stamp_id": 10030
	        },
	        {
	            "slot": 31,
	            "stamp_id": 10031
	        },
	        {
	            "slot": 32,
	            "stamp_id": 10201
	        }
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 709	Expires: Sun, 04 Sep 2022 14:25:47 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:25:47 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "equip_stamp_list": [
	            {
	                "slot": 1,
	                "stamp_id": 10001
	            },
	            {
	                "slot": 2,
	                "stamp_id": 10004
	            },
	            {
	                "slot": 3,
	                "stamp_id": 10003
	            },
	            {
	                "slot": 4,
	                "stamp_id": 10002
	            },
	            {
	                "slot": 5,
	                "stamp_id": 10005
	            },
	            {
	                "slot": 6,
	                "stamp_id": 10303
	            },
	            {
	                "slot": 7,
	                "stamp_id": 10007
	            },
	            {
	                "slot": 8,
	                "stamp_id": 10008
	            },
	            {
	                "slot": 9,
	                "stamp_id": 10009
	            },
	            {
	                "slot": 10,
	                "stamp_id": 10010
	            },
	            {
	                "slot": 11,
	                "stamp_id": 10011
	            },
	            {
	                "slot": 12,
	                "stamp_id": 10012
	            },
	            {
	                "slot": 13,
	                "stamp_id": 10013
	            },
	            {
	                "slot": 14,
	                "stamp_id": 10014
	            },
	            {
	                "slot": 15,
	                "stamp_id": 10015
	            },
	            {
	                "slot": 16,
	                "stamp_id": 10016
	            },
	            {
	                "slot": 17,
	                "stamp_id": 10017
	            },
	            {
	                "slot": 18,
	                "stamp_id": 10018
	            },
	            {
	                "slot": 19,
	                "stamp_id": 10019
	            },
	            {
	                "slot": 20,
	                "stamp_id": 10020
	            },
	            {
	                "slot": 21,
	                "stamp_id": 10021
	            },
	            {
	                "slot": 22,
	                "stamp_id": 10022
	            },
	            {
	                "slot": 23,
	                "stamp_id": 10023
	            },
	            {
	                "slot": 24,
	                "stamp_id": 10024
	            },
	            {
	                "slot": 25,
	                "stamp_id": 10025
	            },
	            {
	                "slot": 26,
	                "stamp_id": 10026
	            },
	            {
	                "slot": 27,
	                "stamp_id": 10027
	            },
	            {
	                "slot": 28,
	                "stamp_id": 10028
	            },
	            {
	                "slot": 29,
	                "stamp_id": 10029
	            },
	            {
	                "slot": 30,
	                "stamp_id": 10030
	            },
	            {
	                "slot": 31,
	                "stamp_id": 10031
	            },
	            {
	                "slot": 32,
	                "stamp_id": 10201
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
