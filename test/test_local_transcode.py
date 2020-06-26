import tator
import subprocess

def test_local_transcode(host, token, project, video_type, video_file):
    cmd = [
        'python3', '-m', 'tator.transcode', video_file,
        '--tus_url', f'{host}/files/',
        '--url', f'{host}/rest',
        '--token', token,
        '--project', str(project),
        '--type', str(video_type),
        '--section', 'Locally transcoded',
    ]
    subprocess.run(cmd, check=True)
