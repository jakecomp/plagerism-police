# plagerism-police
Parses a Google Image search frequently for changes, and notifying you so you can protect your IP

Requires an account and project at https://console.developers.google.com, and enable "Custom Search API" in the project settings. You will need your project API keys.

The default request quota limit is 100 requests/day. This can be increased, but for the purpose of this non-time sensitive project I will not push beyond this boundry, and make it scalable for theoretically a near-ininite number of images (as more images are added, frequency of checks will decrease)
