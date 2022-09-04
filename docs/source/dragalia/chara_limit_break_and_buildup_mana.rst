/chara/limit_break_and_buildup_mana
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 42156f332fe00e7cd0833d02cdbf756429482b4ceda53471246a4ded78922de7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888846184132002	Request-Time: 1662304762	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 98

Request body
----------------

.. code-block:: json

	{
	    "chara_id": 10650501,
	    "next_limit_break_count": 4,
	    "mana_circle_piece_id_list": [
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
	    "is_use_grow_material": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1536	Expires: Sun, 04 Sep 2022 15:19:31 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:19:31 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "album_passive_notice": {
	                "is_update_chara": 1,
	                "is_update_dragon": 0
	            },
	            "chara_list": [
	                {
	                    "chara_id": 10650501,
	                    "rarity": 5,
	                    "exp": 1191950,
	                    "level": 80,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 4,
	                    "is_new": 1,
	                    "gettime": 1557305081,
	                    "skill_1_level": 3,
	                    "skill_2_level": 2,
	                    "ability_1_level": 2,
	                    "ability_2_level": 2,
	                    "ability_3_level": 2,
	                    "burst_attack_level": 2,
	                    "combo_buildup_count": 0,
	                    "hp": 801,
	                    "attack": 472,
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
	                    "material_id": 104001001,
	                    "quantity": 25
	                },
	                {
	                    "material_id": 104001052,
	                    "quantity": 351
	                },
	                {
	                    "material_id": 104001053,
	                    "quantity": 193
	                },
	                {
	                    "material_id": 104002051,
	                    "quantity": 0
	                },
	                {
	                    "material_id": 104002052,
	                    "quantity": 200
	                },
	                {
	                    "material_id": 104003002,
	                    "quantity": 2
	                }
	            ],
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jaysephine",
	                "level": 174,
	                "exp": 6181433,
	                "crystal": 14140,
	                "coin": 1663538245,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 400,
	                "main_party_no": 1,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 22219,
	                "mana_point": 8931316,
	                "dew_point": 849590,
	                "build_time_point": 1067,
	                "last_login_time": 1662304453,
	                "stamina_single": 13,
	                "last_stamina_single_update_time": 1662213130,
	                "stamina_single_surplus_second": 283,
	                "stamina_multi": 6,
	                "last_stamina_multi_update_time": 1662213130,
	                "stamina_multi_surplus_second": 3498,
	                "tutorial_status": 60999,
	                "tutorial_flag_list": [
	                    1001,
	                    1002,
	                    1003,
	                    1004,
	                    1005,
	                    1006,
	                    1007,
	                    1008,
	                    1009,
	                    1010,
	                    1011,
	                    1012,
	                    1013,
	                    1014,
	                    1015,
	                    1016,
	                    1017,
	                    1018,
	                    1019,
	                    1020,
	                    1021,
	                    1022,
	                    1023,
	                    1024,
	                    1025,
	                    1026,
	                    1027,
	                    1028,
	                    1029,
	                    1030
	                ],
	                "prologue_end_time": 1557120311,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1557120036
	            },
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 12
	            },
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
