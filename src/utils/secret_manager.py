
import os

class SecretManager:
    def __init__(self):
        #these would be loaded from key vault in production
        self.corpus_id = 5
        self.vectara_client_id = '1s2b6jrp71t9srf1e9ibe1fiph'
        self.vectara_api_key = '1bvgbikdadl1rgfacg9o0ntvobk80v86duv339i3arjirp9sfken'

        self.customer_id = '1464859115'
        self.oauth_url = "https://vectara-prod-1464859115.auth.us-west-2.amazoncognito.com"
        self.openai_api_key = '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'
        self.vectara2_api_key = 'zwt_V0_565r6ynhNoRqSaIVCnfD1EIzpf67bGWA5fA'