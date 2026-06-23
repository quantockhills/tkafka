import os, re, json, shutil
from datetime import datetime

CONTENT_DIR = "/home/madhav22m/gitrepos/tkafka/src/content/music"
IMG_SRC = "/home/madhav22m/gitrepos/tkafka/hallelucinating/images"
IMG_DST = "/home/madhav22m/gitrepos/tkafka/public/images/instagram"

os.makedirs(CONTENT_DIR, exist_ok=True)
os.makedirs(IMG_DST, exist_ok=True)

with open("/home/madhav22m/gitrepos/tkafka/hallelucinating/posts.json") as f:
    posts = json.load(f)

titles = {
    "CpZrfret-Hn": {
        "title": "The Slaughter of False Selves",
        "desc": "On Leonard Cohen\u2019s writing process"
    },
    "CjdDnr0tU4w": {
        "title": "Conversations with the Beat Generation",
        "desc": "On Patti Smith\u2019s \u2018M Train\u2019"
    },
    "Ccyo5ago0dL": {
        "title": "A Fever Dream in Prose",
        "desc": "Georges Bataille and the depravity of the everyday"
    },
    "Brs_D_BHhti": {
        "title": "Half Shadows and the Language of Crows",
        "desc": "On Haruki Murakami\u2019s \u2018Kafka on the Shore\u2019"
    },
    "Brs9sPbHzc9": {
        "title": "The Quiet Devastation",
        "desc": "On Kazuo Ishiguro\u2019s \u2018Never Let Me Go\u2019"
    },
    "BjC-lkXj3Lz": {
        "title": "Cathedrals of Melancholy",
        "desc": "Anupama Nair on The Cure\u2019s \u2018Disintegration\u2019"
    },
    "BiGfgIDDWUL": {
        "title": "The Unbearable Tenderness of Youth",
        "desc": "On Arcade Fire\u2019s \u2018Funeral\u2019"
    },
    "BhMX9SKBGn0": {
        "title": "Kaleidoscopic Revelations",
        "desc": "Jai on Radiohead\u2019s \u2018In Rainbows\u2019"
    },
    "Bg8ah_yhrfa": {
        "title": "The Space Between People",
        "desc": "Shivangi on Steven Wilson\u2019s \u2018Hand. Cannot. Erase.\u2019"
    },
    "BgeLQQPDFoK": {
        "title": "A House of Many Rooms",
        "desc": "On Sufjan Stevens\u2019 \u2018Michigan\u2019"
    },
    "BgWY6ASDYk8": {
        "title": "Where the Light Goes Quiet",
        "desc": "On Grouper\u2019s \u2018Dragging a Dead Deer Up a Hill\u2019"
    },
    "BgQb4aEj9u8": {
        "title": "Sunday Morning Music for the Soul",
        "desc": "Anupama Nair on AIR\u2019s \u2018Moon Safari\u2019"
    },
    "BgIubTfjCr4": {
        "title": "Introducing \u2018This Album Changed My Life\u2019",
        "desc": "A call for writing on music that shapes us"
    },
    "BgGET3tjaZi": {
        "title": "The Stream of Conscious World",
        "desc": "Deerhunter\u2019s Bradford Cox on making music without a map"
    },
    "BgF4pw9jgyr": {
        "title": "Finding Solace in the Suburbs",
        "desc": "On Deerhunter and the art of isolation"
    },
    "BgETuZnjqoT": {
        "title": "A Brief and Brilliant Arc",
        "desc": "On Tim Buckley\u2019s \u2018Song to the Siren\u2019"
    },
    "BgER90wDr92": {
        "title": "The Quiet Radicalism",
        "desc": "On Radiohead\u2019s \u2018No Surprises\u2019"
    },
    "BgERAS4jgc4": {
        "title": "Seven Visions of \u2018DAMN.\u2019",
        "desc": "Fan-made artwork for Kendrick Lamar"
    },
    "BgDSanKD5E6": {
        "title": "A Morning with Grouper",
        "desc": "On \u2018Holding\u2019 and the comfort of ambience"
    },
    "BgDM6qnDtE5": {
        "title": "The Grace of Letting Go",
        "desc": "On Sufjan Stevens\u2019 \u2018Carrie and Lowell\u2019"
    },
    "BgDIOf4D5i3": {
        "title": "The Voice That Wasn\u2019t There",
        "desc": "My Bloody Valentine\u2019s Bilinda Butcher"
    },
    "BgDG3SKjCfc": {
        "title": "The Impossible Album",
        "desc": "On My Bloody Valentine\u2019s \u2018Loveless\u2019"
    }
}

seen_slugs = set()

for post in posts:
    code = post["code"]
    info = titles[code]
    title = info["title"]
    desc = info["desc"]
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s'-]", '', slug)
    slug = re.sub(r"[']", '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    slug = slug[:50].rstrip('-')

    suffix = 1
    base = slug
    while slug in seen_slugs:
        slug = f"{base}-{suffix}"
        suffix += 1
    seen_slugs.add(slug)

    taken_at = post["taken_at"]
    date_str = datetime.fromtimestamp(taken_at).strftime("%Y-%m-%d")
    caption = post["caption"]

    tags = []
    if 'Album Appreciation' in caption:
        tags.append('album-appreciation')
    if 'Album Changed My Life' in caption or 'This Album Changed My Life' in caption:
        tags.append('album-changed-my-life')
    if 'review' in caption.lower() or 'Fiction review' in caption:
        tags.append('review')
    if '#' in caption:
        raw_tags = re.findall(r'#(\w+)', caption)
        known = ['indie', 'folk', 'rock', 'alternative', 'psychedelic', 'ambient',
                 'radiohead', 'shoegaze', 'dreampop', 'acoustic', 'hiphop',
                 'electronica', 'experimental', 'prog', 'jazz', 'classical']
        tags.extend([t for t in raw_tags if t.lower() in known])
    tags = list(dict.fromkeys(tags))
    if 'review' in tags:
        tags.remove('review')
        tags.insert(0, 'review')

    img_filename = f"{code}.jpg"
    src_img = os.path.join(IMG_SRC, img_filename)
    dst_img = os.path.join(IMG_DST, img_filename)
    if os.path.exists(src_img):
        shutil.copy2(src_img, dst_img)

    cleaned = caption
    cleaned = re.sub(r'\(@\w+\)', '', cleaned)
    cleaned = re.sub(r"@\w+(?:'\w+)?", '', cleaned)
    cleaned = re.sub(r' +', ' ', cleaned)
    cleaned = re.sub(r',\s*\)', ')', cleaned)
    cleaned = re.sub(r'\(\s*\)', '', cleaned)
    cleaned = re.sub(r'\(Link to tracks in bio!?\)', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\(link in bio!?\)', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\(Link to playlist[^)]*\)', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\(Link to the music[^)]*\)', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\(contd\.?\)', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\(By @\w+\)', '', cleaned)
    cleaned = re.sub(r'Written by @\w+,?\s*', '', cleaned)
    cleaned = re.sub(r'Written \(and illustrated\) by @\w+,?\s*', '', cleaned)
    cleaned = re.sub(r'\(The tracks called[^)]*\)', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\(again, link[^)]*\)', '', cleaned, flags=re.IGNORECASE)
    lines = cleaned.split('\n')
    lines = [re.sub(r'#\S+', '', l).strip() for l in lines]
    lines = [l for l in lines if l.strip()]
    cleaned = '\n\n'.join(lines)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

    md = f"""---
title: "{title}"
date: {date_str}
description: "{desc}"
tags: {json.dumps(tags) if tags else '[]'}
---

<img src="/images/instagram/{img_filename}" alt="" style="max-width:100%;height:auto;margin-bottom:1.5rem" />

{cleaned}
"""
    filepath = os.path.join(CONTENT_DIR, f"{slug}.md")
    with open(filepath, "w") as f:
        f.write(md)
    print(f"  {slug}.md")

print(f"\nDone! {len(posts)} posts written.")
