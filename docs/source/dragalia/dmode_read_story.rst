/dmode/read_story
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: d1d3e0dc85e564407811ed5afd4c108d6ba1251cb2023eff01a38d17e26433ec	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27892257126353338	Request-Time: 1662508077	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 17

Request body
----------------

.. code-block:: json

	{
	    "dmode_story_id": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 282	Expires: Tue, 06 Sep 2022 23:47:58 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Tue, 06 Sep 2022 23:47:58 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_story_reward_list": [
	            {
	                "entity_type": 23,
	                "entity_id": 0,
	                "entity_quantity": 25
	            }
	        ],
	        "update_data_list": {
	            "dmode_story_list": [
	                {
	                    "dmode_story_id": 1,
	                    "is_read": 1
	                }
	            ],
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 14
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
