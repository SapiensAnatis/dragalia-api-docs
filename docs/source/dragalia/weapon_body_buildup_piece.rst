/weapon_body/buildup_piece
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 1a5a3cb1aa568946e14a539ae29b79f74c58858365dc2bb0dbe8d8e5150215ed	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886509621250185	Request-Time: 1662165498	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 125

Request body
----------------

.. code-block:: json

	{
	    "weapon_body_id": 30139901,
	    "buildup_weapon_body_piece_list": [
	        {
	            "buildup_piece_type": 7,
	            "buildup_piece_no": 1,
	            "step": 2,
	            "is_use_dedicated_material": 0
	        }
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 524	Expires: Sat, 03 Sep 2022 00:38:20 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 00:38:20 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "weapon_body_list": [
	                {
	                    "weapon_body_id": 30139901,
	                    "buildup_count": 2,
	                    "limit_break_count": 4,
	                    "limit_over_count": 0,
	                    "equipable_count": 1,
	                    "additional_crest_slot_type_1_count": 0,
	                    "additional_crest_slot_type_2_count": 0,
	                    "additional_crest_slot_type_3_count": 0,
	                    "additional_effect_count": 0,
	                    "unlock_weapon_passive_ability_no_list": [
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0,
	                        0
	                    ],
	                    "fort_passive_chara_weapon_buildup_count": 0,
	                    "is_new": 1,
	                    "gettime": 1662165347
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 103001001,
	                    "quantity": 16
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
