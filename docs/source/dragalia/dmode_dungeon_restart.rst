/dmode_dungeon/restart
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
	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886464926746962
	Request-Time: 1662162833
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 1


Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 739
	Expires: Fri, 02 Sep 2022 23:53:55 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:53:55 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_dungeon_state": 7,
	        "dmode_dungeon_info": {
	            "chara_id": 10230501,
	            "floor_num": 2,
	            "quest_time": 57,
	            "dungeon_score": 1400,
	            "is_play_end": 0,
	            "state": 7
	        },
	        "dmode_ingame_data": {
	            "recovery_count": 1,
	            "recovery_time": 1662162807,
	            "unique_key": "66709573935_1662162703",
	            "start_floor_num": 1,
	            "target_floor_num": 60,
	            "dmode_level_group_id": 1,
	            "unit_data": {
	                "chara_id": 10230501,
	                "dmode_chara_level_group_id": 1,
	                "skill_1_level": 3,
	                "skill_2_level": 2,
	                "ability_1_level": 2,
	                "ability_2_level": 2,
	                "ability_3_level": 1,
	                "ex_ability_level": 5,
	                "ex_ability_2_level": 5,
	                "burst_attack_level": 2,
	                "combo_buildup_count": 0
	            },
	            "servitor_id": 2,
	            "dmode_servitor_passive_list": []
	        },
	        "update_data_list": {
	            "dmode_info": {
	                "total_max_floor_num": 0,
	                "recovery_count": 1,
	                "recovery_time": 1662162807,
	                "floor_skip_count": 0,
	                "floor_skip_time": 0,
	                "dmode_point_1": 0,
	                "dmode_point_2": 0,
	                "is_entry": 1
	            },
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
