/ability_crest/reset_plus_count
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 42156f332fe00e7cd0833d02cdbf756429482b4ceda53471246a4ded78922de7	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888843986316700	Request-Time: 1662304631	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 46

Request body
----------------

.. code-block:: json

	{
	    "ability_crest_id": 40050010,
	    "plus_count_type_list": [
	        1
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 991	Expires: Sun, 04 Sep 2022 15:17:20 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:17:20 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "ability_crest_list": [
	                {
	                    "ability_crest_id": 40050010,
	                    "buildup_count": 0,
	                    "limit_break_count": 0,
	                    "equipable_count": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 50,
	                    "is_new": 1,
	                    "is_favorite": 0,
	                    "gettime": 1601459403
	                }
	            ],
	            "material_list": [
	                {
	                    "material_id": 122001001,
	                    "quantity": 3592
	                }
	            ],
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jaysephine",
	                "level": 174,
	                "exp": 6181433,
	                "crystal": 14140,
	                "coin": 1663578245,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 400,
	                "main_party_no": 1,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 22219,
	                "mana_point": 9042316,
	                "dew_point": 922590,
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
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------
