import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0'}],
    external_stylesheets=[{
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "rel": "stylesheet",
        "integrity": "sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==",
        "crossorigin": "anonymous",
        "referrerpolicy": "no-referrer",
    }],
    )