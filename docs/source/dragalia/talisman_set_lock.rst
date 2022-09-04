/talisman/set_lock
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 42156f332fe00e7cd0833d02cdbf756429482b4ceda53471246a4ded78922de7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888854136532421	Request-Time: 1662305236	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 31

Request body
----------------

.. code-block:: json

	{
	    "talisman_key_id": 181020,
	    "is_lock": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 268	Expires: Sun, 04 Sep 2022 15:27:25 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:27:25 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "talisman_list": [
	                {
	                    "talisman_key_id": 181020,
	                    "talisman_id": 50150101,
	                    "is_lock": 1,
	                    "is_new": 1,
	                    "talisman_ability_id_1": 0,
	                    "talisman_ability_id_2": 0,
	                    "talisman_ability_id_3": 0,
	                    "additional_hp": 100,
	                    "additional_attack": 100,
	                    "gettime": 1662242831
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
