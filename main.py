# legit just the documentation of the python GoogleImagesSearch API lul

from google_images_search import GoogleImagesSearch

# if you don't enter api key and cx, the package will try to search
# them from environment variables GCS_DEVELOPER_KEY and GCS_CX
gis = GoogleImagesSearch('your_dev_api_key', 'your_project_cx')

# example: GoogleImagesSearch('ABcDeFGhiJKLmnopqweRty5asdfghGfdSaS4abC', '012345678987654321012:abcde_fghij')

#define search params:
search_params = {
    'q': '...',
    'num': 1-50,
    'safe': 'high|medium|off',
    'fileType': 'jpg|gif|png',
    'imgType': 'clipart|face|lineart|news|photo',
    'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
    'searchType': 'image',
    'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow'
}

# this will only search for images:
gis.search(search_params=search_params)

# this will search and download:
gis.search(search_params=search_params, path_to_dir='/path/')

# search first, then download afterwards
gis.search(search_params=search_params)
for image in gis.results():
    image.download('/path/') 
    
