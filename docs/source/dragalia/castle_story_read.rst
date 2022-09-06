/castle_story/read
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: feda37ed2ee2b7c0a6241ae29aa8ea8a2f5b8c7b49a31163ed570110051eab85	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27891794897275394	Request-Time: 1662480526	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 22

Request body
----------------

.. code-block:: json

	{
	    "castle_story_id": 1003301
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 334	Expires: Tue, 06 Sep 2022 16:08:48 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Tue, 06 Sep 2022 16:08:48 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "castle_story_reward_list": [
	            {
	                "entity_type": 23,
	                "entity_id": 0,
	                "entity_quantity": 50
	            }
	        ],
	        "update_data_list": {
	            "castle_story_list": [
	                {
	                    "castle_story_id": 1003301,
	                    "is_read": 1
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 201008001,
	                    "quantity": 0
	                }
	            ],
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 723
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
