/dragon/set_lock
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888799610571506	Request-Time: 1662301993	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 29

Request body
----------------

.. code-block:: json

	{
	    "dragon_key_id": 19126832,
	    "is_lock": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 274	Expires: Sun, 04 Sep 2022 14:33:15 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:33:15 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "dragon_list": [
	                {
	                    "dragon_key_id": 19126832,
	                    "dragon_id": 20040102,
	                    "level": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "exp": 0,
	                    "is_lock": 1,
	                    "is_new": 1,
	                    "get_time": 1662244194,
	                    "skill_1_level": 1,
	                    "ability_1_level": 1,
	                    "ability_2_level": 0,
	                    "limit_break_count": 0
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
