/present/receive
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com<device_id>
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
	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883470680230101
	Request-Time: 1661984363
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 63


Request body
----------------

.. code-block:: json

	{
	    "present_id_list": [
	        122414502,
	        122414501,
	        122414500,
	        122414499,
	        122414498,
	        122414482,
	        122414215
	    ],
	    "is_limit": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 1318
	Expires: Wed, 31 Aug 2022 22:19:25 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:19:25 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "present_limit_list": [
	            {
	                "present_id": 122414215,
	                "viewer_id": 66709573935,
	                "master_id": 630,
	                "state": 0,
	                "entity_type": 16,
	                "entity_id": 0,
	                "entity_quantity": 100,
	                "entity_level": 0,
	                "entity_limit_break_count": 0,
	                "entity_status_plus_count": 0,
	                "message_id": 1002000,
	                "message_param_value_1": 0,
	                "message_param_value_2": 0,
	                "message_param_value_3": 0,
	                "message_param_value_4": 0,
	                "extra_parameter_1": 0,
	                "extra_parameter_2": 0,
	                "extra_parameter_3": 0,
	                "extra_parameter_4": 0,
	                "extra_parameter_5": 0,
	                "create_time": 1661979293,
	                "receive_limit_time": 1662584099
	            }
	        ],
	        "receive_present_id_list": [
	            122414502,
	            122414501,
	            122414500,
	            122414499,
	            122414498,
	            122414482
	        ],
	        "not_receive_present_id_list": [
	            122414215
	        ],
	        "delete_present_id_list": [],
	        "limit_over_present_id_list": [],
	        "converted_entity_list": [],
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Euden",
	                "level": 1,
	                "exp": 30,
	                "crystal": 450,
	                "coin": 2000001215,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 312,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 547,
	                "dew_point": 0,
	                "build_time_point": 0,
	                "last_login_time": 1661979293,
	                "stamina_single": 18,
	                "last_stamina_single_update_time": 1661984335,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 12,
	                "last_stamina_multi_update_time": 1661897736,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 10401,
	                "tutorial_flag_list": [
	                    1020,
	                    1022
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1661897736
	            },
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 1
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
