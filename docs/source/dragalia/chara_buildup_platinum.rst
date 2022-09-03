/chara/buildup_platinum
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
	Request-Token: 27886442160064757
	Request-Time: 1662161477
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 15


Request body
----------------

.. code-block:: json

	{
	    "chara_id": 10950503
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 2069
	Expires: Fri, 02 Sep 2022 23:31:19 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:31:19 GMT
	Connection: keep-alive


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
	                    "chara_id": 10950503,
	                    "rarity": 5,
	                    "exp": 1191950,
	                    "level": 80,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 4,
	                    "is_new": 1,
	                    "gettime": 1661976624,
	                    "skill_1_level": 3,
	                    "skill_2_level": 2,
	                    "ability_1_level": 2,
	                    "ability_2_level": 2,
	                    "ability_3_level": 2,
	                    "burst_attack_level": 2,
	                    "combo_buildup_count": 0,
	                    "hp": 752,
	                    "attack": 506,
	                    "ex_ability_level": 5,
	                    "ex_ability_2_level": 5,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
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
	                    "material_id": 125001001,
	                    "quantity": 0
	                }
	            ],
	            "unit_story_list": [
	                {
	                    "unit_story_id": 110404013,
	                    "is_read": 0
	                },
	                {
	                    "unit_story_id": 110404014,
	                    "is_read": 0
	                },
	                {
	                    "unit_story_id": 110404015,
	                    "is_read": 0
	                }
	            ],
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 40
	            },
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 10,
	                    "new_complete_mission_id_list": [
	                        10001201,
	                        10001301,
	                        10001401,
	                        10001501,
	                        10001601,
	                        10001002,
	                        10001003,
	                        10001004
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 235,
	                    "completed_mission_count": 28,
	                    "current_mission_id": 0
	                },
	                "daily_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "period_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "beginner_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "special_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 56,
	                    "completed_mission_count": 15,
	                    "current_mission_id": 0
	                },
	                "main_story_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "memory_event_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "drill_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 2,
	                    "new_complete_mission_id_list": [
	                        103700
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 54,
	                    "completed_mission_count": 11,
	                    "current_mission_id": 100300
	                },
	                "album_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                }
	            },
	            "current_main_story_mission": [],
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
