/mission/receive_drill_reward
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888784125201074	Request-Time: 1662301070	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 73

Request body
----------------

.. code-block:: json

	{
	    "drill_mission_id_list": [
	        100100,
	        100200,
	        100300,
	        100400
	    ],
	    "drill_mission_group_id_list": []
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 5589	Expires: Sun, 04 Sep 2022 14:17:51 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:17:51 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "drill_mission_list": [
	            {
	                "drill_mission_id": 100100,
	                "progress": 1,
	                "state": 2,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100200,
	                "progress": 1,
	                "state": 2,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100300,
	                "progress": 1,
	                "state": 2,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100400,
	                "progress": 1,
	                "state": 2,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100500,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100600,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100700,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100800,
	                "progress": 2,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 100900,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101000,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101100,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101200,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101300,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101400,
	                "progress": 2,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101500,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101600,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101700,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101800,
	                "progress": 10,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 101900,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102000,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102100,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102200,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102300,
	                "progress": 2,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102400,
	                "progress": 2,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102500,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102600,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102700,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102800,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 102900,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103000,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103100,
	                "progress": 10,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103200,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103300,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103400,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103500,
	                "progress": 10,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103600,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103700,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103800,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 103900,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104000,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104100,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104200,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104300,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104400,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104500,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104600,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104700,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104800,
	                "progress": 10,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 104900,
	                "progress": 1,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 105000,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 105100,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 105200,
	                "progress": 10,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 105300,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 105400,
	                "progress": 0,
	                "state": 0,
	                "start_date": 0,
	                "end_date": 0
	            },
	            {
	                "drill_mission_id": 105500,
	                "progress": 3,
	                "state": 1,
	                "start_date": 0,
	                "end_date": 0
	            }
	        ],
	        "not_received_mission_id_list": [],
	        "need_entry_event_id_list": [],
	        "converted_entity_list": [],
	        "drill_mission_group_list": [],
	        "update_data_list": {
	            "material_list": [
	                {
	                    "material_id": 101001003,
	                    "quantity": 18
	                }
	            ],
	            "user_data": {
	                "viewer_id": 28894575482,
	                "name": "Euden",
	                "level": 60,
	                "exp": 70040,
	                "crystal": 8450,
	                "coin": 2000167059,
	                "max_dragon_quantity": 185,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 21404,
	                "mana_point": 27783,
	                "dew_point": 1220,
	                "build_time_point": 0,
	                "last_login_time": 1662295186,
	                "stamina_single": 996,
	                "last_stamina_single_update_time": 1662300744,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 99,
	                "last_stamina_multi_update_time": 1662300102,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 60999,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1004,
	                    1007,
	                    1010,
	                    1012,
	                    1014,
	                    1015,
	                    1019,
	                    1020,
	                    1021,
	                    1022,
	                    1023,
	                    1024,
	                    1027
	                ],
	                "prologue_end_time": 1662295246,
	                "is_optin": 0,
	                "fort_open_time": 1662300102,
	                "create_time": 1662243929
	            },
	            "ability_crest_list": [
	                {
	                    "ability_crest_id": 40040001,
	                    "buildup_count": 0,
	                    "limit_break_count": 0,
	                    "equipable_count": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "is_new": 1,
	                    "is_favorite": 0,
	                    "gettime": 1662301071
	                }
	            ],
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 0,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0
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
	                    "is_update": 1,
	                    "receivable_reward_count": 0,
	                    "new_complete_mission_id_list": [],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 55,
	                    "completed_mission_count": 22,
	                    "current_mission_id": 100500
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
