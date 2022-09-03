/shop/item_summon_exec
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com<device_id>
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
	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883499100834104
	Request-Time: 1661986056
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 68


Request body
----------------

.. code-block:: json

	{
	    "payment_type": 3,
	    "payment_target": {
	        "target_hold_quantity": 870,
	        "target_cost": 0
	    }
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 2665
	Expires: Wed, 31 Aug 2022 22:47:38 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:47:38 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "user_item_summon": {
	            "daily_summon_count": 1,
	            "last_summon_time": 1661986058
	        },
	        "item_summon_reward_list": [
	            {
	                "entity_type": 8,
	                "entity_id": 104001042,
	                "entity_quantity": 3
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 202004002,
	                "entity_quantity": 10
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 101001003,
	                "entity_quantity": 3
	            },
	            {
	                "entity_type": 4,
	                "entity_id": 0,
	                "entity_quantity": 5000
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 102001003,
	                "entity_quantity": 5
	            },
	            {
	                "entity_type": 4,
	                "entity_id": 0,
	                "entity_quantity": 5000
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 104001052,
	                "entity_quantity": 3
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 104002041,
	                "entity_quantity": 3
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 101001003,
	                "entity_quantity": 3
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 104002031,
	                "entity_quantity": 3
	            }
	        ],
	        "update_data_list": {
	            "shop_notice": {
	                "is_shop_notification": 0
	            },
	            "material_list": [
	                {
	                    "material_id": 101001003,
	                    "quantity": 17
	                },
	                {
	                    "material_id": 102001003,
	                    "quantity": 5
	                },
	                {
	                    "material_id": 104001042,
	                    "quantity": 3
	                },
	                {
	                    "material_id": 104001052,
	                    "quantity": 3
	                },
	                {
	                    "material_id": 104002031,
	                    "quantity": 3
	                },
	                {
	                    "material_id": 104002041,
	                    "quantity": 3
	                },
	                {
	                    "material_id": 202004002,
	                    "quantity": 10
	                }
	            ],
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 1,
	                "exp": 60,
	                "crystal": 870,
	                "coin": 1999991425,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 312,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 6114,
	                "dew_point": 600,
	                "build_time_point": 0,
	                "last_login_time": 1661979293,
	                "stamina_single": 138,
	                "last_stamina_single_update_time": 1661985465,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 12,
	                "last_stamina_multi_update_time": 1661897736,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 10601,
	                "tutorial_flag_list": [
	                    1002,
	                    1020,
	                    1022,
	                    1027
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1661897736
	            },
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
	                },
	                "daily_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 1,
	                    "new_complete_mission_id_list": [
	                        15070101
	                    ],
	                    "pickup_mission_count": 1,
	                    "all_mission_count": 10,
	                    "completed_mission_count": 2,
	                    "current_mission_id": 0
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
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
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
	                    "receivable_reward_count": 1,
	                    "new_complete_mission_id_list": [
	                        100100
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 54,
	                    "completed_mission_count": 2,
	                    "current_mission_id": 100200
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
