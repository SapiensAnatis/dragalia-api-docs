/friend/get_support_chara_detail
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888812545805097	Request-Time: 1662302764	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 28

Request body
----------------

.. code-block:: json

	{
	    "support_viewer_id": 25839548314
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 2793	Expires: Sun, 04 Sep 2022 14:46:05 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:46:05 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "support_user_data_detail": {
	            "user_support_data": {
	                "viewer_id": 25839548314,
	                "name": "L3GEND",
	                "level": 60,
	                "last_login_date": 1662233863,
	                "emblem_id": 40000001,
	                "max_party_power": 2733,
	                "support_chara": {
	                    "chara_id": 10140101,
	                    "level": 34,
	                    "additional_max_level": 0,
	                    "rarity": 4,
	                    "element_type": 1,
	                    "hp": 261,
	                    "attack": 175,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "ability_1_level": 1,
	                    "ability_2_level": 1,
	                    "ability_3_level": 0,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "is_unlock_edit_skill": 1
	                },
	                "support_dragon": {
	                    "dragon_key_id": 0
	                },
	                "support_weapon_body": {
	                    "weapon_body_id": 0
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
	                        "ability_crest_id": 0
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
	                    "guild_id": 0
	                }
	            },
	            "fort_bonus_list": {
	                "param_bonus": [
	                    {
	                        "weapon_type": 1,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 2,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 3,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 4,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 5,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 6,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 7,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 8,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    },
	                    {
	                        "weapon_type": 9,
	                        "hp": 11.0,
	                        "attack": 10.0
	                    }
	                ],
	                "param_bonus_by_weapon": [
	                    {
	                        "weapon_type": 1,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 2,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 3,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 4,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 5,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 6,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 7,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 8,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "weapon_type": 9,
	                        "hp": 0,
	                        "attack": 0
	                    }
	                ],
	                "element_bonus": [
	                    {
	                        "elemental_type": 1,
	                        "hp": 6.0,
	                        "attack": 5.0
	                    },
	                    {
	                        "elemental_type": 2,
	                        "hp": 6.0,
	                        "attack": 5.0
	                    },
	                    {
	                        "elemental_type": 3,
	                        "hp": 6.0,
	                        "attack": 5.0
	                    },
	                    {
	                        "elemental_type": 4,
	                        "hp": 6.0,
	                        "attack": 5.0
	                    },
	                    {
	                        "elemental_type": 5,
	                        "hp": 6.0,
	                        "attack": 5.0
	                    },
	                    {
	                        "elemental_type": 99,
	                        "hp": 0,
	                        "attack": 0
	                    }
	                ],
	                "chara_bonus_by_album": [
	                    {
	                        "elemental_type": 1,
	                        "hp": 0.9,
	                        "attack": 0.9
	                    },
	                    {
	                        "elemental_type": 2,
	                        "hp": 1.0,
	                        "attack": 1.0
	                    },
	                    {
	                        "elemental_type": 3,
	                        "hp": 0.8,
	                        "attack": 0.8
	                    },
	                    {
	                        "elemental_type": 4,
	                        "hp": 1.3,
	                        "attack": 1.3
	                    },
	                    {
	                        "elemental_type": 5,
	                        "hp": 1.3,
	                        "attack": 1.3
	                    },
	                    {
	                        "elemental_type": 99,
	                        "hp": 0,
	                        "attack": 0
	                    }
	                ],
	                "all_bonus": {
	                    "hp": 0,
	                    "attack": 0
	                },
	                "dragon_bonus": [
	                    {
	                        "elemental_type": 1,
	                        "dragon_bonus": 1.0,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "elemental_type": 2,
	                        "dragon_bonus": 1.0,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "elemental_type": 3,
	                        "dragon_bonus": 1.0,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "elemental_type": 4,
	                        "dragon_bonus": 1.0,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "elemental_type": 5,
	                        "dragon_bonus": 1.0,
	                        "hp": 0,
	                        "attack": 0
	                    },
	                    {
	                        "elemental_type": 99,
	                        "dragon_bonus": 0,
	                        "hp": 0,
	                        "attack": 0
	                    }
	                ],
	                "dragon_bonus_by_album": [
	                    {
	                        "elemental_type": 1,
	                        "hp": 0.4,
	                        "attack": 0.4
	                    },
	                    {
	                        "elemental_type": 2,
	                        "hp": 0.4,
	                        "attack": 0.4
	                    },
	                    {
	                        "elemental_type": 3,
	                        "hp": 0.5,
	                        "attack": 0.5
	                    },
	                    {
	                        "elemental_type": 4,
	                        "hp": 0.4,
	                        "attack": 0.4
	                    },
	                    {
	                        "elemental_type": 5,
	                        "hp": 0.6,
	                        "attack": 0.6
	                    },
	                    {
	                        "elemental_type": 99,
	                        "hp": 0,
	                        "attack": 0
	                    }
	                ],
	                "dragon_time_bonus": {
	                    "dragon_time_bonus": 0
	                }
	            },
	            "mana_circle_piece_id_list": [
	                1,
	                2,
	                3,
	                4,
	                5,
	                6,
	                7,
	                8,
	                9,
	                10
	            ],
	            "dragon_reliability_level": 0,
	            "is_friend": 0,
	            "apply_send_status": 0
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
