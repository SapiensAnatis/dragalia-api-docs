/dragon/buy_gift_to_send
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888801539951355	Request-Time: 1662302108	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 34

Request body
----------------

.. code-block:: json

	{
	    "dragon_id": 20030502,
	    "dragon_gift_id": 10001
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1569	Expires: Sun, 04 Sep 2022 14:35:10 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:35:10 GMT	Connection: keep-alive

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
	                "is_buy": 1
	            },
	            {
	                "dragon_gift_id": 10003,
	                "price": 4000,
	                "is_buy": 0
	            },
	            {
	                "dragon_gift_id": 10004,
	                "price": 8000,
	                "is_buy": 1
	            },
	            {
	                "dragon_gift_id": 20006,
	                "price": 15000,
	                "is_buy": 1
	            }
	        ],
	        "return_gift_list": [
	            {
	                "entity_type": 18,
	                "entity_id": 0,
	                "entity_quantity": 500,
	                "is_over": 0
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201005001,
	                "entity_quantity": 2,
	                "is_over": 0
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 104001052,
	                "entity_quantity": 1,
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
	        ],
	        "dragon_contact_free_gift_count": 0,
	        "update_data_list": {
	            "dragon_reliability_list": [
	                {
	                    "dragon_id": 20030502,
	                    "gettime": 1662244194,
	                    "reliability_level": 5,
	                    "reliability_total_exp": 700,
	                    "last_contact_time": 1662302110
	                }
	            ],
	            "dragon_gift_list": [],
	            "party_power_data": {
	                "max_party_power": 5738
	            },
	            "user_data": {
	                "viewer_id": 28894575482,
	                "name": "Euden",
	                "level": 60,
	                "exp": 70040,
	                "crystal": 10225,
	                "coin": 2000163059,
	                "max_dragon_quantity": 185,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 324,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 21404,
	                "mana_point": 79783,
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
	                    1013,
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
	            "material_list": [
	                {
	                    "material_id": 104001052,
	                    "quantity": 1
	                },
	                {
	                    "material_id": 201005001,
	                    "quantity": 2
	                }
	            ],
	            "unit_story_list": [
	                {
	                    "unit_story_id": 210066011,
	                    "is_read": 0
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
