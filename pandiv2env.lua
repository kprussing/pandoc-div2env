function Div(elem)
    if FORMAT ~= 'latex' then return end
    local attr = elem.attributes["data-environment"]
    if attr then
        -- Find the first ','
        local _, loc = string.find(attr, ',')
        -- If we have no arguments, the full string is the environment
        if not loc then loc = string.len(attr) + 1 end
        --print(attr, loc)

        -- Now split into the environment and arguments
        local env = string.sub(attr, 1, loc-1)
        local args = string.sub(attr, loc+1, string.len(attr)+1)

        -- If we have arguments, put them inside '[...]'
        if args ~= ""  then args = "[" .. args .. "]" end
        --print("env = '" .. env .. "'", "args = '" .. args .. "'")

        -- Now create the barriers.  We include the '%' to strip the
        -- intervening spaces
        local begin = pandoc.RawBlock(
                FORMAT, "\\begin{" .. env .. "}" .. args .. "%"
            )
        --for k,v in pairs(elem.content) do print(k,v) end
        local last = pandoc.RawInline(FORMAT, "\\end{" .. env .. "}")
        elem.content:extend({last})
        --local div = pandoc.Div(elem.content:extend({last}))
        return elem -- { begin, elem, last }
    end
end

