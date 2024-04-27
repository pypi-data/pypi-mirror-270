from .. import IconBase


class IconSnowflake(IconBase):
    class_name = "lucide lucide-snowflake"
    svg_data = {
    "attrs": {
        "width": "24",
        "height": "24",
        "view_box": "0 0 24 24",
        "fill": "none",
        "stroke": "currentColor",
        "stroke_width": "2",
        "stroke_linecap": "round",
        "stroke_linejoin": "round"
    },
    "items": [
        {
            "line": {
                "x1": "2",
                "x2": "22",
                "y1": "12",
                "y2": "12"
            }
        },
        {
            "line": {
                "x1": "12",
                "x2": "12",
                "y1": "2",
                "y2": "22"
            }
        },
        {
            "path": {
                "d": "m20 16-4-4 4-4"
            }
        },
        {
            "path": {
                "d": "m4 8 4 4-4 4"
            }
        },
        {
            "path": {
                "d": "m16 4-4 4-4-4"
            }
        },
        {
            "path": {
                "d": "m8 20 4-4 4 4"
            }
        }
    ]
}
