-- Render every table as a plain (non-breaking) booktabs tabular instead of longtable.
local function cell_tex(cell)
  local doc = pandoc.Pandoc(cell)
  local s = pandoc.write(doc, "latex")
  return (s:gsub("\n+$", ""):gsub("\n", " "))
end

function Table(tbl)
  local st = pandoc.utils.to_simple_table(tbl)
  local ncol = #st.headers
  local widths = {}
  local total = 0
  for i = 1, ncol do
    local w = st.widths[i] or 0
    if w == 0 then w = 1 / ncol end
    widths[i] = w; total = total + w
  end
  local spec = "@{}"
  for i = 1, ncol do
    spec = spec .. string.format(">{\\raggedright\\arraybackslash}p{\\dimexpr %.4f\\linewidth-2\\tabcolsep\\relax}", widths[i] / total * 0.995)
  end
  spec = spec .. "@{}"
  local lines = {"\\begin{center}\\small\\begin{tabular}{" .. spec .. "}", "\\toprule"}
  local hdr = {}
  for i, h in ipairs(st.headers) do hdr[i] = "\\textbf{" .. cell_tex(h) .. "}" end
  table.insert(lines, table.concat(hdr, " & ") .. " \\\\")
  table.insert(lines, "\\midrule")
  for _, row in ipairs(st.rows) do
    local cells = {}
    for i, c in ipairs(row) do cells[i] = cell_tex(c) end
    table.insert(lines, table.concat(cells, " & ") .. " \\\\ \\addlinespace[2pt]")
  end
  table.insert(lines, "\\bottomrule")
  table.insert(lines, "\\end{tabular}\\end{center}")
  return pandoc.RawBlock("latex", table.concat(lines, "\n"))
end
