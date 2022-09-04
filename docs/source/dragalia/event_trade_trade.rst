/event_trade/trade
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 3a274ffeda4fcd1bab0359046ee101be73db0fc79d52b437c6ff591f2a31f9f5	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888871366723741	Request-Time: 1662306261	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 46

Request body
----------------

.. code-block:: json

	{
	    "trade_group_id": 10701,
	    "trade_id": 107011202,
	    "trade_count": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 8984	Expires: Sun, 04 Sep 2022 15:44:31 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:44:31 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "user_event_item_data": [],
	        "user_event_trade_list": [
	            {
	                "event_trade_id": 107010102,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107010103,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107010104,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107010107,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107010108,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107010109,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107011101,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107011202,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107011501,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107011602,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107011702,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107011901,
	                "trade_count": 1
	            },
	            {
	                "event_trade_id": 107012106,
	                "trade_count": 2
	            },
	            {
	                "event_trade_id": 107012107,
	                "trade_count": 4
	            },
	            {
	                "event_trade_id": 107012109,
	                "trade_count": 0
	            }
	        ],
	        "event_trade_list": [
	            {
	                "event_trade_id": 107011102,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011102,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10150201,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011201,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011201,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10240101,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011301,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011301,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10340101,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011302,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011302,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10340502,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011401,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011401,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10440301,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011402,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011402,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10450303,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011502,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011502,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10540201,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011601,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011601,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10640401,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011701,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011701,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10740202,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011801,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011801,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10840501,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107011802,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107011802,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 1,
	                "destination_entity_type": 36,
	                "destination_entity_id": 10840403,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 50
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012101,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 100100,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 0,
	                "destination_entity_type": 8,
	                "destination_entity_id": 101001003,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 5
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012102,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 100200,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 0,
	                "destination_entity_type": 8,
	                "destination_entity_id": 102001003,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 5
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012103,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 100300,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 0,
	                "destination_entity_type": 8,
	                "destination_entity_id": 103001003,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 5
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012104,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 100400,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 0,
	                "destination_entity_type": 8,
	                "destination_entity_id": 113001003,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 5
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012105,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 100700,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 0,
	                "destination_entity_type": 18,
	                "destination_entity_id": 0,
	                "destination_entity_quantity": 50000,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 5
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012108,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 2,
	                "priority": 107012108,
	                "commence_date": 0,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 0,
	                "limit": 4,
	                "destination_entity_type": 8,
	                "destination_entity_id": 104003001,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 20
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012109,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 100500,
	                "commence_date": 1606456800,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 6,
	                "limit": 100,
	                "destination_entity_type": 4,
	                "destination_entity_id": 0,
	                "destination_entity_quantity": 30000,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 5
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012111,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 100,
	                "commence_date": 1606456800,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 6,
	                "limit": 2,
	                "destination_entity_type": 8,
	                "destination_entity_id": 201012001,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 300
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012112,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 200,
	                "commence_date": 1606456800,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 6,
	                "limit": 2,
	                "destination_entity_type": 8,
	                "destination_entity_id": 201011001,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 300
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012113,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 300,
	                "commence_date": 1606456800,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 6,
	                "limit": 20,
	                "destination_entity_type": 8,
	                "destination_entity_id": 104001001,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 30
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012114,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 400,
	                "commence_date": 1606456800,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 6,
	                "limit": 20,
	                "destination_entity_type": 8,
	                "destination_entity_id": 202004003,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 30
	                    }
	                ]
	            },
	            {
	                "event_trade_id": 107012115,
	                "trade_group_id": 10701,
	                "read_story_count": 0,
	                "tab_group_id": 1,
	                "priority": 500,
	                "commence_date": 1606456800,
	                "complete_date": 0,
	                "is_lock_view": 0,
	                "clear_target_quest_id": 0,
	                "reset_type": 6,
	                "limit": 3,
	                "destination_entity_type": 8,
	                "destination_entity_id": 202004004,
	                "destination_entity_quantity": 1,
	                "need_entity_list": [
	                    {
	                        "entity_type": 36,
	                        "entity_id": 223010101,
	                        "entity_quantity": 150
	                    }
	                ]
	            }
	        ],
	        "update_data_list": {
	            "battle_royal_chara_skin_list": [
	                {
	                    "battle_royal_chara_skin_id": 10250403,
	                    "gettime": 1662306271
	                }
	            ],
	            "battle_royal_event_item_list": [
	                {
	                    "event_id": 22301,
	                    "item_id": 10140101,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10140503,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10230201,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10250403,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10330301,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10430401,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10530501,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10550101,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10630201,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10650303,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10730501,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10750504,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10830301,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10930401,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 10950401,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010101,
	                    "quantity": 265
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010201,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010202,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010203,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010204,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010205,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010206,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010207,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010208,
	                    "quantity": 1
	                },
	                {
	                    "event_id": 22301,
	                    "item_id": 223010209,
	                    "quantity": 1
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
