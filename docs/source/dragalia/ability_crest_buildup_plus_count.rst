/ability_crest/buildup_plus_count
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 42156f332fe00e7cd0833d02cdbf756429482b4ceda53471246a4ded78922de7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888843835321755	Request-Time: 1662304622	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 107

Request body
----------------

.. code-block:: json

	{
	    "ability_crest_id": 40050010,
	    "plus_count_params_list": [
	        {
	            "plus_count_type": 1,
	            "plus_count": 50
	        },
	        {
	            "plus_count_type": 2,
	            "plus_count": 50
	        }
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 356	Expires: Sun, 04 Sep 2022 15:17:11 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:17:11 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "ability_crest_list": [
	                {
	                    "ability_crest_id": 40050010,
	                    "buildup_count": 0,
	                    "limit_break_count": 0,
	                    "equipable_count": 1,
	                    "hp_plus_count": 50,
	                    "attack_plus_count": 50,
	                    "is_new": 1,
	                    "is_favorite": 0,
	                    "gettime": 1601459403
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 122001001,
	                    "quantity": 3542
	                },
	                {
	                    "material_id": 123001001,
	                    "quantity": 3818
	                }
	            ],
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
