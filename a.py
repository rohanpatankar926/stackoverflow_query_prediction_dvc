from xml.etree import ElementTree as ET
import re
import random

def process_posts(f_in, target_tag, f_out_train, f_out_test, split):
    try:
        root = ET.fromstring(f_in)
        for child in root:
            pid = child.get('Id', "")
            label = 1 if target_tag in child.get('Tags', "") else 0
            title = re.sub(r"\s+", " ", child.get('Title', "")).strip()
            body = re.sub(r"\s+", " ", child.get('Body', "")).strip()
            text = title + " " + body
            f_out = f_out_train if random.random() > split else f_out_test
            f_out.write(f"{pid}\t{label}\t{text}\n")
    except Exception as e:
        msg = f"{e}\n"
        raise Exception(msg)    
