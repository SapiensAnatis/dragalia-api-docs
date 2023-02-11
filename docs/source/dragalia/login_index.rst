/login/index
=======================

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
	SID: 6b4a7cb93afcd1c848e76c8062d88e963a3ba8ae04f3bbe0c1d107b9dee39fff
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883444893649156
	Request-Time: 1661982823
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 29


Request body
----------------

.. code-block:: json

	{
	    "jws_result": "7: NETWORK_ERROR"
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 49
	Expires: Wed, 31 Aug 2022 21:53:47 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 21:53:47 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
		"data_headers": {
			"result_code": 1
		},
		"data": {
			"login_bonus_list": [
				{
					"reward_code": 1,
					"login_bonus_id": 17,
					"total_login_day": 540,
					"reward_day": 0,
					"entity_type": 0,
					"entity_id": 0,
					"entity_quantity": 0,
					"entity_level": 0,
					"entity_limit_break_count": 0
				},
				{
					"reward_code": 1,
					"login_bonus_id": 74,
					"total_login_day": 2,
					"reward_day": 0,
					"entity_type": 0,
					"entity_id": 0,
					"entity_quantity": 0,
					"entity_level": 0,
					"entity_limit_break_count": 0
				}
			],
			"login_lottery_reward_list": [
				[
				]
			],
			"dragon_contact_free_gift_count": 1,
			"monthly_wall_receive_list": [
				{
					"quest_group_id": 21601,
					"is_receive_reward": 2
				}
			],
			"penalty_data": [
			],
			"exchange_summom_point_list": [
			],
			"before_exchange_summon_item_quantity": 0,
			"server_time": 1648506926,
			"update_data_list": {
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

Notice: The response data was captured from an iOS device, which passed the safety check, while the request comes from an Android device that failed it. Yes, "summom_point" is the correct key name.
