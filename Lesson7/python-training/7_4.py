import os


SRC_FOLDER = 'my_project'
DST_FOLDER = 'templates'


for root, _, _ in os.walk (SRC_FOLDER):
    os.makedirs(os.path.jion(DST_FOLDER, os.path.repath(root, SRC_FOLDER)), exist_ok=True)