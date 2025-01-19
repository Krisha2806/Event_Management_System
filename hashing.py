import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
hashed_passwords = stauth.Hasher(['abc']).generate()

print(hashed_passwords)