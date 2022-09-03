/plotsynopsis/top/
==================================================

- Base address: production-api.dragalialost.com
- Method: GET
- Status code: 200

Request headers
----------------

.. code-block:: text

	user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0	accept: application/json, text/javascript, */*; q=0.01	accept-language: en-GB,en;q=0.5	accept-encoding: gzip, deflate, br	origin: https://dragalialost.akamaized.net	dnt: 1	referer: https://dragalialost.akamaized.net/	sec-fetch-dest: empty	sec-fetch-mode: cors	sec-fetch-site: cross-site	te: trailers

Request body
----------------

.. code-block:: json

	null

Response headers
----------------

.. code-block:: text

	content-type: application/json	access-control-allow-origin: *	vary: Accept-Encoding	content-encoding: gzip	expires: Sat, 03 Sep 2022 16:47:04 GMT	cache-control: max-age=0, no-cache, no-store	pragma: no-cache	date: Sat, 03 Sep 2022 16:47:04 GMT	content-length: 478	set-cookie: ak_bmsc=2BF0D4EA5CF30652272C20FE090C3F24~000000000000000000000000000000~YAAQ0tPerRIvx/2CAQAAo6k/BBDXqLViAxZOqFVuTi3uDlpHQbGmFa0IzywhHMWVWuiv5VIlwjUKZ1yau3pf/RyFFT2FAnNzB65UE/qHU9iIVQut6D1hAMsw1tr/8WASaNmTKHbVBtZKhx9Pkgpjjs8uJsX+IWv/iIB0bDSq289gmQpjhWUMuMEKwfE6xA31Gu13MNEQJ8D8fLiW05+qTdA0lXObGqns5h7hE7/Eye9ua75qp0ENA3lvOsaOyijjqrMJWKrdt0SfPgLALMdjF6Izjyk7dJVkeNMfdX4UmkjyzalKEnKPN3QV9j4pXnGA70Vd2KtqaKzhJ4cQO93NX52LiKV0XPyviubD9Uq7fP4nyoI9068i/ncvljXYk9bQGmaLrq7YMR70Zwnsf/0U; Domain=.dragalialost.com; Path=/; Expires=Sat, 03 Sep 2022 18:47:04 GMT; Max-Age=7200; HttpOnly

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "latest_cartoon": "#468 added!",
	        "top": {
	            "id_1st": 6,
	            "id": 126,
	            "episode": 32,
	            "title": "Resurgent Despair: Part Four",
	            "image": "https://dragalialost.akamaized.net/attached/plotsynopsis/images/a5fdae305ee4ce24912050e7afe2e9e6.png"
	        },
	        "text_list": [
	            {
	                "message_id": "back_to_comic_list",
	                "text": "View All",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "comic_banner",
	                "text": "https://dragalialost.akamaized.net/static/image/comic/localized/en_us/banner_top_comic_01_webview.png",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "comic_episode_format",
	                "text": "#%s",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "comic_help_link_image",
	                "text": "https://dragalialost.akamaized.net/static/image/comic/localized/en_us/btn_helpcomic_01.png\t",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "comic_link_image_plotsynopsis",
	                "text": "https://dragalialost.akamaized.net/static/image/comic/localized/en_us/btn_comic_01.png",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "comic_update_info",
	                "text": "#%s added!",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "comic_update_info_accent",
	                "text": "#%s added!",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "plotsynopsis_banner",
	                "text": "https://dragalialost.akamaized.net/static/image/comic/localized/en_us/banner_top_plotsynopsis_01_webview.png\t",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "read_from_first_episode",
	                "text": "Start from #1",
	                "function_name": "comic"
	            },
	            {
	                "message_id": "to_comic_help",
	                "text": "Need help? Start here!",
	                "function_name": "comic"
	            }
	        ]
	    }
	}

Notes
------
