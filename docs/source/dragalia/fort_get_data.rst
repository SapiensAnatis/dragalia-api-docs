/fort/get_data
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com
	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
	Accept: */*
	Accept-Encoding: deflate, gzip
	App-Ver: 2.19.0
	Device: 2
	Platform: 2
	Carrier: OnePlus
	DeviceId: <device_id>
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886414024673386
	Request-Time: 1662159799
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 1


Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 2276
	Expires: Fri, 02 Sep 2022 23:03:21 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:03:21 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "build_list": [
	            {
	                "build_id": 1376766,
	                "fort_plant_detail_id": 10010101,
	                "position_x": 16,
	                "position_z": 17,
	                "build_status": 0,
	                "build_start_date": 0,
	                "build_end_date": 0,
	                "level": 1,
	                "plant_id": 100101,
	                "is_new": 1,
	                "remain_time": 0,
	                "last_income_date": 1662159709,
	                "last_income_time": 92
	            },
	            {
	                "build_id": 1376767,
	                "fort_plant_detail_id": 10140101,
	                "position_x": 21,
	                "position_z": 3,
	                "build_status": 0,
	                "build_start_date": 0,
	                "build_end_date": 0,
	                "level": 1,
	                "plant_id": 101401,
	                "is_new": 1,
	                "remain_time": 0,
	                "last_income_date": -1
	            }
	        ],
	        "fort_detail": {
	            "max_carpenter_count": 5,
	            "carpenter_num": 2,
	            "working_carpenter_num": 0
	        },
	        "fort_bonus_list": {
	            "param_bonus": [
	                {
	                    "weapon_type": 1,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 2,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 3,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 4,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 5,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 6,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 7,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 8,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 9,
	                    "hp": 0,
	                    "attack": 0
	                }
	            ],
	            "param_bonus_by_weapon": [
	                {
	                    "weapon_type": 1,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 2,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 3,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 4,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 5,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 6,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 7,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 8,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "weapon_type": 9,
	                    "hp": 0,
	                    "attack": 0
	                }
	            ],
	            "element_bonus": [
	                {
	                    "elemental_type": 1,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 2,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 3,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 4,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 5,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 99,
	                    "hp": 0,
	                    "attack": 0
	                }
	            ],
	            "chara_bonus_by_album": [
	                {
	                    "elemental_type": 1,
	                    "hp": 0.8,
	                    "attack": 0.8
	                },
	                {
	                    "elemental_type": 2,
	                    "hp": 0.7,
	                    "attack": 0.7
	                },
	                {
	                    "elemental_type": 3,
	                    "hp": 0.9,
	                    "attack": 0.9
	                },
	                {
	                    "elemental_type": 4,
	                    "hp": 0.8,
	                    "attack": 0.8
	                },
	                {
	                    "elemental_type": 5,
	                    "hp": 0.7,
	                    "attack": 0.7
	                },
	                {
	                    "elemental_type": 99,
	                    "hp": 0,
	                    "attack": 0
	                }
	            ],
	            "all_bonus": {
	                "hp": 0,
	                "attack": 0
	            },
	            "dragon_bonus": [
	                {
	                    "elemental_type": 1,
	                    "dragon_bonus": 0,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 2,
	                    "dragon_bonus": 0,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 3,
	                    "dragon_bonus": 0,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 4,
	                    "dragon_bonus": 0,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 5,
	                    "dragon_bonus": 0,
	                    "hp": 0,
	                    "attack": 0
	                },
	                {
	                    "elemental_type": 99,
	                    "dragon_bonus": 0,
	                    "hp": 0,
	                    "attack": 0
	                }
	            ],
	            "dragon_bonus_by_album": [
	                {
	                    "elemental_type": 1,
	                    "hp": 0.5,
	                    "attack": 0.5
	                },
	                {
	                    "elemental_type": 2,
	                    "hp": 0.3,
	                    "attack": 0.3
	                },
	                {
	                    "elemental_type": 3,
	                    "hp": 0.5,
	                    "attack": 0.5
	                },
	                {
	                    "elemental_type": 4,
	                    "hp": 0.3,
	                    "attack": 0.3
	                },
	                {
	                    "elemental_type": 5,
	                    "hp": 0.3,
	                    "attack": 0.3
	                },
	                {
	                    "elemental_type": 99,
	                    "hp": 0,
	                    "attack": 0
	                }
	            ],
	            "dragon_time_bonus": {
	                "dragon_time_bonus": 0
	            }
	        },
	        "production_rp": {
	            "speed": 0,
	            "max": 0
	        },
	        "production_df": {
	            "speed": 0,
	            "max": 0
	        },
	        "production_st": {
	            "speed": 0.03,
	            "max": 144
	        },
	        "dragon_contact_free_gift_count": 1,
	        "current_server_time": 1662159801,
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
