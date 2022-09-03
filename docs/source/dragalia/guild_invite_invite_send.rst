/guild_invite/invite_send
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
	    "target_viewer_id": 35789437060,
	    "guild_id": 72987015,
	    "guild_invite_message_id": 1
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
	        "guild_invite_send_list": [
	            {
	                "guild_invite_id": 14606,
	                "send_viewer_id": 97571459880,
	                "send_user_name": "Jay",
	                "receive_viewer_id": 35789437060,
	                "receive_user_name": "Archie",
	                "receive_user_level": 56,
	                "receive_max_party_power": 18412,
	                "receive_profile_entity_type": 7,
	                "receive_profile_entity_id": 20050110,
	                "receive_profile_entity_rarity": 5,
	                "receive_last_active_time": 1644963512,
	                "guild_invite_message_id": 1,
	                "limit_time": 1662464753
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------