import math
import os
import requests
import subprocess
import tempfile

from tator.transcode.upload import upload_file
import tator

def _download_file(headers, url, out_path):
    CHUNK_SIZE=2*1024*1024
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        total_size = r.headers['Content-Length']
        total_chunks = math.ceil(int(total_size) / CHUNK_SIZE)
        chunk_count = 0
        last_progress = 0
        with open(out_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    chunk_count += 1
                    f.write(chunk)
                    
def make_multi_stream(api, type_id, layout,name, media_ids,section=None,quality=None):
    """ Uploads a single media file.

    :param api: :class:`tator.TatorApi` object.
    :param type_id: Unique integer identifying a multi-stream media type.
    :param layout: Path to the media file.
    :param name: Name of the file to use
    :param media_ids: List of media_ids to multi-stream
    :param quality: [Optional] Media section to upload to.
    :param section [Optional]: Section attribute to apply to media element
    :returns: Boolean representing success (True means success)
    """

    # Fetch the stuff we need to download files
    config = api.api_client.configuration
    host = config.host
    token = config.api_key['Authorization']
    prefix = config.api_key_prefix['Authorization']

    # use a multi extension
    name += ".multi"

    # Fetch the media type
    multi_stream_type = api.get_media_type(type_id)
    project = multi_stream_type.project

    assert(len(media_ids) == layout[0]*layout[1])
    
    media_objects = api.get_media_list(project,media_id=media_ids)
    assert(len(media_objects) == len(media_ids))

    media_lookup={}
    for media in media_objects:
        media_lookup[media.id] = media

    attributes={}
    if section:
        attributes.update({"tator_user_sections": section})

    headers = {
        'Authorization': f'{prefix} {token}',
        'Content-Type': f'application/json',
        'Accept-Encoding': 'gzip',
    }
    
    # Download the thumbnails into a temporary
    with tempfile.TemporaryDirectory() as d:
        for pos,media_id in enumerate(media_ids):
            media = media_lookup[media_id]
            thumb = host + "/media/" + media.thumbnail
            thumb_gif = host + "/media/" + media.thumbnail_gif
            _download_file(headers, thumb, os.path.join(d,
                                                        f"thumb_{pos:09d}.jpg"))
            _download_file(headers, thumb_gif, os.path.join(d,
                                                        f"gif_{pos:09d}.gif"))

        cmd = ["ffmpeg",
               "-y",
               "-i", "thumb_%09d.jpg",
               "-vf",f"tile={layout[0]}x{layout[1]},scale=256:-1",
               os.path.join(d,"tiled_thumb.jpg")]
        subprocess.run(cmd,cwd=d,check=True)

        input_files=[]
        rows=layout[0]
        cols=layout[1]
        filter_graph=""
        idx = 0
        for row in range(rows):
            for col in range(cols):
                filter_graph += f"[{idx}:v]"
                idx+=1
            filter_graph += f"hstack=inputs={cols}[r{row}];"
        for row in range(rows):
            filter_graph += f"[r{row}]"
        filter_graph+=f'vstack=inputs={rows}[tiled_gif];[tiled_gif]scale=256:-1[raw];[raw]split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse[final]'
        print(filter_graph)
        for pos,_ in enumerate(media_ids):
            input_files.extend(['-i', f'gif_{pos:09d}.gif'])
        cmd = ["ffmpeg",
               "-y",
               *input_files,
               "-filter_complex", filter_graph,
               "-map", "[final]",
               "-shortest",
               "tiled_gif.gif"]

        subprocess.run(cmd,cwd=d,check=True)

        thumbnail_url = upload_file(os.path.join(d,'tiled_thumb.jpg'),
                                    api)
        thumbnail_gif_url = upload_file(os.path.join(d,'tiled_gif.gif'),
                                        api)

        md5=tator.util.md5sum(os.path.join(d,'tiled_gif.gif'))

        media_spec = {'attributes':attributes,
                      'name':name,
                      'thumbnail_url':thumbnail_url,
                      'md5': md5,
                      'section':section,
                      'type':type_id}
        
        resp = api.create_media(project,media_spec)

        print(f"Created {resp.id}")
        media_files={"layout": layout,
                     "ids": media_ids}
        if quality:
            media_files.update({"quality": quality})
        api.update_media(resp.id,
                         {"thumbnail_gif_url": thumbnail_gif_url,
                          "thumbnail_url": thumbnail_url,
                          "media_files": media_files})
        
        
        
                                   

            
            
                           
    

        
    
    
    
