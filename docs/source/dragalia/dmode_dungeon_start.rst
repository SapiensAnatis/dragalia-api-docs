/dmode_dungeon/start
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886466403141976	Request-Time: 1662162922	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 87

Request body
----------------

.. code-block:: json

	{
	    "chara_id": 10950503,
	    "start_floor_num": 1,
	    "servitor_id": 2,
	    "bring_edit_skill_chara_id_list": [
	        10840501,
	        10440301
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 502	Expires: Fri, 02 Sep 2022 23:55:24 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Fri, 02 Sep 2022 23:55:24 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_dungeon_state": 2,
	        "dmode_ingame_data": {
	            "recovery_count": 1,
	            "recovery_time": 1662162807,
	            "unique_key": "66709573935_1662162924",
	            "start_floor_num": 1,
	            "target_floor_num": 60,
	            "dmode_level_group_id": 1,
	            "unit_data": {
	                "chara_id": 10950503,
	                "dmode_chara_level_group_id": 1,
	                "skill_1_level": 3,
	                "skill_2_level": 2,
	                "ability_1_level": 2,
	                "ability_2_level": 2,
	                "ability_3_level": 2,
	                "ex_ability_level": 5,
	                "ex_ability_2_level": 5,
	                "burst_attack_level": 2,
	                "combo_buildup_count": 0
	            },
	            "servitor_id": 2,
	            "dmode_servitor_passive_list": []
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
