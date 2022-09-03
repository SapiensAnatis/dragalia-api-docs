/dmode_dungeon/floor
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Relates to
-----------
Kaleidoscape

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
	Request-Token: 27886462796040525
	Request-Time: 1662162707
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 20


Request body
----------------

.. code-block:: json

	{
	    "dmode_play_record": null
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 2069
	Expires: Fri, 02 Sep 2022 23:51:49 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:51:49 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_dungeon_state": 5,
	        "dmode_floor_data": {
	            "unique_key": "66709573935_1662162703",
	            "floor_key": "cfb5ec8cc7a0a77d133e25793832310ef9658ebb",
	            "is_play_end": 0,
	            "is_view_area_start_equipment": 0,
	            "dmode_area_info": {
	                "floor_num": 1,
	                "quest_time": 0,
	                "dmode_score": 0,
	                "current_area_theme_id": 1,
	                "current_area_id": 102
	            },
	            "dmode_unit_info": {
	                "level": 1,
	                "exp": 0,
	                "dmode_hold_dragon_list": [],
	                "equip_crest_item_no_sort_list": [
	                    0,
	                    0,
	                    0
	                ],
	                "bag_item_no_sort_list": [
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0
	                ],
	                "skill_bag_item_no_sort_list": [
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0,
	                    0
	                ],
	                "take_dmode_point_1": 0,
	                "take_dmode_point_2": 0
	            },
	            "dmode_dungeon_odds": {
	                "dmode_odds_info": {
	                    "dmode_drop_obj": [
	                        {
	                            "dmode_drop_list": [
	                                {
	                                    "type": 13,
	                                    "id": 1001,
	                                    "quantity": 1
	                                }
	                            ],
	                            "obj_id": 1,
	                            "obj_type": 2
	                        },
	                        {
	                            "dmode_drop_list": [
	                                {
	                                    "type": 43,
	                                    "id": 3,
	                                    "quantity": 1
	                                },
	                                {
	                                    "type": 43,
	                                    "id": 4,
	                                    "quantity": 1
	                                },
	                                {
	                                    "type": 43,
	                                    "id": 5,
	                                    "quantity": 1
	                                }
	                            ],
	                            "obj_id": 2,
	                            "obj_type": 1
	                        },
	                        {
	                            "dmode_drop_list": [
	                                {
	                                    "type": 13,
	                                    "id": 1001,
	                                    "quantity": 1
	                                }
	                            ],
	                            "obj_id": 3,
	                            "obj_type": 2
	                        },
	                        {
	                            "dmode_drop_list": [
	                                {
	                                    "type": 13,
	                                    "id": 1001,
	                                    "quantity": 1
	                                }
	                            ],
	                            "obj_id": 4,
	                            "obj_type": 2
	                        }
	                    ],
	                    "dmode_enemy": [
	                        {
	                            "enemy_idx": 0,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010118,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 1,
	                            "is_pop": 1,
	                            "level": 3,
	                            "param_id": 231010118,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 2,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010211,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 3,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010118,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 4,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010513,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 5,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010612,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 6,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010716,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 7,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010211,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 8,
	                            "is_pop": 1,
	                            "level": 3,
	                            "param_id": 231010118,
	                            "dmode_drop_list": [
	                                {
	                                    "type": 43,
	                                    "id": 6,
	                                    "quantity": 1
	                                }
	                            ]
	                        },
	                        {
	                            "enemy_idx": 9,
	                            "is_pop": 1,
	                            "level": 3,
	                            "param_id": 231010211,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 10,
	                            "is_pop": 1,
	                            "level": 2,
	                            "param_id": 231010303,
	                            "dmode_drop_list": []
	                        },
	                        {
	                            "enemy_idx": 11,
	                            "is_pop": 1,
	                            "level": 3,
	                            "param_id": 231010612,
	                            "dmode_drop_list": [
	                                {
	                                    "type": 43,
	                                    "id": 7,
	                                    "quantity": 1
	                                }
	                            ]
	                        }
	                    ]
	                },
	                "dmode_dungeon_item_list": [
	                    {
	                        "item_no": 1,
	                        "item_id": 108405011,
	                        "item_state": 14,
	                        "option": []
	                    },
	                    {
	                        "item_no": 2,
	                        "item_id": 104403011,
	                        "item_state": 14,
	                        "option": []
	                    },
	                    {
	                        "item_no": 3,
	                        "item_id": 40020001,
	                        "item_state": 0,
	                        "option": {
	                            "strength_param_id": 4010103,
	                            "strength_ability_id": 4010115,
	                            "strength_skill_id": 0,
	                            "abnormal_status_invalid_count": 0
	                        }
	                    },
	                    {
	                        "item_no": 4,
	                        "item_id": 109502022,
	                        "item_state": 0,
	                        "option": []
	                    },
	                    {
	                        "item_no": 5,
	                        "item_id": 104501012,
	                        "item_state": 0,
	                        "option": []
	                    },
	                    {
	                        "item_no": 6,
	                        "item_id": 108305011,
	                        "item_state": 0,
	                        "option": []
	                    },
	                    {
	                        "item_no": 7,
	                        "item_id": 104501012,
	                        "item_state": 0,
	                        "option": []
	                    }
	                ],
	                "dmode_select_dragon_list": []
	            }
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
