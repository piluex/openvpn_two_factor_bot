source ./config
TOTP="$(./totp.py $TOTP_KEY)"
sudo ./expect-answers $USER $PASSWORD $TOTP

