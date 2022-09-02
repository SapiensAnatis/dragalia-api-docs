/summon/request
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27883474186668252	Request-Time: 1661984571	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 104

Request body
----------------

.. code-block:: json

	{
	    "summon_id": 1020203,
	    "exec_type": 2,
	    "exec_count": 0,
	    "payment_type": 10,
	    "payment_target": {
	        "target_hold_quantity": 0,
	        "target_cost": 0
	    }
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 4420	Expires: Wed, 31 Aug 2022 22:22:53 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Wed, 31 Aug 2022 22:22:53 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "reversal_effect_index": -1,
	        "presage_effect_list": [
	            2,
	            2
	        ],
	        "result_unit_list": [
	            {
	                "entity_type": 1,
	                "id": 10430201,
	                "rarity": 3,
	                "is_new": false,
	                "dew_point": 150
	            },
	            {
	                "entity_type": 7,
	                "id": 20030201,
	                "rarity": 3,
	                "is_new": true
	            },
	            {
	                "entity_type": 1,
	                "id": 10130401,
	                "rarity": 3,
	                "is_new": false,
	                "dew_point": 150
	            },
	            {
	                "entity_type": 1,
	                "id": 10530101,
	                "rarity": 3,
	                "is_new": true
	            },
	            {
	                "entity_type": 1,
	                "id": 10130103,
	                "rarity": 3,
	                "is_new": false,
	                "dew_point": 150
	            },
	            {
	                "entity_type": 7,
	                "id": 20030301,
	                "rarity": 3,
	                "is_new": false
	            },
	            {
	                "entity_type": 7,
	                "id": 20030401,
	                "rarity": 3,
	                "is_new": true
	            },
	            {
	                "entity_type": 7,
	                "id": 20040102,
	                "rarity": 4,
	                "is_new": false
	            },
	            {
	                "entity_type": 1,
	                "id": 10430301,
	                "rarity": 3,
	                "is_new": false,
	                "dew_point": 150
	            },
	            {
	                "entity_type": 7,
	                "id": 20040202,
	                "rarity": 4,
	                "is_new": true
	            }
	        ],
	        "result_prize_list": [],
	        "summon_ticket_list": [
	            {
	                "key_id": 367919,
	                "summon_ticket_id": 10102,
	                "quantity": 1,
	                "use_limit_time": 0
	            }
	        ],
	        "result_summon_point": 10,
	        "user_summon_list": [
	            {
	                "summon_id": 1010001,
	                "summon_count": 0,
	                "campaign_type": 0,
	                "free_count_rest": 0,
	                "is_beginner_campaign": 0,
	                "beginner_campaign_count_rest": 0,
	                "consecution_campaign_count_rest": 0
	            },
	            {
	                "summon_id": 1020203,
	                "summon_count": 1,
	                "campaign_type": 0,
	                "free_count_rest": 0,
	                "is_beginner_campaign": 1,
	                "beginner_campaign_count_rest": 0,
	                "consecution_campaign_count_rest": 0
	            },
	            {
	                "summon_id": 1040001,
	                "summon_count": 0,
	                "campaign_type": 0,
	                "free_count_rest": 0,
	                "is_beginner_campaign": 0,
	                "beginner_campaign_count_rest": 0,
	                "consecution_campaign_count_rest": 0
	            },
	            {
	                "summon_id": 1060001,
	                "summon_count": 0,
	                "campaign_type": 0,
	                "free_count_rest": 0,
	                "is_beginner_campaign": 0,
	                "beginner_campaign_count_rest": 0,
	                "consecution_campaign_count_rest": 0
	            },
	            {
	                "summon_id": 1090010,
	                "summon_count": 0,
	                "campaign_type": 0,
	                "free_count_rest": 0,
	                "is_beginner_campaign": 0,
	                "beginner_campaign_count_rest": 0,
	                "consecution_campaign_count_rest": 0
	            },
	            {
	                "summon_id": 1100008,
	                "summon_count": 0,
	                "campaign_type": 0,
	                "free_count_rest": 0,
	                "is_beginner_campaign": 0,
	                "beginner_campaign_count_rest": 0,
	                "consecution_campaign_count_rest": 0
	            },
	            {
	                "summon_id": 1110003,
	                "summon_count": 0,
	                "campaign_type": 0,
	                "free_count_rest": 0,
	                "is_beginner_campaign": 0,
	                "beginner_campaign_count_rest": 0,
	                "consecution_campaign_count_rest": 0
	            }
	        ],
	        "update_data_list": {
	            "user_data": {
	                "viewer_id": 66709573935,
	                "name": "Euden",
	                "level": 1,
	                "exp": 30,
	                "crystal": 450,
	                "coin": 2000001215,
	                "max_dragon_quantity": 160,
	                "max_weapon_quantity": 0,
	                "max_amulet_quantity": 0,
	                "quest_skip_point": 312,
	                "main_party_no": 1,
	                "emblem_id": 40000001,
	                "active_memory_event_id": 0,
	                "mana_point": 547,
	                "dew_point": 600,
	                "build_time_point": 0,
	                "last_login_time": 1661979293,
	                "stamina_single": 18,
	                "last_stamina_single_update_time": 1661984335,
	                "stamina_single_surplus_second": 0,
	                "stamina_multi": 12,
	                "last_stamina_multi_update_time": 1661897736,
	                "stamina_multi_surplus_second": 0,
	                "tutorial_status": 10601,
	                "tutorial_flag_list": [
	                    1020,
	                    1022
	                ],
	                "prologue_end_time": 1661979402,
	                "is_optin": 0,
	                "fort_open_time": 0,
	                "create_time": 1661897736
	            },
	            "dragon_list": [
	                {
	                    "dragon_key_id": 19273128,
	                    "dragon_id": 20030201,
	                    "level": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "exp": 0,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "get_time": 1661984573,
	                    "skill_1_level": 1,
	                    "ability_1_level": 1,
	                    "ability_2_level": 0,
	                    "limit_break_count": 0
	                },
	                {
	                    "dragon_key_id": 19273129,
	                    "dragon_id": 20030301,
	                    "level": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "exp": 0,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "get_time": 1661984573,
	                    "skill_1_level": 1,
	                    "ability_1_level": 1,
	                    "ability_2_level": 0,
	                    "limit_break_count": 0
	                },
	                {
	                    "dragon_key_id": 19273130,
	                    "dragon_id": 20030401,
	                    "level": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "exp": 0,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "get_time": 1661984573,
	                    "skill_1_level": 1,
	                    "ability_1_level": 1,
	                    "ability_2_level": 0,
	                    "limit_break_count": 0
	                },
	                {
	                    "dragon_key_id": 19273131,
	                    "dragon_id": 20040102,
	                    "level": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "exp": 0,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "get_time": 1661984573,
	                    "skill_1_level": 1,
	                    "ability_1_level": 1,
	                    "ability_2_level": 0,
	                    "limit_break_count": 0
	                },
	                {
	                    "dragon_key_id": 19273132,
	                    "dragon_id": 20040202,
	                    "level": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "exp": 0,
	                    "is_lock": 0,
	                    "is_new": 1,
	                    "get_time": 1661984573,
	                    "skill_1_level": 1,
	                    "ability_1_level": 1,
	                    "ability_2_level": 0,
	                    "limit_break_count": 0
	                }
	            ],
	            "dragon_reliability_list": [
	                {
	                    "dragon_id": 20030201,
	                    "gettime": 1661984573,
	                    "reliability_level": 1,
	                    "reliability_total_exp": 0,
	                    "last_contact_time": 0
	                },
	                {
	                    "dragon_id": 20030301,
	                    "gettime": 1661976618,
	                    "reliability_level": 1,
	                    "reliability_total_exp": 0,
	                    "last_contact_time": 0
	                },
	                {
	                    "dragon_id": 20030401,
	                    "gettime": 1661984573,
	                    "reliability_level": 1,
	                    "reliability_total_exp": 0,
	                    "last_contact_time": 0
	                },
	                {
	                    "dragon_id": 20040102,
	                    "gettime": 1661976618,
	                    "reliability_level": 1,
	                    "reliability_total_exp": 0,
	                    "last_contact_time": 0
	                },
	                {
	                    "dragon_id": 20040202,
	                    "gettime": 1661984573,
	                    "reliability_level": 1,
	                    "reliability_total_exp": 0,
	                    "last_contact_time": 0
	                }
	            ],
	            "chara_list": [
	                {
	                    "chara_id": 10530101,
	                    "rarity": 3,
	                    "exp": 0,
	                    "level": 1,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 0,
	                    "is_new": 1,
	                    "gettime": 1661984573,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "ability_1_level": 0,
	                    "ability_2_level": 0,
	                    "ability_3_level": 0,
	                    "burst_attack_level": 0,
	                    "combo_buildup_count": 0,
	                    "hp": 46,
	                    "attack": 25,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [],
	                    "list_view_flag": 1
	                }
	            ],
	            "summon_point_list": [
	                {
	                    "summon_point_id": 1020203,
	                    "summon_point": 10,
	                    "cs_summon_point": 0,
	                    "cs_point_term_min_date": 0,
	                    "cs_point_term_max_date": 0
	                }
	            ],
	            "unit_story_list": [
	                {
	                    "unit_story_id": 110001011,
	                    "is_read": 0
	                }
	            ],
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": [],
	            "new_get_entity_list": [
	                {
	                    "entity_type": 1,
	                    "entity_id": 10530101
	                },
	                {
	                    "entity_type": 7,
	                    "entity_id": 20030201
	                },
	                {
	                    "entity_type": 7,
	                    "entity_id": 20030401
	                },
	                {
	                    "entity_type": 7,
	                    "entity_id": 20040202
	                }
	            ]
	        }
	    }
	}

Notes
------
