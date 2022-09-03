/event_summon/get_data
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
	Request-Token: 27886431187765442
	Request-Time: 1662160822
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 13


Request body
----------------

.. code-block:: json

	{
	    "event_id": 20455
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 3500
	Expires: Fri, 02 Sep 2022 23:20:24 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:20:24 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "box_summon_data": {
	            "event_id": 20455,
	            "event_point": 0,
	            "box_summon_seq": 1,
	            "reset_possible": 0,
	            "remaining_quantity": 535,
	            "box_summon_detail": [
	                {
	                    "id": 1,
	                    "entity_type": 7,
	                    "entity_id": 20050517,
	                    "entity_quantity": 1,
	                    "limit": 1,
	                    "reset_item_flag": 1,
	                    "pickup_item_state": 1,
	                    "total_count": 1
	                },
	                {
	                    "id": 2,
	                    "entity_type": 8,
	                    "entity_id": 202004004,
	                    "entity_quantity": 1,
	                    "limit": 1,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 2,
	                    "total_count": 1
	                },
	                {
	                    "id": 4,
	                    "entity_type": 23,
	                    "entity_id": 0,
	                    "entity_quantity": 25,
	                    "limit": 1,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 1
	                },
	                {
	                    "id": 5,
	                    "entity_type": 18,
	                    "entity_id": 0,
	                    "entity_quantity": 5000,
	                    "limit": 5,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 5
	                },
	                {
	                    "id": 6,
	                    "entity_type": 18,
	                    "entity_id": 0,
	                    "entity_quantity": 200,
	                    "limit": 50,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 50
	                },
	                {
	                    "id": 7,
	                    "entity_type": 4,
	                    "entity_id": 0,
	                    "entity_quantity": 10000,
	                    "limit": 50,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 50
	                },
	                {
	                    "id": 8,
	                    "entity_type": 8,
	                    "entity_id": 202004003,
	                    "entity_quantity": 1,
	                    "limit": 8,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 8
	                },
	                {
	                    "id": 9,
	                    "entity_type": 8,
	                    "entity_id": 202001003,
	                    "entity_quantity": 1,
	                    "limit": 9,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 9
	                },
	                {
	                    "id": 10,
	                    "entity_type": 8,
	                    "entity_id": 202002003,
	                    "entity_quantity": 1,
	                    "limit": 9,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 9
	                },
	                {
	                    "id": 11,
	                    "entity_type": 8,
	                    "entity_id": 202003003,
	                    "entity_quantity": 1,
	                    "limit": 9,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 9
	                },
	                {
	                    "id": 12,
	                    "entity_type": 8,
	                    "entity_id": 104002052,
	                    "entity_quantity": 1,
	                    "limit": 1,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 1
	                },
	                {
	                    "id": 13,
	                    "entity_type": 8,
	                    "entity_id": 104002051,
	                    "entity_quantity": 1,
	                    "limit": 5,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 5
	                },
	                {
	                    "id": 14,
	                    "entity_type": 8,
	                    "entity_id": 104001053,
	                    "entity_quantity": 1,
	                    "limit": 2,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 2
	                },
	                {
	                    "id": 15,
	                    "entity_type": 8,
	                    "entity_id": 104001052,
	                    "entity_quantity": 1,
	                    "limit": 8,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 8
	                },
	                {
	                    "id": 16,
	                    "entity_type": 8,
	                    "entity_id": 104001051,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 17,
	                    "entity_type": 8,
	                    "entity_id": 202004001,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 18,
	                    "entity_type": 8,
	                    "entity_id": 202001002,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 19,
	                    "entity_type": 8,
	                    "entity_id": 202001001,
	                    "entity_quantity": 1,
	                    "limit": 30,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 30
	                },
	                {
	                    "id": 20,
	                    "entity_type": 8,
	                    "entity_id": 202002002,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 21,
	                    "entity_type": 8,
	                    "entity_id": 202002001,
	                    "entity_quantity": 1,
	                    "limit": 30,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 30
	                },
	                {
	                    "id": 22,
	                    "entity_type": 8,
	                    "entity_id": 202003002,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 23,
	                    "entity_type": 8,
	                    "entity_id": 202003001,
	                    "entity_quantity": 1,
	                    "limit": 30,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 30
	                },
	                {
	                    "id": 24,
	                    "entity_type": 0,
	                    "entity_id": 0,
	                    "entity_quantity": 1,
	                    "limit": 50,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 50,
	                    "two_step_id": 6
	                },
	                {
	                    "id": 25,
	                    "entity_type": 8,
	                    "entity_id": 101001003,
	                    "entity_quantity": 1,
	                    "limit": 13,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 13
	                },
	                {
	                    "id": 26,
	                    "entity_type": 8,
	                    "entity_id": 101001002,
	                    "entity_quantity": 1,
	                    "limit": 15,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 15
	                },
	                {
	                    "id": 27,
	                    "entity_type": 8,
	                    "entity_id": 101001001,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 28,
	                    "entity_type": 8,
	                    "entity_id": 102001003,
	                    "entity_quantity": 1,
	                    "limit": 13,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 13
	                },
	                {
	                    "id": 29,
	                    "entity_type": 8,
	                    "entity_id": 102001002,
	                    "entity_quantity": 1,
	                    "limit": 15,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 15
	                },
	                {
	                    "id": 30,
	                    "entity_type": 8,
	                    "entity_id": 102001001,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 31,
	                    "entity_type": 8,
	                    "entity_id": 103001001,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                },
	                {
	                    "id": 32,
	                    "entity_type": 8,
	                    "entity_id": 113001001,
	                    "entity_quantity": 1,
	                    "limit": 20,
	                    "reset_item_flag": 0,
	                    "pickup_item_state": 0,
	                    "total_count": 20
	                }
	            ],
	            "max_exec_count": 535
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
