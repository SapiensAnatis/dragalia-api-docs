/chara/set_chara_unit_set
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 0d529f74bec02cbdd6ed8e24f91f5d1a3c8aae212bdd684643033eef032f2d95	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888761056528937	Request-Time: 1662299695	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 339

Request body
----------------

.. code-block:: json

	{
	    "unit_set_no": 1,
	    "unit_set_name": "Set 1",
	    "chara_id": 10850403,
	    "request_chara_unit_set_data": {
	        "dragon_key_id": 19126829,
	        "weapon_body_id": 0,
	        "crest_slot_type_1_crest_id_1": 0,
	        "crest_slot_type_1_crest_id_2": 0,
	        "crest_slot_type_1_crest_id_3": 0,
	        "crest_slot_type_2_crest_id_1": 0,
	        "crest_slot_type_2_crest_id_2": 0,
	        "crest_slot_type_3_crest_id_1": 0,
	        "crest_slot_type_3_crest_id_2": 0,
	        "talisman_key_id": 0
	    }
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 441	Expires: Sun, 04 Sep 2022 13:54:57 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 13:54:57 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "chara_unit_set_list": [
	                {
	                    "chara_id": 10850403,
	                    "chara_unit_set_detail_list": [
	                        {
	                            "unit_set_no": 1,
	                            "unit_set_name": "Set 1",
	                            "dragon_key_id": 19126829,
	                            "weapon_body_id": 0,
	                            "crest_slot_type_1_crest_id_1": 0,
	                            "crest_slot_type_1_crest_id_2": 0,
	                            "crest_slot_type_1_crest_id_3": 0,
	                            "crest_slot_type_2_crest_id_1": 0,
	                            "crest_slot_type_2_crest_id_2": 0,
	                            "crest_slot_type_3_crest_id_1": 0,
	                            "crest_slot_type_3_crest_id_2": 0,
	                            "talisman_key_id": 0
	                        }
	                    ]
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
