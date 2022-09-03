/friend/set_support_chara
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
	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883481652529390
	Request-Time: 1661985016
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 320


Request body
----------------

.. code-block:: json

	{
	    "chara_id": 10130103,
	    "dragon_key_id": 0,
	    "weapon_key_id": 0,
	    "amulet_key_id": 0,
	    "amulet_2_key_id": 0,
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

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 1608
	Expires: Wed, 31 Aug 2022 22:30:18 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:30:18 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "result": 1,
	        "setting_support": {
	            "last_active_time": 1661984335,
	            "chara_id": 10130103,
	            "equip_dragon_key_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "user_level_group": 0
	        },
	        "update_data_list": {
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 1,
	                    "new_complete_mission_id_list": [
	                        10005101
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 222,
	                    "completed_mission_count": 5,
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
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
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
	        }
	    }
	}

Notes
------
