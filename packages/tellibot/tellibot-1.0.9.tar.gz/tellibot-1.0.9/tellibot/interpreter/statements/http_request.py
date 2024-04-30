import requests

def http_request(self, statement):
    self.debug_print("http_request")
    try:
        pointer = statement.get("pointer")
        url = self.execute_statement(pointer.get("url"))
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        method = pointer.get("method")
        headers = self.execute_statement(pointer.get("headers")) or {}
        body_type = pointer.get("bodyType")
        body = self.execute_statement(pointer.get("body")) or {}
        cookies = self.execute_statement(pointer.get("cookies")) or {}

        if method == "GET":
            response = requests.get(url, headers=headers, cookies=cookies)
        elif method == "POST":
            if body_type == "json":
                response = requests.post(url, json=body, headers=headers, cookies=cookies)
            else:
                response = requests.post(url, data=body, headers=headers, cookies=cookies)
        else:
            raise ValueError("Invalid request method")

        return {
            "statusCode": response.status_code,
            "text": response.text,
            "headers": dict(response.headers),
            "isRedirect": response.is_redirect,
            "isSuccessful": response.ok,
            "statusMessage": response.reason,
        }
    except Exception as e:
        self.show_error(statement, e)
    return None
