/dmode/expedition_finish
===========================

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
    SID: 0e05309ea4d2a900ab9ddbfad0b20cbf0277b7fb31eaa5b4cecd7c540c696add
    Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
    Res-Ver: y2XM6giU6zz56wCm
    Request-Token: 27887807036917863
    Request-Time: 1662242823
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
    Content-Length: 2537
    Expires: Sat, 03 Sep 2022 22:07:11 GMT
    Cache-Control: max-age=0, no-cache, no-store
    Pragma: no-cache
    Date: Sat, 03 Sep 2022 22:07:11 GMT
    Connection: keep-alive

Response
----------------

.. code-block:: json

    {
        "data_headers": {
            "result_code": 1
        },
        "data": {
            "dmode_ingame_result": {
                "floor_num": 30,
                "is_record_floor_num": 0,
                "chara_id_list": [
                    10150104,
                    10150103,
                    10150102,
                    10150101
                ],
                "reward_talisman_list": [
                    {
                        "talisman_id": 50150104,
                        "talisman_ability_id_1": 340000065,
                        "talisman_ability_id_2": 340000057,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 0,
                        "additional_attack": 0
                    },
                    {
                        "talisman_id": 50150103,
                        "talisman_ability_id_1": 340000065,
                        "talisman_ability_id_2": 340000085,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 0,
                        "additional_attack": 0
                    },
                    {
                        "talisman_id": 50150102,
                        "talisman_ability_id_1": 340000024,
                        "talisman_ability_id_2": 340000035,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 0,
                        "additional_attack": 0
                    },
                    {
                        "talisman_id": 50150101,
                        "talisman_ability_id_1": 0,
                        "talisman_ability_id_2": 0,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 100,
                        "additional_attack": 100
                    }
                ],
                "take_dmode_point_1": 5775,
                "take_dmode_point_2": 0,
                "take_player_exp": 0,
                "player_level_up_fstone": 0,
                "quest_time": 0,
                "is_view_quest_time": 0,
                "dmode_score": 0,
                "clear_state": 0
            },
            "dmode_expedition": {
                "chara_id_1": 10150104,
                "chara_id_2": 10150103,
                "chara_id_3": 10150102,
                "chara_id_4": 10150101,
                "start_time": 1662209613,
                "target_floor_num": 30,
                "state": 1
            },
            "update_data_list": {
                "user_data": {
                    "viewer_id": 97571459880,
                    "name": "Jay",
                    "level": 174,
                    "exp": 6181433,
                    "crystal": 14110,
                    "coin": 1664578245,
                    "max_dragon_quantity": 305,
                    "max_weapon_quantity": 0,
                    "max_amulet_quantity": 0,
                    "quest_skip_point": 392,
                    "main_party_no": 1,
                    "emblem_id": 50004301,
                    "active_memory_event_id": 22219,
                    "mana_point": 9042316,
                    "dew_point": 922590,
                    "build_time_point": 1067,
                    "last_login_time": 1662204727,
                    "stamina_single": 13,
                    "last_stamina_single_update_time": 1662213130,
                    "stamina_single_surplus_second": 283,
                    "stamina_multi": 6,
                    "last_stamina_multi_update_time": 1662213130,
                    "stamina_multi_surplus_second": 3498,
                    "tutorial_status": 60999,
                    "tutorial_flag_list": [
                        1001,
                        1002,
                        1003,
                        1004,
                        1005,
                        1006,
                        1007,
                        1008,
                        1009,
                        1010,
                        1011,
                        1012,
                        1013,
                        1014,
                        1015,
                        1016,
                        1017,
                        1018,
                        1019,
                        1020,
                        1021,
                        1022,
                        1023,
                        1024,
                        1025,
                        1026,
                        1027,
                        1028,
                        1029,
                        1030
                    ],
                    "prologue_end_time": 1557120311,
                    "is_optin": 0,
                    "fort_open_time": 0,
                    "create_time": 1557120036
                },
                "dmode_info": {
                    "total_max_floor_num": 60,
                    "recovery_count": 3,
                    "recovery_time": 1653360289,
                    "floor_skip_count": 1,
                    "floor_skip_time": 1653243974,
                    "dmode_point_1": 6062,
                    "dmode_point_2": 703,
                    "is_entry": 1
                },
                "talisman_list": [
                    {
                        "talisman_key_id": 181017,
                        "talisman_id": 50150104,
                        "is_lock": 0,
                        "is_new": 1,
                        "talisman_ability_id_1": 340000065,
                        "talisman_ability_id_2": 340000057,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 0,
                        "additional_attack": 0,
                        "gettime": 1662242831
                    },
                    {
                        "talisman_key_id": 181018,
                        "talisman_id": 50150103,
                        "is_lock": 0,
                        "is_new": 1,
                        "talisman_ability_id_1": 340000065,
                        "talisman_ability_id_2": 340000085,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 0,
                        "additional_attack": 0,
                        "gettime": 1662242831
                    },
                    {
                        "talisman_key_id": 181019,
                        "talisman_id": 50150102,
                        "is_lock": 0,
                        "is_new": 1,
                        "talisman_ability_id_1": 340000024,
                        "talisman_ability_id_2": 340000035,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 0,
                        "additional_attack": 0,
                        "gettime": 1662242831
                    },
                    {
                        "talisman_key_id": 181020,
                        "talisman_id": 50150101,
                        "is_lock": 0,
                        "is_new": 1,
                        "talisman_ability_id_1": 0,
                        "talisman_ability_id_2": 0,
                        "talisman_ability_id_3": 0,
                        "additional_hp": 100,
                        "additional_attack": 100,
                        "gettime": 1662242831
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

Notes:
------

- Write down any remarks or comments here