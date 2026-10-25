-- Pandoc filter: render footnotes as sidenotes.
-- Each note becomes a numbered marker plus a <span class="sidenote"> placed
-- right after it; CSS floats the span into the right margin on wide screens
-- and shows it inline below the text on narrow ones.

function Note(note)
  local html = pandoc.write(pandoc.Pandoc(note.content), "html")
  -- sidenotes must stay inline: flatten paragraphs into line breaks
  html = html:gsub("^%s*<p>", ""):gsub("</p>%s*$", "")
  html = html:gsub("</p>%s*<p>", "<br>")
  return pandoc.RawInline(
    "html",
    '<span class="sn-ref" aria-hidden="true"></span>'
      .. '<span class="sidenote" role="note">' .. html .. "</span>"
  )
end
