/earn_event/receive_event_point_reward
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 8674027400a802915be40b6cf1a10c6549dd9b767119e969491596ee95ae6617	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27973281818615856	Request-Time: 1667337517	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 13

Request body
----------------

.. code-block:: json

	{
	    "event_id": 22907
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 164	Expires: Tue, 01 Nov 2022 21:18:46 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Tue, 01 Nov 2022 21:18:46 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "event_reward_list": [],
	        "event_reward_entity_list": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
