/quest/read_story
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
	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883452879603885
	Request-Time: 1661983302
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 21


Request body
----------------

.. code-block:: json

	{
	    "quest_story_id": 2230101
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 767
	Expires: Wed, 31 Aug 2022 22:01:44 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:01:44 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "quest_story_reward_list": [],
	        "converted_entity_list": [],
	        "update_data_list": {
	            "quest_story_list": [
	                {
	                    "quest_story_id": 2230101,
	                    "state": 1
	                }
	            ],
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Euden",
	                "level": 1,
	                "exp": 0,
	                "crystal": 400,
	                "coin": 2000001000,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 312,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 500,
	                "dew_point": 0,
	                "build_time_point": 0,
	                "last_login_time": 1661979293,
	                "stamina_single": 18,
	                "last_stamina_single_update_time": 1661897736,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 12,
	                "last_stamina_multi_update_time": 1661897736,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 10301,
	                "tutorial_flag_list": [
	                    1020,
	                    1022
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1661897736
	            },
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": [],
				"new_get_entity_list": [
					{
						"entity_type": 1,
						"entity_id": 10540201
					}
				]
	        }
	    }
	}

Notes
------
