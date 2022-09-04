/clb01_event/receive_clb01_point_reward
==================================================

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
	SID: 6324a591e02637df60f38339554fa633a0a05343d1a33a995aef6920096cd9c4
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27887236477356201
	Request-Time: 1662208815
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 13


Request body
----------------

.. code-block:: json

	{
	    "event_id": 21404
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 3120
	Expires: Sat, 03 Sep 2022 12:40:24 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Sat, 03 Sep 2022 12:40:24 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
		"data_headers": {
			"result_code": 1
		},
		"data": {
			"clb_01_event_reward_list": [
				{
					"event_id": 21404,
					"event_reward_id": 1
				},
				{
					"event_id": 21404,
					"event_reward_id": 2
				},
				{
					"event_id": 21404,
					"event_reward_id": 3
				},
				{
					"event_id": 21404,
					"event_reward_id": 4
				},
				{
					"event_id": 21404,
					"event_reward_id": 5
				},
				{
					"event_id": 21404,
					"event_reward_id": 6
				}
			],
			"clb_01_event_reward_entity_list": [
				{
					"entity_type": 18,
					"entity_id": 0,
					"entity_quantity": 3000
				},
				{
					"entity_type": 8,
					"entity_id": 101001002,
					"entity_quantity": 30
				},
				{
					"entity_type": 8,
					"entity_id": 104001041,
					"entity_quantity": 20
				},
				{
					"entity_type": 4,
					"entity_id": 0,
					"entity_quantity": 50000
				},
				{
					"entity_type": 8,
					"entity_id": 113001002,
					"entity_quantity": 20
				},
				{
					"entity_type": 37,
					"entity_id": 30150403,
					"entity_quantity": 1
				}
			],
			"update_data_list": {
				"user_data": {
					"viewer_id": 28894575482,
					"name": "Euden",
					"level": 60,
					"exp": 70040,
					"crystal": 8450,
					"coin": 2000152059,
					"max_dragon_quantity": 185,
					"max_weapon_quantity": 0,
					"max_amulet_quantity": 0,
					"quest_skip_point": 324,
					"main_party_no": 1,
					"emblem_id": 40000001,
					"active_memory_event_id": 21404,
					"mana_point": 8783,
					"dew_point": 1220,
					"build_time_point": 0,
					"last_login_time": 1662295186,
					"stamina_single": 996,
					"last_stamina_single_update_time": 1662300744,
					"stamina_single_surplus_second": 0,
					"stamina_multi": 99,
					"last_stamina_multi_update_time": 1662300102,
					"stamina_multi_surplus_second": 0,
					"tutorial_status": 60999,
					"tutorial_flag_list": [
						1001,
						1002,
						1004,
						1007,
						1010,
						1012,
						1014,
						1015,
						1019,
						1020,
						1021,
						1022,
						1023,
						1024
					],
					"prologue_end_time": 1662295246,
					"is_optin": 0,
					"fort_open_time": 1662300102,
					"create_time": 1662243929
				},
				"material_list": [
					{
						"material_id": 101001002,
						"quantity": 30
					},
					{
						"material_id": 104001041,
						"quantity": 20
					},
					{
						"material_id": 113001002,
						"quantity": 23
					}
				],
				"weapon_skin_list": [
					{
						"weapon_skin_id": 30150403,
						"is_new": 1,
						"gettime": 1662300796
					}
				],
				"functional_maintenance_list": [
				]
			},
			"entity_result": {
				"converted_entity_list": [
				]
			}
		}
	}

Notes
------
