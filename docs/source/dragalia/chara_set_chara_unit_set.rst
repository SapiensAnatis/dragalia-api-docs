/chara/set_chara_unit_set
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com

Request body
----------------

.. code-block:: json

	{
	    "unit_set_no": 1,
	    "unit_set_name": "Set 1",
	    "chara_id": 10850403,
	    "request_chara_unit_set_data": {
	        "dragon_key_id": 19126829,
	        "weapon_body_id": 0,
	        "crest_slot_type_1_crest_id_1": 0,
	        "crest_slot_type_1_crest_id_2": 0,
	        "crest_slot_type_1_crest_id_3": 0,
	        "crest_slot_type_2_crest_id_1": 0,
	        "crest_slot_type_2_crest_id_2": 0,
	        "crest_slot_type_3_crest_id_1": 0,
	        "crest_slot_type_3_crest_id_2": 0,
	        "talisman_key_id": 0
	    }
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "chara_unit_set_list": [
	                {
	                    "chara_id": 10850403,
	                    "chara_unit_set_detail_list": [
	                        {
	                            "unit_set_no": 1,
	                            "unit_set_name": "Set 1",
	                            "dragon_key_id": 19126829,
	                            "weapon_body_id": 0,
	                            "crest_slot_type_1_crest_id_1": 0,
	                            "crest_slot_type_1_crest_id_2": 0,
	                            "crest_slot_type_1_crest_id_3": 0,
	                            "crest_slot_type_2_crest_id_1": 0,
	                            "crest_slot_type_2_crest_id_2": 0,
	                            "crest_slot_type_3_crest_id_1": 0,
	                            "crest_slot_type_3_crest_id_2": 0,
	                            "talisman_key_id": 0
	                        }
	                    ]
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------