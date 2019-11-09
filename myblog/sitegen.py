import os
from glob import glob
from os.path import basename, splitext, join
import subprocess
import shutil


def generate_posts_html(default_tpl, post_tpl):
    # ------ gen posts
    # form the full template
    post_html = default_tpl.replace("$body$", post_tpl)
    # correct relative directories
    post_html = post_html.replace('href="/', 'href="../')
    posts_org = glob("./posts/*.org")
    posts_name = []
    posts_published = []
    posts_title = []

    for orgname in posts_org:
        print(orgname)
        with open(orgname, "r") as fi:
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

        with open("./tmp.org", "w") as fi:
            fi.write(content)

        subprocess.run(["pandoc", "-o", "tmp.html", "tmp.org"], check=True)

        with open("./tmp.html", "r") as fi:
            content = fi.read()
            # correct relative directories
            content = content.replace('href="/', 'href="../')

        # print(content)

        # replace variables
        post_final = post_html.replace("$title$", desc["title"])
        post_final = post_final.replace("$created$", desc["created"])
        post_final = post_final.replace("$published$", desc["published"])
        post_final = post_final.replace("$body$", content)

        save_postname = splitext(basename(orgname))[0] + ".html"
        with open(join("../posts/", save_postname), "w") as fi:
            fi.write(post_final)

        # save to list
        posts_name.append(save_postname)
        posts_published.append(desc["published"])
        posts_title.append(desc["title"])

    # remove tmp stuff
    os.remove("./tmp.org")
    os.remove("./tmp.html")

    return posts_name, posts_published, posts_title


def generate_archive_html(
    default_tpl, archive_tpl, posts_name, posts_published, posts_title
):
    print("generate archive.html ...")
    # --- make Archives.html

    # new sort by date desc
    new_index = sorted(
        range(len(posts_published)), key=lambda k: posts_published[k], reverse=True
    )

    posts_published = [posts_published[i] for i in new_index]
    posts_name = [posts_name[i] for i in new_index]
    posts_title = [posts_title[i] for i in new_index]

    # create post link list
    list_html = "\n<ul>\n"
    for pub, name, title in zip(posts_published, posts_name, posts_title):
        list_html += (
            "<li>\n"
            + pub
            + " - <a href='./posts/"
            + name
            + "'>"
            + title
            + "</a></li>\n"
        )
    list_html += "</ul>\n"

    archive_final = default_tpl.replace("$body$", archive_tpl)
    archive_final = archive_final.replace('href="/', 'href="./')
    archive_final = archive_final.replace("$title$", "Archives")
    archive_final = archive_final.replace("$post-list$", list_html)

    save_name = "../archive.html"
    with open(save_name, "w") as fi:
        fi.write(archive_final)

    print("done")


def main():

    checkcwd = os.getcwd().split("/")[-1]
    if checkcwd != "myblog":
        print("please run this inside 'myblog' directory!")
        quit()

    # get the templates
    with open("./templates/default.html", "r") as fi:
        default_tpl = fi.read()
    with open("./templates/post.html", "r") as fi:
        post_tpl = fi.read()
    with open("./templates/archive.html", "r") as fi:
        archive_tpl = fi.read()

    # remove old files
    shutil.rmtree("../posts/")
    os.makedirs("../posts/")

    posts_name, posts_published, posts_title = generate_posts_html(
        default_tpl, post_tpl
    )
    generate_archive_html(
        default_tpl, archive_tpl, posts_name, posts_published, posts_title
    )


if __name__ == "__main__":
    main()
