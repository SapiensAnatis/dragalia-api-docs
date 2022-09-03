/dungeon/get_area_odds
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
	Request-Token: 27883469891700943
	Request-Time: 1661984315
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 65


Request body
----------------

.. code-block:: json

	{
	    "dungeon_key": "af7704da374abb78c65e1aa00217f0de45f77c18",
	    "area_idx": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 513
	Expires: Wed, 31 Aug 2022 22:18:37 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:18:37 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "odds_info": {
	            "area_index": 1,
	            "reaction_obj_count": 1,
	            "drop_obj": [],
	            "enemy": [
	                {
	                    "param_id": 100010109,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [
	                                {
	                                    "type": 8,
	                                    "id": 101001001,
	                                    "quantity": 1,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 4,
	                                    "id": 0,
	                                    "quantity": 40,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 8,
	                                    "id": 202001001,
	                                    "quantity": 1,
	                                    "place": 0
	                                }
	                            ],
	                            "coin": 1,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 0
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 0,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 1
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 0,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 2
	                }
	            ],
	            "grade": []
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
