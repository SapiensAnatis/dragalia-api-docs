/shop/normal_shop_purchase
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
	Request-Token: 27883489135167761
	Request-Time: 1661985463
	Content-Type: application/octet-stream
	X-Unity-Version: 2019.4.31f1
	Content-Length: 124


Request body
----------------

.. code-block:: json

	null

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 784
	Expires: Wed, 31 Aug 2022 22:37:45 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:37:45 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "normal_shop_purchase": [
	            {
	                "goods_id": 20001,
	                "last_buy_time": 1661985465,
	                "effect_start_time": 0,
	                "effect_end_time": 0,
	                "buy_count": 1
	            }
	        ],
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Eudenh",
	                "level": 1,
	                "exp": 60,
	                "crystal": 570,
	                "coin": 1999981425,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 312,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 1114,
	                "dew_point": 600,
	                "build_time_point": 0,
	                "last_login_time": 1661979293,
	                "stamina_single": 138,
	                "last_stamina_single_update_time": 1661985465,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 12,
	                "last_stamina_multi_update_time": 1661897736,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 10601,
	                "tutorial_flag_list": [
	                    1002,
	                    1020,
	                    1022,
	                    1027
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1661897736
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
