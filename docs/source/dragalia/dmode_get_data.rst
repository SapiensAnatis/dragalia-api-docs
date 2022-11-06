/dmode/get_data
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
	SID: 31b6ad12f3268a17000cb8d9ab010a46a1728266b069dd7b26dd307d65b5c4a2
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886464456984912
	Request-Time: 1662162806
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
	Content-Length: 676
	Expires: Fri, 02 Sep 2022 23:53:27 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Fri, 02 Sep 2022 23:53:27 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	  "data_headers": {
	    "result_code": 1
	  },
	  "data": {
	    "dmode_dungeon_info": {
	      "chara_id": 10950101,
	      "floor_num": 0,
	      "quest_time": 0,
	      "dungeon_score": 0,
	      "is_play_end": 0,
	      "state": 1
	    },
	    "dmode_chara_list": [
	      {
		"chara_id": 10150102,
		"max_floor_num": 50,
		"select_servitor_id": 1,
		"select_edit_skill_chara_id_1": 10250203,
		"select_edit_skill_chara_id_2": 10650505,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 975100
	      },
	      {
		"chara_id": 10150201,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 974950
	      },
	      {
		"chara_id": 10150301,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10250203,
		"select_edit_skill_chara_id_2": 10650505,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1009050
	      },
	      {
		"chara_id": 10150303,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850502,
		"select_edit_skill_chara_id_2": 10650505,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 918250
	      },
	      {
		"chara_id": 10150306,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10250203,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1125550
	      },
	      {
		"chara_id": 10150404,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 810150
	      },
	      {
		"chara_id": 10150501,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 677000
	      },
	      {
		"chara_id": 10150503,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10540402,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 991400
	      },
	      {
		"chara_id": 10150504,
		"max_floor_num": 60,
		"select_servitor_id": 1,
		"select_edit_skill_chara_id_1": 10850402,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 904800
	      },
	      {
		"chara_id": 10250201,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850502,
		"select_edit_skill_chara_id_2": 10850402,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 999700
	      },
	      {
		"chara_id": 10250203,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850402,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 828650
	      },
	      {
		"chara_id": 10250204,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10950403,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 903000
	      },
	      {
		"chara_id": 10250402,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 703600
	      },
	      {
		"chara_id": 10250403,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 779700
	      },
	      {
		"chara_id": 10250501,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 953850
	      },
	      {
		"chara_id": 10250504,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 907750
	      },
	      {
		"chara_id": 10350301,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10850402,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 993850
	      },
	      {
		"chara_id": 10350302,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 817100
	      },
	      {
		"chara_id": 10350303,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1028350
	      },
	      {
		"chara_id": 10450104,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850402,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 924100
	      },
	      {
		"chara_id": 10450203,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10840501,
		"select_edit_skill_chara_id_2": 10440301,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 784100
	      },
	      {
		"chara_id": 10450305,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1101900
	      },
	      {
		"chara_id": 10550101,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10840102,
		"select_edit_skill_chara_id_2": 10840402,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1674000
	      },
	      {
		"chara_id": 10550204,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1025500
	      },
	      {
		"chara_id": 10550401,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850502,
		"select_edit_skill_chara_id_2": 10750201,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 763100
	      },
	      {
		"chara_id": 10550405,
		"max_floor_num": 31,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10250203,
		"select_edit_skill_chara_id_2": 10840402,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 53300
	      },
	      {
		"chara_id": 10550501,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 671350
	      },
	      {
		"chara_id": 10650202,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 676400
	      },
	      {
		"chara_id": 10650203,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 895250
	      },
	      {
		"chara_id": 10750204,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850502,
		"select_edit_skill_chara_id_2": 10650505,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 607100
	      },
	      {
		"chara_id": 10750501,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 696200
	      },
	      {
		"chara_id": 10850102,
		"max_floor_num": 50,
		"select_servitor_id": 1,
		"select_edit_skill_chara_id_1": 10250203,
		"select_edit_skill_chara_id_2": 10650505,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 874250
	      },
	      {
		"chara_id": 10850402,
		"max_floor_num": 60,
		"select_servitor_id": 1,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 845250
	      },
	      {
		"chara_id": 10950101,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850402,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 848250
	      },
	      {
		"chara_id": 10950103,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10540402,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 970550
	      },
	      {
		"chara_id": 10950302,
		"max_floor_num": 31,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10540402,
		"select_edit_skill_chara_id_2": 10650505,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1400
	      },
	      {
		"chara_id": 10950303,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10250203,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 909200
	      },
	      {
		"chara_id": 10950401,
		"max_floor_num": 60,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10650505,
		"select_edit_skill_chara_id_2": 10850502,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1117150
	      },
	      {
		"chara_id": 10950403,
		"max_floor_num": 50,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10850502,
		"select_edit_skill_chara_id_2": 10650505,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 1021100
	      },
	      {
		"chara_id": 10950501,
		"max_floor_num": 49,
		"select_servitor_id": 2,
		"select_edit_skill_chara_id_1": 10250203,
		"select_edit_skill_chara_id_2": 10840102,
		"select_edit_skill_chara_id_3": 0,
		"max_dmode_score": 584550
	      }
	    ],
	    "dmode_servitor_passive_list": [
	      {
		"passive_no": 1,
		"passive_level": 10
	      },
	      {
		"passive_no": 2,
		"passive_level": 19
	      },
	      {
		"passive_no": 3,
		"passive_level": 10
	      },
	      {
		"passive_no": 4,
		"passive_level": 12
	      },
	      {
		"passive_no": 5,
		"passive_level": 20
	      },
	      {
		"passive_no": 6,
		"passive_level": 10
	      },
	      {
		"passive_no": 7,
		"passive_level": 10
	      },
	      {
		"passive_no": 8,
		"passive_level": 10
	      },
	      {
		"passive_no": 9,
		"passive_level": 10
	      },
	      {
		"passive_no": 10,
		"passive_level": 10
	      },
	      {
		"passive_no": 11,
		"passive_level": 1
	      },
	      {
		"passive_no": 12,
		"passive_level": 1
	      },
	      {
		"passive_no": 13,
		"passive_level": 10
	      },
	      {
		"passive_no": 14,
		"passive_level": 10
	      },
	      {
		"passive_no": 15,
		"passive_level": 1
	      },
	      {
		"passive_no": 16,
		"passive_level": 1
	      },
	      {
		"passive_no": 17,
		"passive_level": 1
	      }
	    ],
	    "dmode_expedition": {
	      "chara_id_1": 10150104,
	      "chara_id_2": 10150103,
	      "chara_id_3": 10150102,
	      "chara_id_4": 10150101,
	      "start_time": 1662209613,
	      "target_floor_num": 30,
	      "state": 1
	    },
	    "dmode_info": {
	      "total_max_floor_num": 60,
	      "recovery_count": 2,
	      "recovery_time": 1662306212,
	      "floor_skip_count": 2,
	      "floor_skip_time": 1662307205,
	      "dmode_point_1": 6133,
	      "dmode_point_2": 706,
	      "is_entry": 1
	    },
	    "dmode_story_list": [
	      {
		"dmode_story_id": 1,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 2,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 3,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 4,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 5,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 6,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 7,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 8,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 9,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 10,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 11,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 12,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 13,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 14,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 15,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 16,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 17,
		"is_read": 1
	      },
	      {
		"dmode_story_id": 18,
		"is_read": 1
	      }
	    ],
	    "current_server_time": 1667698847,
	    "update_data_list": {
	      "functional_maintenance_list": []
	    }
	  }
	}

Notes
------
