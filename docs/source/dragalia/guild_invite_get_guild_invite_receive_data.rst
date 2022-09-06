/guild_invite/get_guild_invite_receive_data
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
	SID: 1a5a3cb1aa568946e14a539ae29b79f74c58858365dc2bb0dbe8d8e5150215ed
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27886512456599724
	Request-Time: 1662165667
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
	Content-Length: 108
	Expires: Sat, 03 Sep 2022 00:41:09 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Sat, 03 Sep 2022 00:41:09 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
		"data_headers": {
			"result_code": 1
		},
		"data": {
			"guild_invite_receive_list": [
				{
					"guild_invite_id": 14171,
					"send_viewer_id": 49673150795,
					"send_user_name": "Timae",
					"send_max_party_power": 55684,
					"send_profile_entity_type": 1,
					"send_profile_entity_id": 10150204,
					"send_profile_entity_rarity": 5,
					"send_last_active_time": 1662307334,
					"guild_invite_message_id": 1,
					"guild_data": {
						"guild_id": 83132741,
						"guild_name": "DeryamiT",
						"guild_emblem_id": 10033,
						"guild_introduction": "Hello, hope we can help each other!",
						"joining_condition_type": 2,
						"activity_policy_type": 5,
						"is_penalty_guild_name": 0,
						"is_penalty_guild_introduction": 0,
						"guild_member_count": 25,
						"guild_board": "",
						"is_penalty_guild_board": 0
					}
				}
			],
			"update_data_list": {
				"functional_maintenance_list": [
				]
			}
		}
	}

Notes
------
