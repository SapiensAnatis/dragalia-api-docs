/load/index/
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
    DeviceId: 94e58eeb39e0f05c528aa0582d4032f8
    DeviceName: OnePlus ONEPLUS A6003
    OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
    GraphicsDeviceName: Adreno (TM) 540
    SID: 455da64045a2a9844632eb1e48b53dfbcb7d22dbca8f3cb5a20e0055750f6270
    Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
    Res-Ver: y2XM6giU6zz56wCm
    Request-Token: 27883386055953188
    Request-Time: 1661979321
    Content-Type: application/octet-stream
    X-Unity-Version: 2019.4.31f1
    Content-Length: 76

Request body
----------------

.. code-block:: json

    {
    }

Response headers
----------------

.. code-block:: text

    Content-Type: application/x-msgpack
    Access-Control-Allow-Origin: *
    Content-Length: 15412
    Expires: Wed, 31 Aug 2022 20:55:20 GMT
    Cache-Control: max-age=0, no-cache, no-store
    Pragma: no-cache
    Date: Wed, 31 Aug 2022 20:55:20 GMT
    Connection: keep-alive

Response
----------------

.. note:: 

    The following JSON response contained a great deal of repetitive data (originally ~200kb and ~12k lines), so some long arrays have been trimmed. You can view the raw unabridged file here: <https://raw.githubusercontent.com/SapiensAnatis/dragalia-api-docs/blob/main/docs/source/dragalia/savefile.json>


.. code-block:: javascript

    {
        "data_headers": {
            "result_code": 1
        },
        "data": {
            "quest_bonus": [
            ],
            "special_shop_purchase": [
            ],
            "user_treasure_trade_list": [
            ],
            "treasure_trade_all_list": [
                {
                    "treasure_trade_id": 10010101,
                    "priority": 1000,
                    "tab_group_id": 1,
                    "commence_date": 0,
                    "complete_date": 0,
                    "is_lock_view": 0,
                    "reset_type": 0,
                    "limit": 0,
                    "destination_entity_type": 8,
                    "destination_entity_id": 112002001,
                    "destination_entity_quantity": 1,
                    "destination_limit_break_count": 0,
                    "need_trade_entity_list": [
                        {
                            "entity_type": 8,
                            "entity_id": 201007001,
                            "entity_quantity": 10,
                            "limit_break_count": 0
                        }
                    ]
                },
                // --- array trimmed ---
            ]
            "user_data": {
                "viewer_id": 66709573935,
                "name": "Euden",
                "level": 1,
                "exp": 0,
                "crystal": 400,
                "coin": 2000001000,
                "max_dragon_quantity": 160,
                "max_weapon_quantity": 0,
                "max_amulet_quantity": 0,
                "quest_skip_point": 312,
                "main_party_no": 1,
                "emblem_id": 40000001,
                "active_memory_event_id": 0,
                "mana_point": 500,
                "dew_point": 0,
                "build_time_point": 0,
                "last_login_time": 1661979293,
                "stamina_single": 18,
                "last_stamina_single_update_time": 1661897736,
                "stamina_single_surplus_second": 0,
                "stamina_multi": 12,
                "last_stamina_multi_update_time": 1661897736,
                "stamina_multi_surplus_second": 0,
                "tutorial_status": 10301,
                "tutorial_flag_list": [
                    1020
                ],
                "prologue_end_time": 1661979402,
                "is_optin": 0,
                "fort_open_time": 0,
                "create_time": 1661897736
            },
            "party_power_data": {
                "max_party_power": 1707
            },
            "party_list": [
                {
                    "party_no": 1,
                    "party_name": "",
                    "party_setting_list": [
                        {
                            "unit_no": 1,
                            "chara_id": 10140101,
                            "equip_dragon_key_id": 19273109,
                            "equip_weapon_body_id": 30129901,
                            "equip_weapon_skin_id": 0,
                            "equip_crest_slot_type_1_crest_id_1": 0,
                            "equip_crest_slot_type_1_crest_id_2": 0,
                            "equip_crest_slot_type_1_crest_id_3": 0,
                            "equip_crest_slot_type_2_crest_id_1": 0,
                            "equip_crest_slot_type_2_crest_id_2": 0,
                            "equip_crest_slot_type_3_crest_id_1": 0,
                            "equip_crest_slot_type_3_crest_id_2": 0,
                            "equip_talisman_key_id": 0,
                            "edit_skill_1_chara_id": 0,
                            "edit_skill_2_chara_id": 0
                        },
                        {
                            "unit_no": 2,
                            "chara_id": 10230101,
                            "equip_dragon_key_id": 19273108,
                            "equip_weapon_body_id": 0,
                            "equip_weapon_skin_id": 0,
                            "equip_crest_slot_type_1_crest_id_1": 0,
                            "equip_crest_slot_type_1_crest_id_2": 0,
                            "equip_crest_slot_type_1_crest_id_3": 0,
                            "equip_crest_slot_type_2_crest_id_1": 0,
                            "equip_crest_slot_type_2_crest_id_2": 0,
                            "equip_crest_slot_type_3_crest_id_1": 0,
                            "equip_crest_slot_type_3_crest_id_2": 0,
                            "equip_talisman_key_id": 0,
                            "edit_skill_1_chara_id": 0,
                            "edit_skill_2_chara_id": 0
                        },
                        {
                            "unit_no": 3,
                            "chara_id": 10130103,
                            "equip_dragon_key_id": 19273096,
                            "equip_weapon_body_id": 0,
                            "equip_weapon_skin_id": 0,
                            "equip_crest_slot_type_1_crest_id_1": 0,
                            "equip_crest_slot_type_1_crest_id_2": 0,
                            "equip_crest_slot_type_1_crest_id_3": 0,
                            "equip_crest_slot_type_2_crest_id_1": 0,
                            "equip_crest_slot_type_2_crest_id_2": 0,
                            "equip_crest_slot_type_3_crest_id_1": 0,
                            "equip_crest_slot_type_3_crest_id_2": 0,
                            "equip_talisman_key_id": 0,
                            "edit_skill_1_chara_id": 0,
                            "edit_skill_2_chara_id": 0
                        },
                        {
                            "unit_no": 4,
                            "chara_id": 10830101,
                            "equip_dragon_key_id": 19273093,
                            "equip_weapon_body_id": 0,
                            "equip_weapon_skin_id": 0,
                            "equip_crest_slot_type_1_crest_id_1": 0,
                            "equip_crest_slot_type_1_crest_id_2": 0,
                            "equip_crest_slot_type_1_crest_id_3": 0,
                            "equip_crest_slot_type_2_crest_id_1": 0,
                            "equip_crest_slot_type_2_crest_id_2": 0,
                            "equip_crest_slot_type_3_crest_id_1": 0,
                            "equip_crest_slot_type_3_crest_id_2": 0,
                            "equip_talisman_key_id": 0,
                            "edit_skill_1_chara_id": 0,
                            "edit_skill_2_chara_id": 0
                        }
                    ]
                },
                // --- array trimmed ---
            ],
            "chara_list": [
                {
                    "chara_id": 10130103,
                    "rarity": 3,
                    "exp": 0,
                    "level": 1,
                    "additional_max_level": 0,
                    "hp_plus_count": 0,
                    "attack_plus_count": 0,
                    "limit_break_count": 0,
                    "is_new": 1,
                    "gettime": 1661976620,
                    "skill_1_level": 1,
                    "skill_2_level": 0,
                    "ability_1_level": 0,
                    "ability_2_level": 0,
                    "ability_3_level": 0,
                    "burst_attack_level": 0,
                    "combo_buildup_count": 0,
                    "hp": 45,
                    "attack": 27,
                    "ex_ability_level": 1,
                    "ex_ability_2_level": 1,
                    "is_temporary": 0,
                    "is_unlock_edit_skill": 0,
                    "mana_circle_piece_id_list": [
                    ],
                    "list_view_flag": 1
                },
                // --- array trimmed ---
            ],
            "dragon_list": [
                {
                    "dragon_key_id": 19273088,
                    "dragon_id": 20030101,
                    "level": 1,
                    "hp_plus_count": 0,
                    "attack_plus_count": 0,
                    "exp": 0,
                    "is_lock": 0,
                    "is_new": 1,
                    "get_time": 1661976618,
                    "skill_1_level": 1,
                    "ability_1_level": 1,
                    "ability_2_level": 0,
                    "limit_break_count": 0
                },
                // --- array trimmed ---
            ],
            "dragon_gift_list": [
            ],
            "dragon_reliability_list": [
                {
                    "dragon_id": 20030101,
                    "gettime": 1661976618,
                    "reliability_level": 1,
                    "reliability_total_exp": 0,
                    "last_contact_time": 0
                },
                // --- array trimmed ---
            ],
            "material_list": [
                {
                    "material_id": 101001001,
                    "quantity": 1
                },
                // --- array trimmed ---
            ],
            "fort_bonus_list": {
                "param_bonus": [
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
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 2,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 3,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 4,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 5,
                        "hp": 0,
                        "attack": 0
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
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 2,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 3,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 4,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 5,
                        "hp": 0,
                        "attack": 0
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
                        "dragon_bonus": 0,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 2,
                        "dragon_bonus": 0,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 3,
                        "dragon_bonus": 0,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 4,
                        "dragon_bonus": 0,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 5,
                        "dragon_bonus": 0,
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
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 2,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 3,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 4,
                        "hp": 0,
                        "attack": 0
                    },
                    {
                        "elemental_type": 5,
                        "hp": 0,
                        "attack": 0
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
            "fort_plant_list": [
            ],
            "build_list": [
            ],
            "equip_stamp_list": [
                {
                    "slot": 1,
                    "stamp_id": 10001
                },
                // --- array trimmed ---
            ],
            "unit_story_list": [
                {
                    "unit_story_id": 110002011,
                    "is_read": 0
                },
                // --- array trimmed ---
            ],
            "castle_story_list": [
            ],
            "quest_list": [
            ],
            "quest_event_list": [
            ],
            "quest_story_list": [
                {
                    "quest_story_id": 1000100,
                    "state": 1
                }
            ],
            "quest_treasure_list": [
            ],
            "quest_carry_list": [
            ],
            "quest_entry_condition_list": [
            ],
            "summon_ticket_list": [
                {
                    "key_id": 367919,
                    "summon_ticket_id": 10102,
                    "quantity": 1,
                    "use_limit_time": 0
                }
            ],
            "summon_point_list": [
            ],
            "present_notice": {
                "present_count": 0,
                "present_limit_count": 1
            },
            "friend_notice": {
                "friend_new_count": 0,
                "apply_new_count": 0
            },
            "mission_notice": {
                "normal_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 3,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 222,
                    "completed_mission_count": 3,
                    "current_mission_id": 0
                },
                "daily_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 1,
                    "all_mission_count": 9,
                    "completed_mission_count": 0,
                    "current_mission_id": 0
                },
                "period_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 10,
                    "completed_mission_count": 0,
                    "current_mission_id": 0
                },
                "beginner_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 0,
                    "completed_mission_count": 0,
                    "current_mission_id": 0
                },
                "special_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 56,
                    "completed_mission_count": 0,
                    "current_mission_id": 0
                },
                "main_story_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 0,
                    "completed_mission_count": 0,
                    "current_mission_id": 0
                },
                "memory_event_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 0,
                    "completed_mission_count": 0,
                    "current_mission_id": 0
                },
                "drill_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 54,
                    "completed_mission_count": 1,
                    "current_mission_id": 100100
                },
                "album_mission_notice": {
                    "is_update": 1,
                    "receivable_reward_count": 0,
                    "new_complete_mission_id_list": [
                    ],
                    "pickup_mission_count": 0,
                    "all_mission_count": 22,
                    "completed_mission_count": 0,
                    "current_mission_id": 0
                }
            },
            "current_main_story_mission": [
            ],
            "guild_notice": {
                "is_update_guild_apply_reply": 0,
                "guild_apply_count": 0,
                "is_update_guild_board": 0,
                "is_update_guild": 0,
                "is_update_guild_invite": 0
            },
            "shop_notice": {
                "is_shop_notification": 1
            },
            "album_passive_notice": {
                "is_update_chara": 1,
                "is_update_dragon": 1
            },
            "functional_maintenance_list": [
            ],
            "quest_wall_list": [
            ],
            "astral_item_list": [
            ],
            "user_guild_data": [
            ],
            "guild_data": [
            ],
            "lottery_ticket_list": [
            ],
            "gather_item_list": [
            ],
            "weapon_skin_list": [
                {
                    "weapon_skin_id": 30129901,
                    "is_new": 0,
                    "gettime": 1661976574
                }
            ],
            "weapon_body_list": [
                {
                    "weapon_body_id": 30129901,
                    "buildup_count": 0,
                    "limit_break_count": 0,
                    "limit_over_count": 0,
                    "equipable_count": 1,
                    "additional_crest_slot_type_1_count": 0,
                    "additional_crest_slot_type_2_count": 0,
                    "additional_crest_slot_type_3_count": 0,
                    "additional_effect_count": 0,
                    "unlock_weapon_passive_ability_no_list": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "fort_passive_chara_weapon_buildup_count": 0,
                    "is_new": 0,
                    "gettime": 1661976574
                }
            ],
            "weapon_passive_ability_list": [
            ],
            "ability_crest_list": [
            ],
            "exchange_ticket_list": [
            ],
            "album_dragon_list": [
                {
                    "dragon_id": 20030101,
                    "max_level": 1,
                    "max_limit_break_count": 0
                },
               // --- array trimmed ---
            ],
            "talisman_list": [
            ],
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
                    "summon_count": 0,
                    "campaign_type": 0,
                    "free_count_rest": 0,
                    "is_beginner_campaign": 1,
                    "beginner_campaign_count_rest": 1,
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
            "server_time": 1661983024,
            "stamina_multi_user_max": 12,
            "stamina_multi_system_max": 99,
            "quest_bonus_stack_base_time": 1617775200,
            "spec_upgrade_time": 1548730800,
            "quest_skip_point_use_limit_max": 30,
            "quest_skip_point_system_max": 400,
            "multi_server": {
                "host": "",
                "app_id": "a4a64ca9-6190-45cf-815b-da292d9dc461"
            },
            "walker_data": {
                "reliability_level": 1,
                "reliability_total_exp": 0,
                "last_contact_time": 0,
                "skill_2_level": 1
            },
            "update_data_list": {
                "functional_maintenance_list": [
                ]
            }
        }
    }


Notes:
------

- This appears to be the player savefile, containing information about owned units and dragons, as well as saved parties and many other things.
- Having now identified the savefile endpoint, we could in theory allow players to download their savefile and upload it to a future private server. However, setting up packet capture and coneshell.dll bypass is very involved, so this seems to be an unlikely possibility.