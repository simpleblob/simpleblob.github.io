import os
from glob import glob
from os.path import basename,splitext,join

def main():

    # get the templates
    with open("./templates/default.html","r") as fi:
        default_html = fi.read()
    with open("./templates/post.html","r") as fi:
        post_html = fi.read()

    # gen posts
    posts_org = glob("./posts/*.org")

    for orgname in posts_org:
        with open(orgname,"r") as fi:
            post_org = fi.read()
        
        # read header information
        keylines = post_org.split("---")[1].split("\n")
        desc = {}
        for line in keylines:
            if ": " in line:
                key, content = line.split(": ")
                desc[key.strip()] = content.strip()

        print(desc)
        quit()
        


if __name__ == "__main__":
    main()
