# appdown

Install các thư viện:
tkinter
youtube_dl

Vào đường dẫn cài đặt python
Example: Home/.local/lib/python3/site-packages/youtube_dl/extractor/youtube.py

Chỉnh sửa từ
Before:
'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id') if owner_profile_url else None

After:
'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id' , fatal=False ) if owner_profile_url else None
