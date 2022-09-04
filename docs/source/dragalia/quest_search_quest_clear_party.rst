/quest/search_quest_clear_party
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 3a274ffeda4fcd1bab0359046ee101be73db0fc79d52b437c6ff591f2a31f9f5	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888878513817788	Request-Time: 1662306687	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 127

Request body
----------------

.. code-block:: json

	{
	    "quest_id": 232011101,
	    "party_switch_no": 1,
	    "chara_id_list": [
	        10150306,
	        10350303,
	        10550306,
	        10850301
	    ],
	    "dragon_id_list": null,
	    "weapon_body_id_list": null,
	    "ability_crest_id_list": null
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 21596	Expires: Sun, 04 Sep 2022 15:51:38 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 15:51:38 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "search_quest_clear_party_list": [
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50750304,
	                        "equip_crest_slot_type_1_crest_id_1": 40050153,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050073,
	                        "equip_crest_slot_type_2_crest_id_1": 40040042,
	                        "equip_crest_slot_type_2_crest_id_2": 40040080,
	                        "equip_crest_slot_type_3_crest_id_1": 40090002,
	                        "equip_crest_slot_type_3_crest_id_2": 40090025,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10250203,
	                        "equip_talisman_ability_id_1": 340000008,
	                        "equip_talisman_ability_id_2": 340000056,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50350303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050069,
	                        "equip_crest_slot_type_1_crest_id_2": 40050121,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040083,
	                        "equip_crest_slot_type_2_crest_id_2": 40040097,
	                        "equip_crest_slot_type_3_crest_id_1": 40090026,
	                        "equip_crest_slot_type_3_crest_id_2": 40090014,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10550101,
	                        "equip_talisman_ability_id_1": 340000010,
	                        "equip_talisman_ability_id_2": 340000110,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50450304,
	                        "equip_crest_slot_type_1_crest_id_1": 40050034,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050091,
	                        "equip_crest_slot_type_2_crest_id_1": 40040106,
	                        "equip_crest_slot_type_2_crest_id_2": 40040102,
	                        "equip_crest_slot_type_3_crest_id_1": 40090019,
	                        "equip_crest_slot_type_3_crest_id_2": 40090006,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10540402,
	                        "equip_talisman_ability_id_1": 340000007,
	                        "equip_talisman_ability_id_2": 340000084,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050308,
	                        "equip_talisman_id": 50550302,
	                        "equip_crest_slot_type_1_crest_id_1": 40050008,
	                        "equip_crest_slot_type_1_crest_id_2": 40050060,
	                        "equip_crest_slot_type_1_crest_id_3": 40050020,
	                        "equip_crest_slot_type_2_crest_id_1": 40040082,
	                        "equip_crest_slot_type_2_crest_id_2": 40040062,
	                        "equip_crest_slot_type_3_crest_id_1": 40090010,
	                        "equip_crest_slot_type_3_crest_id_2": 40090018,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000118,
	                        "equip_talisman_ability_id_2": 340000107,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50150304,
	                        "equip_crest_slot_type_1_crest_id_1": 40050128,
	                        "equip_crest_slot_type_1_crest_id_2": 40050061,
	                        "equip_crest_slot_type_1_crest_id_3": 40050153,
	                        "equip_crest_slot_type_2_crest_id_1": 40040018,
	                        "equip_crest_slot_type_2_crest_id_2": 40040068,
	                        "equip_crest_slot_type_3_crest_id_1": 40090007,
	                        "equip_crest_slot_type_3_crest_id_2": 40090019,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10250402,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000038,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050315,
	                        "equip_talisman_id": 50150305,
	                        "equip_crest_slot_type_1_crest_id_1": 40050150,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050086,
	                        "equip_crest_slot_type_2_crest_id_1": 40040068,
	                        "equip_crest_slot_type_2_crest_id_2": 40030019,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090012,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000058,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50350303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050150,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050121,
	                        "equip_crest_slot_type_2_crest_id_1": 40040082,
	                        "equip_crest_slot_type_2_crest_id_2": 40030019,
	                        "equip_crest_slot_type_3_crest_id_1": 40090002,
	                        "equip_crest_slot_type_3_crest_id_2": 40090006,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000010,
	                        "equip_talisman_ability_id_2": 340000079,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050313,
	                        "equip_talisman_id": 50850301,
	                        "equip_crest_slot_type_1_crest_id_1": 40050097,
	                        "equip_crest_slot_type_1_crest_id_2": 40050020,
	                        "equip_crest_slot_type_1_crest_id_3": 40050008,
	                        "equip_crest_slot_type_2_crest_id_1": 40040062,
	                        "equip_crest_slot_type_2_crest_id_2": 40030004,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090012,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000133,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860301,
	                        "equip_dragon_id": 20050302,
	                        "equip_talisman_id": 50950303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050070,
	                        "equip_crest_slot_type_1_crest_id_2": 40050060,
	                        "equip_crest_slot_type_1_crest_id_3": 40050028,
	                        "equip_crest_slot_type_2_crest_id_1": 40040062,
	                        "equip_crest_slot_type_2_crest_id_2": 40030011,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090022,
	                        "edit_skill_1_chara_id": 10850402,
	                        "edit_skill_2_chara_id": 10950403,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000109,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50150306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050061,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050091,
	                        "equip_crest_slot_type_2_crest_id_1": 40040068,
	                        "equip_crest_slot_type_2_crest_id_2": 40040018,
	                        "equip_crest_slot_type_3_crest_id_1": 40090001,
	                        "equip_crest_slot_type_3_crest_id_2": 40090007,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10350204,
	                        "equip_talisman_ability_id_1": 340000010,
	                        "equip_talisman_ability_id_2": 340000060,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50550304,
	                        "equip_crest_slot_type_1_crest_id_1": 40050121,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050070,
	                        "equip_crest_slot_type_2_crest_id_1": 40040008,
	                        "equip_crest_slot_type_2_crest_id_2": 40030011,
	                        "equip_crest_slot_type_3_crest_id_1": 40090002,
	                        "equip_crest_slot_type_3_crest_id_2": 40090013,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000119,
	                        "equip_talisman_ability_id_2": 340000132,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50350303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050128,
	                        "equip_crest_slot_type_1_crest_id_2": 40050121,
	                        "equip_crest_slot_type_1_crest_id_3": 40050004,
	                        "equip_crest_slot_type_2_crest_id_1": 40040097,
	                        "equip_crest_slot_type_2_crest_id_2": 40040083,
	                        "equip_crest_slot_type_3_crest_id_1": 40090001,
	                        "equip_crest_slot_type_3_crest_id_2": 40090025,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000119,
	                        "equip_talisman_ability_id_2": 340000132,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50550201,
	                        "equip_crest_slot_type_1_crest_id_1": 40050153,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050073,
	                        "equip_crest_slot_type_2_crest_id_1": 40040042,
	                        "equip_crest_slot_type_2_crest_id_2": 40040080,
	                        "equip_crest_slot_type_3_crest_id_1": 40090002,
	                        "equip_crest_slot_type_3_crest_id_2": 40090025,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10250203,
	                        "equip_talisman_ability_id_1": 340000116,
	                        "equip_talisman_ability_id_2": 340000035,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50350302,
	                        "equip_crest_slot_type_1_crest_id_1": 40050069,
	                        "equip_crest_slot_type_1_crest_id_2": 40050121,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040083,
	                        "equip_crest_slot_type_2_crest_id_2": 40020003,
	                        "equip_crest_slot_type_3_crest_id_1": 40090026,
	                        "equip_crest_slot_type_3_crest_id_2": 40090014,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10550101,
	                        "equip_talisman_ability_id_1": 340000065,
	                        "equip_talisman_ability_id_2": 340000035,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50230101,
	                        "equip_crest_slot_type_1_crest_id_1": 40050034,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050035,
	                        "equip_crest_slot_type_2_crest_id_1": 40040106,
	                        "equip_crest_slot_type_2_crest_id_2": 40040102,
	                        "equip_crest_slot_type_3_crest_id_1": 40090019,
	                        "equip_crest_slot_type_3_crest_id_2": 40090006,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10540402,
	                        "equip_talisman_ability_id_1": 340000064,
	                        "equip_talisman_ability_id_2": 340000085,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050308,
	                        "equip_talisman_id": 50550101,
	                        "equip_crest_slot_type_1_crest_id_1": 40050008,
	                        "equip_crest_slot_type_1_crest_id_2": 40050060,
	                        "equip_crest_slot_type_1_crest_id_3": 40050020,
	                        "equip_crest_slot_type_2_crest_id_1": 40020003,
	                        "equip_crest_slot_type_2_crest_id_2": 40040062,
	                        "equip_crest_slot_type_3_crest_id_1": 40090027,
	                        "equip_crest_slot_type_3_crest_id_2": 40090018,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000064,
	                        "equip_talisman_ability_id_2": 340000106,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050308,
	                        "equip_talisman_id": 50450305,
	                        "equip_crest_slot_type_1_crest_id_1": 40050036,
	                        "equip_crest_slot_type_1_crest_id_2": 40050060,
	                        "equip_crest_slot_type_1_crest_id_3": 40050086,
	                        "equip_crest_slot_type_2_crest_id_1": 40040063,
	                        "equip_crest_slot_type_2_crest_id_2": 40030011,
	                        "equip_crest_slot_type_3_crest_id_1": 40090029,
	                        "equip_crest_slot_type_3_crest_id_2": 40090018,
	                        "edit_skill_1_chara_id": 10250203,
	                        "edit_skill_2_chara_id": 10550401,
	                        "equip_talisman_ability_id_1": 340000068,
	                        "equip_talisman_ability_id_2": 340000037,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050315,
	                        "equip_talisman_id": 50450305,
	                        "equip_crest_slot_type_1_crest_id_1": 40050128,
	                        "equip_crest_slot_type_1_crest_id_2": 40050145,
	                        "equip_crest_slot_type_1_crest_id_3": 40050042,
	                        "equip_crest_slot_type_2_crest_id_1": 40040080,
	                        "equip_crest_slot_type_2_crest_id_2": 40040042,
	                        "equip_crest_slot_type_3_crest_id_1": 40090006,
	                        "equip_crest_slot_type_3_crest_id_2": 40090018,
	                        "edit_skill_1_chara_id": 10250203,
	                        "edit_skill_2_chara_id": 10550101,
	                        "equip_talisman_ability_id_1": 340000099,
	                        "equip_talisman_ability_id_2": 340000058,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50250301,
	                        "equip_crest_slot_type_1_crest_id_1": 40050121,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050034,
	                        "equip_crest_slot_type_2_crest_id_1": 40040102,
	                        "equip_crest_slot_type_2_crest_id_2": 40040072,
	                        "equip_crest_slot_type_3_crest_id_1": 40090012,
	                        "equip_crest_slot_type_3_crest_id_2": 40090023,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000049,
	                        "equip_talisman_ability_id_2": 340000087,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50350504,
	                        "equip_crest_slot_type_1_crest_id_1": 40050121,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050105,
	                        "equip_crest_slot_type_2_crest_id_1": 40040083,
	                        "equip_crest_slot_type_2_crest_id_2": 40040097,
	                        "equip_crest_slot_type_3_crest_id_1": 40090021,
	                        "equip_crest_slot_type_3_crest_id_2": 40090012,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000017,
	                        "equip_talisman_ability_id_2": 340000126,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50350303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050128,
	                        "equip_crest_slot_type_1_crest_id_2": 40050145,
	                        "equip_crest_slot_type_1_crest_id_3": 40050136,
	                        "equip_crest_slot_type_2_crest_id_1": 40040068,
	                        "equip_crest_slot_type_2_crest_id_2": 40040042,
	                        "equip_crest_slot_type_3_crest_id_1": 40090013,
	                        "equip_crest_slot_type_3_crest_id_2": 40090025,
	                        "edit_skill_1_chara_id": 10250203,
	                        "edit_skill_2_chara_id": 10250504,
	                        "equip_talisman_ability_id_1": 340000008,
	                        "equip_talisman_ability_id_2": 340000059,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50550302,
	                        "equip_crest_slot_type_1_crest_id_1": 40050128,
	                        "equip_crest_slot_type_1_crest_id_2": 40050115,
	                        "equip_crest_slot_type_1_crest_id_3": 40050039,
	                        "equip_crest_slot_type_2_crest_id_1": 40040102,
	                        "equip_crest_slot_type_2_crest_id_2": 40040068,
	                        "equip_crest_slot_type_3_crest_id_1": 40090021,
	                        "equip_crest_slot_type_3_crest_id_2": 40090019,
	                        "edit_skill_1_chara_id": 10250203,
	                        "edit_skill_2_chara_id": 10550101,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000086,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50350304,
	                        "equip_crest_slot_type_1_crest_id_1": 40050121,
	                        "equip_crest_slot_type_1_crest_id_2": 40050128,
	                        "equip_crest_slot_type_1_crest_id_3": 40050150,
	                        "equip_crest_slot_type_2_crest_id_1": 40040083,
	                        "equip_crest_slot_type_2_crest_id_2": 40040097,
	                        "equip_crest_slot_type_3_crest_id_1": 40090019,
	                        "equip_crest_slot_type_3_crest_id_2": 40090001,
	                        "edit_skill_1_chara_id": 10250203,
	                        "edit_skill_2_chara_id": 10550101,
	                        "equip_talisman_ability_id_1": 340000010,
	                        "equip_talisman_ability_id_2": 340000037,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860301,
	                        "equip_dragon_id": 20050308,
	                        "equip_talisman_id": 50950302,
	                        "equip_crest_slot_type_1_crest_id_1": 40050008,
	                        "equip_crest_slot_type_1_crest_id_2": 40050020,
	                        "equip_crest_slot_type_1_crest_id_3": 40050031,
	                        "equip_crest_slot_type_2_crest_id_1": 40040062,
	                        "equip_crest_slot_type_2_crest_id_2": 40030011,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090011,
	                        "edit_skill_1_chara_id": 10540402,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000069,
	                        "equip_talisman_ability_id_2": 340000107,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50150306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050061,
	                        "equip_crest_slot_type_1_crest_id_2": 40050150,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040072,
	                        "equip_crest_slot_type_2_crest_id_2": 40040068,
	                        "equip_crest_slot_type_3_crest_id_1": 40090021,
	                        "equip_crest_slot_type_3_crest_id_2": 40090006,
	                        "edit_skill_1_chara_id": 10250203,
	                        "edit_skill_2_chara_id": 10950503,
	                        "equip_talisman_ability_id_1": 340000030,
	                        "equip_talisman_ability_id_2": 340000132,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50350303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050077,
	                        "equip_crest_slot_type_1_crest_id_2": 40050121,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040083,
	                        "equip_crest_slot_type_2_crest_id_2": 40040097,
	                        "equip_crest_slot_type_3_crest_id_1": 40090006,
	                        "equip_crest_slot_type_3_crest_id_2": 40090018,
	                        "edit_skill_1_chara_id": 10950301,
	                        "edit_skill_2_chara_id": 10150202,
	                        "equip_talisman_ability_id_1": 340000019,
	                        "equip_talisman_ability_id_2": 340000036,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50550306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050150,
	                        "equip_crest_slot_type_1_crest_id_2": 40050121,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040102,
	                        "equip_crest_slot_type_2_crest_id_2": 40040063,
	                        "equip_crest_slot_type_3_crest_id_1": 40090021,
	                        "equip_crest_slot_type_3_crest_id_2": 40090019,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000069,
	                        "equip_talisman_ability_id_2": 340000132,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050302,
	                        "equip_talisman_id": 50850301,
	                        "equip_crest_slot_type_1_crest_id_1": 40050060,
	                        "equip_crest_slot_type_1_crest_id_2": 40050008,
	                        "equip_crest_slot_type_1_crest_id_3": 40050020,
	                        "equip_crest_slot_type_2_crest_id_1": 40040062,
	                        "equip_crest_slot_type_2_crest_id_2": 40030011,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090027,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000119,
	                        "equip_talisman_ability_id_2": 340000132,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50150306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050042,
	                        "equip_crest_slot_type_1_crest_id_2": 40050145,
	                        "equip_crest_slot_type_1_crest_id_3": 40050146,
	                        "equip_crest_slot_type_2_crest_id_1": 40040068,
	                        "equip_crest_slot_type_2_crest_id_2": 40040042,
	                        "equip_crest_slot_type_3_crest_id_1": 40090012,
	                        "equip_crest_slot_type_3_crest_id_2": 40090023,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10250203,
	                        "equip_talisman_ability_id_1": 340000010,
	                        "equip_talisman_ability_id_2": 340000128,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50550306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050034,
	                        "equip_crest_slot_type_1_crest_id_2": 40050146,
	                        "equip_crest_slot_type_1_crest_id_3": 40050086,
	                        "equip_crest_slot_type_2_crest_id_1": 40040102,
	                        "equip_crest_slot_type_2_crest_id_2": 40040068,
	                        "equip_crest_slot_type_3_crest_id_1": 40090026,
	                        "equip_crest_slot_type_3_crest_id_2": 40090027,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000057,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050315,
	                        "equip_talisman_id": 50350303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050115,
	                        "equip_crest_slot_type_1_crest_id_2": 40050069,
	                        "equip_crest_slot_type_1_crest_id_3": 40050146,
	                        "equip_crest_slot_type_2_crest_id_1": 40040083,
	                        "equip_crest_slot_type_2_crest_id_2": 40040072,
	                        "equip_crest_slot_type_3_crest_id_1": 40090004,
	                        "equip_crest_slot_type_3_crest_id_2": 40090012,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000134,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050308,
	                        "equip_talisman_id": 50850302,
	                        "equip_crest_slot_type_1_crest_id_1": 40050060,
	                        "equip_crest_slot_type_1_crest_id_2": 40050151,
	                        "equip_crest_slot_type_1_crest_id_3": 40050100,
	                        "equip_crest_slot_type_2_crest_id_1": 40040082,
	                        "equip_crest_slot_type_2_crest_id_2": 40040068,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090029,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000007,
	                        "equip_talisman_ability_id_2": 340000039,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050315,
	                        "equip_talisman_id": 50150306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050146,
	                        "equip_crest_slot_type_1_crest_id_2": 40050153,
	                        "equip_crest_slot_type_1_crest_id_3": 40050136,
	                        "equip_crest_slot_type_2_crest_id_1": 40040018,
	                        "equip_crest_slot_type_2_crest_id_2": 40040080,
	                        "equip_crest_slot_type_3_crest_id_1": 40090025,
	                        "equip_crest_slot_type_3_crest_id_2": 40090013,
	                        "edit_skill_1_chara_id": 10250402,
	                        "edit_skill_2_chara_id": 10550101,
	                        "equip_talisman_ability_id_1": 340000099,
	                        "equip_talisman_ability_id_2": 340000132,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50350303,
	                        "equip_crest_slot_type_1_crest_id_1": 40050121,
	                        "equip_crest_slot_type_1_crest_id_2": 40050002,
	                        "equip_crest_slot_type_1_crest_id_3": 40050146,
	                        "equip_crest_slot_type_2_crest_id_1": 40040083,
	                        "equip_crest_slot_type_2_crest_id_2": 40040097,
	                        "equip_crest_slot_type_3_crest_id_1": 40090021,
	                        "equip_crest_slot_type_3_crest_id_2": 40090006,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000020,
	                        "equip_talisman_ability_id_2": 340000134,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50550306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050002,
	                        "equip_crest_slot_type_1_crest_id_2": 40050146,
	                        "equip_crest_slot_type_1_crest_id_3": 40050034,
	                        "equip_crest_slot_type_2_crest_id_1": 40040063,
	                        "equip_crest_slot_type_2_crest_id_2": 40040068,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090022,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000049,
	                        "equip_talisman_ability_id_2": 340000133,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050308,
	                        "equip_talisman_id": 50650304,
	                        "equip_crest_slot_type_1_crest_id_1": 40050015,
	                        "equip_crest_slot_type_1_crest_id_2": 40050020,
	                        "equip_crest_slot_type_1_crest_id_3": 40050100,
	                        "equip_crest_slot_type_2_crest_id_1": 40040082,
	                        "equip_crest_slot_type_2_crest_id_2": 40040062,
	                        "equip_crest_slot_type_3_crest_id_1": 40090018,
	                        "equip_crest_slot_type_3_crest_id_2": 40090006,
	                        "edit_skill_1_chara_id": 10250203,
	                        "edit_skill_2_chara_id": 10840501,
	                        "equip_talisman_ability_id_1": 340000068,
	                        "equip_talisman_ability_id_2": 340000109,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            },
	            {
	                "archive_party_unit_list": [
	                    {
	                        "unit_no": 1,
	                        "chara_id": 10150306,
	                        "equip_weapon_body_id": 30160304,
	                        "equip_dragon_id": 20050320,
	                        "equip_talisman_id": 50150301,
	                        "equip_crest_slot_type_1_crest_id_1": 40050042,
	                        "equip_crest_slot_type_1_crest_id_2": 40050145,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040057,
	                        "equip_crest_slot_type_2_crest_id_2": 40040063,
	                        "equip_crest_slot_type_3_crest_id_1": 40090012,
	                        "equip_crest_slot_type_3_crest_id_2": 40090020,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000098,
	                        "equip_talisman_ability_id_2": 340000132,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 2,
	                        "chara_id": 10850301,
	                        "equip_weapon_body_id": 30860304,
	                        "equip_dragon_id": 20050308,
	                        "equip_talisman_id": 50850301,
	                        "equip_crest_slot_type_1_crest_id_1": 40050020,
	                        "equip_crest_slot_type_1_crest_id_2": 40050028,
	                        "equip_crest_slot_type_1_crest_id_3": 40050060,
	                        "equip_crest_slot_type_2_crest_id_1": 40040082,
	                        "equip_crest_slot_type_2_crest_id_2": 40040062,
	                        "equip_crest_slot_type_3_crest_id_1": 40090024,
	                        "equip_crest_slot_type_3_crest_id_2": 40090018,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000010,
	                        "equip_talisman_ability_id_2": 340000110,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 3,
	                        "chara_id": 10550306,
	                        "equip_weapon_body_id": 30560304,
	                        "equip_dragon_id": 20050319,
	                        "equip_talisman_id": 50550306,
	                        "equip_crest_slot_type_1_crest_id_1": 40050034,
	                        "equip_crest_slot_type_1_crest_id_2": 40050121,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040103,
	                        "equip_crest_slot_type_2_crest_id_2": 40040063,
	                        "equip_crest_slot_type_3_crest_id_1": 40090010,
	                        "equip_crest_slot_type_3_crest_id_2": 40090028,
	                        "edit_skill_1_chara_id": 10840501,
	                        "edit_skill_2_chara_id": 10440301,
	                        "equip_talisman_ability_id_1": 340000009,
	                        "equip_talisman_ability_id_2": 340000133,
	                        "equip_talisman_ability_id_3": 0
	                    },
	                    {
	                        "unit_no": 4,
	                        "chara_id": 10350303,
	                        "equip_weapon_body_id": 30360304,
	                        "equip_dragon_id": 20050316,
	                        "equip_talisman_id": 50350304,
	                        "equip_crest_slot_type_1_crest_id_1": 40050069,
	                        "equip_crest_slot_type_1_crest_id_2": 40050121,
	                        "equip_crest_slot_type_1_crest_id_3": 40050128,
	                        "equip_crest_slot_type_2_crest_id_1": 40040097,
	                        "equip_crest_slot_type_2_crest_id_2": 40040106,
	                        "equip_crest_slot_type_3_crest_id_1": 40090006,
	                        "equip_crest_slot_type_3_crest_id_2": 40090026,
	                        "edit_skill_1_chara_id": 0,
	                        "edit_skill_2_chara_id": 10540402,
	                        "equip_talisman_ability_id_1": 340000008,
	                        "equip_talisman_ability_id_2": 340000133,
	                        "equip_talisman_ability_id_3": 0
	                    }
	                ]
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
