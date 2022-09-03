/dmode/get_data
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886464456984912	Request-Time: 1662162806	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 676	Expires: Fri, 02 Sep 2022 23:53:27 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Fri, 02 Sep 2022 23:53:27 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_dungeon_info": {
	            "chara_id": 10230501,
	            "floor_num": 2,
	            "quest_time": 57,
	            "dungeon_score": 1400,
	            "is_play_end": 0,
	            "state": 6
	        },
	        "dmode_chara_list": [
	            {
	                "chara_id": 10230501,
	                "max_floor_num": 0,
	                "select_servitor_id": 2,
	                "select_edit_skill_chara_id_1": 10840501,
	                "select_edit_skill_chara_id_2": 10440301,
	                "select_edit_skill_chara_id_3": 0,
	                "max_dmode_score": 0
	            }
	        ],
	        "dmode_servitor_passive_list": [],
	        "dmode_expedition": {
	            "chara_id_1": 0,
	            "chara_id_2": 0,
	            "chara_id_3": 0,
	            "chara_id_4": 0,
	            "start_time": 0,
	            "target_floor_num": 0,
	            "state": 1
	        },
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
	        "dmode_story_list": [],
	        "current_server_time": 1662162807,
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
