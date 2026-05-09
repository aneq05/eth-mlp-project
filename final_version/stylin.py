from IPython.display import display, HTML



class InfoDisplayStyler:
    def __init__(self):
        self.base_style = [
            {"selector": "table", "props": [("background-color", "#000000"), ("border-collapse", "collapse")]},
            {"selector": "th", "props": [("background-color", "#000000"), ("color", "#f472b6"), ("font-weight", "bold"), ("border", "1px solid #1f2937")]},
            {"selector": "td", "props": [("background-color", "#000000"), ("color", "#ffffff"), ("border", "1px solid #1f2937")]},
            {"selector": "tbody tr:hover td", "props": [("background-color", "#111111")]},
        ]
    
    def show_meta(self, data):
        display(HTML(f"""
        <div style="
            background:#000000; color:#f9a8d4; padding:12px 16px; border-radius:10px;
            border-left:6px solid #ec4899; margin:8px 0 14px 0; font-family:Arial;">
            <b>Shape:</b> {data.shape} &nbsp;&nbsp; &nbsp;&nbsp;
            <b>Size:</b> {data.size} &nbsp;&nbsp; &nbsp;&nbsp;
            <b>Columns:</b> {len(data.columns)}
        </div>
        """))

    def style_me(self, df_part, title=None):
        if title:
            display(HTML(f"<h3 style='color:#f472b6'>{title}</h3>"))
        display(df_part.style.set_table_styles(self.base_style))
        
    def show_line(self, *args, sep=" ", title=None):
        text = sep.join(str(a) for a in args).strip()
        content = f"<b>{title}:</b> {text}" if title else text

        display(HTML(f"""
        <div style="
            background:#000000; color:#f9a8d4; padding:12px 16px; border-radius:10px;
            border-left:6px solid #ec4899; margin:8px 0 14px 0; font-family:Arial;">
            {content}
        </div>
        """))

    
