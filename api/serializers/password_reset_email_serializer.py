from rest_framework import serializers

from api.third_parties.email_helper.email_util import EmailUtil


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        try:
            EmailUtil.send_forget_password_email(attrs)
            return attrs
        except Exception:
            raise serializers.ValidationError("Data not verified.")
