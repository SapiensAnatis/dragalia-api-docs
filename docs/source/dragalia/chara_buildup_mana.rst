/chara/buildup_mana
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 142f3eef616e3c196682f8a8b744773db057593eb3e238707c538acd7cd9c8e2	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886393741019242	Request-Time: 1662158590	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 65

Request body
----------------

.. code-block:: json

	{
	    "chara_id": 10140101,
	    "mana_circle_piece_id_list": [
	        7
	    ],
	    "is_use_grow_material": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 556	Expires: Fri, 02 Sep 2022 22:43:13 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Fri, 02 Sep 2022 22:43:13 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "party_power_data": {
	                "max_party_power": 1906
	            },
	            "chara_list": [
	                {
	                    "chara_id": 10140101,
	                    "rarity": 4,
	                    "exp": 4610,
	                    "level": 16,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 0,
	                    "is_new": 0,
	                    "gettime": 1661976574,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "ability_1_level": 0,
	                    "ability_2_level": 0,
	                    "ability_3_level": 0,
	                    "burst_attack_level": 1,
	                    "combo_buildup_count": 0,
	                    "hp": 129,
	                    "attack": 86,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 1,
	                    "mana_circle_piece_id_list": [
	                        7
	                    ],
	                    "list_view_flag": 1
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
