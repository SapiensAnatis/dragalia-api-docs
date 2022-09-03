/matching/get_room_list
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
	Request-Token: 27886454407432498
	Request-Time: 1662162206
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 37


Request body
----------------

.. code-block:: json

	{
	    "region": "usw",
	    "tab_type": 3,
	    "compatible_id": 36
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 4847
	Expires: Fri, 02 Sep 2022 23:43:28 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:43:28 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "room_list": [
	            {
	                "room_id": 911948,
	                "room_name": "7942ce2a-c0ac-4e41-8472-0cf5918f3953",
	                "region": "usw",
	                "cluster_name": "usw",
	                "language": "en_us",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 25768895,
	                "host_viewer_id": 67360270076,
	                "host_name": "Irzendal",
	                "host_level": 223,
	                "leader_chara_id": 10140101,
	                "leader_chara_level": 100,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550501,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 67360270076,
	                        "party_no_list": [
	                            54
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    },
	                    {
	                        "viewer_id": 96497712067,
	                        "party_no_list": [
	                            4
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662160789,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": []
	                },
	                "compatible_id": 36,
	                "member_num": 2
	            },
	            {
	                "room_id": 9677158,
	                "room_name": "7fc46e80-118b-4add-b0e8-8aeee25b4781",
	                "region": "usw",
	                "cluster_name": "usw",
	                "language": "en_us",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 17150800,
	                "host_viewer_id": 44018812036,
	                "host_name": "Euden",
	                "host_level": 202,
	                "leader_chara_id": 10650501,
	                "leader_chara_level": 100,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550604,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 44018812036,
	                        "party_no_list": [
	                            6
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    },
	                    {
	                        "viewer_id": 23285164327,
	                        "party_no_list": [
	                            6
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662162168,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": []
	                },
	                "compatible_id": 36,
	                "member_num": 2
	            },
	            {
	                "room_id": 3635352,
	                "room_name": "972ce17c-4cf8-4779-ba75-abd238a68e19",
	                "region": "jp",
	                "cluster_name": "jp",
	                "language": "zh_tw",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 0,
	                "host_viewer_id": 98323380300,
	                "host_name": "\u5c24\u5e1d\u723e",
	                "host_level": 177,
	                "leader_chara_id": 10550203,
	                "leader_chara_level": 100,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550401,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 98323380300,
	                        "party_no_list": [
	                            1
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    },
	                    {
	                        "viewer_id": 15821005846,
	                        "party_no_list": [
	                            1
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    },
	                    {
	                        "viewer_id": 86163255677,
	                        "party_no_list": [
	                            49
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662162180,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": []
	                },
	                "compatible_id": 36,
	                "member_num": 3
	            },
	            {
	                "room_id": 3659224,
	                "room_name": "617004ff-3f01-4b69-b592-3538d9cbfe0f",
	                "region": "usw",
	                "cluster_name": "usw",
	                "language": "en_us",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 62085274,
	                "host_viewer_id": 82739314244,
	                "host_name": "Euden",
	                "host_level": 193,
	                "leader_chara_id": 10950501,
	                "leader_chara_level": 80,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550302,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 82739314244,
	                        "party_no_list": [
	                            6
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662162193,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": [
	                        1,
	                        2,
	                        3,
	                        4
	                    ]
	                },
	                "compatible_id": 36,
	                "member_num": 1
	            },
	            {
	                "room_id": 3010587,
	                "room_name": "6e210042-4ec4-42ef-843a-aab90cb8fe86",
	                "region": "jp",
	                "cluster_name": "jp",
	                "language": "ja_jp",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 32626605,
	                "host_viewer_id": 52385820328,
	                "host_name": "\u30a8\u30bc\u611b\u597d\u5bb6",
	                "host_level": 208,
	                "leader_chara_id": 10750505,
	                "leader_chara_level": 80,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550302,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 52385820328,
	                        "party_no_list": [
	                            7
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662162200,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": []
	                },
	                "compatible_id": 36,
	                "member_num": 1
	            },
	            {
	                "room_id": 8964657,
	                "room_name": "7569ee1d-59e4-4ba2-92ec-7154881efc58",
	                "region": "jp",
	                "cluster_name": "jp",
	                "language": "ja_jp",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 0,
	                "host_viewer_id": 17882114310,
	                "host_name": "\u30e6\u30fc\u30c7\u30a3\u30eb",
	                "host_level": 173,
	                "leader_chara_id": 10150502,
	                "leader_chara_level": 80,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550302,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 17882114310,
	                        "party_no_list": [
	                            5
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662162202,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": []
	                },
	                "compatible_id": 36,
	                "member_num": 1
	            },
	            {
	                "room_id": 6296245,
	                "room_name": "4f4d9f4f-f174-4313-9a11-252f80a1d528",
	                "region": "usw",
	                "cluster_name": "usw",
	                "language": "en_us",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 54124212,
	                "host_viewer_id": 40136160951,
	                "host_name": "Simon",
	                "host_level": 160,
	                "leader_chara_id": 10150504,
	                "leader_chara_level": 80,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550401,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 40136160951,
	                        "party_no_list": [
	                            1
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    },
	                    {
	                        "viewer_id": 16099774964,
	                        "party_no_list": [
	                            9
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662162207,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": []
	                },
	                "compatible_id": 36,
	                "member_num": 2
	            },
	            {
	                "room_id": 495614,
	                "room_name": "0eb0bfcb-8404-45ea-b6ab-eb69ded6526e",
	                "region": "jp",
	                "cluster_name": "jp",
	                "language": "ja_jp",
	                "status": 1,
	                "entry_type": 1,
	                "entry_guild_id": 37261016,
	                "host_viewer_id": 88561147611,
	                "host_name": "\u30a8\u30b3\u30fc\u30c7\u30eb\u30bf",
	                "host_level": 180,
	                "leader_chara_id": 10150502,
	                "leader_chara_level": 100,
	                "leader_chara_rarity": 5,
	                "quest_id": 204550302,
	                "quest_type": 1,
	                "room_member_list": [
	                    {
	                        "viewer_id": 88561147611,
	                        "party_no_list": [
	                            19
	                        ],
	                        "is_first_clear": 0,
	                        "is_clear_party": 0
	                    }
	                ],
	                "start_entry_time": 1662162207,
	                "entry_conditions": {
	                    "objective_text_id": 0,
	                    "unaccepted_weapon_type_list": [],
	                    "required_party_power": 0,
	                    "unaccepted_element_type_list": []
	                },
	                "compatible_id": 36,
	                "member_num": 1
	            }
	        ],
	        "friend_room_list": [],
	        "event_room_list": [],
	        "event_friend_room_list": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
