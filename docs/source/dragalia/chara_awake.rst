/chara/awake
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886418537744517	Request-Time: 1662160069	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 28

Request body
----------------

.. code-block:: json

	{
	    "chara_id": 10330101,
	    "next_rarity": 4
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 2214	Expires: Fri, 02 Sep 2022 23:07:50 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Fri, 02 Sep 2022 23:07:50 GMT	Connection: keep-alive

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
	                    "chara_id": 10330101,
	                    "rarity": 4,
	                    "exp": 0,
	                    "level": 1,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 0,
	                    "is_new": 1,
	                    "gettime": 1661976630,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "ability_1_level": 0,
	                    "ability_2_level": 0,
	                    "ability_3_level": 0,
	                    "burst_attack_level": 0,
	                    "combo_buildup_count": 0,
	                    "hp": 55,
	                    "attack": 32,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [],
	                    "list_view_flag": 1
	                }
	            ],
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 3,
	                "exp": 280,
	                "crystal": 894,
	                "coin": 1999970689,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 14995,
	                "dew_point": 3170,
	                "build_time_point": 0,
	                "last_login_time": 1662158090,
	                "stamina_single": 180,
	                "last_stamina_single_update_time": 1662159096,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 36,
	                "last_stamina_multi_update_time": 1662159096,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 11101,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1020,
	                    1022,
	                    1023,
	                    1027
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 1662159858,
	                "create_time": 1661897736
	            },
	            "mission_notice": {
	                "normal_mission_notice": {
	                    "is_update": 1,
	                    "receivable_reward_count": 2,
	                    "new_complete_mission_id_list": [
	                        10000601
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 225,
	                    "completed_mission_count": 13,
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
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
