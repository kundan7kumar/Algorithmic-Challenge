#!/usr/bin/env python
# coding: utf-8
import json
import base64

data = {}
with open('1.jpeg', mode='rb') as file:
    img = file.read()

data['img'] = base64.b64encode(img)
print(json.dumps(data))
