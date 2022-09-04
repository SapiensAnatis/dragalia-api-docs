/chara/unlock_edit_skill
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 42156f332fe00e7cd0833d02cdbf756429482b4ceda53471246a4ded78922de7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888843231341976	Request-Time: 1662304586	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 15

Request body
----------------

.. code-block:: json

	{
	    "chara_id": 10140501
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 618	Expires: Sun, 04 Sep 2022 15:16:34 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:16:34 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "chara_list": [
	                {
	                    "chara_id": 10140501,
	                    "rarity": 5,
	                    "exp": 1191950,
	                    "level": 80,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 4,
	                    "is_new": 1,
	                    "gettime": 1564728128,
	                    "skill_1_level": 3,
	                    "skill_2_level": 2,
	                    "ability_1_level": 2,
	                    "ability_2_level": 2,
	                    "ability_3_level": 1,
	                    "burst_attack_level": 2,
	                    "combo_buildup_count": 0,
	                    "hp": 806,
	                    "attack": 444,
	                    "ex_ability_level": 5,
	                    "ex_ability_2_level": 5,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 1,
	                    "mana_circle_piece_id_list": [
	                        1,
	                        2,
	                        3,
	                        4,
	                        5,
	                        6,
	                        7,
	                        8,
	                        9,
	                        10,
	                        11,
	                        12,
	                        13,
	                        14,
	                        15,
	                        16,
	                        17,
	                        18,
	                        19,
	                        20,
	                        21,
	                        22,
	                        23,
	                        24,
	                        25,
	                        26,
	                        27,
	                        28,
	                        29,
	                        30,
	                        31,
	                        32,
	                        33,
	                        34,
	                        35,
	                        36,
	                        37,
	                        38,
	                        39,
	                        40,
	                        41,
	                        42,
	                        43,
	                        44,
	                        45,
	                        46,
	                        47,
	                        48,
	                        49,
	                        50
	                    ],
	                    "list_view_flag": 1
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 201019051,
	                    "quantity": 13
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
