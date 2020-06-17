# simpleblob.github.io
My personal website

## Redirects
- `simpleblob.com`
- `rarelyrandom.com`
- `simpleblob.github.io`

## setup
- all the posts are written in emac org file, inside `myblog/posts/`. This place is also where I take all the notes and do a brain-dump.
- originally, hakyll was used to convert these org files into a static site. now I am changing that to custom python script because of familiarity. not done yet.

### how to use (draft)
- requires
  - python 3
  - pandoc
  - (optional) emacs for writing org file
- writing
  - posts as .org file in `myblog/post/`
- how to convert to html
  - open terminal
  - `cd myblog`
  - `python3 sitegen.py`
- how to check if the files has changed properly
  - go to root repo directory
  - `python3 -m http.server 8000`
  - in any web browser, go to `http://localhost:8000`
