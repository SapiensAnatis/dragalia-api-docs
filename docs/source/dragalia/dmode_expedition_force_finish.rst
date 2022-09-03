/dmode/expedition_force_finish
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27887241443412163	Request-Time: 1662209111	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1125	Expires: Sat, 03 Sep 2022 12:45:19 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 12:45:19 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_ingame_result": {
	            "floor_num": 0,
	            "is_record_floor_num": 0,
	            "chara_id_list": [
	                10150104,
	                0,
	                0,
	                0
	            ],
	            "reward_talisman_list": [],
	            "take_dmode_point_1": 0,
	            "take_dmode_point_2": 0,
	            "take_player_exp": 0,
	            "player_level_up_fstone": 0,
	            "quest_time": 0,
	            "is_view_quest_time": 0,
	            "dmode_score": 0,
	            "clear_state": 0
	        },
	        "dmode_expedition": {
	            "chara_id_1": 10150104,
	            "chara_id_2": 0,
	            "chara_id_3": 0,
	            "chara_id_4": 0,
	            "start_time": 1662209056,
	            "target_floor_num": 30,
	            "state": 1
	        },
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 97571459880,
	                "name": "Jay",
	                "level": 174,
	                "exp": 6179247,
	                "crystal": 13870,
	                "coin": 1664255200,
	                "max_dragon_quantity": 305,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 394,
	                "main_party_no": 2,
	                "emblem_id": 50004301,
	                "active_memory_event_id": 21404,
	                "mana_point": 9032108,
	                "dew_point": 922290,
	                "build_time_point": 1067,
	                "last_login_time": 1662204727,
	                "stamina_single": 41,
	                "last_stamina_single_update_time": 1662208876,
	                "stamina_single_surplus_second": 349,
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
