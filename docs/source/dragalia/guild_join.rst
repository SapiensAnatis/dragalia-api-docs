/guild/join
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888797362424547	Request-Time: 1662301860	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 15

Request body
----------------

.. code-block:: json

	{
	    "guild_id": 87745518
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1188	Expires: Sun, 04 Sep 2022 14:31:01 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:31:01 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "guild_member_list": [
	            {
	                "viewer_id": 28894575482,
	                "user_name": "Euden",
	                "user_level": 60,
	                "max_party_power": 5738,
	                "profile_entity_type": 1,
	                "profile_entity_id": 10140101,
	                "profile_entity_rarity": 4,
	                "last_active_time": 1662300744,
	                "last_guild_active_time": 1662301841,
	                "last_attend_time": 0,
	                "guild_position_type": 3,
	                "temporary_end_time": 0
	            },
	            {
	                "viewer_id": 30305325753,
	                "user_name": "Sturmy",
	                "user_level": 23,
	                "max_party_power": 9632,
	                "profile_entity_type": 1,
	                "profile_entity_id": 10140101,
	                "profile_entity_rarity": 5,
	                "last_active_time": 1566625250,
	                "last_guild_active_time": 0,
	                "last_attend_time": 1565592941,
	                "guild_position_type": 1,
	                "temporary_end_time": 0
	            }
	        ],
	        "update_data_list": {
	            "user_guild_data": {
	                "guild_id": 87745518,
	                "guild_apply_id": 0,
	                "penalty_end_time": 0,
	                "guild_push_notification_type_running": 1,
	                "guild_push_notification_type_suspending": 1,
	                "profile_entity_type": 1,
	                "profile_entity_id": 10140101,
	                "profile_entity_rarity": 4,
	                "last_attend_time": 0,
	                "is_enable_invite_receive": 1,
	                "is_enable_invite_send": 0
	            },
	            "guild_data": {
	                "guild_id": 87745518,
	                "guild_name": "Pendragon",
	                "guild_emblem_id": 10008,
	                "guild_introduction": "role-play is important, but real life always comes first.",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 2,
	                "guild_board": "Let's seize the day!",
	                "is_penalty_guild_board": 0
	            },
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
