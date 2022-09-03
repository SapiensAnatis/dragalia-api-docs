/battle_royal_event/receive_event_cycle_point_reward
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
	Request-Token: 27883454104340658
	Request-Time: 1661983376
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 29


Request body
----------------

.. code-block:: json

	{
	    "event_id": 22301,
	    "event_cycle_id": 0
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 176
	Expires: Wed, 31 Aug 2022 22:02:58 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:02:58 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
		"data_headers": {
			"result_code": 1
		},
		"data": {
			"event_cycle_reward_list": [
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22001
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22002
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22003
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22004
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22005
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22006
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22007
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22008
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22009
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22010
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22011
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22012
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22013
				},
				{
					"event_id": 22301,
					"event_cycle_id": 22301022,
					"event_cycle_reward_id": 22014
				}
			],
			"event_cycle_reward_entity_list": [
			],
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
