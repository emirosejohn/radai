from index import attach_params 

def test_attach_params():
    print("here")
    assert attach_params(params) is None
    parsed_url = urlparse(url)
    print("     ",parsed_url.params)