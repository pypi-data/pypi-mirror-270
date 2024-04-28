import re
from typing import Union, Tuple, List, Dict

pii_patterns = [
            {
                'regex': re.compile(
                    r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]'),
                'type': 'Email Address',
                'risk': 'Low'
            },
            {
                'regex': re.compile(
                    r'^-----BEGIN(?: (?:RSA|OPENSSH|ED25519))? PRIVATE KEY-----\s*(\S[\s\S]*?)\s*-----END(?: (?:RSA|OPENSSH|ED25519))? PRIVATE KEY-----\n$'),
                'type': 'Private SSH Key',
                'risk': 'Critical'
            },
            {
                'regex': re.compile(r'access_token,production\$[0-9a-z]{161}[0-9a,]{32}'),
                'type': 'PayPal/Braintree Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'-----BEGIN PRIVATE KEY-----[a-zA-Z0-9\n\/+]+=*-----END PRIVATE KEY-----'),
                'type': 'Private RSA Key',
                'risk': 'Critical'
            },
            {
                'regex': re.compile(r'^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'),
                'type': 'Phone Number',
                'risk': 'Mid'
            },
            {
                'regex': re.compile(r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}(\b|:(?:[0-9a-fA-F]{1,4})?\b)'),
                'type': 'IPv6 Address',
                'risk': 'Low'
            },
            {
                'regex': re.compile(r'^github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}$'),
                'type': 'GitHub Personal Access Token (Fine-Grained)',
                'risk': 'High'
            },
            {
                'regex': re.compile(
                    r'\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b'),
                'type': 'IPv4 Address',
                'risk': 'Low'
            },
            {
                'regex': re.compile(r'eyJ[A-Za-z0-9-_=]+\.eyJ[A-Za-z0-9-_=]+(\.[A-Za-z0-9-_.+/=]*)?'),
                'type': 'Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'\b(?:\d[ -\.]*?){13,16}\b'),
                'type': 'Credit Card Number',
                'risk': 'Critical'
            },
            {
                'regex': re.compile(r'\b(?:[A-Za-z0-9_]{35,})\b'),
                'type': 'API Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a,]{4}-[0-9a-f]{12}'),
                'type': 'Amazon Marketing Services Auth Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'^ghp_[a-zA-Z0-9]{36}$'),
                'type': 'GitHub Personal Access Token (Classic)',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'^gho_[a-zA-Z0-9]{36}$'),
                'type': 'GitHub OAuth 2.0 Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'^ghu_[a-zA-Z0-9]{36}$'),
                'type': 'GitHub User-to-Server Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'^ghs_[a-zA-Z0-9]{36}$'),
                'type': 'GitHub Server-to-Server Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'^ghr_[a-zA-Z0-9]{36}$'),
                'type': 'GitHub Refresh Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'(^|[^@\w])@(\w{1,15})\b'),
                'type': 'Twitter Username',
                'risk': 'Low'
            },
            {
                'regex': re.compile(r'1\/[0-9A-Za-z-]{43}|1\/[0-9A-Za-z-]{64}'),
                'type': 'Google OAuth 2.0 Refresh Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'sk_live_[0-9a-zA-Z]{24}'),
                'type': 'Stripe Standard API Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'xoxe\.xoxp-1-[0-9a-zA-Z]{166}'),
                'type': 'Slack OAuth v2 Configuration Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'EAACEdEose0cBA[0-9A-Za-z]+'),
                'type': 'Facebook Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'sk_live_[0-9a-z]{32}'),
                'type': 'Picatic API Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'sqOatp-[0-9A-Za-z-_]{22}'),
                'type': 'Square Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'q0csp-[0-9A-Za-z-_]{43}'),
                'type': 'Square OAuth Secret',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'T[a-zA-Z0-9_]{8}\/B[a-zA-Z0-9_]{8}\/[a-zA-Z0-9_]{24}'),
                'type': 'Slack Webhook',
                'risk': 'Mid'
            },
            {
                'regex': re.compile(r'[0-9a-fA-F]{7}\.[0-9a-fA-F]{32}'),
                'type': 'Instagram OAuth 2.0',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'xoxb-[0-9]{11}-[0-9]{11}-[0-9a-zA-Z]{24}'),
                'type': 'Slack OAuth v2 Bot Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'xoxp-[0-9]{11}-[0-9]{11}-[0-9a-zA-Z]{24}'),
                'type': 'Slack OAuth v2 User Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'xoxe-1-[0-9a-zA-Z]{147}'),
                'type': 'Slack OAuth v2 Refresh Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[a-zA-Z0-9\/+]{64}'),
                'type': 'Azure Storage Account Key',
                'risk': 'Critical'
            },
            {
                'regex': re.compile(r'ya29\.[0-9A-Za-z-_]+'),
                'type': 'Google OAuth 2.0 Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'key-[0-9a-zA-Z]{32}'),
                'type': 'Mailgun Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'AIza[0-9A-Za-z-_]{35}'),
                'type': 'Google API Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'4\/[0-9A-Za-z-_]+'),
                'type': 'Google OAuth 2.0 Auth Code',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[0-9a-f]{32}-us[0-9]{1,2}'),
                'type': 'MailChimp Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'),
                'type': 'Google Cloud Platform OAuth 2.0',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[A-Za-z0-9_]{21}--[A-Za-z0-9_]{8}'),
                'type': 'Google Cloud Platform API Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'),
                'type': 'Heroku API Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'),
                'type': 'Heroku OAuth 2.0',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[1-9][0-9]+-[0-9a-zA-Z]{40}'),
                'type': 'Twitter Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[A-Za-z0-9]{125}'),
                'type': 'Facebook OAuth 2.0',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[0-9a-zA-Z-_]{24}'),
                'type': 'Google OAuth 2.0 Secret Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'55[0-9a-fA-F]{32}'),
                'type': 'Twilio Access Token',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'AKIA[0-9A-Z]{16}'),
                'type': 'AWS Access ID Key',
                'risk': 'Mid'
            },
            {
                'regex': re.compile(r'R_[0-9a-f]{32}'),
                'type': 'Foursquare Secret Key',
                'risk': 'High'
            },
            {
                'regex': re.compile(r'[A-Za-z0-9]{40}'),
                'type': 'AWS Secret Access Key',
                'risk': 'Critical'
            },
            {
                'regex': re.compile(r'\b\d{5}\b'),
                'type': 'Postal Code',
                'risk': 'Low'
            }
        ]


def scrub_all(text: Union[str, Dict[str, Union[str, Dict]]]) -> Tuple[Union[str, Dict], List[Dict[str, str]]]:
    """
    Scrub all PII in text using predefined patterns and report the types of PII found and their risks.

    :param text: Input to be scrubbed of PII
    :type text: str | dict
    :return: Tuple containing the scrubbed input text and a list of detected PII types with their risks
    :rtype: Tuple[Union[str, dict], List[Dict[str, str]]]
    """
    detected_pii = []  # To store detected PII types and risks

    if isinstance(text, dict):
        # Recursively scrub content values in dict and collect PII detections
        scrubbed_text = {}
        for key, value in text.items():
            scrubbed_result, pii_detected = scrub_all(value)
            scrubbed_text[key] = scrubbed_result
            detected_pii.extend(pii_detected)
        return scrubbed_text, detected_pii
    elif not isinstance(text, str):
        raise TypeError(f"Expected str or dict, got {type(text).__name__}")

    # Apply all PII scrubbing patterns to the text
    for pattern in pii_patterns:
        matches = re.findall(pattern['regex'], text)
        if matches:
            detected_pii.append({'type': pattern['type'], 'risk': pattern['risk']})
            for match in set(matches):  # Use set to avoid duplicating replacements for the same match
                text = re.sub(re.escape(match), f"[{pattern['type']}]", text)

    return text, detected_pii
