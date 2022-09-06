/ability_crest/update_ability_crest_set_name
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 0b6afd9cd7827680606bfec9471a6c73d29f5ce287465ad2c17e62e85f61c8e7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27892203808360598	Request-Time: 1662504892	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 67

Request body
----------------

.. code-block:: json

	{
	    "ability_crest_set_no": 49,
	    "ability_crest_set_name": "extremely overpowere"
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 431	Expires: Tue, 06 Sep 2022 22:55:00 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Tue, 06 Sep 2022 22:55:00 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "ability_crest_set_list": [
	                {
	                    "ability_crest_set_no": 49,
	                    "ability_crest_set_name": "extremely overpowere",
	                    "crest_slot_type_1_crest_id_1": 40050058,
	                    "crest_slot_type_1_crest_id_2": 40050145,
	                    "crest_slot_type_1_crest_id_3": 40050106,
	                    "crest_slot_type_2_crest_id_1": 40040048,
	                    "crest_slot_type_2_crest_id_2": 40040059,
	                    "crest_slot_type_3_crest_id_1": 40090002,
	                    "crest_slot_type_3_crest_id_2": 40090019,
	                    "talisman_key_id": 79147
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
