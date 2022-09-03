/dmode_dungeon/finish
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
	Request-Token: 27886465379731797
	Request-Time: 1662162860
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 15


Request body
----------------

.. code-block:: json

	{
	    "is_game_over": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 1503
	Expires: Fri, 02 Sep 2022 23:54:22 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:54:22 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_dungeon_state": 1,
	        "dmode_ingame_result": {
	            "floor_num": 1,
	            "is_record_floor_num": 1,
	            "chara_id_list": [
	                10230501
	            ],
	            "reward_talisman_list": [
	                {
	                    "talisman_id": 50230501,
	                    "talisman_ability_id_1": 0,
	                    "talisman_ability_id_2": 0,
	                    "talisman_ability_id_3": 0,
	                    "additional_hp": 100,
	                    "additional_attack": 100
	                }
	            ],
	            "take_dmode_point_1": 33,
	            "take_dmode_point_2": 0,
	            "take_player_exp": 0,
	            "player_level_up_fstone": 0,
	            "quest_time": 64,
	            "is_view_quest_time": 1,
	            "dmode_score": 1500,
	            "clear_state": 1
	        },
	        "dmode_dungeon_info": {
	            "chara_id": 10230501,
	            "floor_num": 0,
	            "quest_time": 0,
	            "dungeon_score": 0,
	            "is_play_end": 0,
	            "state": 1
	        },
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 5,
	                "exp": 790,
	                "crystal": 2119,
	                "coin": 2000418638,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 6,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 20841,
	                "mana_point": 44923,
	                "dew_point": 3170,
	                "build_time_point": 10,
	                "last_login_time": 1662158090,
	                "stamina_single": 250,
	                "last_stamina_single_update_time": 1662162305,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 65,
	                "last_stamina_multi_update_time": 1662162305,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 20501,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1009,
	                    1019,
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
	            "dmode_info": {
	                "total_max_floor_num": 1,
	                "recovery_count": 1,
	                "recovery_time": 1662162807,
	                "floor_skip_count": 0,
	                "floor_skip_time": 0,
	                "dmode_point_1": 33,
	                "dmode_point_2": 0,
	                "is_entry": 1
	            },
	            "talisman_list": [
	                {
	                    "talisman_key_id": 174172,
	                    "talisman_id": 50230501,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "talisman_ability_id_1": 0,
	                    "talisman_ability_id_2": 0,
	                    "talisman_ability_id_3": 0,
	                    "additional_hp": 100,
	                    "additional_attack": 100,
	                    "gettime": 1662162862
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
