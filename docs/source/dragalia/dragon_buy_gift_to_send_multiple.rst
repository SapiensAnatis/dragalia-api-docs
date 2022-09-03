/dragon/buy_gift_to_send_multiple
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
	Request-Token: 27886415064860788
	Request-Time: 1662159862
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 52


Request body
----------------

.. code-block:: json

	{
	    "dragon_id": 20040301,
	    "dragon_gift_id_list": [
	        20005,
	        10004,
	        10003,
	        10002,
	        10001
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Expires: Fri, 02 Sep 2022 23:04:24 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:04:24 GMT
	Content-Length: 3347
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "shop_gift_list": [
	            {
	                "dragon_gift_id": 10001,
	                "price": 0,
	                "is_buy": 0
	            },
	            {
	                "dragon_gift_id": 10002,
	                "price": 1500,
	                "is_buy": 0
	            },
	            {
	                "dragon_gift_id": 10003,
	                "price": 4000,
	                "is_buy": 0
	            },
	            {
	                "dragon_gift_id": 10004,
	                "price": 8000,
	                "is_buy": 0
	            },
	            {
	                "dragon_gift_id": 20005,
	                "price": 12000,
	                "is_buy": 0
	            }
	        ],
	        "dragon_gift_reward_list": [
	            {
	                "dragon_gift_id": 20005,
	                "return_gift_list": [
	                    {
	                        "entity_type": 8,
	                        "entity_id": 102001001,
	                        "entity_quantity": 4,
	                        "is_over": 0
	                    }
	                ],
	                "is_favorite": 0,
	                "reward_reliability_list": [
	                    {
	                        "levelup_entity_list": [
	                            {
	                                "entity_type": 0,
	                                "entity_id": 0,
	                                "entity_quantity": 0,
	                                "is_over": 0
	                            }
	                        ],
	                        "level": 5,
	                        "is_release_story": 1
	                    }
	                ]
	            },
	            {
	                "dragon_gift_id": 10004,
	                "return_gift_list": [
	                    {
	                        "entity_type": 18,
	                        "entity_id": 0,
	                        "entity_quantity": 500,
	                        "is_over": 0
	                    },
	                    {
	                        "entity_type": 8,
	                        "entity_id": 104001032,
	                        "entity_quantity": 1,
	                        "is_over": 0
	                    }
	                ],
	                "is_favorite": 0,
	                "reward_reliability_list": []
	            },
	            {
	                "dragon_gift_id": 10003,
	                "return_gift_list": [
	                    {
	                        "entity_type": 8,
	                        "entity_id": 201005001,
	                        "entity_quantity": 1,
	                        "is_over": 0
	                    },
	                    {
	                        "entity_type": 18,
	                        "entity_id": 0,
	                        "entity_quantity": 500,
	                        "is_over": 0
	                    }
	                ],
	                "is_favorite": 0,
	                "reward_reliability_list": [
	                    {
	                        "levelup_entity_list": [
	                            {
	                                "entity_type": 8,
	                                "entity_id": 201005001,
	                                "entity_quantity": 4,
	                                "is_over": 0
	                            }
	                        ],
	                        "level": 10,
	                        "is_release_story": 0
	                    }
	                ]
	            },
	            {
	                "dragon_gift_id": 10002,
	                "return_gift_list": [
	                    {
	                        "entity_type": 18,
	                        "entity_id": 0,
	                        "entity_quantity": 500,
	                        "is_over": 0
	                    }
	                ],
	                "is_favorite": 0,
	                "reward_reliability_list": []
	            },
	            {
	                "dragon_gift_id": 10001,
	                "return_gift_list": [
	                    {
	                        "entity_type": 18,
	                        "entity_id": 0,
	                        "entity_quantity": 1000,
	                        "is_over": 0
	                    }
	                ],
	                "is_favorite": 0,
	                "reward_reliability_list": []
	            }
	        ],
	        "dragon_contact_free_gift_count": 0,
	        "update_data_list": {
	            "dragon_reliability_list": [
	                {
	                    "dragon_id": 20040301,
	                    "gettime": 1661976574,
	                    "reliability_level": 11,
	                    "reliability_total_exp": 3200,
	                    "last_contact_time": 1662159863
	                }
	            ],
	            "dragon_gift_list": [],
	            "party_power_data": {
	                "max_party_power": 1992
	            },
	            "material_list": [
	                {
	                    "material_id": 102001001,
	                    "quantity": 4
	                },
	                {
	                    "material_id": 104001032,
	                    "quantity": 1
	                },
	                {
	                    "material_id": 201005001,
	                    "quantity": 5
	                }
	            ],
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 3,
	                "exp": 280,
	                "crystal": 895,
	                "coin": 1999967129,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 14995,
	                "dew_point": 1270,
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
	            "unit_story_list": [
	                {
	                    "unit_story_id": 210001011,
	                    "is_read": 0
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
	                    "receivable_reward_count": 2,
	                    "new_complete_mission_id_list": [
	                        101500,
	                        105400
	                    ],
	                    "pickup_mission_count": 0,
	                    "all_mission_count": 54,
	                    "completed_mission_count": 7,
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
