/friend/id_search
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888800852085493	Request-Time: 1662302068	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 20

Request body
----------------

.. code-block:: json

	{
	    "search_id": 98766658116
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1303	Expires: Sun, 04 Sep 2022 14:34:29 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:34:29 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "result": 1,
	        "search_user": {
	            "viewer_id": 98766658116,
	            "name": "die okda",
	            "level": 180,
	            "last_login_date": 1660931497,
	            "emblem_id": 50007102,
	            "max_party_power": 53379,
	            "support_chara": {
	                "chara_id": 10350502,
	                "level": 100,
	                "additional_max_level": 20,
	                "rarity": 5,
	                "element_type": 5,
	                "hp": 956,
	                "attack": 572,
	                "hp_plus_count": 100,
	                "attack_plus_count": 100,
	                "ability_1_level": 3,
	                "ability_2_level": 3,
	                "ability_3_level": 3,
	                "ex_ability_level": 5,
	                "ex_ability_2_level": 5,
	                "skill_1_level": 4,
	                "skill_2_level": 3,
	                "is_unlock_edit_skill": 0
	            },
	            "support_dragon": {
	                "dragon_key_id": 16728752,
	                "dragon_id": 20050520,
	                "level": 100,
	                "hp": 368,
	                "attack": 128,
	                "skill_1_level": 2,
	                "ability_1_level": 5,
	                "ability_2_level": 0,
	                "hp_plus_count": 0,
	                "attack_plus_count": 0,
	                "limit_break_count": 4
	            },
	            "support_weapon_body": {
	                "weapon_body_id": 30360501,
	                "buildup_count": 90,
	                "limit_break_count": 9,
	                "limit_over_count": 2,
	                "equipable_count": 2,
	                "additional_crest_slot_type_1_count": 1,
	                "additional_crest_slot_type_2_count": 0,
	                "additional_crest_slot_type_3_count": 2
	            },
	            "support_talisman": {
	                "talisman_key_id": 0
	            },
	            "support_crest_slot_type_1_list": [
	                {
	                    "ability_crest_id": 0
	                },
	                {
	                    "ability_crest_id": 0
	                },
	                {
	                    "ability_crest_id": 0
	                }
	            ],
	            "support_crest_slot_type_2_list": [
	                {
	                    "ability_crest_id": 0
	                },
	                {
	                    "ability_crest_id": 40030011,
	                    "buildup_count": 20,
	                    "limit_break_count": 4,
	                    "hp_plus_count": 50,
	                    "attack_plus_count": 50,
	                    "equipable_count": 4
	                }
	            ],
	            "support_crest_slot_type_3_list": [
	                {
	                    "ability_crest_id": 0
	                },
	                {
	                    "ability_crest_id": 0
	                }
	            ],
	            "guild": {
	                "guild_id": 19307778,
	                "guild_emblem_id": 10033,
	                "guild_name": "Trap Room",
	                "is_penalty_guild_name": 0
	            }
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
