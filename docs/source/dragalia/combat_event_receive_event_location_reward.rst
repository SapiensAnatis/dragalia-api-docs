/combat_event/receive_event_location_reward
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887259965458699	Request-Time: 1662210216	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 43

Request body
----------------

.. code-block:: json

	{
	    "event_id": 22224,
	    "event_location_reward_id": 2222402
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1621	Expires: Sat, 03 Sep 2022 13:03:44 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 13:03:44 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "user_event_location_reward_list": [
	            {
	                "event_id": 22224,
	                "location_reward_id": 2222402
	            }
	        ],
	        "event_location_reward_entity_list": [
	            {
	                "entity_type": 34,
	                "entity_id": 2222401,
	                "entity_quantity": 150
	            },
	            {
	                "entity_type": 34,
	                "entity_id": 2222403,
	                "entity_quantity": 1
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 202004004,
	                "entity_quantity": 1
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201009001,
	                "entity_quantity": 100
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201009002,
	                "entity_quantity": 50
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201009003,
	                "entity_quantity": 20
	            },
	            {
	                "entity_type": 4,
	                "entity_id": 0,
	                "entity_quantity": 10000
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 102001003,
	                "entity_quantity": 10
	            },
	            {
	                "entity_type": 8,
	                "entity_id": 201005001,
	                "entity_quantity": 20
	            }
	        ],
	        "update_data_list": {
	            "combat_event_user_list": [
	                {
	                    "event_id": 22224,
	                    "event_point": 4200,
	                    "exchange_item_01": 172,
	                    "quest_unlock_item_01": 3,
	                    "story_unlock_item_01": 1,
	                    "advent_item_01": 1
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 102001003,
	                    "quantity": 19120
	                },
	                {
	                    "material_id": 201005001,
	                    "quantity": 8919
	                },
	                {
	                    "material_id": 201009001,
	                    "quantity": 42493
	                },
	                {
	                    "material_id": 201009002,
	                    "quantity": 12112
	                },
	                {
	                    "material_id": 201009003,
	                    "quantity": 11642
	                },
	                {
	                    "material_id": 202004004,
	                    "quantity": 567
	                }
	            ],
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jay",
	                "level": 174,
	                "exp": 6179403,
	                "crystal": 13870,
	                "coin": 1664261778,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 394,
	                "main_party_no": 2,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 22224,
	                "mana_point": 9039322,
	                "dew_point": 922290,
	                "build_time_point": 1067,
	                "last_login_time": 1662204727,
	                "stamina_single": 36,
	                "last_stamina_single_update_time": 1662210188,
	                "stamina_single_surplus_second": 221,
	                "stamina_multi": 5,
	                "last_stamina_multi_update_time": 1662207177,
	                "stamina_multi_surplus_second": 1145,
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
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
