import os
from glob import glob
from os.path import basename,splitext,join
import subprocess
import shutil

def main():

    checkcwd = os.getcwd().split("/")[-1]
    if checkcwd != "myblog":
        print("please run this inside 'myblog' directory!")
        quit()

    # get the templates
    with open("./templates/default.html","r") as fi:
        default_tpl = fi.read()
    with open("./templates/post.html","r") as fi:
        post_tpl = fi.read()

    # form the full template
    post_html = default_tpl.replace("$body$",post_tpl)
    # correct relative directories
    post_html = post_html.replace('href="/','href="../')

    # remove old files
    shutil.rmtree("../posts/")
    os.makedirs("../posts/")

    #------ gen posts
    posts_org = glob("./posts/*.org")
    posts_name = []
    posts_published = []
    posts_title = []

    for orgname in posts_org:
        with open(orgname,"r") as fi:
            post_org = fi.read()
        
        sp = post_org.split("---")

        # read header information
        keylines = sp[1].split("\n")
        desc = {}
        for line in keylines:
            if ": " in line:
                key, text = line.split(": ")
                desc[key.strip()] = text.strip()

        print(desc)

        # convert org content to html 
        content = "".join(sp[2:])

        with open("./tmp.org","w") as fi:
            fi.write(content)

        subprocess.run(["pandoc","-o","tmp.html","tmp.org"],check=True)

        with open("./tmp.html","r") as fi:
            content = fi.read()
            # correct relative directories
            content = content.replace('href="/','href="../')

        # print(content)

        # replace variables
        post_final = post_html.replace("$title$",desc["title"])
        post_final = post_final.replace("$created$",desc["created"])
        post_final = post_final.replace("$published$",desc["published"])
        post_final = post_final.replace("$body$",content)


        save_postname = splitext(basename(orgname))[0] + ".html"
        with open(join("../posts/",save_postname),"w") as fi:
            fi.write(post_final)

        # save to list
        posts_name.append(save_postname)
        posts_published.append(desc["published"])
        posts_title.append(desc["title"])

    # --- make Archives.html
    archives_html = default_tpl

    # create post link list
    list_html = "\n<ul>\n"
    for pub,title,name in zip(posts_published,posts_name,posts_title):
        list_html += "<li>" + "<a href='./posts/" + name + "'>"
        pub + " - " + title + "</a></li>\n"
    list_html += "</ul>\n"


if __name__ == "__main__":
    main()
