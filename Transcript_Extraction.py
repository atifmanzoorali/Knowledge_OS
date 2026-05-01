import os
import re
import sys
from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi

links_file = "Starter-Story-Links.xlsx"

def sanitize_filename(title, max_length=50):
    if not title:
        return ""
    invalid_chars = r'[\\/*?:"<>|]'
    sanitized = re.sub(invalid_chars, '', title)
    sanitized = sanitized.replace(' ', '_')
    return sanitized[:max_length].rstrip('_')

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "be/" in url:
        return url.split("be/")[1].split("?")[0]
    return None

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi().list(video_id)
        try:
            transcript = transcript_list.find_manually_created_transcript(['en'])
        except:
            transcript = transcript_list.find_generated_transcript(['en'])
        data = transcript.fetch()
        return " ".join([item.text for item in data])
    except Exception as e:
        print(f"    Transcript error: {e}")
        return ""

url = sys.argv[1] if len(sys.argv) > 1 else None
output_dir = sys.argv[2] if len(sys.argv) > 2 else "Raw_Data"

if not url:
    print("Usage: python Transcript_Extraction.py <youtube_url> <output_folder>")
    sys.exit(1)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video_id = get_video_id(url)
if not video_id:
    print(f"Invalid URL: {url}")
    sys.exit(1)

print(f"Processing: {video_id}")

try:
    ydl_opts = {
        'skip_download': True,
        'quiet': True,
        'no_warnings': True
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        
        metadata = {
            'video_id': video_id,
            'title': info.get('title'),
            'channel': info.get('channel'),
            'duration': info.get('duration'),
            'view_count': info.get('view_count'),
            'upload_date': info.get('upload_date'),
            'tags': info.get('tags', []),
            'thumbnail': info.get('thumbnail'),
        }
    
    transcript_text = get_transcript(video_id)
    
    sanitized_title = sanitize_filename(metadata.get('title', ''))
    if sanitized_title:
        filename = f'{video_id}_{sanitized_title}.md'
    else:
        filename = f'{video_id}.md'
    
    output_path = os.path.join(output_dir, filename)
    
    tags_str = ', '.join([f'"{tag}"' for tag in metadata.get('tags', [])])
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"---\n")
        f.write(f"video_id: {metadata['video_id']}\n")
        f.write(f"title: \"{metadata['title']}\"\n")
        f.write(f"channel: \"{metadata['channel']}\"\n")
        f.write(f"duration: {metadata['duration']}\n")
        f.write(f"view_count: {metadata['view_count']}\n")
        f.write(f"upload_date: {metadata['upload_date']}\n")
        f.write(f"tags: [{tags_str}]\n")
        f.write(f"thumbnail: {metadata['thumbnail']}\n")
        f.write(f"---\n\n")
        f.write(transcript_text)
    
    print(f"Saved: {filename}")
    
except Exception as e:
    print(f"Failed: {str(e)}")
    sys.exit(1)