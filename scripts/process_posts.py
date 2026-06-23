import json, re, os, shutil
from datetime import datetime

with open("/home/madhav22m/gitrepos/tkafka/hallelucinating/posts.json") as f:
    posts = json.load(f)

IMG_SRC = "/home/madhav22m/gitrepos/tkafka/hallelucinating/images"
IMG_DST = "/home/madhav22m/gitrepos/tkafka/public/images/instagram"
CONTENT_DST = "/home/madhav22m/gitrepos/tkafka/src/content/music"

os.makedirs(IMG_DST, exist_ok=True)
os.makedirs(CONTENT_DST, exist_ok=True)

def clean_caption(text):
    text = re.sub(r'\(@\w+\)', '', text)
    text = re.sub(r"@\w+(?:'\w+)?", '', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r',\s*\)', ')', text)
    text = re.sub(r'\(\s*\)', '', text)
    text = re.sub(r'\(Link to tracks in bio!?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(link in bio!?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(Link to playlist in the bio(?: in the description)?!?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(Link to the music in a playlist in the bio\.?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(Link to playlist in the bio in the description!?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(contd\.?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(Link to tracks in bio!?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(again, link to the playlist in the bio!?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(again, link to playlist in the bio in the description!?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(By @\w+\)', '', text)
    text = re.sub(r'Written by @\w+,?', '', text)
    text = re.sub(r'Written \(and illustrated\) by @\w+,?', '', text)
    text = re.sub(r'\(The tracks called[^)]*\)', '', text, flags=re.IGNORECASE)
    lines = text.split('\n')
    lines = [l.strip() for l in lines]
    lines = [re.sub(r'#\S+', '', l).strip() for l in lines]
    text = '\n\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_title(caption):
    first_line = caption.split('\n')[0].strip()
    title = re.sub(r'\(@\w+\)', '', first_line)
    title = re.sub(r"@\w+(?:'\w+)?", '', title)
    title = re.sub(r'#\S+', '', title)
    title = re.sub(r'^Pictured (?:are|is).*?\.\s*', '', title)
    title = re.sub(r'^Video courtesy.*?\.\s*', '', title)
    title = re.sub(r"^'", '', title)
    title = re.sub(r'\(link in bio!?\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\(The tracks called[^)]*\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r' +', ' ', title)
    title = title.strip().rstrip(".,:;")
    if not title or len(title) < 5:
        title = first_line.strip().rstrip(".,:;")[:60]
    if not title or len(title) < 5:
        title = f"Post {code}"
    if len(title) > 80:
        title = title[:77] + "..."
    return title

def make_slug(code, title, seen):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    slug = slug[:50].rstrip('-')
    if len(slug) < 5:
        slug = code.lower()
    suffix = 1
    base = slug
    while slug in seen:
        slug = f"{base}-{suffix}"
        suffix += 1
    seen.add(slug)
    return slug

seen_slugs = set()

for i, post in enumerate(posts):
    code = post["code"]
    caption = post["caption"]
    taken_at = post["taken_at"]
    date_str = datetime.utcfromtimestamp(taken_at).strftime("%Y-%m-%d")

    cleaned = clean_caption(caption)
    title = extract_title(caption)

    slug = make_slug(code, title, seen_slugs)

    img_filename = f"{code}.jpg"
    src_img = os.path.join(IMG_SRC, img_filename)
    dst_img = os.path.join(IMG_DST, img_filename)
    if os.path.exists(src_img):
        shutil.copy2(src_img, dst_img)

    tags = []
    if 'Album Appreciation' in caption:
        tags.append('album-appreciation')
    if 'Album Changed My Life' in caption or 'This Album Changed My Life' in caption:
        tags.append('album-changed-my-life')
    if 'review' in caption.lower() or 'Fiction review' in caption:
        tags.append('review')
    if '#' in post.get('caption', ''):
        raw_tags = re.findall(r'#(\w+)', caption)
        known = ['indie', 'folk', 'rock', 'alternative', 'psychedelic', 'ambient',
                 'radiohead', 'shoegaze', 'dreampop', 'acoustic', 'hiphop',
                 'electronica', 'experimental', 'prog', 'jazz', 'classical']
        tags.extend([t for t in raw_tags if t.lower() in known])
    tags = list(dict.fromkeys(tags))

    md = f"""---
title: "{title}"
date: {date_str}
description: ""
tags: {json.dumps(tags) if tags else '[]'}
---

<img src="/images/instagram/{img_filename}" alt="" style="max-width:100%;height:auto;margin-bottom:1.5rem" />

{cleaned}
"""
    filepath = os.path.join(CONTENT_DST, f"{slug}.md")
    with open(filepath, "w") as f:
        f.write(md)
    print(f"  [{i+1}/{len(posts)}] {slug}.md — {title[:50]}")

print(f"\nDone! {len(posts)} posts written to {CONTENT_DST}")
