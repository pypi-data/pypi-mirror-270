import requests
import json
import time

u = "https://www.spiegel.de/schlagzeilen/tops/index.rss"

x = requests.get(u)

def replace_special_chars(src):
    mapping = {}
    mapping['ä'] = "ae";
    mapping['ü'] = "ue";
    mapping['ö'] = "oe";
    mapping['Ä'] = "Ae";
    mapping['Ü'] = "Ue";
    mapping['Ö'] = "Oe";
    mapping['ß'] = "ss";
    n=src

    for k in mapping.keys():
        n = n.replace(k, mapping[k])
    
    return n

def drop_special_chars(src):
    n=""
    alp = "0123456789,.-:/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for c in src:
        if c in alp:
            n+=c
    
    return n


def extract_firsttag_inner(src, tag_name):
    o_tag = "<%s>" % tag_name
    c_tag = "</%s>" % tag_name
    pos1 = src.find(o_tag)
    pos2 = src.find(c_tag)
    body = src[pos1+len(o_tag):pos2]
    return body

def spiegel_main(src):
    with open("spiegel.txt", "w") as f:
        f.write(src)


    title_cols = src.split("<item>")[1:]

    articles = []
    for t in title_cols:
        z_title = extract_firsttag_inner(t, "title")
        z_title = replace_special_chars(z_title)
        z_title = drop_special_chars(z_title)
        z_title = z_title.strip()
        z_link = extract_firsttag_inner(t, "link")
        z_link = z_link.strip()

        z = {"title": z_title, "link": z_link.split("#")[0], "epoch_timestamp": int(time.time())}
        articles.append(z)

    with open("spiegel.js", "w") as f:
        f.write(json.dumps(articles, indent=4))


spiegel_main(x.text)
