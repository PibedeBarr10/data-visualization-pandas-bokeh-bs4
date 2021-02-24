import colorcet as cc
from bokeh.models import ColumnDataSource, Legend, LegendItem, HoverTool
from bokeh.plotting import figure, output_file, show, save
from bokeh.transform import linear_cmap
from math import pi

def plot(df):
    source = ColumnDataSource(df)

    # Setting up colors by mapper (linear_cmap function)
    palette = [cc.rainbow[i*15] for i in range(17)]
    mini, maxi = min(df['xG_diff']), max(df['xG_diff'])

    if abs(min(df['xG_diff'])) > abs(max(df['xG_diff'])):
        mini, maxi = min(df['xG_diff']), -min(df['xG_diff'])
    else:
        mini, maxi = -max(df['xG_diff']), max(df['xG_diff'])

    mapper = linear_cmap(field_name = 'xG_diff', palette = palette, low = mini, high = maxi)

    # Tooltips
    tooltips = [
        ("Name", "@player_name"),
        ("Games", "@games"),
        ("Goals", "@goals"),
        ("xG", "@xG"),
        ("(xG - goals)", "@xG_diff")
    ]

    # Draw plot
    p = figure(title = "Premier League - difference between xG and goals (last 5 games or 30 days ago)", x_range = df['player_name'], height = 800, width = 1600)    # x_range !!! do source?

    # Title style
    p.title.text_color = "#dddddd"
    p.title.text_font = "Consolas"
    p.title.text_font_size = '24px'
    p.title.align = 'center'

    # Displaying data on plot
    r1 = p.circle("player_name", "xG", size = 10, color = mapper, source = source)  # xG (circles)
    r2 = p.square('player_name', 'goals', size = 10, fill_color = mapper, line_color = None, source = source)  # goals (rectangle)
    r3 = p.segment('player_name', 'xG', 'player_name', 'goals', color = mapper, source = source)    # xG - goals (lines)

    # Styling plot
    p.yaxis.axis_label = 'Goals and xG'
    p.yaxis.axis_label_text_color = '#dddddd'   # color of y label text
    p.yaxis.axis_label_text_font = 'Consolas'
    p.xaxis.major_label_orientation = pi/4

    p.axis.major_label_text_color = '#dddddd'   # color of axis's values
    p.axis.major_label_text_font = 'Consolas'
    p.axis.axis_line_color = '#dddddd'

    p.border_fill_color = "#1b1b1b"
    p.background_fill_color = "#1b1b1b"

    p.grid.grid_line_color = "#242424"

    p.min_border_top = 40
    p.min_border_left = 60

    # Legend
    legend = Legend(items =[
        LegendItem(label = 'xG', renderers = [r1]),
        LegendItem(label = 'goals', renderers = [r2]),
        LegendItem(label = '(xG - goals)', renderers = [r3])
    ], 
    background_fill_color = "#1b1b1b",
    label_text_color = '#dddddd',
    label_text_font = 'Consolas')

    p.add_layout(legend, 'right')
    p.legend.click_policy = "hide"

    # HoverTool
    on_hover = HoverTool(renderers = [r1, r2], tooltips = tooltips)
    p.add_tools(on_hover)

    # Show plot on screen and save it to file
    show(p)
    output_file("PL.html", title="Premier League - difference between goals and xG")
    save(p)