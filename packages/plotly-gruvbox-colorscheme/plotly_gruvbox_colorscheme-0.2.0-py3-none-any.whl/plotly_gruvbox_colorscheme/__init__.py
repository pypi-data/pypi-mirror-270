import plotly.io as pio
from copy import copy

dark = {
    "bg": "#282828",
    "red": "#cc241d",
    "green": "#98971a",
    "yellow": "#d79921",
    "blue": "#458588",
    "purple": "#b16286",
    "aqua": "#689d6a",
    "gray": "#a89984",
    "gray0": "#928374",
    "red0": "#fb4934",
    "green0": "#b8bb26",
    "yellow0": "#fabd2f",
    "blue0": "#83a598",
    "purple0": "#d3869b",
    "aqua0": "#8ec07c",
    "fg": "#ebdbb2",
    "bg0_h": "#1d2021",
    "bg0": "#282828",
    "bg1": "#3c3836",
    "bg2": "#504945",
    "bg3": "#665c54",
    "bg4": "#7c6f64",
    "gray1": "#928374",
    "orange": "#d65d0e",
    "bg0_s": "#32302f",
    "fg4": "#a89984",
    "fg3": "#bdae93",
    "fg2": "#d5c4a1",
    "fg1": "#ebdbb2",
    "fg0": "#fbf1c7",
    "orange0": "#fe8019"
}

light = {
        "bg": "#fbf1c7",
        "red": "#cc241d",
        "green": "#98971a",
        "yellow": "#d79921",
        "blue": "#458588",
        "purple": "#b16286",
        "aqua": "#689d6a",
        "gray": "#7c6f64",
        "gray0": "#928374",
        "red0": "#9d0006",
        "green0": "#79740e",
        "yellow0": "#b57614",
        "blue0": "#076678",
        "purple0": "#8f3f71",
        "aqua0": "#427b58",
        "fg": "#3c3836",
        "bg0_h": "#f9f5d7",
        "bg0": "#fbf1c7",
        "bg1": "#ebdbb2",
        "bg2": "#d5c4a1",
        "bg3": "#bdae93",
        "bg4": "#a89984",
        "gray1": "#928374",
        "orange": "#d65d0e",
        "bg0_s": "#f2e5bc",
        "fg4": "#7c6f64",
        "fg3": "#665c54",
        "fg2": "#504945",
        "fg1": "#3c3836",
        "fg0": "#282828",
        "orange0": "#af3a03"
        }

palette = dark
palette = light

plotly_template = copy(pio.templates["plotly_dark"])
plotly_template.layout.colorway
def getPlotlyTemplate(palette):
    plotly_template = copy(pio.templates["plotly_dark"])
    colorscale = (
        (0.0, palette["aqua"]),
        (0.1111111111111111, palette["aqua0"]),
        (0.2222222222222222, palette["green0"]),
        (0.3333333333333333, palette["yellow0"]),
        (0.4444444444444444, palette["yellow"]),
        (0.5555555555555556, palette["orange"]),
        (0.6666666666666666, palette["red0"]),
        (0.7777777777777778, palette["red"]),
        (0.8888888888888888, palette["purple"]),
        (1.0, palette["purple0"])
    )

    plotly_template.data.bar[0].error_x.color = palette["fg0"]
    plotly_template.data.bar[0].error_y.color = palette["fg0"]
    plotly_template.data.bar[0].marker.line.color = palette["bg0_h"]
    plotly_template.data.barpolar[0].marker.line.color = palette["bg0_h"]
    plotly_template.data.carpet[0].aaxis.endlinecolor = palette["blue"]
    plotly_template.data.carpet[0].aaxis.gridcolor = palette["blue0"]
    plotly_template.data.carpet[0].aaxis.minorgridcolor = palette["blue0"]
    plotly_template.data.carpet[0].aaxis.startlinecolor = palette["blue"]
    plotly_template.data.carpet[0].baxis.endlinecolor = palette["blue"]
    plotly_template.data.carpet[0].baxis.gridcolor = palette["blue0"]
    plotly_template.data.carpet[0].baxis.minorgridcolor = palette["blue0"]
    plotly_template.data.carpet[0].baxis.startlinecolor = palette["blue"]
    plotly_template.data.contour[0].colorscale = colorscale
    plotly_template.data.heatmap[0].colorscale = colorscale
    plotly_template.data.heatmapgl[0].colorscale = colorscale
    plotly_template.data.histogram2d[0].colorscale = colorscale
    plotly_template.data.histogram2dcontour[0].colorscale = colorscale
    plotly_template.data.scatter[0].marker.line.color = palette["bg4"]
    plotly_template.data.scattergl[0].marker.line.color = palette["bg4"]
    plotly_template.data.surface[0].colorscale = colorscale
    plotly_template.data.table[0].cells.fill.color = palette["yellow0"]
    plotly_template.data.table[0].cells.line.color = palette["bg0_h"]
    plotly_template.data.table[0].header.fill.color = palette["yellow"]
    plotly_template.data.table[0].header.line.color = palette["bg0_h"]
    plotly_template.layout.annotationdefaults.arrowcolor = palette["fg0"]
    plotly_template.layout.colorscale.diverging = colorscale
    plotly_template.layout.colorscale.sequential = colorscale
    plotly_template.layout.colorscale.sequentialminus = colorscale
    plotly_template.layout.colorway = (
        palette["red"], palette["green"], palette["blue"], palette["orange"], 
        palette["purple"], palette["yellow"], palette["aqua"],
        palette["red0"], palette["green0"], palette["blue0"], palette["orange0"],
        palette["purple0"], palette["yellow0"], palette["aqua0"]
    )
    # plotly_template.layout.colorway = ('#636efa', '#EF553B', '#00cc96', '#ab63fa', '#FFA15A', '#19d3f3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52') # original colours
    plotly_template.layout.font.color = palette["fg0"]
    plotly_template.layout.geo.bgcolor = palette["bg0_h"]
    plotly_template.layout.geo.lakecolor = palette["bg0_h"]
    plotly_template.layout.geo.landcolor = palette["bg0_h"]
    plotly_template.layout.geo.subunitcolor = palette["blue0"]
    plotly_template.layout.paper_bgcolor = palette["bg0_h"]
    plotly_template.layout.plot_bgcolor = palette["bg0_h"]
    plotly_template.layout.polar.angularaxis.gridcolor = palette["blue0"]
    plotly_template.layout.polar.angularaxis.linecolor = palette["blue0"]
    plotly_template.layout.polar.bgcolor = palette["bg0_h"]
    plotly_template.layout.polar.radialaxis.gridcolor = palette["blue0"]
    plotly_template.layout.polar.radialaxis.linecolor = palette["blue0"]
    plotly_template.layout.scene.xaxis.backgroundcolor = palette["bg0_h"]
    plotly_template.layout.scene.xaxis.gridcolor = palette["blue0"]
    plotly_template.layout.scene.xaxis.linecolor = palette["blue0"]
    plotly_template.layout.scene.xaxis.zerolinecolor = palette["blue"]
    plotly_template.layout.scene.yaxis.backgroundcolor = palette["bg0_h"]
    plotly_template.layout.scene.yaxis.gridcolor = palette["blue0"]
    plotly_template.layout.scene.yaxis.linecolor = palette["blue0"]
    plotly_template.layout.scene.yaxis.zerolinecolor = palette["blue"]
    plotly_template.layout.scene.zaxis.backgroundcolor = palette["bg0_h"]
    plotly_template.layout.scene.zaxis.gridcolor = palette["blue0"]
    plotly_template.layout.scene.zaxis.linecolor = palette["blue0"]
    plotly_template.layout.scene.zaxis.zerolinecolor = palette["blue"]
    plotly_template.layout.shapedefaults.line.color = palette["fg0"]
    plotly_template.layout.sliderdefaults.bgcolor = palette["blue"]
    plotly_template.layout.sliderdefaults.bordercolor = palette["bg0_h"]
    plotly_template.layout.ternary.aaxis.gridcolor = palette["blue0"]
    plotly_template.layout.ternary.aaxis.linecolor = palette["blue0"]
    plotly_template.layout.ternary.baxis.gridcolor = palette["blue0"]
    plotly_template.layout.ternary.baxis.linecolor = palette["blue0"]
    plotly_template.layout.ternary.bgcolor = palette["bg0_h"]
    plotly_template.layout.ternary.caxis.gridcolor = palette["blue0"]
    plotly_template.layout.ternary.caxis.linecolor = palette["blue0"]
    plotly_template.layout.updatemenudefaults.bgcolor = palette["blue0"]
    plotly_template.layout.xaxis.gridcolor = palette["bg4"]
    plotly_template.layout.xaxis.linecolor = palette["blue0"]
    plotly_template.layout.xaxis.zerolinecolor = palette["bg4"]
    plotly_template.layout.yaxis.gridcolor = palette["bg4"]
    plotly_template.layout.yaxis.linecolor = palette["blue0"]
    plotly_template.layout.yaxis.zerolinecolor = palette["bg4"]
    return plotly_template


pio.templates["gruvbox_dark"] = getPlotlyTemplate(dark)
pio.templates["gruvbox_light"] = getPlotlyTemplate(light)

experimental = "gruvbox_dark"
