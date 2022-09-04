/dmode/entry
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888776625785495	Request-Time: 1662300623	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 476	Expires: Sun, 04 Sep 2022 14:10:25 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:10:25 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "dmode_dungeon_info": {
	            "chara_id": 0,
	            "floor_num": 0,
	            "quest_time": 0,
	            "dungeon_score": 0,
	            "is_play_end": 0,
	            "state": 1
	        },
	        "dmode_chara_list": [],
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
	            "recovery_count": 0,
	            "recovery_time": 0,
	            "floor_skip_count": 0,
	            "floor_skip_time": 0,
	            "dmode_point_1": 0,
	            "dmode_point_2": 0,
	            "is_entry": 1
	        },
	        "dmode_story_list": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
